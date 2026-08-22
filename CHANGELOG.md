# Changelog

Repo-level history. The spec keeps its own detailed changelog in `spec/powerpoint-brand-skill.md`.

## 3.4.1 (August 2026)

Removed `line: { width: 0 }` from all ten pptxgenjs helper call sites in
Section 11. Measured against pptxgenjs 4.0.1, that form emits a solid 1pt
`333333` stroke rather than suppressing the outline: the zero width is falsy
and falls back to the 1pt default, and the absent color falls back to
`DEF_SHAPE_LINE_COLOR = '333333'`. Every deck built from the spec's own helpers
since v2.4 carried these outlines. Replaced with `line: { type: 'none' }`.
`addBottomBar`, the only helper with no `line` key, now sets it explicitly.
Section 4a's pptxgenjs guidance replaced with a measured emission table. Repo
guard now fails on any `line: { width: 0 }` outside the changelog.

## 3.4.0 (August 2026)

- New spec Section 4a (Outline Control). Default rule: every shape ships with no outline unless the spec names it. Replaces the additive model, which only held if the authoring tool defaulted to no border; none of PowerPoint, Google Slides, pptxgenjs, or python-pptx do.
- Four legal strokes only: slate-200 `E2E8F0` (white cards), teal-200 `A0DCE0` (teal-50 cards), red-200 `DD9AA3` (red-50 cards), slate-300 `CBD5E1` (reporting table row separators).
- `333333` banned as a shape stroke. It is the Google Slides and pptxgenjs default shape border. It remains valid as the `dark-line` token, the fill of an internal divider rule on a dark slide, so the ban is scoped to `<a:ln>` blocks only.
- Theme-inherited strokes banned: an `<a:lnRef>` with no explicit `<a:ln>` override picks up the Office theme `lnStyleLst`, which carries a filled line at all three indices.
- Per-tool suppression documented for PowerPoint (hand-drawn and template), Google Slides and the Slides API, pptxgenjs, and python-pptx.
- New guard `scripts/validate_deck_outlines.py`, wired into the validate workflow. Fails on banned strokes, unsanctioned stroke colors, and unoverridden theme line references.
- New Pre-Ship Checklist row (Outlines) and Common Mistake #8; prior mistakes #8-#24 renumbered #9-#25.
- Prompted by the 11x recap deck, which shipped from Google Slides with 50 unintended `333333` outlines on accent bars, bullet dots, chart bars, numbered circles, table rows, and section grounds.

## 3.3.0 (July 2026)

- Plain-language voice overhaul (founder call). Em dashes are banned in all deck copy and in every file in this repo; the sweep removed them from the spec, index.html, tokens.css, and all docs.
- Spec Section 9 (Voice) rewritten: 13 principles, including no em dashes, complete ordinary sentences, no aphorisms, no personification, no second-person sales hooks, no manufactured candor, and no invented quotes. Voice examples replaced with plain reporting statements; the Don't list now carries the founder's flagged examples.
- Layout I (quote interstitial) now requires a real quote from a named person or cited source, attributed with name, title, and organization. No real quote means no quote slide; use Layout O with a stated finding instead.
- Conclusion-style slide titles kept, with guardrails: a title is a statement of fact with a subject and a verb. No imperatives, no second person, no questions as hooks, no inverted-promise framing.
- Mission wording changed from "tell the truth about what is working" to "report what is working and what is not."
- Pre-Ship Checklist rows for Titles and Voice expanded; Common Mistakes 22-24 added (em dashes, invented quotes, slogan copy).
- Styleguide (index.html) prose swept to match: hero, section titles, voice examples, and the slide-gallery quote (now an attributed-client placeholder).

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
