## Blitz-Fangen — Reaktion (minigame-categories.md §3.3.3)
## Den Blitzen von ArenaStar so lange wie möglich ausweichen.
extends MinigameBase

const MAX_HEARTS: int = 3
const WARNING_TIME: float = 1.0
const BOLT_RADIUS: float = 2.0

var _hearts: Dictionary = {}       # player_id -> int (verbleibende Herzen)
var _survival_time: Dictionary = {} # player_id -> float (Überlebenszeit)
var _eliminated: Dictionary = {}   # player_id -> bool
var _elimination_order: Array = []
var _spawn_timer: float = 0.0
var _bolt_frequency: float = 1.0
var _arena_half_size: float = 5.0
var _active_bolts: Array = []  # [{position, warning_remaining, active}]


func _ready() -> void:
	results_mode = "by_points"
	# f(n) = 0.8 + 0.1*n Blitze/s
	_bolt_frequency = 0.8 + 0.1 * float(player_count)
	_arena_half_size = sqrt(36.0 + 8.0 * float(maxi(player_count - 2, 0))) * 0.5


func start_game() -> void:
	super.start_game()
	_hearts.clear()
	_survival_time.clear()
	_eliminated.clear()
	_elimination_order.clear()
	_active_bolts.clear()
	_spawn_timer = 0.0

	for p in players:
		var pid: int = p.player_id
		_hearts[pid] = MAX_HEARTS
		_survival_time[pid] = 0.0


func _process(delta: float) -> void:
	if not is_game_running():
		return

	_elapsed += delta
	_spawn_timer += delta

	# Überlebenszeit für aktive Spieler aktualisieren
	for p in players:
		var pid: int = p.player_id
		if not _eliminated.has(pid):
			_survival_time[pid] = _elapsed

	# Blitze spawnen
	var spawn_interval: float = 1.0 / _bolt_frequency
	while _spawn_timer >= spawn_interval:
		_spawn_timer -= spawn_interval
		_spawn_bolt()

	# Aktive Blitze aktualisieren
	var i: int = _active_bolts.size() - 1
	while i >= 0:
		var bolt: Dictionary = _active_bolts[i]
		bolt["warning_remaining"] -= delta
		if bolt["warning_remaining"] <= 0.0 and not bolt["active"]:
			bolt["active"] = true
			bolt["lifetime"] = 0.5  # Blitz schlägt für 0.5 s ein
		if bolt.get("active", false):
			bolt["lifetime"] -= delta
			if bolt["lifetime"] <= 0.0:
				_active_bolts.remove_at(i)
		i -= 1

	# Prüfe, ob nur noch 1 Spieler übrig
	var active_count: int = 0
	for p in players:
		var pid: int = p.player_id
		if not _eliminated.has(pid):
			active_count += 1
	if active_count <= 1:
		request_end.emit()


func _spawn_bolt() -> void:
	var pos: Vector3 = Vector3(
		randf_range(-_arena_half_size, _arena_half_size),
		0.0,
		randf_range(-_arena_half_size, _arena_half_size)
	)
	_active_bolts.append({
		"position": pos,
		"warning_remaining": WARNING_TIME,
		"active": false,
		"lifetime": 0.0
	})


## Spieler von Blitz getroffen (vom Kollisions-System aufgerufen)
func hit_player(player_id: int) -> void:
	if not is_game_running():
		return
	if _eliminated.has(player_id):
		return

	var hearts: int = _hearts.get(player_id, MAX_HEARTS)
	hearts -= 1
	_hearts[player_id] = hearts

	if hearts <= 0:
		_eliminated[player_id] = true
		_elimination_order.append(player_id)


func end_game() -> void:
	# Score = Überlebenszeit; bei Gleichstand zählen Herzen (implizit durch Score-Differenz)
	for p in players:
		var pid: int = p.player_id
		var surv: float = _survival_time.get(pid, 0.0)
		# Bonus für verbleibende Herzen
		var heart_bonus: float = float(_hearts.get(pid, 0)) * 0.01
		_scores[pid] = surv + heart_bonus
	super.end_game()


func get_results() -> Array:
	return super.get_results()


func cleanup() -> void:
	_hearts.clear()
	_survival_time.clear()
	_eliminated.clear()
	_elimination_order.clear()
	_active_bolts.clear()
	super.cleanup()
