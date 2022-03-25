extends KinematicBody

const SPEED = 5
const JUMP_POWER = 8
const GRAVITY = 18

enum State {
	IDLE,
	RUN,
	JUMP
}

var info: Lobby.PlayerInfo

var acceleration := Vector3(0, 0, 0)
var state = State.IDLE

var ai_current_waypoint: Spatial = null
var ai_rand_start: float

func _ready():
	set_network_master(info.addr.peer_id)
	$CameraTracker.set_as_toplevel(true)
	
	if info.is_ai():
		ai_current_waypoint = $"../Ground/Waypoint"
		ai_rand_start = randf()

puppet func position_updated(trans: Vector3, rot: Vector3, new_state):
	self.translation = trans
	self.rotation = rot
	$CameraTracker.translation.x = self.translation.x
	$CameraTracker.translation.z = self.translation.z
	if state != new_state:
		state = new_state
		match state:
			State.IDLE:
				$Model.play_animation("idle")
			State.RUN:
				$Model.play_animation("run")
			State.JUMP:
				$Model.play_animation("jump")

func calc_movement(previous: float, next: float) -> float:
	if is_on_floor():
		return next
	elif sign(previous) == sign(next):
		return clamp(next, min(previous, 0), max(previous, 0))
	else:
		return previous * 0.9

func _physics_process(delta):
	if not info.is_local():
		return
	
	ai_rand_start -= delta
	if ai_rand_start > 0:
		return
	var jump = false
	if not info.is_ai():
		acceleration.x = calc_movement(acceleration.x, (Input.get_action_strength("player%d_right" % info.player_id) - Input.get_action_strength("player%d_left" % info.player_id)) * SPEED)
		acceleration.z = calc_movement(acceleration.z, (Input.get_action_strength("player%d_down" % info.player_id) - Input.get_action_strength("player%d_up" % info.player_id)) * SPEED)
		jump = Input.is_action_pressed("player%d_action1" % info.player_id)
	else:
		var dir: Vector3 = ai_current_waypoint.global_transform.origin - translation
		dir.y = 0
		
		if dir.length() < randf() * 0.5:
			jump = true
			ai_current_waypoint = ai_current_waypoint.get_node(ai_current_waypoint.get_nodes()[0])
		
		if abs(dir.x) < 0.05:
			dir.x = 0
		if abs(dir.z) < 0.05:
			dir.z = 0
		
		dir = dir.normalized()
		dir.x = dir.x * SPEED
		dir.z = dir.z * SPEED
		acceleration.x = dir.x
		acceleration.z = dir.z

	if acceleration.x or acceleration.z:
		if state == State.IDLE:
			$Model.play_animation("run")
			state = State.RUN
		$Model.rotation.y = atan2(acceleration.x, acceleration.z)
	elif state == State.RUN:
		$Model.play_animation("idle")
		state = State.IDLE
	
	if is_on_floor():
		if state == State.JUMP:
			if acceleration.x:
				$Model.play_animation("run")
				state = State.RUN
			else:
				$Model.play_animation("idle")
				state = State.IDLE
		else:
			acceleration.y = 0
			if jump:
				acceleration.y = JUMP_POWER
				$Model.play_animation("jump")
				state = State.JUMP
	acceleration.y -= GRAVITY * delta
	
	move_and_slide(acceleration + get_floor_velocity() * delta, Vector3(0, 1, 0), true)
	get_parent().lobby.broadcast_unreliable(self, "position_updated", [self.translation, self.rotation, self.state])
	
	$CameraTracker.translation.x = self.translation.x
	$CameraTracker.translation.z = self.translation.z
