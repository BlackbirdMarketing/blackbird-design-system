#!/usr/bin/env python3
"""Repo guard for the outline rules (design system v3.4.0, spec Section 4a).

CI cannot check decks, since no .pptx lives in this repo. This script checks
that the rules themselves stay intact and stay mirrored, so Section 4a cannot
be dropped, weakened, or drift between the spec and the skill copy.

Deck-level checking is scripts/validate_deck_outlines.py, run by hand against
a .pptx before it ships.

Run from repo root: python3 scripts/validate_spec_outline_rules.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []

SPEC = ROOT / "spec" / "powerpoint-brand-skill.md"
SKILL = ROOT / "skill" / "blackbird-pptx-brand" / "SKILL.md"

spec = SPEC.read_text(encoding="utf-8")
skill = SKILL.read_text(encoding="utf-8")

# 1. Spec and skill mirror must stay byte-identical.
if spec != skill:
    errors.append(
        "spec/powerpoint-brand-skill.md and skill/blackbird-pptx-brand/SKILL.md "
        "have diverged; they must stay identical"
    )

# 2. Section 4a must exist and carry its default rule.
if "## 4a. Outline Control" not in spec:
    errors.append("spec is missing Section 4a (Outline Control)")

RULE = "Every shape ships with no outline unless this section names it."
if RULE not in spec:
    errors.append(f"spec is missing the Section 4a default rule: {RULE!r}")

# 3. The four legal stroke values must all be named in Section 4a.
LEGAL = {
    "E2E8F0": "slate-200, white card outline",
    "A0DCE0": "teal-200, teal-50 card outline",
    "DD9AA3": "red-200, red-50 card outline",
    "CBD5E1": "slate-300, table row separator",
}
start = spec.find("## 4a. Outline Control")
end = spec.find("## 5. Slide Anatomy", start)
section = spec[start:end] if start != -1 and end != -1 else ""
for hexv, label in LEGAL.items():
    if hexv not in section.upper():
        errors.append(f"Section 4a does not name legal stroke {hexv} ({label})")

# 4. 333333 must be named as banned, and must appear nowhere as a live token.
if "333333" not in section:
    errors.append("Section 4a does not name 333333 as a banned stroke")

# 333333 stays a valid token (dark-line, the divider FILL on dark slides).
# The ban is scoped to strokes, so Section 4a must say so explicitly rather
# than banning the value outright.
if "dark-line" not in section:
    errors.append(
        "Section 4a bans 333333 without noting the dark-line exception; "
        "333333 is still a valid divider fill on dark slides"
    )

# 5. Every tool we ship decks with needs a documented suppression path.
for tool in ["PowerPoint", "Google Slides", "pptxgenjs", "python-pptx"]:
    if tool not in section:
        errors.append(f"Section 4a has no suppression guidance for {tool}")

if "NOT_RENDERED" not in section:
    errors.append("Section 4a omits the Google Slides NOT_RENDERED suppression call")
if "lnRef" not in section:
    errors.append("Section 4a omits the theme-inherited <a:lnRef> case")

# 5b. `line: { width: 0 }` must not appear in live guidance.
# Measured on pptxgenjs 4.0.1: that form emits <a:ln w="12700"> with a solid
# 333333 fill. It reads as a suppression and behaves as an addition. The only
# permitted occurrence is inside the historical changelog, where it is quoted
# and explicitly marked as corrected.
# Prose may quote the form in order to ban it. Code fences may not contain it,
# because code fences are what people copy.
import re

BAD_LINE = re.compile(r"line\s*:\s*\{[^}]*width\s*:\s*0[^}]*\}")
for fence in re.findall(r"```(?:javascript|js)\n(.*?)```", spec, re.S):
    for m in BAD_LINE.finditer(fence):
        errors.append(
            f"pptxgenjs code fence contains {m.group(0)!r}; it emits a solid "
            "1pt 333333 stroke. Use line: { type: 'none' }"
        )

# Every pptxgenjs addShape call must state its line handling one way or another.
for fence in re.findall(r"```(?:javascript|js)\n(.*?)```", spec, re.S):
    for call in re.findall(r"addShape\((?:[^()]|\([^()]*\))*\)", fence, re.S):
        if "line:" not in call:
            errors.append(
                "pptxgenjs addShape call omits the line key entirely: "
                f"{' '.join(call.split())[:70]}..."
            )

# 5c. Section 4a must carry the measured pptxgenjs facts, not soft language.
if "DEF_SHAPE_LINE_COLOR" not in section:
    errors.append(
        "Section 4a does not name DEF_SHAPE_LINE_COLOR, the pptxgenjs fallback "
        "that makes line: { width: 0 } emit 333333"
    )

# 5d. addBottomBar must suppress its outline explicitly. It is the helper that
# historically shipped with no `line` key at all.
bar_start = spec.find("function addBottomBar")
if bar_start == -1:
    errors.append("spec no longer defines addBottomBar")
else:
    bar = spec[bar_start:bar_start + 400]
    bar_end = bar.find("}\n}")
    bar = bar[:bar_end] if bar_end != -1 else bar
    if "type: 'none'" not in bar and 'type: "none"' not in bar:
        errors.append("addBottomBar does not set line: { type: 'none' }")

# 6. Checklist row and common mistake must be present.
if "**Outlines**" not in spec:
    errors.append("Pre-Ship Checklist has no Outlines row")
if "Shipping tool-default outlines" not in spec:
    errors.append("Common Mistakes list has no tool-default outline entry")

# 7. Version must be in lockstep across VERSION, spec, and index.html.
version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
if f"system version {version}" not in spec:
    errors.append(f"spec does not declare system version {version}")
html = (ROOT / "index.html").read_text(encoding="utf-8")
if f"v{version}" not in html:
    errors.append(f"index.html does not carry v{version}")

# 8. The deck validator must exist and stay in sync with the legal set.
deck_validator = ROOT / "scripts" / "validate_deck_outlines.py"
if not deck_validator.exists():
    errors.append("scripts/validate_deck_outlines.py is missing")
else:
    dv = deck_validator.read_text(encoding="utf-8").upper()
    for hexv in LEGAL:
        if hexv not in dv:
            errors.append(f"validate_deck_outlines.py does not allow {hexv}")
    if '"333333"' not in deck_validator.read_text(encoding="utf-8"):
        errors.append("validate_deck_outlines.py does not ban the 333333 stroke")

if errors:
    print(f"FAIL: {len(errors)} outline-rule problem(s)")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print(f"PASS: outline rules intact, spec and skill mirrored, v{version} in lockstep")
