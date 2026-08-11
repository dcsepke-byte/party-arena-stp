#!/usr/bin/env python3
"""
Test: Feld-Verteilung im Test-Board validieren.

Prüft, dass das REFERENCE_LAYOUT in board.gd exakt die
in der Game Bible (design/gdd/board-architecture.md, Sektion 3.2)
spezifizierte Feldtypen-Mengengerüst erfüllt.

Kontrollsummen:
  START=1, STERN_SHOP=2, ITEM_SHOP=2, EREIGNIS=5,
  GLUECK_PECH=3, MUENZ_BONUS=4, MINISPIEL=23 → Summe=40
"""

import re
import sys

# Erwartete Verteilung (Game Bible Sektion 3.2)
EXPECTED = {
    "START": 1,
    "STERN_SHOP": 2,
    "ITEM_SHOP": 2,
    "EREIGNIS": 5,
    "GLUECK_PECH": 3,
    "MUENZ_BONUS": 4,
    "MINISPIEL": 23,
}

TOTAL_EXPECTED = 40


def parse_reference_layout(filepath: str) -> dict:
    """Extrahiert das REFERENCE_LAYOUT aus der board.gd und zählt die Typen."""
    with open(filepath, "r") as f:
        content = f.read()

    # Finde das REFERENCE_LAYOUT Array
    layout_match = re.search(
        r"const REFERENCE_LAYOUT.*?=\s*\[(.*?)\]", content, re.DOTALL
    )
    if not layout_match:
        print("ERROR: REFERENCE_LAYOUT not found in board.gd!")
        return None

    layout_text = layout_match.group(1)

    # Zähle die FELD_TYP Referenzen
    counts = {}
    for name in ["START", "STERN_SHOP", "ITEM_SHOP", "EREIGNIS",
                  "GLUECK_PECH", "MUENZ_BONUS", "MINISPIEL"]:
        pattern = r"NodeBoard\.FELD_TYP\." + name
        count = len(re.findall(pattern, layout_text))
        counts[name] = count

    return counts


def main():
    board_gd_path = "plugins/boards/test/board.gd"
    counts = parse_reference_layout(board_gd_path)

    if counts is None:
        sys.exit(1)

    total = sum(counts.values())
    all_ok = True

    print("=== Field Distribution Test ===")
    print(f"Reference: {board_gd_path}")
    print()

    for name, expected in EXPECTED.items():
        actual = counts.get(name, 0)
        status = "PASS" if actual == expected else "FAIL"
        if status == "FAIL":
            all_ok = False
        print(f"  [{status}] {name}: expected={expected}, actual={actual}")

    print()
    total_status = "PASS" if total == TOTAL_EXPECTED else "FAIL"
    if total != TOTAL_EXPECTED:
        all_ok = False
    print(f"  [{total_status}] TOTAL: expected={TOTAL_EXPECTED}, actual={total}")

    print()
    if all_ok:
        print("=== RESULT: ALL TESTS PASSED ===")
        sys.exit(0)
    else:
        print("=== RESULT: SOME TESTS FAILED ===")
        sys.exit(1)


if __name__ == "__main__":
    main()
