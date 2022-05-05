extends "../common.gd"

func setup_scene():
	var i := 0
	for p in lobby.playerstates:
		i += 1
		var player_id = p.info.player_id
		var node: Position3D = get_node("ViewportContainer/Viewport/Placement" + str(i))
		if lobby.minigame_summary.placement:
			load_character(player_id, node, "happy")
		else:
			load_character(player_id, node, "sad")
		
		var ui_container: Control = node.get_node("VBoxContainer")
		ui_container.get_node("ContinueCheck").player_id = player_id
		var cookie_text = ui_container.get_node("CookieText")
		cookie_text.total_cookies = p.cakes
		cookie_text.cookies = -lobby.minigame_summary.reward[i - 1]
		position_beneath(node, ui_container)

func _ready():
	setup_scene()
	if not lobby.minigame_summary.placement and not multiplayer.is_network_server():
		$Background/AudioStreamPlayer.stream = preload("res://assets/sounds/minigame_end_screen/stuxparty_lossjingle.ogg")
