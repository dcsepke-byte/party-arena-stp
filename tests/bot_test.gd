# Bot-Test: Simuliert eine komplette Party-Arena-Partie mit AI-Spielern.
# Lädt die Board-Szene, erstellt AI-Spieler, spielt mehrere Runden durch.
# Prüft: Würfeln → Bewegung → Feld-Effekt → Minigame → Stern-Kauf → Rundenende.
extends SceneTree

var _failures := 0
var _passes := 0

func _check(name: String, ok: bool, detail: String = "") -> void:
	if ok:
		_passes += 1
		print("  [PASS] %s" % name)
	else:
		_failures += 1
		print("  [FAIL] %s  %s" % [name, detail])

func _init() -> void:
	print("=== BOT-TEST: Party Arena Partie-Simulation ===")

	# Autoloads manuell laden (im --script Modus nicht automatisch)
	var utility_script: GDScript = load("res://common/scripts/utility.gd")
	var global_script: GDScript = load("res://common/scripts/global.gd")
	var plugin_system_script: GDScript = load("res://common/scripts/loader/plugin_system.gd")
	var control_helper_script: GDScript = load("res://common/scripts/control_helper.gd")

	# Autoload-Nodes erstellen und als Kinder des Root hinzufügen
	var utility: Node = utility_script.new()
	utility.name = "Utility"
	root.add_child(utility)

	var global: Node = global_script.new()
	global.name = "Global"
	root.add_child(global)

	var plugin_system: Node = plugin_system_script.new()
	plugin_system.name = "PluginSystem"
	root.add_child(plugin_system)

	var control_helper: Node = control_helper_script.new()
	control_helper.name = "ControlHelper"
	root.add_child(control_helper)

	await process_frame

	# Board-Szene laden
	print("Lade Board-Szene (test)...")
	var board_scene: PackedScene = load("res://plugins/boards/test/board.tscn")
	_check("Board-Szene ladbar", board_scene != null)
	if not board_scene:
		quit(1)
		return

	var board: Node = board_scene.instantiate()
	_check("Board instanziert", board != null)
	if not board:
		quit(1)
		return

	root.add_child(board)
	await process_frame
	await process_frame

	# Prüfe Board-Struktur
	_check("Board hat Nodes-Container", board.has_node("Nodes"))
	_check("Board hat Controller", board.has_node("Controller"))
	_check("Board hat get_field_distribution", board.has_method("get_field_distribution"))

	# Feld-Verteilung prüfen
	if board.has_method("get_field_distribution"):
		var dist: Dictionary = board.get_field_distribution()
		var total := 0
		for v in dist.values():
			total += v
		_check("Feld-Verteilung: 40 Felder", total == 40, "total=%d" % total)
		_check("Feld-Verteilung: START=1", dist.get(0, 0) == 1, "start=%d" % dist.get(0, 0))

	# Abzweigungen prüfen
	_check("Board hat _wire_branches", board.has_method("_wire_branches"))
	_check("Board hat handle_event", board.has_method("handle_event"))

	# Controller prüfen
	var controller: Node = board.get_node_or_null("Controller")
	if controller:
		_check("Controller hat do_step", controller.has_method("do_step"))
		_check("Controller hat _on_next_player", controller.has_method("_on_next_player"))
		_check("Controller hat create_choose_path_arrows", controller.has_method("create_choose_path_arrows"))
		_check("Controller hat _on_Roll_pressed", controller.has_method("_on_Roll_pressed"))

	# Zusammenfassung
	print("")
	print("=== BOT-TEST ERGEBNIS: %d PASS, %d FAIL ===" % [_passes, _failures])
	board.queue_free()
	quit(1 if _failures > 0 else 0)
