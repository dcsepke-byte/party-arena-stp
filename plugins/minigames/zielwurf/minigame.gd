## Zielwurf — Geschicklichkeit (minigame-categories.md §3.2.4)
## In 30 s die meisten Treffer auf Gegner erzielen.
extends MinigameBase

const MAX_BALLS_PER_PLAYER: int = 3
const INVULN_TIME: float = 0.5

var _player_balls: Dictionary = {}    # player_id -> int (Anzahl Bälle)
var _player_hits: Dictionary = {}     # player_id -> int (Treffer)
var _invuln_timers: Dictionary = {}   # player_id -> float (Unverwundbarkeits-Timer)


func _ready() -> void:
	pass


func start_game() -> void:
	super.start_game()
	_player_balls.clear()
	_player_hits.clear()
	_invuln_timers.clear()
	for p in players:
		var pid: int = p.player_id
		_player_balls[pid] = MAX_BALLS_PER_PLAYER
		_player_hits[pid] = 0
		_scores[pid] = 0.0


func _process(delta: float) -> void:
	if not is_game_running():
		return

	_elapsed += delta

	# Unverwundbarkeits-Timer aktualisieren
	for pid in _invuln_timers.keys():
		_invuln_timers[pid] -= delta
		if _invuln_timers[pid] <= 0.0:
			_invuln_timers.erase(pid)


## Registriert einen Treffer (vom Minigame-Logik-Knoten aufgerufen)
func register_hit(shooter_id: int, target_id: int) -> void:
	if not is_game_running():
		return
	# Prüfe Unverwundbarkeit
	if _invuln_timers.has(target_id):
		return
	# Prüfe Munition
	var balls: int = _player_balls.get(shooter_id, 0)
	if balls <= 0:
		return

	_player_balls[shooter_id] = balls - 1
	_player_hits[shooter_id] = _player_hits.get(shooter_id, 0) + 1
	add_player_score(shooter_id, 1.0)
	_invuln_timers[target_id] = INVULN_TIME


## Ball aufheben (vom Minigame-Logik-Knoten aufgerufen)
func pickup_ball(player_id: int) -> void:
	var current: int = _player_balls.get(player_id, 0)
	if current < MAX_BALLS_PER_PLAYER:
		_player_balls[player_id] = current + 1


func end_game() -> void:
	super.end_game()


func get_results() -> Array:
	return super.get_results()


func cleanup() -> void:
	_player_balls.clear()
	_player_hits.clear()
	_invuln_timers.clear()
	super.cleanup()
