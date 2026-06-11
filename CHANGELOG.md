# Changelog

Repo-level history. The spec keeps its own detailed changelog in `spec/powerpoint-brand-skill.md`.

## 3.0.0 (June 2026)

- Single system version: `VERSION` file governs `index.html` and the spec; CI enforces it along with asset existence and core-six hex parity (`scripts/validate_assets.py`, `.github/workflows/validate.yml`).
- Restored the five missing image assets (the `icons/` folder was never committed) by recovering originals from the v2.1 PDF snapshot, and restructured into `assets/logos/`, `assets/photography/`, `assets/clients/`, `assets/meta/`.
- Logo pack: all six lockups at source quality plus deck-ready crops, including a 90%-alpha pre-faded bird mark for python-pptx.
- Photography library: 14 cleared images (9 SF nightscapes, 5 corvids) with a per-file license manifest. The pre-v3.0 Twin Peaks hero is flagged license-unverified.
- Styleguide: photo section divider (Layout G, live) and an off-black rhythm band; photography library grid and overlay-treatment triptych in 06 Imagery; deck rhythm strip and ten-frame slide gallery (Cover, TOC, B, C, D, F, G, I, K, J) in 09 Examples.
- Accessibility: new `--color-link` token (teal-600). Small teal text (eyebrows, section numbers, component labels, nav hover) moves off teal-500, which is 3.88:1 on the surface and fails WCAG AA below 18px.
- Head metadata: description, OpenGraph and Twitter cards, favicons.
- Client logos renamed and converted to RGBA; Meraki spelling fixed.
- Spec to v3.0: canonical asset paths, corrected corner-mark geometry (the old helper squished the padded file), python-pptx appendix (11b), file renamed to `powerpoint-brand-skill.md`.
- `tokens/tokens.css` and `tokens/tokens.json` shipped; the code section's "ship as tokens.css" claim is now true.
- Packaged skill at `skill/blackbird-pptx-brand/` with bundled assets, ready to upload.

## 2.x (May to June 2026)

- `index.html` v2.1 styleguide and PowerPoint brand skill v2.2 through v2.8. See the spec changelog.
