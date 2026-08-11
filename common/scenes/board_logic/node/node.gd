@tool
extends Node3D
class_name NodeBoard

# Party Arena: Feldtypen-System (ersetzt STP NODE_TYPES)
# Game Bible: design/gdd/board-architecture.md, Sektion 3.1
enum FELD_TYP {
	START,
	STERN_SHOP,
	ITEM_SHOP,
	EREIGNIS,
	GLUECK_PECH,
	MUENZ_BONUS,
	MINISPIEL
}

@export var _visible: bool = true: set = set_hidden
# The setter and getter for this variables ensure that the changes are
# immediately visible to the editor.
@export var type: FELD_TYP = FELD_TYP.MINISPIEL: set = set_type
@export var potential_star := false: set = set_star

@export var next: Array[NodePath]:
	set(x):
		var new_elements := x.filter(func(q): return not q in next)
		var removed_elements := next.filter(func(q): return not q in x)
		next = x
		if not is_inside_tree():
			return
		for n in new_elements:
			if n.is_empty():
				continue
			var node := get_node(n)
			node.prev.append(node.get_path_to(self))
		for n in removed_elements:
			if n.is_empty():
				continue
			var node := get_node(n)
			node.prev.erase(node.get_path_to(self))
		update_configuration_warnings()
@export var prev: Array[NodePath]:
	set(x):
		var new_elements := x.filter(func(q): return not q in prev)
		var removed_elements := prev.filter(func(q): return not q in x)
		prev = x
		if not is_inside_tree():
			return
		for n in new_elements:
			if n.is_empty():
				continue
			var node := get_node(n)
			node.next.append(node.get_path_to(self))
		for n in removed_elements:
			if n.is_empty():
				continue
			var node := get_node(n)
			node.next.erase(node.get_path_to(self))
		update_configuration_warnings()

# Settings for shop node.
const MAX_STORE_SIZE = 6

# "const" properties are not valid in export declarations, therefore the
# content MAX_STORE_SIZE is repeated as upper bound here.
@export var amount_of_items_sold := 8
@export var custom_items: Array[String] = []

var star_active := false: set = set_active_star

# An item that was placed onto this node.
var trap: Item: set = set_trap
var trap_player = null

# Radius of a node, used for drawing arrows in the editor.
const NODE_RADIUS = 1

func set_hidden(v: bool):
	_visible = v
	$Model.visible = v

func is_visible_space() -> bool:
	return _visible

func _ready() -> void:
	set_material()

	if Engine.is_editor_hint():
		set_process(true)

		# Search for a previous node if not present (autoconnect).
		# Attaches to the previous node in the scene order, if it is the first,
		# it has no effect.
		if prev.is_empty():
			var nodes: Array = get_tree().get_nodes_in_group("nodes")

			var pos: int = nodes.find(self)
			if pos > 0:
				assert (nodes[pos - 1] != null)
				nodes[pos - 1].next.append(nodes[pos - 1].get_path_to(self))
				prev.append(get_path_to(nodes[pos - 1]))
	else:
		$EditorLines.queue_free()
		# Only the node model should be rotated/scaled.
		# Because it's an instanced scene, only modifications to the root model
		# are saved.
		# Therefore we can't just forward the transformation in the editor.
		# That's why we do it here.
		$Model.transform.basis = self.transform.basis * $Model.transform.basis
		self.transform.basis = Basis()

# Updates the changes in the editor when potential_star is changed
func set_star(enabled: bool) -> void:
	potential_star = enabled

	if potential_star:
		if Engine.is_editor_hint() and has_node("Star"):
			$Star.show()
	else:
		if Engine.is_editor_hint() and has_node("Star"):
			$Star.hide()

func play_star_collection_animation():
	$Star/AnimationPlayer.play("collect")
	await $Star/AnimationPlayer.animation_finished

# Sets whether this node is the currently active star statue spot
func set_active_star(enabled: bool) -> void:
	star_active = enabled
	if star_active:
		$Star.show()
		$Star/AnimationPlayer.play_backwards("collect")
		$Star/AnimationPlayer.queue("float")
	else:
		$Star.hide()

# Updates the visual changes in the editor when the type is being changed.
func set_type(t) -> void:
	if t != null:
		type = t

	# Check if it has already been added to the tree to prevent errors from
	# flooding the console when opening it in the editor.
	if has_node("Model/Cylinder"):
		set_material()

func set_trap(item: Item) -> void:
	trap = item

	set_material()

	if item == null:
		remove_from_group("trap")
	else:
		add_to_group("trap")

# Helper function to update the material based on the node-type.
func set_material() -> void:
	if trap != null:
		$Model/Cylinder.set_surface_override_material(0, trap.material)
		return

	match type:
		FELD_TYP.START:
			$Model/Cylinder.set_surface_override_material(0, preload(
					"res://common/scenes/board_logic/node/material/" +
					"node_green_material.tres"))
		FELD_TYP.STERN_SHOP:
			$Model/Cylinder.set_surface_override_material(0, preload(
					"res://common/scenes/board_logic/node/material/" +
					"node_purple_material.tres"))
		FELD_TYP.ITEM_SHOP:
			$Model/Cylinder.set_surface_override_material(0, preload(
					"res://common/scenes/board_logic/node/material/" +
					"node_purple_material.tres"))
		FELD_TYP.EREIGNIS:
			$Model/Cylinder.set_surface_override_material(0, preload(
					"res://common/scenes/board_logic/node/material/" +
					"node_red_material.tres"))
		FELD_TYP.GLUECK_PECH:
			$Model/Cylinder.set_surface_override_material(0, preload(
					"res://common/scenes/board_logic/node/material/" +
					"node_yellow_material.tres"))
		FELD_TYP.MUENZ_BONUS:
			$Model/Cylinder.set_surface_override_material(0, preload(
					"res://common/scenes/board_logic/node/material/" +
					"node_blue_material.tres"))
		FELD_TYP.MINISPIEL:
			$Model/Cylinder.set_surface_override_material(0, preload(
					"res://common/scenes/board_logic/node/material/" +
					"node_blue_material.tres"))

func _enter_tree() -> void:
	set_material()

	if potential_star:
		if Engine.is_editor_hint() == true:
			$Star.show()
		else:
			add_to_group("star_nodes")
	elif not Engine.is_editor_hint():
		$Star.queue_free()
		$EditorLines.queue_free()

const SHOW_NEXT_NODES = 1
const SHOW_PREV_NODES = 2
const SHOW_ALL = 3

# Renders the linking arrows.
func _process(_delta: float) -> void:
	if Engine.is_editor_hint():
		# Only the node model should be rotated/scaled
		# Because the root node is being edited, we can't just forward
		# Those transformation to the node model and keep the rest normal.
		# If we'd try, it won't be saved as it's an instanced scene
#		var inverse_rotation = -self.transform.basis.get_euler()
#		var inverse_scale = self.scale.inverse()
#		$Star.rotation = inverse_rotation
#		$Star.scale = inverse_scale
		var controllers: Array = get_tree().get_nodes_in_group("Controller")
		var show_linking_type: int = SHOW_ALL
		if controllers.size() > 0:
			show_linking_type = controllers[0].show_linking_type

		var tool := SurfaceTool.new()
		tool.begin(Mesh.PRIMITIVE_LINES)
		if (show_linking_type & SHOW_NEXT_NODES) != 0 and not next.is_empty():
			for n in next:
				if n.is_empty():
					continue
				var node := get_node(n)
				tool.set_color(Color(0.0, 1.0, 1.0, 1.0))
				var dir: Vector3 = node.global_position - self.global_position

				var offset: Vector3 =\
						0.25 * Vector3(0, 1, 0).cross(dir.normalized())
				dir *= (dir.length() - 2*NODE_RADIUS) / dir.length()
				offset += dir.normalized() * NODE_RADIUS
				tool.add_vertex(self.global_position + offset)
				tool.add_vertex(self.global_position + dir + offset)
				tool.add_vertex(self.global_position + dir + offset)
				tool.add_vertex(self.global_position + dir + offset +
						(-0.25 * dir.normalized()).\
						rotated(Vector3(0, 1, 0), 0.2617994))
				tool.add_vertex(self.global_position + dir + offset)
				tool.add_vertex(self.global_position + dir + offset +
						(-0.25 * dir.normalized()).\
						rotated(Vector3(0, 1, 0), -0.2617994))
		if (show_linking_type & SHOW_PREV_NODES) != 0 and not prev.is_empty():
			for n in prev:
				if n.is_empty():
					continue
				var node := get_node(n)

				tool.set_color(Color(1.0, 0.0, 0.5, 1.0))
				var dir = node.global_position - self.global_position

				var offset = 0.25 * Vector3(0, 1, 0).cross(dir.normalized())
				dir *= (dir.length() - 2*NODE_RADIUS) / dir.length()
				offset += dir.normalized() * NODE_RADIUS
				tool.add_vertex(self.global_position + offset)
				tool.add_vertex(self.global_position + dir + offset)
				tool.add_vertex(self.global_position + dir + offset)
				tool.add_vertex(self.global_position + dir + offset +
						(-0.25 * dir.normalized()).\
						rotated(Vector3(0, 1, 0), 0.2617994))
				tool.add_vertex(self.global_position + dir + offset)
				tool.add_vertex(self.global_position + dir + offset +
						(-0.25 * dir.normalized()).\
						rotated(Vector3(0, 1, 0), -0.2617994))
		$EditorLines.mesh = tool.commit()
		$EditorLines.global_transform = Transform3D()

func _get_configuration_warnings() -> PackedStringArray:
	var warnings := []
	if next.is_empty():
		warnings.append("No outgoing nodes configured")
	if prev.is_empty():
		warnings.append("No incoming nodes configured")
	return warnings
