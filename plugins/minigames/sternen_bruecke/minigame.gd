## Sternen-Brücke — Kooperation (minigame-categories.md §3.6.2)
## Gemeinsam eine Brücke über eine Schlucht bauen. Alle gewinnen zusammen.
extends MinigameBase

var _total_segments: int = 4       # M(n) = n
var _placed_segments: int = 0
var _progress: float = 0.0         # 0.0 - 1.0


func _ready() -> void:
	team_mode = "coop_all"
	results_mode = "by_points"
	_total_segments = player_count  # M(n) = n Pro-Kopf-Arbeitslast


func start_game() -> void:
	super.start_game()
	_placed_segments = 0
	_progress = 0.0
	# Alle Spieler starten mit gleichem Score (Koop-Basis)
	for p in players:
		var pid: int = p.player_id
		_scores[pid] = 0.0


func _process(delta: float) -> void:
	if not is_game_running():
		return

	_elapsed += delta

	# Prüfe ob die Brücke fertig ist
	if _placed_segments >= _total_segments:
		request_end.emit()


## Ein Segment wurde platziert (vom Minigame-Logik-Knoten aufgerufen)
func place_segment(player_id: int) -> void:
	if not is_game_running():
		return
	if _placed_segments >= _total_segments:
		return

	_placed_segments += 1
	_progress = float(_placed_segments) / float(_total_segments)


func end_game() -> void:
	# Fortschritt als Score für alle (Team-Ergebnis)
	_progress = float(_placed_segments) / float(_total_segments)
	for p in players:
		var pid: int = p.player_id
		_scores[pid] = _progress * 100.0  # Prozent
	super.end_game()


func get_results() -> Array:
	return super.get_results()


func cleanup() -> void:
	super.cleanup()
