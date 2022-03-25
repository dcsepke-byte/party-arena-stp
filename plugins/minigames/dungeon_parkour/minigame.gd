extends Spatial

onready var lobby := Lobby.get_lobby(self)
var fireball = preload("res://plugins/minigames/dungeon_parkour/fireball.tscn")

func _ready():
	create_fireballs()

puppet func create_fireball(pos: Vector3):
	var instance = fireball.instance()
	instance.translation = pos
	add_child(instance)

func create_fireballs():
	if not multiplayer.is_network_server():
		return
	lobby.broadcast(self, "create_fireball", [$Fireball2.translation])
	create_fireball($Fireball2.translation)
	
	yield(get_tree().create_timer(0.25), "timeout")
	
	lobby.broadcast(self, "create_fireball", [$Fireball3.translation])
	create_fireball($Fireball3.translation)
	
	yield(get_tree().create_timer(0.25), "timeout")
	
	lobby.broadcast(self, "create_fireball", [$Fireball1.translation])
	$Fireball1.translation

func _client_process(_delta: float):
	$Remaining.text = str(stepify($Timer2.time_left, 0.1))

func _server_process(_delta: float):
	if $Player1.translation.y < -5:
		lobby.minigame_nolok_loose()

func _on_Finish_body_entered(_body):
	if not multiplayer.is_network_server():
		return
	lobby.minigame_nolok_win()

func _on_Timer2_timeout():
	if not multiplayer.is_network_server():
		return
	lobby.minigame_nolok_loose()
