#!/usr/bin/env python3
"""Generiert eine visuelle Vorschau der 40-Felder-Spielkarte als HTML.
Zeigt die Felder in einer kreisförmigen Anordnung (wie im Spiel) mit Farben
und Icons je Feldtyp. Für Danny's Review.
"""
import json
import re

# ── Farben je Feldtyp ──
FELD_FARBE = {
    "START": "#e8b04b",        # gold
    "STERN_SHOP": "#ffd700",   # gelb
    "ITEM_SHOP": "#9b59b6",    # lila
    "EREIGNIS": "#e74c3c",     # rot
    "GLUECK_PECH": "#2ecc71",  # grün
    "MUENZ_BONUS": "#f39c12",  # orange
    "MINISPIEL": "#3498db",    # blau
}
FELD_ICON = {
    "START": "🏁", "STERN_SHOP": "⭐", "ITEM_SHOP": "🎁", "EREIGNIS": "❓",
    "GLUECK_PECH": "🍀", "MUENZ_BONUS": "🪙", "MINISPIEL": "🎮",
}

def parse_layout(board_gd):
    """Extrahiert REFERENCE_LAYOUT aus board.gd und mappt Indizes zu Typnamen."""
    with open(board_gd) as f:
        content = f.read()
    m = re.search(r"REFERENCE_LAYOUT.*?=\s*\[(.*?)\]", content, re.DOTALL)
    if not m:
        return []
    ints = re.findall(r"FELD_TYP\.(\w+)", m.group(1))
    return ints  # Typ-Namen in Reihenfolge

def build_board_html(name, board_dir, theme):
    layout = parse_layout(f"{board_dir}/board.gd")
    # Kreis-Positionen für 40 Felder
    import math
    cells = []
    n = len(layout)
    for i, typ in enumerate(layout):
        ang = 2 * math.pi * i / n - math.pi/2
        x = 50 + 40 * math.cos(ang)
        y = 50 + 40 * math.sin(ang)
        farbe = FELD_FARBE.get(typ, "#999")
        icon = FELD_ICON.get(typ, "•")
        cells.append(f'<div class="cell" style="left:{x:.1f}%;top:{y:.1f}%;background:{farbe}" title="Feld {i+1}: {typ}">{icon}<span class="num">{i+1}</span></div>')
    return f"""
<div class="board-box">
  <h3>{name} <span class="theme">{theme}</span></h3>
  <div class="board">
    {''.join(cells)}
  </div>
</div>"""

# ── Alle 7 Inseln ──
islands = [
    ("Sonnenstrand", "plugins/boards/sonnenstrand", "Urlaub & Wasser"),
    ("Zuckerwald", "plugins/boards/zuckerwald", "Süßigkeiten"),
    ("Wolkenwerk", "plugins/boards/wolkenwerk", "Schwebende Himmel"),
    ("Frostgipfel", "plugins/boards/frostgipfel", "Eis & Schnee"),
    ("Dschungeltempel", "plugins/boards/dschungeltempel", "Ruinen"),
    ("Mechanik-Stadt", "plugins/boards/mechanik-stadt", "Spielzeug-Technik"),
    ("Sternenzitadelle", "plugins/boards/sternenzitadelle", "Finale"),
]

boards_html = "".join(build_board_html(n, d, t) for n, d, t in islands)

html = f"""<!DOCTYPE html>
<html lang="de"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Party Arena — Karten-Übersicht</title><style>
body{{background:#0f1117;color:#e5e7eb;font-family:system-ui;margin:0;padding:20px}}
h1{{color:#e8b04b;text-align:center}}h2{{color:#e8b04b;margin:30px 0 10px}}
.board-box{{background:#1a1c25;border:1px solid #2a2d3a;border-radius:12px;padding:16px;margin:20px 0}}
.board-box h3{{color:#fff;margin:0 0 4px}}.theme{{color:#9ca3af;font-weight:400;font-size:.85em}}
.board{{position:relative;width:100%;max-width:500px;aspect-ratio:1;margin:10px auto;border-radius:50%;border:3px solid #2a2d3a;background:radial-gradient(circle,#1a1c25,#0f1117)}}
.cell{{position:absolute;width:38px;height:38px;margin:-19px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:18px;transform:translate(-50%,-50%);border:2px solid #0f1117}}
.cell .num{{position:absolute;bottom:-6px;right:-2px;font-size:8px;background:#0f1117;color:#fff;padding:1px 3px;border-radius:4px}}
.legend{{text-align:center;margin:20px 0;display:flex;flex-wrap:wrap;gap:10px;justify-content:center}}
.legend span{{display:inline-flex;align-items:center;gap:5px;font-size:.85em}}
.legend .dot{{width:14px;height:14px;border-radius:50%;display:inline-block}}
</style></head><body>
<h1>🎮 Party Arena — Karten-Übersicht</h1>
<div class="legend">
  <span><span class="dot" style="background:#e8b04b"></span>Start</span>
  <span><span class="dot" style="background:#ffd700"></span>Sternen-Shop</span>
  <span><span class="dot" style="background:#9b59b6"></span>Item-Shop</span>
  <span><span class="dot" style="background:#e74c3c"></span>Ereignis</span>
  <span><span class="dot" style="background:#2ecc71"></span>Glück/Pech</span>
  <span><span class="dot" style="background:#f39c12"></span>Münz-Bonus</span>
  <span><span class="dot" style="background:#3498db"></span>Minispiel</span>
</div>
{boards_html}
</body></html>"""

with open("/opt/data/SuperTuxParty/design/boards-vorschau.html", "w") as f:
    f.write(html)
print("Karten-Vorschau geschrieben: design/boards-vorschau.html")
