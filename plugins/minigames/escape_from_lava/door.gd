extends StaticBody

var can_be_opened = true setget set_can_be_opened

func destroy():
	$"Scene Root/AnimationPlayer".play("destroy")
	$CollisionShape.disabled = true

func open():
	if can_be_opened:
		$"Scene Root/AnimationPlayer".play("open")
		$CollisionShape.disabled = true
		can_be_opened = false

func set_can_be_opened(enabled: bool):
	set_enabled(enabled)
	Lobby.get_lobby(self).broadcast(self, "set_enabled", [enabled])

puppet func set_enabled(enabled: bool):
	can_be_opened = enabled

func _on_Area_body_entered(body):
	if body.is_in_group("players"):
		open()
