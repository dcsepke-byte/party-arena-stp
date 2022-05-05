extends Spatial

const SPEED = 2

func _ready():
	$Armature/AnimationPlayer.play("fly-start")
	$Armature/AnimationPlayer.queue("fly")

func _server_process(delta):
	var dir = Vector3(-self.translation.x, 0, -self.translation.z).normalized()
	self.rotation.y = atan2(dir.x, dir.z)
	self.translation += dir * delta * SPEED
	get_parent().lobby.broadcast_unreliable(self, "position_updated", [translation, rotation])

puppet func position_updated(trans: Vector3, rot: Vector3):
	self.translation = trans
	self.rotation = rot

puppet func delete():
	queue_free()

func _on_Area_body_entered(body):
	if not multiplayer.is_network_server():
		return
	if body.is_in_group("player"):
		get_parent().lobby.broadcast(self, "delete")
		queue_free()

func _on_Area_area_entered(area):
	if not multiplayer.is_network_server():
		return
	if area.is_in_group("target"):
		get_parent().end_game()
