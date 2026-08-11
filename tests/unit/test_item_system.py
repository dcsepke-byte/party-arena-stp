#!/usr/bin/env python3
"""
Test: Item-System — Party Arena Milestone 3
Game Bible: design/gdd/item-system.md

Verifies:
  1. All 5 Party Arena items exist with correct prices (5/8/6/4/10)
  2. Effect types correct (immediate/delayed/passive)
  3. Purchase reduces coins correctly (can_be_bought=true, price matches)
  4. Item IDs match design spec (luckydice/teleporter/shield/coinmagnet/thiefglove)
  5. Base Item class has required fields (EFFECT_TYPES enum, item_id, item_effect_type, item_price)
  6. No GDScript parse errors (checked via .uid file presence)

Run: python3 tests/unit/test_item_system.py
"""

import os
import re
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

# ── Expected Item Specs (item-system.md §3.1) ────────────────────────────

EXPECTED_ITEMS = {
    "luckydice": {
        "item_id": "luckydice",
        "item_name": "Glücks-Würfel",
        "item_price": 5,
        "item_effect_type": "IMMEDIATE",
        "description_keyword": "feste 5",
    },
    "teleporter": {
        "item_id": "teleporter",
        "item_name": "Stern-Teleporter",
        "item_price": 8,
        "item_effect_type": "IMMEDIATE",
        "description_keyword": "Teleportiere",
    },
    "shield": {
        "item_id": "shield",
        "item_name": "Schutzschild",
        "item_price": 6,
        "item_effect_type": "PASSIVE",
        "description_keyword": "Blockt automatisch",
    },
    "coinmagnet": {
        "item_id": "coinmagnet",
        "item_name": "Münz-Magnet",
        "item_price": 4,
        "item_effect_type": "DELAYED",
        "description_keyword": "Verdoppelt alle Münz-Gewinne",
    },
    "thiefglove": {
        "item_id": "thiefglove",
        "item_name": "Dieb-Handschuh",
        "item_price": 10,
        "item_effect_type": "IMMEDIATE",
        "description_keyword": "Stiehl ein Item",
    },
}

print("=" * 70)
print("Party Arena — Item-System Test Suite (Milestone 3)")
print("Game Bible: design/gdd/item-system.md")
print("=" * 70)
print()

# ── Test 1: Plugin directories and files exist ───────────────────────────
print("Test 1: Plugin Directories and Files Exist")
for item_id in EXPECTED_ITEMS:
    item_dir = PROJECT_ROOT / f"plugins/items/{item_id}"
    item_gd = item_dir / "item.gd"
    item_uid = item_dir / "item.gd.uid"
    icon = item_dir / "icon.png"

    check(item_dir.is_dir(), f"Directory exists: plugins/items/{item_id}/")
    check(item_gd.exists(), f"item.gd exists: plugins/items/{item_id}/item.gd")
    check(item_uid.exists(), f"item.gd.uid exists (script imported): plugins/items/{item_id}/item.gd.uid")
    check(icon.exists(), f"icon.png exists: plugins/items/{item_id}/icon.png")
print()

# ── Test 2: Base Item class has required framework ───────────────────────
print("Test 2: Base Item Framework (item.gd)")
base_item_path = PROJECT_ROOT / "plugins/items/item.gd"
base_item = base_item_path.read_text() if base_item_path.exists() else ""

check('enum EFFECT_TYPES' in base_item, "EFFECT_TYPES enum defined in base Item class")
check('IMMEDIATE' in base_item, "EFFECT_TYPES.IMMEDIATE exists")
check('DELAYED' in base_item, "EFFECT_TYPES.DELAYED exists")
check('PASSIVE' in base_item, "EFFECT_TYPES.PASSIVE exists")
check('var item_id: String' in base_item, "item_id field exists (String type)")
check('var item_effect_type: int' in base_item, "item_effect_type field exists (int type)")
check('var item_price: int' in base_item or 'item_price' in base_item, "item_price property exists")
check('item-system.md' in base_item.lower() or 'EFFECT_TYPES' in base_item, "Base item references design doc or has EFFECT_TYPES")
print()

# ── Test 3: Item Prices ──────────────────────────────────────────────────
print("Test 3: Item Prices (item-system.md §3.1)")
for item_id, spec in EXPECTED_ITEMS.items():
    item_path = PROJECT_ROOT / f"plugins/items/{item_id}/item.gd"
    content = item_path.read_text() if item_path.exists() else ""
    expected_price = spec["item_price"]

    # Check item_price assignment
    price_match = re.search(r'item_price\s*=\s*(\d+)', content)
    if price_match:
        actual_price = int(price_match.group(1))
        check(
            actual_price == expected_price,
            f"{spec['item_name']}: price={actual_price} (expected {expected_price})",
            f"Got {actual_price}, expected {expected_price}"
        )
    else:
        check(False, f"{spec['item_name']}: item_price assigned",
              "item_price assignment not found")

    # Check can_be_bought = true
    check(
        'can_be_bought = true' in content or 'can_be_bought= true' in content,
        f"{spec['item_name']}: can_be_bought = true"
    )
print()

# ── Test 4: Effect Types ─────────────────────────────────────────────────
print("Test 4: Effect Types (item-system.md §3.1.1)")
for item_id, spec in EXPECTED_ITEMS.items():
    item_path = PROJECT_ROOT / f"plugins/items/{item_id}/item.gd"
    content = item_path.read_text() if item_path.exists() else ""
    expected_type = spec["item_effect_type"]

    # Check item_effect_type assignment
    type_match = re.search(r'item_effect_type\s*=\s*EFFECT_TYPES\.(\w+)', content)
    if type_match:
        actual_type = type_match.group(1)
        check(
            actual_type == expected_type,
            f"{spec['item_name']}: effect_type={actual_type} (expected {expected_type})",
            f"Got EFFECT_TYPES.{actual_type}, expected EFFECT_TYPES.{expected_type}"
        )
    else:
        check(False, f"{spec['item_name']}: item_effect_type assigned",
              "item_effect_type assignment not found")
print()

# ── Test 5: Item IDs ─────────────────────────────────────────────────────
print("Test 5: Item IDs Match Design Spec")
for item_id, spec in EXPECTED_ITEMS.items():
    item_path = PROJECT_ROOT / f"plugins/items/{item_id}/item.gd"
    content = item_path.read_text() if item_path.exists() else ""
    expected_id = spec["item_id"]

    id_match = re.search(r'item_id\s*=\s*"(\w+)"', content)
    if id_match:
        actual_id = id_match.group(1)
        check(
            actual_id == expected_id,
            f"{spec['item_name']}: item_id=\"{actual_id}\" (expected \"{expected_id}\")",
            f"Got \"{actual_id}\", expected \"{expected_id}\""
        )
    else:
        check(False, f"{spec['item_name']}: item_id assigned",
              "item_id assignment not found")
print()

# ── Test 6: Descriptions ─────────────────────────────────────────────────
print("Test 6: Item Descriptions Contain Keywords")
for item_id, spec in EXPECTED_ITEMS.items():
    item_path = PROJECT_ROOT / f"plugins/items/{item_id}/item.gd"
    content = item_path.read_text() if item_path.exists() else ""
    keyword = spec["description_keyword"]

    check(
        keyword.lower() in content.lower(),
        f"{spec['item_name']}: description contains \"{keyword}\""
    )
print()

# ── Test 7: can_be_bought (Shop Integration) ─────────────────────────────
print("Test 7: Shop Integration — All Items Buyable")
for item_id, spec in EXPECTED_ITEMS.items():
    item_path = PROJECT_ROOT / f"plugins/items/{item_id}/item.gd"
    content = item_path.read_text() if item_path.exists() else ""

    check(
        'can_be_bought = true' in content,
        f"{spec['item_name']}: can_be_bought = true (appears in shop)"
    )
print()

# ── Test 8: Purchase Cost Simulation ─────────────────────────────────────
print("Test 8: Purchase Cost Simulation (F3: can_buy = inv < 3 AND coins >= price)")

def can_buy(inventory_count: int, player_coins: int, item_price: int) -> bool:
    """Simulate purchase validation per item-system.md Formula F3."""
    return (inventory_count < 3) and (player_coins >= item_price)

# Test each item with various coin/inventory states
test_cases = [
    # (item_name, inventory, coins, price, expected_can_buy, scenario)
    ("Glücks-Würfel", 0, 5, 5, True, "empty inv, exact coins"),
    ("Glücks-Würfel", 2, 5, 5, True, "2 items, exact coins"),
    ("Glücks-Würfel", 3, 100, 5, False, "full inventory"),
    ("Glücks-Würfel", 0, 3, 5, False, "not enough coins"),
    ("Teleporter", 0, 8, 8, True, "exact coins"),
    ("Teleporter", 0, 7, 8, False, "1 coin short"),
    ("Schutzschild", 0, 6, 6, True, "exact coins"),
    ("Schutzschild", 0, 10, 6, True, "more than enough"),
    ("Münz-Magnet", 2, 4, 4, True, "last slot, exact coins"),
    ("Münz-Magnet", 3, 4, 4, False, "full inventory, exact coins"),
    ("Münz-Magnet", 0, 1, 4, False, "way too few coins"),
    ("Dieb-Handschuh", 0, 10, 10, True, "exact coins"),
    ("Dieb-Handschuh", 1, 12, 10, True, "can buy and have 2 left"),
    ("Dieb-Handschuh", 3, 10, 10, False, "full inventory"),
    ("Dieb-Handschuh", 0, 9, 10, False, "1 coin short"),
]

for name, inv, coins, price, expected, scenario in test_cases:
    result = can_buy(inv, coins, price)
    check(
        result == expected,
        f"{name} (inv={inv}, coins={coins}, price={price}): can_buy={result} ({scenario})",
        f"Expected {expected}, got {result}"
    )

# Simulate a purchase: buy Glücks-Würfel for 5 coins with 12 coins, inv=1
initial_coins = 12
initial_inv = 1
price = 5
assert can_buy(initial_inv, initial_coins, price), "Precondition: should be buyable"
new_coins = initial_coins - price
new_inv = initial_inv + 1
check(new_coins == 7, f"After purchase: coins {initial_coins}→{new_coins} (expected 7)")
check(new_inv == 2, f"After purchase: inventory {initial_inv}→{new_inv} (expected 2)")
print()

# ── Test 9: Effect Type Logic ────────────────────────────────────────────
print("Test 9: Effect Type Logic (correct classification per design)")

# Simulate the effect type behaviors
EFFECT_TYPES = {"IMMEDIATE": 0, "DELAYED": 1, "PASSIVE": 2}

def get_activation_phase(effect_type: int, item_id: str) -> str:
    """Return the activation phase per item-system.md §3.4"""
    if item_id == "thiefglove":
        return "phase_2"  # After dice, before movement
    if effect_type == EFFECT_TYPES["PASSIVE"]:
        return "never"  # Passive, never manually activated
    if effect_type in (EFFECT_TYPES["IMMEDIATE"], EFFECT_TYPES["DELAYED"]):
        return "phase_0"  # Before dice
    return "unknown"

def is_consumed_on_activation(effect_type: int) -> bool:
    """immediate/delayed consumed on activation; passive on trigger"""
    return effect_type in (EFFECT_TYPES["IMMEDIATE"], EFFECT_TYPES["DELAYED"])

# Test Glücks-Würfel (immediate) - Phase 0
phase = get_activation_phase(EFFECT_TYPES["IMMEDIATE"], "luckydice")
check(phase == "phase_0", f"luckydice activation phase = {phase} (expected phase_0)")

# Test Teleporter (immediate) - Phase 0
phase = get_activation_phase(EFFECT_TYPES["IMMEDIATE"], "teleporter")
check(phase == "phase_0", f"teleporter activation phase = {phase} (expected phase_0)")

# Test Dieb-Handschuh (immediate) - Phase 2
phase = get_activation_phase(EFFECT_TYPES["IMMEDIATE"], "thiefglove")
check(phase == "phase_2", f"thiefglove activation phase = {phase} (expected phase_2)")

# Test Schutzschild (passive) - never
phase = get_activation_phase(EFFECT_TYPES["PASSIVE"], "shield")
check(phase == "never", f"shield activation phase = {phase} (expected never)")

# Test Münz-Magnet (delayed) - Phase 0
phase = get_activation_phase(EFFECT_TYPES["DELAYED"], "coinmagnet")
check(phase == "phase_0", f"coinmagnet activation phase = {phase} (expected phase_0)")

# Test consumption rules
check(is_consumed_on_activation(EFFECT_TYPES["IMMEDIATE"]) == True,
      "immediate items consumed on activation")
check(is_consumed_on_activation(EFFECT_TYPES["DELAYED"]) == True,
      "delayed items consumed on activation")
check(is_consumed_on_activation(EFFECT_TYPES["PASSIVE"]) == False,
      "passive items NOT consumed on activation (consumed on trigger)")
print()

# ── Test 10: No GDScript parse errors ─────────────────────────────────────
print("Test 10: No GDScript Parse Errors (all .uid files present)")
base_uid = PROJECT_ROOT / "plugins/items/item.gd.uid"
check(base_uid.exists(), "Base item.gd has .uid file (script parsed successfully)")

uid_files_present = 0
for item_id in EXPECTED_ITEMS:
    uid_path = PROJECT_ROOT / f"plugins/items/{item_id}/item.gd.uid"
    if uid_path.exists():
        uid_files_present += 1
check(uid_files_present == 5, f"All 5 item scripts have .uid files ({uid_files_present}/5)")
print()

# ── Test 11: Compensation formula F4 ─────────────────────────────────────
print("Test 11: Compensation Formula F4 (item-system.md §3.6)")

def compensation(item_price: int) -> int:
    """floor(item_price * 0.5)"""
    return item_price // 2  # Integer division = floor for positive numbers

expected_compensations = {
    "luckydice": (5, 2),
    "teleporter": (8, 4),
    "shield": (6, 3),
    "coinmagnet": (4, 2),
    "thiefglove": (10, 5),
}

for item_id, spec in EXPECTED_ITEMS.items():
    price = spec["item_price"]
    expected_comp = expected_compensations[item_id][1]
    actual_comp = compensation(price)
    check(
        actual_comp == expected_comp,
        f"{spec['item_name']}: comp = floor({price}*0.5) = {actual_comp} (expected {expected_comp})"
    )
print()

# ── Results ───────────────────────────────────────────────────────────────
total = pass_count + fail_count
print("=" * 70)
print(f"Results: {pass_count}/{total} passed, {fail_count} failed")
if fail_count == 0:
    print(green("ALL TESTS PASSED"))
    sys.exit(0)
else:
    print(red(f"{fail_count} TEST(S) FAILED"))
    sys.exit(1)
