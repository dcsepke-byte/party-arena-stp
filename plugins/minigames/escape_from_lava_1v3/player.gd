extends "res://plugins/minigames/escape_from_lava/player.gd"

export(bool) var is_solo_player

func _ready():
	if is_solo_player:
		remove_from_group("players")

func _do_process(delta):
	if not info.is_local() or state == STATE.DEAD:
		return
	if not is_solo_player:
		# Call the process implementation from the superclass
		# This takes care of stuff like moving around and AI pathfinding
		._do_process(delta)

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

puppetsync func close_door(idx: int):
	# only relevant for the server
	if multiplayer.get_network_unique_id() != 1:
		return
	
	get_parent().close_door(idx)

func _on_Timer_timeout():
	rpc_id(1, "close_door", randi() % 3)
