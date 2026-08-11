## Knöpfchen-Drücker — Reaktion (minigame-categories.md §3.3.4)
## So viele aufleuchtende Knöpfe wie möglich drücken.
extends MinigameBase

const BUTTON_COUNT: int = 4
const BUTTON_COLORS: Array = ["Rot", "Blau", "Gelb", "Grün"]
const REACTION_PAUSE: float = 0.3

var _current_button: int = -1  # Index des aktuell leuchtenden Knopfes (-1 = keiner)
var _pause_timer: float = 0.0
var _correct_presses: Dictionary = {}  # player_id -> int


func _ready() -> void:
	results_mode = "by_points"


func start_game() -> void:
	super.start_game()
	_correct_presses.clear()
	_current_button = -1
	_pause_timer = 0.0
	for p in players:
		var pid: int = p.player_id
		_correct_presses[pid] = 0
		_scores[pid] = 0.0


func _process(delta: float) -> void:
	if not is_game_running():
		return

	_elapsed += delta

	if _current_button < 0 and _pause_timer <= 0.0:
		# Nächsten Knopf aufleuchten lassen
		_current_button = randi() % BUTTON_COUNT
	elif _pause_timer > 0.0:
		_pause_timer -= delta
		if _pause_timer <= 0.0:
			_current_button = -1  # Bereit für nächsten Knopf


## Spieler drückt einen Knopf (vom Input-Handler aufgerufen)
func press_button(player_id: int, button_index: int) -> void:
	if not is_game_running():
		return
	if _current_button < 0:
		return  # Kein Knopf leuchtet gerade

	if button_index == _current_button:
		# Korrekt!
		_correct_presses[player_id] = _correct_presses.get(player_id, 0) + 1
		add_player_score(player_id, 1.0)
		_current_button = -1
		_pause_timer = REACTION_PAUSE
	# Falscher Knopf: kein Punkt, kleiner Ruckel-Effekt (visuell, kein Abzug)


func end_game() -> void:
	super.end_game()


func get_results() -> Array:
	return super.get_results()


func cleanup() -> void:
	_correct_presses.clear()
	super.cleanup()
