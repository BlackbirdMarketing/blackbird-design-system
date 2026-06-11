#!/usr/bin/env python3
"""Repo guard. Fails if index.html references a file that does not exist,
or if the core six hex values drift between index.html and the spec.
Run from repo root: python3 scripts/validate_assets.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []

html = (ROOT / "index.html").read_text(encoding="utf-8")

# 1. Every local src="..." and url(...) must exist on disk.
refs = set(re.findall(r'src="([^"]+)"', html))
refs |= {m.strip("'\"") for m in re.findall(r'url\(([^)]+)\)', html)}
local = [r for r in sorted(refs) if not r.startswith(("http", "data:", "#"))]
for r in local:
    if not (ROOT / r).exists():
        errors.append(f"missing asset referenced by index.html: {r}")

# 2. Core six must match between index.html and the spec.
CORE = ["FAFAFA", "008C95", "862633", "64748B", "000000", "0D0D0D"]
spec_path = next((ROOT / "spec").glob("powerpoint-brand-skill*.md"))
spec = spec_path.read_text(encoding="utf-8").upper()
html_u = html.upper()
for hexv in CORE:
    if hexv not in html_u:
        errors.append(f"core hex {hexv} missing from index.html")
    if hexv not in spec:
        errors.append(f"core hex {hexv} missing from {spec_path.name}")

# 3. Single system version: VERSION file appears in both artifacts.
version = (ROOT / "VERSION").read_text().strip()
if f"v{version.rsplit('.', 1)[0]}" not in html and version not in html:
    errors.append(f"index.html does not carry system version {version}")
if version not in spec_path.read_text(encoding="utf-8"):
    errors.append(f"{spec_path.name} does not carry system version {version}")

if errors:
    print(f"FAIL ({len(errors)}):")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print(f"OK: {len(local)} local asset refs verified, core six aligned, version {version} consistent.")
