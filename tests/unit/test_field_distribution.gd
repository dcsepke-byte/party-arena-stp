# Test: Feld-Verteilung im Test-Board zur Laufzeit validieren.
# Game Bible: design/gdd/board-architecture.md, Sektion 3.2
#
# Ausführung:
#   godot --headless --script tests/unit/test_field_distribution.gd
extends SceneTree

# Erwartete Verteilung (Game Bible 3.2) — Schlüssel = FELD_TYP-Integer
const EXPECTED := {
	0: 1,   # START
	1: 2,   # STERN_SHOP
	2: 2,   # ITEM_SHOP
	3: 5,   # EREIGNIS
	4: 3,   # GLUECK_PECH
	5: 4,   # MUENZ_BONUS
	6: 23,  # MINISPIEL
}

const FELD_TYP_NAMES := {
	0: "START",
	1: "STERN_SHOP",
	2: "ITEM_SHOP",
	3: "EREIGNIS",
	4: "GLUECK_PECH",
	5: "MUENZ_BONUS",
	6: "MINISPIEL",
}

const TOTAL_EXPECTED := 40


func _init() -> void:
	print("=== Field Distribution Runtime Test ===")
	print("Loading test board scene...")

	var board_scene: PackedScene = load("res://plugins/boards/test/board.tscn")
	if not board_scene:
		printerr("FAIL: Could not load board scene!")
		quit(1)
		return

	var board: Node = board_scene.instantiate()
	if not board:
		printerr("FAIL: Could not instantiate board!")
		quit(1)
		return

	# Warte einen Frame, damit _ready() ausgeführt wird
	await process_frame
	await process_frame

	# Prüfe, ob die Distributions-Funktion existiert
	if not board.has_method("get_field_distribution"):
		printerr("FAIL: board.gd has no get_field_distribution() method!")
		board.queue_free()
		quit(1)
		return

	var counts: Dictionary = board.get_field_distribution()
	var all_ok := true

	for typ in EXPECTED:
		var expected: int = EXPECTED[typ]
		var actual: int = counts.get(typ, 0)
		var name: String = FELD_TYP_NAMES.get(typ, "UNKNOWN")
		if actual == expected:
			print("  [PASS] %s: %d" % [name, actual])
		else:
			printerr("  [FAIL] %s: expected=%d, actual=%d" % [name, expected, actual])
			all_ok = false

	var total: int = 0
	for v in counts.values():
		total += v

	if total == TOTAL_EXPECTED:
		print("  [PASS] TOTAL: %d" % total)
	else:
		printerr("  [FAIL] TOTAL: expected=%d, actual=%d" % [TOTAL_EXPECTED, total])
		all_ok = false

	print("")
	if all_ok:
		print("=== RESULT: ALL TESTS PASSED ===")
	else:
		printerr("=== RESULT: SOME TESTS FAILED ===")

	board.queue_free()
	quit(0 if all_ok else 1)
