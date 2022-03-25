extends Spatial

var info: Lobby.PlayerInfo

var paddle_cooldown := 0.0

export var force_dir: Vector3
export var flip_paddle: bool

func _ready():
	if info.is_ai() and multiplayer.is_network_server():
		paddle_cooldown = randf()
	if flip_paddle:
		$"Scene Root".rotation.y *= -1
		$"Scene Root".scale.x *= -1
		$"Scene Root".translation.x *= -1

puppet func fired():
	$Model.play_animation("punch")
	$Model.play_animation("idle")
	$AnimationPlayer.play("paddle")

mastersync func fire():
	if info.addr.peer_id != multiplayer.get_rpc_sender_id():
		return
	if get_parent().fire(self.translation, force_dir) and paddle_cooldown == 0:
		get_parent().lobby.broadcast(self, "fired")
		paddle_cooldown = 1 if not info.is_ai() else 2

func _server_process(delta: float):
	paddle_cooldown = max(0, paddle_cooldown - delta)

func _process(delta: float):
	if not info.is_local():
		return
	if not info.is_ai():
		if Input.is_action_just_pressed("player%d_action1" % info.player_id):
			rpc_id(1, "fire")
	else:
		var pos = get_parent().translation
		var rot = get_parent().rotation_degrees
		
		if (rot.y > 20 and force_dir.x > 0) or (rot.y < -20 and force_dir.x < 0):
			return
		
		var rocks = []
		for rock in get_tree().get_nodes_in_group("rock"):
			if rock.translation.z < pos.z + 10 and rock.translation.z > pos.z and abs(rock.translation.x - pos.x) < 6:
				rocks.append(rock)
		
		if len(rocks) == 0:
			rpc_id(1, "fire")
			return
		
		for rock in rocks:
			if rock.translation.x - pos.x >= -0.1 and force_dir.x < 0:
				rpc_id(1, "fire")
				return
			elif rock.translation.x - pos.x < -0.1 and force_dir.x > 0:
				rpc_id(1, "fire")
				return
