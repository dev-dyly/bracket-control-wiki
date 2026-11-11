"""Check source/navigation, Jekyll output and (optionally) published Pages output.

Run from the repository root: python _internal/check_docs.py [--live]
Requires PyYAML and requests. Jekyll output must exist at _internal/site.
"""
import argparse
import hashlib
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

import requests
import yaml

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_internal/site'
ORIGIN = 'https://docs.devdylnz.com'
BASELINE = 'f0720bea5c470814ff827389f3829d652db21eba'


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.pagers, self.headings = set(), [], {}, []
        self.redirect = False
        self.feed(html)

    def handle_starttag(self, tag, attributes):
        a = dict(attributes)
        if 'id' in a:
            assert a['id'] not in self.ids, f'Duplicate id: {a["id"]}'
            self.ids.add(a['id'])
        if tag == 'a' and 'href' in a:
            self.links.append(a['href'])
            if a.get('rel') in ('prev', 'next'):
                assert a['rel'] not in self.pagers, 'Duplicate pager'
                self.pagers[a['rel']] = a['href']
        if tag in ('link', 'script', 'img'):
            if a.get('href') or a.get('src'):
                self.links.append(a.get('href') or a.get('src'))
        if tag == 'meta' and a.get('http-equiv', '').lower() == 'refresh':
            self.redirect = True


def site_path(url):
    path = unquote(urlsplit(url).path)
    return SITE / (path.lstrip('/') + ('index.html' if path.endswith('/') else ''))


def sha(content):
    return hashlib.sha256(content).hexdigest()


def main():
    options = argparse.ArgumentParser()
    options.add_argument('--live', action='store_true')
    args = options.parse_args()
    navigation = yaml.safe_load((ROOT / '_data/navigation.yml').read_text(encoding='utf-8-sig'))
    chapters = [c for c in navigation if not c.get('pdf')]
    urls = [c['url'] for c in chapters]
    assert len(urls) == len(set(urls)), 'Duplicate navigation URL'
    pages = {}
    for file in ROOT.rglob('*.md'):
        if any(p.startswith('.') or p == '_internal' for p in file.relative_to(ROOT).parts):
            continue
        text = file.read_text(encoding='utf-8-sig')
        if not text.startswith('---\n'):
            continue
        front = yaml.safe_load(text.split('---', 2)[1])
        url = front.get('permalink')
        assert url and url not in pages, f'Missing or duplicate permalink: {file}'
        html = site_path(url).read_text(encoding='utf-8-sig')
        assert '{{' not in html and '{%' not in html, f'Unrendered Liquid: {url}'
        page = Page(html)
        assert not page.redirect and 'window.location' not in html, f'Automatic redirect: {url}'
        pages[url] = page
        if file.parent.name == 'guides':
            assert url in urls, f'Guide missing from navigation: {url}'
            assert front['layout'] == 'default', f'Guide bypasses common layout: {url}'
            assert not re.search(r'```|\b(?:API|backend|frontend|migration|pull request)\b', text, re.I), f'Developer wording: {file}'
    # New standalone guides are navigable without joining the ordered pager chain.
    chain = [c['url'] for c in chapters if c.get('previous_url') or c.get('next_url')]
    for chapter in chapters:
        url = chapter['url']
        i = chain.index(url) if url in chain else None
        assert url in pages, f'Navigation destination missing: {url}'
        for key, offset, rel in [('previous_url', -1, 'prev'), ('next_url', 1, 'next')]:
            expected = chain[i + offset] if i is not None and 0 <= i + offset < len(chain) else None
            assert chapter.get(key) == expected, f'Broken ordered {key}: {url}'
            assert pages[url].pagers.get(rel) == expected, f'Rendered pager mismatch: {url}'
            if expected:
                assert not expected.lower().endswith('.pdf'), 'Pager opens PDF'
    checked = set()
    for source, page in pages.items():
        for href in page.links:
            full = urlsplit(urljoin(ORIGIN + source, href))
            if full.netloc != 'docs.devdylnz.com':
                continue
            target = full.path
            assert site_path(target).is_file(), f'Broken link: {source} -> {href}'
            if full.fragment:
                assert target in pages and unquote(full.fragment) in pages[target].ids, f'Broken fragment: {source} -> {href}'
            checked.add(target)
    pdfs = list((ROOT / 'assets/guides').rglob('*.pdf'))
    assert len(pdfs) == 3, 'Original PDF count changed'
    for file in pdfs:
        relative = file.relative_to(ROOT).as_posix()
        original = subprocess.check_output(['git', 'show', BASELINE + ':' + relative], cwd=ROOT)
        assert sha(file.read_bytes()) == sha(original), f'Original PDF modified: {relative}'
        assert any(c.get('pdf') and c['url'] == '/' + relative for c in navigation), f'PDF link missing: {relative}'
    assert not (SITE / '_internal').exists(), 'Internal review files exposed by Jekyll'
    print(f'PASS: {len(pages)} rendered pages; {len(chain)} ordered chapters; {len(checked)} internal destinations; all anchors and pagers; 3 unchanged PDFs.')
    if args.live:
        def fetch(path):
            response = requests.get(ORIGIN + path, timeout=45)
            response.raise_for_status()
            assert urlsplit(response.url).path == path, f'Unexpected live redirect: {path}'
            local = site_path(path).read_bytes()
            if path.endswith(('.pdf', '.jpg', '.png')):
                assert response.content == local, f'Live binary differs from validated build: {path}'
            else:
                assert response.content.replace(b'\r\n', b'\n') == local.replace(b'\r\n', b'\n'), f'Live content differs from validated build: {path}'
            return path
        with ThreadPoolExecutor(max_workers=6) as pool:
            live = list(pool.map(fetch, sorted(checked)))
        print(f'PASS: all {len(live)} published destinations return HTTP 200 and match the validated build (text line endings normalised), including PDFs, CSS and every published page.')


if __name__ == '__main__':
    main()
