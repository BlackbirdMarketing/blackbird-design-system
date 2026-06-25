---
name: blackbird-pptx-brand
description: "Blackbird PPC PowerPoint brand guidelines (v3.1, June 2026). Use this skill whenever creating, editing, or reviewing a PowerPoint presentation for Blackbird PPC or any Blackbird client deliverable. Triggers include: any request to make a deck, slides, or presentation mentioning Blackbird; any pptx creation where the user is Jay or a Blackbird team member (Hillary, Thomas, Gabby, Jack); any request to 'make it on-brand' or 'use our brand' in a presentation context; any request referencing 'our deck style' or 'Blackbird template'. This skill defines Blackbird's identity layer (mission, pillars), color system, typography, layout patterns, slide anatomy, voice, and a pre-ship checklist for slide decks. Always read this skill BEFORE the general pptx skill when both apply. If this skill conflicts with the general pptx skill, this skill wins."
---

# Blackbird PPC -- PowerPoint Brand Guidelines (v3.1)

Source of truth: the `blackbird-design-system` repo, system version 3.1.0 (see `VERSION` at repo root). The styleguide (`index.html`) and this skill now carry one shared version number. **v3.1 promotes red to a full co-accent (12-18%) and a sanctioned text color, switches icons to black by default with an expanded icon set, and grows the photography library to 24 cleared images (14 SF nightscapes, 10 corvids).** **v3.0 ships canonical assets: the logo pack (`assets/logos/`) and the cleared photography library (`assets/photography/` + `PHOTOS.md`), plus a python-pptx implementation appendix.** **v2.8 relabels slate as structure, not a brand color (teal and red are the only brand colors).** **v2.7 adds Dark Slate `1E293B` as the sixth Core anchor** — the reading-text and cool-dark-card color, kept distinct from Black `000000`, which stays display-only (headlines, max-contrast marks, small UI). **v2.6 settled the dark-surface question across the deck skill, the design-system HTML, and the live site.** One dark section ground: off-black `0D0D0D` (default) or slate-500 `64748B` for warm/structural emphasis — both Core anchors. Pure black `000000` is text/UI only and is **never a section surface**. Slate-800 `1E293B` is now a **sanctioned cool dark-card token** (card on a dark ground), but is **never a full-bleed section ground**. Cards on a dark ground: neutral `1C1C1C`/`222222`, or cool slate-800 `1E293B` (white text). v2.5 had removed slate-800 from every surface; v2.6 brings it back for cards only, to legalize the live site's dark cards without blessing pure-black grounds. v2.4 closed the "no top-edge bars on cards" rule. v2.3 enforces 10px radius on every card-like container. When the general pptx skill conflicts with anything here, these rules override.

## Quick Reference

| Element | Value |
|---------|-------|
| Slide size | 16:9 (10.00" x 5.625") |
| Page surface | Off-white `FAFAFA` (not pure white) |
| Card surface | Pure white `FFFFFF`, 1pt slate-200 (`E2E8F0`) outline, 10px radius |
| Default dark surface | Off-black `0D0D0D` (Core dark-surface anchor) |
| Slate emphasis surface | Slate-500 `64748B` (Core slate anchor; medium cool-gray, not "dark") |
| Headlines | Black `000000` |
| Body | Slate-800 `1E293B` |
| Headline font | Futura (Mac) / embed Futura on Win, fallback Bahnschrift > Trebuchet MS |
| Body font | Avenir (Mac) / embed Avenir on Win, fallback Calibri |
| Bottom accent bar | Teal `008C95`, 0.10" tall, full width, y=5.53" |
| Top margin (section number) | 0.28" |
| Left margin (text) | 0.45" |
| Left margin (card edges) | 0.38" |

---

## 0. Identity Layer

This is the meaning the visual system carries. Slide titles, body copy, and stat-callout context strings should sound like a brand that holds these positions.

### One-liner
High-performance advertising for ambitious teams, built on measurement and made with craft.

### Motto
Pride in the craft of advertising.

### Mission
We exist to correct the common failures of modern performance marketing by uniting paid media craft with measurement rigor. We tie spend to business outcomes, tell the truth about what is working, and treat stewardship of client budgets and relationships as a professional duty.

### Six Strategic Pillars

| Pillar | What it means in slide copy |
|--------|------------------------------|
| **Craft** | Operational discipline, not aesthetic preference. Every query, bid, and message is worth getting right. |
| **Performance** | Defined in business terms (pipeline, revenue), not clicks. Outcomes framed as revenue increase and lead efficiency improvement. |
| **Advanced Analytics & Measurement** | MMM, multi-touch attribution, incrementality and holdout testing, on/off tests, marginal return analysis, first-party data. Tied to decisions, not reporting. |
| **Client Stewardship** | High-touch service as differentiator. Clients describe Blackbird as an extension of their team. Stewardship of budgets and relationships treated as a professional duty, not a selling point. |
| **Intellectual Honesty** | Truth-seeking measurement. Distrust of misleading attribution conventions. Analytics to detect manipulation, not dress up reporting. |
| **Ambition** | Mapped to client growth stakes. Ideal client is technology-forward, growth-driven, sophisticated in analytics or finance. |

### Core Intersection: Ambition, Analytics, Artistry
- **Ambition** maps to client expectations and growth stakes
- **Analytics** maps to the measurement stack and truth standards
- **Artistry** maps to craft discipline in execution, copy, creative testing, and the refusal of generic agency language

Use this trio as a structural anchor on capabilities slides, executive summaries, and the cover-after-cover positioning slide.

---

## 1. Color System

### The Core Six (carry 90% of every slide)

| Token | Hex | Role | Approx Deck Weight |
|-------|-----|------|---------------------|
| Surface | `FAFAFA` | **Primary.** Off-white page. Matches the live site. | 50-55% |
| Brand accent (Teal) | `008C95` | **Primary accent.** Section numbers, the bottom-of-slide accent bar, bullets, links, primary buttons, key data, chart primary series. | 12-15% |
| Signal (Red) | `862633` | **Co-accent.** Counterweight to teal — declarative, brand-anchored. Headlines and section eyebrows, secondary CTAs, output/risk/optionality columns, award badges, the bar+dot motif, key stats and pull quotes, hairline accents on dark surfaces, critical callouts. **Sanctioned as a text color** (red-500 on FAFAFA is ~8.3:1, AA at any size) for headlines, eyebrows, stats, and pull quotes. | 12-18% |
| Slate (structure) | `64748B` | **Structural spine, not a brand color.** Icons on light bg, secondary CTAs, dividers, the warm/structural emphasis ground, caption/secondary text. | 12-15% |
| Black | `000000` | **Display anchor.** Headlines, section titles, big stat numbers, maximum-contrast display type; small solid black UI (dark buttons, pills); content-role icons. Short, high-salience marks — never long body runs, never a surface. | 5-7% |
| Dark Slate (6th anchor) | `1E293B` | **Reading + cool-dark anchor.** Body/reading copy on light (where pure black glares) and table text; plus the cool dark-card surface on a dark ground (white text). The softened counterpart to Black. Never a section ground. | 5-8% |

**A seventh hex needs to earn its place.** Almost always the answer is no.

**Only two of the six are brand colors: teal and red.** The rest are surface (`FAFAFA`) plus structure/ink (slate, black, dark slate), with off-black `0D0D0D` the dark ground. Brand colors carry identity and may lead a composition; surface and structure recede. Slate is a structural neutral (its hex is Tailwind's slate-500), not an identity color, so never push it forward to "feel like the brand" the way teal and red can.

**Black vs Dark Slate — the rule that keeps six colors from blurring.** Black `000000` is for *display and punch*: headlines, section titles, big stat numbers, anything meant to read as a headline or hit maximum contrast, plus small solid black UI (dark button/pill) and the bird mark on light. Dark Slate `1E293B` is for *reading and cool dark*: body copy and any text read at length (paragraphs, descriptions, table cells), where pure black would glare, plus the cool dark-card on a dark ground (white text on it). Quick test: a headline or one-liner is **black**; a sentence you actually read is **dark slate**; a big flat dark area is off-black `0D0D0D` (neither). Black never runs long and is never a surface; dark slate is never the section ground.

### Teal Scale (anchor at 500)

| Step | Hex | Use |
|------|-----|-----|
| 50 | `ECF7F8` | Subtle backgrounds, info banner, accent pill, card tint |
| 100 | `CFEEF0` | Light teal fill, subtle highlight |
| 200 | `A0DCE0` | Card outlines on tinted cards |
| 300 | `6EC6CB` | Light variant, hover backgrounds |
| 400 | `36AAB1` | Mid-light tint |
| **500** | **`008C95`** | **Brand accent.** Workhorse. |
| 600 | `007078` | Hover state |
| 700 | `00565D` | Active/pressed, dark teal accent text |
| 800 | `003E43` | Deep teal accent |
| 900 | `00282C` | Footer band when teal preferred over black |
| 950 | `001316` | Maximum dark teal |

### Red Scale (anchor at 500)

| Step | Hex | Use |
|------|-----|-----|
| 50 | `F8E9EC` | Signal pill background, error banner, output column tint |
| 100 | `EFC9CF` | Light red fill (rare) |
| 200 | `DD9AA3` | Border on tinted output cards |
| 500 | `862633` | **Signal.** |
| 700 | `561821` | Output column title text on red-50 background |

### Slate Scale (cool, anchor at 500 = structural spine)

| Step | Hex | Use |
|------|-----|-----|
| 50 | `F8FAFC` | Page section bg, card hover, Quick Win callout |
| 100 | `F1F5F9` | Cards, calculators, secondary panels, table header fills |
| 200 | `E2E8F0` | Card borders, dividers, hairlines on white |
| 300 | `CBD5E1` | Stronger dividers, table borders |
| 400 | `94A3B8` | Timestamps, faint metadata |
| **500** | **`64748B`** | **Structural spine (not a brand color).** Slate accents, icon strokes, secondary CTAs, neutral numbered prefix, the warm emphasis surface. |
| 600 | `475569` | Mid-dark slate |
| 700 | `334155` | Body secondary, slate-toned dark sections |
| 800 | `1E293B` | Body text on light; the cool dark-card on a dark ground (`dark-card-cool`, white text). Never a section ground. |
| 900 | `0F172A` | Deep slate (rare) |
| 950 | `000000` | Brand black, headline anchor |

### Dark Surface Set

| Token | Hex | Use |
|-------|-----|-----|
| `dark-bg` | `0D0D0D` | True off-black. The dark **section ground** — emphasis slides, closing, code blocks |
| `dark-card1` | `1C1C1C` | Neutral panel cards on off-black |
| `dark-card2` | `222222` | Neutral panel cards on off-black (alt) |
| `dark-card-cool` | `1E293B` | **Cool dark-card (slate-800).** Card on a dark ground when a cooler cast is wanted. White text. Border slate-500 `64748B` @ ~40%. Never a full-bleed section ground. |
| `dark-row` | `2A2A2A` | Alternating rows inside dark cards |
| `dark-line` | `333333` | Internal dividers on dark slides |

**Default dark section ground = off-black `0D0D0D`** (the Core Five Dark Surface anchor). Two section grounds, both anchored: off-black `0D0D0D` for heavy/dark emphasis, and slate-500 `64748B` for warm/structural emphasis (a medium cool-gray, not actually "dark"). **Pure black `000000` is never a section ground** — it is the text/headline and small-UI anchor only. **Cards on a dark ground** are neutral (`1C1C1C`/`222222`) or cool slate-800 (`1E293B`, white text); slate-800 reads as a card *because* it sits ~1.3:1 above the off-black ground (more separation than the neutral grays), but it is a card token, never a section ground. Slate-700 stays a text/accent primitive.

### Color Rules

1. **Off-white carries the surface.** Page is `FAFAFA`, not pure white. 50-55% of slide area. Pure white `FFFFFF` is for cards lifted above the surface.
2. **Cards = white on off-white. No top-edge bars on cards. Ever.** `FFFFFF` background, 1pt `E2E8F0` outline (for white cards specifically), 10px radius. Tinted cards (teal-50, red-50) use matching teal-200 or red-200 borders. Depth comes from surface contrast, not drop shadows, not colored bars. The teal top-edge bar that lived on cards in v2.0 is removed — that pattern duplicated the bar+dot signature inside containers.
3. **No pastel cards.** Blush, Mint, Cream, Ice are dead. If a card needs tint, use `teal-50` or `red-50` with matching border, and only when the meaning calls for it.
4. **Slate is the structural spine, not a brand color.** Teal and red are the only brand colors. Slate carries structure and recedes: tertiary CTAs, icon strokes on light bg, dividers between major sections, the warm emphasis ground.
5. **Teal as primary accent, not punctuation.** Target 12-15% of any view. Surfaces, fills, links, CTAs, dividers. The constraint is meaning: teal carries positive/primary signal.
6. **Red is a full co-accent, not signal-only.** Target 12-18% per deck. Counterweight to teal — declarative, confident, brand-anchored. Use for headlines and section eyebrows, secondary CTAs and pill buttons, output/risk/optionality columns, award badges, the bar+dot motif, key stats and pull quotes, hairline accents on dark surfaces, critical callouts. Red is also a **sanctioned text color** — red-500 on the FAFAFA surface is ~8.3:1 and passes WCAG AA at any size, so it may set headlines, eyebrows, key stats, and pull quotes. Pair intentionally against teal so the meanings stay distinct: teal = primary/positive, red = emphasis/counterpoint. The only limits: avoid red as a full content background, as long runs of body copy, or in long runs of solid fill.
7. **Emphasis surfaces.** Two anchored options, both Core anchors: off-black `0D0D0D` for heavy/dark emphasis, slate-500 `64748B` for warm/structural emphasis (medium cool-gray, not "dark"). Pick by the feeling you want. No slate-700/-800 section grounds (slate-800 is the cool dark-card, not a ground).
8. **No gradients.** Flat color only. Exception: the roadmap connector line (teal-500 → red-500 hairline, see Roadmap pattern).
9. **No new colors without a token.** If you reach for a seventh hex, ask if it earned its place. The answer is almost always no.
10. **Chart series = Teal, Slate, Black.** More series = data density problem, not a color problem. Red only for outliers.
11. **Bar+dot motif: maximum once per slide.** The teal-bar-red-dot signature is a signature, not a repeating decoration. Two on one slide reads as pattern, not punctuation — and the second one weakens the first. Roughly 1 in 3-4 slides across the deck.

### Photo-Backed Slide Treatment

Cover, section dividers, closing slide:
- Full-bleed San Francisco nightscape photo
- Dark overlay to taste (goal is mood, not a fixed opacity number — typically 60-75%)
- White headlines, slate-300 or white subtitles
- Teal for section numbers (88pt on dividers)

### Alternating Rhythm

Break up white slides with a dark slide every 3-5 slides. Dark slides can be:
- **Section divider** — full-bleed photo + overlay
- **Off-black emphasis slide** — solid `0D0D0D`, key finding, executive callout, case-study stat strip, code blocks, closing (default for every dark slide)
- **Slate emphasis slide** — solid slate-500 `64748B`, the warm/structural alternative ground when off-black is too heavy. (The slide *ground* is never slate-800 `1E293B` and never pure black `000000`; slate-800 is a card color on a dark ground, not a section ground.)
- **Quote interstitial** — solid off-black, centered quote, teal rules above/below

### Teal Bar + Red Dot Motif (signature)

The strongest Blackbird visual signature.

**Anatomy:**
- Teal bar: `008C95`, height 0.05-0.06", width typically 1-3" depending on placement
- Red dot: `862633`, filled circle, 0.12-0.14" diameter
- Dot sits at right end of bar, vertically centered, with a small gap (~0.03") between bar end and dot center

**Use:**
- Below slide titles as a divider
- Below quotes or key statements
- As section-end punctuation
- On dark slides as the primary decorative element

**Don't:**
- Inside cards (gets lost)
- On every slide. Roughly 1 in 3-4
- **Multiple times on one slide. Maximum once per slide, no exceptions.** Two on one slide reads as pattern, not punctuation — and the second one weakens the first. If you need a second separator, use whitespace or the bottom accent bar.

```javascript
function addTealBarRedDot(slide, pres, x, y, barWidth) {
  slide.addShape(pres.shapes.RECTANGLE, {
    x, y, w: barWidth, h: 0.055,
    fill: { color: COLORS.TEAL },
  });
  const dotSize = 0.13;
  slide.addShape(pres.shapes.OVAL, {
    x: x + barWidth + 0.03,
    y: y + 0.055 / 2 - dotSize / 2,
    w: dotSize, h: dotSize,
    fill: { color: COLORS.RED },
  });
}
```

---

## 2. Typography

### Font Stack

| Role | Font | Weight | Cross-platform fallback |
|------|------|--------|--------------------------|
| Headlines / Section titles | Futura | Bold | Mac: Futura. Win: embed Futura, else Bahnschrift > Trebuchet MS. Slides: Jost. |
| Body / Descriptions | Avenir | Book (regular) | Mac: Avenir. Win: embed Avenir, else Calibri. Slides: Nunito Sans. Squarespace: europa. |
| Section numbers ("01") | Futura | Bold | Same as headline |
| Data / Captions | Avenir | Book, smaller | Same as body |

**Always embed Futura and Avenir in shared `.pptx` files.** PowerPoint > File > Save > Embed Fonts in File. ~200KB cost. Without this, Windows recipients see Calibri substitutes.

### Type Scale

| Element | Size | Font | Color | Notes |
|---------|------|------|-------|-------|
| Cover headline | 48pt | Futura Bold | White | Uppercase, letter-spaced |
| Section number (top-left) | 13pt | Futura Bold | Teal `008C95` | Always two digits ("01") |
| Section number (divider slide) | 88pt | Futura Bold | Teal `008C95` | Photo-backed dividers |
| Page title | 24pt | Futura Bold | Black `000000` | Left-aligned, below section number |
| Subtitle / lead-in | 18pt | Futura Bold | Slate-700 `334155` | Short statement under page title |
| Card title | 14pt | Futura Bold | Black `000000` | Uppercase, letter-spacing 0.02em |
| Body (primary) | ~13pt | Avenir | Slate-800 `1E293B` | Primary reading size |
| Small body / descriptions | ~11pt | Avenir | Slate-700 `334155` | Card descriptions, secondary |
| Caption / footnote | ~9pt | Avenir | Slate-500 `64748B` | Sources, disclaimers |
| Large stat callout | 60-80pt | Futura Bold | Teal `008C95` | NPS, key metric. Cap at ~80pt. |
| Quote text | 24-36pt | Avenir | White on dark | Italics, curly quotes |

### Typography Rules

1. **Left-align everything.** Three exceptions only: cover slide, quote interstitial, and roadmap card text (component-scoped exception).
2. **No underlines.** Emphasis through weight or color, never underlines. Two motif exceptions: the teal bar+red dot signature and the section-header underline (matches headline width).
3. **Futura for hierarchy, Avenir for reading.** Heading/label/category = Futura. Paragraph/description = Avenir.
4. **Two-digit section numbering.** Always "01" not "1". Futura Bold.
5. **Mix the rhythm.** A good content slide has 2-3 different text formats running through it. Mix fonts (Futura headers, Avenir body), weights (bold key terms inside running prose), color (one teal phrase per paragraph), and bullet styles. A bad slide has eight identical rows.

---

## 3. Logo

Three lockups. Black on light, white on dark. Never recolor.

| Lockup | Min size | Use for |
|--------|----------|---------|
| **Horizontal lockup** | 120px wide on screen | Default. TOC slide right-center (~2.5" wide), footers, signatures. |
| **Circular badge** | 48px wide | Profile photos, app icons, sticker moments. |
| **Bird mark** | 24px wide | Watermarks, content slide bottom-right corner, tight contexts. |

### Logo placement on decks

- **Cover slide:** No logo. The project/client name does the work.
- **TOC slide:** Horizontal lockup, right-center area, ~2.5" wide.
- **Every content slide:** Bird mark in bottom-right corner, ~0.32" tall, opacity ~0.9.
- **Closing slide:** No logo. Just "Thank you" centered.

The pattern is bird mark = quiet brand presence on the most-used layout; horizontal lockup = louder statement, used sparingly.

### Canonical asset files (v3.0)

All lockups live in the repo at `assets/logos/` and are bundled inside this skill folder under `assets/`. Use these files; do not regenerate or trace the mark.

| File | What it is | Notes |
|------|------------|-------|
| `bb-horizontal-lockup.png` / `_white.png` | Horizontal lockup, 820x312 | TOC right-center at ~2.5" wide |
| `bb-circular-badge.png` / `_white.png` | Circular badge, 800x800 | Profile photos, favicons, stickers |
| `bb-bird-mark.png` / `_white.png` | Bird mark on full 1148x774 canvas | Watermarks, large placements |
| `bb-bird-mark-deck.png` | Bird mark, tight crop 633x597 (aspect 1.06) | The content-slide corner mark |
| `bb-bird-mark-deck-faded.png` | Same crop with 90% alpha baked in | Use in python-pptx, which cannot set picture opacity |
| `bb-bird-mark-deck_white.png` | White tight crop | Corner mark on sanctioned dark content layouts |

Corner-mark geometry on the 10.00" x 5.625" slide: height 0.32", width 0.34" (preserve the 1.06 aspect; the old padded file forced a squish at w=0.40), x=9.34", y=5.05".

### Logo rules

1. **Don't recolor.** Black on light, white on dark. Never teal, never red, never gradient.
2. **Don't stretch, skew, rotate.** Scale uniformly. Bird faces upper-right, always.
3. **Don't add effects.** No drop shadows, glows, outlines, embossing. Flat ink only.
4. **Don't place on busy backgrounds without overlay.** If on a photo, the photo carries a dark overlay heavy enough that the logo reads cleanly.
5. **Reserve clear space** equal to the cap height of the wordmark. No text or graphic enters that zone.

---

## 4. Spacing, Radii, Shadows

### Spacing scale (4px base)

`space-1` 4px, `space-2` 8px, `space-3` 12px, `space-4` 16px, `space-5` 24px, `space-6` 32px, `space-7` 48px, `space-8` 64px, `space-9` 96px.

In PowerPoint inches: 4px ≈ 0.04", 8px ≈ 0.08", 16px ≈ 0.17", 24px ≈ 0.25", 32px ≈ 0.33", 48px ≈ 0.50".

### Radii

- `radius-xs` 2px → tags
- `radius-sm` 4px → buttons
- `radius-md` 6px → chips
- `radius-lg` 10px → **every card-like container** (default for all cards)
- `radius-pill` 999px → pills

**"Card-like" means everything visually card-shaped:** standard white content cards, tinted callout cards (teal-50/red-50), solid color callouts (Layout M), dark emphasis containers (Layout O), stat cards inside dark emphasis strips, roadmap step cards (Layout N), image panels inside slide mockups, the chart panel in Layout A. One radius — 10px — for all of them. No card-like element uses 4px or 6px.

Buttons, pills, tags, list rows (Inputs/Outputs items), icon row containers, and small demo elements keep their smaller radii. Those aren't cards.

In pptxgenjs, use `rectRadius` on `pres.shapes.ROUNDED_RECTANGLE`. Card radius = 0.10".

### Shadows

Restrained. Hairlines, not big drops.
- `shadow-1` `0 1px 2px rgba(0,0,0,0.04)` — hairline, default
- `shadow-2` `0 4px 12px rgba(0,0,0,0.06)` — card lift
- `shadow-3` `0 12px 32px rgba(0,0,0,0.10)` — modals only

For decks: prefer the surface-contrast (FAFAFA page + FFFFFF cards) over shadows. Shadows are usually unnecessary.

---

## 5. Slide Anatomy & Layout Patterns

### Global Structure (every white content slide)

```
y=0.28"  Section number ("01") — Futura 13pt, teal
y=0.55"  Page title — Futura 24pt, black
y=1.10-1.22"  Content area begins
y=5.53"  Bottom accent bar — teal, full width, 0.10" tall
bottom-right Bird mark in corner — ~0.32" tall, opacity ~0.9
```

Left margin (text): **0.45"**
Left margin (card edges): **0.38"**
Right content edge: **~9.55"**
Content area width: **~9.10"**

### Layout A: Image + Text Two-Column (most-used)

The default content slide. Image left, text right.

- Title row at top: page title (24pt Futura Bold)
- Image / chart panel: left ~55% of content area, x=0.45", w≈4.95", aspect 16:9 or 4:3. The panel is card-like — 0.10" radius, 1pt slate-200 outline on light bg, **no top-edge bar**. Charts use the canonical series (teal · slate · black).
- Text: right ~45%, x=5.55", w≈4.00"
  - `ts-header` (Avenir Bold, 18pt, black) at top
  - 2-4 short body paragraphs (Avenir 13pt, slate-800)
  - **Bold key terms** within running prose for emphasis
- Bird mark in bottom-right corner

### Layout B: Two-Column Cards (2x2 Grid)

Used on Executive Summary, capabilities grids.

- Two columns of cards, each 4.45" wide
- Left column at x=0.38", right at x=5.20"
- Two rows: top y=1.22", bottom y=3.22"
- Cards = `FFFFFF` fill, 1pt `E2E8F0` outline, 0.10" radius
- **No top-edge accent bar on cards.** The card stands on its outline alone. (Removed in v2.1 — duplicated the bar+dot signature inside the container.)
- Internal padding ~0.18" from edge to text
- Card title in 14pt Futura Bold uppercase, body in 13pt Avenir

### Layout C: Three-Column Cards (3x2 Grid)

Used on Contents (TOC), Services.
- Three columns, each 3.00" wide at x=0.38", x=3.60", x=6.82"
- Same card styling as B
- Internal text width 2.65-2.70"

### Layout D: Five-Column Cards (Pillars)

Used on Strategic Pillars.
- Five columns, each 1.78" wide, increments of ~1.90"
- Full height cards y=1.10" to y=5.22"
- Narrow text width 1.50"
- **Same card styling as B**: `FFFFFF` fill, 1pt `E2E8F0` outline, 0.10" radius. **No top-edge accent bar on the cards** (v2.1 rule). Use the `addCard` helper.
- Left edge stripe: 0.18" wide teal bar at x=0", full slide height. **This is a slide-edge decoration, not a card decoration** — it lives at the slide edge before the leftmost card begins, not on top of any card.

### Layout E: Inputs / Outputs (Numbered Columns)

Two parallel columns of numbered items, outlined and tinted.

- Two columns at x=0.45" and x=5.20", each ~4.30" wide
- **Inputs (left, teal):** column header in Futura Bold 18pt teal, thin teal underline matching header width below it. Items = teal-50 fill, teal-200 1pt border, teal-500 two-digit number prefix, slate-800 body.
- **Outputs (right, red):** column header in Futura Bold 18pt red-700, thin red underline. Items = red-50 fill, red-200 1pt border, red-500 number prefix, slate-800 body.
- Item rows: ~0.45" tall, 0.06" radius, padded 0.10" vertical, 0.16" horizontal
- 4-6 items per column, ~0.10" gap

### Layout F: Data Table

- Header row: Teal `008C95` fill, white text, Futura Bold 10pt
- Data rows: alternating `FFFFFF` and `F8FAFC` (slate-50)
- Highlighted row: teal-100 (`CFEEF0`) fill, or teal left-edge accent (0.06" wide)
- The key cell gets a teal left-edge accent, bold weight, or teal-100 fill — something that says "this is the point"
- Row height: 0.44"
- Footer: 9pt Avenir, slate-500

### Layout G: Photo Section Divider

- Full-bleed San Francisco nightscape
- Dark overlay to taste (60-75%)
- Large section number: Futura Bold 88pt, teal, left-aligned at x=0.45"
- Section title: Futura Bold 40pt, white
- Subtitle: Avenir 13pt, slate-300, italic

### Layout H: Cover Slide

- Full-bleed nightscape, dark overlay to taste
- Project/client name as headline: Futura Bold 48pt, white, uppercase, letter-spaced, upper-left
- Subtitle: Avenir 15pt, white or slate-300, deck scope
- "Prepared by Blackbird PPC" byline: Avenir 13pt, white/gray, lower-left
- **No logo on cover.** Project name does the work.

### Layout I: Quote / Interstitial

- Solid off-black (`0D0D0D`) background (default for dark emphasis). Slate-500 (`64748B`) is the alternative emphasis surface for warm/structural quote interstitials.
- Centered quote text: Futura 36-44pt, white
- Teal bar+red dot above and below the quote
- "BLACKBIRD PPC" attribution: Futura 11pt, white, letter-spaced

### Layout J: Closing Slide

- Off-black `0D0D0D` background OR full-bleed nightscape with overlay
- "Thank you" centered, Futura Bold 40pt, white
- No logo, no contact info, no URL. Contact details belong in the email.

### Layout K: Numbered Best Practices List

Used on best practices, checklists, ranked recommendations.

- Horizontal rows spanning content width (~9.20"), alternating `FFFFFF` and `F8FAFC` fills, height ~0.55-0.65"
- Left: two-digit number in white inside a teal circle (0.35-0.40"), then a topic icon (line-stroke teal, ~0.32") in a second teal circle OR as a flat teal icon
- Right of icons: title (Futura Bold 11pt, black) + description (Avenir 9pt, slate-700)
- 5 items per slide. For 10+, split with "(cont.)" in subtitle

### Layout L: POD / POP / Optionality Stack

Three-tier strategic positioning. Labels carry color meaning.

- Single column, three stacked items, each separated by a 120px-wide teal underline bar
- Each item:
  - Label (Futura Bold 11pt, uppercase, letter-spaced 0.06em): "POINT OF DIFFERENCE" in teal, "POINT OF PARITY" in slate-500, "OPTIONALITY" in red
  - Headline (Futura Bold 22pt, black)
  - Description (Avenir 13pt, slate-700)
- Each item ~1.4" tall, divider bar between them

### Layout M: Solid Color Callout

Replaces the typical white-card-with-quote pattern.

- Solid teal `008C95` block, full content width or 2/3 width, ~0.80-1.20" tall
- Bold black text on top: Futura Bold 22-24pt, line-height 1.15
- Use once per slide. Never two solid blocks side by side.

### Layout N: Roadmap (Teal-to-Red Gradient)

Process steps in a brand-color spectrum. 3-5 steps only.

- Horizontal sequence of numbered circles connected by a hairline gradient
- Each step has: circle (top), short vertical line, tinted-and-outlined card (bottom)

**Color anchors by step count:**
- 3 steps: teal-500 → `594853` → red-500
- 4 steps: teal-500 → `2D6A74` → `594853` → red-500
- 5 steps: linear interpolation teal-500 → red-500

**Per step:**
- Circle: 0.65" diameter, filled with step color, white two-digit number (Futura Bold 18pt). Number is white regardless of fill.
- Vertical connector: 1.5pt line, color = step color, ~0.36" tall
- Card: tinted+outlined. Background = `{color}-50`, border = `{color}-200` (1.5pt), 0.10" radius, title centered Futura Bold 15pt in `{color}-700`, description centered Avenir 12pt slate-700. **No top-edge accent bar** (per v2.1 rule; tinted cards stand on their tinted border).

**Connector hairline:** 2pt line spanning circle-center to circle-center, gradient fill matching the step colors. Sits behind circles in z-order.

**Roadmap rules:**
- Title carries the conclusion ("Synthesize, interview, iterate, build"), not "Next Steps"
- Order steps left-to-right by time, not priority. Teal = now, red = future.
- Don't use for ranked priorities. Use Layout K or POD/POP/Optionality.
- Don't mix step counts within one deck.
- Centered text inside cards is the only component-scoped exception to left-align.

### Layout O: Dark Emphasis Stat Strip

Used for case studies, key findings, executive callouts. Two emphasis surfaces, both Core anchored: off-black for dark/heavy emphasis (default), slate-500 for warm/structural emphasis.

- Background: off-black `0D0D0D` (default for dark emphasis) or slate-500 `64748B` (warm/structural emphasis surface)
- Eyebrow label: Futura Bold 12pt teal, with a 1.5pt teal underline below (~0.04" tall)
- Title: Futura Bold 32-36pt white, letter-spaced -0.02em
- Subtitle: Avenir 14pt, white-65%-opacity (off-black) or white-80%-opacity (slate-500 — needs more contrast)
- Stat strip: 2-4 cards in a row
  - Card bg: `1C1C1C`/`222222` neutral on off-black (default), or cool slate-800 `1E293B` on off-black (the `dark-card-cool` token — white text, slate-500 @40% border; matches the live-site dark cards), or slate-700 `334155` on a slate-500 ground (the contrast step needed inside the lighter slate emphasis surface)
  - **Radius: 0.10"** (10px — matches every other card in the system per v2.3)
  - **No top-edge teal bar** (per v2.1 "no bars on cards" rule). The big teal stat number carries the brand inside the card.
  - White logo frame at top (16pt padding)
  - Big stat: Futura Bold 56pt teal
  - Stat label: Futura Bold 11pt white, uppercase, letter-spaced
  - Stat detail: Avenir 13pt, white-85%
  - Outcome line: Avenir 13pt italic, teal

---

## 6. Signature Motifs

Five small marks that make a page read as Blackbird.

### 1. Teal Bar + Red Dot
The strongest signature. See Section 1 for full anatomy. Use roughly 1 in 3-4 slides. Below titles, under quotes, as section-end punctuation. Never inside cards. Never twice on one slide.

### 2. Bottom Accent Bar
Full-width teal bar (10.0" x 0.10") at y=5.53" on every white-background content slide. The deck's foundation line. Skipped only on dark slides (where the dark surface is the foundation) and on photo slides.

### 3. Numbered Colored Prefix
Two-digit number in Futura Bold, colored to match meaning:
- **Teal** for inputs, positives, points of difference, "now" steps
- **Red** for outputs, risks, optionality, "future" steps
- **Slate-500** for neutral context

The number carries the color signal so the title text stays plain black/slate.

### 4. Section Header Underline
Bold uppercase headline (Futura Bold 18pt) with a thin matching colored line beneath. Width matches the headline, not the column. Quieter than a tag, louder than nothing. Teal underline for primary sections, red for outputs/risks.

### 5. Teal Bullet Dot
8px filled teal circle. Replaces standard bullet characters. No nested bullets — if you need hierarchy, restructure. In PowerPoint inches, dot = 0.06-0.08" diameter.

---

## 7. Imagery

### Photography

**Subjects:** San Francisco (skyline, urban detail, the bay) and bird imagery (blackbirds, ravens, crows, silhouettes against sky).

**Mood:** Nightscape — dusk, after-dark, atmospheric, low-key.

**Treatment:** Dark overlay to taste; goal is mood, not a fixed opacity. Typically 60-75% black overlay.

**Where:** Cover, section dividers, closing slide.

**Where not:** Content slides, cards, dividers within sections.

**Never:** Generic stock, daylight skylines, abstract gradients, AI-generated cityscapes or birds.

**The library (v3.1):** Twenty-four cleared images at `assets/photography/`: fourteen SF nightscapes (Twin Peaks skyline, Bay Bridge trails / dusk span / light rails / starry-sky / black-and-white from Yerba Buena, downtown blue hour and skyline overview, Bernal light field, Sutro above fog, Golden Gate tower / night fog / city lights, Chinatown) and ten corvids (pair on wire, wings silhouette, branch against storm sky, raven profile, raven portrait, raven in flight, dusk-cloud silhouette, blue-hour silhouette, bare-branch silhouette, blackbird silhouette). Pull covers, dividers, and closings from this folder first. Every file has a license row in `assets/photography/PHOTOS.md`; an image without a manifest row does not ship. One flag: `sf-night-skyline-twinpeaks.jpg` predates v3.0 with an unverified license; confirm or replace it for client-facing work.

### Icons

**Style:** Lucide / Feather, line stroke only. No filled shapes, no dual-tone, no novelty illustrations.

**Color (light bg):**
- **Black `0D0D0D`** is the default — icons read like content and line up next to copy without competing for the eye. Use it unless you have a reason not to.
- **Teal `008C95`** is the opt-in accent for category-marker / hero roles — icons meant to read as accents alongside headlines.
- Pick one color per grid and hold it. Mixed-color icons in a single grid look like a mistake, not a choice.

**Color (dark bg):** White. Always. Teal-on-dark goes muddy; black-on-dark disappears.

**Stroke:** 1.5pt, no fill. Corners are square or barely rounded — no soft consumer shapes.

**Size:** ~32px (~0.32") on slides, ~24px (~0.24") in compact rows. Optical-sized in pairs, never stretched.

**Position:** Top-left of card, or left of row. Aligned to the cap-height of the headline next to them.

**Where not:** Section dividers, quote slides, data tables, cover, closing.

**Consistency:** If one item in a grid has an icon, all do. If one is black, all are black (default); if one is teal, all are teal. One color per grid.

**Container:** Bare on white cards. Optional filled-circle treatment (teal-500 circle with white icon) for hero rows — pick one or the other across the deck, never both in the same deck.

### Implementation in pptxgenjs

Build line-stroke icons from native shapes (lines, ovals, rectangles) with `line` properties only, no fills. Stroke them in black `0D0D0D` by default; switch to the teal accent color only for category-marker / hero grids.

```javascript
// Simple line icon: search (circle + handle line)
function addSearchIcon(slide, pres, x, y, size) {
  // Circle
  slide.addShape(pres.shapes.OVAL, {
    x: x, y: y,
    w: size * 0.6, h: size * 0.6,
    fill: { type: 'none' },
    line: { color: COLORS.TEAL, width: 1.5 },
  });
  // Handle (note: pptxgenjs LINE uses w/h as offsets, not absolute end coords)
  slide.addShape(pres.shapes.LINE, {
    x: x + size * 0.5, y: y + size * 0.5,
    w: size * 0.4, h: size * 0.4,
    line: { color: COLORS.TEAL, width: 1.5 },
  });
}
```

For grids that need icons but want simpler implementation, use a line-stroke teal Unicode character inside an outlined teal circle (1.5pt stroke, no fill). Safe characters: `✓` (check), `→` (arrow), `○` (circle), `+`. Do NOT use emoji codepoints.

---

## 8. Data Presentation

### Three Rules for Data Slides

1. **Title states the finding.** "Marginal CPA is 4x higher than reported above $50K spend" — not "CPA Analysis."
2. **Highlight the key number.** Pull the most important data point into a stat callout (Futura Bold 60-80pt, teal).
3. **Annotate, do not decorate.** Label inflection points directly on charts (Avenir 9pt, teal or slate-700).

Plus: **ask if every number pushes the narrative.** Five stats on one slide make four of them noise.

### Data Callout Pattern

```
[Large stat]      [Context paragraph]
 80pt teal         13pt Avenir, slate-800
 Futura Bold       2-3 sentences explaining
                   what the number means
```

Position callout left (x=0.45", w~3.5") and context right (x=4.5", w~5.0"). Or stack: callout above, context below.

**Stat strip on emphasis surface** (case studies, see Layout O): 2-4 cards on off-black (dark emphasis, default) or slate-500 (warm/structural emphasis), big teal stat, white label, italic teal outcome line.

### Chart Color Mapping

- Primary data series: Teal `008C95`
- Secondary/comparison series: Slate-500 `64748B`
- Tertiary: Black `000000`
- Benchmark or threshold line: Black `000000`, dashed
- Alert/outlier highlight: Red `862633` (sparingly)
- Background/gridlines: `F8FAFC` (slate-50) or transparent

### Horizontal Bar Charts Inside Cards

For distributions, rankings, share-of-voice. Shape-based bars, not chart objects.

- Each row: label (Avenir 9pt, black) + teal rectangle (width proportional to value, height 0.15-0.18") + value text (Avenir 9pt, slate-700)
- Row spacing ~0.30", max bar width ~3.5" inside a half-width card
- Place inside a standard white card (slate-200 outline, no top bar). Pairs well with a stat callout to the left.

### Table Best Practices

- Header row: Teal `008C95` fill, white text, Futura Bold 10pt
- Data rows: alternating `FFFFFF` and `F8FAFC` fills
- The key row/cell gets a teal left-edge accent (0.06" wide), bold weight, OR a teal-100 fill — pick one
- Footnotes: 9pt Avenir, slate-500

---

## 9. Voice & Tone for Slide Copy

The visual system is set by Section 1-8. The voice that fills it draws directly from Section 0 (Identity).

### Principles

1. **Direct, not promotional.** State what Blackbird does and what it means. No superlatives or hype ("revolutionary", "world-class", "cutting-edge", "best-in-class", "passionate").
2. **Precise.** Name specific methods (MMM, incrementality, holdout testing, marginal return analysis) rather than vague capabilities. Specificity is credibility.
3. **Declarative sentences.** "We do X" not "We can help you with X."
4. **No exclamation marks.** Ever.
5. **Numbers over adjectives.** "NPS of 90" not "highly rated."
6. **Truth-seeking.** This is the Intellectual Honesty pillar at sentence level. If the data complicates the story, the slide says so.

### Voice — Do

- "We do not hide behind dashboards."
- "We tell the truth about what is working and show the math behind it."
- "Holdout testing revealed 98% of attributed conversions were organic."
- "Four inputs determine whether AI cites your brand."
- "Pride in the craft of advertising."

### Voice — Don't

- "We're passionate about driving results."
- "Best-in-class solutions for modern marketers."
- "Revolutionary new approach to paid media."
- "We help unlock the full potential of your marketing."
- "Game-changing performance."

### Slide Titles Carry the Point

Titles state the slide's conclusion, not the topic. A reader who only scans titles should understand the deck's argument.

- Good: "Four inputs determine whether AI cites your brand"
- Good: "Holdout testing revealed 98% of attributed conversions were organic"
- Bad: "AI Citation Overview"
- Bad: "Test Results"

Categorical slides (TOC, divider, roster) can use topic-label titles. Two-line titles are fine if needed for clarity.

### Pillar Vocabulary

When writing capabilities, services, or executive-summary copy, draw terms from the six pillars (Section 0). The active vocabulary set:

| Concept | Use these terms |
|---------|-----------------|
| What we do | Performance marketing, paid media, advertising. Not "growth marketing", not "demand gen". |
| How we measure | MMM, multi-touch attribution, incrementality testing, holdout tests, on/off tests, marginal CPA, marginal ROI, first-party data. |
| What we deliver | Pipeline, revenue, lead efficiency. Not "leads", not "conversions" alone. |
| What we are | Stewards. Craft-driven. Honest about measurement. Not "partners", not "experts", not "ninjas". |

---

## 10. Deck Structure

```
Cover (H, no logo)
> TOC (B + horizontal logo right-center)
> Section Divider (G)
> Content slides (A-F, K-N as needed)
> Dark Emphasis (O) every 3-5 slides
> Quote Interstitial (I, optional)
> Closing (J, "Thank you" only)
```

Section numbers: "01" through N, two-digit. Appears on divider slide (88pt), content slide top-left (13pt), and TOC cards.

Bird mark in bottom-right corner of every content slide. Skipped on cover, dividers, quote interstitials, and closing.

---

## 11. Implementation Notes (pptxgenjs)

### Color Constants

```javascript
const COLORS = {
  // Core six (surface, teal, slate-500, red, black, dark-slate 1E293B)
  SURFACE:    'FAFAFA',   // off-white page
  WHITE:      'FFFFFF',   // pure white, cards on top of surface
  BLACK:      '000000',   // headlines
  TEAL:       '008C95',   // brand accent
  SLATE:      '64748B',   // structural spine (not a brand color)
  RED:        '862633',   // signal

  // Teal scale
  TEAL_50:    'ECF7F8',
  TEAL_100:   'CFEEF0',
  TEAL_200:   'A0DCE0',
  TEAL_300:   '6EC6CB',
  TEAL_400:   '36AAB1',
  TEAL_500:   '008C95',
  TEAL_600:   '007078',
  TEAL_700:   '00565D',
  TEAL_800:   '003E43',
  TEAL_900:   '00282C',
  TEAL_950:   '001316',

  // Red scale
  RED_50:     'F8E9EC',
  RED_100:    'EFC9CF',
  RED_200:    'DD9AA3',
  RED_500:    '862633',
  RED_700:    '561821',

  // Slate scale (cool, structural spine)
  SLATE_50:   'F8FAFC',
  SLATE_100:  'F1F5F9',
  SLATE_200:  'E2E8F0',   // card outline default
  SLATE_300:  'CBD5E1',
  SLATE_400:  '94A3B8',
  SLATE_500:  '64748B',
  SLATE_600:  '475569',
  SLATE_700:  '334155',   // body secondary, slate-toned dark
  SLATE_800:  '1E293B',   // slate-800 — body text on light + primitive; as a dark-card use DARK_CARD_COOL (same hex)
  SLATE_900:  '0F172A',
  SLATE_950:  '000000',

  // Dark surfaces
  DARK_BG:        '0D0D0D',   // off-black — the dark SECTION ground (never pure black 000000)
  DARK_CARD1:     '1C1C1C',   // neutral card on off-black
  DARK_CARD2:     '222222',   // neutral card on off-black (alt)
  DARK_CARD_COOL: '1E293B',   // slate-800 — sanctioned cool dark-card (v2.6), white text, never a section ground
  DARK_ROW:       '2A2A2A',
  DARK_LINE:      '333333',

  // Text
  TEXT_DEFAULT:   '000000',   // headlines on white
  TEXT_BODY:      '1E293B',   // body on white (slate-800)
  TEXT_SECONDARY: '334155',   // slate-700
  TEXT_MUTED:     '64748B',   // slate-500
  TEXT_FAINT:     '94A3B8',   // slate-400
  TEXT_INVERSE:   'FFFFFF',

  // Roadmap interpolation anchors (4-step)
  ROADMAP_2:  '2D6A74',
  ROADMAP_3:  '594853',
};
```

### Font Constants

```javascript
const FONT_HEADLINE = 'Futura';   // Mac. Win: embed Futura, fallback 'Bahnschrift' or 'Trebuchet MS'
const FONT_BODY = 'Avenir';       // Mac. Win: embed Avenir, fallback 'Calibri'
```

### Reusable Helpers

```javascript
// Slide background — off-white surface
// Note: pptxgenjs ≥3.10 supports `{ color }`. On older versions use `{ fill: 'FAFAFA' }`.
function setSlideBackground(slide) {
  slide.background = { color: COLORS.SURFACE };  // FAFAFA
}

// Bottom accent bar (every white-bg content slide)
function addBottomBar(slide, pres) {
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 5.53, w: 10.0, h: 0.10,
    fill: { color: COLORS.TEAL },
  });
}

// Section number + page title header
function addSectionHeader(slide, number, title) {
  slide.addText(number, {
    x: 0.45, y: 0.28, w: 1.0, h: 0.30,
    fontFace: FONT_HEADLINE, fontSize: 13,
    color: COLORS.TEAL, bold: true, margin: 0,
  });
  slide.addText(title, {
    x: 0.45, y: 0.55, w: 8.50, h: 0.50,
    fontFace: FONT_HEADLINE, fontSize: 24,
    color: COLORS.BLACK, bold: true, margin: 0,
  });
}

// Bird mark in bottom-right corner (every content slide)
// v3.0: use the canonical tight crop. The old padded 1148x774 file at w=0.40
// both squished the mark (true aspect is 1.06, not 1.25) and rendered the
// visible bird smaller than spec because of canvas padding.
function addBirdMarkCorner(slide, pres) {
  slide.addImage({
    path: "assets/bb-bird-mark-deck.png",
    x: 9.34, y: 5.05, w: 0.34, h: 0.32,
    transparency: 10,  // pptxgenjs supports 0-100 on addImage
  });
}

// Card on FAFAFA surface — white fill, slate-200 outline, 10px radius.
// NO top-edge bar (v2.1 rule: no bars on cards, ever). The card stands on its outline alone.
function addCard(slide, pres, x, y, w, h) {
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w, h,
    fill: { color: COLORS.WHITE },
    line: { color: COLORS.SLATE_200, width: 1 },
    rectRadius: 0.10,
  });
}

// Tinted card variant — for teal-50 / red-50 callout cards (use sparingly, only when meaning calls for it).
// Tinted cards skip the slate-200 outline in favor of matching tinted borders.
function addTintedCard(slide, pres, x, y, w, h, variant) {
  // variant: 'teal' | 'red'
  const fills  = { teal: COLORS.TEAL_50,  red: COLORS.RED_50  };
  const lines  = { teal: COLORS.TEAL_200, red: COLORS.RED_200 };
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w, h,
    fill: { color: fills[variant] },
    line: { color: lines[variant], width: 1 },
    rectRadius: 0.10,
  });
}

// Tinted+outlined item row (Inputs/Outputs pattern)
function addTintedItem(slide, pres, x, y, w, h, variant, number, label) {
  // variant: 'teal' | 'red'
  const fills = { teal: COLORS.TEAL_50,  red: COLORS.RED_50  };
  const lines = { teal: COLORS.TEAL_200, red: COLORS.RED_200 };
  const nums  = { teal: COLORS.TEAL_500, red: COLORS.RED_500 };

  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w, h,
    fill: { color: fills[variant] },
    line: { color: lines[variant], width: 1.5 },
    rectRadius: 0.06,
  });
  slide.addText(number, {
    x: x + 0.15, y: y, w: 0.40, h: h,
    fontFace: FONT_HEADLINE, fontSize: 14, bold: true,
    color: nums[variant], align: 'left', valign: 'middle',
  });
  slide.addText(label, {
    x: x + 0.60, y: y, w: w - 0.75, h: h,
    fontFace: FONT_BODY, fontSize: 13,
    color: COLORS.TEXT_BODY, align: 'left', valign: 'middle',
  });
}

// Teal bullet dot
function addBulletDot(slide, pres, x, y) {
  slide.addShape(pres.shapes.OVAL, {
    x, y, w: 0.07, h: 0.07,
    fill: { color: COLORS.TEAL },
    line: { width: 0 },
  });
}

// Teal bar + red dot signature
function addTealBarRedDot(slide, pres, x, y, barWidth) {
  slide.addShape(pres.shapes.RECTANGLE, {
    x, y, w: barWidth, h: 0.055,
    fill: { color: COLORS.TEAL }, line: { width: 0 },
  });
  const dotSize = 0.13;
  slide.addShape(pres.shapes.OVAL, {
    x: x + barWidth + 0.03,
    y: y + 0.055 / 2 - dotSize / 2,
    w: dotSize, h: dotSize,
    fill: { color: COLORS.RED }, line: { width: 0 },
  });
}

// Section header underline (motif 4)
function addSectionUnderline(slide, pres, x, y, headlineText, variant) {
  // variant: 'teal' (default) | 'red'
  const color = variant === 'red' ? COLORS.RED_500 : COLORS.TEAL_500;
  slide.addText(headlineText, {
    x, y, w: 5.0, h: 0.32,
    fontFace: FONT_HEADLINE, fontSize: 18, bold: true,
    color: color, align: 'left',
    charSpacing: 100,  // pptxgenjs uses 1/100 pt; 100 ≈ 1pt of letter-spacing
  });
  // Underline matches the headline width approximately
  const underlineWidth = Math.min(headlineText.length * 0.10, 1.5);
  slide.addShape(pres.shapes.RECTANGLE, {
    x, y: y + 0.34, w: underlineWidth, h: 0.025,
    fill: { color: color }, line: { width: 0 },
  });
}

// Solid color callout (Layout M) — rounded to 0.10" per v2.3 (all card-like containers = 10px)
function addSolidCallout(slide, pres, x, y, w, h, text) {
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w, h,
    fill: { color: COLORS.TEAL },
    line: { width: 0 },
    rectRadius: 0.10,
  });
  slide.addText(text, {
    x: x + 0.25, y, w: w - 0.50, h,
    fontFace: FONT_HEADLINE, fontSize: 22, bold: true,
    color: COLORS.BLACK, align: 'left', valign: 'middle',
  });
}

// Roadmap step circle + card
function addRoadmapStep(slide, pres, x, yCircle, stepNum, fillColor, title, desc) {
  const circleSize = 0.65;
  // Circle
  slide.addShape(pres.shapes.OVAL, {
    x, y: yCircle, w: circleSize, h: circleSize,
    fill: { color: fillColor }, line: { width: 0 },
  });
  slide.addText(stepNum, {
    x, y: yCircle, w: circleSize, h: circleSize,
    fontFace: FONT_HEADLINE, fontSize: 18, bold: true,
    color: COLORS.WHITE, align: 'center', valign: 'middle',
  });
  // Vertical connector
  slide.addShape(pres.shapes.LINE, {
    x: x + circleSize / 2, y: yCircle + circleSize,
    w: 0, h: 0.36,
    line: { color: fillColor, width: 1.5 },
  });
  // Card: tinted + outlined matching color (use 50/200/700 of the same hue)
  // Simplified: caller supplies tint/border/title colors via fillColor mapping
}
```

### Roadmap step color tables

For 3-5 step roadmaps, anchor colors:

```javascript
const ROADMAP_3 = ['008C95', '594853', '862633'];
const ROADMAP_4 = ['008C95', '2D6A74', '594853', '862633'];
// 5 steps: linear interpolate teal-500 -> red-500
```

For each step, the card uses:
- Step 1 (teal anchor): bg `ECF7F8`, border `A0DCE0`, title `00565D`
- Step 4 (red anchor): bg `F8E9EC`, border `DD9AA3`, title `561821`
- Intermediate steps: tint/border/title at proportional steps along the same scale

---

## 11b. Implementation Notes (python-pptx)

Decks generated in Claude/Cowork environments are built with python-pptx, not pptxgenjs. The constants below mirror Section 11. The slide is 10.00" x 5.625" (16:9).

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

TEAL      = RGBColor(0x00, 0x8C, 0x95)
RED       = RGBColor(0x86, 0x26, 0x33)
SLATE_500 = RGBColor(0x64, 0x74, 0x8B)
SLATE_200 = RGBColor(0xE2, 0xE8, 0xF0)
BLACK     = RGBColor(0x00, 0x00, 0x00)
SLATE_800 = RGBColor(0x1E, 0x29, 0x3B)
OFF_BLACK = RGBColor(0x0D, 0x0D, 0x0D)
SURFACE   = RGBColor(0xFA, 0xFA, 0xFA)

SLIDE_W, SLIDE_H = Inches(10.0), Inches(5.625)

def add_bird_mark_corner(slide):
    """Bird mark, bottom-right of every content slide.
    Skipped on cover, dividers, quote interstitials, and closing.
    python-pptx cannot set picture transparency, so the asset itself
    carries the 90% alpha (bb-bird-mark-deck-faded.png)."""
    slide.shapes.add_picture(
        "assets/bb-bird-mark-deck-faded.png",
        left=Inches(9.34), top=Inches(5.05), height=Inches(0.32),
    )  # width follows the 1.06 aspect automatically: ~0.34"

def add_bottom_accent_bar(slide):
    """Full-width teal bar, 0.10\" tall, on every white content slide."""
    bar = slide.shapes.add_shape(1, Inches(0), Inches(5.525), SLIDE_W, Inches(0.10))
    bar.fill.solid(); bar.fill.fore_color.rgb = TEAL
    bar.line.fill.background()

def add_toc_lockup(slide):
    """Horizontal lockup, right-center, ~2.5\" wide. TOC only."""
    slide.shapes.add_picture(
        "assets/bb-horizontal-lockup.png",
        left=Inches(6.6), top=Inches(2.33), width=Inches(2.5),
    )
```

Asset paths resolve relative to the skill folder, which bundles `assets/` next to `SKILL.md`. When running from the repo instead, prefix with `assets/logos/`.

---

## 12. Rules

### System rules

1. **Off-white carries the surface.** 50-55% of slide area is `FAFAFA`. Pure white is for cards on top.
2. **Reference semantic intent, not just hex.** The semantic intent (brand-accent, signal, slate-structural) is the contract. Pick the closest semantic role first; the hex follows from that.
3. **Don't hardcode a seventh hex.** If you reach for a color outside the system, ask whether it earned its place. Almost always no.
4. **Teal as primary accent, not punctuation.** 12-15% of any view. Surfaces, fills, links, CTAs, dividers.
5. **Red is a full co-accent, not signal-only.** 12-18% per deck. Counterweight to teal — headlines, secondary CTAs, output/risk columns, key stats, pull quotes, hairline accents on dark surfaces, critical callouts. Sanctioned as a text color (red-500 on FAFAFA is ~8.3:1, AA at any size). Avoid red as a full content background or in long runs of solid fill/body copy.
6. **Don't add gradients or saturated extras.** Flat color. The roadmap connector is the only sanctioned gradient.
7. **Don't use filled containers for content.** No pastel cards. Containers are outlined+tinted (teal-50/red-50 with matching border) or absent.
8. **No top-edge bars on cards. Ever.** Cards stand on their outline, not on a colored bar. The bottom-of-slide accent and the bar+dot signature are the only sanctioned horizontal bars in the system. A teal bar across the top of a card duplicates one of those signatures inside a container.
9. **Slate outline is for white cards specifically.** 1pt slate-200 (`E2E8F0`) on `FFFFFF` cards over `FAFAFA` surface. Tinted cards (teal-50, red-50) use matching teal-200 or red-200 borders. Dark cards skip the outline.
10. **Bar+dot motif: max once per slide.** Maximum one. Roughly 1 in 3-4 slides. Two on one slide reads as pattern, not punctuation.
11. **Color the numbered prefix to match meaning.** Teal = inputs/positives/POD. Red = outputs/risks/optionality. Slate-500 = neutral.
12. **Don't add decorative lines under headlines.** Hallmark of generic AI slides. Use whitespace. Two motif exceptions: teal bar+red dot, and section-header underline matching headline width.
13. **Drop into an emphasis section every 3-5 slides.** Two anchored options: off-black `0D0D0D` for dark/heavy emphasis (default), slate-500 `64748B` for warm/structural emphasis (medium cool-gray, not "dark"). Both are Core anchors. Pick by the feeling you want.
14. **Slate is the structural spine, not a brand color.** Teal and red are the only brand colors. Slate carries structure (tertiary CTAs, icon strokes, dividers, captions, the warm emphasis ground) and should recede, not compete for identity.
15. **Icons: pick one color per grid.** Teal for accent/category-marker roles. Black for content-role icons that line up next to body copy. Never mixed in a single grid.
16. **Vary the rhythm of every list.** Mix fonts, weights, color, bullet styles. A good content slide has 2-3 different formats. A bad one has eight identical rows.
17. **Don't bullet every line.** Two consecutive bullet lists on one slide is a smell. Rewrite one as prose, callout, stat strip, or icon row.

### Slide composition rules

1. **Let images carry the message when they can.** A full-bleed photo with no text overlay is a valid slide if the image makes the point. Don't add text to "balance" the slide.
2. **Title is the message, not the topic.** "Marginal CPA is 4x higher above $50K spend" not "CPA Analysis."
3. **Direct the eye in tables.** The key cell gets a teal left-edge accent, bold weight, or teal-100 fill. If nothing is highlighted, the audience doesn't know why the table is there.
4. **Every number must push the narrative.** Five stats on one slide make four of them noise. Selectivity is rigor.

### Roadmap rules

Roadmap (Layout N) is a worked example, not a chapter. The full spec lives in Section 5 Layout N. Three rules:
1. **Title with the conclusion**, not "Next Steps." "Synthesize, interview, iterate, build" tells the audience what they're seeing.
2. **Order steps left-to-right by time.** Teal = now, red = later. Not for ranked priorities (use Layout K or POD/POP/Optionality).
3. **Same step count across the deck.** If two roadmap slides share a deck, both have the same step count and color anchors.

---

## 13. Pre-Ship Checklist

Final-pass review. Walk every slide top-to-bottom against this list before the deck leaves your hands. Most brand drift is caught here, not in early drafts.

| Check | What to verify |
|-------|-----------------|
| **Color budget** | Each slide reads as ~50-55% surface, 12-15% teal, 12-18% red, 12-15% slate, 5-7% black, 5-8% dark slate. No seventh hex. |
| **Cards** | No top-edge bars. White cards have a slate-200 outline; tinted cards use matching teal-200 or red-200 borders. |
| **Bar + dot motif** | Maximum one per slide. Roughly 1 in 3-4 slides across the deck. Never inside a container. |
| **Titles** | Each carries the conclusion, not the topic. Scan-only readers should follow the argument. |
| **Images** | Check every image for stretching, squishing, or skew. Aspect ratios preserved. Spacing around images consistent slide-to-slide. No image touches a slide edge unless it's a full-bleed cover or divider. |
| **Spacing** | Margins consistent across slides. Card padding matches the spec. No element jammed against another or floating in dead space. |
| **Icons** | One color per grid — either all teal or all black. Line stroke only, 1.5px, no fill. If one card has an icon, all cards in that grid have icons. |
| **Dark rhythm** | One dark slide every 3-5 slides. Section ground is off-black `0D0D0D` by default (Core Five anchor) or slate-500 `64748B` for warm emphasis — never pure black `000000`, never slate-800 `1E293B`. Dark cards may be neutral `1C1C1C`/`222222` or cool slate-800 `1E293B`. |
| **Fonts** | Futura and Avenir embedded in shared .pptx files. Cross-platform fallbacks set. |
| **Logo placement** | Bird mark in bottom-right of every content slide. No logo on cover or closing. Horizontal lockup reserved for TOC. |
| **Numbers** | Every stat advances the argument. Cut interesting-but-irrelevant. Sources cited where claimed. |
| **Voice** | No hype words ("revolutionary", "best-in-class", "passionate"). Declarative sentences. No exclamation marks. |

---

## 14. Common Mistakes to Avoid

1. **Using pure white `FFFFFF` as the page surface.** The page is `FAFAFA`. Pure white is for cards on top.
2. **Pastel cards (Blush, Mint, Cream, Ice).** Dead pattern from v1. Use white cards with slate-200 outline, or outlined+tinted teal-50/red-50 when meaning calls for it.
3. **Stone Gray `D7D2CB`.** Replaced by the slate scale. Use slate-200 for borders/dividers, slate-500 for the structural spine.
4. **Using pure black `000000` or slate-800 `1E293B` as a section ground.** The two section grounds are off-black `0D0D0D` (dark/heavy) and slate-500 `64748B` (warm/structural). Pure black is text/UI only — never a full-bleed surface. Slate-800 is valid only as the cool dark-*card* (`dark-card-cool`, white text) sitting on a dark ground; it is never the ground itself. Slate-700 stays a text/accent token. (History: v2.0 made slate-800 the default dark ground, v2.2 demoted it, v2.5 removed it from all surfaces, v2.6 restored it for cards only — never grounds.)
5. **Bullet-heavy slides.** Use cards, grids, structured layouts. If bullets are needed, use teal dots and mix with prose.
6. **Hype copy.** "Revolutionary", "game-changing", "best-in-class", "passionate", "world-class" are not in Blackbird's vocabulary.
7. **Accent lines under titles.** Hallmark of AI-generated slides. Use whitespace. Allowed exceptions: bar+dot signature, section-header underline matching headline width.
8. **Same-color card grids.** Adjacent cards should differ — but with the new system, the answer is usually NOT pastel rotation. Use the white-on-FAFAFA card with no top bar. Variation comes from icon, content, and headline color, not card fill.
9. **Top-edge teal bars on cards.** Removed in v2.1. Cards stand on their outline alone — the colored bar duplicates the bar+dot signature inside a container. Applies to all card layouts (B, D, O stat cards, etc.).
10. **Two bar+dot motifs on one slide.** Maximum one per slide. The second one weakens the first.
11. **Teal outline on a teal-tinted card.** Tinted cards (teal-50 background) use teal-200 borders, not slate-200. Match the tint family. Same for red.
12. **Mixed-color icons in a grid.** If one icon is teal and another is black in the same grid, it looks like a mistake. Pick one color per grid.
13. **Card-like containers with non-10px radii.** Every visually card-shaped element — stat cards, callouts (teal-50/red-50 and solid), dark emphasis containers, roadmap step cards, image panels in slide mockups — uses 0.10" radius. Don't use 4px or 6px on anything card-like. The eye registers radius inconsistencies as carelessness before it registers them as variety.
14. **Logo on cover or closing.** Cover and closing carry no logo. TOC carries the horizontal lockup. Every other content slide carries the bird mark in the bottom-right corner.
15. **Filling chart with multiple colors.** Three series max: Teal, Slate, Black. More series = data density problem.
16. **Skipping font embed when sharing.** Always embed Futura and Avenir in shared `.pptx` files. ~200KB cost.
17. **Two solid color callouts on one slide.** Use Layout M once per slide max.
18. **Roadmap with 6+ steps.** 3-5 only. More is a checklist (Layout K), not a roadmap.

---

## Changelog

**v3.1 (June 2026)** — red co-accent + text role, black icons, bigger photo library
- **Red is now a full co-accent (12-18%) and a sanctioned text color.** Red `862633` on `FAFAFA` is ~8.3:1, passing WCAG AA at any size, so red is legal for headlines, eyebrows, key stats, and pull quotes. The old "second accent, 8-10%, avoid long runs" framing is replaced: red can carry more of the page. The one guardrail that stays: not for long body runs, and never a full content background. The bar+dot signature is unchanged.
- **Icons default to black.** Line icons now stroke in off-black `0D0D0D` by default on light grounds; teal is an opt-in accent stroke, not the default. Icons read as content, not decoration. New icons added to the set (growth, trends, insight, velocity, performance, audience, message, trust, budget).
- **Photography library grown to 24 cleared images** (14 SF nightscapes, 10 corvids), each with a `PHOTOS.md` manifest row. Nightscape-only rule unchanged: dusk/after-dark/atmospheric/low-key, no daylight, no AI-generated.

**v3.0 (June 2026)** — assets shipped, single system version
- **Single system version.** The repo `VERSION` file (3.0.0) now governs both the styleguide (`index.html`) and this skill. The two-number era (site v2.1, skill v2.8) ends here; CI fails the build if either artifact drops the shared version.
- **Logo pack shipped.** `assets/logos/` carries all six lockups recovered at source quality, plus deck-ready crops: `bb-bird-mark-deck.png` (tight 633x597 crop, aspect 1.06) and `bb-bird-mark-deck-faded.png` (90% alpha baked in for python-pptx). The skill folder bundles the same files, so deck generation no longer depends on the repo or the network.
- **Corner-mark geometry corrected.** The old helper forced the padded 1148x774 file into a 0.40 x 0.32 box: a 1.25 aspect on a 1.48 canvas holding a 1.06 mark, which both squished the file and rendered the visible bird under spec size. New geometry: 0.34 x 0.32 at x=9.34, y=5.05.
- **Photography library shipped.** Fourteen cleared images at `assets/photography/` (nine SF nightscapes, five corvids) with a per-file license manifest (`PHOTOS.md`). Covers, dividers, and closings pull from the library first. The pre-v3.0 Twin Peaks hero is flagged license-unverified.
- **python-pptx appendix added (Section 11b)** with color constants, corner-mark, bottom-bar, and TOC-lockup helpers matching the pptxgenjs notes.
- File renamed `powerpoint-brand-skill-v2.8.md` to `powerpoint-brand-skill.md`; the version lives in the document and `VERSION`, not the filename.

**v2.8 (June 2026)** — slate relabeled: structure, not brand
- **Only teal and red are brand colors.** Slate `64748B` (and its dark sibling `1E293B`) are structure/ink, not brand colors. Core Six membership is unchanged; the labels got honest: 2 brand (teal, red) + surface (`FAFAFA`) + structure/ink (slate, black, dark slate), with off-black `0D0D0D` the dark ground.
- Rationale: `64748B` is Tailwind's slate-500, the web's default neutral. It is load-bearing (dividers, captions, icon strokes, the warm emphasis surface) but carries no ownable identity. Calling it a "brand color" invited it to lead; "structure" tells it to recede, which is right for a mid-gray.
- Updated: Core Six table, the new brand-vs-structure note, Slate Scale heading, Color Rule 4, System Rule 14, Common Mistake 3, `COLORS` comments. No hex changed, no color removed.
- Cites Design System v2.1 (the HTML was bumped to v2.1 for the same relabel). All three artifacts aligned: skill v2.8, design-system HTML v2.1.

**v2.7 (June 2026)** — Core Five → Core Six
- **Dark Slate `1E293B` promoted to the sixth Core anchor** (founder call). It now sits in the carries-90% palette alongside surface, teal, red, slate-500, and black. Same hex as the v2.6 `dark-card-cool` token and the body-text color — now elevated to anchor tier.
- **Black vs Dark Slate rule added** (the rule that keeps six colors from blurring): Black `000000` = display/punch (headlines, section titles, big stat numbers, max-contrast marks, small solid UI, bird mark) — never long body runs, never a surface. Dark Slate `1E293B` = reading/cool-dark (body copy, table text where pure black glares; the cool dark-card on a dark ground, white text) — never a section ground. Quick test: headline → black; sentence you read → dark slate; flat dark area → off-black `0D0D0D`.
- **Deck budget rebalanced to ~100% across six:** surface 50-55, teal 12-15, red 8-10, slate 12-15 (was 15-18), black 5-7 (was 7-10), dark slate 5-8 (new).
- "A sixth hex must earn its place" → "a seventh hex." Updated the Quick Reference, Color Rules, Layout O, System Rules, Pre-Ship Checklist color-budget row, and the `COLORS` comment to the six-anchor framing.
- Off-black `0D0D0D` remains the dark section ground (not an entry in the six-ink palette table, same as before); dark slate is never a ground. No change to the v2.6 ground/card decision.
- Cites Design System **v2.0** (bumped from v1.9 to carry the Core Six into the HTML).

**v2.6 (June 2026)** — three-way reconciliation (skill ↔ design-system HTML ↔ live site)
- **Settled the dark-surface question after auditing all three artifacts.** The two written specs already agreed (off-black `0D0D0D` ground). The live site (blackbirdppc.com) was the outlier: measured computed styles showed dark sections painted **pure black `000000`** (Squarespace "Black (bold)" color theme) with **slate-800 `1E293B` cards**, and off-black used nowhere. (A prior note claiming the site used navy `0F172A` was wrong — zero navy measured in production.)
- **Decision: hybrid.** Keep off-black `0D0D0D` as the only dark section ground; keep pure black `000000` out of surfaces entirely (text/UI only); **sanction slate-800 `1E293B` as the cool dark-card token** (`dark-card-cool`) so the site's dark cards become legal without blessing pure-black grounds. This reverses *only the card half* of v2.5's slate-800 removal; slate-800 is still never a section ground.
- New token `dark-card-cool` (`1E293B`) added to the Dark Surface Set table and the `COLORS` object. White text, slate-500 `64748B` @ ~40% border, 10px radius. Contrast checked: white-on-slate-800 = 14.6:1; the card sits 1.33:1 above off-black (more separation than neutral `1C1C1C` at 1.14:1).
- Fixed two stale v2.5 contradictions: the Alternating Rhythm "Slate-800 variant" full-slide bullet and the Pre-Ship Checklist "slate-800 only when off-black feels too heavy" line both implied a slate-800 *ground*. Rewritten to the slate-500 emphasis ground + slate-800 *card*.
- Common Mistake #4 reframed from "slate-700/-800 as a surface" to "pure black or slate-800 as a section *ground*."
- Layout O stat cards now list the cool slate-800 card option explicitly.
- **Version alignment.** Design-system HTML reconciled to a single label **v1.9** (it had carried `<title>` v0.1 / header v1.4 while this skill cited a phantom v1.8). All three artifacts now reference v1.9 / v2.6.
- Companion site change (delivered as paste-ready CSS, applied by Jay): dark section ground `000000` → `0D0D0D` scoped to `[data-section-theme="black-bold"]`; `.bb-card` text color corrected from an inherited `0D0D0D` (1.33:1, invisible) to white.

**v2.5 (May 2026)**
- **Slate-800 removed as a surface entirely.** v2.2 demoted it from "default dark" to "softer variant"; v2.5 removes it from the active system. The new framing: two anchored emphasis surfaces, both Core Five — off-black `0D0D0D` for dark/heavy emphasis (default), slate-500 `64748B` for warm/structural emphasis (medium cool-gray, not "dark").
- `--color-surface-slate-dark` now resolves to slate-500 in the design system. The slate variant of dark-emphasis sections renders as the slate brand color, not as slate-700.
- Layout O: stat-card backgrounds on the slate emphasis surface are now slate-700 (`334155`) instead of slate-900 — needed because slate-500 is a much lighter surface than off-black; slate-900 inner cards would have too little contrast against slate-500.
- Common Mistake #4 reframed: "Using slate-700 or slate-800 as a surface."
- Slate-700 (`334155`) and slate-800 (`1E293B`) remain in the primitive scale for color math / inner card contrast, but are no longer used for any surface in the active system.
- Reasoning: anchoring strictly on the Core Five. Slate-500 IS the slate brand color; using slate-500 directly as a surface is more honest than using an interpolated shade.

**v2.4 (May 2026)**
- **Closed all gaps in the "no top-edge bars on cards" rule.** Previously only Layouts B, C (by reference to B), and O explicitly stated the no-bar rule. v2.4 makes it explicit on every card-using layout:
  - **Layout A (Image + Text):** image/chart panel now explicitly card-like — 0.10" radius, slate-200 outline on light bg, no top-edge bar.
  - **Layout D (Pillars):** added "Same card styling as B" reference plus explicit no-top-bar note. Clarified that the slide-edge teal stripe is a *slide* decoration at x=0, not a per-card decoration. This was the source of the pillar cards rendering with top bars in earlier output.
  - **Layout N (Roadmap):** roadmap step cards (tinted+outlined) now explicitly say "No top-edge accent bar — tinted cards stand on their tinted border."
- Border audit confirmed: only cards and tinted list rows get borders. Buttons (primary/dark/signal), pills, tags, solid callouts, section bars, bullet dots, roadmap circles all have `line: { width: 0 }`. The skill does NOT add small borders to all objects.

**v2.3 (May 2026)**
- **Card radius enforced at 10px across the board.** Every card-like container — stat cards, callouts (teal-50/red-50 and solid), dark emphasis sections, roadmap step cards, image panels — uses 0.10" radius. The Radii section now explicitly enumerates which elements are "card-like" and which aren't.
- `addSolidCallout` helper converted from `RECTANGLE` to `ROUNDED_RECTANGLE` with `rectRadius: 0.10`.
- Layout O stat cards now spec the 0.10" radius explicitly (was implicit).
- New Common Mistake #13: "Card-like containers with non-10px radii."
- Companion design-system change (HTML): removed the decorative teal→slate→red gradient bar under section numbers — it violated the "no gradients" rule (only the roadmap connector is a sanctioned gradient). No skill change needed for this; the rule was already correct.

**v2.2 (May 2026)**
- **Rebalanced on the Core Five.** The full-saturation values that carry the brand are exactly five: Surface `FAFAFA`, Brand Accent `008C95`, Signal `862633`, Slate `64748B`, Dark Surface `0D0D0D`. Interpolated tones (slate-700, slate-800) are supporting variants, not anchors.
- **Default dark surface reverted to off-black `0D0D0D`** (the Core Five Dark Surface anchor). Slate-800 (`1E293B`) is demoted from "default dark" (a v2.0 decision) back to a softer variant — used sparingly when off-black feels too heavy for a specific slide.
- Updated across all touchpoints: Quick Reference, Color Rules, System Rules #13, Common Mistake #4, Layout I (Quote), Layout O (Dark Emphasis Stat Strip), Pre-Ship Checklist Dark-rhythm row, Section 9 Voice notes, Section 11 helpers (`SLATE_800` comment), and primitives-table for slate-800.
- Slate-700 (`334155`) clarified as a text/accent token, not a dark-surface token.
- Reasoning: the "dark slate creep" of v2.0 introduced two competing dark anchors (slate-800 and off-black) and made the system blurry. v2.2 reverts to one dark anchor, matching the Core Five.

**v2.1 (May 2026)**
- Synced to `Blackbird Design System v1.5`
- **No top-edge bars on cards. Ever.** Removed from `addCard` helper, Layout B, Layout O stat cards, and all card layouts. Cards stand on their outline alone.
- New `addTintedCard` helper for teal-50/red-50 callout cards (uses matching teal-200/red-200 borders, no slate-200)
- Color budget rebalanced and now sums to 100%: Surface 50-55% (was 55-65%), Teal 12-15% (was 10-15%), **Red 8-10% (was 1-3%)**, Slate 15-18% (was 15-20%), Black 7-10% (was 8-12%)
- **Red repositioned as the second accent, not signal-only.** Now used for headlines, eyebrows, secondary CTAs, key stats, pull quotes, output/risk columns, hairline accents on dark surfaces. Pair against teal for primary-vs-counterpoint meaning.
- Slate-200 outline scoped specifically to white cards on FAFAFA. Tinted cards use matching tinted borders; dark cards skip the outline.
- **Icons can now be black** (content/structural role) in addition to teal (accent/category-marker role). One color per grid, never mixed.
- **Bar+dot motif: max once per slide** (formalized as a top-level rule; was previously buried in motif notes).
- New Section 13: Pre-Ship Checklist (12-row review pass covering color budget, cards, motifs, titles, image stretching, spacing, icons, dark rhythm, fonts, logos, numbers, voice).
- System rules expanded from 13 to 17 to absorb the above.
- Common mistakes expanded from 13 to 17 to flag top-bars-on-cards, two-bar+dots, mismatched tinted-card borders, mixed-color icon grids.

**v2 (May 2026)**
- Adopted `blackbird-design-system v1.4` (May 2026) and `Brand Identity System` (Mar 2026) as source of truth
- Added Section 0: Identity Layer (one-liner, motto, mission, six pillars, Ambition/Analytics/Artistry trio)
- Page surface changed: `FFFFFF` → `FAFAFA` (off-white, matches live site)
- Card surface: pure `FFFFFF` with 1pt slate-200 outline and 10px radius
- Replaced Stone Gray (`D7D2CB`) with cool slate scale
- Promoted slate-500 (`64748B`) to 4th brand color
- Killed pastel card system (Blush, Mint, Cream, Ice). Use outlined+tinted teal-50/red-50 instead
- Default dark surface: slate-800 (`1E293B`), not off-black. Off-black reserved for code/closing
- Teal usage target: 10-15% (was 5-8%)
- Card title: 14pt uppercase (was 12pt)
- Subtitle: 18pt Futura Bold (was 15pt)
- Stat callout cap: 80pt (was 88-96pt)
- Logo system formalized: 3 lockups, bird mark in bottom-right corner of content slides
- New layouts: Image+Text Two-Column (A), Inputs/Outputs (E), POD/POP/Optionality (L), Solid Callout (M), Roadmap (N), Dark Emphasis Stat Strip (O)
- New motifs: Numbered Colored Prefix, Section Header Underline
- Cross-platform font fallback chains (PowerPoint Mac/Win, Slides, Squarespace, PDF)
- Voice section expanded with pillar vocabulary

**v1 (initial)**
- Original Blackbird PowerPoint brand skill
