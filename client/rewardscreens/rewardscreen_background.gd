extends Control

func _ready():
	if not multiplayer.is_network_server():
		yield(get_tree(), "idle_frame")
		$AudioStreamPlayer2.play()
		get_tree().create_timer(4).connect("timeout", $AudioStreamPlayer, "play")
