extends Control

onready var lobby := Lobby.get_lobby(self)

func _ready():
	clear_display()

puppet func _client_display_action(action):
	_client_clear_display()
	var conf = InputMap.get_action_list(action)[0]
	
	var control = ControlHelper.get_from_event(conf)
	if control is Texture:
		$TextureRect.texture = control
		$Label.text = ""
	else:
		if conf is InputEventKey:
			$TextureRect.texture = load("res://assets/textures/controls/keyboard/key_blank.png")
		else:
			$TextureRect.texture = null
		$Label.text = control

func display_action(action):
	# Replicate the state to the clients if applicable
	if lobby and is_network_master():
		lobby.broadcast(self, "_client_display_action", [action])
	_client_display_action(action)

puppet func _client_clear_display():
	$Label.text = ""
	$TextureRect.texture = null

func clear_display():
	# Replicate the state to the clients if applicable
	if lobby and is_network_master():
		lobby.broadcast(self, "_client_clear_display")
	_client_clear_display()
