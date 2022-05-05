extends Node

func create_local_server(public: bool = false) -> Node:
	var game_server := preload("res://server/game.tscn").instance()
	var server := NetworkedMultiplayerENet.new()
	if not public:
		server.set_bind_ip("127.0.0.1")
	if server.create_server(7163) != OK:
		return null
	var client := NetworkedMultiplayerENet.new()
	if client.create_client("127.0.0.1", 7163) != OK:
		return null
	
	game_server.get_node("Game").custom_multiplayer = MultiplayerAPI.new()
	game_server.get_node("Game").custom_multiplayer.network_peer = server
	get_tree().network_peer = client
	get_tree().root.add_child(game_server)
	
	var game_client := preload("res://client/game.tscn").instance()
	get_tree().root.add_child(game_client)
	return game_client.get_node("Game")

func destroy_local_server():
	get_node("/root/Client").free()
	get_node("/root/Server").free()

func connect_remote_server(ip, port) -> Node:
	var peer = NetworkedMultiplayerENet.new()
	if peer.create_client(ip, port) != OK:
		return null
	get_tree().network_peer = peer
	var game_client := preload("res://client/game.tscn").instance()
	get_tree().root.add_child(game_client)
	return game_client.get_node("Game")

func get_current_server() -> Node:
	return get_node_or_null("/root/Client/Game")

func destroy_remote_connection():
	get_node("/root/Client").free()

func shutdown_connection():
	if has_node("/root/Server"):
		destroy_local_server()
	elif has_node("/root/Client"):
		destroy_remote_connection()

func is_local_multiplayer() -> bool:
	return has_node("/root/Client") and has_node("/root/Server")

const USER_STORAGE_FILE = "user://data.cfg"
#
#var savegame_loader := SaveGameLoader.new()
#
# warning-ignore:unused_signal
signal language_changed

var interactive_loaders := {}

# Pause game if the window loses focus.
var pause_window_unfocus := true

# Mute game if the window loses focus.
var mute_window_unfocus := true
var _was_muted := false

# ConfigFile to store custom data between sessions
var storage: ConfigFile = ConfigFile.new()

# Stops the controller from loading information when starting a new game.
#
#var current_savegame: Object
#var is_new_savegame := false

func _ready() -> void:
	randomize()
	var err = storage.load(USER_STORAGE_FILE)
	if err != OK:
		print("Error while loading saved data: " + Utility.error_code_to_string(err))

#	savegame_loader.read_savegames()

func _notification(what: int) -> void:
	match what:
		MainLoop.NOTIFICATION_WM_FOCUS_IN:
			if mute_window_unfocus:
				if not _was_muted:
					AudioServer.set_bus_mute(0, false)
				else:
					_was_muted = false
		MainLoop.NOTIFICATION_WM_FOCUS_OUT:
			if mute_window_unfocus:
				if not AudioServer.is_bus_mute(0):
					AudioServer.set_bus_mute(0, true)
				else:
					_was_muted = true

func _input(event):
	if event.is_action_pressed("screenshot"):
		var time = OS.get_datetime()
		var image = get_tree().root.get_texture().get_data()
		image.flip_y()
		var directory = Directory.new()
		directory.make_dir("user://screenshots")
		image.save_png("user://screenshots/%04dY-%02dM-%02dD %02dh-%02dm-%02ds.png" % [time.year, time.month, time.day, time.hour, time.minute, time.second])

func _process(_delta: float) -> void:
	for path in interactive_loaders.keys():
		var data = interactive_loaders[path]
		var err = data[0].poll()
		match err:
			OK:
				break
			ERR_FILE_EOF:
				for callback in data[1]:
					callback[0].call(callback[1], data[0].get_resource(), callback[2])
				interactive_loaders.erase(path)
			_:
				print(err)
				push_error("Failed to load resource: %s" % path)

func get_loader_progress():
	var loaded = 0
	var stages = 0
	for data in interactive_loaders.values():
		loaded += data[0].get_stage()
		stages += data[0].get_stage_count()
	return [loaded, stages]

func _load_interactive(path: String, base: Object, method: String, arg):
	# Resourceloader cannot load the same resource multiple times simultaneously
	# Check if we're already loading the path, so we can add another callback
	if path in interactive_loaders:
		interactive_loaders[path][1].append([base, method, arg])
		return
	var loader = ResourceLoader.load_interactive(path)
	if loader:
		interactive_loaders[path] = [loader, [[base, method, arg]]]
	else:
		push_error("Failed to obtain loader for `{0}`".format([path]))

#func new_savegame() -> void:
#	current_savegame = SaveGameLoader.SaveGame.new()
#	is_new_savegame = true
#
#func save_game() -> void:
#	var r_players: Array = get_tree().get_nodes_in_group("players")
#	var controller: Spatial = get_tree().get_nodes_in_group("Controller")[0]
#
#	current_savegame.board_path = current_board;
#	for i in amount_of_players:
#		current_savegame.players[i].player_name = r_players[i].player_name
#		current_savegame.players[i].is_ai = r_players[i].is_ai
#		current_savegame.players[i].ai_difficulty = r_players[i].ai_difficulty
#		current_savegame.players[i].space = r_players[i].space.get_path()
#		current_savegame.players[i].character = players[i].character
#		current_savegame.players[i].cookies = r_players[i].cookies
#		current_savegame.players[i].cakes = r_players[i].cakes
#		current_savegame.players[i].items = duplicate_items(r_players[i].items)
#		current_savegame.players[i].roll_modifiers = r_players[i].roll_modifiers
#
#	current_savegame.cake_space = cake_space
#	if minigame_state:
#		current_savegame.current_minigame = minigame_state.minigame_config
#		current_savegame.minigame_type = minigame_state.minigame_type
#		current_savegame.minigame_teams = minigame_state.minigame_teams.duplicate()
#	else:
#		current_savegame.current_minigame = null
#	current_savegame.player_turn = controller.player_turn
#	current_savegame.turn = turn
#	current_savegame.cake_cost = overrides.cake_cost
#	current_savegame.max_turns = overrides.max_turns
#	current_savegame.award_type = overrides.award
#
#	current_savegame.trap_states = []
#
#	for trap in get_tree().get_nodes_in_group("trap"):
#		var state := {
#			node = trap.get_path(),
#			item = inst2dict(trap.trap),
#			player = trap.trap_player.get_path()
#		}
#
#		current_savegame.trap_states.push_back(state)
#
#	savegame_loader.save(current_savegame)

func save_storage():
	storage.save(USER_STORAGE_FILE)
