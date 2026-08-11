extends Node3D

# Party Arena: Wolkenwerk-Board
# Schwierigkeit: ★★★☆☆
# Game Bible: design/gdd/world-wolkenwerk.md

# Referenz-Layout (40 Felder) gemäß Game Bible Tabelle 3.8 + Insel-Kapitel 3.1
const REFERENCE_LAYOUT: Array[int] = [
		NodeBoard.FELD_TYP.START,  # 0,
		NodeBoard.FELD_TYP.MINISPIEL,  # 1,
		NodeBoard.FELD_TYP.MINISPIEL,  # 2,
		NodeBoard.FELD_TYP.MUENZ_BONUS,  # 3,
		NodeBoard.FELD_TYP.EREIGNIS,  # 4,
		NodeBoard.FELD_TYP.MINISPIEL,  # 5,
		NodeBoard.FELD_TYP.MINISPIEL,  # 6,
		NodeBoard.FELD_TYP.GLUECK_PECH,  # 7,
		NodeBoard.FELD_TYP.EREIGNIS,  # 8,
		NodeBoard.FELD_TYP.ITEM_SHOP,  # 9,
		NodeBoard.FELD_TYP.MINISPIEL,  # 10,
		NodeBoard.FELD_TYP.MINISPIEL,  # 11,
		NodeBoard.FELD_TYP.EREIGNIS,  # 12,
		NodeBoard.FELD_TYP.MINISPIEL,  # 13,
		NodeBoard.FELD_TYP.STERN_SHOP,  # 14,
		NodeBoard.FELD_TYP.MINISPIEL,  # 15,
		NodeBoard.FELD_TYP.MUENZ_BONUS,  # 16,
		NodeBoard.FELD_TYP.MINISPIEL,  # 17,
		NodeBoard.FELD_TYP.GLUECK_PECH,  # 18,
		NodeBoard.FELD_TYP.MINISPIEL,  # 19,
		NodeBoard.FELD_TYP.EREIGNIS,  # 20,
		NodeBoard.FELD_TYP.MINISPIEL,  # 21,
		NodeBoard.FELD_TYP.MINISPIEL,  # 22,
		NodeBoard.FELD_TYP.MINISPIEL,  # 23,
		NodeBoard.FELD_TYP.MINISPIEL,  # 24,
		NodeBoard.FELD_TYP.ITEM_SHOP,  # 25,
		NodeBoard.FELD_TYP.MUENZ_BONUS,  # 26,
		NodeBoard.FELD_TYP.MINISPIEL,  # 27,
		NodeBoard.FELD_TYP.STERN_SHOP,  # 28,
		NodeBoard.FELD_TYP.MINISPIEL,  # 29,
		NodeBoard.FELD_TYP.EREIGNIS,  # 30,
		NodeBoard.FELD_TYP.MINISPIEL,  # 31,
		NodeBoard.FELD_TYP.GLUECK_PECH,  # 32,
		NodeBoard.FELD_TYP.MINISPIEL,  # 33,
		NodeBoard.FELD_TYP.MINISPIEL,  # 34,
		NodeBoard.FELD_TYP.MUENZ_BONUS,  # 35,
		NodeBoard.FELD_TYP.EREIGNIS,  # 36,
		NodeBoard.FELD_TYP.MINISPIEL,  # 37,
		NodeBoard.FELD_TYP.STERN_SHOP,  # 38,
		NodeBoard.FELD_TYP.MINISPIEL,  # 39
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
var board_id: String = "wolkenwerk"
var board_name: String = "Wolkenwerk"
var difficulty: int = 3
var item_price_tier: int = 1

# Abzweigungs-Daten (Single Source of Truth: board.json)
# Wolkenwerk verwendet Inline-Abzweigungen (0-basierte Nummerierung 0-39)
# Einstieg/Ausstieg/Δ gemäß Game Bible world-wolkenwerk.md
# Sonderregeln (windkanal_express, regenbogen_gleitfahrt) folgen in
# einem späteren Milestone; hier wird die Grundverdrahtung gelegt.
const BRANCHES: Array[Dictionary] = [
	{
		"name": "Windkanal",
		"entry": 9,
		"exit": 13,
		"delta": -3,
		"fields": [10, 11, 12, 13],
	},
	{
		"name": "Regenbogen-Rutsche",
		"entry": 21,
		"exit": 25,
		"delta": 2,
		"fields": [22, 23, 24],
	},
]

# 0-basierte Feld-Nummerierung: Feld 0 = sorted_nodes[0]
const FIRST_FIELD: int = 0


func _ready() -> void:
	_apply_reference_layout()
	_wire_branches()
	_validate_distribution()
	_init_event_system()


## Wendet die Feldtypen des Referenz-Layouts auf die vorhandenen
## NodeBoard-Knoten an (nach Namen sortiert: Node1, Node2, ...).
func _apply_reference_layout() -> void:
	if not has_node("Nodes"):
		push_error("wolkenwerk board: 'Nodes' container not found!")
		return

	var nodes_container := $Nodes
	var node_boards: Array[Node] = []

	for child in nodes_container.get_children():
		if child is NodeBoard:
			node_boards.append(child)

	if node_boards.is_empty():
		push_error("wolkenwerk board: No NodeBoard instances found!")
		return

	node_boards.sort_custom(func(a, b): return a.name.naturalnocase_to(b.name) < 0)

	for i in range(min(node_boards.size(), REFERENCE_LAYOUT.size())):
		var node: NodeBoard = node_boards[i]
		node.type = REFERENCE_LAYOUT[i]

	for i in range(REFERENCE_LAYOUT.size(), node_boards.size()):
		var node: NodeBoard = node_boards[i]
		node._visible = false

	print("wolkenwerk board: Applied reference layout to %d nodes (%d hidden)" %
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
		print("wolkenwerk board: Field distribution VALID (all %d types match Game Bible 3.8)" %
				EXPECTED_DISTRIBUTION.size())
	else:
		push_error("wolkenwerk board: Field distribution INVALID — see warnings above")


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
## (nach Namen: Node0, Node1, ... Node39) zurück.
func _get_sorted_nodes() -> Array[NodeBoard]:
	var nodes: Array[NodeBoard] = []
	if not has_node("Nodes"):
		return nodes
	for child in $Nodes.get_children():
		if child is NodeBoard and child._visible:
			nodes.append(child as NodeBoard)
	nodes.sort_custom(func(a, b): return a.name.naturalnocase_to(b.name) < 0)
	return nodes


## Wolkenwerk: Inline-Abzweigungs-Verdrahtung (0-basierte Felder 0-39).
## Anders als die Standard-Inseln (Hauptpfad 1-32 + Branches 33-40)
## verwendet Wolkenwerk Inline-Abzweigungen, bei denen die Branch-Felder
## im selben Nummernbereich wie der Hauptpfad liegen (10-13, 22-24).
##
## Die Basis-Verdrahtung ist ein geschlossener Loop aller 40 Felder.
## Die Abzweigungs-Sonderregeln (windkanal_express, regenbogen_gleitfahrt)
## überlagern diesen Loop; sie werden in einem späteren Milestone
## (Board-Sonderregeln) implementiert.
func _wire_branches() -> void:
	var sorted: Array[NodeBoard] = _get_sorted_nodes()
	if sorted.size() < 40:
		push_error("%s board: Not enough visible nodes for branch wiring (%d)" % [board_id, sorted.size()])
		return

	# Geschlossener Loop aller 40 Felder: 0→1→2→...→39→0
	for i: int in range(sorted.size()):
		var current: NodeBoard = sorted[i]
		var next_node: NodeBoard
		if i < sorted.size() - 1:
			next_node = sorted[i + 1]
		else:
			next_node = sorted[0]  # Loop: Feld 39 → Feld 0
		current.next = [current.get_path_to(next_node)]

	# Abzweigungen als Junction-Markierungen registrieren
	# (die tatsächliche Pfadwahl-Logik erfolgt über Sonderregeln)
	for branch: Dictionary in BRANCHES:
		var entry: int = branch["entry"]
		var entry_node: NodeBoard = sorted[entry - FIRST_FIELD]
		# Junction-Markierung: Zusätzlicher next-Eintrag für Pfadwahl-UI.
		# Beide Pfade (Hauptpfad + Abzweigung) beginnen auf demselben
		# ersten Feld; die Sonderregel entscheidet über Effekte und Tempo.
		var fields: Array = branch["fields"]
		var first_branch: NodeBoard = sorted[fields[0] - FIRST_FIELD]
		# Prüfen ob first_branch bereits in next ist (Inline-Branch)
		var already_present: bool = false
		for np: NodePath in entry_node.next:
			if entry_node.get_node(np) == first_branch:
				already_present = true
				break
		if not already_present:
			var entry_next: Array[NodePath] = entry_node.next.duplicate()
			entry_next.append(entry_node.get_path_to(first_branch))
			entry_node.next = entry_next

	print("%s board: Branch wiring complete — full loop 0-39, %d inline branches (special rules pending)" %
			[board_id, BRANCHES.size()])

# EVENT SYSTEM — Party Arena Milestone 6c
# Game Bible: design/gdd/field-event.md, design/gdd/world-wolkenwerk.md
# ============================================================

# Ereignis-Kartei: Definitionen (ID, Name, Gewicht)
const EVENT_DEFINITIONS: Dictionary = 	{
		"turbulenz": {
			"name": "Turbulenz",
			"weight": 0,
		},
		"aufwind": {
			"name": "Aufwind",
			"weight": 0,
		},
		"regenbogen_schatz": {
			"name": "Regenbogen-Schatz",
			"weight": 0,
		},
		"nebelbank": {
			"name": "Nebelbank",
			"weight": 0,
		},
		"windstoss": {
			"name": "Windstoß",
			"weight": 0,
		},
	}

# Gebundene Ereignis-Felder (Feld -> Event-ID)
const BOUND_EVENTS: Dictionary = {
	4: "turbulenz",
	12: "aufwind",
	20: "regenbogen_schatz",
	30: "nebelbank",
	36: "windstoss",
}

# Abzweigungs-Sonderregeln
const SPECIAL_RULES: Array[String] = ["windkanal_express", "regenbogen_gleitfahrt"]

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

	# Alle Felder sind gebunden (deterministisch)
	if BOUND_EVENTS.has(field_num):
		event_id = BOUND_EVENTS[field_num]
	else:
		# Fallback: gewichtete Ziehung
		event_id = _draw_weighted_event()
		if event_id.is_empty():
			ctrl.board_continue()
			return

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
		"turbulenz":
			await _ev_turbulenz(player, ctrl)
		"aufwind":
			await _ev_aufwind(player, ctrl)
		"regenbogen_schatz":
			await _ev_regenbogen_schatz(player, ctrl)
		"nebelbank":
			await _ev_nebelbank(player, ctrl)
		"windstoss":
			await _ev_windstoss(player, ctrl)
		_:
			push_warning("%s: Unknown event \'%s\'" % [board_id, event_id])

# --- Ereignis-Effekte ---

## Turbulenz: Alle Spieler tauschen zufällig ihre Positionen (Permutation ohne Fixpunkt).
func _ev_turbulenz(_player: Node3D, ctrl: Controller) -> void:
	if ctrl.players.size() < 2:
		return

	if ctrl.players.size() == 2:
		var pos0: NodeBoard = ctrl.players[0].space
		var pos1: NodeBoard = ctrl.players[1].space
		ctrl.players[0].teleport_to(pos1)
		ctrl.players[1].teleport_to(pos0)
		await ctrl.get_tree().create_timer(0.3).timeout
		return

	var positions: Array[NodeBoard] = []
	for p: PlayerBoard in ctrl.players:
		positions.append(p.space)

	# Fisher-Yates Shuffle
	var shuffled: Array[NodeBoard] = positions.duplicate()
	for i in range(shuffled.size() - 1, 0, -1):
		var j: int = randi() % (i + 1)
		var tmp: NodeBoard = shuffled[i]
		shuffled[i] = shuffled[j]
		shuffled[j] = tmp

	# Korrigiere Fixpunkte (Tausch mit Nachbar)
	for i in range(shuffled.size()):
		if shuffled[i] == positions[i]:
			var swap_idx: int = (i + 1) % shuffled.size()
			var tmp2: NodeBoard = shuffled[i]
			shuffled[i] = shuffled[swap_idx]
			shuffled[swap_idx] = tmp2

	for i in range(ctrl.players.size()):
		ctrl.players[i].teleport_to(shuffled[i])
	await ctrl.get_tree().create_timer(0.5).timeout

## Aufwind: Aktiver Spieler 5 Felder vorwärts (keine Feld-Effekte).
func _ev_aufwind(player: Node3D, ctrl: Controller) -> void:
	var p_active: PlayerBoard = player as PlayerBoard
	if p_active:
		await _move_player_forward(p_active, 5, ctrl)

## Regenbogen-Schatz: Aktiver Spieler +8 Münzen.
func _ev_regenbogen_schatz(player: Node3D, _ctrl: Controller) -> void:
	var p_active: PlayerBoard = player as PlayerBoard
	if p_active:
		p_active.cookies += 8

## Nebelbank: Nächster Wurf des aktiven Spielers -2 (Minimum 1).
func _ev_nebelbank(player: Node3D, _ctrl: Controller) -> void:
	var p_active: PlayerBoard = player as PlayerBoard
	if p_active:
		p_active.add_roll_modifier(-2, 1)

## Windstoß: Alle Spieler 2 Felder vorwärts (keine Feld-Effekte).
func _ev_windstoss(_player: Node3D, ctrl: Controller) -> void:
	for p: PlayerBoard in ctrl.players:
		await _move_player_forward(p, 2, ctrl)

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
