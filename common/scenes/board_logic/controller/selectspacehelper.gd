extends Spatial

signal space_selected(space)

onready var controller: Controller = get_parent()

var current_player: PlayerBoard
var selected_space: NodeBoard
var selected_space_distance: int
var select_space_max_distance: int

func _ready():
	set_as_toplevel(true)

func get_next_spaces(space: NodeBoard):
	var result = []

	for p in space.next:
		if p.is_visible_space():
			result.append(p)
		else:
			result += get_next_spaces(p)

	return result

func get_prev_spaces(space: NodeBoard):
	var result = []

	for p in space.prev:
		if p.is_visible_space():
			result.append(p)
		else:
			result += get_prev_spaces(p)

	return result

func select_random_space(space: NodeBoard, max_distance: int) -> NodeBoard:
	# Select random space in front of or behind player
	# Can be the same space as well
	var distance: int = (randi() % (2*max_distance + 1)) - max_distance

	if distance > 0:
		while distance > 0:
			var possible_spaces = get_next_spaces(space)
			if possible_spaces.size() == 0:
				break

			space = possible_spaces[randi() % possible_spaces.size()]
			distance -= 1
	else:
		while distance < 0:
			var possible_spaces = get_prev_spaces(space)
			if possible_spaces.size() == 0:
				break

			space = possible_spaces[randi() % possible_spaces.size()]
			distance += 1
	return space

func select_space(player: PlayerBoard, max_distance: int) -> void:
	if player.info.is_ai():
		var space := select_random_space(player.space, max_distance)

		yield(get_tree().create_timer(1), "timeout")
		emit_signal("space_selected", space)
	else:
		current_player = player
		selected_space = player.space
		select_space_max_distance = max_distance
		rpc_id(player.info.addr.peer_id, "_client_select_space", player.info.player_id, max_distance)

func get_reachable(space: NodeBoard, distance: int):
	var nodes := []
	var prev := [space]
	var next := [space]
	for i in range(distance):
		var nprev = []
		var nnext = []
		for node in prev:
			nodes.append(node)
			nprev += get_prev_spaces(node)
		for node in next:
			nodes.append(node)
			nnext += get_prev_spaces(node)
		prev = nprev
		next = nnext
	return nodes + prev + next

# Called when player disconnects while waiting for space selection
func end_selection():
	current_player = null
	emit_signal("space_selected", selected_space)

puppet func _client_select_space(player_id: int, max_distance: int):
		selected_space_distance = 0
		select_space_max_distance = max_distance

		selected_space = controller.players[player_id - 1].space
		show_select_space_arrows()

master func _client_space_selected(path: NodePath):
	if not current_player or multiplayer.get_rpc_sender_id() != current_player.info.addr.peer_id:
		return
	var space = get_node(path)
	print(space)
	if not space is NodeBoard or not controller.lobby.is_a_parent_of(space):
		controller.lobby.kick(multiplayer.get_rpc_sender_id(), "Misbehaving Client")
		return
	print(get_reachable(selected_space, select_space_max_distance))
	if not space in get_reachable(selected_space, select_space_max_distance):
		controller.lobby.kick(multiplayer.get_rpc_sender_id(), "Misbehaving Client")
		return
	current_player = null
	emit_signal("space_selected", space)

func show_select_space_arrows() -> void:
	var keep_arrow = preload(\
			"res://common/scenes/board_logic/node/arrow/arrow_keep.tscn").instance()

	keep_arrow.next_node = selected_space
	keep_arrow.translation = selected_space.translation

	keep_arrow.connect("arrow_activated", self,
			"_on_select_space_arrow_activated", [keep_arrow, 0])

	var arrows := [keep_arrow]
	add_child(keep_arrow)

	var previous = keep_arrow

	if selected_space_distance < select_space_max_distance:
		for node in get_next_spaces(selected_space):
			var arrow = preload("res://common/scenes/board_logic/node/arrow/" +\
					"arrow.tscn").instance()
			var dir: Vector3 = node.translation - selected_space.translation

			dir = dir.normalized()

			arrow.previous_arrow = previous
			previous.next_arrow = arrow

			arrow.next_node = node
			arrow.translation = selected_space.translation
			arrow.rotation.y = atan2(dir.normalized().x, dir.normalized().z)

			arrow.connect("arrow_activated", self,
					"_on_select_space_arrow_activated", [arrow, 1])

			add_child(arrow)
			previous = arrow
			arrows.append(arrow)

	if selected_space_distance > -select_space_max_distance:
		for node in get_prev_spaces(selected_space):
			var arrow = preload("res://common/scenes/board_logic/node/arrow/" +\
					"arrow.tscn").instance()
			var dir: Vector3 = node.translation - selected_space.translation

			dir = dir.normalized()

			arrow.previous_arrow = previous
			previous.next_arrow = arrow

			arrow.next_node = node
			arrow.translation = selected_space.translation
			arrow.rotation.y = atan2(dir.normalized().x, dir.normalized().z)

			arrow.connect("arrow_activated", self,
					"_on_select_space_arrow_activated", [arrow, -1])

			add_child(arrow)
			previous = arrow
			arrows.append(arrow)

	previous.next_arrow = keep_arrow
	keep_arrow.previous_arrow = previous

	keep_arrow.selected = true

	controller.camera_focus = selected_space

	for arrow in arrows:
		arrow.arrow_nodes = arrows

func _on_select_space_arrow_activated(arrow, distance: int) -> void:
	print(arrow.next_node, selected_space)
	if arrow.next_node == selected_space:
		rpc_id(1, "_client_space_selected", get_path_to(selected_space))
		return

	selected_space = arrow.next_node
	selected_space_distance += distance

	show_select_space_arrows()
