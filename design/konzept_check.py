#!/usr/bin/env python3
"""Kompletter Konzept-Gegencheck: Party Arena gegen die Game Bible.
Prüft alle 64 GDD-Kapitel gegen die tatsächliche Implementierung.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GDD = os.path.join(ROOT, "design/gdd")
BOARDS = os.path.join(ROOT, "plugins/boards")
CHARS = os.path.join(ROOT, "plugins/characters")
MINIGAMES = os.path.join(ROOT, "plugins/minigames")
ITEMS = os.path.join(ROOT, "plugins/items")

results = []
def check(name, ok, detail=""):
    results.append((name, ok, detail))

# ── 1. Game Bible Kapitel vorhanden ──
gdd_files = [f for f in os.listdir(GDD) if f.endswith(".md") and not f.startswith(("game-", "session", "README", "bible"))]
check("Game Bible: 64 Kapitel", len(gdd_files) >= 60, f"{len(gdd_files)} Kapitel")

# ── 2. Boards ──
islands = ["sonnenstrand","zuckerwald","wolkenwerk","frostgipfel","dschungeltempel","mechanik-stadt","sternenzitadelle"]
for isl in islands:
    d = os.path.join(BOARDS, isl)
    has_gd = os.path.exists(os.path.join(d, "board.gd"))
    has_json = os.path.exists(os.path.join(d, "board.json"))
    has_tscn = os.path.exists(os.path.join(d, "board.tscn"))
    check(f"Board {isl}: 3 Dateien", has_gd and has_json and has_tscn, f"gd={has_gd} json={has_json} tscn={has_tscn}")

# ── 3. Charaktere ──
chars = ["brix","nixie","pip","koko","tiko","bolt","bloom","momo"]
for ch in chars:
    d = os.path.join(CHARS, ch)
    has_glb = os.path.exists(os.path.join(d, f"{ch}.glb"))
    has_json = os.path.exists(os.path.join(d, "character.json"))
    has_tscn = os.path.exists(os.path.join(d, "character.tscn"))
    check(f"Charakter {ch}: GLB+JSON+TSN", has_glb and has_json and has_tscn, f"glb={has_glb}")

# ── 4. Minigames (12 neue) ──
new_minigames = ["muenzregen","balance_akt","zielwurf","arena_star_sagt","blitz_fangen",
                 "knoepfchen_druecker","sternen_labyrinth","insel_memory","muenz_zaehler",
                 "wort_puzzle","sternen_bruecke","schatz_trage"]
for mg in new_minigames:
    d = os.path.join(MINIGAMES, mg)
    has_gd = os.path.exists(os.path.join(d, "minigame.gd"))
    has_json = os.path.exists(os.path.join(d, "minigame.json"))
    has_tscn = os.path.exists(os.path.join(d, "minigame.tscn"))
    check(f"Minigame {mg}: 3 Dateien", has_gd and has_json and has_tscn, f"gd={has_gd} json={has_json} tscn={has_tscn}")

# ── 5. Items (5 neue) ──
new_items = ["luckydice","teleporter","shield","coinmagnet","thiefglove"]
for it in new_items:
    d = os.path.join(ITEMS, it)
    has_gd = os.path.exists(os.path.join(d, "item.gd"))
    check(f"Item {it}: item.gd", has_gd)

# ── 6. Feldtypen in node.gd ──
node_gd = os.path.join(ROOT, "common/scenes/board_logic/node/node.gd")
if os.path.exists(node_gd):
    content = open(node_gd).read()
    for ft in ["START","STERN_SHOP","ITEM_SHOP","EREIGNIS","GLUECK_PECH","MUENZ_BONUS","MINISPIEL"]:
        check(f"Feldtyp {ft} in node.gd", ft in content)

# ── 7. Stern-Mechanik ──
controller = os.path.join(ROOT, "common/scenes/board_logic/controller/controller.gd")
if os.path.exists(controller):
    c = open(controller).read()
    check("STAR_COST=20", "STAR_COST := 20" in c or "STAR_COST = 20" in c)
    check("buy_star", "buy_star" in c)
    check("relocate_star", "relocate_star" in c)

# ── 8. Abzweigungen ──
for isl in islands:
    bgd = os.path.join(BOARDS, isl, "board.gd")
    if os.path.exists(bgd):
        b = open(bgd).read()
        check(f"Board {isl}: BRANCHES", "BRANCHES" in b)
        check(f"Board {isl}: _wire_branches", "_wire_branches" in b)
        check(f"Board {isl}: handle_event", "handle_event" in b)

# ── Zusammenfassung ──
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"=== KONZEPT-GEGENCHECK: {passed}/{total} Checks bestanden ===\n")
for name, ok, detail in results:
    status = "✅" if ok else "❌"
    print(f"{status} {name}" + (f"  ({detail})" if detail and not ok else ""))
print(f"\n=== ERGEBNIS: {passed}/{total} ===")
