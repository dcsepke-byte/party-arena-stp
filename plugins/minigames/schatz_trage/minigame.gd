## Schatz-Trage — Kooperation (minigame-categories.md §3.6.3)
## Als Team den Schatz schneller als das andere Team ins Ziel tragen.
extends MinigameBase

const CARRY_RADIUS: float = 2.0
const TRACK_LENGTH: float = 50.0

var _team_a_progress: float = 0.0    # Team A (ungerade IDs): zurückgelegte Strecke
var _team_b_progress: float = 0.0    # Team B (gerade IDs): zurückgelegte Strecke
var _team_a_finished: bool = false
var _team_b_finished: bool = false


func _ready() -> void:
	team_mode = "coop_teams"
	results_mode = "by_points"
	# Nur gerade Spielerzahlen ≥ 4 gültig


func _get_team(player_id: int) -> String:
	return "A" if (player_id % 2) == 1 else "B"


func start_game() -> void:
	super.start_game()
	_team_a_progress = 0.0
	_team_b_progress = 0.0
	_team_a_finished = false
	_team_b_finished = false
	for p in players:
		var pid: int = p.player_id
		_scores[pid] = 0.0


func _process(delta: float) -> void:
	if not is_game_running():
		return

	_elapsed += delta

	# Prüfe ob ein Team das Ziel erreicht hat oder beide
	if _team_a_finished or _team_b_finished:
		request_end.emit()


## Fortschritt eines Teams aktualisieren (vom Minigame-Logik-Knoten aufgerufen)
func update_team_progress(team: String, progress: float) -> void:
	if not is_game_running():
		return

	if team == "A":
		_team_a_progress = progress
		if _team_a_progress >= TRACK_LENGTH:
			_team_a_finished = true
	else:
		_team_b_progress = progress
		if _team_b_progress >= TRACK_LENGTH:
			_team_b_finished = true


func end_game() -> void:
	# Siegerteam: erreicht Ziel zuerst ODER mehr Fortschritt bei Zeitablauf
	var team_a_wins: bool = false
	if _team_a_finished and not _team_b_finished:
		team_a_wins = true
	elif _team_b_finished and not _team_a_finished:
		team_a_wins = false
	else:
		team_a_wins = _team_a_progress >= _team_b_progress

	for p in players:
		var pid: int = p.player_id
		var team: String = _get_team(pid)
		if (team == "A" and team_a_wins) or (team == "B" and not team_a_wins):
			_scores[pid] = 100.0  # Sieger-Team
		else:
			_scores[pid] = 50.0   # Zweites Team (Trostpunkte)

	super.end_game()


func get_results() -> Array:
	return super.get_results()


func cleanup() -> void:
	super.cleanup()
