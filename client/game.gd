extends Node

signal create_lobby_callback(name)
signal join_lobby_callback(success)

func _ready():
	multiplayer.set_root_node(self)
	multiplayer.connect("server_disconnected", self, "_on_connection_lost")

func _on_connection_lost():
	get_tree().change_scene("res://client/menus/main_menu.tscn")
	Global.shutdown_connection()

func _process(delta: float):
	# Run the client main loop
	self.propagate_call("_client_process", [delta])

func create_lobby(count: int) -> Node:
	rpc_id(1, "create_lobby", count)
	var name = yield(self, "create_lobby_callback")
	if not name:
		return null
	var lobby = preload("res://client/lobby.tscn").instance()
	lobby.name = name
	add_child(lobby)
	return lobby

func join_lobby(name: String, count: int) -> Node:
	var lobby = preload("res://client/lobby.tscn").instance()
	lobby.name = name
	add_child(lobby)
	rpc_id(1, "join_lobby", name, count)
	if not yield(self, "join_lobby_callback"):
		lobby.free()
		return null
	return lobby

puppet func lobby_creation_failed():
	emit_signal("create_lobby_callback", null)

puppet func lobby_created(name: String):
	emit_signal("create_lobby_callback", name)

puppet func lobby_join_failed():
	emit_signal("join_lobby_callback", false)

puppet func lobby_joined():
	emit_signal("join_lobby_callback", true)
