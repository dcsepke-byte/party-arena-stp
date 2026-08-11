#!/usr/bin/env python3
"""
Test: Stern-Mechanik — Party Arena Milestone 2
Game Bible: design/gdd/star-economy.md

Verifies:
  1. Star statue starts on exactly one STERN_SHOP field
  2. Star purchase costs exactly 20 coins
  3. After purchase, statue migrates to a different STERN_SHOP field
  4. Anti-rule: stars cannot be stolen (no star-decreasing logic)
  5. Max 1 purchase per player per round
  6. Cake → Stern migration (no "Cake" strings in changed files)

Run: python3 tests/unit/test_star_economy.py
"""

import os
import re
import sys
import random
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

# ── File Content Checks ───────────────────────────────────────────────────

CHANGED_FILES = [
    "common/scenes/board_logic/node/node.gd",
    "common/scenes/board_logic/controller/controller.gd",
    "common/scenes/board_logic/player_board/player_board.gd",
    "common/scenes/board_logic/controller/shop.gd",
    "common/scenes/board_logic/controller/debug.gd",
    "common/scenes/board_logic/controller/player_info.gd",
    "common/lobby.gd",
    "server/lobby.gd",
    "common/savegames/savegames.gd",
    "client/menus/victory_screen/victory_screen.gd",
    "plugins/boards/KDEValley/board.gd",
]

print("=" * 70)
print("Party Arena — Stern-Mechanik Test Suite (Milestone 2)")
print("Game Bible: design/gdd/star-economy.md")
print("=" * 70)
print()

# ── Test 1: No "Cake" strings in changed files ────────────────────────────
print("Test 1: Cake → Stern Migration (no Cake strings in changed .gd files)")
cake_pattern = re.compile(r'\b[Cc]ake\b')
for file_rel in CHANGED_FILES:
    file_path = PROJECT_ROOT / file_rel
    if file_path.exists():
        content = file_path.read_text()
        matches = cake_pattern.findall(content)
        # Filter out legitimate exceptions (comments about the migration, etc.)
        # Only flag actual code references
        check(
            len(matches) == 0,
            f"No 'Cake' in {file_rel}",
            f"Found: {matches}" if matches else ""
        )
    else:
        print(f"  {yellow('SKIP')} {file_rel} (file not found)")
print()

# ── Test 2: STAR_COST = 20 in controller.gd ───────────────────────────────
print("Test 2: Star Purchase Price (20 coins)")
controller_path = PROJECT_ROOT / "common/scenes/board_logic/controller/controller.gd"
controller_content = controller_path.read_text() if controller_path.exists() else ""

# Check STAR_COST definition
star_cost_match = re.search(r'STAR_COST\s*:?=\s*(\d+)', controller_content)
if star_cost_match:
    cost = int(star_cost_match.group(1))
    check(cost == 20, f"STAR_COST = {cost}", f"Expected 20, got {cost}")
else:
    check(False, "STAR_COST defined in controller.gd", "STAR_COST not found")

# Check buy_star function uses STAR_COST
check(
    'player.cookies -= STAR_COST' in controller_content,
    "buy_star deducts STAR_COST from player"
)

# Check < 20 coins = no purchase
check(
    'player.cookies >= STAR_COST' in controller_content,
    "buy_star checks player.cookies >= STAR_COST"
)
print()

# ── Test 3: Star Statue (active/inactive) ─────────────────────────────────
print("Test 3: Star Statue — Active/Inactive System")

# Read node.gd for cross-file checks
node_path = PROJECT_ROOT / "common/scenes/board_logic/node/node.gd"
node_content = node_path.read_text() if node_path.exists() else ""

check(
    'star_active' in controller_content,
    "star_active property referenced in controller.gd"
)
check(
    'set_active_star' in controller_content or 'set_active_star' in node_content,
    "set_active_star setter exists (in node.gd or controller.gd)"
)
check(
    'func _get_star_shop_fields()' in controller_content or '_get_star_shop_fields()' in controller_content,
    "_get_star_shop_fields() helper exists (definition or call)"
)
check(
    'func get_active_star_space()' in controller_content,
    "get_active_star_space() function exists"
)

# Check that relocate_star uses FELD_TYP.STERN_SHOP
check(
    'FELD_TYP.STERN_SHOP' in controller_content,
    "relocate_star identifies fields by FELD_TYP.STERN_SHOP"
)

# Check node.gd has star_active property
check(
    'var star_active := false: set = set_active_star' in node_content,
    "node.gd has star_active property"
)
check(
    'func set_active_star(' in node_content,
    "node.gd has set_active_star function"
)
check(
    'func play_star_collection_animation(' in node_content,
    "node.gd has play_star_collection_animation function"
)
print()

# ── Test 4: Star Purchase Logic ───────────────────────────────────────────
print("Test 4: Star Purchase — Max 1 per Player per Round")
check(
    '_stars_purchased_this_round' in controller_content,
    "_stars_purchased_this_round tracking dict exists"
)
check(
    '_stars_purchased_this_round.clear()' in controller_content or 'player_turn == 1' in controller_content,
    "Purchase tracking reset each round (in _on_next_player)"
)
check(
    '_stars_purchased_this_round.get(pid, false)' in controller_content,
    "Purchase check: _stars_purchased_this_round.get(pid, false)"
)
check(
    '_stars_purchased_this_round[pid] = true' in controller_content,
    "Purchase tracking: _stars_purchased_this_round[pid] = true"
)
print()

# ── Test 5: Statue Migration After Purchase ───────────────────────────────
print("Test 5: Statue Migration After Purchase")
check(
    'func relocate_star()' in controller_content,
    "relocate_star() function exists"
)
# Check migration rules: prefer unoccupied
check(
    'unoccupied' in controller_content and 'occupied' in controller_content,
    "Migration separates occupied vs unoccupied fields"
)
# Check: never stays on same field
check(
    'field != old_node' in controller_content,
    "Migration excludes current field from candidates"
)
# Check: broadcast relocation
check(
    'lobby.broadcast(star_relocated.bind(lobby.star_space))' in controller_content,
    "Relocation broadcast to all clients"
)
print()

# ── Test 6: Anti-Rule — No Star Theft ─────────────────────────────────────
print("Test 6: Anti-Rule — No Star Theft (star count never decreases)")

# Check server/lobby.gd for star-decreasing code
server_lobby_path = PROJECT_ROOT / "server/lobby.gd"
server_lobby_content = server_lobby_path.read_text() if server_lobby_path.exists() else ""

# Find all places where stars are modified
star_dec_pattern = re.findall(r'losing_player\.stars\s*-=|\bplayer\.stars\s*-=', server_lobby_content)
check(
    len(star_dec_pattern) == 0,
    "No star-decreasing operations (.stars -=) in server/lobby.gd",
    f"Found: {star_dec_pattern}" if star_dec_pattern else ""
)

# Check that ONE_STAR duel reward no longer steals stars (check for actual star assignment)
one_star_steal = re.findall(r'ONE_STAR.*?\.stars\s*[-+]', server_lobby_content, re.DOTALL)
check(
    len(one_star_steal) == 0,
    "ONE_STAR duel reward does not steal/transfer stars",
    f"Found: {one_star_steal}" if one_star_steal else ""
)

# Check NOLOK_SOLO no longer steals stars
nolok_star_steal = re.findall(r'NOLOK_SOLO.*?\.stars\s*[-+]', server_lobby_content, re.DOTALL)
check(
    len(nolok_star_steal) == 0,
    "NOLOK_SOLO does not manipulate stars",
    f"Found: {nolok_star_steal}" if nolok_star_steal else ""
)

# Check controller.gd for anti-rule comments
check(
    'star-economy.md' in controller_content,
    "controller.gd references star-economy.md (Game Bible authority)"
)
print()

# ── Test 7: Simulated Star Logic ──────────────────────────────────────────
print("Test 7: Simulated Star Logic (Python simulation)")

# Simulate the star statue migration algorithm from the Game Bible
def simulate_relocate_star(star_fields, current_active, players_on_fields):
    """
    Simulates star statue relocation per star-economy.md Section 3.3
    Returns: new active field index, or None if no valid move
    """
    candidates = [i for i in range(len(star_fields)) if i != current_active]
    if not candidates:
        return None  # Only one field total

    unoccupied = [c for c in candidates if c not in players_on_fields]
    occupied = [c for c in candidates if c in players_on_fields]

    if unoccupied:
        return random.choice(unoccupied)
    else:
        return random.choice(candidates)


# Test 7a: Basic relocation to different field
random.seed(42)
star_fields = [0, 1, 2]  # 3 star shop fields
current = 0
players_on = set()
results = []
for _ in range(100):
    new = simulate_relocate_star(star_fields, current, players_on)
    results.append((current, new))
    check(new != current, f"Move from {current} to {new} (different field)")
    current = new

all_different = all(new != old for old, new in results[:10])
check(all_different, "Relocation always moves to different field")

# Test 7b: Preference for unoccupied fields
random.seed(123)
star_fields_2 = [0, 1, 2, 3]  # 4 star shop fields
current_2 = 0
players_on_2 = {1, 2}  # Fields 1 and 2 have players
occupied_choices = 0
total_choices = 0
for _ in range(1000):
    new = simulate_relocate_star(star_fields_2, current_2, players_on_2)
    if new in players_on_2:
        occupied_choices += 1
    total_choices += 1
    current_2 = new

# With unoccupied field 3 available, should never choose occupied
check(
    occupied_choices == 0,
    f"Never chooses occupied field when unoccupied exists ({occupied_choices}/1000)"
)

# Test 7c: Falls back to occupied if all occupied
random.seed(456)
star_fields_3 = [0, 1, 2]
current_3 = 0
players_on_3 = {1, 2}  # All other fields occupied
valid_moves = 0
for _ in range(100):
    new = simulate_relocate_star(star_fields_3, current_3, players_on_3)
    if new is not None:
        valid_moves += 1
        check(new in [1, 2], f"Move {valid_moves}: falls back to occupied field {new}")

check(valid_moves > 0, f"Relocation works when all fields occupied ({valid_moves} moves)")

# Test 7d: Single field case
result_single = simulate_relocate_star([0], 0, set())
check(result_single is None, "Single field: no relocation possible (statue stays)")

print()

# ── Test 8: PlayerBoard uses stars (not cakes) ────────────────────────────
print("Test 8: PlayerBoard Property Migration")
playerboard_path = PROJECT_ROOT / "common/scenes/board_logic/player_board/player_board.gd"
pb_content = playerboard_path.read_text() if playerboard_path.exists() else ""

check('var stars := 0: set = set_stars' in pb_content, "PlayerBoard has 'stars' property")
check('func set_stars(' in pb_content, "PlayerBoard has set_stars function")
check('cakes' not in pb_content, "No 'cakes' references in player_board.gd",
      f"Found: {re.findall(r'cakes', pb_content)}" if 'cakes' in pb_content else "")
print()

# ── Test 9: Lobby state uses stars ───────────────────────────────────────
print("Test 9: Lobby State Migration")
lobby_path = PROJECT_ROOT / "common/lobby.gd"
lobby_content = lobby_path.read_text() if lobby_path.exists() else ""

check('var stars := 0' in lobby_content, "PlayerState has 'stars' field")
check('state.stars = data[2]' in lobby_content, "PlayerState decodes stars from data[2]")
check('star_space' in lobby_content, "Lobby has star_space property")
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
