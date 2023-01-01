extends Spatial

const MAX_KNOCKOUT := 3
var knocked_out := 0

var lobby: Lobby

var box_counter := 0
var minigame_time := 20.0

var winner := -1

func _enter_tree() -> void:
	lobby = Lobby.get_lobby(self)

puppet func _client_win():
	$Screen/Time.hide()
	$Screen/Label.show()

func win(team: int):
	lobby.broadcast(self, "_client_win")
	winner = team
	$EndTimer.start()

func _process(delta: float):
	if winner != -1:
		return
	
	minigame_time -= delta
	if minigame_time <= 0:
		minigame_time = 0
		if multiplayer.is_network_server():
			win(0)
		
	$Screen/Time.text= str(stepify(minigame_time, 0.1))

func knockout():
	assert (multiplayer.is_network_server())
	if winner != -1:
		return
	
	knocked_out += 1
	if knocked_out == MAX_KNOCKOUT:
		win(1)

func _on_EndTimer_timeout():
	lobby.minigame_team_win(winner)

func _on_Countdown_finish():
	$Screen/Time.show()

func _on_SpawnTimer_timeout():
	if winner != -1:
		return
	if not multiplayer.is_network_server():
		return
	
	var pos := Vector3(rand_range(-2.5, 2.5), 5, rand_range(-2.5, -0.5))
	_spawn_box(pos)
	lobby.broadcast(self, "_spawn_box", [pos])

puppet func _spawn_box(pos: Vector3):
	var box = preload("res://plugins/minigames/bowling/box.tscn").instance()
	# Prevent desync issues
	# Generate a unique name, so that the names on the client and the server
	# will always match
	box.name = "Box" + str(box_counter)
	box.translation = pos
	add_child(box)
	
	box_counter += 1

puppet func die(player_id: int, movement: Vector3):
	for player in Utility.get_nodes_in_group(self, "players"):
		if player.info.player_id == player_id:
			player.state = player.STATE.DEAD
			player.movement = movement
