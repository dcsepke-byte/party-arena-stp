#!/usr/bin/env python3
"""Generate the 7 island boards for Party Arena Milestone 6."""

import os
import json

BOARDS_DIR = "/opt/data/SuperTuxParty/plugins/boards"

# Field distributions from world-overview.md Table 3.8
# Format: (stern_shops, ereignis, minispiel)
# START=1, ITEM_SHOP=2, GLUECK_PECH=3, MUENZ_BONUS=4 are fixed
ISLANDS = {
    "sonnenstrand": {
        "name_de": "Sonnenstrand",
        "theme": "Urlaub & Wasser",
        "difficulty": 1,
        "colors": ["#00f0ff", "#f4d58d", "#ff6b6b"],
        "music": {"style": "Steel Drums, Ukulele", "bpm": 110, "scale": "Dur"},
        "field_distribution": {"START": 1, "STERN_SHOP": 3, "ITEM_SHOP": 2, "EREIGNIS": 6, "GLUECK_PECH": 3, "MUENZ_BONUS": 4, "MINISPIEL": 21},
        "item_price_tier": 0,
        "intro_duration": 5,
        "branches": [
            {"name": "Korallenriff", "entry": 16, "exit": 20, "delta": 1, "fields": [33, 34, 35, 36]},
            {"name": "Klippen", "entry": 26, "exit": 32, "delta": -1, "fields": [37, 38, 39, 40]},
        ],
        "event_pool": ["springflut", "muschel_suche", "quallen_schwarm"],
        "milestones": [20, 30],
        "special_rules": [],
    },
    "zuckerwald": {
        "name_de": "Zuckerwald",
        "theme": "Süßigkeiten",
        "difficulty": 2,
        "colors": ["#ff4d6d", "#8b4513", "#98ff98"],
        "music": {"style": "Glockenspiel, Fagott", "bpm": 120, "scale": "Dur"},
        "field_distribution": {"START": 1, "STERN_SHOP": 3, "ITEM_SHOP": 2, "EREIGNIS": 5, "GLUECK_PECH": 3, "MUENZ_BONUS": 4, "MINISPIEL": 22},
        "item_price_tier": 0,
        "intro_duration": 5,
        "branches": [
            {"name": "Schokoladen-Fluss", "entry": 16, "exit": 20, "delta": 1, "fields": [33, 34, 35, 36]},
            {"name": "Zuckerwatte-Wolken", "entry": 25, "exit": 32, "delta": -2, "fields": [37, 38, 39, 40]},
        ],
        "event_pool": ["klebriger_boden", "zucker_rausch", "keks_regen"],
        "milestones": [15, 25],
        "special_rules": ["floss_fahrt", "zuckerwatte_bonus_minigame"],
    },
    "wolkenwerk": {
        "name_de": "Wolkenwerk",
        "theme": "Schwebende Himmel",
        "difficulty": 3,
        "colors": ["#87ceeb", "#ffffff", "regenbogen"],
        "music": {"style": "Harfe, Flöte", "bpm": 100, "scale": "Lydisch"},
        "field_distribution": {"START": 1, "STERN_SHOP": 3, "ITEM_SHOP": 2, "EREIGNIS": 6, "GLUECK_PECH": 3, "MUENZ_BONUS": 4, "MINISPIEL": 21},
        "item_price_tier": 1,
        "intro_duration": 5,
        "branches": [
            {"name": "Windkanal", "entry": 9, "exit": 13, "delta": -3, "fields": [10, 11, 12, 13]},
            {"name": "Regenbogen-Rutsche", "entry": 21, "exit": 25, "delta": 2, "fields": [22, 23, 24]},
        ],
        "event_pool": ["turbulenz", "aufwind", "regenbogen_schatz", "windstoss"],
        "milestones": [15, 27],
        "special_rules": ["windkanal_express", "regenbogen_gleitfahrt"],
    },
    "frostgipfel": {
        "name_de": "Frostgipfel",
        "theme": "Eis & Schnee",
        "difficulty": 3,
        "colors": ["#a8d8ea", "#f0f0f0", "#9b59b6"],
        "music": {"style": "Celesta, Tremolo-Strings", "bpm": 90, "scale": "Moll"},
        "field_distribution": {"START": 1, "STERN_SHOP": 3, "ITEM_SHOP": 2, "EREIGNIS": 5, "GLUECK_PECH": 3, "MUENZ_BONUS": 4, "MINISPIEL": 22},
        "item_price_tier": 1,
        "intro_duration": 5,
        "branches": [
            {"name": "Eishöhle", "entry": 11, "exit": 17, "delta": -1, "fields": [33, 34, 35, 36]},
            {"name": "Vereister See", "entry": 25, "exit": 30, "delta": 0, "fields": [37, 38, 39, 40]},
        ],
        "event_pool": ["schneesturm", "eisglaette", "nordlicht"],
        "milestones": [11, 30],
        "special_rules": ["eishoehlen_dunkelheit", "eisglaette_rutsch"],
    },
    "dschungeltempel": {
        "name_de": "Dschungeltempel",
        "theme": "Ruinen & Abenteuer",
        "difficulty": 4,
        "colors": ["#2d6a4f", "#ffd700", "#8b4513"],
        "music": {"style": "Marimba, Bongos", "bpm": 130, "scale": "Phrygisch"},
        "field_distribution": {"START": 1, "STERN_SHOP": 3, "ITEM_SHOP": 2, "EREIGNIS": 6, "GLUECK_PECH": 3, "MUENZ_BONUS": 4, "MINISPIEL": 21},
        "item_price_tier": 2,
        "intro_duration": 5,
        "branches": [
            {"name": "Lianen-Schwung", "entry": 15, "exit": 18, "delta": 2, "fields": [33, 34, 35, 36]},
            {"name": "Tempel-Inneres", "entry": 22, "exit": 30, "delta": -3, "fields": [37, 38, 39, 40]},
        ],
        "event_pool": ["fluch_des_tempels", "goldrausch", "lianen_schwung"],
        "milestones": [11, 26],
        "special_rules": ["lianen_express", "tempel_fluch_zone"],
    },
    "mechanik-stadt": {
        "name_de": "Mechanik-Stadt",
        "theme": "Spielzeug-Technik",
        "difficulty": 4,
        "colors": ["#c0c0c0", "#ff6a00", "#ffd34e"],
        "music": {"style": "Marimba/Xylophon, Tuba", "bpm": 140, "scale": "Mixolydisch"},
        "field_distribution": {"START": 1, "STERN_SHOP": 3, "ITEM_SHOP": 2, "EREIGNIS": 6, "GLUECK_PECH": 3, "MUENZ_BONUS": 4, "MINISPIEL": 21},
        "item_price_tier": 2,
        "intro_duration": 5,
        "branches": [
            {"name": "Rohrpost-Teleport", "entry": 13, "exit": 17, "delta": 1, "fields": [33, 34, 35, 36]},
            {"name": "Förderband-Fabrik", "entry": 24, "exit": 30, "delta": -1, "fields": [37, 38, 39, 40]},
        ],
        "event_pool": ["zahnrad_stau", "erfindermesse", "dampf_explosion"],
        "milestones": [19, 31],
        "special_rules": ["rohrpost_teleport", "foerderband_fabrik"],
    },
    "sternenzitadelle": {
        "name_de": "Sternenzitadelle",
        "theme": "Kosmisch & Finale",
        "difficulty": 5,
        "colors": ["#ffd700", "#1a1a4e", "#ff00ff"],
        "music": {"style": "Volle Orchester, Chor", "bpm": "80-160", "scale": "heroisch"},
        "field_distribution": {"START": 1, "STERN_SHOP": 4, "ITEM_SHOP": 2, "EREIGNIS": 6, "GLUECK_PECH": 3, "MUENZ_BONUS": 4, "MINISPIEL": 20},
        "item_price_tier": 3,
        "intro_duration": 7,
        "branches": [
            {"name": "Kosmische Drift", "entry": 12, "exit": 17, "delta": -1, "fields": [33, 34, 35, 36]},
            {"name": "Geister-Felder", "entry": 22, "exit": 27, "delta": -1, "fields": [37, 38, 39, 40]},
        ],
        "event_pool": ["sternen_regen", "zeit_verzerrung", "arenastars_segen", "schwarzes_loch"],
        "milestones": [15, 26],
        "special_rules": ["kosmische_drift", "geister_felder"],
    },
}

# GDD field layouts for each island (Feld -> Typ mapping)
# From each world-*.md Section 3.1
# 0=START, 1=STERN_SHOP, 2=ITEM_SHOP, 3=EREIGNIS, 4=GLUECK_PECH, 5=MUENZ_BONUS, 6=MINISPIEL
ISLAND_FIELD_LAYOUTS = {
    "sonnenstrand": {
        1:0, 2:6, 3:5, 4:6, 5:6, 6:4, 7:6, 8:2, 9:6, 10:6,
        11:6, 12:1, 13:6, 14:5, 15:6, 16:3, 17:6, 18:4, 19:5, 20:6,
        21:3, 22:6, 23:6, 24:1, 25:6, 26:3, 27:6, 28:2, 29:6, 30:6,
        31:6, 32:6,
        33:4, 34:5, 35:3, 36:1,
        37:3, 38:3, 39:6, 40:6,
    },
    "zuckerwald": {
        1:0, 2:6, 3:5, 4:6, 5:6, 6:2, 7:6, 8:4, 9:6, 10:1,
        11:6, 12:5, 13:6, 14:6, 15:6, 16:6, 17:6, 18:6, 19:5, 20:6,
        21:3, 22:1, 23:6, 24:4, 25:6, 26:3, 27:6, 28:6, 29:3, 30:2,
        31:6, 32:6,
        33:6, 34:1, 35:4, 36:5,
        37:3, 38:3, 39:6, 40:6,
    },
    "wolkenwerk": {
        0:0, 1:6, 2:6, 3:5, 4:3, 5:6, 6:6, 7:4, 8:3, 9:2,
        10:6, 11:6, 12:3, 13:6, 14:1, 15:6, 16:5, 17:6, 18:4, 19:6,
        20:3, 21:6, 22:6, 23:6, 24:6, 25:2, 26:5, 27:6, 28:1, 29:6,
        30:3, 31:6, 32:4, 33:6, 34:6, 35:5, 36:3, 37:6, 38:1, 39:6,
    },
    "frostgipfel": {
        1:0, 2:6, 3:5, 4:6, 5:6, 6:4, 7:6, 8:6, 9:6, 10:1,
        11:6, 12:2, 13:6, 14:6, 15:5, 16:6, 17:6, 18:3, 19:6, 20:1,
        21:6, 22:4, 23:6, 24:6, 25:3, 26:6, 27:6, 28:2, 29:6, 30:6,
        31:3, 32:6,
        33:6, 34:4, 35:3, 36:1,
        37:3, 38:5, 39:6, 40:5,
    },
    "dschungeltempel": {
        1:0, 2:6, 3:5, 4:6, 5:6, 6:3, 7:4, 8:6, 9:6, 10:1,
        11:6, 12:2, 13:6, 14:6, 15:3, 16:5, 17:6, 18:6, 19:1, 20:6,
        21:3, 22:3, 23:6, 24:6, 25:4, 26:6, 27:3, 28:2, 29:6, 30:6,
        31:6, 32:6,
        33:4, 34:6, 35:6, 36:5,
        37:1, 38:3, 39:6, 40:5,
    },
    "mechanik-stadt": {
        1:0, 2:6, 3:5, 4:6, 5:6, 6:3, 7:4, 8:2, 9:6, 10:6,
        11:1, 12:6, 13:3, 14:6, 15:5, 16:6, 17:6, 18:1, 19:6, 20:4,
        21:3, 22:3, 23:6, 24:6, 25:3, 26:2, 27:5, 28:6, 29:6, 30:4,
        31:6, 32:6,
        33:6, 34:5, 35:6, 36:1,
        37:3, 38:6, 39:6, 40:6,
    },
    "sternenzitadelle": {
        1:0, 2:6, 3:5, 4:6, 5:3, 6:6, 7:2, 8:3, 9:6, 10:1,
        11:6, 12:3, 13:6, 14:4, 15:6, 16:5, 17:6, 18:1, 19:6, 20:6,
        21:6, 22:3, 23:6, 24:6, 25:2, 26:6, 27:6, 28:4, 29:5, 30:1,
        31:6, 32:6,
        33:4, 34:6, 35:1, 36:3,
        37:5, 38:3, 39:6, 40:6,
    },
}

# Read the test board TSCN as template
def read_template():
    with open(os.path.join(BOARDS_DIR, "test", "board.tscn"), "r") as f:
        return f.read()

def generate_board_gd(island_id, island_data):
    """Generate board.gd for an island."""
    layout = ISLAND_FIELD_LAYOUTS[island_id]
    # Build the REFERENCE_LAYOUT array
    max_fields = max(layout.keys())
    layout_lines = []
    for i in range(1, max_fields + 1):
        if i in layout:
            typ = layout[i]
        else:
            typ = 6  # Default to MINISPIEL

    dist = island_data["field_distribution"]

    # Build layout array lines
    layout_lines = []
    # Determine if this island uses 0-based or 1-based indexing
    if 0 in layout:
        # 0-based (Wolkenwerk)
        for i in range(max_fields + 1):
            typ = layout.get(i, 6)
            type_name = {0: "START", 1: "STERN_SHOP", 2: "ITEM_SHOP", 3: "EREIGNIS",
                        4: "GLUECK_PECH", 5: "MUENZ_BONUS", 6: "MINISPIEL"}[typ]
            layout_lines.append(f"\t\tNodeBoard.FELD_TYP.{type_name},  # {i}")
    else:
        # 1-based
        for i in range(1, max_fields + 1):
            typ = layout.get(i, 6)
            type_name = {0: "START", 1: "STERN_SHOP", 2: "ITEM_SHOP", 3: "EREIGNIS",
                        4: "GLUECK_PECH", 5: "MUENZ_BONUS", 6: "MINISPIEL"}[typ]
            layout_lines.append(f"\t\tNodeBoard.FELD_TYP.{type_name},  # {i}")

    layout_str = ",\n".join(layout_lines)

    gd_content = f'''extends Node3D

# Party Arena: {island_data["name_de"]}-Board
# Schwierigkeit: {"★" * island_data["difficulty"]}{"☆" * (5 - island_data["difficulty"])}
# Game Bible: design/gdd/world-{island_id.replace("_", "-") if "_" in island_id else island_id}.md

# Referenz-Layout (40 Felder) gemäß Game Bible Tabelle 3.8 + Insel-Kapitel 3.1
const REFERENCE_LAYOUT: Array[int] = [
{layout_str}
]

# Erwartete Verteilung (Game Bible world-overview.md 3.8)
const EXPECTED_DISTRIBUTION := {{
	NodeBoard.FELD_TYP.START: {dist["START"]},
	NodeBoard.FELD_TYP.STERN_SHOP: {dist["STERN_SHOP"]},
	NodeBoard.FELD_TYP.ITEM_SHOP: {dist["ITEM_SHOP"]},
	NodeBoard.FELD_TYP.EREIGNIS: {dist["EREIGNIS"]},
	NodeBoard.FELD_TYP.GLUECK_PECH: {dist["GLUECK_PECH"]},
	NodeBoard.FELD_TYP.MUENZ_BONUS: {dist["MUENZ_BONUS"]},
	NodeBoard.FELD_TYP.MINISPIEL: {dist["MINISPIEL"]},
}}

# Feldtyp-Namen für Debugging
const FELD_TYP_NAMES := {{
	NodeBoard.FELD_TYP.START: "START",
	NodeBoard.FELD_TYP.STERN_SHOP: "STERN_SHOP",
	NodeBoard.FELD_TYP.ITEM_SHOP: "ITEM_SHOP",
	NodeBoard.FELD_TYP.EREIGNIS: "EREIGNIS",
	NodeBoard.FELD_TYP.GLUECK_PECH: "GLUECK_PECH",
	NodeBoard.FELD_TYP.MUENZ_BONUS: "MUENZ_BONUS",
	NodeBoard.FELD_TYP.MINISPIEL: "MINISPIEL",
}}

# Insel-Metadaten
var board_id: String = "{island_id}"
var board_name: String = "{island_data['name_de']}"
var difficulty: int = {island_data['difficulty']}
var item_price_tier: int = {island_data['item_price_tier']}


func _ready() -> void:
	_apply_reference_layout()
	_validate_distribution()


## Wendet die Feldtypen des Referenz-Layouts auf die vorhandenen
## NodeBoard-Knoten an (nach Namen sortiert: Node1, Node2, ...).
func _apply_reference_layout() -> void:
	if not has_node("Nodes"):
		push_error("{island_id} board: 'Nodes' container not found!")
		return

	var nodes_container := $Nodes
	var node_boards: Array[Node] = []

	for child in nodes_container.get_children():
		if child is NodeBoard:
			node_boards.append(child)

	if node_boards.is_empty():
		push_error("{island_id} board: No NodeBoard instances found!")
		return

	node_boards.sort_custom(func(a, b): return a.name.naturalnocase_to(b.name) < 0)

	for i in range(min(node_boards.size(), REFERENCE_LAYOUT.size())):
		var node: NodeBoard = node_boards[i]
		node.type = REFERENCE_LAYOUT[i]

	for i in range(REFERENCE_LAYOUT.size(), node_boards.size()):
		var node: NodeBoard = node_boards[i]
		node._visible = false

	print("{island_id} board: Applied reference layout to %d nodes (%d hidden)" %
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
		print("{island_id} board: Field distribution VALID (all %d types match Game Bible 3.8)" %
				EXPECTED_DISTRIBUTION.size())
	else:
		push_error("{island_id} board: Field distribution INVALID — see warnings above")


## Gibt die aktuelle Feld-Verteilung als Dictionary zurück.
func get_field_distribution() -> Dictionary:
	var counts := {{}}
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
	return "\\n".join(lines)


# Event-Handler für board-spezifische Ereignisse (EREIGNIS-Felder)
func handle_event(player: Node3D, space: Node3D):
	# Platzhalter: Insel-spezifische Ereignis-Logik folgt
	# in einem späteren Milestone (Board-Events & Effekte)
	await get_tree().process_frame
	if has_node("Controller"):
		$Controller.board_continue()
'''
    return gd_content


def generate_board_json(island_id, island_data):
    """Generate board.json for an island."""
    return json.dumps(island_data, indent=2, ensure_ascii=False) + "\n"


def generate_board_tscn(island_id, island_data):
    """Generate a minimal board.tscn for an island.

    Uses the test board layout as a base, referencing the island's board.gd.
    We create a simplified circular layout with 50 nodes (40 active + buffer)
    to match the test board structure.
    """
    import math

    name_de = island_data["name_de"]
    colors = island_data["colors"]

    # Use fixed UIDs for external resources (these exist in the project)
    node_scene_uid = "uid://dw3dff20fschf"  # node.tscn
    player_scene_uid = "uid://wtj7iedl45l7"  # player_board.tscn
    controller_scene_uid = "uid://dcyoe2uryyyef"  # controller.tscn

    # Build TSCN content
    lines = []
    # Use a unique uid for this board scene
    lines.append(f'[gd_scene load_steps=5 format=3 uid="uid://{island_id}board000"]')
    lines.append('')
    lines.append(f'[ext_resource type="Script" path="res://plugins/boards/{island_id}/board.gd" id="1"]')
    lines.append(f'[ext_resource type="PackedScene" uid="{player_scene_uid}" path="res://common/scenes/board_logic/player_board/player_board.tscn" id="2"]')
    lines.append(f'[ext_resource type="PackedScene" uid="{controller_scene_uid}" path="res://common/scenes/board_logic/controller/controller.tscn" id="3"]')
    lines.append(f'[ext_resource type="PackedScene" uid="{node_scene_uid}" path="res://common/scenes/board_logic/node/node.tscn" id="4"]')
    lines.append('')

    # Root node
    lines.append(f'[node name="Board" type="Node3D"]')
    lines.append(f'script = ExtResource("1")')
    lines.append('')

    # Players (4, using test board positions)
    for p in range(1, 5):
        positions = {
            1: (0, 0.25, -0.75),
            2: (0.75, 0.25, 0),
            3: (0, 0.25, 0.75),
            4: (-0.75, 0.25, 0),
        }
        x, y, z = positions[p]
        lines.append(f'[node name="Player{p}" parent="." instance=ExtResource("2")]')
        lines.append(f'transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, {x}, {y}, {z})')
        lines.append('')

    # Controller
    lines.append('[node name="Controller" parent="." instance=ExtResource("3")]')
    lines.append('COOKIES_FOR_CAKE = 20')
    lines.append('start_node = NodePath("../Nodes/Node1")')
    lines.append('')

    # Sun light
    lines.append('[node name="Sun" type="DirectionalLight3D" parent="."]')
    lines.append('transform = Transform3D(0.642788, 0.627507, -0.439385, 0, 0.573576, 0.819152, 0.766044, -0.526541, 0.368688, -6, 4, 3)')
    lines.append('light_energy = 0.75')
    lines.append('shadow_enabled = true')
    lines.append('')

    # Nodes container
    lines.append('[node name="Nodes" type="Node3D" parent="."]')
    lines.append('')

    # Generate 50 NodeBoard instances (like test board, we create extra)
    # Arrange in a circular pattern
    radius = 15.0
    for i in range(1, 51):
        # Calculate circle position for first 40 nodes
        if i <= 40:
            angle = (i - 1) * 2 * math.pi / 40 - math.pi / 2
            x = radius * math.cos(angle)
            z = radius * math.sin(angle)
        elif i <= 44:
            # Branch A (nodes 41-44): inner path
            angle = (i - 5) * 2 * math.pi / 40 - math.pi / 2
            x = (radius * 0.7) * math.cos(angle + 0.3)
            z = (radius * 0.7) * math.sin(angle + 0.3)
        else:
            # Branch B (nodes 45-50): offset
            angle = (i - 15) * 2 * math.pi / 40 - math.pi / 2
            x = (radius * 0.7) * math.cos(angle - 0.3)
            z = (radius * 0.7) * math.sin(angle - 0.3)

        y = 0.0
        lines.append(f'[node name="Node{i}" parent="Nodes" instance=ExtResource("4")]')
        lines.append(f'transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, {x:.4f}, {y:.4f}, {z:.4f})')

        # Set next/prev for basic loop topology
        if i <= 40:
            if i < 40:
                lines.append(f'next = Array[NodePath]([NodePath("../Node{i+1}")])')
            else:
                lines.append(f'next = Array[NodePath]([NodePath("../Node1")])')

            if i > 1:
                lines.append(f'prev = Array[NodePath]([NodePath("../Node{i-1}")])')
            else:
                lines.append(f'prev = Array[NodePath]([NodePath("../Node40")])')

        lines.append('amount_of_items_sold = 4')
        lines.append('')

    # Add connection signal
    lines.append('[connection signal="trigger_event" from="Controller" to="." method="handle_event"]')
    lines.append('')

    return '\n'.join(lines)


def main():
    for island_id, island_data in ISLANDS.items():
        board_dir = os.path.join(BOARDS_DIR, island_id)
        os.makedirs(board_dir, exist_ok=True)

        # Generate board.gd
        gd_path = os.path.join(board_dir, "board.gd")
        with open(gd_path, "w") as f:
            f.write(generate_board_gd(island_id, island_data))
        print(f"Created {gd_path}")

        # Generate board.json
        json_path = os.path.join(board_dir, "board.json")
        with open(json_path, "w") as f:
            f.write(generate_board_json(island_id, island_data))
        print(f"Created {json_path}")

        # Generate board.tscn
        tscn_path = os.path.join(board_dir, "board.tscn")
        with open(tscn_path, "w") as f:
            f.write(generate_board_tscn(island_id, island_data))
        print(f"Created {tscn_path}")

        print(f"  -> {island_data['name_de']}: {island_data['field_distribution']}")
        total = sum(island_data['field_distribution'].values())
        print(f"  -> Total fields: {total} (expected: 40)")


if __name__ == "__main__":
    main()
