## Sternen-Labyrinth — Puzzle/Logik (minigame-categories.md §3.4.2)
## Als erste(r) durch das Labyrinth zum Zielstern gelangen.
extends MinigameBase

var _maze_size: int = 5      # s(n) = 4 + ceil(n/2)
var _finish_order: Array = []  # [player_id, ...] in Zielankunfts-Reihenfolge
var _player_distances: Dictionary = {}  # player_id -> float (erreichte Wegstrecke)
var _finished: Dictionary = {}  # player_id -> float (Zielankunftszeit)


func _ready() -> void:
	results_mode = "by_position"
	_maze_size = 4 + ceili(float(player_count) / 2.0)


func start_game() -> void:
	super.start_game()
	_finish_order.clear()
	_player_distances.clear()
	_finished.clear()
	for p in players:
		var pid: int = p.player_id
		_player_distances[pid] = 0.0


func _process(delta: float) -> void:
	if not is_game_running():
		return

	_elapsed += delta

	# Prüfe ob alle Spieler im Ziel sind
	if _finish_order.size() >= player_count:
		request_end.emit()


## Spieler erreicht das Ziel (vom Minigame-Logik-Knoten aufgerufen)
func player_reached_goal(player_id: int) -> void:
	if not is_game_running():
		return
	if _finished.has(player_id):
		return

	_finished[player_id] = _elapsed
	_finish_order.append(player_id)


## Distanz eines Spielers aktualisieren (vom Minigame-Logik-Knoten aufgerufen)
func update_player_distance(player_id: int, distance: float) -> void:
	if _finished.has(player_id):
		return
	_player_distances[player_id] = distance


func end_game() -> void:
	super.end_game()


func get_results() -> Array:
	var results: Array = []

	# Angekommene Spieler: nach Reihenfolge
	var rank: int = 1
	for pid in _finish_order:
		results.append({"player_id": pid, "score": float(player_count - rank + 1)})
		rank += 1

	# Nicht angekommene Spieler: nach erreichter Distanz
	var remaining: Array = []
	for p in players:
		var pid: int = p.player_id
		if not _finished.has(pid):
			remaining.append({"player_id": pid, "distance": _player_distances.get(pid, 0.0)})

	# Sortiere nach Distanz absteigend
	remaining.sort_custom(func(a, b): return a["distance"] > b["distance"])
	for entry in remaining:
		results.append({"player_id": entry["player_id"], "score": float(player_count - rank + 1)})
		rank += 1

	return results


func cleanup() -> void:
	_finish_order.clear()
	_player_distances.clear()
	_finished.clear()
	super.cleanup()
