#!/usr/bin/env python3
"""
Test: Charakter-System — Party Arena Milestone 5
Game Bible: design/gdd/characters-overview.md

Verifies:
  1. All 8 Arenian plugin folders exist (brix, nixie, pip, koko, tiko, bolt, bloom, momo)
  2. Each has the 3 required files (character.tscn, character.json, icon.png)
  3. character.json is valid (name, type, home, personality, color_hex)
  4. Color hex values match the design specification exactly
  5. character.tscn has the character.gd script attached
  6. Tux-IP characters are NOT loadable (character.tscn renamed to .legacy)

Run: python3 tests/unit/test_character_system.py
"""

import json
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# ── Test Helpers ──────────────────────────────────────────────────────────

def green(msg: str) -> str:
    return f"\033[32m{msg}\033[0m"

def red(msg: str) -> str:
    return f"\033[31m{msg}\033[0m"

def yellow(msg: str) -> str:
    return f"\033[33m{msg}\033[0m"

pass_count = 0
fail_count = 0

def check(condition: bool, name: str, detail: str = "") -> None:
    global pass_count, fail_count
    if condition:
        pass_count += 1
        print(f"  {green('PASS')} {name}")
    else:
        fail_count += 1
        print(f"  {red('FAIL')} {name}")
        if detail:
            print(f"       {detail}")


# ── Expected Characters (characters-overview.md §1) ──────────────────────

EXPECTED_CHARACTERS = {
    "brix": {
        "name": "Brix",
        "type": "Stein-Golem",
        "home": "Mechanik-Stadt",
        "personality": "mutig, tollpatschig, gutherzig",
        "color_hex": "#ff6a00",
    },
    "nixie": {
        "name": "Nixie",
        "type": "Axolotl",
        "home": "Sonnenstrand",
        "personality": "neugierig, wasseraffin, verspielt",
        "color_hex": "#00f0ff",
    },
    "pip": {
        "name": "Pip",
        "type": "Fliegendes Eichhörnchen",
        "home": "Wolkenwerk",
        "personality": "schnell, frech, immer in Bewegung",
        "color_hex": "#ffd34e",
    },
    "koko": {
        "name": "Koko",
        "type": "Panda",
        "home": "Zuckerwald",
        "personality": "freundlich, stark, gemütlich",
        "color_hex": "#ff4d6d",
    },
    "tiko": {
        "name": "Tiko",
        "type": "Vogel (Tukan)",
        "home": "Dschungeltempel",
        "personality": "chaotisch, lustig, Feder-Wirbel",
        "color_hex": "#2bffb9",
    },
    "bolt": {
        "name": "Bolt",
        "type": "Roboter",
        "home": "Mechanik-Stadt",
        "personality": "logisch, präzise, liebenswert",
        "color_hex": "#3a86ff",
    },
    "bloom": {
        "name": "Bloom",
        "type": "Kaktus",
        "home": "Dschungeltempel (Oasen-Rand)",
        "personality": "ruhig, humorvoll, Stacheln nur Deko",
        "color_hex": "#7b2ff7",
    },
    "momo": {
        "name": "Momo",
        "type": "Waschbär",
        "home": "Frostgipfel",
        "personality": "clever, trickreich, Schabernack",
        "color_hex": "#ff3cac",
    },
}

# Legacy Tux-IP that must NOT be loadable as playable characters
LEGACY_CHARACTERS = ["Tux", "Godette", "Beastie", "Green Tux"]

CHARACTERS_DIR = PROJECT_ROOT / "plugins" / "characters"


# ── Tests ──────────────────────────────────────────────────────────────────

def test_character_plugin_folders_exist():
    """Verify all 8 Arenian plugin folders exist."""
    print("\n" + "=" * 60)
    print("TEST 1: All 8 Arenian plugin folders exist")
    print("=" * 60)

    for char_id in EXPECTED_CHARACTERS:
        folder = CHARACTERS_DIR / char_id
        check(folder.is_dir(), f"Folder '{char_id}' exists",
              f"Path: {folder}")


def test_character_required_files():
    """Verify each character has character.tscn, character.json, icon.png."""
    print("\n" + "=" * 60)
    print("TEST 2: Required files exist (character.tscn, character.json, icon.png)")
    print("=" * 60)

    required_files = ["character.tscn", "character.json", "icon.png"]

    for char_id in EXPECTED_CHARACTERS:
        folder = CHARACTERS_DIR / char_id
        for filename in required_files:
            filepath = folder / filename
            check(filepath.is_file(), f"{char_id}: {filename} exists",
                  f"Missing: {filepath}")


def test_character_json_validity():
    """Verify each character.json has correct metadata matching the game bible."""
    print("\n" + "=" * 60)
    print("TEST 3: character.json validity (name, type, home, personality, color_hex)")
    print("=" * 60)

    for char_id, expected in EXPECTED_CHARACTERS.items():
        json_path = CHARACTERS_DIR / char_id / "character.json"

        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            check(False, f"{char_id}: valid JSON", f"Parse error: {e}")
            continue
        except FileNotFoundError:
            check(False, f"{char_id}: character.json found", f"File not found")
            continue

        check(data is not None, f"{char_id}: JSON is not empty")

        # Check each field
        check(data.get("name") == expected["name"],
              f"{char_id}: name = '{expected['name']}'",
              f"Got: '{data.get('name')}'")

        check(data.get("type") == expected["type"],
              f"{char_id}: type = '{expected['type']}'",
              f"Got: '{data.get('type')}'")

        check(data.get("home") == expected["home"],
              f"{char_id}: home = '{expected['home']}'",
              f"Got: '{data.get('home')}'")

        check(data.get("personality") == expected["personality"],
              f"{char_id}: personality = '{expected['personality']}'",
              f"Got: '{data.get('personality')}'")

        check(data.get("color_hex") == expected["color_hex"],
              f"{char_id}: color_hex = '{expected['color_hex']}'",
              f"Got: '{data.get('color_hex')}'")


def test_color_hex_validation():
    """Verify color hex values are valid and match the specification exactly."""
    print("\n" + "=" * 60)
    print("TEST 4: Color hex validation")
    print("=" * 60)

    for char_id, expected in EXPECTED_CHARACTERS.items():
        json_path = CHARACTERS_DIR / char_id / "character.json"

        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            continue

        color = data.get("color_hex", "")

        # Valid hex format: #RRGGBB
        valid_hex = bool(color.startswith("#") and len(color) == 7)
        if valid_hex:
            try:
                int(color[1:], 16)
            except ValueError:
                valid_hex = False

        check(valid_hex, f"{char_id}: valid hex format '{color}'")

        # Case-insensitive comparison for hex (both upper and lower case are fine)
        check(color.lower() == expected["color_hex"].lower(),
              f"{char_id}: color matches spec '{expected['color_hex']}'",
              f"Got: '{color}'")


def test_character_tscn_script():
    """Verify character.tscn has the character.gd script reference."""
    print("\n" + "=" * 60)
    print("TEST 5: character.tscn references character.gd script")
    print("=" * 60)

    for char_id in EXPECTED_CHARACTERS:
        tscn_path = CHARACTERS_DIR / char_id / "character.tscn"

        try:
            content = tscn_path.read_text(encoding="utf-8")
        except FileNotFoundError:
            check(False, f"{char_id}: character.tscn readable")
            continue

        # The script should be referenced as ext_resource
        has_script = "character.gd" in content
        check(has_script,
              f"{char_id}: references character.gd",
              "Script reference not found in TSCN")

        # Check for the root node having the script
        has_script_attach = 'script = ExtResource("1")' in content
        check(has_script_attach,
              f"{char_id}: script attached to root node",
              "Missing 'script = ExtResource(...)' on root node")


def test_tux_ip_removed():
    """Verify Tux-IP characters are NOT loadable from the character selection."""
    print("\n" + "=" * 60)
    print("TEST 6: Tux-IP removed from selection")
    print("=" * 60)

    for legacy_name in LEGACY_CHARACTERS:
        legacy_dir = CHARACTERS_DIR / legacy_name
        tscn_path = legacy_dir / "character.tscn"
        legacy_path = legacy_dir / "character.tscn.legacy"

        # character.tscn should NOT exist (it was renamed)
        check(not tscn_path.exists(),
              f"{legacy_name}: character.tscn NOT loadable",
              f"character.tscn still exists at {tscn_path}")

        # character.tscn.legacy SHOULD exist (preserved for reference)
        check(legacy_path.exists(),
              f"{legacy_name}: preserved as .legacy",
              f"Legacy backup not found at {legacy_path}")


def test_no_extra_characters():
    """Verify no unexpected character folders exist besides the 8 Arenians and legacy."""
    print("\n" + "=" * 60)
    print("TEST 7: No unexpected character folders")
    print("=" * 60)

    expected_folders = set(EXPECTED_CHARACTERS.keys()) | set(LEGACY_CHARACTERS)

    for entry in CHARACTERS_DIR.iterdir():
        if entry.is_dir():
            check(entry.name in expected_folders,
                  f"Folder '{entry.name}' is expected",
                  f"Unexpected character folder: {entry}")


# ── Main ──────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("Character System Test — Party Arena Milestone 5")
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Characters dir: {CHARACTERS_DIR}")
    print("=" * 60)

    test_character_plugin_folders_exist()
    test_character_required_files()
    test_character_json_validity()
    test_color_hex_validation()
    test_character_tscn_script()
    test_tux_ip_removed()
    test_no_extra_characters()

    # Summary
    total = pass_count + fail_count
    print("\n" + "=" * 60)
    print(f"RESULTS: {pass_count}/{total} passed, {fail_count}/{total} failed")
    print("=" * 60)

    if fail_count > 0:
        print(red(f"\nFAILED: {fail_count} test(s) failed"))
        sys.exit(1)
    else:
        print(green(f"\nALL {pass_count} TESTS PASSED — Milestone 5 Character System OK"))
        sys.exit(0)


if __name__ == "__main__":
    main()
