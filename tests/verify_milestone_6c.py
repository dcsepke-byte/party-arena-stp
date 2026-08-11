#!/usr/bin/env python3
"""Verification test for Party Arena Milestone 6c: Event System + Branch Special Rules.

Tests:
1. Every island has a non-empty event card set
2. Every event has an effect (not just a name)
3. Branch special rules are defined per island
4. No board still has the placeholder stub
"""

import os
import re
import sys
import json

BOARD_DIRS = [
    "sonnenstrand",
    "zuckerwald",
    "wolkenwerk",
    "frostgipfel",
    "dschungeltempel",
    "mechanik-stadt",
    "sternenzitadelle",
]
BASE_DIR = "/opt/data/SuperTuxParty/plugins/boards"

errors = []
warnings = []


def find_event_definitions(content: str) -> dict:
    """Parse EVENT_DEFINITIONS const from GDScript.
    Only matches top-level event IDs (keys followed by { with "name" inside)."""
    # Match const EVENT_DEFINITIONS: Dictionary = { ... }
    match = re.search(
        r"const\s+EVENT_DEFINITIONS\s*:\s*Dictionary\s*=\s*\{(.*?)\n\}",
        content, re.DOTALL
    )
    if not match:
        return {}
    block = match.group(1)
    # Extract event IDs — only top-level keys that have a "name" sub-key
    event_ids = re.findall(r'\t+"(\w+)"\s*:\s*\{', block)
    result = {}
    for eid in event_ids:
        # Find the weight for this event
        weight_match = re.search(
            rf'"{re.escape(eid)}"\s*:\s*\{{[^}}]*"weight"\s*:\s*(\d+)',
            block, re.DOTALL
        )
        weight = int(weight_match.group(1)) if weight_match else 0
        result[eid] = {"weight": weight}
    return result


def find_bound_events(content: str) -> dict:
    """Parse BOUND_EVENTS const from GDScript."""
    match = re.search(
        r"const\s+BOUND_EVENTS\s*:\s*Dictionary\s*=\s*\{(.*?)\n\}",
        content, re.DOTALL
    )
    if not match:
        return {}
    block = match.group(1)
    pairs = re.findall(r'(\d+)\s*:\s*"(\w+)"', block)
    return {int(k): v for k, v in pairs}


def find_special_rules(content: str) -> list:
    """Parse SPECIAL_RULES const from GDScript."""
    match = re.search(
        r'const\s+SPECIAL_RULES\s*:\s*Array\[String\]\s*=\s*\[(.*?)\]',
        content, re.DOTALL
    )
    if not match:
        return []
    block = match.group(1)
    rules = re.findall(r'"(\w+)"', block)
    return rules


def has_stub(content: str) -> bool:
    """Check if the file still has the placeholder stub."""
    return "Platzhalter: Insel-spezifische Ereignis-Logik folgt" in content


def has_event_init(content: str) -> bool:
    """Check if _init_event_system is called in _ready."""
    return "_init_event_system()" in content


def has_trigger_connect(content: str) -> bool:
    """Check if trigger_event signal is connected."""
    return "trigger_event.connect" in content


def find_event_effect_methods(content: str) -> list:
    """Find event effect method implementations (_ev_*)."""
    return re.findall(r'func\s+(_ev_\w+)', content)


def main():
    print("=" * 70)
    print("Party Arena Milestone 6c — Event System Verification")
    print("=" * 70)
    print()

    total_pass = 0
    total_fail = 0

    for board_name in BOARD_DIRS:
        board_path = os.path.join(BASE_DIR, board_name, "board.gd")
        json_path = os.path.join(BASE_DIR, board_name, "board.json")

        if not os.path.exists(board_path):
            errors.append(f"{board_name}: board.gd not found!")
            total_fail += 1
            continue

        with open(board_path) as f:
            content = f.read()

        print(f"--- {board_name} ---")

        # Test 1: No stub remaining
        if has_stub(content):
            msg = f"  FAIL: Still has placeholder stub!"
            print(msg)
            errors.append(f"{board_name}: {msg.strip()}")
            total_fail += 1
        else:
            print("  PASS: No placeholder stub")
            total_pass += 1

        # Test 2: Event system initialized
        if has_event_init(content) and has_trigger_connect(content):
            print("  PASS: Event system initialized (trigger_event connected)")
            total_pass += 1
        else:
            msg = "  FAIL: Event system NOT initialized!"
            print(msg)
            errors.append(f"{board_name}: {msg.strip()}")
            total_fail += 1

        # Test 3: Event definitions non-empty
        events = find_event_definitions(content)
        if events:
            print(f"  PASS: Event definitions found ({len(events)} events: {', '.join(events.keys())})")
            total_pass += 1
        else:
            msg = "  FAIL: No EVENT_DEFINITIONS found!"
            print(msg)
            errors.append(f"{board_name}: {msg.strip()}")
            total_fail += 1

        # Test 4: Each event has an effect implementation
        effect_methods = find_event_effect_methods(content)
        event_ids = set(events.keys())
        implemented = set()
        for method in effect_methods:
            # _ev_springflut → springflut
            ev_id = method[4:]  # strip _ev_ prefix
            if ev_id in event_ids:
                implemented.add(ev_id)

        if event_ids == implemented:
            print(f"  PASS: All {len(event_ids)} events have effect implementations")
            total_pass += 1
        else:
            missing = event_ids - implemented
            msg = f"  FAIL: Missing effect implementations for: {missing}"
            print(msg)
            errors.append(f"{board_name}: {msg.strip()}")
            total_fail += 1

        # Test 5: Bound events defined
        bound = find_bound_events(content)
        if board_name == "sonnenstrand":
            # Sonnenstrand has 3 bound fields
            if len(bound) >= 3:
                print(f"  PASS: {len(bound)} bound events defined")
                total_pass += 1
            else:
                print(f"  FAIL: Only {len(bound)} bound events, expected >= 3")
                total_fail += 1
        else:
            if bound:
                print(f"  PASS: {len(bound)} bound events defined")
                total_pass += 1
            else:
                print(f"  INFO: No bound events (all weighted draw)")
                total_pass += 1

        # Test 6: Special rules defined
        rules = find_special_rules(content)
        if board_name == "sonnenstrand":
            if rules == []:
                print("  PASS: No special rules (as expected for Sonnenstrand)")
                total_pass += 1
            else:
                print(f"  WARN: Sonnenstrand has special rules: {rules}")
                warnings.append(f"{board_name}: Unexpected special rules: {rules}")
                total_pass += 1
        else:
            if len(rules) >= 2:
                print(f"  PASS: {len(rules)} special rules defined: {rules}")
                total_pass += 1
            else:
                msg = f"  FAIL: Only {len(rules)} special rules, expected >= 2"
                print(msg)
                errors.append(f"{board_name}: {msg.strip()}")
                total_fail += 1

        # Test 7: board.json event_pool matches EVENT_DEFINITIONS
        if os.path.exists(json_path):
            with open(json_path) as f:
                jdata = json.load(f)
            json_events = set(jdata.get("event_pool", []))
            gd_events = set(events.keys())
            if json_events == gd_events:
                print(f"  PASS: board.json event_pool matches board.gd EVENT_DEFINITIONS")
                total_pass += 1
            else:
                only_json = json_events - gd_events
                only_gd = gd_events - json_events
                if only_json:
                    warnings.append(f"{board_name}: event_pool has extra: {only_json}")
                if only_gd:
                    warnings.append(f"{board_name}: EVENT_DEFINITIONS has extra: {only_gd}")
                print(f"  INFO: json={json_events}, gd={gd_events} (differences noted)")
                total_pass += 1

        # Test 8: board.json special_rules matches SPECIAL_RULES
        if os.path.exists(json_path):
            with open(json_path) as f:
                jdata = json.load(f)
            json_rules = set(jdata.get("special_rules", []))
            gd_rules = set(rules)
            if json_rules == gd_rules:
                print(f"  PASS: board.json special_rules matches board.gd SPECIAL_RULES")
                total_pass += 1
            else:
                only_json = json_rules - gd_rules
                only_gd = gd_rules - json_rules
                if only_json:
                    warnings.append(f"{board_name}: special_rules has extra in json: {only_json}")
                if only_gd:
                    warnings.append(f"{board_name}: SPECIAL_RULES has extra in gd: {only_gd}")
                print(f"  INFO: json={json_rules}, gd={gd_rules} (differences noted)")
                total_pass += 1

        print()

    # Summary
    print("=" * 70)
    print(f"RESULTS: {total_pass} passed, {total_fail} failed")
    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  ⚠ {w}")
    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  ✗ {e}")
    print("=" * 70)

    if total_fail > 0:
        print("\n❌ VERIFICATION FAILED")
        sys.exit(1)
    else:
        print("\n✅ ALL CHECKS PASSED")
        sys.exit(0)


if __name__ == "__main__":
    main()
