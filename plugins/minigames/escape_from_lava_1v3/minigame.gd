extends Spatial

const LAVA_RISE_SPEED = 0.25

var lobby: Lobby

var num_players_alive = 4

onready var stages = [$Stage1, $Stage2, $Stage3]
var current_stage = -1
var has_chosen = false

func _enter_tree() -> void:
	lobby = Lobby.get_lobby(self)

func _ready():
	enter_stage($Player1, 0)

func close_door(index):
	if current_stage < stages.size() and not has_chosen and index < stages[current_stage].get_child_count() and index >= 0:
		stages[current_stage].get_child(index).can_be_opened = false
		has_chosen = true
		lobby.broadcast(self, "door_closed", [index])

puppet func door_closed(index):
	if current_stage < stages.size() and not has_chosen and index < stages[current_stage].get_child_count() and index >= 0:
		stages[current_stage].get_child(index).can_be_opened = false
		$Screen/ControlView2D.clear_display()
		$Screen/ControlView2D2.clear_display()
		$Screen/ControlView2D3.clear_display()

func enter_stage(body, new_stage):
	if not body.is_in_group("players"):
		return
	
	if new_stage > current_stage:
		current_stage = new_stage
		has_chosen = false
		
		if current_stage < stages.size() and $Player4.info.is_local():
			$Player4.process_next_stage()
			
			$Screen/ControlView2D.display_action("player%d_action1" % $Player4.info.player_id)
			$Screen/ControlView2D2.display_action("player%d_action2" % $Player4.info.player_id)
			$Screen/ControlView2D3.display_action("player%d_action3" % $Player4.info.player_id)

func _process(delta):
	var min_progress = null
	
	for player in Utility.get_nodes_in_group(self, "players"):
		if not player.is_dead() and (min_progress == null or player.translation.z < min_progress.z):
			min_progress = player.translation
	
	if min_progress != null:
		$Camera.translation +=  (Vector3(0, min_progress.y, min_progress.z) + Vector3(0, 3, -4) - $Camera.translation) * delta
	
	$Lava.translation += Vector3(0, 1, 0) * delta * LAVA_RISE_SPEED

func _on_Lava_body_entered(body):
	if not is_network_master():
		return
	if body.is_in_group("players"):
		if not body.is_dead():
			body.die()
			num_players_alive -= 1
			
			if num_players_alive == 1:
				$EndTimer.start()
				lobby.broadcast(self, "end_game")
	elif body.is_in_group("door"):
		body.destroy()

func _on_Finish_body_entered(body):
	if not is_network_master():
		return
	if body.is_in_group("players"):
		body.has_finished = true
		body.die()
		
		$EndTimer.start()
		lobby.broadcast(self, "end_game")

puppet func end_game():
	$Screen/Label.show()

func _on_EndTimer_timeout():
	if num_players_alive > 1:
		lobby.minigame_1v3_win_team_players()
	else:
		lobby.minigame_1v3_win_solo_player()
