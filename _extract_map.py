# -*- coding: utf-8 -*-
"""One-off: extract the real Pakistan map SVG from the reference HTML in Downloads,
recolour it from the old palette to the logo-derived palette, and save it into the
project as assets/img/pakistan-map.svg (self-contained, inlined by build.py)."""
import os, re

SRC = r"C:\Users\com\Downloads\Meezab_Z_Pakistan_Map.html"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "img", "pakistan-map.svg")

html = open(SRC, encoding="utf-8").read()

start = html.index('<svg class="map-areas"')
end = html.index('</svg>', start) + len('</svg>')
svg = html[start:end]

# Old palette -> new logo-derived palette (white #FFFFFF stays)
for old, new in [
    ("#1F8B8B", "#187986"),  # served / primary teal
    ("#0F5C5C", "#0E5660"),  # deep teal (hover, label strokes, hatch line)
    ("#D4ECEC", "#D2EBEE"),  # inactive districts
    ("#7FD6D6", "#5FC8CB"),  # upcoming hatch base
]:
    svg = svg.replace(old, new).replace(old.lower(), new)

svg = '<?xml version="1.0" encoding="UTF-8"?>\n' + svg + "\n"

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(svg)
print(f"wrote {OUT} ({len(svg):,} bytes)")
print("contains old hex still?",
      any(h in svg for h in ["#1F8B8B", "#0F5C5C", "#D4ECEC", "#7FD6D6"]))
