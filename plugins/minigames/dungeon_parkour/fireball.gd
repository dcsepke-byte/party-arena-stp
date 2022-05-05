extends Spatial

func _process(delta):
	self.translation.z += 10 * delta

func _on_Area_body_entered(_body):
	if not multiplayer.is_network_server():
		return
	get_parent().lobby.minigame_nolok_loose()
