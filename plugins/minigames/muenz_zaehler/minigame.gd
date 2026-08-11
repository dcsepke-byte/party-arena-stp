## Münz-Zähler — Rechnen/Wort (minigame-categories.md §3.5.2)
## Die von ArenaStar kurz gezeigte Münzmenge möglichst genau schätzen.
extends MinigameBase

const TOTAL_ROUNDS: int = 5
const SHOW_TIME: float = 2.0
const INPUT_TIME: float = 3.0

enum RoundState {SHOWING, INPUT, RESULT}

var _current_round: int = 0
var _round_state: int = RoundState.SHOWING
var _state_timer: float = 0.0
var _correct_amount: int = 0
var _round_scores: Dictionary = {}   # player_id -> int (Punkte diese Runde)
var _total_scores: Dictionary = {}    # player_id -> int (Gesamtpunkte)
var _guesses: Dictionary = {}         # player_id -> int (Schätzung diese Runde)
var _lo: int = 3
var _hi: int = 10


func _ready() -> void:
	results_mode = "by_points"
	# lo(n) = 3 + 2*(n-2), hi(n) = 10 + 5*(n-2)
	_lo = 3 + 2 * (player_count - 2)
	_hi = 10 + 5 * (player_count - 2)


func start_game() -> void:
	super.start_game()
	_current_round = 0
	_round_state = RoundState.SHOWING
	_state_timer = 0.0
	_guesses.clear()
	_total_scores.clear()
	for p in players:
		var pid: int = p.player_id
		_total_scores[pid] = 0
		_scores[pid] = 0.0
	_start_round()


func _start_round() -> void:
	_round_state = RoundState.SHOWING
	_state_timer = 0.0
	_correct_amount = randi_range(_lo, _hi)
	_guesses.clear()


func _process(delta: float) -> void:
	if not is_game_running():
		return

	_elapsed += delta
	_state_timer += delta

	match _round_state:
		RoundState.SHOWING:
			if _state_timer >= SHOW_TIME:
				_round_state = RoundState.INPUT
				_state_timer = 0.0

		RoundState.INPUT:
			if _state_timer >= INPUT_TIME:
				_evaluate_round()

		RoundState.RESULT:
			if _state_timer >= 1.5:
				_current_round += 1
				if _current_round >= TOTAL_ROUNDS:
					request_end.emit()
				else:
					_start_round()


func _evaluate_round() -> void:
	_round_state = RoundState.RESULT
	_state_timer = 0.0

	# Spieler nach Distanz zur richtigen Zahl sortieren
	var distances: Array = []
	for p in players:
		var pid: int = p.player_id
		var guess: int = _guesses.get(pid, 0)
		var dist: int = absi(guess - _correct_amount)
		distances.append({"player_id": pid, "distance": dist})

	distances.sort_custom(func(a, b): return a["distance"] < b["distance"])

	# Top 3 erhalten Punkte: 3, 2, 1 (Gleichstände mitteln)
	var points: Array = [3, 2, 1]
	var rank: int = 0
	var index: int = 0
	while index < distances.size() and rank < 3:
		# Gruppe gleicher Distanz finden
		var group: Array = []
		var group_dist: int = distances[index]["distance"]
		while index < distances.size() and distances[index]["distance"] == group_dist:
			group.append(distances[index]["player_id"])
			index += 1

		# Punkte für diese Gruppe (Mittelung)
		var total_points: int = 0
		var count: int = 0
		for r in range(rank, mini(rank + group.size(), 3)):
			total_points += points[r]
			count += 1

		if count > 0:
			var avg: int = ceili(float(total_points) / float(count))
			for pid in group:
				_total_scores[pid] = _total_scores.get(pid, 0) + avg

		rank += group.size()


## Schätzung eines Spielers entgegennehmen (vom Input-Handler aufgerufen)
func submit_guess(player_id: int, guess: int) -> void:
	if not is_game_running():
		return
	if _round_state != RoundState.INPUT:
		return
	_guesses[player_id] = clampi(guess, 0, 99)


func end_game() -> void:
	for p in players:
		var pid: int = p.player_id
		_scores[pid] = float(_total_scores.get(pid, 0))
	super.end_game()


func get_results() -> Array:
	return super.get_results()


func cleanup() -> void:
	_guesses.clear()
	_round_scores.clear()
	_total_scores.clear()
	super.cleanup()
