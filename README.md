# Blackbird PPC Design System

The single source of truth for the Blackbird PPC brand. Colors, typography, logo, spacing, layout patterns, signature motifs, imagery, and voice, in one versioned place.

The main artifact is [`index.html`](index.html), a self-contained styleguide you can open in any browser or publish as a live page.

## Brand in 30 seconds

**Two brand colors.** Teal and red. Everything else is surface, structure, or ink.

| Token | Hex | Role | Weight |
|-------|-----|------|--------|
| Surface | `#FAFAFA` | Off-white page, never pure white | 50-55% |
| Teal | `#008C95` | Brand accent. Numbers, links, primary data | 12-15% |
| Red (Signal) | `#862633` | Second accent. Headlines, key stats, the bar+dot | 8-10% |
| Slate | `#64748B` | Structure. Dividers, captions, icon strokes | 12-15% |
| Black | `#000000` | Display. Headlines and big stat numbers | 5-7% |
| Dark Slate | `#1E293B` | Reading. Body copy, table text, cool dark cards | 5-8% |
| Off-black | `#0D0D0D` | The dark section ground | dark slides |

**Two fonts.** Futura for headlines, Avenir for body. Web stand-ins: Jost and Nunito Sans.

**One signature.** The teal bar with the red dot. Maximum once per page.

**One hard rule.** No bars on cards. Ever. Cards stand on their outline alone.

## What is in this repo

```
index.html      The styleguide. The main thing. Open it in a browser.
spec/           The canonical written spec (PowerPoint brand skill v2.8).
reference/      A portable PDF snapshot of the styleguide.
icons/          Blackbird logos and reference imagery used by index.html.
Logos/          Client logos used by index.html.
blackbird_logo*.png   Root logos used by index.html.
```

## View it

Open `index.html` in any browser. No build step, no dependencies. The only external load is Google Fonts (Jost and Nunito Sans), which resolves automatically online.

Once this repo is on GitHub with Pages enabled, the live styleguide lives at:

```
https://<your-org>.github.io/blackbird-design-system/
```

## Source of truth and versions

This repo closes the brand's longest-standing governance gap: three artifacts that carried three different version numbers. From here, the repo is canonical.

- **Design system styleguide:** `index.html`, v2.1
- **PowerPoint brand skill:** `spec/powerpoint-brand-skill-v2.8.md`, v2.8

The two are aligned. When the brand changes, change it here first, bump the version, and let the website and decks follow.

## Update it

1. Edit `index.html` (or the spec).
2. Bump the version in the file and note the change in the spec changelog.
3. Commit. If Pages is enabled, the live styleguide updates on push.
