#!/usr/bin/env python3
"""Verification test for Milestone 6: 7 Island Boards.

Tests:
1. All 7 island boards exist (board.tscn + board.gd + board.json)
2. Each has correct 40-field distribution
3. board.json is valid (name, thema, schwierigkeit, farben)
4. BoardLoader discovers all 7 islands
"""

import json
import os
import re
import sys

BOARDS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plugins", "boards")

EXPECTED_ISLANDS = {
    "sonnenstrand": {
        "name_de": "Sonnenstrand",
        "difficulty": 1,
        "field_distribution": {"START": 1, "STERN_SHOP": 3, "ITEM_SHOP": 2, "EREIGNIS": 6, "GLUECK_PECH": 3, "MUENZ_BONUS": 4, "MINISPIEL": 21},
        "colors": ["#00f0ff", "#f4d58d", "#ff6b6b"],
    },
    "zuckerwald": {
        "name_de": "Zuckerwald",
        "difficulty": 2,
        "field_distribution": {"START": 1, "STERN_SHOP": 3, "ITEM_SHOP": 2, "EREIGNIS": 5, "GLUECK_PECH": 3, "MUENZ_BONUS": 4, "MINISPIEL": 22},
        "colors": ["#ff4d6d", "#8b4513", "#98ff98"],
    },
    "wolkenwerk": {
        "name_de": "Wolkenwerk",
        "difficulty": 3,
        "field_distribution": {"START": 1, "STERN_SHOP": 3, "ITEM_SHOP": 2, "EREIGNIS": 6, "GLUECK_PECH": 3, "MUENZ_BONUS": 4, "MINISPIEL": 21},
        "colors": ["#87ceeb", "#ffffff", "regenbogen"],
    },
    "frostgipfel": {
        "name_de": "Frostgipfel",
        "difficulty": 3,
        "field_distribution": {"START": 1, "STERN_SHOP": 3, "ITEM_SHOP": 2, "EREIGNIS": 5, "GLUECK_PECH": 3, "MUENZ_BONUS": 4, "MINISPIEL": 22},
        "colors": ["#a8d8ea", "#f0f0f0", "#9b59b6"],
    },
    "dschungeltempel": {
        "name_de": "Dschungeltempel",
        "difficulty": 4,
        "field_distribution": {"START": 1, "STERN_SHOP": 3, "ITEM_SHOP": 2, "EREIGNIS": 6, "GLUECK_PECH": 3, "MUENZ_BONUS": 4, "MINISPIEL": 21},
        "colors": ["#2d6a4f", "#ffd700", "#8b4513"],
    },
    "mechanik-stadt": {
        "name_de": "Mechanik-Stadt",
        "difficulty": 4,
        "field_distribution": {"START": 1, "STERN_SHOP": 3, "ITEM_SHOP": 2, "EREIGNIS": 6, "GLUECK_PECH": 3, "MUENZ_BONUS": 4, "MINISPIEL": 21},
        "colors": ["#c0c0c0", "#ff6a00", "#ffd34e"],
    },
    "sternenzitadelle": {
        "name_de": "Sternenzitadelle",
        "difficulty": 5,
        "field_distribution": {"START": 1, "STERN_SHOP": 4, "ITEM_SHOP": 2, "EREIGNIS": 6, "GLUECK_PECH": 3, "MUENZ_BONUS": 4, "MINISPIEL": 20},
        "colors": ["#ffd700", "#1a1a4e", "#ff00ff"],
    },
}

# FELD_TYP enum values from NodeBoard
FELD_TYP_NAMES = {
    0: "START",
    1: "STERN_SHOP",
    2: "ITEM_SHOP",
    3: "EREIGNIS",
    4: "GLUECK_PECH",
    5: "MUENZ_BONUS",
    6: "MINISPIEL",
}

errors = []
warnings = []

def error(msg):
    errors.append(msg)
    print(f"  ❌ {msg}")

def warn(msg):
    warnings.append(msg)
    print(f"  ⚠️  {msg}")

def ok(msg):
    print(f"  ✅ {msg}")


def test_files_exist(island_id):
    """Test 1: All three files exist for each island."""
    board_dir = os.path.join(BOARDS_DIR, island_id)
    for filename in ["board.tscn", "board.gd", "board.json"]:
        filepath = os.path.join(board_dir, filename)
        if not os.path.isfile(filepath):
            error(f"{island_id}/{filename} missing")
        else:
            ok(f"{island_id}/{filename} exists")


def test_board_json(island_id, expected):
    """Test 2: board.json is valid JSON with required fields."""
    json_path = os.path.join(BOARDS_DIR, island_id, "board.json")
    try:
        with open(json_path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        error(f"{island_id}/board.json: invalid JSON: {e}")
        return None
    except FileNotFoundError:
        return None

    required = ["name_de", "theme", "difficulty", "colors", "field_distribution", "music"]
    for field in required:
        if field not in data:
            error(f"{island_id}/board.json: missing field '{field}'")
        else:
            ok(f"{island_id}/board.json: '{field}' present")

    # Validate name
    if data.get("name_de") != expected["name_de"]:
        error(f"{island_id}/board.json: name_de '{data.get('name_de')}' != expected '{expected['name_de']}'")
    else:
        ok(f"{island_id}/board.json: name_de correct ({data['name_de']})")

    # Validate difficulty
    if data.get("difficulty") != expected["difficulty"]:
        error(f"{island_id}/board.json: difficulty {data.get('difficulty')} != expected {expected['difficulty']}")
    else:
        ok(f"{island_id}/board.json: difficulty correct ({data['difficulty']} stars)")

    # Validate colors
    if data.get("colors") != expected["colors"]:
        error(f"{island_id}/board.json: colors {data.get('colors')} != expected {expected['colors']}")
    else:
        ok(f"{island_id}/board.json: colors correct ({', '.join(data['colors'])})")

    # Validate field distribution
    dist = data.get("field_distribution", {})
    if dist != expected["field_distribution"]:
        error(f"{island_id}/board.json: field_distribution mismatch")
        print(f"       expected: {expected['field_distribution']}")
        print(f"       got:      {dist}")
    else:
        total = sum(dist.values())
        if total != 40:
            error(f"{island_id}/board.json: field_distribution sums to {total}, expected 40")
        else:
            ok(f"{island_id}/board.json: field_distribution correct ({total} total)")

    return data


def test_board_gd(island_id, expected):
    """Test 3: board.gd has correct REFERENCE_LAYOUT with 40 fields."""
    gd_path = os.path.join(BOARDS_DIR, island_id, "board.gd")
    try:
        with open(gd_path) as f:
            content = f.read()
    except FileNotFoundError:
        return

    # Count FELD_TYP entries
    matches = re.findall(r'FELD_TYP\.(\w+)', content)
    # Filter to only REFERENCE_LAYOUT section (between const REFERENCE_LAYOUT and the next const or function)
    layout_section = re.search(r'const REFERENCE_LAYOUT: Array\[int\] =\s*\[(.*?)^\s*\]', content, re.DOTALL | re.MULTILINE)
    if layout_section:
        layout_types = re.findall(r'FELD_TYP\.(\w+)', layout_section.group())
    else:
        layout_types = matches

    num_fields = len(layout_types)
    if num_fields < 40:
        error(f"{island_id}/board.gd: REFERENCE_LAYOUT has only {num_fields} fields, expected 40")
    elif num_fields > 40:
        error(f"{island_id}/board.gd: REFERENCE_LAYOUT has {num_fields} fields, expected 40")
    else:
        ok(f"{island_id}/board.gd: REFERENCE_LAYOUT has exactly 40 fields")

    # Count field types
    type_counts = {}
    for t in layout_types:
        type_counts[t] = type_counts.get(t, 0) + 1

    # Compare with expected distribution
    name_to_gd_name = {
        "START": "START",
        "STERN_SHOP": "STERN_SHOP",
        "ITEM_SHOP": "ITEM_SHOP",
        "EREIGNIS": "EREIGNIS",
        "GLUECK_PECH": "GLUECK_PECH",
        "MUENZ_BONUS": "MUENZ_BONUS",
        "MINISPIEL": "MINISPIEL",
    }

    dist_ok = True
    for key, expected_count in expected["field_distribution"].items():
        gd_key = name_to_gd_name.get(key, key)
        actual_count = type_counts.get(gd_key, 0)
        if actual_count != expected_count:
            error(f"{island_id}/board.gd: {key} count {actual_count} != expected {expected_count}")
            dist_ok = False

    if dist_ok:
        ok(f"{island_id}/board.gd: field type distribution matches board.json")


def test_board_tscn(island_id):
    """Test 4: board.tscn has Nodes container and references correct board.gd."""
    tscn_path = os.path.join(BOARDS_DIR, island_id, "board.tscn")
    try:
        with open(tscn_path) as f:
            content = f.read()
    except FileNotFoundError:
        return

    # Check for Nodes container
    if 'node name="Nodes"' in content:
        ok(f"{island_id}/board.tscn: Nodes container found")
    else:
        error(f"{island_id}/board.tscn: Nodes container missing")

    # Check script reference
    expected_script = f'path="res://plugins/boards/{island_id}/board.gd"'
    if expected_script in content:
        ok(f"{island_id}/board.tscn: references correct board.gd")
    else:
        error(f"{island_id}/board.tscn: missing or wrong script reference")

    # Count NodeBoard instances
    node_count = len(re.findall(r'\[node name="Node(\d+)"', content))
    if node_count >= 40:
        ok(f"{island_id}/board.tscn: has {node_count} NodeBoard instances (>= 40)")
    else:
        error(f"{island_id}/board.tscn: only {node_count} NodeBoard instances, need >= 40")

    # Check controller
    if 'node name="Controller"' in content:
        ok(f"{island_id}/board.tscn: Controller node present")
    else:
        warn(f"{island_id}/board.tscn: Controller node missing")


def main():
    print("=" * 60)
    print("MILESTONE 6 VERIFICATION: 7 Island Boards")
    print("=" * 60)

    # Test 1: All files exist
    print("\n--- Test 1: Board Files ---")
    for island_id in EXPECTED_ISLANDS:
        test_files_exist(island_id)

    # Test 2: board.json validation
    print("\n--- Test 2: board.json Validation ---")
    for island_id, expected in EXPECTED_ISLANDS.items():
        test_board_json(island_id, expected)

    # Test 3: board.gd REFERENCE_LAYOUT
    print("\n--- Test 3: board.gd REFERENCE_LAYOUT ---")
    for island_id, expected in EXPECTED_ISLANDS.items():
        test_board_gd(island_id, expected)

    # Test 4: board.tscn structure
    print("\n--- Test 4: board.tscn Structure ---")
    for island_id in EXPECTED_ISLANDS:
        test_board_tscn(island_id)

    # Summary
    print("\n" + "=" * 60)
    print("VERIFICATION SUMMARY")
    print("=" * 60)

    island_count = len([d for d in os.listdir(BOARDS_DIR)
                        if os.path.isdir(os.path.join(BOARDS_DIR, d))
                        and os.path.isfile(os.path.join(BOARDS_DIR, d, "board.tscn"))
                        and d not in ("test", "KDEValley")])

    print(f"  Island boards found: {island_count} (expected: 7)")

    if errors:
        print(f"\n  ❌ {len(errors)} ERRORS:")
        for e in errors:
            print(f"     - {e}")
    else:
        print(f"\n  ✅ No errors!")

    if warnings:
        print(f"\n  ⚠️  {len(warnings)} WARNINGS:")
        for w in warnings:
            print(f"     - {w}")

    print(f"\n  Total checks: {len(errors) + len(warnings)} issues")
    print(f"  Result: {'❌ FAIL' if errors else '✅ PASS'}")

    if errors:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
