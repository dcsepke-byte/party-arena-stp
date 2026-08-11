## Balance-Akt — Geschicklichkeit (minigame-categories.md §3.2.3)
## Als letzte(r) auf der Kugel balancieren. Eliminations-Minispiel.
extends MinigameBase

const WOBBLE_STAGES: Array = [
	{"time": 0.0, "amplitude": 0.02, "frequency": 1.0},
	{"time": 10.0, "amplitude": 0.04, "frequency": 1.5},
	{"time": 20.0, "amplitude": 0.07, "frequency": 2.0},
	{"time": 26.0, "amplitude": 0.10, "frequency": 3.0},
]

var _eliminated: Dictionary = {}  # player_id -> elimination_time
var _elimination_order: Array = []  # [player_id, ...] in Eliminationsreihenfolge


func _ready() -> void:
	results_mode = "by_position"


func start_game() -> void:
	super.start_game()
	_eliminated.clear()
	_elimination_order.clear()


func _process(delta: float) -> void:
	if not is_game_running():
		return

	_elapsed += delta

	# Prüfe, ob nur noch 1 Spieler übrig ist → Früh-Ende
	var active_count: int = 0
	for p in players:
		var pid: int = p.player_id
		if not _eliminated.has(pid):
			active_count += 1

	if active_count <= 1:
		request_end.emit()


## Einen Spieler eliminieren (vom Minigame-Logik-Knoten aufgerufen)
func eliminate_player(player_id: int) -> void:
	if _eliminated.has(player_id):
		return
	_eliminated[player_id] = _elapsed
	_elimination_order.append(player_id)


func end_game() -> void:
	# Sicherstellen, dass alle nicht eliminierten Spieler markiert sind
	for p in players:
		var pid: int = p.player_id
		if not _eliminated.has(pid):
			_eliminated[pid] = duration
			_elimination_order.append(pid)
	super.end_game()


func get_results() -> Array:
	# Platzierung = umgekehrte Eliminationsreihenfolge
	# Letzter eliminierter = Platz 1
	var results: Array = []
	var total: int = _elimination_order.size()

	# Spieler die nie eliminiert wurden (noch aktiv bei Zeitablauf) bekommen beste Plätze
	var active_players: Array = []
	for p in players:
		var pid: int = p.player_id
		if pid in _elimination_order:
			var idx: int = _elimination_order.find(pid)
			var placement: int = total - idx  # Spätere Elimination = besserer Platz
			results.append({"player_id": pid, "score": float(placement)})
		else:
			active_players.append(pid)

	# Aktive Spieler bekommen die höchsten Platzierungen
	var next_place: int = active_players.size()
	for pid in active_players:
		results.append({"player_id": pid, "score": float(next_place)})
		next_place -= 1

	return results


func cleanup() -> void:
	_eliminated.clear()
	_elimination_order.clear()
	super.cleanup()
