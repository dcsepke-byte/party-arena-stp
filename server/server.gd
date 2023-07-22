extends Node

func _ready() -> void:
	# Set up the network
	# TODO: load port and max_players from a config file?
	var peer = ENetMultiplayerPeer.new()
	peer.create_server(ProjectSettings.get("server/port"),
			ProjectSettings.get("server/max_players"))
	get_tree().network_peer = peer

	# Start the actual server code
	get_tree().change_scene_to_file("res://server/game.tscn")
