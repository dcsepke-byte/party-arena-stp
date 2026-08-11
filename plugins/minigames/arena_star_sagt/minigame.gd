## ArenaStar sagt — Reaktion (minigame-categories.md §3.3.2)
## Simon-Says mit ArenaStar: Befehle befolgen, ausscheiden bei Fehlern.
extends MinigameBase

enum Command {JUMP, TURN, WAVE, CROUCH}

const COMMAND_NAMES: Array = ["Springen", "Drehen", "Winken", "Hinhocken"]
const ROUND_INTERVAL_BASE: float = 3.0
const TEMPO_GROWTH: float = 0.15
const SAYS_CHANCE: float = 0.6

var _round: int = 0
var _total_rounds: int = 0
var _round_timer: float = 0.0
var _current_command: int = -1
var _current_is_says: bool = false
var _eliminated: Dictionary = {}
var _elimination_order: Array = []
var _command_shown: bool = false


func _ready() -> void:
	results_mode = "by_position"
	# R(n) = ceil(n/2) + 2
	_total_rounds = ceili(float(player_count) / 2.0) + 2


func start_game() -> void:
	super.start_game()
	_round = 0
	_round_timer = 0.0
	_current_command = -1
	_eliminated.clear()
	_elimination_order.clear()
	_command_shown = false


func _process(delta: float) -> void:
	if not is_game_running():
		return

	_elapsed += delta

	# Aktive Spieler zählen
	var active_count: int = 0
	for p in players:
		var pid: int = p.player_id
		if not _eliminated.has(pid):
			active_count += 1

	if active_count <= 1:
		request_end.emit()
		return

	if _round >= _total_rounds:
		request_end.emit()
		return

	_round_timer += delta

	# Tempo-Faktor: t(r) = 1 + 0.15*(r-1)
	var tempo: float = 1.0 + TEMPO_GROWTH * float(_round)
	var interval: float = ROUND_INTERVAL_BASE / tempo

	if _round_timer >= interval and not _command_shown:
		_command_shown = true
		_show_command()
	elif _round_timer >= interval + 2.5:  # 2.5 s Reaktionszeit
		_next_round()


func _show_command() -> void:
	_current_command = randi() % 4
	_current_is_says = randf() < SAYS_CHANCE
	_round_timer = 0.0


func _next_round() -> void:
	_round += 1
	_command_shown = false
	_round_timer = 0.0
	_current_command = -1


## Spieler-Reaktion prüfen (vom Input-Handler aufgerufen)
func check_player_action(player_id: int, action: int) -> void:
	if not is_game_running():
		return
	if _eliminated.has(player_id):
		return
	if _current_command < 0:
		return

	var should_act: bool = (action == _current_command)
	var allowed: bool = _current_is_says

	# Fehler: Handlung ohne "ArenaStar sagt" oder falsche/nicht Handlung mit "sagt"
	if should_act != allowed:
		eliminate_player(player_id, "falsche Aktion")


func eliminate_player(player_id: int, reason: String = "") -> void:
	if _eliminated.has(player_id):
		return
	_eliminated[player_id] = _round
	_elimination_order.append(player_id)


func end_game() -> void:
	for p in players:
		var pid: int = p.player_id
		if not _eliminated.has(pid):
			_eliminated[pid] = _total_rounds + 1
			_elimination_order.append(pid)
	super.end_game()


func get_results() -> Array:
	var results: Array = []
	var total: int = _elimination_order.size()
	for p in players:
		var pid: int = p.player_id
		if pid in _elimination_order:
			var idx: int = _elimination_order.find(pid)
			var placement: int = total - idx
			results.append({"player_id": pid, "score": float(placement)})
		else:
			results.append({"player_id": pid, "score": 1.0})
	return results


func cleanup() -> void:
	_eliminated.clear()
	_elimination_order.clear()
	super.cleanup()
