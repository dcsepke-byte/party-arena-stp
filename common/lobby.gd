extends Node
class_name Lobby

signal loading_finished

# We need to uniquely identify players
# There can be multiple players playing on one computer
# The idx field enumerates the players on a single pc
# Combined with the network id of the client this is a unique identifier
class PlayerAddress:
	var peer_id: int
	var idx: int

	func _init(peer_id: int, idx: int):
		self.peer_id = peer_id
		self.idx = idx

	func eq(other: PlayerAddress) -> bool:
		return peer_id == other.peer_id and idx == other.idx

	func encode():
		return [peer_id, idx]

	static func decode(data):
		return PlayerAddress.new(data[0], data[1])

class PlayerInfo:
	var lobby: Lobby
	var player_id: int
	var addr: PlayerAddress
	var name: String
	var character: String
	var ai_difficulty: int = Difficulty.NORMAL
	
	func _init(lobby: Node, addr: PlayerAddress, name: String, character: String):
		self.lobby = lobby
		self.addr = addr
		self.name = name
		self.character = character
	
	func encode():
		return [addr.encode(), name, character, ai_difficulty]
	
	static func decode(lobby: Node, data) -> PlayerInfo:
		return PlayerInfo.new(lobby, PlayerAddress.decode(data[0]), data[1], data[2])
	
	func is_ai() -> bool:
		return addr.peer_id == 1
	
	func is_local() -> bool:
		return addr.peer_id == lobby.multiplayer.get_network_unique_id()

# Game State of a player, includes information such as cookies, cakes, etc.
class PlayerState:
	var info: Lobby.PlayerInfo
	var cookies := 10
	var cakes := 0
	var items := [ preload("res://plugins/items/dice/item.gd").new().serialize() ]
	var roll_modifiers := []
	
	func _init(info: Lobby.PlayerInfo):
		self.info = info

	func encode():
		return [info.player_id, cookies, cakes, items, roll_modifiers]

	static func decode(lobby: Lobby, data) -> PlayerState:
		var info := lobby.get_player_by_id(data[0])
		if not info:
			return null
		var state = PlayerState.new(info)
		state.cookies = data[1]
		state.cakes = data[2]
		state.items = data[3]
		state.roll_modifiers = data[4]
		return state

	# Which space on the board the player is standing on.
	var space

class MinigameState:
	var minigame_config: MinigameLoader.MinigameConfigFile
	var minigame_teams: Array = []
	var minigame_type: int = -1

	# Whether the current minigame was meant to be tried only
	var is_try: bool = false
	
	func encode():
		return [minigame_config.filename, minigame_teams, minigame_type]
	
	static func decode(data) -> MinigameState:
		var state = MinigameState.new()
		state.minigame_config = PluginSystem.minigame_loader.get_config_by_path(data[0])
		if not state.minigame_config:
			return null
		state.minigame_teams = data[1]
		state.minigame_type = data[2]
		return state

class MinigameSummary:
	var state: Lobby.MinigameState
	var placement
	var reward

class MinigameReward:
	var duel_reward: int = -1
	var gnu_solo_item_reward: Item = null

enum MINIGAME_TYPES {
	DUEL,
	ONE_VS_THREE,
	TWO_VS_TWO,
	FREE_FOR_ALL,
	NOLOK_SOLO,
	NOLOK_COOP,
	GNU_SOLO,
	GNU_COOP,
}

enum MINIGAME_DUEL_REWARDS {
	TEN_COOKIES,
	ONE_CAKE
}

enum Difficulty {
	EASY,
	NORMAL,
	HARD
}

# The players in the lobby described by a PlayerInfo (see above)
var player_info := []
var playerstates := []

# Pointer to top-level node in current scene.
var current_scene: Node = null

# Resource location of the current board.
var current_board: String

# The minigame that is currently being played.
# If we're returning to the game and this is not null, then
# we've been in the "try minigame" mode.
# Therefore we need to show the minigame screen again to
# do the actual minigame
var minigame_state: MinigameState = null

# Hold's information regarding the last played minigame
var minigame_summary: MinigameSummary = null

# Hold's the reward type for the current minigame:
# Only used in Duel and Gnu Solo minigames
var minigame_reward: MinigameReward = null

var cake_space := NodePath()

var interactive_loaders := []
var loaded_scene: Node = null

static func get_lobby(caller: Node) -> Lobby:
	# The scripts for each lobby (if present)
	var client_lobby
	var server_lobby
	if ResourceLoader.exists("res://client/lobby.gd"):
		client_lobby = load("res://client/lobby.gd")
	if ResourceLoader.exists("res://server/lobby.gd"):
		server_lobby = load("res://server/lobby.gd")
	while caller != null:
		if client_lobby and client_lobby.instance_has(caller):
			return caller as Lobby
		if server_lobby and server_lobby.instance_has(caller):
			return caller as Lobby
		caller = caller.get_parent()
	# Couldn't find a lobby
	return null

func is_lobby_owner(id: int):
	return player_info and id == player_info[0].addr.peer_id

func assign_player_ids():
	var player_id := 1
	for player in self.player_info:
		player.player_id = player_id
		player_id += 1

func get_player_count():
	return len(player_info)

func get_player_by_id(id: int) -> PlayerInfo:
	return player_info[id - 1]

func get_player_by_addr(addr: PlayerAddress) -> PlayerInfo:
	for player in self.player_info:
		if player.addr.eq(addr):
			return player
	return null

func get_players_by_network_id(id: int) -> Array:
	var res = []
	for player in self.player_info:
		if player.addr.peer_id == id:
			res.append(player)
	return res

func get_playerstate(id: int) -> PlayerState:
	return playerstates[id - 1]

# ----- Network helper ----- #

func broadcast(node: Node, method: String, args := []):
	# Don't send message to self
	var messaged := [ multiplayer.get_network_unique_id() ]
	for player in self.player_info:
		if player.addr.peer_id in messaged:
			continue
		messaged.append(player.addr.peer_id)
		node.callv("rpc_id", [player.addr.peer_id, method] + args)

func broadcast_unreliable(node: Node, method: String, args := []):
	# Don't send message to self
	var messaged := [ multiplayer.get_network_unique_id() ]
	for player in self.player_info:
		if player.addr.peer_id in messaged:
			continue
		messaged.append(player.addr.peer_id)
		node.callv("rpc_unreliable_id", [player.addr.peer_id, method] + args)

# ----- Scene instantiation ----- #

# Internal function for loading a character's model and other data
# into the nodes used by the loaded scene
func _load_player(player: Node, info: PlayerInfo):
	var character := info.character
	var wants_model := player.has_node("Model")
	var wants_shape := player.has_node("Shape")

	if wants_model:
		var model: Spatial = PluginSystem.character_loader.load_character(character)
		model.name = "Model"

		var shape: CollisionShape = model.get_node_or_null(model.collision_shape)
		if shape:
			# global_transform only works when the node is in the scene tree
			# Therefore, we have to compute it ourselves
			var transform := shape.transform
			var parent := shape.get_parent()
			while parent != null:
				if parent is Spatial:
					transform = parent.transform * transform
				parent = parent.get_parent()
			shape.get_parent().remove_child(shape)
			shape.transform = transform
			shape.name = "Shape"
		else:
			push_warning("Character `{0}` has no shape".format([character]))

		var placeholder: Spatial = player.get_node("Model")
		# The model should be at the place, the placeholder was originally
		model.transform = placeholder.transform * model.transform
		# The shape should be at the same position as the model
		if shape:
			shape.transform = model.transform * shape.transform

		placeholder.replace_by(model, true)
		if wants_shape:
			# shape must be a direct child of kinematicBody and similar
			# Therefore we need to move it one up in the scene tree
			player.get_node("Shape").replace_by(shape)
	elif wants_shape:
		push_warning(
			"`{0}` in scene `{1}`".format([player.name, player.owner.filename])
			+ " has a `Shape` child, but no `Model` child.\n"
			+ "This is not allowed. Ignoring `Shape`")

	player.info = info

# ----- Scene changing code ----- #

func set_current_scene(scene: Node):
	self.current_scene = scene

func _goto_scene_instant(scene: PackedScene) -> void:
	if current_scene:
		current_scene.free()
	current_scene = scene.instance()
	add_child(current_scene)

func change_scene():
	if current_scene:
		current_scene.free()
	current_scene = loaded_scene
	loaded_scene = null

	add_child(current_scene)

var _objects_to_load := 0
func _load_interactive(path: String, base: Object, method: String, arg):
	_objects_to_load += 1
	Global._load_interactive(path, self, "_object_loaded", [base, method, arg])

func _object_loaded(resource: Resource, arg: Array):
	_objects_to_load -= 1
	arg[0].call(arg[1], resource, arg[2])
	if _objects_to_load == 0:
		emit_signal("loading_finished")
