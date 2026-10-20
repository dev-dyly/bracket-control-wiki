# Bracket Control Wiki — publication staging package

This package is a **staging-only documentation site**, prepared for `docs.devdylnz.com`. It **excludes all three unapproved legal drafts** so that uploading it to a public repository does not publish legal placeholders or unverified age/contact terms. Pages remain publicly readable if you enable Pages.

**Do not call this the final legally cleared public launch.** The operator must verify privacy collection notices, policies, correct email/contact route, age restrictions and the live production feature baseline before linking the wiki as official policy.

## Setup

1. Create a separate public repository at `dev-dyly/bracket-control-wiki`. The existing `dev-dyly/Bracket-App` private source repository remains unchanged.
2. Extract this ZIP, then upload **all extracted contents** (not the ZIP file itself, and not an enclosing folder) into the repository root on `main`. Preserve `_layouts`, `assets`, `guides`, `_config.yml`, `index.md`, and `CNAME`.
3. Configure repository **Settings → Pages → Deploy from a branch → main / (root)**.
4. Verify `devdylnz.com` ownership in your GitHub account **Settings → Pages** using the GitHub-provided TXT record in Cloudflare.
5. Configure the repository's **Settings → Pages → Custom domain** as `docs.devdylnz.com`.
6. In Cloudflare DNS set `CNAME` name `docs`, target `dev-dyly.github.io`, **DNS only**. Do not change the existing `app` record.
7. Enable **Enforce HTTPS** when available, then check pages, navigation and mobile formatting.
8. Before public release, reconcile guides with actual deployment and publish legally approved Privacy Policy, Terms and Cookie Notice. Restore legal navigation only after publishing those pages.

The original complete archive retains the draft legal files for private review. This staging version must never be substituted for the production legal compliance process.

## Documentation navigation maintenance

The ordered chapters in `_data/navigation.yml` power the header, sidebar, page progress, breadcrumbs and Previous/Next links. When adding or moving a page, include its exact `permalink` (including leading and trailing slashes) in that file, then confirm it renders and links work on desktop and mobile. The first page has no Previous link; the final page offers Back to Home. Never link to unpublished legal drafts.
