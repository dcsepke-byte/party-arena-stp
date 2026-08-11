extends Node3D

# Party Arena: Test-Board mit korrektem Feldtypen-System
# Game Bible Referenz: design/gdd/board-architecture.md, Sektion 3.3
#
# Dieses Board baut die Feldtypen zum Ladenzeitpunkt gemäß
# dem Referenz-Layout auf. Die NodeBoard-Instanzen werden
# aus der board.tscn geladen; ihre Typen werden hier gesetzt.

# Referenz-Layout (Indizes 0–39) gemäß Game Bible Tabelle 3.3
const REFERENCE_LAYOUT: Array[int] = [
	NodeBoard.FELD_TYP.START,         # 0
	NodeBoard.FELD_TYP.MINISPIEL,      # 1
	NodeBoard.FELD_TYP.EREIGNIS,       # 2
	NodeBoard.FELD_TYP.MUENZ_BONUS,    # 3
	NodeBoard.FELD_TYP.MINISPIEL,      # 4
	NodeBoard.FELD_TYP.GLUECK_PECH,    # 5
	NodeBoard.FELD_TYP.EREIGNIS,       # 6
	NodeBoard.FELD_TYP.MINISPIEL,      # 7
	NodeBoard.FELD_TYP.ITEM_SHOP,      # 8
	NodeBoard.FELD_TYP.MINISPIEL,      # 9
	NodeBoard.FELD_TYP.MINISPIEL,      # 10
	NodeBoard.FELD_TYP.MINISPIEL,      # 11
	NodeBoard.FELD_TYP.STERN_SHOP,     # 12
	NodeBoard.FELD_TYP.MINISPIEL,      # 13
	NodeBoard.FELD_TYP.EREIGNIS,       # 14
	NodeBoard.FELD_TYP.GLUECK_PECH,    # 15
	NodeBoard.FELD_TYP.MINISPIEL,      # 16
	NodeBoard.FELD_TYP.MINISPIEL,      # 17
	NodeBoard.FELD_TYP.EREIGNIS,       # 18
	NodeBoard.FELD_TYP.MINISPIEL,      # 19
	NodeBoard.FELD_TYP.MUENZ_BONUS,    # 20
	NodeBoard.FELD_TYP.MINISPIEL,      # 21
	NodeBoard.FELD_TYP.MINISPIEL,      # 22
	NodeBoard.FELD_TYP.MINISPIEL,      # 23
	NodeBoard.FELD_TYP.MINISPIEL,      # 24
	NodeBoard.FELD_TYP.EREIGNIS,       # 25
	NodeBoard.FELD_TYP.STERN_SHOP,     # 26
	NodeBoard.FELD_TYP.GLUECK_PECH,    # 27
	NodeBoard.FELD_TYP.ITEM_SHOP,      # 28
	NodeBoard.FELD_TYP.MINISPIEL,      # 29
	NodeBoard.FELD_TYP.MINISPIEL,      # 30
	NodeBoard.FELD_TYP.MINISPIEL,      # 31
	NodeBoard.FELD_TYP.MINISPIEL,      # 32 (Abzweigung A1)
	NodeBoard.FELD_TYP.MUENZ_BONUS,    # 33 (Abzweigung A2)
	NodeBoard.FELD_TYP.MINISPIEL,      # 34 (Abzweigung A3)
	NodeBoard.FELD_TYP.MINISPIEL,      # 35 (Abzweigung A4)
	NodeBoard.FELD_TYP.MINISPIEL,      # 36 (Abzweigung B1)
	NodeBoard.FELD_TYP.MUENZ_BONUS,    # 37 (Abzweigung B2)
	NodeBoard.FELD_TYP.MINISPIEL,      # 38 (Abzweigung B3)
	NodeBoard.FELD_TYP.MINISPIEL,      # 39 (Abzweigung B4)
]

# Erwartete Verteilung (Game Bible 3.2)
const EXPECTED_DISTRIBUTION := {
	NodeBoard.FELD_TYP.START: 1,
	NodeBoard.FELD_TYP.STERN_SHOP: 2,
	NodeBoard.FELD_TYP.ITEM_SHOP: 2,
	NodeBoard.FELD_TYP.EREIGNIS: 5,
	NodeBoard.FELD_TYP.GLUECK_PECH: 3,
	NodeBoard.FELD_TYP.MUENZ_BONUS: 4,
	NodeBoard.FELD_TYP.MINISPIEL: 23,
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


func _ready() -> void:
	# Wende das Referenz-Layout auf die geladenen NodeBoard-Knoten an
	_apply_reference_layout()
	# Validiere die Verteilung
	_validate_distribution()


## Wendet die Feldtypen des Referenz-Layouts auf die vorhandenen
## NodeBoard-Knoten an (nach Namen sortiert: Node1, Node2, ...).
func _apply_reference_layout() -> void:
	if not has_node("Nodes"):
		push_error("Test board: 'Nodes' container not found!")
		return

	var nodes_container := $Nodes
	var node_boards: Array[Node] = []

	# Sammle alle NodeBoard-Instanzen
	for child in nodes_container.get_children():
		if child is NodeBoard:
			node_boards.append(child)

	if node_boards.is_empty():
		push_error("Test board: No NodeBoard instances found!")
		return

	# Sortiere nach Namen (Node1 < Node2 < ... < Node50)
	node_boards.sort_custom(func(a, b): return a.name.naturalnocase_to(b.name) < 0)

	# Setze Feldtypen gemäß Referenz-Layout
	for i in range(min(node_boards.size(), REFERENCE_LAYOUT.size())):
		var node: NodeBoard = node_boards[i]
		node.type = REFERENCE_LAYOUT[i]

	# Verstecke überzählige Knoten (>39)
	for i in range(REFERENCE_LAYOUT.size(), node_boards.size()):
		var node: NodeBoard = node_boards[i]
		node._visible = false

	print("Test board: Applied reference layout to %d nodes (%d hidden)" %
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
		print("Test board: Field distribution VALID (all %d types match Game Bible 3.2)" %
				EXPECTED_DISTRIBUTION.size())
	else:
		push_error("Test board: Field distribution INVALID — see warnings above")


## Gibt die aktuelle Feld-Verteilung als Dictionary zurück.
## Schlüssel: FELD_TYP-Integer, Wert: Anzahl sichtbarer Felder dieses Typs.
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


# Legacy: Event-Handler für board-spezifische Ereignisse (EREIGNIS-Felder)
func handle_event(player: Node3D, space: Node3D):
	# Vereinfachter Event-Handler für das Test-Board
	# Detaillierte Ereignis-Logik folgt in field-event.md
	match space.name:
		"Node6":
			player.walk_to($Nodes/Node27)
		"Node25":
			player.walk_to($Nodes/Node26)
		"Node31":
			player.walk_to($Nodes/Node29)
		"Node26":
			player.walk_to($Nodes/Node25)
		"Node27":
			player.walk_to($Nodes/Node6)
		"Node29":
			player.walk_to($Nodes/Node31)
		"Node15":
			player.walk_to($Nodes/Node50)
		"Node19":
			player.walk_to($Nodes/Node41)
		"Node41":
			player.walk_to($Nodes/Node19)
		"Node50":
			player.walk_to($Nodes/Node15)

	await player.walking_ended
	$Controller.board_continue()
