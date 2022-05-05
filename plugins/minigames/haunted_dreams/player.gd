extends KinematicBody

const SPEED := 3

var info: Lobby.PlayerInfo

func _ready():
	set_network_master(info.addr.peer_id)

func _process(_delta):
	if not info.is_local():
		return
	
	var dir: Vector3
	if not info.is_ai():
		dir.x = Input.get_action_strength("player%d_right" % info.player_id) - Input.get_action_strength("player%d_left" % info.player_id)
		dir.z = Input.get_action_strength("player%d_down" % info.player_id) - Input.get_action_strength("player%d_up" % info.player_id)
	else:
		var target
		var dist = INF
		for ghost in Utility.get_nodes_in_group(get_parent(), "ghost"):
			var ndist = (ghost.translation - self.translation).length_squared()
			if ghost.translation.length_squared() < 25 and dist > ndist:
				target = ghost
				dist = ndist
		
		if target:
			var array = Array(get_parent().get_simple_path(self.translation, target.translation))
			dir = (array[1] - self.translation).normalized() * SPEED
			dir.y = 0
	
	var animation := "idle"
	if dir.length_squared() > 0:
		dir = dir.normalized() * SPEED
		rotation.y = atan2(dir.x, dir.z)
		animation = "run"
	
	$Model.play_animation(animation)
	move_and_slide(dir + Vector3(0, -1, 0))
	get_parent().lobby.broadcast_unreliable(self, "position_updated", [self.translation, rotation, animation])

puppet func position_updated(trans, rot, anim):
	self.translation = trans
	self.rotation = rot
	$Model.play_animation(anim)
