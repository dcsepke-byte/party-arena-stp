extends "../common.gd"

func setup_scene():
	var i := 0
	var is_tie: bool = len(lobby.minigame_summary.placement) == 1
	for p in lobby.minigame_summary.placement:
		for player_id in p:
			i += 1
			var node: Position3D = get_node("ViewportContainer/Viewport/Placement" + str(i))
			load_character(player_id, node, "happy" if i == 1 and not is_tie else "sad")
			
			var ui_container: Control = node.get_node("VBoxContainer")
			ui_container.get_node("ContinueCheck").player_id = player_id
			var cookie_text = ui_container.get_node("CookieText")
			match lobby.minigame_reward.duel_reward:
				lobby.MINIGAME_DUEL_REWARDS.ONE_CAKE:
					cookie_text.icon = preload("res://common/scenes/board_logic/controller/icons/cake.png")
					cookie_text.total_cookies = lobby.get_playerstate(player_id).cakes
				lobby.MINIGAME_DUEL_REWARDS.TEN_COOKIES:
					cookie_text.total_cookies = lobby.get_playerstate(player_id).cookies
				_:
					assert(false, "Invalid duel reward: {0}".format([lobby.minigame_reward.duel_reward]))
			position_beneath(node, ui_container)
			if not is_tie:
				if i == 1:
					cookie_text.cookies = lobby.minigame_summary.reward
				else:
					cookie_text.cookies = -lobby.minigame_summary.reward
	if not is_tie:
		position_above($ViewportContainer/Viewport/Placement1, $ViewportContainer/Viewport/Placement1/WinnerText)
	else:
		$ViewportContainer/Viewport/Placement1/WinnerText.hide()

func _ready():
	setup_scene()
