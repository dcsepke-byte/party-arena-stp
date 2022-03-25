extends KinematicBody

const SPEED = 4
const GRAVITY = 9.8
const GRAVITY_DIR = Vector3(0, -1, 0)

var info: Lobby.PlayerInfo

export(bool) var is_solo_player

var has_finished

var movement = Vector3()

onready var ai_waypoint = get_node("../Navigation/Waypoint")
var required_distance = 1

enum STATE {
	IDLE,
	RUNNING,
	DEAD
}

var state = STATE.IDLE setget set_state

func set_state(new_state):
	if state != new_state:
		match new_state:
			STATE.IDLE:
				$Model.play_animation("idle")
			STATE.RUNNING:
				$Model.play_animation("run")
			STATE.DEAD:
				$Model.play_animation("idle")
		state = new_state

func _ready():
	if is_solo_player:
		remove_from_group("players")

func _process(delta):
	if not info.is_local():
		return
	if not is_solo_player:
		var dir = Vector3()
		if not has_finished:
			if not info.is_ai() and state != STATE.DEAD:
				dir.x = Input.get_action_strength("player%d_left" % info.player_id) - Input.get_action_strength("player%d_right" % info.player_id)
				dir.z = Input.get_action_strength("player%d_up" % info.player_id) - Input.get_action_strength("player%d_down" % info.player_id)
			elif info.is_ai() and state != STATE.DEAD:
				dir = ai_waypoint.translation - self.translation
				dir = Vector3(dir.x, 0, dir.z)
				
				if dir.length_squared() < required_distance and ai_waypoint.nodes and ai_waypoint.nodes.size() > 0:
					var index = randi() % ai_waypoint.nodes.size()
					ai_waypoint = ai_waypoint.get_node(ai_waypoint.nodes[index])
					required_distance = 0.1
		
		if dir.length_squared() > 0:
			dir = dir.normalized()
			rotation.y = atan2(dir.x, dir.z)
			if state == STATE.IDLE:
				self.state = STATE.RUNNING
		elif dir.length_squared() == 0 and state == STATE.RUNNING:
			self.state = STATE.IDLE
		
		movement += GRAVITY_DIR * GRAVITY * delta
		if state != STATE.DEAD:
			move_and_slide(movement + dir * SPEED, Vector3(0, 1, 0))
		
		if is_on_floor():
			movement = Vector3()
	rpc_id(1, "update_position", self.translation, self.rotation, self.state)

mastersync func update_position(translation: Vector3, rotation: Vector3, state: int):
	if multiplayer.get_rpc_sender_id() != info.addr.peer_id:
		return
	if state == STATE.DEAD:
		return
	self.translation = translation
	self.rotation = rotation
	self.state = state
	get_parent().lobby.broadcast_unreliable(self, "position_updated", [translation, rotation, state])

puppet func position_updated(translation: Vector3, rotation: Vector3, state: int):
	if info.is_local():
		return
	self.translation = translation
	self.rotation = rotation
	self.state = state

func process_next_stage():
	if info.is_ai():
		$Timer.start()

func _unhandled_input(event):
	if not info.is_local():
		return
	if is_solo_player:
		if event.is_action_pressed("player%d_action1" % info.player_id):
			rpc_id(1, "close_door", 0)
		elif event.is_action_pressed("player%d_action2" % info.player_id):
			rpc_id(1, "close_door", 1)
		elif event.is_action_pressed("player%d_action3" % info.player_id):
			rpc_id(1, "close_door", 2)

func die():
	self.state = STATE.DEAD
	get_parent().lobby.broadcast_unreliable(self, "disable_player")

puppet func disable_player():
	self.state = STATE.DEAD

func is_dead():
	return state == STATE.DEAD

mastersync func close_door(idx: int):
	get_parent().close_door(idx)

func _on_Timer_timeout():
	rpc_id(1, "close_door", randi() % 3)
