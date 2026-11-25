#!/usr/bin/env python3
"""WCAG contrast check of the site's colour pairs (default and high-contrast themes). Exit 1 if any pair fails.
Run: python3 tools/contrast.py   Update PAIRS when a colour pair is added to css/style.css."""
import sys
def lum(h):
    h = h.lstrip('#'); c = [int(h[i:i+2], 16)/255 for i in (0, 2, 4)]
    c = [x/12.92 if x <= .03928 else ((x+.055)/1.055)**2.4 for x in c]
    return .2126*c[0] + .7152*c[1] + .0722*c[2]
def ratio(a, b):
    a, b = lum(a), lum(b); a, b = max(a, b), min(a, b); return (a+.05)/(b+.05)
# (name, foreground, background, minimum): 4.5 text, 3.0 large text / UI components
DEFAULT = [
 ("body text", "#1F2F44", "#F6F9FB", 4.5), ("muted text on surface", "#4A5F78", "#FFFFFF", 4.5),
 ("muted text on page", "#4A5F78", "#F6F9FB", 4.5), ("muted text on band", "#4A5F78", "#DCE4EC", 4.5),
 ("link on page", "#34495E", "#F6F9FB", 4.5), ("eyebrow amber on night", "#E9A23B", "#17222F", 4.5),
 ("lead paper on ink", "#DCE4EC", "#1F2F44", 4.5), ("nav paper on night", "#DCE4EC", "#17222F", 4.5),
 ("nav active night on amber", "#17222F", "#E9A23B", 4.5), ("ghost button white on ink", "#FFFFFF", "#1F2F44", 4.5),
 ("footer mist on night", "#9FB4C7", "#17222F", 4.5), ("icon aqua on ink (UI)", "#4FB3BF", "#1F2F44", 3.0),
 ("icon amber on ink (UI)", "#E9A23B", "#1F2F44", 3.0), ("focus ring ink on page (UI)", "#1F2F44", "#F6F9FB", 3.0),
 ("focus ring amber on night (UI)", "#E9A23B", "#17222F", 3.0), ("a11y panel text on surface", "#1F2F44", "#FFFFFF", 4.5),
]
HIGH = [
 ("text white on black", "#FFFFFF", "#000000", 7.0), ("link yellow on black", "#FFD600", "#000000", 7.0),
 ("button black on yellow", "#000000", "#FFD600", 7.0), ("focus yellow on black (UI)", "#FFD600", "#000000", 3.0),
 ("borders white on black (UI)", "#FFFFFF", "#000000", 3.0),
]
bad = 0
for title, pairs in (("default", DEFAULT), ("high contrast", HIGH)):
    print(f"[{title}]")
    for n, f, b, m in pairs:
        r = ratio(f, b); ok = r >= m; bad += not ok
        print(f"  {'OK ' if ok else 'FAIL'} {r:5.2f}:1 (min {m})  {n}")
sys.exit(1 if bad else 0)
