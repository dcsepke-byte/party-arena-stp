## Insel-Memory — Puzzle/Logik (minigame-categories.md §3.4.3)
## In 30 s die meisten Kartenpaare finden. 4×4 Feld = 8 Paare.
extends MinigameBase

const GRID_SIZE: int = 4        # 4×4 = 16 Karten = 8 Paare
const TOTAL_PAIRS: int = 8

var _pairs_found: Dictionary = {}  # player_id -> int (Anzahl gefundener Paare)
var _player_grids: Dictionary = {}  # player_id -> Array (Kartenzustand des Spielers)


func _ready() -> void:
	results_mode = "by_points"


func _generate_grid() -> Array:
	# Erzeugt ein gemischtes 4×4-Grid: Werte 0-7, je zweimal = 8 Paare
	var cards: Array = []
	for pair_id in range(TOTAL_PAIRS):
		cards.append(pair_id)
		cards.append(pair_id)
	cards.shuffle()

	var grid: Array = []
	for row in range(GRID_SIZE):
		var grid_row: Array = []
		for col in range(GRID_SIZE):
			var idx: int = row * GRID_SIZE + col
			grid_row.append({
				"value": cards[idx],
				"revealed": false,
				"matched": false
			})
		grid.append(grid_row)
	return grid


func start_game() -> void:
	super.start_game()
	_pairs_found.clear()
	_player_grids.clear()
	for p in players:
		var pid: int = p.player_id
		_pairs_found[pid] = 0
		_scores[pid] = 0.0
		# Jeder Spieler hat ein unabhängig gemischtes Feld
		_player_grids[pid] = _generate_grid()


func _process(delta: float) -> void:
	if not is_game_running():
		return

	_elapsed += delta

	# Prüfe ob alle Paare von allen Spielern gefunden wurden
	var all_done: bool = true
	for p in players:
		var pid: int = p.player_id
		if _pairs_found.get(pid, 0) < TOTAL_PAIRS:
			all_done = false
			break
	if all_done:
		request_end.emit()


## Karte aufdecken (vom Input-Handler aufgerufen)
func reveal_card(player_id: int, row: int, col: int) -> int:
	if not is_game_running():
		return -1

	var grid: Array = _player_grids.get(player_id, [])
	if grid.is_empty():
		return -1
	if row < 0 or row >= GRID_SIZE or col < 0 or col >= GRID_SIZE:
		return -1

	var card = grid[row][col]
	if card["revealed"] or card["matched"]:
		return -1

	return card["value"]


## Paar gefunden melden (vom Minigame-Logik-Knoten aufgerufen)
func pair_matched(player_id: int, row1: int, col1: int, row2: int, col2: int) -> void:
	if not is_game_running():
		return

	var grid: Array = _player_grids.get(player_id, [])
	if grid.is_empty():
		return

	grid[row1][col1]["matched"] = true
	grid[row2][col2]["matched"] = true

	_pairs_found[player_id] = _pairs_found.get(player_id, 0) + 1
	add_player_score(player_id, 1.0)


## Karten wieder zudecken (kein Paar)
func hide_cards(player_id: int, row1: int, col1: int, row2: int, col2: int) -> void:
	var grid: Array = _player_grids.get(player_id, [])
	if grid.is_empty():
		return
	if not grid[row1][col1]["matched"]:
		grid[row1][col1]["revealed"] = false
	if not grid[row2][col2]["matched"]:
		grid[row2][col2]["revealed"] = false


func end_game() -> void:
	super.end_game()


func get_results() -> Array:
	return super.get_results()


func cleanup() -> void:
	_pairs_found.clear()
	_player_grids.clear()
	super.cleanup()
