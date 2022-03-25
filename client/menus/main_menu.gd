extends Control

# Path to the board being used on game start.
var current_player := 0

var lobby: Node

var human_players := 0

func _ready() -> void:
	# Wait with main menu music until audio options have been loaded
	$AudioStreamPlayer.play()
	#var award_type = $BoardSettings/Options/Award/AwardType
	#award_type.add_item("MENU_LABEL_LINEAR", Global.AWARD_TYPE.LINEAR)
	#award_type.add_item("MENU_LABEL_WINNER_TAKES_ALL", Global.AWARD_TYPE.WINNER_ONLY);

	$MainMenu/Buttons/Play.grab_focus()
	load_boards()
	load_characters()

	if false:
		#Lobby.get_lobby().quit_to_menu = false

		$MainMenu.hide()
		$SelectionBoard.show()
		$Animation.play("SelectionBoard")
		if $SelectionBoard/ScrollContainer/Buttons.get_child_count() > 0:
			$SelectionBoard/ScrollContainer/Buttons.get_child(0).grab_focus()
		else:
			$SelectionBoard/Back.grab_focus()

		var i := 1;

		for p in Global.players:
			if p.is_ai:
				continue
			else:
				human_players += 1

			get_node("PlayerInfo" + str(i) + "/Name").text = p.player_name;
			get_node("PlayerInfo" + str(i) + "/Character").text =\
					tr("MENU_LABEL_CHARACTER") + " " + p.character;
			get_node("PlayerInfo" + str(i) + "/Ready").text =\
					"MENU_LABEL_READY"
			get_node("PlayerInfo" + str(i)).visible = true

			i += 1

		current_player = human_players

		lobby.start()

func load_boards() -> void:
	var selection_board_list := $SelectionBoard/ScrollContainer/Buttons as\
			VBoxContainer

	var button_template: PackedScene =\
			preload("res://common/scenes/sound_button/sound_button.tscn")
	for board in PluginSystem.board_loader.get_loaded_boards():
		var board_list_entry: Button = button_template.instance()
		board_list_entry.size_flags_horizontal = SIZE_EXPAND_FILL

		board_list_entry.text = board
		board_list_entry.connect(
				"pressed", self, "_on_board_select", [board_list_entry])

		selection_board_list.add_child(board_list_entry)

func load_characters() -> void:
	var selection_char_list := $SelectionChar/Buttons/VScrollBar/Grid as\
			GridContainer
	var button_template: PackedScene =\
			preload("res://common/scenes/sound_button/sound_button.tscn")
	var character_loader = PluginSystem.character_loader
	for character in character_loader.get_loaded_characters():
		var character_list_entry: Button = button_template.instance()
		character_list_entry.size_flags_horizontal = SIZE_EXPAND_FILL

		character_list_entry.text = character
		character_list_entry.icon = character_loader.load_character_icon(character)
		character_list_entry.expand_icon = true
		character_list_entry.connect("pressed", self, "_on_character_select",
				[character_list_entry])

		selection_char_list.add_child(character_list_entry)

#*** Options menu ***#

func _on_Options_pressed() -> void:
	$Animation.play_backwards("MainMenu")
	yield($Animation, "animation_finished")
	$MainMenu/Buttons.hide()
	$MainMenu/ViewportContainer.hide()
	$OptionsMenu.show()
	$Animation.play("OptionsMenu")
	$OptionsMenu/OptionsMenu/Menu/Back.grab_focus()

func _on_OptionsMenu_quit() -> void:
	$OptionsMenu/OptionsMenu/Menu/Back.disabled = true
	$Animation.play_backwards("OptionsMenu")
	yield($Animation, "animation_finished")
	$OptionsMenu.hide()
	$MainMenu/Buttons.show()
	$OptionsMenu/OptionsMenu/Menu/Back.disabled = false
	$MainMenu/ViewportContainer.show()
	$Animation.play("MainMenu")
	$MainMenu/Buttons/Options.grab_focus()

#*** Amount of players menu ***#

func _on_PopupDialog_confirmed() -> void:
	remote_server($PopupDialog/VBoxContainer/LineEdit.text)

func remote_server(ip) -> void:
	var players := 1
	var game := Global.connect_remote_server(ip, 7634)
	yield(get_tree().network_peer, "connection_succeeded")
	lobby = yield(game.create_lobby(players), "completed")
	if not lobby:
		Global.destroy_local_server()
		_on_Amount_Of_Players_Back_pressed()
		return
	lobby.connect("player_info_updated", self, "_on_player_info_updated")
	lobby.set_current_scene(self)
	human_players = players
	for i in range(1, human_players + 1):
		get_node("PlayerInfo{0}".format([i])).show()
	$Animation.play_backwards("MainMenu")
	yield($Animation, "animation_finished")
	$MainMenu.hide()
	$SelectionChar.show()
	$Animation.play("SelectionChar")
	if $SelectionChar/Buttons/VScrollBar/Grid.get_child_count() > 0:
		$SelectionChar/Buttons/VScrollBar/Grid.get_child(0).grab_focus()
	else:
		$SelectionChar/Buttons/Back.grab_focus()

func _select_player_amount(players) -> void:
	var game := Global.create_local_server()
	yield(get_tree().network_peer, "connection_succeeded")
	lobby = yield(game.create_lobby(players), "completed")
	if not lobby:
		Global.destroy_local_server()
		_on_Amount_Of_Players_Back_pressed()
		return
	lobby.connect("player_info_updated", self, "_on_player_info_updated")
	lobby.set_current_scene(self)
	human_players = players
	for i in range(1, human_players + 1):
		get_node("PlayerInfo{0}".format([i])).show()

	$Animation.play_backwards("SelectionPlayers")
	yield($Animation, "animation_finished")
	$SelectionPlayers.hide()
	$SelectionChar.show()
	$Animation.play("SelectionChar")
	if $SelectionChar/Buttons/VScrollBar/Grid.get_child_count() > 0:
		$SelectionChar/Buttons/VScrollBar/Grid.get_child(0).grab_focus()
	else:
		$SelectionChar/Buttons/Back.grab_focus()

func _on_Play_pressed() -> void:
	$Animation.play_backwards("MainMenu")
	yield($Animation, "animation_finished")
	$MainMenu/Buttons.hide()
	$SelectionPlayers.show()
	$Animation.play("SelectionPlayers")
	$SelectionPlayers/Buttons/VScrollBar/Grid/One.grab_focus()

func _on_Play2_pressed() -> void:
	$PopupDialog.popup_centered()

func _on_Amount_Of_Players_Back_pressed() -> void:
	$SelectionPlayers/Buttons/Back.disabled = true
	$Animation.play_backwards("SelectionPlayers")
	yield($Animation, "animation_finished")
	$SelectionPlayers.hide()
	$MainMenu/Buttons.show()
	$SelectionPlayers/Buttons/Back.disabled = false
	$Animation.play("MainMenu")
	$MainMenu/Buttons/Play.grab_focus()

#*** Character selection menu ***#

func _on_player_info_updated(playerinfo):
	for player in playerinfo:
		if player.addr.peer_id == multiplayer.get_network_unique_id() and player.character:
			character_selected(player.addr.idx, player.character)

func character_selected(idx: int, character: String):
	get_node("PlayerInfo" + str(idx + 1) + "/Character").text =\
			tr("MENU_LABEL_CHARACTER") + " " + character
	get_node("PlayerInfo" + str(idx + 1) + "/Ready").text =\
			"MENU_LABEL_READY"

func _on_character_select(target: Button) -> void:
	lobby.select_character(current_player, target.text)
	current_player += 1

# TODO: synchronize this with remote
#	if PluginSystem.character_loader.get_loaded_characters().size() >=\
#			Global.amount_of_players:
#		target.disabled = true

	if current_player == human_players:
		$Animation.play_backwards("SelectionChar")
		yield($Animation, "animation_finished")
		$SelectionChar.hide()
		$SelectionBoard.show()
		$Animation.play("SelectionBoard")
		if $SelectionBoard/ScrollContainer/Buttons.get_child_count() > 0:
			$SelectionBoard/ScrollContainer/Buttons.get_child(0).grab_focus()
		else:
			$SelectionBoard/Back.grab_focus()

	$SelectionChar/Title.text =\
			"MENU_LABEL_SELECT_CHARACTER_PLAYER_" + str(current_player + 1)

func _on_SelectionChar_Back_pressed() -> void:
	Global.destroy_local_server()
	$SelectionChar/Buttons/Back.disabled = true
	$Animation.play_backwards("SelectionChar")
	yield($Animation, "animation_finished")
	$SelectionChar.hide()
	$SelectionPlayers.show()
	$SelectionChar/Buttons/Back.disabled = false
	$Animation.play("SelectionPlayers")
	$SelectionPlayers/Buttons/VScrollBar/Grid/One.grab_focus()

	current_player = 0

	$SelectionChar/Title.text = "MENU_LABEL_SELECT_CHARACTER_PLAYER_1"

	for i in range(1, 5):
		get_node("PlayerInfo" + str(i) + "/Character").text =\
				"MENU_LABEL_CHARACTER"
		get_node("PlayerInfo" + str(i) + "/Ready").text =\
				"MENU_LABEL_NOT_READY_ELLIPSIS"
		get_node("PlayerInfo" + str(i)).hide()

	# Reenable all characters.
	for child in $SelectionChar/Buttons/VScrollBar/Grid.get_children():
		child.disabled = false

#*** Board selection menu ***#

func _on_board_select(target: Button) -> void:
	lobby.select_board(target.get_text())
	#board = board_loader.get_board_path(target.get_text())

	$Animation.play_backwards("SelectionBoard")
	yield($Animation, "animation_finished")
	$SelectionBoard.hide()
	$BoardSettings.show()
	$Animation.play("BoardSettings")
	$BoardSettings/Start.grab_focus()

	var cake_cost: int = 30
	var turns: int = 10

	$BoardSettings/Options/CakeCost/SpinBox.value = cake_cost
	$BoardSettings/Options/Turns/SpinBox.value = turns

func _on_Selection_Back_pressed() -> void:
	$SelectionBoard/Back.disabled = true
	$Animation.play_backwards("SelectionBoard")
	yield($Animation, "animation_finished")
	$SelectionBoard.hide()
	$SelectionBoard/Back.disabled = false
	$Animation.play("SelectionChar")
	current_player = 0
	$SelectionChar/Title.text = "MENU_LABEL_SELECT_CHARACTER_PLAYER_1"

	for i in range(1, 5):
		get_node("PlayerInfo" + str(i) + "/Ready").text =\
				"MENU_LABEL_NOT_READY_ELLIPSIS"

	# Reenable all characters.
	for child in $SelectionChar/Buttons/VScrollBar/Grid.get_children():
		child.disabled = false

	if $SelectionChar/Buttons/VScrollBar/Grid.get_child_count() > 0:
		$SelectionChar/Buttons/VScrollBar/Grid.get_child(0).grab_focus()
	else:
		$SelectionChar/Buttons/Back.grab_focus()

#*** Load game menu ***#

func _on_Load_pressed() -> void:
	var savegame_template: PackedScene =\
			preload("res://client/savegames/savegame_entry.tscn")
	for i in Global.savegame_loader.get_num_savegames():
		var savegame_entry := savegame_template.instance() as Control
		var savegame: SaveGameLoader.SaveGame =\
				Global.savegame_loader.get_savegame(i)
		savegame_entry.get_node("Load").text = savegame.name

		savegame_entry.get_node("Load").connect("pressed", self,
				"_on_SaveGame_Load_pressed", [savegame])
		savegame_entry.get_node("Delete").connect("pressed", self,
				"_on_SaveGame_Delete_pressed", [savegame, savegame_entry])

		$LoadGameMenu/ScrollContainer/Saves.add_child(savegame_entry)

	$Animation.play_backwards("MainMenu")
	yield($Animation, "animation_finished")
	$MainMenu/Buttons.hide()
	$LoadGameMenu.show()
	$Animation.play("LoadGameMenu")
	if $LoadGameMenu/ScrollContainer/Saves.get_child_count() > 0:
			$LoadGameMenu/ScrollContainer/Saves.\
					get_child(0).get_child(0).grab_focus()
	else:
		$LoadGameMenu/Back.grab_focus()

func _on_SaveGame_Load_pressed(savegame: SaveGameLoader.SaveGame) -> void:
	Global.load_board_from_savegame(savegame)

func _on_SaveGame_Delete_pressed(savegame: SaveGameLoader.SaveGame,
		node: Control) -> void:
	var index: int = node.get_index()
	node.queue_free()
	$LoadGameMenu/ScrollContainer/Saves.remove_child(node)

	var num_children: int =\
			$LoadGameMenu/ScrollContainer/Saves.get_child_count()
	if num_children > 0:
		# warning-ignore:narrowing_conversion
		$LoadGameMenu/ScrollContainer/Saves.get_child(
				min(index, num_children - 1)).get_child(0).grab_focus()
	else:
		$LoadGameMenu/Back.grab_focus()

	Global.savegame_loader.delete_savegame(savegame)

func _on_LoadGame_Back_pressed() -> void:
	for i in $LoadGameMenu/ScrollContainer/Saves.get_children():
		i.queue_free()

	$LoadGameMenu/Back.disabled = true
	$Animation.play_backwards("LoadGameMenu")
	yield($Animation, "animation_finished")
	$LoadGameMenu.hide()
	$MainMenu/Buttons.show()
	$LoadGameMenu/Back.disabled = false
	$Animation.play("MainMenu")
	$MainMenu/Buttons/Load.grab_focus()

func _on_Quit_pressed() -> void:
	get_tree().quit()

func _on_BoardSettings_Back_pressed():
	$BoardSettings/Back.disabled = true
	$Animation.play_backwards("BoardSettings")
	yield($Animation, "animation_finished")
	$BoardSettings.hide()
	$SelectionBoard.show()
	$BoardSettings/Back.disabled = false
	$Animation.play("SelectionBoard")

	if $SelectionBoard/ScrollContainer/Buttons.get_child_count() > 0:
		$SelectionBoard/ScrollContainer/Buttons.get_child(0).grab_focus()
	else:
		$SelectionBoard/Back.grab_focus()

func _on_BoardSettings_Start_pressed():
	lobby.start()

func _on_Screenshots_pressed():
	OS.shell_open("file://{0}/screenshots".format([OS.get_user_data_dir()]))


func _on_AnimationPlayer_animation_finished(_anim_name: String) -> void:
	yield(get_tree().create_timer(5), "timeout")
	$MainMenu/ViewportContainer/Viewport/tux/AnimationPlayer.play()
	$MainMenu/ViewportContainer/Viewport/tux/AnimationPlayer2.play()
