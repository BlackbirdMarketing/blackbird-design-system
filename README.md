# Blackbird PPC Design System

The single source of truth for the Blackbird PPC brand. Colors, typography, logo, spacing, layout patterns, signature motifs, imagery, voice, and the PowerPoint skill, in one versioned place.

The main artifact is [`index.html`](index.html), a self-contained styleguide you can open in any browser or publish as a live page.

## Brand in 30 seconds

**Two brand colors.** Teal and red. Everything else is surface, structure, or ink.

| Token | Hex | Role | Weight |
|-------|-----|------|--------|
| Surface | `#FAFAFA` | Off-white page, never pure white | 50-55% |
| Teal | `#008C95` | Brand accent. Fills, bars, chart series, large numerals | 12-15% |
| Red (Signal) | `#862633` | Co-accent + sanctioned text color. Headlines, eyebrows, key stats, the bar+dot | 12-18% |
| Slate | `#64748B` | Structure. Dividers, captions, icon strokes | 12-15% |
| Black | `#000000` | Display. Headlines and big stat numbers | 5-7% |
| Dark Slate | `#1E293B` | Reading. Body copy, table text, cool dark cards | 5-8% |
| Off-black | `#0D0D0D` | The dark section ground | dark slides |

**Small-text accent (v3.0):** teal-500 on the off-white surface is 3.88:1 and fails WCAG AA below 18px. Links, eyebrows, and section numbers use `--color-link` (teal-600, 5.61:1). Teal-500 keeps every fill, bar, and large-numeral role.

**Two fonts.** Futura for headlines, Avenir for body. Web stand-ins: Jost and Nunito Sans.

**One signature.** The teal bar with the red dot. Maximum once per page.

**One hard rule.** No bars on cards, no exceptions. Cards stand on their outline alone.

## What is in this repo

```
index.html        The styleguide. Open it in a browser.
spec/             The canonical written spec (PowerPoint brand skill).
skill/            The packaged skill: SKILL.md + bundled logo assets, ready to upload.
assets/logos/     All six lockups plus deck-ready crops (tight + pre-faded).
assets/photography/  24 cleared images (14 SF nightscapes, 10 corvids) + PHOTOS.md license manifest.
assets/clients/   Client logos used by the case-study examples.
assets/meta/      Favicons and the social-share card.
tokens/           tokens.css and tokens.json. Drop into any project.
scripts/          validate_assets.py, the CI guard.
reference/        Portable PDF snapshots of the styleguide.
VERSION           The single system version. Governs index.html and the spec.
CHANGELOG.md      Repo-level history.
```

## View it

Open `index.html` in any browser. No build step. External loads: Google Fonts (Jost, Nunito Sans).

With GitHub Pages enabled (Settings, Pages, deploy from `main`), the live styleguide lives at:

```
https://blackbirdmarketing.github.io/blackbird-design-system/
```

## One version

`VERSION` at the repo root is the system version. `index.html` and `spec/powerpoint-brand-skill.md` both carry it, and CI (`.github/workflows/validate.yml`) fails any push where they diverge, where the core six hex values drift between the two artifacts, or where `index.html` references a file that does not exist.

## Update it

1. Edit `index.html` and/or the spec.
2. Bump `VERSION`, note the change in `CHANGELOG.md` and the spec changelog.
3. If the skill changed, re-copy the spec into `skill/blackbird-pptx-brand/SKILL.md` and re-upload the skill folder.
4. Run `python3 scripts/validate_assets.py`, then commit. Pages updates on push.

## Photography rules

Nightscape only: dusk, after-dark, atmospheric, low-key. No AI-generated cityscapes or birds. Every image gets a row in `assets/photography/PHOTOS.md` in the same commit; an image without a manifest row does not ship.
