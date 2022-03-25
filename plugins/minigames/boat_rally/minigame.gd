extends RigidBody

const BOMB := preload("res://plugins/minigames/boat_rally/bomb.tscn")
const MAX_SPEED := 10.0

onready var lobby := Lobby.get_lobby(self)

var countdown := 1.0
var is_hit := false

func _integrate_forces(state):
	if is_hit:
		state.linear_velocity = Vector3()
		state.angular_velocity = Vector3()
	
	if state.linear_velocity.length() > MAX_SPEED:
		state.linear_velocity = state.linear_velocity.normalized() * MAX_SPEED
	if rotation_degrees.y < -45:
		rotation_degrees.y = -45
		state.angular_velocity = Vector3(0, 1, 0)
	elif rotation_degrees.y > 45:
		rotation_degrees.y = 45
		state.angular_velocity = Vector3(0, -1, 0)

func _ready():
	$Ground.set_as_toplevel(true)

master func fire(pos: Vector3, dir: Vector3):
	if not is_hit:
		self.apply_impulse(pos, dir)
		return true
	return false

func _process(delta):
	$"Ground/Scene Root2".translation.z = self.translation.z + 20
	$"Ground/Scene Root3".translation.z = self.translation.z + 40

puppet func spawn_bombs(positions: Array):
	var i := 0
	for position in positions:
		var bomb = BOMB.instance()
		bomb.translation = position
		bomb.name = "Bomb" + str(i)
		$Ground.add_child(bomb)
		i += 1
	if not multiplayer.is_network_server():
		$AudioStreamPlayer.play()

puppet func update_position(trans: Vector3, rot: Vector3):
	self.translation = trans
	self.rotation = rot

func _server_process(delta):
	countdown -= delta
	if countdown <= 0 and translation.z <= 85:
		var positions := []
		for _i in range(4):
			positions.append(Vector3((randf() - 0.5) * 16, 20, 10 + randf() * 10 + translation.z))
			positions.append(Vector3((randf() - 0.5) * 16, 20, randf() * 5 + translation.z))
		lobby.broadcast(self, "spawn_bombs", [positions])
		spawn_bombs(positions)
		countdown = 4
	lobby.broadcast_unreliable(self, "update_position", [self.translation, self.rotation])

func _on_Area_body_entered(body):
	if not multiplayer.is_network_server():
		return
	if body.is_in_group("player"):
		lobby.minigame_nolok_win()
