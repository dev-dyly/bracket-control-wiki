# Bracket Control documentation and policies

The existing GitHub Pages/Jekyll site publishes `main` from the repository root at **https://docs.devdylnz.com/**. Keep `CNAME` and the existing address unchanged.

User guides use plain language and production button names. `_data/navigation.yml` controls their reading order, sidebar, top navigation and Previous/Next links. Every guide has a matching permalink. PDF references remain explicit links outside the reading chain; preserve original PDF paths and files.

Production evidence and review limitations are recorded in [_internal/production-review.md](_internal/production-review.md). `_internal` is excluded from publication. Legal policies and their archived versions are preserved separately from user-guide instructions; this documentation update does not revise legal agreements or the application's configured document versions.

## Documentation checks

From this repository, build with the local Docker image (no application services or infrastructure are changed):

```powershell
docker build -t bracket-wiki-jekyll:review -f _internal/Dockerfile .
docker run --rm --mount "type=bind,source=$PWD,target=/site" bracket-wiki-jekyll:review build --strict_front_matter --destination _internal/site
python _internal/check_docs.py
```

The Python checks require `PyYAML` and `requests`. They check every rendered page, internal destination and fragment, reciprocal Previous/Next links, guide inclusion, absence of automatic redirects, and preservation of the three original PDFs. The local Jekyll version is 3.10.0.

`python _internal/probe_production.py` performs read-only production health, feature availability and served UI-label checks. It does not sign in, change data or test Discord delivery.

After pushing the validated changes, check the GitHub Pages build for that commit and run `python _internal/check_docs.py --live`. This also compares the published HTML, stylesheet and PDFs with the validated local build, allowing text line-ending differences.
