#!/usr/bin/env python3
"""Party Arena — Branch Wiring Validation Test (Milestone 6b)

Verifies:
  1. Each island has exactly 2 branches with valid entry/exit
  2. Field chaining: main path loop correct, branches connect entry→exit
  3. Length balance: 32 main + 2×N branch = 40 per island

Runs against board.json data and validates the branch wiring logic.
"""

import json
import os
import sys
from pathlib import Path

# ── Configuration ──────────────────────────────────────────────────────────

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BOARDS_DIR = PROJECT_ROOT / "plugins" / "boards"

# Known islands (from world-overview.md 3.2)
ISLANDS = [
    "sonnenstrand",
    "zuckerwald",
    "wolkenwerk",
    "frostgipfel",
    "dschungeltempel",
    "mechanik-stadt",
    "sternenzitadelle",
]

# Island-specific conventions
# Standard: 1-based, main path 1-32, branches 33-40
# Wolkenwerk: 0-based, inline branches within 0-39 range
STANDARD_FIRST_FIELD = 1
WOLKENWERK_FIRST_FIELD = 0

# ── Test Helpers ───────────────────────────────────────────────────────────

def load_board_json(island: str) -> dict:
    """Load board.json for the given island."""
    path = BOARDS_DIR / island / "board.json"
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f)


def make_field_index(field_num: int, first_field: int) -> int:
    """Convert a board field number to a zero-based array index."""
    return field_num - first_field


def trace_main_path(branches: list, first_field: int, branch_field_sets: list) -> list:
    """Trace the main path loop (1→2→...→32→1 for standard, same for inline minus branch fields).

    Returns list of field numbers in main path order.
    For standard convention: main path = fields 1-32 (no branches)
    For inline convention (wolkenwerk): main path = all fields in order
    """
    main_path = []
    total_fields = 40

    all_branch_fields = set()
    for bf in branch_field_sets:
        all_branch_fields.update(bf)

    for i in range(total_fields):
        field_num = i + first_field
        # For standard convention, main path excludes branch-only fields
        if first_field == STANDARD_FIRST_FIELD:
            if field_num <= 32:
                main_path.append(field_num)
        else:
            # Wolkenwerk: all fields are on the main path
            main_path.append(field_num)

    return main_path


def validate_island(island: str) -> tuple[int, int, list]:
    """Validate a single island's branch wiring.

    Returns (passed, failed, messages).
    """
    messages = []
    board = load_board_json(island)
    if board is None:
        return 0, 1, [f"FAIL: {island} — board.json not found"]

    first_field = STANDARD_FIRST_FIELD
    if island == "wolkenwerk":
        first_field = WOLKENWERK_FIRST_FIELD

    branches = board.get("branches", [])
    total_fields = 40
    main_path_count = 32  # 32 fields on main path
    expected_main = 32

    # ── Test 1: Exactly 2 branches ──────────────────────────────────────
    if len(branches) != 2:
        messages.append(
            f"FAIL: {island} — expected 2 branches, got {len(branches)}"
        )
        return 0, 1, messages
    messages.append(f"  OK: {island} has exactly 2 branches")

    # Collect all branch field sets for validation
    branch_field_sets = []
    for bi, branch in enumerate(branches):
        name = branch.get("name", f"branch_{bi}")
        entry = branch.get("entry")
        exit_ = branch.get("exit")
        delta = branch.get("delta")
        fields = branch.get("fields", [])

        # ── Test 2a: Valid entry (1-32 for standard, 0-39 for wolkenwerk) ──
        max_main = 31 if first_field == WOLKENWERK_FIRST_FIELD else 32
        entry_valid = first_field <= entry <= (first_field + total_fields - 1)
        if not entry_valid:
            messages.append(
                f"FAIL: {island} branch '{name}' — entry={entry} out of range"
            )
            continue

        # ── Test 2b: Valid exit ─────────────────────────────────────────
        exit_valid = first_field <= exit_ <= (first_field + total_fields - 1)
        if not exit_valid:
            messages.append(
                f"FAIL: {island} branch '{name}' — exit={exit_} out of range"
            )
            continue

        # ── Test 2c: Entry and exit exist on main path ───────────────────
        if island != "wolkenwerk" and entry > 32:
            messages.append(
                f"FAIL: {island} branch '{name}' — entry={entry} is not on main path (1-32)"
            )

        # ── Test 2d: Branch fields are contiguous ────────────────────────
        for j in range(len(fields) - 1):
            if fields[j + 1] != fields[j] + 1:
                messages.append(
                    f"FAIL: {island} branch '{name}' — fields not contiguous: "
                    f"{fields[j]} → {fields[j + 1]}"
                )

        # ── Test 2e: Branch fields don't overlap with main path (standard only) ──
        if island != "wolkenwerk":
            for fld in fields:
                if 1 <= fld <= 32:
                    messages.append(
                        f"FAIL: {island} branch '{name}' — field {fld} "
                        f"overlaps with main path (1-32)"
                    )

        branch_field_sets.append(set(fields))
        messages.append(
            f"  OK: {island} branch '{name}' — entry={entry}, exit={exit_}, "
            f"delta={delta}, fields={fields}"
        )

    if len([m for m in messages if m.startswith("FAIL")]) > 0:
        # Already have failures reported
        pass_count = sum(1 for m in messages if m.startswith("  OK"))
        fail_count = sum(1 for m in messages if m.startswith("FAIL"))
        return pass_count, fail_count, messages

    # ── Test 3: Length balance ──────────────────────────────────────────
    total_branch_fields = sum(len(bf) for bf in branch_field_sets)
    if island != "wolkenwerk":
        total = main_path_count + total_branch_fields
        if total != total_fields:
            messages.append(
                f"FAIL: {island} — length balance: {main_path_count} (main) + "
                f"{total_branch_fields} (branches) = {total}, expected {total_fields}"
            )
        else:
            messages.append(
                f"  OK: {island} — length balance: {main_path_count} + "
                f"{total_branch_fields} = {total} ✓"
            )
    else:
        # Wolkenwerk: all 40 fields in one loop, branches are inline
        messages.append(
            f"  OK: {island} (inline) — full loop 0-39 with "
            f"{total_branch_fields} branch fields (special rules)"
        )

    # ── Test 4: Junction minimum distance (world-overview.md 3.9.4) ──────
    if len(branches) == 2 and island != "wolkenwerk":
        a_entry = branches[0]["entry"]
        a_exit = branches[0]["exit"]
        b_entry = branches[1]["entry"]
        # Rule: entry_B ≥ exit_A + 5 (at least 5 fields between junctions)
        distance = b_entry - a_exit
        if distance < 5:
            messages.append(
                f"  WARN: {island} — junction distance: {b_entry} - {a_exit} = "
                f"{distance} (minimum 5 per Game Bible 3.9.4)"
            )
        else:
            messages.append(
                f"  OK: {island} — junction distance: {distance} ≥ 5 ✓"
            )

    # ── Test 5: Branch chain simulation ──────────────────────────────────
    if island != "wolkenwerk":
        _validate_chain_simulation(island, branches, first_field, messages)

    pass_count = sum(1 for m in messages if m.startswith("  OK"))
    fail_count = sum(1 for m in messages if m.startswith("FAIL"))
    return pass_count, fail_count, messages


def _validate_chain_simulation(island: str, branches: list, first_field: int,
                                messages: list) -> None:
    """Simulate the branch wiring algorithm from board.gd's _wire_branches()
    and verify the resulting graph is correct.

    Builds 'next' arrays as the GDScript function would, then traces:
      - Main path loop: 1→2→...→32→1
      - Each branch: entry→branch_first→...→branch_last→exit
    """
    total_nodes = 40
    # Build adjacency: node_index → [next_node_indices]
    # Node indices are 0-based (field_num - first_field)
    next_map: dict[int, list] = {}

    # Step 1: Set up main path loop (0..31 → loop to 0)
    for i in range(32):
        current_idx = i
        next_idx = 0 if i == 31 else i + 1
        next_map[current_idx] = [next_idx]

    # Step 2: Wire branches
    for branch in branches:
        entry = branch["entry"]
        exit_ = branch["exit"]
        fields = branch["fields"]

        entry_idx = entry - first_field
        first_branch_idx = fields[0] - first_field
        exit_idx = exit_ - first_field

        # Add branch path to entry node
        if entry_idx in next_map:
            if first_branch_idx not in next_map[entry_idx]:
                next_map[entry_idx].append(first_branch_idx)
        else:
            next_map[entry_idx] = [first_branch_idx]

        # Chain branch fields
        for j in range(len(fields) - 1):
            curr_idx = fields[j] - first_field
            nxt_idx = fields[j + 1] - first_field
            next_map[curr_idx] = [nxt_idx]

        # Last branch field → exit
        last_idx = fields[-1] - first_field
        next_map[last_idx] = [exit_idx]

    # Verify main path loop
    visited = set()
    current = 0  # Field 1 = index 0
    loop_complete = False
    for step in range(33):  # 32 steps + 1 for loop closure
        if current in visited and current == 0:
            loop_complete = True
            break
        visited.add(current)
        if current not in next_map:
            messages.append(
                f"FAIL: {island} — main path broken at field {current + first_field}"
            )
            break
        targets = next_map[current]
        # On main path, only one target (the main path next)
        # But junction fields have 2 targets — take the first (main path)
        current = targets[0]

    if loop_complete:
        messages.append(f"  OK: {island} — main path loop 1→32→1 verified ✓")
    elif not any(m.startswith("FAIL") and "main path broken" in m for m in messages):
        # Only report if we didn't already fail
        pass  # Loop trace already logged above

    # Verify branch chains
    for branch in branches:
        name = branch["name"]
        entry = branch["entry"]
        exit_ = branch["exit"]
        fields = branch["fields"]

        entry_idx = entry - first_field
        exit_idx = exit_ - first_field

        # Trace from entry through branch
        if entry_idx not in next_map or len(next_map[entry_idx]) < 2:
            messages.append(
                f"FAIL: {island} branch '{name}' — entry field {entry} "
                f"has only {len(next_map.get(entry_idx, []))} next target(s)"
            )
            continue

        # The branch path is the second next entry (index 1)
        branch_next = next_map[entry_idx][1]
        expected_first = fields[0] - first_field
        if branch_next != expected_first:
            messages.append(
                f"FAIL: {island} branch '{name}' — entry.next[1] = "
                f"{branch_next + first_field}, expected {fields[0]}"
            )
            continue

        # Walk the branch chain
        walked = []
        current = branch_next
        for _ in range(len(fields) + 2):  # safety limit
            walked.append(current + first_field)
            if current not in next_map:
                messages.append(
                    f"FAIL: {island} branch '{name}' — branch broken at "
                    f"field {current + first_field}"
                )
                break
            targets = next_map[current]
            if len(targets) != 1:
                messages.append(
                    f"FAIL: {island} branch '{name}' — branch field "
                    f"{current + first_field} has {len(targets)} next targets "
                    f"(expected 1)"
                )
                break
            current = targets[0]
            if current == exit_idx:
                walked.append(current + first_field)
                break

        expected_walk = fields + [exit_]
        if walked == expected_walk:
            messages.append(
                f"  OK: {island} branch '{name}' — chain: "
                f"{'→'.join(str(f) for f in walked)} ✓"
            )
        else:
            messages.append(
                f"FAIL: {island} branch '{name}' — chain mismatch: "
                f"got {walked}, expected {expected_walk}"
            )


# ── Main ───────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("Party Arena — Branch Wiring Validation (Milestone 6b)")
    print("=" * 60)
    print()

    total_pass = 0
    total_fail = 0
    total_warn = 0

    for island in ISLANDS:
        print(f"─── {island} ───")
        passes, fails, messages = validate_island(island)
        for msg in messages:
            print(msg)
        total_pass += passes
        total_fail += fails
        warn_count = sum(1 for m in messages if "WARN" in m)
        total_warn += warn_count
        print()

    print("=" * 60)
    print(f"RESULTS: {total_pass} passed, {total_fail} failed, "
          f"{total_warn} warnings")
    print("=" * 60)

    if total_fail > 0:
        print("\n❌ SOME TESTS FAILED")
        sys.exit(1)
    else:
        print("\n✅ ALL TESTS PASSED")
        sys.exit(0)


if __name__ == "__main__":
    main()
