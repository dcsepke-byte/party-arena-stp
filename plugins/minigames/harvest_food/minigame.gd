extends Spatial

var lobby: Lobby

const ROTTEN_PLANTS = [
						preload("res://plugins/minigames/harvest_food/plants/carrot_rotten.tscn"),
						preload("res://plugins/minigames/harvest_food/plants/radish_rotten.tscn"),
						preload("res://plugins/minigames/harvest_food/plants/potato_rotten.tscn")
					  ]
const NORMAL_PLANTS = [
						preload("res://plugins/minigames/harvest_food/plants/carrot.tscn"), preload("res://plugins/minigames/harvest_food/plants/carrot.tscn"),
						preload("res://plugins/minigames/harvest_food/plants/carrot.tscn"), preload("res://plugins/minigames/harvest_food/plants/radish.tscn"),
						preload("res://plugins/minigames/harvest_food/plants/carrot.tscn"), preload("res://plugins/minigames/harvest_food/plants/potato.tscn")
					  ]

var rounds = 5

var plants
var rotten_index

func _enter_tree() -> void:
	self.lobby = Lobby.get_lobby(self)

func _ready():
	if lobby.minigame_state.minigame_type != Lobby.MINIGAME_TYPES.DUEL:
		plants = [$Area1, $Area2, $Area3, $Area4]
	else:
		plants = [$Area2, $Area4]
		rounds = 3
		
		$Area1.queue_free()
		$Area3.queue_free()
	if multiplayer.is_network_server():
		spawn_plants()
	else:
		$Timer.disconnect("timeout", self, "_on_Timer_timeout")

func spawn_plants():
	rotten_index = randi() % plants.size()
	
	var idx := []
	for i in range(plants.size()):
		var plant
		if i == rotten_index:
			idx.append(randi() % ROTTEN_PLANTS.size())
			plant = ROTTEN_PLANTS[idx[-1]].instance()
		else:
			idx.append(randi() % NORMAL_PLANTS.size())
			plant = NORMAL_PLANTS[idx[-1]].instance()
		
		plants[i].add_child(plant)
	# TODO: this exposes which plant is rotten to the client, allowing to "cheat"
	# Will need to be fixed when this minigame is reworked
	lobby.broadcast(self, "_client_spawn_plants", [idx, rotten_index])
	$Timer.start()

puppet func _client_spawn_plants(idx: Array, rotten_index: int):
	self.rotten_index = rotten_index
	for i in range(plants.size()):
		var plant
		if i == rotten_index:
			plant = ROTTEN_PLANTS[idx[i]].instance()
		else:
			plant = NORMAL_PLANTS[idx[i]].instance()
		
		plants[i].add_child(plant)
	$Timer.start()

puppet func round_finished():
	$Timer.stop()
	# Move every player in front of the spot
	$Player1.input_disabled = true
	$Player1.current_destination = $Player1.translation - $Player1.translation.normalized()
	$Player2.input_disabled = true
	$Player2.current_destination = $Player2.translation - $Player2.translation.normalized()
	if lobby.minigame_state.minigame_type != Lobby.MINIGAME_TYPES.DUEL:
		$Player3.input_disabled = true
		$Player3.current_destination = $Player3.translation - $Player3.translation.normalized()
		$Player3.rotation = Vector3(0, -PI/2, 0)
		$Player4.input_disabled = true
		$Player4.current_destination = $Player4.translation - $Player4.translation.normalized()
		$Player4.rotation = Vector3(0, -PI/2, 0)
	
	for i in range(plants.size()):
		var colliders = plants[i].get_overlapping_bodies()
		
		if i != rotten_index:
			for collider in colliders:
				if collider.is_in_group("players"):
					collider.play_animation("happy")
		else:
			for collider in colliders:
				if collider.is_in_group("players"):
					collider.play_animation("sad")
					var player := lobby.get_player_by_id(collider.info.player_id)
					$Screen/Message.text = tr("HARVEST_FOOD_SELECT_ROTTEN_PLANT_MSG").format({"player": player.name})
		
		var animationplayer = plants[i].get_node("Plant/AnimationPlayer")
		animationplayer.play("show")

puppet func reset():
	$Player1.input_disabled = false
	$Player1.play_animation("idle")
	$Player1.translation = Vector3(-1, 0, -1)
	$Player1.current_destination = null
	$Player2.input_disabled = false
	$Player2.play_animation("idle")
	$Player2.translation = Vector3(1, 0, -1)
	$Player2.current_destination = null
	if lobby.minigame_state.minigame_type != Lobby.MINIGAME_TYPES.DUEL:
		$Player3.input_disabled = false
		$Player3.play_animation("idle")
		$Player3.translation = Vector3(1, 0, 1)
		$Player3.current_destination = null
		$Player4.input_disabled = false
		$Player4.play_animation("idle")
		$Player4.translation = Vector3(-1, 0, 1)
		$Player4.current_destination = null
	
	$Screen/Message.text = ""
	
	for plant in plants:
		var model = plant.get_node("Plant")
		
		plant.remove_child(model)
		model.queue_free()

func _on_Timer_timeout():
	for i in range(plants.size()):
		var colliders = plants[i].get_overlapping_bodies()
		
		if i != rotten_index:
			for collider in colliders:
				if collider.is_in_group("players"):
					collider.plants += 1
	rounds -= 1
	
	lobby.broadcast(self, "round_finished")
	
	# Update scores
	$Screen/ScoreOverlay.set_score($Player1.info.player_id, $Player1.plants)
	$Screen/ScoreOverlay.set_score($Player2.info.player_id, $Player2.plants)
	if lobby.minigame_state.minigame_type != Lobby.MINIGAME_TYPES.DUEL:
		$Screen/ScoreOverlay.set_score($Player3.info.player_id, $Player3.plants)
		$Screen/ScoreOverlay.set_score($Player4.info.player_id, $Player4.plants)
	# Wait 5 seconds
	yield(get_tree().create_timer(5.0), "timeout")
	
	reset()
	lobby.broadcast(self, "reset")
	
	if rounds > 0:
		spawn_plants()
	else:
		match lobby.minigame_state.minigame_type:
			Lobby.MINIGAME_TYPES.FREE_FOR_ALL:
				lobby.minigame_win_by_points([$Player1.plants, $Player2.plants, $Player3.plants, $Player4.plants])
			Lobby.MINIGAME_TYPES.DUEL:
				lobby.minigame_win_by_points([$Player1.plants, $Player2.plants])
			Lobby.MINIGAME_TYPES.TWO_VS_TWO:
				lobby.minigame_team_win_by_points([$Player1.plants + $Player2.plants, $Player3.plants + $Player4.plants])

func _client_process(_delta):
	$Screen/Time.text = str(stepify($Timer.time_left, 0.01))
