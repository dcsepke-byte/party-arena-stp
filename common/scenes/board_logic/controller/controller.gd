extends Spatial
class_name Controller

signal trigger_event(player, space)

signal path_chosen(idx)
signal item_selected(idx)

signal next_player()
signal rolled(player, num)

# FIXME: Remove once Godot 4 is released (need support for await, see in _step)
signal purchase_cake(player)
signal cake_purchased

signal players_acknowledged()

signal _calculate_step(player, previous_space, last)
# This signal is emitted with a
# 'call_deferred("emit_signal", "_step_finished")'.
# warning-ignore:unused_signal
signal _step_finished(is_visible)
# This signal is emitted with a
# 'call_deferred("emit_signal", "_event_completed")'.
# warning-ignore:unused_signal
signal _event_completed()
signal _camera_focus_aquired()

# If multiple players get on one space, this array decides the translation of
# each.
const PLAYER_TRANSLATION = [Vector3(0, 0, -0.75), Vector3(0.75, 0, 0),
		Vector3(0, 0, 0.75), Vector3(-0.75, 0, 0)]
const EMPTY_SPACE_PLAYER_TRANSLATION = Vector3(0, 0.05, 0)
const CAMERA_SPEED = 6

const PLAYER = preload("res://common/scenes/board_logic/player_board/player_board.gd")
const PLACEMENT_COLORS := [Color("#FFD700"), Color("#C9C0BB"), Color("#CD7F32"), Color(0.3, 0.3, 0.3)]

# Game options that can be customized in the Godot editor
# Useful for board creation
export var COOKIES_FOR_CAKE := 30
export var MAX_TURNS := 10

var lobby: Lobby

# Are we the game server or a client?
var server: bool

# Array containing the player nodes.
var players: Array

# Keeps track of whose turn it is.
var player_turn := 1

# Keeps track whether the current player has already rolled,
# thus preventing them from rolling multiple times during their own turn
# Reset in _on_next_player
var has_rolled := true

var wait_for_path_select := false
var wait_for_select_item := false
var wait_for_duel_selection := false

var camera_focus: Spatial

enum EDITOR_NODE_LINKING_DISPLAY {
	DISABLED,
	NEXT_NODES,
	PREV_NODES,
	ALL
}

# Path to the node, where Players start.
export var start_node: NodePath
export(EDITOR_NODE_LINKING_DISPLAY) var show_linking_type: int =\
		EDITOR_NODE_LINKING_DISPLAY.ALL

# Stores the value of steps that still need to be performed after a dice roll.
# Used for display.
var step_count := 0

func _ready() -> void:
	# FIXME: obsolete once Godot supports await (Godot 4)
	connect("purchase_cake", self, "buy_cake")

	lobby = Lobby.get_lobby(self)

	server = multiplayer.is_network_server()
	players = Utility.get_nodes_in_group(lobby, "players")
	for p in players:
		p.controller = self

	if server:
		connect("next_player", self, "_on_next_player")
		connect("rolled", self, "do_step")
		connect("_calculate_step", self, "_step")
		lobby.connect("player_left", self, "_on_player_disconnected")
		lobby.load_board_state(self)
		lobby.broadcast(self, "set_turn", [lobby.turn, lobby.overrides.max_turns])
		# Teleporting to the start position needs a valid space for each player
		# Therefore, we use 2 loops to set this stuff up
		for p in players:
			if not p.space:
				p.space = get_node(start_node)
			p.teleport_to(p.space)
			p.update_client()
		lobby.broadcast(self, "_setup_finished")
	else:
		var pause_menu = load("res://client/menus/pause_menu.tscn").instance()
		pause_menu.can_save_game = true
		$Screen.add_child(pause_menu)
		for p in players:
			# Update the "spaces to walk" counter
			p.connect("walking_step", self, "animation_step", [p.info.player_id])
			# Play a short fx when passing a step
			p.connect("walking_step", self, "play_space_step_sfx", [p.info.player_id])

	if not server:
		if player_turn <= players.size():
			camera_focus = players[player_turn - 1]

		update_player_info()

	$Screen/Debug.setup()
	if lobby.minigame_summary:
		# Do some moderation according to the last minigame type being played
		if server:
			match lobby.minigame_summary.state.minigame_type:
				Lobby.MINIGAME_TYPES.GNU_SOLO:
					var player_id = player_turn
					players[player_id - 1].give_item(lobby.minigame_summary.reward)
					player_turn += 1
					# TODO: better timeouts
					yield(get_tree().create_timer(5.0), "timeout")
				Lobby.MINIGAME_TYPES.GNU_COOP:
					player_turn += 1
					yield(get_tree().create_timer(5.0), "timeout")
				Lobby.MINIGAME_TYPES.NOLOK_SOLO:
					player_turn += 1
					yield(get_tree().create_timer(5.0), "timeout")
				Lobby.MINIGAME_TYPES.NOLOK_COOP:
					player_turn += 1
					yield(get_tree().create_timer(5.0), "timeout")
		else:
			match lobby.minigame_summary.state.minigame_type:
				Lobby.MINIGAME_TYPES.GNU_SOLO:
					var player_id = player_turn
					if lobby.minigame_summary.placement:
						$Screen/SpeechDialog.show_dialog("CONTEXT_GNU_NAME", "res://common/scenes/board_logic/controller/icons/gnu_icon.png", "CONTEXT_GNU_SOLO_VICTORY", player_id)
					else:
						$Screen/SpeechDialog.show_dialog("CONTEXT_GNU_NAME", "res://common/scenes/board_logic/controller/icons/gnu_icon.png", "CONTEXT_GNU_SOLO_LOSS", player_id)
				Lobby.MINIGAME_TYPES.GNU_COOP:
					var player_id = player_turn
					if lobby.minigame_summary.placement:
						$Screen/SpeechDialog.show_dialog("CONTEXT_GNU_NAME", "res://common/scenes/board_logic/controller/icons/gnu_icon.png", "CONTEXT_GNU_COOP_VICTORY", player_id)
					else:
						$Screen/SpeechDialog.show_dialog("CONTEXT_GNU_NAME", "res://common/scenes/board_logic/controller/icons/gnu_icon.png", "CONTEXT_GNU_COOP_LOSS", player_id)
				Lobby.MINIGAME_TYPES.NOLOK_SOLO:
					var player_id = player_turn
					if lobby.minigame_summary.placement:
						$Screen/SpeechDialog.show_dialog("CONTEXT_NOLOK_NAME", "res://common/scenes/board_logic/controller/icons/nolokicon.png", "CONTEXT_NOLOK_SOLO_VICTORY", player_id)
					else:
						$Screen/SpeechDialog.show_dialog("CONTEXT_NOLOK_NAME", "res://common/scenes/board_logic/controller/icons/nolokicon.png", "CONTEXT_NOLOK_SOLO_LOSS", player_id)
				Lobby.MINIGAME_TYPES.NOLOK_COOP:
					var player_id = player_turn
					if lobby.minigame_summary.placement:
						$Screen/SpeechDialog.show_dialog("CONTEXT_NOLOK_NAME", "res://common/scenes/board_logic/controller/icons/nolokicon.png", "CONTEXT_NOLOK_COOP_VICTORY", player_id)
					else:
						$Screen/SpeechDialog.show_dialog("CONTEXT_NOLOK_NAME", "res://common/scenes/board_logic/controller/icons/nolokicon.png", "CONTEXT_NOLOK_COOP_LOSS", player_id)

#	if not server:
#		if Global.storage.get_value("Controller", "show_tutorial", true):
#			if yield(ask_yes_no("CONTEXT_SHOW_TUTORIAL"), "completed"):
#				yield(show_tutorial(), "completed")
#			Global.storage.set_value("Controller", "show_tutorial", false)
#			Global.save_storage()

	if server:
		if not lobby.cake_space:
			yield(relocate_cake(), "completed")
		if lobby.minigame_state:
			# If we did try the minigame out, the minigame_state will be set
			# Therefore we still have to play the minigame
			lobby.broadcast(self, "show_minigame", [lobby.minigame_state.encode()])
		else:
			# Continue with the board action
			emit_signal("next_player")

func acknowledge():
	rpc_id(1, "client_acknowledged")

func _on_player_disconnected(player_id: int):
	# when a player has left/kicked, the AI must continue currently active actions
	if player_id != player_turn:
		return
	var player: PlayerBoard = players[player_turn - 1]
	# This includes:
	# * Start your turn
	if not has_rolled:
		_on_Roll_pressed()
	# * Item Shopping
	elif $Screen/Shop.current_player:
		$Screen/Shop.end_shopping()
	# * Item Selection
	elif wait_for_select_item:
		wait_for_select_item = false
		emit_signal("item_selected", randi() % len(player.items))
	# * Path Selection
	elif wait_for_path_select:
		wait_for_path_select = false
		var idx: int = randi() % player.space.next.size()
		emit_signal("path_chosen", player.space.next[idx])
	# * Space Selection (trap items)
	elif wait_for_duel_selection:
		var players: Array = self.players.duplicate()
		players.erase(player)
		var enemy_player = players[randi() % players.size()].info.player_id
		$Screen/DuelSelection.emit_signal("selected", enemy_player)
	elif $SelectSpaceHelper.current_player:
		$SelectSpaceHelper.end_selection()

var current_timer: SceneTreeTimer = null
func player_timeout(addr: Lobby.PlayerAddress):
	lobby.kick(addr.peer_id, "Inactivity")

func start_timer_for_player(addr: Lobby.PlayerAddress):
	if lobby.timeout <= 0:
		return
	assert(current_timer == null, "A previous timer was not stopped")
	current_timer = get_tree().create_timer(lobby.timeout)
	current_timer.connect("timeout", self, "player_timeout", [addr])

func cancel_timer():
	if not current_timer:
		return
	current_timer.disconnect("timeout", self, "player_timeout")
	current_timer = null

var acknowledgements_needed := {}
var acknowledgement_timer: SceneTreeTimer = null
func acknowledgement_timeout():
	acknowledgement_timer = null
	for peer in acknowledgements_needed:
		lobby.kick(peer, "Inactivity")
	acknowledgements_needed.clear()
	emit_signal("players_acknowledged")

func wait_for_acknowledgement():
	assert (not acknowledgements_needed, "Nested acknowledgements")
	if lobby.timeout > 0:
		acknowledgement_timer = get_tree().create_timer(lobby.timeout)
		acknowledgement_timer.connect("timeout", self, "acknowledgement_timeout")
	for player in players:
		if player.info.is_ai():
			continue
		acknowledgements_needed[player.info.addr.peer_id] = true

master func client_acknowledged():
	if  not acknowledgements_needed:
		return
	acknowledgements_needed.erase(multiplayer.get_rpc_sender_id())
	if not acknowledgements_needed:
		if acknowledgement_timer:
			acknowledgement_timer.disconnect("timeout", self, "acknowledgement_timeout")
			acknowledgement_timer = null
		emit_signal("players_acknowledged")

func announce(text: String, format_args := {}):
	var current_player = players[player_turn - 1]
	var sara_icon := "res://common/scenes/board_logic/controller/icons/sara.png"
	$Screen/SpeechDialog.show_dialog("CONTEXT_SPEAKER_SARA", sara_icon, text, current_player.info.player_id, format_args)
	yield($Screen/SpeechDialog, "dialog_finished")

func ask_yes_no(text: String, format_args := {}):
	var current_player = players[player_turn - 1]
	var sara_icon := "res://common/scenes/board_logic/controller/icons/sara.png"
	$Screen/SpeechDialog.show_accept_dialog("CONTEXT_SPEAKER_SARA", sara_icon, text, current_player.info.player_id, format_args)
	return yield($Screen/SpeechDialog, "dialog_option_taken")

func query_range(text: String, minimum: int, maximum: int, start_value: int, format_args := {}):
	var current_player = players[player_turn - 1]
	var sara_icon := "res://common/scenes/board_logic/controller/icons/sara.png"
	$Screen/SpeechDialog.show_query_dialog("CONTEXT_SPEAKER_SARA", sara_icon, text, current_player.info.player_id, minimum, maximum, start_value, format_args)
	return yield($Screen/SpeechDialog, "dialog_option_taken")

# TODO: Provide a tutorial option in the main menu instead of at game creation?
# Then other players wouldn't need to wait for you to finish your tutorial...
func show_tutorial():
	yield(announce("CONTEXT_TUTORIAL_DICE"), "completed")
	yield(announce("CONTEXT_TUTORIAL_SPACES_NORMAL"), "completed")
	yield(announce("CONTEXT_TUTORIAL_SPACES_SPECIAL"), "completed")
	yield(announce("CONTEXT_TUTORIAL_MINIGAMES"), "completed")
	yield(announce("CONTEXT_TUTORIAL_MINIGAMES_FFA"), "completed")
	yield(announce("CONTEXT_TUTORIAL_MINIGAMES_2V2"), "completed")
	yield(announce("CONTEXT_TUTORIAL_MINIGAMES_1V3"), "completed")
	yield(announce("CONTEXT_TUTORIAL_MINIGAMES_SPECIAL"), "completed")
	yield(announce("CONTEXT_TUTORIAL_COOKIES"), "completed")
	yield(announce("CONTEXT_TUTORIAL_CAKES"), "completed")
	yield(announce("CONTEXT_TUTORIAL_END"), "completed")

func get_player_by_player_id(id: int) -> PlayerBoard:
	for player in players:
		if player.info.player_id == id:
			return player
	return null

puppet func _setup_finished():
	# We simulate a continuation of the loading screen until the server is fully set up
	# The server may have loaded the game slower than we did after all
	# This prevents us from rendering an incomplete (and broken) scene
	$Screen/BeforeSetupCurtain.free()

puppet func set_turn(turn: int, max_turn: int):
	$Screen/Turn.text = tr("CONTEXT_LABEL_TURN_NUM").format({"turn": turn, "total": max_turn})

puppet func cake_collected():
	var old_node = get_cake_space()
	yield(old_node.play_cake_collection_animation(), "completed")
	old_node.cake = false
	acknowledge()

puppet func cake_relocated(path: NodePath):
	var new_node = get_node(path)
	if not new_node is NodeBoard or not lobby.is_a_parent_of(new_node):
		# Server is misbehaving
		lobby.leave()
		return
	var old_focus = camera_focus
	camera_focus = new_node
	new_node.cake = true
	yield(self, "_camera_focus_aquired")
	yield(announce("CONTEXT_CAKE_PLACED"), "completed")
	camera_focus = old_focus
	yield(self, "_camera_focus_aquired")
	lobby.cake_space = path
	acknowledge()

func relocate_cake() -> void:
	var cake_nodes: Array = Utility.get_nodes_in_group(lobby, "cake_nodes")
	# Randomly place cake spot on board.
	if cake_nodes.size() > 0:
		if lobby.cake_space:
			var old_node = get_cake_space()
			wait_for_acknowledgement()
			lobby.broadcast(self, "cake_collected", [])
			yield(self, "players_acknowledged")
			old_node.cake = false
			if cake_nodes.size() > 1:
				cake_nodes.remove(cake_nodes.find(old_node))
		var new_node: Node = cake_nodes[randi() % cake_nodes.size()]
		lobby.cake_space = get_path_to(new_node)
		new_node.cake = true

		wait_for_acknowledgement()
		lobby.broadcast(self, "cake_relocated", [lobby.cake_space])
		yield(self, "players_acknowledged")
	yield(get_tree().create_timer(0.0), "timeout")

puppet func next_player(player_turn: int):
	if player_turn < 1 || player_turn > len(players):
		return
	$Screen/SpeechDialog.hide()
	self.player_turn = player_turn
	show_splash()

puppet func splash_ended():
	$Screen/Splash.play("hide")

puppet func select_item(player_id: int):
	if player_id < 1 || player_id > len(players):
		return
	$Screen/ItemSelection.select_item(players[player_id - 1])
	rpc_id(1, "_client_item_selected", yield($Screen/ItemSelection, "item_selected"))

master func _client_item_selected(idx: int):
	var info = lobby.get_player_by_id(player_turn)
	if info.addr.peer_id != multiplayer.get_rpc_sender_id():
		return
	if idx < 0 or idx >= len(players[player_turn - 1].items):
		# Client is misbehaving
		lobby.kick(info.addr.peer_id, "Misbehaving Client")
		return
	emit_signal("item_selected", idx)

func _on_next_player():
	if player_turn <= len(players):
		has_rolled = false
		lobby.broadcast(self, "next_player", [player_turn])
		if players[player_turn - 1].info.is_ai():
			yield(get_tree().create_timer(1.0), "timeout")
			_on_Roll_pressed()
		else:
			# Timer will be deactivated in roll()
			start_timer_for_player(players[player_turn - 1].info.addr)
	else:
		prepare_minigame()

func show_splash():
	var info := lobby.get_player_by_id(player_turn)
	var character := info.character
	$Screen/Splash/Background/Player.texture =\
			PluginSystem.character_loader.load_character_splash(character)
	$Screen/Splash.play("show")
	if info.is_local():
		$Screen/Roll.show()
	else:
		$Screen/Roll.hide()

	camera_focus = players[player_turn - 1]
	$Screen/Dice.hide()

func _on_Roll_pressed() -> void:
	rpc_id(1, "roll")

puppet func item_placed(target: NodePath, item_data: Dictionary, player_id: int):
	var space = get_node(target)
	if not space is NodeBoard or not lobby.is_a_parent_of(space):
		# Server is misbehaving
		lobby.leave()
		return
	var item = Item.deserialize(item_data)
	if not item:
		lobby.leave()
		return
	var player = players[player_id - 1]
	space.trap = item
	space.trap_player = player
	camera_focus = space
	yield(get_tree().create_timer(1), "timeout")
	camera_focus = players[player_id - 1]
	acknowledge()

# Roll for the current player.
mastersync func roll() -> void:
	var info := lobby.get_player_by_id(player_turn)
	if multiplayer.get_rpc_sender_id() != info.addr.peer_id:
		return
	if has_rolled:
		return
	# Timer started in _on_next_player
	cancel_timer()
	has_rolled = true
	lobby.broadcast(self, "splash_ended", [])
	var player = players[player_turn - 1]
	var item: Item
	if not player.info.is_ai():
		start_timer_for_player(player.info.addr)
		rpc_id(info.addr.peer_id, "select_item", player_turn)
		wait_for_select_item = true
		var item_idx: int = yield(self, "item_selected")
		cancel_timer()
		wait_for_select_item = false
		item = player.items[item_idx]
	else:
		item = player.items[randi() % len(player.items)]

	# Remove the item from the inventory if it is consumed.
	if item.is_consumed:
		player.remove_item(item)

	match item.type:
		Item.TYPES.DICE:
			var dice = item.activate(player, self)

			dice = max(dice + player.get_total_roll_modifier(), 0)
			player.roll_modifiers_count_down()
			step_count = dice

			emit_signal("rolled", player, dice)
			lobby.broadcast(self, "rolled", [dice])
		Item.TYPES.PLACABLE:
			start_timer_for_player(player.info.addr)
			$SelectSpaceHelper.select_space(player, item.max_place_distance)
			var selected_space = yield($SelectSpaceHelper, "space_selected")
			cancel_timer()
			selected_space.trap = item
			selected_space.trap_player = player

			wait_for_acknowledgement()
			lobby.broadcast(self, "item_placed", [get_path_to(selected_space), item.serialize(), player.info.player_id])
			yield(self, "players_acknowledged")

			# Use default dice.
			var dice = (randi() % 6) + 1
			step_count = dice

			emit_signal("rolled", player, dice)
			lobby.broadcast(self, "rolled", [dice])
		Item.TYPES.ACTION:
			item.activate(player, self)

			# Use default dice.
			var dice = (randi() % 6) + 1
			step_count = dice

			emit_signal("rolled", player, dice)
			lobby.broadcast(self, "rolled", [dice])
		_:
			push_error("Invalid type: %d (%s != %d)" % [item.type, typeof(item.type), TYPE_INT])

puppet func rolled(dice: int):
	step_count = dice
	$Screen/Stepcounter.text = str(step_count)

func prepare_minigame():
	var blue_team = []
	var red_team = []

	for p in players:
		match p.space.type:
			NodeBoard.NODE_TYPES.BLUE:
				blue_team.push_back(p.info.player_id)
			NodeBoard.NODE_TYPES.RED:
				red_team.push_back(p.info.player_id)
			_:
				if randi() % 2 == 0:
					blue_team.push_back(p.info.player_id)
				else:
					red_team.push_back(p.info.player_id)

	if blue_team.size() < red_team.size():
		var tmp = blue_team
		blue_team = red_team
		red_team = tmp

	var state = Lobby.MinigameState.new()
	state.minigame_teams = [blue_team, red_team]

	match [blue_team.size(), red_team.size()]:
		[4, 0]:
			state.minigame_type = Lobby.MINIGAME_TYPES.FREE_FOR_ALL
			state.minigame_config = PluginSystem.minigame_loader.get_random_ffa()
		[3, 1]:
			state.minigame_type = Lobby.MINIGAME_TYPES.ONE_VS_THREE
			state.minigame_config = PluginSystem.minigame_loader.get_random_1v3()
		[2, 2]:
			state.minigame_type = Lobby.MINIGAME_TYPES.TWO_VS_TWO
			state.minigame_config = PluginSystem.minigame_loader.get_random_2v2()

	lobby.turn += 1
	player_turn = 1
	lobby.minigame_state = state
	lobby.broadcast(self, "show_minigame", [state.encode()])

puppet func show_minigame(encoded_state: Array):
	var state = Lobby.MinigameState.decode(encoded_state)
	lobby.minigame_state = state
	yield(show_minigame_animation(state), "completed")
	show_minigame_info(state)

puppet func select_path():
	create_choose_path_arrows(players[player_turn - 1])

master func path_chosen(idx: int):
	if player_turn >= len(players):
		return
	var player = players[player_turn - 1]
	var info := lobby.get_player_by_id(player_turn)
	if info.addr.peer_id != multiplayer.get_rpc_sender_id():
		return
	if idx < 0 or idx >= player.space.next.size() or not wait_for_path_select:
		# Client is misbehaving
		lobby.kick(info.addr.peer_id, "Misbehaving Client")
		return
	emit_signal("path_chosen", player.space.next[idx])

func create_choose_path_arrows(player: PlayerBoard) -> void:
	var first = null
	var previous = null
	var i := 0
	for node in player.space.next:
		var arrow = preload("res://common/scenes/board_logic/node/arrow/" +\
				"arrow.tscn").instance()
		var dir = node.translation - player.space.translation

		dir = dir.normalized()

		if first != null:
			arrow.previous_arrow = previous
			previous.next_arrow = arrow
		else:
			first = arrow

		arrow.translation = player.space.translation
		arrow.rotation.y = atan2(dir.normalized().x, dir.normalized().z)

		arrow.connect("arrow_activated", self,
				"_on_choose_path_arrow_activated", [i])

		get_parent().add_child(arrow)
		previous = arrow
		i += 1

	first.previous_arrow = previous
	previous.next_arrow = first
	first.selected = true

func _step(player: PlayerBoard, previous_space: NodeBoard, last: bool) -> void:
	# If there are multiple branches.
	if player.space.next.size() > 1:
		if previous_space != player.space:
			update_space(previous_space)
		update_space(player.space)
		previous_space = player.space
		yield(player, "walking_ended")
		if not player.info.is_ai():
			wait_for_path_select = true
			rpc_id(player.info.addr.peer_id, "select_path")
			start_timer_for_player(player.info.addr)
			player.space = yield(self, "path_chosen")
			cancel_timer()
			wait_for_path_select = false
		else:
			player.space = player.space.next[randi() % player.space.next.size()]
			yield(get_tree().create_timer(1), "timeout")
	elif player.space.next.size() == 1:
		player.space = player.space.next[0]

	var stopped := false
	# If player passes a cake-spot.
	if player.space.cake:
		if player.space != previous_space:
			update_space(previous_space)
		update_space(player.space)
		previous_space = player.space
		stopped = true

		yield(player, "walking_ended")
		if not player.info.is_ai():
			# FIXME: There is no await in Godot yet
			# Use signals as a workaround
			# Use await buy_cake(player) when upgrading to Godot 4
			emit_signal("purchase_cake", player)
			yield(self, "cake_purchased")
			# await buy_cake(player)
		else:
			ai_purchase_cake(player)
			yield(get_tree().create_timer(1), "timeout")

	# If player passes a shop space
	if player.space.type == NodeBoard.NODE_TYPES.SHOP:
		if not stopped:
			if player.space != previous_space:
				update_space(previous_space)
			update_space(player.space)
		previous_space = player.space

		yield(player, "walking_ended")
		if not player.info.is_ai():
			start_timer_for_player(player.info.addr)
			$Screen/Shop.player_do_shopping(player)
			yield($Screen/Shop, "shopping_completed")
			cancel_timer()
		else:
			$Screen/Shop.ai_do_shopping(player)
			yield(get_tree().create_timer(1), "timeout")

	# On some circumstances we must not send a movement command, because it will
	# be set during an update_space call.
	#
	# This is either when this is the last step (on a visible space)
	# Or we're right before multiple pathways, a cake or a shop
	var space := player.space
	var last_step := last and space.is_visible_space()
	var next_step_blocking = not last and (space.next.size() > 1 or
			space.cake or space.type == NodeBoard.NODE_TYPES.SHOP)
	if not last_step and not next_step_blocking:
		player._internal_walk_to(player.space, player.space.translation)
	call_deferred("emit_signal", "_step_finished", player.space.is_visible_space(), previous_space)

func land_on_space(player):
	# Activate the item placed onto the node if any.
	if player.space.trap != null and player.space.trap.activate_trap(
		player, player.space.trap_player, self):
		player.space.trap = null

	# Lose cookies if you land on red space.
	match player.space.type:
		NodeBoard.NODE_TYPES.BLUE:
			player.cookies += 3
		NodeBoard.NODE_TYPES.RED:
			player.cookies -= 3
			if player.cookies < 0:
				player.cookies = 0
		NodeBoard.NODE_TYPES.GREEN:
			if len(self.get_signal_connection_list("trigger_event")) > 0:
				emit_signal("trigger_event", player, player.space)
				yield(self, "_event_completed")
			else:
				push_warning("Player stepped on green space, but no board event"
					+ " handler is registered, skipping...")
				yield(get_tree().create_timer(1), "timeout")
		NodeBoard.NODE_TYPES.YELLOW:
			var rewards: Array = lobby.MINIGAME_DUEL_REWARDS.values()
			var reward: int = rewards[randi() % rewards.size()]
			lobby.broadcast(self, "minigame_duel_reward_animation", [reward])
			yield(minigame_duel_reward_animation(reward), "completed")

			var enemy_player: int
			if not player.info.is_ai():
				$Screen/DuelSelection.select(player.info.player_id)
				enemy_player = yield($Screen/DuelSelection, "selected")
			else:
				var players: Array = self.players.duplicate()
				players.erase(player)
				enemy_player = players[randi() % players.size()].info.player_id

			var minigame = PluginSystem.minigame_loader.get_random_duel()
			var state := Lobby.MinigameState.new()
			state.minigame_type = Lobby.MINIGAME_TYPES.DUEL
			state.minigame_config = minigame
			state.minigame_teams = [[enemy_player], [player.info.player_id]]
			lobby.minigame_state = state

			lobby.broadcast(self, "show_minigame", [state.encode()])
			player_turn += 1
			return
		NodeBoard.NODE_TYPES.NOLOK:
			$Screen/SpeechDialog.show_dialog("CONTEXT_NOLOK_NAME", "res://common/scenes/board_logic/controller/icons/nolokicon.png", "CONTEXT_NOLOK_EVENT_START", player.info.player_id)
			yield($Screen/SpeechDialog, "dialog_finished")

			var actions = Global.NOLOK_ACTION_TYPES
			var type = actions.values()[randi() % actions.size()]
			
			var state = null
			var players = []
			
			var dialog_text: String
			var format_args: Dictionary
			
			match type:
				Global.NOLOK_ACTION_TYPES.SOLO_MINIGAME:
					dialog_text = "CONTEXT_NOLOK_MINIGAME_SOLO_MODERATION"
					$Screen/NolokSelection/Content/Selection.text = "CONTEXT_NOLOK_MINIGAME_SOLO"
					state = Global.MinigameState.new()
					state.minigame_type = Global.MINIGAME_TYPES.NOLOK_SOLO
					state.minigame_config = PluginSystem.minigame_loader.get_random_nolok_solo()
					players.append(player.info.player_id)
				Global.NOLOK_ACTION_TYPES.COOP_MINIGAME:
					dialog_text = "CONTEXT_NOLOK_MINIGAME_COOP_MODERATION"
					$Screen/NolokSelection/Content/Selection.text = "CONTEXT_NOLOK_MINIGAME_COOP"
					state = Global.MinigameState.new()
					state.minigame_type = Global.MINIGAME_TYPES.NOLOK_COOP
					state.minigame_config = PluginSystem.minigame_loader.get_random_nolok_coop()
					for player in self.players:
						players.append(player.info.player_id)
				Global.NOLOK_ACTION_TYPES.BOARD_EFFECT:
					# Random negative effect
					match randi() % 2:
						0:
							# Let the player loose cookies depending on rank
							var cookies = [15, 10, 5, 5]
							var rank = _get_player_placement(player)
							
							var stolen_cookies = min(cookies[rank - 1], player.cookies)
							
							# Give them to the last player (that is not yourself)
							var target = null
							for p in self.players:
								if (not target or target.cakes > p.cakes or (target.cakes == p.cakes and target.cookies > p.cookies)) and p != player:
									target = p
							
							player.cookies -= stolen_cookies
							target.cookies += stolen_cookies
							dialog_text = "CONTEXT_NOLOK_LOSE_COOKIES_MODERATION"
							format_args = {"amount": stolen_cookies, "player": target.player_name}
							$Screen/NolokSelection/Content/Selection.text = "CONTEXT_NOLOK_LOSE_COOKIES"
						1:
							# The next 5 rolls of the player are reduced by 2
							player.add_roll_modifier(-2, 5)
							dialog_text = "CONTEXT_NOLOK_ROLL_MODIFIER_MODERATION"
							format_args = {"amount": 2, "duration": 5}
							$Screen/NolokSelection/Content/Selection.text = "CONTEXT_NOLOK_ROLL_MODIFIER"

			$Screen/NolokSelection/AnimationPlayer.play("show")
			yield($Screen/NolokSelection/AnimationPlayer, "animation_finished")
			$Screen/NolokSelection.hide()

			$Screen/SpeechDialog.show_dialog("CONTEXT_NOLOK_NAME", "res://common/scenes/board_logic/controller/icons/nolokicon.png", dialog_text, player.info.player_id, format_args)
			yield($Screen/SpeechDialog, "dialog_finished")

			if state:
				state.minigame_teams = [players, []]
				yield(show_minigame_animation(state), "completed")
				show_minigame_info(state)
				return
		NodeBoard.NODE_TYPES.GNU:
			$Screen/SpeechDialog.show_dialog("CONTEXT_GNU_NAME", "res://common/scenes/board_logic/controller/icons/gnu_icon.png", "CONTEXT_GNU_EVENT_START", player.info.player_id)
			yield($Screen/SpeechDialog, "dialog_finished")
			
			var actions: Array = Global.GNU_ACTION_TYPES.values()
			var type = actions[randi() % actions.size()]
			
			var state = Global.MinigameState.new()
			var players := []
			var dialog_text := ""
			var format_args := {}
			
			match type:
				Global.GNU_ACTION_TYPES.SOLO_MINIGAME:
					var items: Array = PluginSystem.item_loader.get_buyable_items()
					var reward: Item = load(items[randi() % len(items)]).new()
					dialog_text = "CONTEXT_GNU_MINIGAME_SOLO_MODERATION"
					format_args = {"reward": reward.name}
					$Screen/GNUSelection/Content/Selection.text = "CONTEXT_GNU_MINIGAME_SOLO"

					state.minigame_type = Global.MINIGAME_TYPES.GNU_SOLO
					state.minigame_config = PluginSystem.minigame_loader.get_random_gnu_solo()

					Global.minigame_reward = Global.MinigameReward.new()
					Global.minigame_reward.gnu_solo_item_reward = reward

					players.push_back(player.info.player_id)
				Global.GNU_ACTION_TYPES.COOP_MINIGAME:
					dialog_text = "CONTEXT_GNU_MINIGAME_COOP_MODERATION"
					$Screen/GNUSelection/Content/Selection.text = "CONTEXT_GNU_MINIGAME_COOP"
					state.minigame_type = Global.MINIGAME_TYPES.GNU_COOP
					state.minigame_config = PluginSystem.minigame_loader.get_random_gnu_coop()
					for player in self.players:
						players.push_back(player.info.player_id)

			$Screen/GNUSelection/AnimationPlayer.play("show")
			yield($Screen/GNUSelection/AnimationPlayer, "animation_finished")
			$Screen/GNUSelection.hide()

			$Screen/SpeechDialog.show_dialog("CONTEXT_GNU_NAME", "res://common/scenes/board_logic/controller/icons/gnu_icon.png", dialog_text, player.info.player_id, format_args)
			yield($Screen/SpeechDialog, "dialog_finished")

			state.minigame_teams = [players, []]
			yield(show_minigame_animation(state), "completed")
			show_minigame_info(state)
			return

	player_turn += 1
	emit_signal("next_player")

# Moves a player num spaces forward and stops when a cake spot is encountered.
func do_step(player: PlayerBoard, num: int) -> void:
	# Calculates each animation step and sends them to the clients
	var previous_space = player.space
	var i := 0
	while i < num:
		# Await doesn't exist yet in Godot, indirection through signals
		# are used as a workaround
		# When Godot 4 releases, this can be reworked (call await _step(...))
		emit_signal("_calculate_step", player, previous_space, i == num - 1)
		var args = yield(self, "_step_finished")
		# visible?
		if args[0]:
			i += 1
		previous_space = args[1]

	if previous_space != player.space:
		update_space(previous_space)
	if num > 0:
		update_space(player.space)
	yield(player, "walking_ended")
	yield(get_tree().create_timer(0.5), "timeout")
	land_on_space(player)

func update_space(space) -> void:
	var idx := 0
	for player in players:
		if player.space == space:
			var offset = _get_player_offset(player.space, idx)

			var position = player.space.translation + offset
			player._internal_walk_to(player.space, position)
			idx += 1

func show_minigame_info(state) -> void:
	$Screen/MinigameInformation.show_minigame_info(state, players)

func raise_event(name: String, pressed: bool) -> void:
	var event = InputEventAction.new()
	event.action = name
	event.pressed = pressed

	Input.parse_input_event(event)

func _unhandled_input(event: InputEvent) -> void:
	if player_turn <= players.size() and lobby.get_player_by_id(player_turn).is_local():
		if event.is_action_pressed("player%d_ok" % player_turn):
			_on_Roll_pressed()
		elif not players[player_turn - 1].info.is_ai():
			if event.is_action_pressed("player%d_ok" % player_turn):
				raise_event("ui_accept", true)
			elif event.is_action_released("player%d_ok" % player_turn):
				raise_event("ui_accept", false)
			elif event.is_action_pressed("player%d_up" % player_turn):
				raise_event("ui_up", true)
			elif event.is_action_released("player%d_up" % player_turn):
				raise_event("ui_up", false)
			elif event.is_action_pressed("player%d_left" % player_turn):
				raise_event("ui_left", true)
			elif event.is_action_released("player%d_left" % player_turn):
				raise_event("ui_left", false)
			elif event.is_action_pressed("player%d_down" % player_turn):
				raise_event("ui_down", true)
			elif event.is_action_released("player%d_down" % player_turn):
				raise_event("ui_down", false)
			elif event.is_action_pressed("player%d_right" % player_turn):
				raise_event("ui_right", true)
			elif event.is_action_released("player%d_right" % player_turn):
				raise_event("ui_right", false)

func get_players_on_space(space) -> int:
	var num = 0
	for player in players:
		if player.space == space:
			num += 1

	return num

func _get_player_placement(p: Spatial) -> int:
	var placement := 1
	for p2 in players:
		if p2.cakes > p.cakes or p2.cakes == p.cakes and p2.cookies > p.cookies:
			placement += 1
	
	return placement

func _get_player_offset(space: NodeBoard, num := -1) -> Vector3:
	var players_on_space = get_players_on_space(space)
	if num < 0:
		num = players_on_space - 1

	if players_on_space > 1:
		return PLAYER_TRANSLATION[num]
	else:
		return EMPTY_SPACE_PLAYER_TRANSLATION

# This method needs to be called, after an event triggered by landing on a
# green space is fully processed.
func continue() -> void:
	call_deferred("emit_signal", "_event_completed")

# Gets the reference to the node, on which the cake currently can be
# collected
func get_cake_space() -> NodeBoard:
	return get_node(lobby.cake_space) as NodeBoard

func ai_purchase_cake(player):
	var cakes := int(player.cookies / COOKIES_FOR_CAKE)
	var cake_cost = cakes * COOKIES_FOR_CAKE
	player.cookies -= cake_cost
	player.cakes += cakes


func buy_cake(player: PlayerBoard) -> void:
	if player.cookies >= COOKIES_FOR_CAKE:
		if yield(ask_yes_no("CONTEXT_CAKE_WANT_BUY"), "completed"):
			var max_cakes := int(player.cookies / COOKIES_FOR_CAKE)
			var amount := max_cakes
			if amount != 1:
				amount = yield(query_range("CONTEXT_CAKE_BUY_AMOUNT", 1, max_cakes, max_cakes), "completed")
			yield(get_tree().create_timer(0.5), "timeout")
			yield(announce("CONTEXT_CAKE_COLLECTED", {"player": player.name, "amount": amount}), "completed")
			player.cookies -= amount * COOKIES_FOR_CAKE
			player.cakes += amount
			yield(relocate_cake(), "completed")
	else:
		yield(announce("CONTEXT_CAKE_CANT_AFFORD"), "completed")
	# FIXME: obsolete once Godot supports await (Godot 4)
	emit_signal("cake_purchased")

# If we end up on a green space at the end of turn, we execute the board event
# if the board event does a movement, we need to ignore it.
# That's the purpose of this variable.
var _ignore_animation_ended := false

func animation_step(space: NodeBoard, player_id: int) -> void:
	if player_id != player_turn:
		return

	if space.is_visible_space():
		step_count -= 1

	if step_count > 0:
		$Screen/Stepcounter.text = str(step_count)
	else:
		$Screen/Stepcounter.text = ""

func play_space_step_sfx(space: NodeBoard, player_id: int) -> void:
	if player_id == player_turn and space.is_visible_space():
		$StepFX.play()

func _process(delta: float) -> void:
	if camera_focus != null:
		var dir: Vector3 = camera_focus.translation - translation
		if dir.length() > 0.01:
			translation +=\
					CAMERA_SPEED * dir.length() * dir.normalized() * delta
		else:
			emit_signal("_camera_focus_aquired")

# Function that updates the player info shown in the GUI.
func update_player_info() -> void:
	var i := 1

	for p in players:
		var placement = _get_player_placement(p)

		var pos: Label = get_node("Screen/PlayerInfo%d" % i).get_node("Name/Position")
		pos.text = str(placement)
		pos.set("custom_colors/font_color", PLACEMENT_COLORS[placement - 1])
		var info = get_node("Screen/PlayerInfo" + str(i))
		info.get_node("Name/Player").text = p.info.name

		if p.cookies_gui == p.cookies:
			info.get_node("Cookies/Amount").text = str(p.cookies)
		elif p.destination.size() > 0:
			info.get_node("Cookies/Amount").text = str(p.cookies_gui)
		elif p.cookies_gui > p.cookies:
			info.get_node("Cookies/Amount").text = "-" + str(
					p.cookies_gui - p.cookies) + "  " + str(p.cookies_gui)
		else:
			info.get_node("Cookies/Amount").text = "+" + str(
					p.cookies - p.cookies_gui) + "  " + str(p.cookies_gui)

		info.get_node("Cakes/Amount").text = str(p.cakes)
		for j in PLAYER.MAX_ITEMS:
			var item
			if j < p.items.size():
				item = p.items[j]
			var texture_rect = info.get_node("Items/" + str(j))
			if item != null:
				texture_rect.texture = item.icon
			else:
				texture_rect.texture = null

			j += 1

		i += 1

func hide_splash() -> void:
	$Screen/Splash/Background.hide()

func show_minigame_animation(state: Lobby.MinigameState) -> void:
	var i := 1
	for team in state.minigame_teams:
		for player_id in team:
			var character = lobby.get_player_by_id(player_id).character
			var texture = PluginSystem.character_loader.load_character_icon(character)
			$Screen/MinigameTypeAnimation/Root.get_node("Player" + str(i)).texture = texture
			i += 1

	match state.minigame_type:
		Lobby.MINIGAME_TYPES.FREE_FOR_ALL:
			$Screen/MinigameTypeAnimation.play("FFA")
		Lobby.MINIGAME_TYPES.ONE_VS_THREE:
			$Screen/MinigameTypeAnimation.play("1v3")
		Lobby.MINIGAME_TYPES.TWO_VS_TWO:
			$Screen/MinigameTypeAnimation.play("2v2")
		Lobby.MINIGAME_TYPES.DUEL:
			$Screen/MinigameTypeAnimation.play("Duel")

	$Screen/Dice.hide()

	if $Screen/MinigameTypeAnimation.is_playing():
		yield($Screen/MinigameTypeAnimation, "animation_finished")
	else:
		yield(get_tree().create_timer(0), "timeout")

puppet func minigame_duel_reward_animation(reward: int) -> void:
	lobby.minigame_reward = lobby.MinigameReward.new()
	lobby.minigame_reward.duel_reward = reward
	var name := "BUG: Unknown Reward ({0})".format([reward])
	for key in Lobby.MINIGAME_DUEL_REWARDS.keys():
		if Lobby.MINIGAME_DUEL_REWARDS[key] == reward:
			name = key

	if name == "TEN_COOKIES":
		$Screen/DuelReward/Value.text = tr("CONTEXT_LABEL_STEAL_TEN_COOKIES")
	elif name == "ONE_CAKE":
		$Screen/DuelReward/Value.text = tr("CONTEXT_LABEL_STEAL_ONE_CAKE")
	else:
		$Screen/DuelReward/Value.text = name

	$Screen/Dice.hide()

	$Screen/DuelReward.show()
	yield(get_tree().create_timer(2), "timeout")
	$Screen/DuelReward.hide()

func _on_choose_path_arrow_activated(idx: int) -> void:
	rpc_id(1, "path_chosen", idx)
