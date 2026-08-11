#!/usr/bin/env python3
"""Fix the board.gd files - cleanly append event system, replace stubs."""
import os

BASE = "/opt/data/SuperTuxParty/plugins/boards"

# Common helpers shared by all boards
COMMON_HELPERS = '''
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
'''


def build_event_dict(events):
    """Build GDScript dictionary for EVENT_DEFINITIONS."""
    lines = ["\t{"]
    for ev_id, ev_data in events.items():
        lines.append(f'\t\t"{ev_id}": {{')
        lines.append(f'\t\t\t"name": "{ev_data["name"]}",')
        lines.append(f'\t\t\t"weight": {ev_data["weight"]},')
        lines.append('\t\t},')
    lines.append('\t}')
    return '\n'.join(lines)


def build_bound_dict(bound_events):
    """Build GDScript dictionary for BOUND_EVENTS."""
    if not bound_events:
        return '{}'
    lines = ['{']
    for field, ev_id in sorted(bound_events.items()):
        lines.append(f'\t{field}: "{ev_id}",')
    lines.append('}')
    return '\n'.join(lines)


def build_special_rules(rules):
    """Build GDScript array for SPECIAL_RULES."""
    if not rules:
        return '[]'
    quoted = ', '.join(f'"{r}"' for r in rules)
    return f'[{quoted}]'


def build_event_selection(has_bound, is_all_bound=False):
    """Build the event selection code block."""
    if is_all_bound:
        return '''\t# Alle Felder sind gebunden (deterministisch)
\tif BOUND_EVENTS.has(field_num):
\t\tevent_id = BOUND_EVENTS[field_num]
\telse:
\t\t# Fallback: gewichtete Ziehung
\t\tevent_id = _draw_weighted_event()
\t\tif event_id.is_empty():
\t\t\tctrl.board_continue()
\t\t\treturn'''
    elif has_bound:
        return '''\t# Bestimme Ereignis: gebunden oder gewichtete Auslosung
\tif BOUND_EVENTS.has(field_num):
\t\tevent_id = BOUND_EVENTS[field_num]
\telse:
\t\tevent_id = _draw_weighted_event()'''
    else:
        return '''\t# Keine gebundenen Felder — gewichtete Auslosung
\tif BOUND_EVENTS.has(field_num):
\t\tevent_id = BOUND_EVENTS[field_num]
\telse:
\t\tevent_id = _draw_weighted_event()'''


def build_effect_dispatch(events):
    """Build match dispatch for _execute_event."""
    lines = []
    for ev_id in events:
        lines.append(f'\t\t"{ev_id}":')
        lines.append(f'\t\t\tawait _ev_{ev_id}(player, ctrl)')
    lines.append('\t\t_:')
    lines.append('\t\t\tpush_warning("%s: Unknown event \\\'%s\\\'" % [board_id, event_id])')
    return '\n'.join(lines)


def build_event_system(events, bound_events, special_rules, event_selection, effect_dispatch,
                       world_doc, effect_methods, has_event_init=True):
    """Build the complete event system code block."""
    parts = []
    parts.append('# ============================================================')
    parts.append('# EVENT SYSTEM — Party Arena Milestone 6c')
    parts.append(f'# Game Bible: design/gdd/field-event.md, {world_doc}')
    parts.append('# ============================================================')
    parts.append('')
    parts.append('# Ereignis-Kartei: Definitionen (ID, Name, Gewicht)')
    parts.append(f'const EVENT_DEFINITIONS: Dictionary = {build_event_dict(events)}')
    parts.append('')
    parts.append('# Gebundene Ereignis-Felder (Feld -> Event-ID)')
    parts.append(f'const BOUND_EVENTS: Dictionary = {build_bound_dict(bound_events)}')
    parts.append('')
    parts.append('# Abzweigungs-Sonderregeln')
    parts.append(f'const SPECIAL_RULES: Array[String] = {build_special_rules(special_rules)}')
    parts.append('')

    # Extra state variables
    if has_event_init:
        parts.append('')
        parts.append('## Initialisiert das Ereignis-System: verbindet trigger_event-Signal mit handle_event.')
        parts.append('func _init_event_system() -> void:')
        parts.append('\tif has_node("Controller") and $Controller.has_signal("trigger_event"):')
        parts.append('\t\tif not $Controller.trigger_event.is_connected(handle_event):')
        parts.append('\t\t\t$Controller.trigger_event.connect(handle_event)')
        parts.append('\t\tprint("%s board: Event system initialized — %d events, %d bound fields, %d special rules" %')
        parts.append('\t\t\t\t[board_id, EVENT_DEFINITIONS.size(), BOUND_EVENTS.size(), SPECIAL_RULES.size()])')
        parts.append('\telse:')
        parts.append('\t\tpush_error("%s board: Controller not found or missing trigger_event signal!" % board_id)')
        parts.append('')
        parts.append('')
        parts.append('## Event-Handler für board-spezifische Ereignisse (EREIGNIS-Felder).')
        parts.append('func handle_event(player: Node3D, space: Node3D) -> void:')
        parts.append('\tvar ctrl: Controller = $Controller if has_node("Controller") else null')
        parts.append('\tif not ctrl:')
        parts.append('\t\tpush_error("%s: handle_event called without Controller!" % board_id)')
        parts.append('\t\treturn')
        parts.append('')
        parts.append('\tvar field_num: int = _get_field_number(space)')
        parts.append('\tvar event_id: String = ""')
        parts.append('')
        parts.append(event_selection)
        parts.append('')
        parts.append('\tif event_id.is_empty():')
        parts.append('\t\tpush_warning("%s: No event drawn for field %d" % [board_id, field_num])')
        parts.append('\t\tctrl.board_continue()')
        parts.append('\t\treturn')
        parts.append('')
        parts.append('\tvar event_data: Dictionary = EVENT_DEFINITIONS.get(event_id, {})')
        parts.append('\tvar event_name: String = event_data.get("name", event_id)')
        parts.append('\tprint("%s: Event \\\'%s\\\' triggered on field %d by player %d" %')
        parts.append('\t\t\t[board_id, event_name, field_num, _get_player_id(player)])')
        parts.append('')
        parts.append('\tawait _execute_event(event_id, player, ctrl)')
        parts.append('\tctrl.board_continue()')
        parts.append('')
        parts.append('')
        parts.append('## Zieht ein Ereignis aus dem Pool per gewichteter Auslosung.')
        parts.append('func _draw_weighted_event() -> String:')
        parts.append('\tvar total_weight: int = 0')
        parts.append('\tfor ev_id in EVENT_DEFINITIONS:')
        parts.append('\t\ttotal_weight += EVENT_DEFINITIONS[ev_id].get("weight", 0)')
        parts.append('')
        parts.append('\tif total_weight <= 0:')
        parts.append('\t\treturn ""')
        parts.append('')
        parts.append('\tvar roll: int = randi() % total_weight')
        parts.append('\tvar cumulative: int = 0')
        parts.append('\tfor ev_id in EVENT_DEFINITIONS:')
        parts.append('\t\tcumulative += EVENT_DEFINITIONS[ev_id].get("weight", 0)')
        parts.append('\t\tif roll < cumulative:')
        parts.append('\t\t\treturn ev_id')
        parts.append('')
        parts.append('\treturn EVENT_DEFINITIONS.keys()[0]  # Fallback')
        parts.append('')
        parts.append('')
        parts.append('## Führt den Effekt eines Ereignisses aus (Insel-spezifisch).')
        parts.append('func _execute_event(event_id: String, player: Node3D, ctrl: Controller) -> void:')
        parts.append('\tmatch event_id:')
        parts.append(effect_dispatch)
    parts.append('')
    parts.append('')
    parts.append('# --- Ereignis-Effekte ---')
    parts.append('')
    parts.append(effect_methods)

    return '\n'.join(parts)


def clean_file(content):
    """Remove any previously inserted event system code and old stub."""
    # Remove everything after the old handle_event stub (or the _wire_branches ending)
    # Find the old stub marker
    stub_marker = '# Event-Handler für board-spezifische Ereignisse (EREIGNIS-Felder)'
    if stub_marker in content:
        idx = content.find(stub_marker)
        # Remove from stub marker to end of file
        content = content[:idx].rstrip()

    # Remove any previously added event system
    event_marker = '# EVENT SYSTEM — Party Arena Milestone 6c'
    while event_marker in content:
        idx = content.find(event_marker)
        # Find the end (look for next section or end of file)
        content = content[:idx].rstrip()

    # Remove any previously added SPECIAL_RULES
    special_marker = '# Abzweigungs-Sonderregeln (Part B, Milestone 6c)'
    while special_marker in content:
        idx = content.find(special_marker)
        content = content[:idx].rstrip()

    # Remove _init_event_system from _ready
    content = content.replace('\t\t_init_event_system()\n', '\n')

    return content


def add_ready_call(content):
    """Add _init_event_system() call to _ready()."""
    # Find _ready function
    marker = 'func _ready() -> void:'
    if marker not in content:
        return content

    idx = content.find(marker)
    # Find the end of _ready's body (next function or end of content)
    next_func = content.find('\nfunc ', idx + len(marker))
    if next_func == -1:
        return content

    ready_body = content[idx:next_func]
    # Check if _init_event_system is already there
    if '_init_event_system()' in ready_body:
        return content

    # Add before the closing of _ready
    # Insert after the last statement in _ready
    # Find _validate_distribution() call
    val_marker = '_validate_distribution()'
    val_idx = content.find(val_marker, idx)
    if val_idx == -1:
        return content

    # Find end of that line
    line_end = content.find('\n', val_idx)
    if line_end == -1:
        return content

    # Insert _init_event_system() after that line
    content = content[:line_end+1] + '\t\t_init_event_system()' + content[line_end:]

    return content


def add_branch_rules(content, board_name):
    """Add rule field to BRANCHES entries if not present."""
    rule_map = {
        'sonnenstrand': {'Korallenriff': '', 'Klippen': ''},
        'zuckerwald': {'Schokoladen-Fluss': 'floss_fahrt', 'Zuckerwatte-Wolken': 'zuckerwatte_bonus_minigame'},
        'wolkenwerk': {'Windkanal': 'windkanal_express', 'Regenbogen-Rutsche': 'regenbogen_gleitfahrt'},
        'frostgipfel': {'Eishöhle': 'eishoehlen_dunkelheit', 'Vereister See': 'eisglaette_rutsch'},
        'dschungeltempel': {'Lianen-Schwung': 'lianen_express', 'Tempel-Inneres': 'tempel_fluch_zone'},
        'mechanik-stadt': {'Rohrpost-Teleport': 'rohrpost_teleport', 'Förderband-Fabrik': 'foerderband_fabrik'},
        'sternenzitadelle': {'Kosmische Drift': 'kosmische_drift', 'Geister-Felder': 'geister_felder'},
    }

    rules = rule_map.get(board_name, {})
    for name, rule in rules.items():
        pattern = f'"name": "{name}"'
        if pattern not in content:
            continue
        if f'"rule":' in content[content.find(pattern):content.find(pattern)+250]:
            continue
        pos = content.find(pattern)
        # Find closing ] of fields array
        fields_pos = content.find('"fields"', pos)
        bracket_pos = content.find(']', fields_pos)
        # Add rule after ]
        content = content[:bracket_pos+1] + f',\n\t\t\t"rule": "{rule}"' + content[bracket_pos+1:]
    return content


def process_board(board_name, events, bound_events, special_rules, event_selection,
                  world_doc, effect_methods, extra_state_vars=('', ''), is_all_bound=False):
    """Process a single board.gd file."""
    filepath = os.path.join(BASE, board_name, 'board.gd')

    with open(filepath, 'r') as f:
        content = f.read()

    # Clean previous modifications
    content = clean_file(content)

    # Add _init_event_system() call
    content = add_ready_call(content)

    # Add branch rules
    content = add_branch_rules(content, board_name)

    # Build event system
    effect_dispatch = build_effect_dispatch(events)
    event_selection_code = build_event_selection(len(bound_events) > 0, is_all_bound)

    event_system = build_event_system(
        events, bound_events, special_rules,
        event_selection_code, effect_dispatch,
        world_doc, effect_methods,
        has_event_init=True
    )

    # Add extra state variables (before the event system)
    extra_vars, extra_init = extra_state_vars
    if extra_vars:
        content = content.rstrip() + '\n\n' + extra_vars

    # Append event system at end of file
    content = content.rstrip() + '\n\n' + event_system + '\n'

    # Append common helpers
    content = content.rstrip() + '\n' + COMMON_HELPERS

    # Remove duplicate blank lines (max 1 consecutive)
    while '\n\n\n' in content:
        content = content.replace('\n\n\n', '\n\n')

    with open(filepath, 'w') as f:
        f.write(content)

    line_count = len(content.split('\n'))
    print(f'  ✓ {board_name}/board.gd written ({line_count} lines)')


# ============================================================
# BOARD DATA
# ============================================================

# Extra state for Frostgipfel (skip_turns for schneesturm)
frost_extra = (
    '\n# Spieler, die die nächste Runde aussetzen (Schneesturm)\nvar _skip_turns: Dictionary = {}\n',
    ''
)

mech_extra = (
    '\n# Spieler, die die nächste Runde aussetzen (Zahnrad-Stau)\nvar _skip_turns: Dictionary = {}\n'
    '\n# Erfindermesse aktiv? (Item-Preise -2 für diese Runde)\nvar _erfindermesse_active: bool = false\n',
    ''
)

stern_extra = (
    '\n# Extra-Zug Spieler-ID (Zeit-Verzerrung)\nvar _extra_turn_player_id: int = -1\n',
    ''
)

# Sonnenstrand (already done manually, but regenerate for consistency)
# Skip - it was hand-written and is correct

# Zuckerwald
process_board('zuckerwald',
    events={
        'klebriger_boden': {'name': 'Klebriger Boden', 'weight': 35},
        'zucker_rausch': {'name': 'Zucker-Rausch', 'weight': 35},
        'keks_regen': {'name': 'Keks-Regen', 'weight': 30},
    },
    bound_events={37: 'klebriger_boden', 38: 'zucker_rausch'},
    special_rules=['floss_fahrt', 'zuckerwatte_bonus_minigame'],
    event_selection='',
    world_doc='design/gdd/world-zuckerwald.md',
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

# Wolkenwerk (all bound)
process_board('wolkenwerk',
    events={
        'turbulenz': {'name': 'Turbulenz', 'weight': 0},
        'aufwind': {'name': 'Aufwind', 'weight': 0},
        'regenbogen_schatz': {'name': 'Regenbogen-Schatz', 'weight': 0},
        'nebelbank': {'name': 'Nebelbank', 'weight': 0},
        'windstoss': {'name': 'Windstoß', 'weight': 0},
    },
    bound_events={4: 'turbulenz', 12: 'aufwind', 20: 'regenbogen_schatz', 30: 'nebelbank', 36: 'windstoss'},
    special_rules=['windkanal_express', 'regenbogen_gleitfahrt'],
    event_selection='',
    world_doc='design/gdd/world-wolkenwerk.md',
    is_all_bound=True,
    effect_methods='''## Turbulenz: Alle Spieler tauschen zufällig ihre Positionen (Permutation ohne Fixpunkt).
func _ev_turbulenz(_player: Node3D, ctrl: Controller) -> void:
\tif ctrl.players.size() < 2:
\t\treturn

\tif ctrl.players.size() == 2:
\t\tvar pos0: NodeBoard = ctrl.players[0].space
\t\tvar pos1: NodeBoard = ctrl.players[1].space
\t\tctrl.players[0].teleport_to(pos1)
\t\tctrl.players[1].teleport_to(pos0)
\t\tawait ctrl.get_tree().create_timer(0.3).timeout
\t\treturn

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

\t# Korrigiere Fixpunkte (Tausch mit Nachbar)
\tfor i in range(shuffled.size()):
\t\tif shuffled[i] == positions[i]:
\t\t\tvar swap_idx: int = (i + 1) % shuffled.size()
\t\t\tvar tmp2: NodeBoard = shuffled[i]
\t\t\tshuffled[i] = shuffled[swap_idx]
\t\t\tshuffled[swap_idx] = tmp2

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
process_board('frostgipfel',
    events={
        'schneesturm': {'name': 'Schneesturm', 'weight': 30},
        'nordlicht': {'name': 'Nordlicht', 'weight': 40},
        'eiskristall_regen': {'name': 'Eiskristall-Regen', 'weight': 30},
    },
    bound_events={35: 'schneesturm', 37: 'eisglaette', 25: 'nordlicht'},
    special_rules=['eishoehlen_dunkelheit', 'eisglaette_rutsch'],
    event_selection='',
    world_doc='design/gdd/world-frostgipfel.md',
    extra_state_vars=frost_extra,
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

\t# W6/2 aufgerundet -> 1-3 Felder
\tvar distance: int = ceili(float(randi() % 6 + 1) / 2.0)
\tvar forward: bool = randi() % 2 == 0

\tif forward:
\t\tawait _move_player_forward(p_active, distance, ctrl)
\telse:
\t\tawait _move_player_backward(p_active, distance, ctrl)''',
)

# Dschungeltempel
process_board('dschungeltempel',
    events={
        'goldrausch': {'name': 'Goldrausch', 'weight': 35},
        'lianen_segen': {'name': 'Lianen-Segen', 'weight': 30},
        'fluch_des_tempels': {'name': 'Fluch des Tempels', 'weight': 35},
    },
    bound_events={38: 'fluch_des_tempels'},
    special_rules=['lianen_express', 'tempel_fluch_zone'],
    event_selection='',
    world_doc='design/gdd/world-dschungeltempel.md',
    effect_methods='''## Goldrausch: Ärmster Spieler erhält +8 Münzen (Catch-up).
func _ev_goldrausch(_player: Node3D, ctrl: Controller) -> void:
\t# Finde den Spieler mit den wenigsten Münzen (primär Sterne, sekundär Münzen)
\tvar min_rank: int = 999999
\tfor p: PlayerBoard in ctrl.players:
\t\tvar rank_val: int = p.stars * 1000 + p.cookies
\t\tif rank_val < min_rank:
\t\t\tmin_rank = rank_val

\tfor p: PlayerBoard in ctrl.players:
\t\tvar rank_val: int = p.stars * 1000 + p.cookies
\t\tif rank_val == min_rank:
\t\t\tp.cookies += 8


## Lianen-Segen: Aktiver Spieler +5 Münzen und 2 Felder vorwärts.
func _ev_lianen_segen(player: Node3D, ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard
\tif p_active:
\t\tp_active.cookies += 5
\t\tawait _move_player_forward(p_active, 2, ctrl)


## Fluch des Tempels: Ungebunden -> reichster Spieler -5 Münzen.
## Gebunden (Feld 38) -> aktiver Spieler -5 Münzen.
func _ev_fluch_des_tempels(player: Node3D, ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard
\tif not p_active:
\t\treturn

\t# Prüfe ob gebunden (Feld 38 im Tempel-Inneren)
\tvar field_num: int = _get_field_number(p_active.space)
\tvar is_bound: bool = BOUND_EVENTS.has(field_num) and BOUND_EVENTS[field_num] == "fluch_des_tempels"

\tif is_bound:
\t\tp_active.cookies = max(0, p_active.cookies - 5)
\telse:
\t\tvar richest: PlayerBoard = _get_richest_player(ctrl)
\t\tif richest:
\t\t\trichest.cookies = max(0, richest.cookies - 5)''',
)

# Mechanik-Stadt
process_board('mechanik-stadt',
    events={
        'erfindermesse': {'name': 'Erfindermesse', 'weight': 25},
        'zahnrad_stau': {'name': 'Zahnrad-Stau', 'weight': 35},
        'dampf_explosion': {'name': 'Dampf-Explosion', 'weight': 40},
    },
    bound_events={37: 'zahnrad_stau'},
    special_rules=['rohrpost_teleport', 'foerderband_fabrik'],
    event_selection='',
    world_doc='design/gdd/world-mechanik-stadt.md',
    extra_state_vars=mech_extra,
    effect_methods='''## Erfindermesse: Alle Item-Preise -2 für den Rest der Runde.
func _ev_erfindermesse(_player: Node3D, _ctrl: Controller) -> void:
\t_erfindermesse_active = true


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
\t# Nur Hauptpfad-Felder (Indizes 0-31, Felder 1-32)
\tvar main_path: Array[NodeBoard] = []
\tfor i in range(min(32, sorted.size())):
\t\tmain_path.append(sorted[i])

\tif main_path.size() < 2:
\t\treturn

\t# Zufällige Zielfelder (ohne Zurücklegen)
\tvar available: Array[NodeBoard] = main_path.duplicate()
\tfor p: PlayerBoard in ctrl.players:
\t\tif available.size() == 0:
\t\t\tavailable = main_path.duplicate()
\t\tvar idx: int = randi() % available.size()
\t\tp.teleport_to(available[idx])
\t\tavailable.remove_at(idx)

\tawait ctrl.get_tree().create_timer(0.5).timeout''',
)

# Sternenzitadelle
process_board('sternenzitadelle',
    events={
        'sternen_regen': {'name': 'Sternen-Regen', 'weight': 25},
        'zeit_verzerrung': {'name': 'Zeit-Verzerrung', 'weight': 25},
        'schwarzes_loch': {'name': 'Schwarzes Loch', 'weight': 25},
        'arenastars_segen': {'name': 'ArenaStars Segen', 'weight': 25},
    },
    bound_events={36: 'zeit_verzerrung', 38: 'schwarzes_loch'},
    special_rules=['kosmische_drift', 'geister_felder'],
    event_selection='',
    world_doc='design/gdd/world-sternenzitadelle.md',
    extra_state_vars=stern_extra,
    effect_methods='''## Sternen-Regen: Alle +5 Münzen, aktiver Spieler +3 extra (insgesamt +8).
func _ev_sternen_regen(player: Node3D, ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard
\tfor p: PlayerBoard in ctrl.players:
\t\tp.cookies += 5
\tif p_active:
\t\tp_active.cookies += 3


## Zeit-Verzerrung: Aktiver Spieler erhält Extra-Zug (Flag für Controller).
func _ev_zeit_verzerrung(player: Node3D, _ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard
\tif p_active:
\t\t_extra_turn_player_id = p_active.info.player_id


## Schwarzes Loch: Aktiver + 1 zufälliger Spieler verlieren je 1 zufälliges Item.
func _ev_schwarzes_loch(player: Node3D, ctrl: Controller) -> void:
\tvar p_active: PlayerBoard = player as PlayerBoard

\tvar targets: Array[PlayerBoard] = []
\tif p_active and p_active.items.size() > 0:
\t\ttargets.append(p_active)

\tvar others: Array[PlayerBoard] = _get_other_players(ctrl, p_active)
\tif others.size() > 0:
\t\tvar other: PlayerBoard = others[randi() % others.size()]
\t\tif other.items.size() > 0:
\t\t\ttargets.append(other)

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
print('Done! All 6 board.gd files regenerated.')
