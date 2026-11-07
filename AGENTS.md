# SEO & Public Discoverability Rules (AGENTS.md)

1. **Page Metadata & Indexing (`docs.devdylnz.com`)**:
   - Every published documentation guide and current legal policy MUST define a unique, descriptive `title` and a 140–160 character `description` in YAML front matter, written from that page's actual content.
   - `_layouts/default.html` renders `{% seo %}` (via `jekyll-seo-tag`) so every page outputs exactly one `<title>`, `<meta name="description">`, `<link rel="canonical">`, OpenGraph (`og:title`, `og:description`, `og:url`, `og:site_name`), and Twitter metadata block. Do not add duplicate manual `<title>` or `<meta name="description">` tags.
   - Current guides and active legal policies output `<meta name="robots" content="index, follow">`.
   - Archived legal versions under `legal/versions/**` MUST set `sitemap: false` in front matter so they are excluded from `sitemap.xml` and receive `<meta name="robots" content="noindex, follow">`.
2. **Sitemap & Robots Configuration**:
   - Keep `jekyll-seo-tag` and `jekyll-sitemap` enabled in `_config.yml` with `url: "https://docs.devdylnz.com"`.
   - Keep `robots.txt` at the repository root allowing all crawlers (`Allow: /`) and pointing to `Sitemap: https://docs.devdylnz.com/sitemap.xml`.
   - Keep internal/repository-only files (`_internal`, `README.md`, `AGENTS.md`, `Gemfile`, `Gemfile.lock`) in `_config.yml`'s `exclude` list so they are never published or added to `sitemap.xml`.
3. **Structured Data Integrity (`_includes/structured-data.html`)**:
   - Keep `Organization` / `ProfessionalService` / `LocalBusiness` JSON-LD accurate to verified business facts (`name: "Dev Dyl NZ"`, `@id: "https://devdylnz.com/#organization"`, `url: "https://devdylnz.com"`, NZBN `9429054041851`, `email: "contact@devdylnz.com"`, locality `Tauranga, Bay of Plenty, NZ`, slogan `"BUILD • AUTOMATE • COMMUNITIES"`). Never invent or add a street address, phone number, founder name, or `"Limited"`.
   - Keep `SoftwareApplication` / `WebApplication` JSON-LD on the homepage accurate to Bracket Control (`softwareVersion: "2.0"`, marketing URL `https://devdylnz.com/bracket-control`, app URL `https://bracketcontrol.runs-on.dev/app/`, `featureList` strictly matching documented production features).
   - Keep `TechArticle` JSON-LD on documentation pages and `FAQPage` JSON-LD only on pages with genuine question-and-answer content (`/troubleshooting/`). Always escape dynamic strings with `| jsonify`.
4. **Cross-Property Attribution Links**:
   - Preserve visible, crawlable links in `_layouts/default.html` to `https://devdylnz.com/bracket-control` ("Bracket Control by Dev Dyl NZ") and `https://bracketcontrol.runs-on.dev/app/` ("Open Bracket Control").
