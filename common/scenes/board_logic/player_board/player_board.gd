extends Spatial
class_name PlayerBoard

const MOVEMENT_SPEED = 7 # The speed used for walking to destination
const GUI_TIMER = 0.2

const MAX_ITEMS = 3

class WalkingState:
	var space: NodeBoard
	var position: Vector3

# The position this node is walking to, used for animation
var destination := []

signal walking_step
signal walking_ended

var info: Lobby.PlayerInfo

var space: NodeBoard # Space on the board the player is on
var cookies := 0 setget set_cookies
var cakes := 0 setget set_cakes
var cookies_gui := -1
var gui_timer: float = GUI_TIMER
var target_rotation := 0.0

# Set by the controller node
var controller: Node

var is_walking := false

var items := []
var roll_modifiers := []

puppet func set_cookies(c: int):
	cookies = c
	if cookies_gui == -1:
		cookies_gui = c
	controller.update_player_info()
	if multiplayer.is_network_server():
		controller.lobby.broadcast(self, "set_cookies", [c])

puppet func set_cakes(c: int):
	cakes = c
	controller.update_player_info()
	if multiplayer.is_network_server():
		controller.lobby.broadcast(self, "set_cakes", [c])

func serialize_items() -> Array:
	var serialized := []
	for item in items:
		serialized.append(item.serialize())
	return serialized

func deserialize_items(data: Array):
	var deserialized := []
	for item in data:
		var res := Item.deserialize(item)
		if not res:
			return null
		deserialized.append(res)
	return deserialized

func give_item(item: Item) -> bool:
	if items.size() < MAX_ITEMS:
		items.push_back(item)
		update_client()
		return true
	return false

func remove_item(item: Item) -> bool:
	var index: int = items.find(item)
	if index >= 0:
		items.remove(index)
		update_client()
		return true
	return false

func update_client():
	controller.lobby.broadcast(self, "set_items", [serialize_items()])

puppet func set_items(data: Array):
	var items = deserialize_items(data)
	if items:
		self.items = items
		controller.update_player_info()
	else:
		controller.lobby.leave()

func add_roll_modifier(amount: int, num_rounds: int):
	roll_modifiers.push_back([amount, num_rounds])

func get_total_roll_modifier():
	var res := 0
	for mod in roll_modifiers:
		res += mod[0]

	return res

func roll_modifiers_count_down():
	var newarr = []
	for mod in roll_modifiers:
		mod[1] -= 1
		if mod[1] > 0:
			newarr.push_back(mod)
	
	roll_modifiers = newarr

func walk_to(new_space: Spatial) -> void:
	var old_space: NodeBoard = space
	space = new_space
	controller.update_space(old_space)
	controller.update_space(new_space)

func teleport_to(new_space: Spatial) -> void:
	var old_space: NodeBoard = space
	space = new_space
	if old_space:
		controller.update_space(old_space)
	controller.update_space(new_space)
	translation = destination.back().position
	controller.lobby.broadcast(self, "_client_update_position", [get_path_to(new_space), translation])

func _internal_walk_to(space: Spatial, pos: Vector3) -> void:
	var state = WalkingState.new()
	state.space = space
	state.position = pos
	destination.append(state)
	controller.lobby.broadcast(self, "_client_walk_to", [get_path_to(space), pos])

puppet func _client_walk_to(new_space: NodePath, position: Vector3):
	var space := get_node(new_space)
	# Check if the node we got is part of the game
	if not controller.lobby.is_a_parent_of(space):
		controller.lobby.leave()
	self.space = space
	var state = WalkingState.new()
	state.space = self.space
	state.position = position
	self.destination.push_back(state)

puppet func _client_update_position(new_space: NodePath, position: Vector3):
	var space := get_node(new_space)
	# Check if the node we got is a part of the game
	if not controller.lobby.is_a_parent_of(space):
		controller.lobby.leave()
	self.space = space
	self.translation = position
	self.destination.clear()

func _physics_process(delta: float) -> void:
	if destination.size() > 0:
		if not is_walking:
			$Model.play_animation("walk")
			is_walking = true

		var dir: Vector3 = destination[0].position - translation
		var movement: Vector3 = MOVEMENT_SPEED * dir.normalized() * delta
		translation += movement

		target_rotation = atan2(dir.normalized().x, dir.normalized().z)

		if dir.length() < 2 * delta * MOVEMENT_SPEED:
			var state = destination.pop_front()
			emit_signal("walking_step", state.space)

		if destination.size() == 0:
			target_rotation = 0

			$Model.play_animation("idle")
			is_walking = false

			controller.update_player_info()
			emit_signal("walking_ended")
	else:
		target_rotation = 0
		if cookies_gui < cookies:
			gui_timer -= delta

			if gui_timer <= 0:
				gui_timer = GUI_TIMER
				cookies_gui += 1
				controller.update_player_info()
		elif cookies_gui > cookies:
			gui_timer -= delta

			if gui_timer <= 0:
				gui_timer = GUI_TIMER
				cookies_gui -= 1
				controller.update_player_info()

	var dist: float = rotation.y - target_rotation

	if abs(dist) > deg2rad(0.1):
		while dist > PI:
			dist -= TAU
		while dist < -PI:
			dist += TAU

		if dist > 0:
			rotation.y -= 5 * delta * dist
		else:
			rotation.y += 5 * delta * abs(dist)
