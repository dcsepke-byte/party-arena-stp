#!/usr/bin/env python3
"""Transform all board.gd files for Milestone 6c event system."""
import os
import re

BASE = "/opt/data/SuperTuxParty/plugins/boards"

# Common helper methods (appended after event effects)
COMMON_HELPERS = '''
# ============================================================
# HILFSMETHODEN (Event-System, gemeinsam für alle Inseln)
# ============================================================

## Extrahiert die Feld-Nummer aus dem Node-Namen (Node16 → 16).
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
## An Junctions wird der Hauptpfad gewählt.
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


## Gibt die Sonderregel für eine Abzweigung zurück (Name → rule_id).
func get_branch_special_rule(branch_name: String) -> String:
	for branch: Dictionary in BRANCHES:
		if branch.get("name", "") == branch_name:
			return branch.get("rule", "")
	return ""
'''

EVENT_SYSTEM_TEMPLATE = '''
# ============================================================
# EVENT SYSTEM — Party Arena Milestone 6c
# Game Bible: design/gdd/field-event.md, {world_doc}
# ============================================================

# Ereignis-Kartei: Definitionen (ID, Name, Gewicht für ungebundene Felder)
const EVENT_DEFINITIONS: Dictionary = {events_dict}

# Gebundene Ereignis-Felder (Feld → Event-ID)
const BOUND_EVENTS: Dictionary = {bound_dict}

# Abzweigungs-Sonderregeln
const SPECIAL_RULES: Array[String] = {special_rules}


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
## Wird vom Controller via trigger_event-Signal aufgerufen.
func handle_event(player: Node3D, space: Node3D) -> void:
	var ctrl: Controller = $Controller if has_node("Controller") else null
	if not ctrl:
		push_error("%s: handle_event called without Controller!" % board_id)
		return

	var field_num: int = _get_field_number(space)
	var event_id: String = ""
{event_selection}

	if event_id.is_empty():
		push_warning("%s: No event drawn for field %d" % [board_id, field_num])
		ctrl.board_continue()
		return

	# Führe Ereignis-Effekt aus
	var event_data: Dictionary = EVENT_DEFINITIONS.get(event_id, {{}})
	var event_name: String = event_data.get("name", event_id)
	print("%s: Event '%s' triggered on field %d by player %d" %
			[board_id, event_name, field_num, _get_player_id(player)])

	await _execute_event(event_id, player, ctrl)

	# Signalisiere Abschluss an den Controller
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
{effect_dispatch}
		_:
			push_warning("%s: Unknown event '%s'" % [board_id, event_id])
'''

HANDLE_EVENT_STUB = '''	# Event-Handler für board-spezifische Ereignisse (EREIGNIS-Felder)
	func handle_event(player: Node3D, space: Node3D):
		# Platzhalter: Insel-spezifische Ereignis-Logik folgt
		# in einem späteren Milestone (Board-Events & Effekte)
		await get_tree().process_frame
		if has_node("Controller"):
			$Controller.board_continue()'''


def remove_stub(content):
    """Remove the handle_event stub."""
    marker = "# Event-Handler für board-spezifische Ereignisse (EREIGNIS-Felder)"
    if marker not in content:
        return content

    idx = content.find(marker)
    # Find the end of the function
    end_marker = content.find("\n", content.find("board_continue()", idx))
    if end_marker == -1:
        end_marker = len(content)
    else:
        # Find next non-empty line
        rest = content[end_marker:]
        for line in rest.split("\n"):
            if line.strip():
                break
            end_marker += 1

    return content[:idx] + content[end_marker:]


def add_ready_call(content):
    """Add _init_event_system() call to _ready()."""
    old = "func _ready() -> void:\n\t\t_apply_reference_layout()\n\t\t_wire_branches()\n\t\t_validate_distribution()"
    new = "func _ready() -> void:\n\t\t_apply_reference_layout()\n\t\t_wire_branches()\n\t\t_validate_distribution()\n\t\t_init_event_system()"
    if old in content:
        return content.replace(old, new)
    return content


def process_board(board_name, events, bound_events, special_rules,
                  event_selection_code, world_doc_name, effect_methods):
    """Process a single board.gd file."""
    filepath = os.path.join(BASE, board_name, "board.gd")
    with open(filepath, "r") as f:
        content = f.read()

    # Remove existing stub
    content = remove_stub(content)

    # Add _init_event_system() call
    content = add_ready_call(content)

    # Build event system code
    events_dict_str = "{\n"
    for ev_id, ev_data in events.items():
        events_dict_str += f'\t\t"{ev_id}": {{\n'
        events_dict_str += f'\t\t\t"name": "{ev_data["name"]}",\n'
        events_dict_str += f'\t\t\t"weight": {ev_data["weight"]},\n'
        events_dict_str += '\t\t},\n'
    events_dict_str += "\t}"

    bound_dict_str = "{\n"
    for field, ev_id in sorted(bound_events.items()):
        bound_dict_str += f'\t\t{field}: "{ev_id}",\n'
    bound_dict_str += "\t}"

    special_rules_str = str(special_rules).replace("'", '"')

    # Build event selection code
    event_selection = event_selection_code

    # Build effect dispatch
    dispatch_lines = []
    for ev_id in events:
        dispatch_lines.append(f'\t\t"{ev_id}":')
        dispatch_lines.append(f'\t\t\tawait _ev_{ev_id}(player, ctrl)')
    dispatch_str = "\n".join(dispatch_lines)

    # Format the template
    event_system = EVENT_SYSTEM_TEMPLATE.format(
        world_doc=f"design/gdd/{world_doc_name}",
        events_dict=events_dict_str,
        bound_dict=bound_dict_str,
        special_rules=special_rules_str,
        event_selection=event_selection_code,
        effect_dispatch=dispatch_str,
    )

    # Append event effect methods
    event_system += "\n\n# --- Ereignis-Effekte ---\n\n"
    event_system += effect_methods

    # Append common helpers
    event_system += COMMON_HELPERS

    # Insert after BRANCHES section (before _ready)
    # Find the line after BRANCHES definition
    branches_end = content.find("const FIRST_FIELD")
    if branches_end == -1:
        print(f"  WARNING: Could not find FIRST_FIELD in {board_name}")
        # Append at end of file
        content = content.rstrip() + "\n" + event_system
    else:
        # Find end of FIRST_FIELD line
        first_field_end = content.find("\n\n", branches_end)
        if first_field_end == -1:
            first_field_end = content.find("\nfunc _ready()", branches_end)
        if first_field_end == -1:
            content = content.rstrip() + "\n" + event_system
        else:
            content = content[:first_field_end] + "\n\n" + event_system + "\n" + content[first_field_end:]

    # Also add "rule" to BRANCHES
    content = add_branch_rules(content, board_name)

    with open(filepath, "w") as f:
        f.write(content)

    print(f"  ✓ {board_name}/board.gd written ({len(content)} chars)")


def add_branch_rules(content, board_name):
    """Add rule field to BRANCHES dict entries."""
    rule_map = {
        "sonnenstrand": {"Korallenriff": "", "Klippen": ""},
        "zuckerwald": {"Schokoladen-Fluss": "floss_fahrt", "Zuckerwatte-Wolken": "zuckerwatte_bonus_minigame"},
        "wolkenwerk": {"Windkanal": "windkanal_express", "Regenbogen-Rutsche": "regenbogen_gleitfahrt"},
        "frostgipfel": {"Eishöhle": "eishoehlen_dunkelheit", "Vereister See": "eisglaette_rutsch"},
        "dschungeltempel": {"Lianen-Schwung": "lianen_express", "Tempel-Inneres": "tempel_fluch_zone"},
        "mechanik-stadt": {"Rohrpost-Teleport": "rohrpost_teleport", "Förderband-Fabrik": "foerderband_fabrik"},
        "sternenzitadelle": {"Kosmische Drift": "kosmische_drift", "Geister-Felder": "geister_felder"},
    }
    rules = rule_map.get(board_name, {})
    for name, rule in rules.items():
        # Find `"name": "X",` and add rule after fields
        pattern = f'"name": "{name}"'
        if pattern in content:
            # Check if "rule" already exists
            if f'"rule"' in content[content.find(pattern):content.find(pattern)+200]:
                continue
            # Add rule after delta
            delta_pattern = f'"name": "{name}"'
            pos = content.find(delta_pattern)
            # Find next line that has "fields"
            fields_pos = content.find('"fields"', pos)
            bracket_pos = content.find(']', fields_pos)
            # Insert rule after the fields closing bracket
            insert_pos = bracket_pos + 1
            content = content[:insert_pos] + f',\n\t\t\t"rule": "{rule}"' + content[insert_pos:]
    return content


# ============================================================
# BOARD-SPECIFIC DATA
# ============================================================

# Zuckerwald
process_board("zuckerwald",
    events={
        "klebriger_boden": {"name": "Klebriger Boden", "weight": 35},
        "zucker_rausch": {"name": "Zucker-Rausch", "weight": 35},
        "keks_regen": {"name": "Keks-Regen", "weight": 30},
    },
    bound_events={37: "klebriger_boden", 38: "zucker_rausch"},
    special_rules=["floss_fahrt", "zuckerwatte_bonus_minigame"],
    event_selection_code='''\t# 1. Bestimme Ereignis: gebunden oder gewichtete Auslosung
\tif BOUND_EVENTS.has(field_num):
\t\tevent_id = BOUND_EVENTS[field_num]
\telse:
\t\tevent_id = _draw_weighted_event()''',
    world_doc_name="world-zuckerwald.md",
    effect_methods='''## Klebriger Boden: Aktiver Spieler -2 auf nächsten Wurf (Minimum 1).
func _ev_klebriger_boden(player: Node3D, _ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard
\tif p_active:
\t\tp_active.add_roll_modifier(-2, 1)


## Zucker-Rausch: Aktiver Spieler +3 Münzen und 3 Felder vorwärts.
func _ev_zucker_rausch(player: Node3D, ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard
\tif p_active:
\t\tp_active.cookies += 3
\t\tawait _move_player_forward(p_active, 3, ctrl)


## Keks-Regen: Alle Spieler erhalten +3 Münzen.
func _ev_keks_regen(_player: Node3D, ctrl: Controller) -> void:
\tfor p: PlayerBoard in ctrl.players:
\t\tp.cookies += 3''',
)

# Wolkenwerk (all bound, 0-based fields)
process_board("wolkenwerk",
    events={
        "turbulenz": {"name": "Turbulenz", "weight": 0},
        "aufwind": {"name": "Aufwind", "weight": 0},
        "regenbogen_schatz": {"name": "Regenbogen-Schatz", "weight": 0},
        "nebelbank": {"name": "Nebelbank", "weight": 0},
        "windstoss": {"name": "Windstoß", "weight": 0},
    },
    bound_events={4: "turbulenz", 12: "aufwind", 20: "regenbogen_schatz", 30: "nebelbank", 36: "windstoss"},
    special_rules=["windkanal_express", "regenbogen_gleitfahrt"],
    event_selection_code='''\t# Alle Felder sind gebunden (deterministisch laut world-wolkenwerk.md 3.4)
\tif BOUND_EVENTS.has(field_num):
\t\tevent_id = BOUND_EVENTS[field_num]
\telse:
\t\t# Fallback: gewichtete Ziehung (für zukünftige ungebundene Felder)
\t\tevent_id = _draw_weighted_event()
\t\tif event_id.is_empty():
\t\t\t# Keine Events verfügbar — Feld nicht in der Kartei
\t\t\tctrl.board_continue()
\t\t\treturn''',
    world_doc_name="world-wolkenwerk.md",
    effect_methods='''## Turbulenz: Alle Spieler tauschen zufällig ihre Positionen (Permutation ohne Fixpunkt).
func _ev_turbulenz(_player: Node3D, ctrl: Controller) -> void:
\tif ctrl.players.size() < 2:
\t\treturn

\tif ctrl.players.size() == 2:
\t\t# Zwei Spieler: tauschen einfach
\t\tvar pos0: NodeBoard = ctrl.players[0].space
\t\tvar pos1: NodeBoard = ctrl.players[1].space
\t\tctrl.players[0].teleport_to(pos1)
\t\tctrl.players[1].teleport_to(pos0)
\t\tawait ctrl.get_tree().create_timer(0.3).timeout
\t\treturn

\t# Mehr als 2: zufällige Permutation ohne Fixpunkt
\tvar positions: Array[NodeBoard] = []
\tfor p: PlayerBoard in ctrl.players:
\t\tpositions.append(p.space)

\t# Fisher-Yates Shuffle
\tvar shuffled: Array[NodeBoard] = positions.duplicate()
\tfor i in range(shuffled.size() - 1, 0, -1):
\t\tvar j: int = randi() % (i + 1)
\t\tvar tmp: NodeBoard = shuffled[i]
\t\tshuffled[i] = shuffled[j]
\t\tshuffled[j] = tmp

\t# Prüfe auf Fixpunkte und korrigiere (Tausch mit Nachbar)
\tfor i in range(shuffled.size()):
\t\tif shuffled[i] == positions[i]:
\t\t\tvar swap_idx: int = (i + 1) % shuffled.size()
\t\t\tvar tmp2: NodeBoard = shuffled[i]
\t\t\tshuffled[i] = shuffled[swap_idx]
\t\t\tshuffled[swap_idx] = tmp2

\t# Teleportiere alle Spieler (Effekt-Platzierung)
\tfor i in range(ctrl.players.size()):
\t\tctrl.players[i].teleport_to(shuffled[i])
\tawait ctrl.get_tree().create_timer(0.5).timeout


## Aufwind: Aktiver Spieler 5 Felder vorwärts (keine Feld-Effekte).
func _ev_aufwind(player: Node3D, ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard
\tif p_active:
\t\tawait _move_player_forward(p_active, 5, ctrl)


## Regenbogen-Schatz: Aktiver Spieler +8 Münzen.
func _ev_regenbogen_schatz(player: Node3D, _ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard
\tif p_active:
\t\tp_active.cookies += 8


## Nebelbank: Nächster Wurf des aktiven Spielers -2 (Minimum 1).
func _ev_nebelbank(player: Node3D, _ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard
\tif p_active:
\t\tp_active.add_roll_modifier(-2, 1)


## Windstoß: Alle Spieler 2 Felder vorwärts (keine Feld-Effekte).
func _ev_windstoss(_player: Node3D, ctrl: Controller) -> void:
\tfor p: PlayerBoard in ctrl.players:
\t\tawait _move_player_forward(p, 2, ctrl)''',
)

# Frostgipfel
process_board("frostgipfel",
    events={
        "schneesturm": {"name": "Schneesturm", "weight": 30},
        "nordlicht": {"name": "Nordlicht", "weight": 40},
        "eiskristall_regen": {"name": "Eiskristall-Regen", "weight": 30},
    },
    bound_events={35: "schneesturm", 37: "eisglaette", 25: "nordlicht"},
    special_rules=["eishoehlen_dunkelheit", "eisglaette_rutsch"],
    event_selection_code='''\t# 1. Bestimme Ereignis: gebunden oder gewichtete Auslosung
\tif BOUND_EVENTS.has(field_num):
\t\tevent_id = BOUND_EVENTS[field_num]
\telse:
\t\tevent_id = _draw_weighted_event()''',
    world_doc_name="world-frostgipfel.md",
    effect_methods='''## Schneesturm: Aktiver Spieler setzt nächste Runde aus.
func _ev_schneesturm(player: Node3D, _ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard
\tif p_active:
\t\t_skip_turns[p_active.info.player_id] = true


## Nordlicht: Aktiver Spieler +5 Münzen, +1 auf nächsten Wurf (Maximum 10).
func _ev_nordlicht(player: Node3D, _ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard
\tif p_active:
\t\tp_active.cookies += 5
\t\tp_active.add_roll_modifier(1, 1)


## Eiskristall-Regen: Aktiver Spieler +3 Münzen, ärmster Spieler +3 Münzen.
func _ev_eiskristall_regen(player: Node3D, ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard
\tif p_active:
\t\tp_active.cookies += 3

\tvar poorest: PlayerBoard = _get_poorest_player(ctrl)
\tif poorest and poorest != p_active:
\t\tpoorest.cookies += 3


## Eisglätte: Aktiver Spieler rutscht 1-3 Felder in zufälliger Richtung.
func _ev_eisglaette(player: Node3D, ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard
\tif not p_active:
\t\treturn

\t# W6/2 aufgerundet → 1-3 Felder
\tvar distance: int = ceili(float(randi() % 6 + 1) / 2.0)
\tvar forward: bool = randi() % 2 == 0

\tif forward:
\t\tawait _move_player_forward(p_active, distance, ctrl)
\telse:
\t\tawait _move_player_backward(p_active, distance, ctrl)''',
)

# Dschungeltempel
process_board("dschungeltempel",
    events={
        "goldrausch": {"name": "Goldrausch", "weight": 35},
        "lianen_segen": {"name": "Lianen-Segen", "weight": 30},
        "fluch_des_tempels": {"name": "Fluch des Tempels", "weight": 35},
    },
    bound_events={38: "fluch_des_tempels"},
    special_rules=["lianen_express", "tempel_fluch_zone"],
    event_selection_code='''\t# 1. Bestimme Ereignis: gebunden oder gewichtete Auslosung
\tif BOUND_EVENTS.has(field_num):
\t\tevent_id = BOUND_EVENTS[field_num]
\telse:
\t\tevent_id = _draw_weighted_event()''',
    world_doc_name="world-dschungeltempel.md",
    effect_methods='''## Goldrausch: Ärmster Spieler erhält +8 Münzen (Catch-up).
func _ev_goldrausch(_player: Node3D, ctrl: Controller) -> void:
\t# Finde den/die Spieler mit den wenigsten Münzen
\tvar min_coins: int = 999999
\tfor p: PlayerBoard in ctrl.players:
\t\t# Primär Sterne, sekundär Münzen (Rangliste)
\t\tvar rank_coins: int = p.stars * 1000 + p.cookies
\t\tif rank_coins < min_coins:
\t\t\tmin_coins = rank_coins

\t# Alle Spieler mit diesem Minimum erhalten +8
\tfor p: PlayerBoard in ctrl.players:
\t\tvar rank_coins: int = p.stars * 1000 + p.cookies
\t\tif rank_coins == min_coins:
\t\t\tp.cookies += 8


## Lianen-Segen: Aktiver Spieler +5 Münzen und 2 Felder vorwärts.
func _ev_lianen_segen(player: Node3D, ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard
\tif p_active:
\t\tp_active.cookies += 5
\t\tawait _move_player_forward(p_active, 2, ctrl)


## Fluch des Tempels: Ungebunden → reichster Spieler -5 Münzen.
## Gebunden (Feld 38) → aktiver Spieler -5 Münzen.
func _ev_fluch_des_tempels(player: Node3D, ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard
\tif not p_active:
\t\treturn

\t# Prüfe ob gebunden (Feld 38 im Tempel-Inneren)
\tvar field_num: int = _get_field_number(p_active.space)
\tvar is_bound: bool = BOUND_EVENTS.has(field_num) and BOUND_EVENTS[field_num] == "fluch_des_tempels"

\tif is_bound:
\t\t# Gebunden: aktiver Spieler verliert -5 Münzen
\t\tp_active.cookies = max(0, p_active.cookies - 5)
\telse:
\t\t# Ungebunden: reichster Spieler verliert -5 Münzen
\t\tvar richest: PlayerBoard = _get_richest_player(ctrl)
\t\tif richest:
\t\t\trichest.cookies = max(0, richest.cookies - 5)''',
)

# Mechanik-Stadt
process_board("mechanik-stadt",
    events={
        "erfindermesse": {"name": "Erfindermesse", "weight": 25},
        "zahnrad_stau": {"name": "Zahnrad-Stau", "weight": 35},
        "dampf_explosion": {"name": "Dampf-Explosion", "weight": 40},
    },
    bound_events={37: "zahnrad_stau"},
    special_rules=["rohrpost_teleport", "foerderband_fabrik"],
    event_selection_code='''\t# 1. Bestimme Ereignis: gebunden oder gewichtete Auslosung
\tif BOUND_EVENTS.has(field_num):
\t\tevent_id = BOUND_EVENTS[field_num]
\telse:
\t\tevent_id = _draw_weighted_event()''',
    world_doc_name="world-mechanik-stadt.md",
    effect_methods='''## Erfindermesse: Alle Item-Preise -2 für den Rest der Runde.
func _ev_erfindermesse(_player: Node3D, _ctrl: Controller) -> void:
\t_erfindermesse_active = true
\tprint("%s: Erfindermesse aktiviert — Item-Preise -2 für diese Runde" % board_id)


## Zahnrad-Stau: Aktiver Spieler setzt nächste Runde aus.
func _ev_zahnrad_stau(player: Node3D, _ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard
\tif p_active:
\t\t_skip_turns[p_active.info.player_id] = true


## Dampf-Explosion: Alle Spieler auf zufällige Hauptpfad-Felder (1-32).
func _ev_dampf_explosion(_player: Node3D, ctrl: Controller) -> void:
\tif ctrl.players.size() < 2:
\t\treturn

\tvar sorted: Array[NodeBoard] = _get_sorted_nodes()
\t# Hauptpfad-Felder: 1-32 (Indizes 0-31)
\tvar main_path: Array[NodeBoard] = []
\tfor i in range(32):
\t\tif i < sorted.size():
\t\t\tmain_path.append(sorted[i])

\tif main_path.size() < 2:
\t\treturn

\t# Zufällige Felder für jeden Spieler (ohne Zurücklegen)
\tvar available: Array[NodeBoard] = main_path.duplicate()
\tfor p: PlayerBoard in ctrl.players:
\t\tif available.size() == 0:
\t\t\tavailable = main_path.duplicate()
\t\tvar idx: int = randi() % available.size()
\t\tvar target: NodeBoard = available[idx]
\t\tavailable.remove_at(idx)
\t\tp.teleport_to(target)

\tawait ctrl.get_tree().create_timer(0.5).timeout''',
)

# Sternenzitadelle
process_board("sternenzitadelle",
    events={
        "sternen_regen": {"name": "Sternen-Regen", "weight": 25},
        "zeit_verzerrung": {"name": "Zeit-Verzerrung", "weight": 25},
        "schwarzes_loch": {"name": "Schwarzes Loch", "weight": 25},
        "arenastars_segen": {"name": "ArenaStars Segen", "weight": 25},
    },
    bound_events={36: "zeit_verzerrung", 38: "schwarzes_loch"},
    special_rules=["kosmische_drift", "geister_felder"],
    event_selection_code='''\t# 1. Bestimme Ereignis: gebunden oder gewichtete Auslosung
\tif BOUND_EVENTS.has(field_num):
\t\tevent_id = BOUND_EVENTS[field_num]
\telse:
\t\tevent_id = _draw_weighted_event()''',
    world_doc_name="world-sternenzitadelle.md",
    effect_methods='''## Sternen-Regen: Alle +5 Münzen, aktiver Spieler +3 extra (insgesamt +8).
func _ev_sternen_regen(player: Node3D, ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard
\tfor p: PlayerBoard in ctrl.players:
\t\tp.cookies += 5
\t# Aktiver Spieler bekommt zusätzlich +3
\tif p_active:
\t\tp_active.cookies += 3


## Zeit-Verzerrung: Aktiver Spieler erhält Extra-Zug.
## (Vereinfachte Implementierung: +1 Bonus-Wurf-Modifikator)
func _ev_zeit_verzerrung(player: Node3D, _ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard
\tif p_active:
\t\t# Signalisiere Extra-Zug über board-Flag (Controller prüft dies)
\t\t_extra_turn_player_id = p_active.info.player_id


## Schwarzes Loch: Aktiver + 1 zufälliger Spieler verlieren je 1 Item.
func _ev_schwarzes_loch(player: Node3D, ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard

\t# Sammle Zielspieler (aktiver + 1 zufälliger anderer)
\tvar targets: Array[PlayerBoard] = []
\tif p_active and p_active.items.size() > 0:
\t\ttargets.append(p_active)

\tvar others: Array[PlayerBoard] = _get_other_players(ctrl, p_active)
\tif others.size() > 0:
\t\tvar other: PlayerBoard = others[randi() % others.size()]
\t\tif other.items.size() > 0:
\t\t\ttargets.append(other)

\t# Zerstöre je 1 zufälliges Item
\tfor target: PlayerBoard in targets:
\t\tif target.items.size() > 0:
\t\t\tvar idx: int = randi() % target.items.size()
\t\t\ttarget.remove_item(target.items[idx])


## ArenaStars Segen: Aktiver Spieler erhält einen Bonus-Stern.
func _ev_arenastars_segen(player: Node3D, _ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard
\tif p_active:
\t\tp_active.stars += 1''',
)

print()
print("✅ All 6 board.gd files updated successfully!")
