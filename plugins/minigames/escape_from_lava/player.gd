extends KinematicBody

const SPEED = 4
const GRAVITY = 9.8
const GRAVITY_DIR = Vector3(0, -1, 0)

var info: Lobby.PlayerInfo

var movement = Vector3()

onready var ai_waypoint = get_node("../Navigation/Waypoint")
onready var lobby := Lobby.get_lobby(self)

enum STATE {
	IDLE,
	RUNNING,
	DEAD
}

var state = STATE.IDLE

func _ready():
	set_network_master(info.addr.peer_id)

func _process(delta):
	_do_process(delta)

# Hack to enable overriding _process in inheritance cases
func _do_process(delta):
	if not info.is_local() or state == STATE.DEAD:
		return
	var dir = Vector3()
	if not info.is_ai():
		dir.x = Input.get_action_strength("player%d_left" % info.player_id) - Input.get_action_strength("player%d_right" % info.player_id)
		dir.z = Input.get_action_strength("player%d_up" % info.player_id) - Input.get_action_strength("player%d_down" % info.player_id)
	elif info.is_ai():
		dir = ai_waypoint.translation - self.translation
		dir = Vector3(dir.x, 0, dir.z)
		
		if dir.length_squared() < 0.1 and ai_waypoint.nodes and ai_waypoint.nodes.size() > 0:
			var index = randi() % ai_waypoint.nodes.size()
			ai_waypoint = ai_waypoint.get_node(ai_waypoint.nodes[index])
	
	if dir.length_squared() > 0:
		dir = dir.normalized()
		rotation.y = atan2(dir.x, dir.z)
		if state == STATE.IDLE:
			state = STATE.RUNNING
	elif dir.length_squared() == 0 and state == STATE.RUNNING:
		state = STATE.IDLE
	
	movement += GRAVITY_DIR * GRAVITY * delta
	move_and_slide(movement + dir * SPEED, Vector3(0, 1, 0))
	
	if is_on_floor():
		movement = Vector3()
	
	lobby.broadcast_unreliable(self, "update_position", [self.translation, self.rotation, self.state])
	# does animation
	update_position(self.translation, self.rotation, self.state)

puppet func update_position(pos: Vector3, rot: Vector3, state: int):
	if self.state == STATE.DEAD or state == STATE.DEAD:
		return
	
	self.state = state
	match state:
		STATE.RUNNING:
			$Model.play_animation("run")
		STATE.IDLE:
			$Model.play_animation("idle")
	
	self.translation = pos
	self.rotation = rot

func die():
	state = STATE.DEAD
	$Model.play_animation("idle")
	lobby.broadcast(self, "_client_die")

remote func _client_die():
	# Only the server is allowed to do this
	# But the network master is the controlling player
	# That's why we cannot use the puppet keyword
	if multiplayer.get_rpc_sender_id() != 1:
		return
	state = STATE.DEAD
	$Model.play_animation("idle")

func is_dead():
	return state == STATE.DEAD
