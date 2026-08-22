#!/usr/bin/env python3
"""Deck guard. Fails if a .pptx contains an outline the brand spec does not sanction.

Blackbird design system v3.4.0, Section 4a (Outline Control).

Checks:
  1. No stroke uses a color outside the four legal values.
  2. No 333333 used as a stroke (Google Slides default border).
     333333 remains legal as the dark-line divider FILL on dark slides.
  3. No shape inherits a theme line via <a:lnRef> without an explicit <a:ln> override.

Usage:
    python3 scripts/validate_deck_outlines.py deck.pptx [deck2.pptx ...]
    python3 scripts/validate_deck_outlines.py --report deck.pptx   # inventory, never fails

Exit 0 clean, exit 1 on any defect.
"""
import re
import sys
import zipfile

LEGAL = {
    "E2E8F0": "slate-200, white card outline",
    "A0DCE0": "teal-200, tinted card outline",
    "DD9AA3": "red-200, tinted card outline",
    "CBD5E1": "slate-300, table row separator",
}
BANNED = {"333333": "Google Slides / pptxgenjs default shape border"}

SLIDE_PART = re.compile(r"^ppt/(slides|slideLayouts|slideMasters)/[^/]+\.xml$")
LN_BLOCK = re.compile(r"<a:ln\b(?:[^>]*/>|.*?</a:ln>)", re.S)
SRGB = re.compile(r'srgbClr val="([0-9A-Fa-f]{6})"')
SHAPE = re.compile(r"<p:(sp|pic|cxnSp)>.*?</p:\1>", re.S)
NAME = re.compile(r'<p:cNvPr[^>]*name="([^"]*)"')


def audit(path):
    """Return (defects, inventory) for one pptx."""
    defects, inv = [], {}
    try:
        z = zipfile.ZipFile(path)
    except (zipfile.BadZipFile, FileNotFoundError) as e:
        return [f"{path}: cannot open ({e})"], {}

    for part in sorted(z.namelist()):
        if not SLIDE_PART.match(part):
            continue
        xml = z.read(part).decode("utf-8", "replace")
        short = part.split("/")[-1]

        # 1 + 2. Stroke colors.
        for m in LN_BLOCK.finditer(xml):
            block = m.group(0)
            if "noFill" in block:
                inv["none"] = inv.get("none", 0) + 1
                continue
            hit = SRGB.search(block)
            if not hit:
                continue
            hexv = hit.group(1).upper()
            inv[hexv] = inv.get(hexv, 0) + 1
            if hexv in BANNED:
                defects.append(f"{short}: banned stroke {hexv} ({BANNED[hexv]})")
            elif hexv not in LEGAL:
                defects.append(f"{short}: unsanctioned stroke {hexv}")

        # 2b. 333333 is a real token (dark-line) as a DIVIDER FILL on dark
        # slides. It is never valid inside an <a:ln>. Only strokes are flagged,
        # and check 1 above already does that, so nothing extra is needed here.

        # 3. Theme-inherited lines.
        for m in SHAPE.finditer(xml):
            s = m.group(0)
            if "<a:lnRef" not in s:
                continue
            sppr = re.search(r"<p:spPr>.*?</p:spPr>", s, re.S)
            if sppr and LN_BLOCK.search(sppr.group(0)):
                continue  # explicitly overridden, fine
            n = NAME.search(s)
            label = n.group(1) if n else "unnamed"
            inv["theme-inherited"] = inv.get("theme-inherited", 0) + 1
            defects.append(
                f"{short}: shape '{label}' inherits theme line via <a:lnRef>, no explicit <a:ln>"
            )

    z.close()
    # Dedupe while preserving order.
    seen, out = set(), []
    for d in defects:
        if d not in seen:
            seen.add(d)
            out.append(d)
    return out, inv


def main(argv):
    report_only = "--report" in argv
    paths = [a for a in argv[1:] if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 2

    failed = False
    for path in paths:
        defects, inv = audit(path)
        print(f"\n{path}")
        print("  outline inventory: " + (
            ", ".join(f"{k}={v}" for k, v in sorted(inv.items())) or "none found"))
        if defects:
            if not report_only:
                failed = True
            print(f"  {len(defects)} defect(s):")
            for d in defects:
                print(f"    - {d}")
        else:
            print("  clean")

    print()
    if failed:
        print("FAIL: outline defects found. See spec Section 4a (Outline Control).")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
