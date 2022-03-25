extends KinematicBody

const MOVEMENT_SPEED = 2.5

var info: Lobby.PlayerInfo

var plants = 0

var movement = Vector3()

var is_walking = false

var input_disabled

var plant_spots

var current_destination = null

func _ready():
	set_network_master(info.addr.peer_id)
	if get_parent().lobby.minigame_state.minigame_type == Lobby.MINIGAME_TYPES.DUEL:
		plant_spots = [$"../Area2", $"../Area4"]
	else:
		plant_spots = [$"../Area1", $"../Area2", $"../Area3", $"../Area4"]

func has_player(colliders, blacklist):
	for collider in colliders:
		if not blacklist.has(collider) and collider.is_in_group("players"):
			return true
	
	return false

func _physics_process(delta):
	if not is_network_master():
		return
	var dir = Vector3()
	
	if not input_disabled:
		if not info.is_ai():
			dir.x = Input.get_action_strength("player%d_up" % info.player_id) - Input.get_action_strength("player%d_down" % info.player_id)
			dir.z = Input.get_action_strength("player%d_right" % info.player_id) - Input.get_action_strength("player%d_left" % info.player_id)
		else:
			if current_destination == null or has_player(current_destination.get_overlapping_bodies(), [self]):
				var spots = []
				
				for plant in plant_spots:
					var colliders = plant.get_overlapping_bodies()
					# Dont blacklist self beause the colliders might not have been updated yet.
					# If everything is occupied, the AI will wait a turn
					if not has_player(colliders, []):
						spots.append(plant)
				
				if not spots.empty():
					current_destination = spots[randi() % spots.size()]
			
			if current_destination:
				var destination_vec = current_destination.translation - self.translation
				
				if destination_vec.length_squared() > 0.01:
					dir = destination_vec.normalized()
	else:
		dir = current_destination - translation
		if dir.length_squared() > pow(delta, 2) + 0.01:
			dir = Vector3(dir.x, 0, dir.z).normalized()
		else:
			dir = Vector3()
			rotation = Vector3(0, -PI/2, 0)
	
	movement += Vector3(0, -9.81, 0) * delta
	move_and_slide(movement + dir * MOVEMENT_SPEED, Vector3(0, 1, 0))
	
	if dir.length_squared() > 0:
		rotation.y = atan2(dir.x, dir.z)
	
	if dir.length_squared() > 0 and not is_walking:
		play_animation("run")
		is_walking = true
	elif dir.length_squared() == 0 and is_walking:
		play_animation("idle")
		is_walking = false
	
	get_parent().lobby.broadcast_unreliable(self, "position_updated", [translation, rotation, is_walking])
	if is_on_floor():
		movement = Vector3()

puppet func position_updated(trans: Vector3, rot: Vector3, walking: bool):
	if not is_walking and walking:
		play_animation("run")
	elif is_walking and not walking:
		play_animation("idle")
	translation = trans
	rotation = rot
	is_walking = walking

func play_animation(name):
	$Model.play_animation(name)
