extends Spatial

signal animation_finished
signal walking_finished

enum State {
	None,
	Fly_out,
	Fly_in,
	WALK_DRAGON
}

var player_to_animate: Spatial
var next_space: NodeBoard
var state: int = State.None
var destination: Vector3

var dragon: Spatial
var start: Vector3
var end: Vector3
var time: float
var duration: float

func _process(delta: float):
	match state:
		State.WALK_DRAGON:
			time += delta
			time = min(time, duration)
			dragon.translation = start * (1 - time/duration) + end * (time/duration)
			if time == duration:
				start = Vector3()
				end = Vector3()
				time = 0
				duration = 0
				state = State.None
				emit_signal("walking_finished")
		State.Fly_out:
			if player_to_animate.translation.y < player_to_animate.space.translation.y + 5:
				player_to_animate.translation.y += 10 * delta
			else:
				state = State.Fly_in
				player_to_animate.translation = next_space.translation
				destination = player_to_animate.translation
				player_to_animate.translation += Vector3(0, 5, 0)
				$Controller.camera_focus = next_space
				next_space = null
		State.Fly_in:
			if player_to_animate.translation.y > destination.y:
				player_to_animate.translation.y -= 10 * delta
			else:
				player_to_animate.translation = destination
				state = State.None
				player_to_animate = null
				destination = Vector3()
				emit_signal("animation_finished")

func handle_event(player: Spatial, space: NodeBoard):
	var name := "KDE_VALLEY_DRAGON_NAME"
	var icon := "res://plugins/boards/KDEValley/dragons/%s_icon.png" % space.name
	var text := "KDE_VALLEY_TAKE_TO_CAKE"
	
	$SpeechDialog.show_accept_dialog(name, icon, text, player.info.player_id)
	if not yield($SpeechDialog, "dialog_option_taken"):
		$Controller.continue()
		return

	$Controller.lobby.broadcast(self, "_dragon_animation", [player.info.player_id, get_path_to(space)])
	return _dragon_animation(player.info.player_id, get_path_to(space))

puppet func _dragon_animation(id: int, name: String):
	var player = $Controller.get_player_by_player_id(id)
	var space = get_node(name)
	var dragon_anim: AnimationPlayer =\
		space.get_node("Dragon/AnimationPlayer")
	dragon_anim.play("walk")

	dragon = space.get_node("Dragon")
	var start_transform: Transform = dragon.transform

	start = dragon.translation
	var d: Vector3 = player.translation - dragon.translation
	end = player.translation - d.normalized() * 0.3
	var dir: Vector3 = (end - start).normalized()
	duration = (end - start).length() * 0.5
	dragon.rotation = Vector3(0, atan2(dir.x, dir.z), 0)
	state = State.WALK_DRAGON
	yield(self, "walking_finished")

	dragon_anim.play("fly_start")

	yield(get_tree().create_timer(0.5), "timeout")
	var target_space = $Controller.get_cake_space()
	next_space = target_space
	player_to_animate = player
	state = State.Fly_out

	$Controller.camera_focus = space

	yield(self, "animation_finished")

	dragon.transform = start_transform
	dragon_anim.play("fly_end")
	dragon = null

	if multiplayer.is_network_server():
		player.teleport_to(target_space)
		yield($Controller.buy_cake(player), "completed")
		yield(get_tree().create_timer(0.5), "timeout")
		$Controller.continue()
