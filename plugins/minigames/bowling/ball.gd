extends KinematicBody

const SPEED = 10
const MAX_TIME = 4

var time = 0

puppet func die():
	queue_free()

puppet func _position_update(pos: Vector3):
	self.translation = pos

func _server_process(delta):
	time += delta
	
	var forward = Vector3(0, 0, -1)
	var collider = move_and_collide(forward * SPEED * delta)
	
	if time > MAX_TIME:
		get_parent().lobby.broadcast(self, "die")
		queue_free()
		return
	
	if collider != null and collider.collider != null:
		var object = collider.collider
		if object.is_in_group("players") or object.is_in_group("box"):
			get_parent().lobby.broadcast(self, "die")
			queue_free()
			object.knockout(Vector3(0, 3.5, -8))
	get_parent().lobby.broadcast_unreliable(self, "_position_update", [self.translation])
