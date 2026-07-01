# Changelog

Repo-level history. The spec keeps its own detailed changelog in `spec/powerpoint-brand-skill.md`.

## 3.2.1 (July 2026)

- Section numbers live on dividers only (founder call): TOC cards are unnumbered; content slides already carried the red eyebrow. The 88pt divider number is the deck's only section number.
- Styleguide slide gallery refreshed to current chrome: red eyebrows replace teal corner numbers, corner bird marks removed, TOC frame unnumbered.
- index.html prose synced to the spec (logo section still mandated corner marks; red sections still read 8-10% second accent).

## 3.2.0 (July 2026)

- Merges the two v3.1 forks (both shipped as 3.1.0). Deck fork (June 11, deployed skill, never pushed): red eyebrow labels replace content-slide section numbers, channel-coded table header fills, Layout F2 narrative + mini-trend band (discussion notes retired), corner bird mark retired, Layout P performance trend, pie/donut rules, flat red dot. Repo fork (June 24, pushed, never deployed): red co-accent (12-18%) + sanctioned text role, black-default icons, 24-image photography library. 3.2.0 carries both; conflicts resolved toward the deliberate decision in each case.
- README red row synced to the co-accent promotion (went stale in 3.1.0).
- Known gap: the styleguide slide gallery still renders v3.0 content-slide chrome (teal section number, corner mark). Refresh queued.
- Spec, packaged skill, and styleguide all carry 3.2.0.

## 3.1.0 (June 2026)

- Red promoted to a full co-accent and a sanctioned text color. Allowed weight raised from 8-10% to 12-18%; new `--color-text-signal` (red-500) token plus `--color-signal-hover`/`--color-signal-active`. Red `862633` on `FAFAFA` is ~8.3:1, passing WCAG AA at any size, so red is legal for headlines, eyebrows, key stats, and pull quotes. Guardrails kept: not for long body runs, never a full content background. Bar+dot signature unchanged.
- Icons default to black. New `--color-icon` token (off-black `0D0D0D`); `.icon-row svg` and demo icon strokes moved off teal. Teal is now an opt-in accent stroke. Nine new line icons added (growth, trends, insight, velocity, performance, audience, message, trust, budget).
- Photography library grown to 24 cleared images (14 SF nightscapes, 10 corvids), each with a `PHOTOS.md` manifest row. Nightscape-only rule unchanged.
- Spec, styleguide, and tokens synced to 3.1.0.

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
