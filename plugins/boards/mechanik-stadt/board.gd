extends Node3D

# Party Arena: Mechanik-Stadt-Board
# Schwierigkeit: ★★★★☆
# Game Bible: design/gdd/world-mechanik-stadt.md

# Referenz-Layout (40 Felder) gemäß Game Bible Tabelle 3.8 + Insel-Kapitel 3.1
const REFERENCE_LAYOUT: Array[int] = [
		NodeBoard.FELD_TYP.START,  # 1,
		NodeBoard.FELD_TYP.MINISPIEL,  # 2,
		NodeBoard.FELD_TYP.MUENZ_BONUS,  # 3,
		NodeBoard.FELD_TYP.MINISPIEL,  # 4,
		NodeBoard.FELD_TYP.MINISPIEL,  # 5,
		NodeBoard.FELD_TYP.EREIGNIS,  # 6,
		NodeBoard.FELD_TYP.GLUECK_PECH,  # 7,
		NodeBoard.FELD_TYP.ITEM_SHOP,  # 8,
		NodeBoard.FELD_TYP.MINISPIEL,  # 9,
		NodeBoard.FELD_TYP.MINISPIEL,  # 10,
		NodeBoard.FELD_TYP.STERN_SHOP,  # 11,
		NodeBoard.FELD_TYP.MINISPIEL,  # 12,
		NodeBoard.FELD_TYP.EREIGNIS,  # 13,
		NodeBoard.FELD_TYP.MINISPIEL,  # 14,
		NodeBoard.FELD_TYP.MUENZ_BONUS,  # 15,
		NodeBoard.FELD_TYP.MINISPIEL,  # 16,
		NodeBoard.FELD_TYP.MINISPIEL,  # 17,
		NodeBoard.FELD_TYP.STERN_SHOP,  # 18,
		NodeBoard.FELD_TYP.MINISPIEL,  # 19,
		NodeBoard.FELD_TYP.GLUECK_PECH,  # 20,
		NodeBoard.FELD_TYP.EREIGNIS,  # 21,
		NodeBoard.FELD_TYP.EREIGNIS,  # 22,
		NodeBoard.FELD_TYP.MINISPIEL,  # 23,
		NodeBoard.FELD_TYP.MINISPIEL,  # 24,
		NodeBoard.FELD_TYP.EREIGNIS,  # 25,
		NodeBoard.FELD_TYP.ITEM_SHOP,  # 26,
		NodeBoard.FELD_TYP.MUENZ_BONUS,  # 27,
		NodeBoard.FELD_TYP.MINISPIEL,  # 28,
		NodeBoard.FELD_TYP.MINISPIEL,  # 29,
		NodeBoard.FELD_TYP.GLUECK_PECH,  # 30,
		NodeBoard.FELD_TYP.MINISPIEL,  # 31,
		NodeBoard.FELD_TYP.MINISPIEL,  # 32,
		NodeBoard.FELD_TYP.MINISPIEL,  # 33,
		NodeBoard.FELD_TYP.MUENZ_BONUS,  # 34,
		NodeBoard.FELD_TYP.MINISPIEL,  # 35,
		NodeBoard.FELD_TYP.STERN_SHOP,  # 36,
		NodeBoard.FELD_TYP.EREIGNIS,  # 37,
		NodeBoard.FELD_TYP.MINISPIEL,  # 38,
		NodeBoard.FELD_TYP.MINISPIEL,  # 39,
		NodeBoard.FELD_TYP.MINISPIEL,  # 40
]

# Erwartete Verteilung (Game Bible world-overview.md 3.8)
const EXPECTED_DISTRIBUTION := {
	NodeBoard.FELD_TYP.START: 1,
	NodeBoard.FELD_TYP.STERN_SHOP: 3,
	NodeBoard.FELD_TYP.ITEM_SHOP: 2,
	NodeBoard.FELD_TYP.EREIGNIS: 6,
	NodeBoard.FELD_TYP.GLUECK_PECH: 3,
	NodeBoard.FELD_TYP.MUENZ_BONUS: 4,
	NodeBoard.FELD_TYP.MINISPIEL: 21,
}

# Feldtyp-Namen für Debugging
const FELD_TYP_NAMES := {
	NodeBoard.FELD_TYP.START: "START",
	NodeBoard.FELD_TYP.STERN_SHOP: "STERN_SHOP",
	NodeBoard.FELD_TYP.ITEM_SHOP: "ITEM_SHOP",
	NodeBoard.FELD_TYP.EREIGNIS: "EREIGNIS",
	NodeBoard.FELD_TYP.GLUECK_PECH: "GLUECK_PECH",
	NodeBoard.FELD_TYP.MUENZ_BONUS: "MUENZ_BONUS",
	NodeBoard.FELD_TYP.MINISPIEL: "MINISPIEL",
}

# Insel-Metadaten
var board_id: String = "mechanik-stadt"
var board_name: String = "Mechanik-Stadt"
var difficulty: int = 4
var item_price_tier: int = 2

# Abzweigungs-Daten (Single Source of Truth: board.json)
# Einstieg/Ausstieg/Δ gemäß Game Bible world-mechanik-stadt.md
const BRANCHES: Array[Dictionary] = [
	{
		"name": "Rohrpost-Teleport",
		"entry": 13,
		"exit": 17,
		"delta": 1,
		"fields": [33, 34, 35, 36],
	},
	{
		"name": "Förderband-Fabrik",
		"entry": 24,
		"exit": 30,
		"delta": -1,
		"fields": [37, 38, 39, 40],
	},
]

# 1-basierte Feld-Nummerierung: Feld 1 = sorted_nodes[0]
const FIRST_FIELD: int = 1


func _ready() -> void:
	_apply_reference_layout()
	_wire_branches()
	_validate_distribution()


## Wendet die Feldtypen des Referenz-Layouts auf die vorhandenen
## NodeBoard-Knoten an (nach Namen sortiert: Node1, Node2, ...).
func _apply_reference_layout() -> void:
	if not has_node("Nodes"):
		push_error("mechanik-stadt board: 'Nodes' container not found!")
		return

	var nodes_container := $Nodes
	var node_boards: Array[Node] = []

	for child in nodes_container.get_children():
		if child is NodeBoard:
			node_boards.append(child)

	if node_boards.is_empty():
		push_error("mechanik-stadt board: No NodeBoard instances found!")
		return

	node_boards.sort_custom(func(a, b): return a.name.naturalnocase_to(b.name) < 0)

	for i in range(min(node_boards.size(), REFERENCE_LAYOUT.size())):
		var node: NodeBoard = node_boards[i]
		node.type = REFERENCE_LAYOUT[i]

	for i in range(REFERENCE_LAYOUT.size(), node_boards.size()):
		var node: NodeBoard = node_boards[i]
		node._visible = false

	print("mechanik-stadt board: Applied reference layout to %d nodes (%d hidden)" %
			[min(node_boards.size(), REFERENCE_LAYOUT.size()), max(0, node_boards.size() - REFERENCE_LAYOUT.size())])


## Validiert die Feld-Verteilung und gibt Warnungen aus,
## wenn sie nicht dem erwarteten Mengengerüst entspricht.
func _validate_distribution() -> void:
	var counts := get_field_distribution()
	var ok := true

	for typ in EXPECTED_DISTRIBUTION:
		var expected: int = EXPECTED_DISTRIBUTION[typ]
		var actual: int = counts.get(typ, 0)
		if actual != expected:
			push_warning("Field distribution mismatch: %s — expected %d, got %d" %
					[FELD_TYP_NAMES.get(typ, "UNKNOWN"), expected, actual])
			ok = false

	if ok:
		print("mechanik-stadt board: Field distribution VALID (all %d types match Game Bible 3.8)" %
				EXPECTED_DISTRIBUTION.size())
	else:
		push_error("mechanik-stadt board: Field distribution INVALID — see warnings above")


## Gibt die aktuelle Feld-Verteilung als Dictionary zurück.
func get_field_distribution() -> Dictionary:
	var counts := {}
	if not has_node("Nodes"):
		return counts

	for child in $Nodes.get_children():
		if child is NodeBoard and child._visible:
			var t: int = child.type
			counts[t] = counts.get(t, 0) + 1

	return counts


## Gibt eine menschenlesbare Zusammenfassung der Feld-Verteilung zurück.
func get_distribution_summary() -> String:
	var counts := get_field_distribution()
	var lines: Array[String] = []
	lines.append("=== Field Distribution ===")
	for typ in counts:
		var name: String = FELD_TYP_NAMES.get(typ, "UNKNOWN_%d" % typ)
		lines.append("  %s: %d" % [name, counts[typ]])
	lines.append("  TOTAL: %d" % counts.values().reduce(func(a, b): return a + b, 0))
	lines.append("===========================")
	return "\n".join(lines)


## Gibt alle sichtbaren NodeBoard-Knoten in sortierter Reihenfolge
## (nach Namen: Node1, Node2, ... Node40) zurück.
func _get_sorted_nodes() -> Array[NodeBoard]:
	var nodes: Array[NodeBoard] = []
	if not has_node("Nodes"):
		return nodes
	for child in $Nodes.get_children():
		if child is NodeBoard and child._visible:
			nodes.append(child as NodeBoard)
	nodes.sort_custom(func(a, b): return a.name.naturalnocase_to(b.name) < 0)
	return nodes


## Verdrahtet die Abzweigungen (BRANCHES) in die next-Arrays der
## NodeBoard-Knoten ein. Die bestehende lineare Verkettung wird
## ersetzt durch: Hauptpfad 1-32 → Loop 32→1, plus 2×4
## Abzweigungs-Felder 33-40 mit Einstieg/Ausstieg.
func _wire_branches() -> void:
	var sorted: Array[NodeBoard] = _get_sorted_nodes()
	if sorted.size() < 40:
		push_error("%s board: Not enough visible nodes for branch wiring (%d)" % [board_id, sorted.size()])
		return

	# Schritt 1: Hauptpfad-Schleife (Felder 1–32 → 1)
	for i: int in range(32):
		var current: NodeBoard = sorted[i]
		var next_node: NodeBoard
		if i == 31:  # Feld 32 → Feld 1 (Loop)
			next_node = sorted[0]
		else:
			next_node = sorted[i + 1]
		current.next = [current.get_path_to(next_node)]

	# Schritt 2: Abzweigungen verdrahten
	for branch: Dictionary in BRANCHES:
		var entry: int = branch["entry"]
		var exit: int = branch["exit"]
		var fields: Array = branch["fields"]

		# Einstieg: Junction-Feld bekommt Abzweigung als zusätzlichen Pfad
		var entry_node: NodeBoard = sorted[entry - FIRST_FIELD]
		var first_branch: NodeBoard = sorted[fields[0] - FIRST_FIELD]
		var entry_next: Array[NodePath] = entry_node.next.duplicate()
		entry_next.append(entry_node.get_path_to(first_branch))
		entry_node.next = entry_next

		# Abzweigungs-Kette: Feld → Feld → ...
		for j: int in range(fields.size() - 1):
			var curr: NodeBoard = sorted[fields[j] - FIRST_FIELD]
			var nxt: NodeBoard = sorted[fields[j + 1] - FIRST_FIELD]
			curr.next = [curr.get_path_to(nxt)]

		# Ausstieg: Letztes Abzweigungs-Feld → Ausstiegs-Feld
		var last_branch: NodeBoard = sorted[fields[fields.size() - 1] - FIRST_FIELD]
		var exit_node: NodeBoard = sorted[exit - FIRST_FIELD]
		last_branch.next = [last_branch.get_path_to(exit_node)]

	print("%s board: Branch wiring complete — main loop 1-32, %d branches wired" % [board_id, BRANCHES.size()])

const EVENT_DEFINITIONS: Dictionary = 	{
		"erfindermesse": {
			"name": "Erfindermesse",
			"weight": 25,
		},
		"zahnrad_stau": {
			"name": "Zahnrad-Stau",
			"weight": 35,
		},
		"dampf_explosion": {
			"name": "Dampf-Explosion",
			"weight": 40,
		},
	}

# Gebundene Ereignis-Felder (Feld -> Event-ID)
const BOUND_EVENTS: Dictionary = {
	37: "zahnrad_stau",
}

# Abzweigungs-Sonderregeln
const SPECIAL_RULES: Array[String] = ["rohrpost_teleport", "foerderband_fabrik"]

## Initialisiert das Ereignis-System: verbindet trigger_event-Signal mit handle_event.
func _init_event_system() -> void:
	if has_node("Controller") and $Controller.has_signal("trigger_event"):
		if not $Controller.trigger_event.is_connected(handle_event):
			$Controller.trigger_event.connect(handle_event)
		print("%s board: Event system initialized — %d events, %d bound fields, %d special rules" %
				[board_id, EVENT_DEFINITIONS.size(), BOUND_EVENTS.size(), SPECIAL_RULES.size()])
	else:
		push_error("%s board: Controller not found or missing trigger_event signal!" % board_id)

## Event-Handler für board-spezifische Ereignisse (EREIGNIS-Felder).
func handle_event(player: Node3D, space: Node3D) -> void:
	var ctrl: Controller = $Controller if has_node("Controller") else null
	if not ctrl:
		push_error("%s: handle_event called without Controller!" % board_id)
		return

	var field_num: int = _get_field_number(space)
	var event_id: String = ""

	# Bestimme Ereignis: gebunden oder gewichtete Auslosung
	if BOUND_EVENTS.has(field_num):
		event_id = BOUND_EVENTS[field_num]
	else:
		event_id = _draw_weighted_event()

	if event_id.is_empty():
		push_warning("%s: No event drawn for field %d" % [board_id, field_num])
		ctrl.board_continue()
		return

	var event_data: Dictionary = EVENT_DEFINITIONS.get(event_id, {})
	var event_name: String = event_data.get("name", event_id)
	print("%s: Event \'%s\' triggered on field %d by player %d" %
			[board_id, event_name, field_num, _get_player_id(player)])

	await _execute_event(event_id, player, ctrl)
	ctrl.board_continue()

## Zieht ein Ereignis aus dem Pool per gewichteter Auslosung.
func _draw_weighted_event() -> String:
	var total_weight: int = 0
	for ev_id in EVENT_DEFINITIONS:
		total_weight += EVENT_DEFINITIONS[ev_id].get("weight", 0)

	if total_weight <= 0:
		return ""

	var roll: int = randi() % total_weight
	var cumulative: int = 0
	for ev_id in EVENT_DEFINITIONS:
		cumulative += EVENT_DEFINITIONS[ev_id].get("weight", 0)
		if roll < cumulative:
			return ev_id

	return EVENT_DEFINITIONS.keys()[0]  # Fallback

## Führt den Effekt eines Ereignisses aus (Insel-spezifisch).
func _execute_event(event_id: String, player: Node3D, ctrl: Controller) -> void:
	match event_id:
		"erfindermesse":
			await _ev_erfindermesse(player, ctrl)
		"zahnrad_stau":
			await _ev_zahnrad_stau(player, ctrl)
		"dampf_explosion":
			await _ev_dampf_explosion(player, ctrl)
		_:
			push_warning("%s: Unknown event \'%s\'" % [board_id, event_id])

# --- Ereignis-Effekte ---

## Erfindermesse: Alle Item-Preise -2 für den Rest der Runde.
func _ev_erfindermesse(_player: Node3D, _ctrl: Controller) -> void:
	_erfindermesse_active = true

## Zahnrad-Stau: Aktiver Spieler setzt nächste Runde aus.
func _ev_zahnrad_stau(player: Node3D, _ctrl: Controller) -> void:
	var p_active: PlayerBoard = player as PlayerBoard
	if p_active:
		_skip_turns[p_active.info.player_id] = true

## Dampf-Explosion: Alle Spieler auf zufällige Hauptpfad-Felder (1-32).
func _ev_dampf_explosion(_player: Node3D, ctrl: Controller) -> void:
	if ctrl.players.size() < 2:
		return

	var sorted: Array[NodeBoard] = _get_sorted_nodes()
	# Nur Hauptpfad-Felder (Indizes 0-31, Felder 1-32)
	var main_path: Array[NodeBoard] = []
	for i in range(min(32, sorted.size())):
		main_path.append(sorted[i])

	if main_path.size() < 2:
		return

	# Zufällige Zielfelder (ohne Zurücklegen)
	var available: Array[NodeBoard] = main_path.duplicate()
	for p: PlayerBoard in ctrl.players:
		if available.size() == 0:
			available = main_path.duplicate()
		var idx: int = randi() % available.size()
		p.teleport_to(available[idx])
		available.remove_at(idx)

	await ctrl.get_tree().create_timer(0.5).timeout

# ============================================================
# HILFSMETHODEN (Event-System)
# ============================================================

## Extrahiert die Feld-Nummer aus dem Node-Namen (Node16 -> 16).
func _get_field_number(space: Node3D) -> int:
	return space.name.trim_prefix("Node").to_int()

## Extrahiert die Player-ID aus dem Player-Knoten.
func _get_player_id(player: Node3D) -> int:
	var pb: PlayerBoard = player as PlayerBoard
	if pb and pb.info:
		return pb.info.player_id
	return -1

## Bewegt einen Spieler um `steps` Felder vorwärts auf dem aktuellen Pfad.
## An Junctions wird der Hauptpfad (erstes next-Element) gewählt.
## Effekt-Platzierung: keine Feld-Effekte auslösen (board-architecture.md 3.11).
func _move_player_forward(p: PlayerBoard, steps: int, ctrl: Controller) -> void:
	if steps <= 0 or not p:
		return

	var current: NodeBoard = p.space
	for _i in range(steps):
		if current.next.is_empty():
			break
		var next_path: NodePath = current.next[0]  # Hauptpfad an Junctions
		var next_node: NodeBoard = current.get_node(next_path) as NodeBoard
		if not next_node:
			break
		current = next_node

	# Teleport (Effekt-Platzierung = keine Feld-Effekte)
	p.teleport_to(current)
	await ctrl.get_tree().create_timer(0.2).timeout

## Bewegt einen Spieler rückwärts auf dem aktuellen Pfad.
func _move_player_backward(p: PlayerBoard, steps: int, ctrl: Controller) -> void:
	if steps <= 0 or not p:
		return

	var sorted: Array[NodeBoard] = _get_sorted_nodes()
	var current: NodeBoard = p.space
	var idx: int = sorted.find(current)

	for _i in range(steps):
		if idx <= 0:
			idx = sorted.size() - 1  # Loop zum Ende
		else:
			idx -= 1

	p.teleport_to(sorted[idx])
	await ctrl.get_tree().create_timer(0.2).timeout

## Gibt den Spieler mit dem höchsten Explorations-Wert zurück
## (Näherung: Spieler auf Feld mit höchstem Index).
## Bei Gleichstand: null (keiner erhält Bonus).
func _get_most_explored_player(ctrl: Controller) -> PlayerBoard:
	if ctrl.players.size() == 0:
		return null

	var sorted: Array[NodeBoard] = _get_sorted_nodes()
	var best: PlayerBoard = ctrl.players[0]
	var best_idx: int = sorted.find(best.space)
	var tie: bool = false

	for i in range(1, ctrl.players.size()):
		var p: PlayerBoard = ctrl.players[i]
		var idx: int = sorted.find(p.space)
		if idx > best_idx:
			best_idx = idx
			best = p
			tie = false
		elif idx == best_idx:
			tie = true

	return null if tie else best

## Gibt den reichsten Spieler zurück (primär Sterne, sekundär Münzen).
func _get_richest_player(ctrl: Controller) -> PlayerBoard:
	var best: PlayerBoard = ctrl.players[0]
	for p: PlayerBoard in ctrl.players:
		if p.stars > best.stars or (p.stars == best.stars and p.cookies > best.cookies):
			best = p
	return best

## Gibt den ärmsten Spieler zurück (primär Sterne, sekundär Münzen).
func _get_poorest_player(ctrl: Controller) -> PlayerBoard:
	var worst: PlayerBoard = ctrl.players[0]
	for p: PlayerBoard in ctrl.players:
		if p.stars < worst.stars or (p.stars == worst.stars and p.cookies < worst.cookies):
			worst = p
	return worst

## Gibt alle Spieler außer dem angegebenen zurück.
func _get_other_players(ctrl: Controller, exclude: PlayerBoard) -> Array[PlayerBoard]:
	var others: Array[PlayerBoard] = []
	for p: PlayerBoard in ctrl.players:
		if p != exclude:
			others.append(p)
	return others

# ============================================================
# ABZWEIGUNGS-SONDERREGELN (Part B, Milestone 6c)
# ============================================================

## Gibt die Sonderregeln dieser Insel zurück.
func get_special_rules() -> Array[String]:
	return SPECIAL_RULES

## Prüft, ob eine bestimmte Sonderregel für diese Insel aktiv ist.
func has_special_rule(rule_id: String) -> bool:
	return rule_id in SPECIAL_RULES

## Gibt die Sonderregel für eine Abzweigung zurück (Name -> rule_id).
func get_branch_special_rule(branch_name: String) -> String:
	for branch: Dictionary in BRANCHES:
		if branch.get("name", "") == branch_name:
			return branch.get("rule", "")
	return ""
