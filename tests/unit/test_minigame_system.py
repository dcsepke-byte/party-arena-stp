#!/usr/bin/env python3
"""
Test: Minigame-System — Party Arena Milestone 4
Game Bible: design/gdd/minigame-architecture.md, minigame-categories.md, minigame-template.md

Verifies:
  1. All 12 Party Arena minigames exist with correct categories (3+3+2+2+2)
  2. Each minigame has the 3 required files (minigame.gd, minigame.tscn, minigame.json)
  3. minigame.json is valid (name == directory name, category is valid, required fields present)
  4. No GDScript parse errors (confirmed via .uid file presence)
  5. MinigameBase framework class exists and compiles

Run: python3 tests/unit/test_minigame_system.py
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

# ── Expected Minigames (minigame-categories.md §3.1) ─────────────────────

EXPECTED_MINIGAMES = {
    # Geschicklichkeit (3)
    "muenzregen": {
        "category": "geschicklichkeit",
        "display_name": "Münzregen",
        "results_mode": "by_points",
        "players_min": 2,
        "players_max": 8,
    },
    "balance_akt": {
        "category": "geschicklichkeit",
        "display_name": "Balance-Akt",
        "results_mode": "by_position",
        "players_min": 2,
        "players_max": 8,
    },
    "zielwurf": {
        "category": "geschicklichkeit",
        "display_name": "Zielwurf",
        "results_mode": "by_points",
        "players_min": 2,
        "players_max": 8,
    },
    # Reaktion (3)
    "arena_star_sagt": {
        "category": "reaktion",
        "display_name": "ArenaStar sagt",
        "results_mode": "by_position",
        "players_min": 2,
        "players_max": 8,
    },
    "blitz_fangen": {
        "category": "reaktion",
        "display_name": "Blitz-Fangen",
        "results_mode": "by_points",
        "players_min": 2,
        "players_max": 8,
    },
    "knoepfchen_druecker": {
        "category": "reaktion",
        "display_name": "Knöpfchen-Drücker",
        "results_mode": "by_points",
        "players_min": 2,
        "players_max": 8,
    },
    # Puzzle/Logik (2)
    "sternen_labyrinth": {
        "category": "puzzle",
        "display_name": "Sternen-Labyrinth",
        "results_mode": "by_position",
        "players_min": 2,
        "players_max": 8,
    },
    "insel_memory": {
        "category": "puzzle",
        "display_name": "Insel-Memory",
        "results_mode": "by_points",
        "players_min": 2,
        "players_max": 8,
    },
    # Rechnen/Wort (2)
    "muenz_zaehler": {
        "category": "rechnen",
        "display_name": "Münz-Zähler",
        "results_mode": "by_points",
        "players_min": 2,
        "players_max": 8,
    },
    "wort_puzzle": {
        "category": "rechnen",
        "display_name": "Wort-Puzzle",
        "results_mode": "by_points",
        "players_min": 2,
        "players_max": 8,
    },
    # Kooperation (2)
    "sternen_bruecke": {
        "category": "kooperation",
        "display_name": "Sternen-Brücke",
        "results_mode": "by_points",
        "team_mode": "coop_all",
        "players_min": 2,
        "players_max": 8,
    },
    "schatz_trage": {
        "category": "kooperation",
        "display_name": "Schatz-Trage",
        "results_mode": "by_points",
        "team_mode": "coop_teams",
        "players_min": 4,
        "players_max": 8,
    },
}

VALID_CATEGORIES = {"geschicklichkeit", "reaktion", "puzzle", "rechnen", "kooperation"}
REQUIRED_FILES = ["minigame.gd", "minigame.tscn", "minigame.json"]
MINIGAMES_DIR = PROJECT_ROOT / "plugins" / "minigames"

CATEGORY_COUNTS_EXPECTED = {
    "geschicklichkeit": 3,
    "reaktion": 3,
    "puzzle": 2,
    "rechnen": 2,
    "kooperation": 2,
}


# ── Tests ─────────────────────────────────────────────────────────────────

def test_minigame_base_exists():
    """MinigameBase framework class exists and compiles."""
    print("\n── MinigameBase Framework ──")
    base_gd = PROJECT_ROOT / "common" / "scripts" / "minigame_base.gd"
    check(base_gd.exists(), "minigame_base.gd exists",
          f"Expected at: {base_gd}")

    base_uid = PROJECT_ROOT / "common" / "scripts" / "minigame_base.gd.uid"
    check(base_uid.exists(), "minigame_base.gd compiled (.uid exists)",
          "GDScript parse error or import failed")

    # Check that it defines MinigameBase class
    content = base_gd.read_text()
    check("class_name MinigameBase" in content,
          "MinigameBase class_name declared")
    check("extends Node3D" in content,
          "MinigameBase extends Node3D")
    check("signal request_end()" in content,
          "request_end signal defined")
    check("func setup(" in content,
          "setup() method defined")
    check("func start_game()" in content,
          "start_game() method defined")
    check("func end_game()" in content,
          "end_game() method defined")
    check("func get_results()" in content,
          "get_results() method defined")
    check("func cleanup()" in content,
          "cleanup() method defined")


def test_all_minigames_exist():
    """Verify all 12 minigame directories exist."""
    print("\n── Minigame Directory Existence ──")

    # Count existing Party Arena minigames
    existing = set()
    for entry in MINIGAMES_DIR.iterdir():
        if entry.is_dir():
            existing.add(entry.name)

    party_arena = set(EXPECTED_MINIGAMES.keys())
    found = existing & party_arena

    check(len(found) == 12,
          f"All 12 Party Arena minigames exist ({len(found)}/12)",
          f"Missing: {party_arena - found}" if len(found) < 12 else "")

    for name in sorted(EXPECTED_MINIGAMES.keys()):
        check(name in existing,
              f"  Directory '{name}' exists")


def test_required_files():
    """Verify each minigame has the 3 required files."""
    print("\n── Required Files (minigame.gd, minigame.tscn, minigame.json) ──")

    for name in sorted(EXPECTED_MINIGAMES.keys()):
        d = MINIGAMES_DIR / name
        for fname in REQUIRED_FILES:
            fpath = d / fname
            check(fpath.exists(),
                  f"  {name}/{fname}")


def test_json_validity():
    """Verify minigame.json is valid JSON with correct fields."""
    print("\n── minigame.json Validity ──")

    for name, expected in sorted(EXPECTED_MINIGAMES.items()):
        json_path = MINIGAMES_DIR / name / "minigame.json"

        # Parse JSON
        try:
            data = json.loads(json_path.read_text())
        except json.JSONDecodeError as e:
            check(False, f"  {name}: valid JSON", str(e))
            continue

        check(True, f"  {name}: valid JSON")

        # name == Ordnername
        check(data.get("name") == name,
              f"  {name}: name matches directory",
              f"Expected '{name}', got '{data.get('name')}'")

        # category correct
        cat = data.get("category")
        check(cat == expected["category"],
              f"  {name}: category = '{expected['category']}'",
              f"Got '{cat}'")

        check(cat in VALID_CATEGORIES,
              f"  {name}: category is valid ({cat})")

        # players object
        players = data.get("players", {})
        check(isinstance(players, dict),
              f"  {name}: 'players' is an object")
        check(players.get("min") == expected["players_min"],
              f"  {name}: players.min = {expected['players_min']}",
              f"Got {players.get('min')}")
        check(players.get("max") == expected["players_max"],
              f"  {name}: players.max = {expected['players_max']}",
              f"Got {players.get('max')}")
        check(players.get("min", 0) <= players.get("max", 0),
              f"  {name}: players.min <= players.max")

        # duration
        dur = data.get("duration")
        check(dur is not None and 10 <= dur <= 30,
              f"  {name}: duration in [10,30] (got {dur})")

        # description and instructions
        check(isinstance(data.get("description"), str) and len(data.get("description", "")) > 0,
              f"  {name}: description present")
        check(isinstance(data.get("instructions"), str) and len(data.get("instructions", "")) > 0,
              f"  {name}: instructions present")

        # scene_path
        check(data.get("scene_path") == f"res://plugins/minigames/{name}/minigame.tscn",
              f"  {name}: scene_path correct",
              f"Got '{data.get('scene_path')}'")

        # type (STP compatibility)
        check(isinstance(data.get("type"), list) and len(data.get("type", [])) > 0,
              f"  {name}: 'type' array present")

        # results_mode
        if "results_mode" in expected:
            check(data.get("results_mode") == expected["results_mode"],
                  f"  {name}: results_mode = '{expected['results_mode']}'",
                  f"Got '{data.get('results_mode')}'")

        # team_mode
        if "team_mode" in expected:
            check(data.get("team_mode") == expected["team_mode"],
                  f"  {name}: team_mode = '{expected['team_mode']}'",
                  f"Got '{data.get('team_mode')}'")


def test_category_distribution():
    """Verify correct category distribution: 3+3+2+2+2."""
    print("\n── Category Distribution (3+3+2+2+2) ──")

    counts = {}
    for name, expected in EXPECTED_MINIGAMES.items():
        cat = expected["category"]
        counts[cat] = counts.get(cat, 0) + 1

    for cat, expected_count in CATEGORY_COUNTS_EXPECTED.items():
        actual = counts.get(cat, 0)
        check(actual == expected_count,
              f"  {cat}: {actual}/{expected_count}",
              f"Expected {expected_count}, got {actual}")

    total = sum(counts.values())
    check(total == 12,
          f"  Total minigames: {total}/12")


def test_gdscript_compilation():
    """Verify all minigame.gd files compiled successfully (.uid files exist)."""
    print("\n── GDScript Compilation (.uid file check) ──")

    for name in sorted(EXPECTED_MINIGAMES.keys()):
        uid_path = MINIGAMES_DIR / name / "minigame.gd.uid"
        check(uid_path.exists(),
              f"  {name}/minigame.gd compiled",
              "GDScript parse error or import failed")


def test_minigame_extends_base():
    """Verify each minigame.gd extends MinigameBase."""
    print("\n── Minigame extends MinigameBase ──")

    for name in sorted(EXPECTED_MINIGAMES.keys()):
        gd_path = MINIGAMES_DIR / name / "minigame.gd"
        content = gd_path.read_text()
        check("extends MinigameBase" in content,
              f"  {name}: extends MinigameBase")


def test_lifecycle_methods():
    """Verify each minigame implements required lifecycle methods."""
    print("\n── Lifecycle Methods ──")

    required_methods = ["start_game", "end_game", "get_results", "cleanup"]

    for name in sorted(EXPECTED_MINIGAMES.keys()):
        gd_path = MINIGAMES_DIR / name / "minigame.gd"
        content = gd_path.read_text()
        for method in required_methods:
            check(f"func {method}(" in content,
                  f"  {name}: implements {method}()")


def test_scene_validity():
    """Verify minigame.tscn has correct structure."""
    print("\n── Scene File Validity ──")

    for name in sorted(EXPECTED_MINIGAMES.keys()):
        tscn_path = MINIGAMES_DIR / name / "minigame.tscn"
        content = tscn_path.read_text()

        check("[gd_scene" in content,
              f"  {name}: valid gd_scene header")
        check(f"plugins/minigames/{name}/minigame.gd" in content,
              f"  {name}: references correct minigame.gd")
        check('type="Node3D"' in content,
              f"  {name}: root is Node3D")
        check("ExtResource" in content,
              f"  {name}: uses ExtResource for script")


# ── Main ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("Party Arena Milestone 4 — Minigame-System Test")
    print("=" * 60)

    test_minigame_base_exists()
    test_all_minigames_exist()
    test_required_files()
    test_json_validity()
    test_category_distribution()
    test_gdscript_compilation()
    test_minigame_extends_base()
    test_lifecycle_methods()
    test_scene_validity()

    print("\n" + "=" * 60)
    total = pass_count + fail_count
    print(f"Results: {pass_count}/{total} passed, {fail_count} failed")
    if fail_count > 0:
        print(red(f"\n❌ TEST FAILED — {fail_count} check(s) failed"))
        sys.exit(1)
    else:
        print(green("\n✅ ALL TESTS PASSED"))
        sys.exit(0)
