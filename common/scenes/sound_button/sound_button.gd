extends Control

@export_file var custom_click

var _click_sound: AudioStream
var _select_sound: AudioStream

func _ready():
	# Lade Sounds zur Laufzeit mit Fallback (robust gegen fehlende Import-Cache)
	_click_sound = _load_sound("res://assets/sounds/ui/rollover2.wav")
	_select_sound = _load_sound("res://assets/sounds/ui/click1.wav")
	if custom_click:
		_click_sound = load(custom_click)

func _load_sound(path: String) -> AudioStream:
	var stream: AudioStream = load(path)
	if stream == null:
		# Fallback: stille AudioStreamPlayer (kein Crash, kein Sound)
		return null
	return stream

func _click():
	if _click_sound:
		UISound.stream = _click_sound
		UISound.play()

func _click_with_arg(_arg):
	_click()

func _select():
	if _select_sound:
		UISound.stream = _select_sound
		UISound.play()

func _select_with_arg(_arg):
	_select()

func _cancel_sound():
	UISound.stop()
