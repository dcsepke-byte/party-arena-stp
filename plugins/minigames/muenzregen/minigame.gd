## Münzregen — Geschicklichkeit (minigame-categories.md §3.2.2)
## Münzen regnen vom Himmel; Spieler sammeln durch Berühren.
extends MinigameBase

const COIN_VALUE: float = 1.0
const STAR_COIN_VALUE: float = 5.0
const COIN_DESPAWN_TIME: float = 6.0
const STAR_COIN_CHANCE: float = 0.1

var _arena_size: float = 6.0
var _spawn_rate: float = 1.1
var _spawn_timer: float = 0.0
var _active_coins: Array = []


func _ready() -> void:
	# Arena-Fläche nach Spielerzahl skalieren: A(n) = 36 + 8*(n-2) m²
	_arena_size = sqrt(36.0 + 8.0 * float(maxi(player_count - 2, 0)))
	# Spawn-Rate: r(n) = 0.8 + 0.15*n Münzen/s
	_spawn_rate = 0.8 + 0.15 * float(player_count)


func start_game() -> void:
	super.start_game()
	_active_coins.clear()
	_spawn_timer = 0.0


func _process(delta: float) -> void:
	if not is_game_running():
		return

	_elapsed += delta
	_spawn_timer += delta

	# Münzen spawnen
	var spawn_interval: float = 1.0 / _spawn_rate
	while _spawn_timer >= spawn_interval:
		_spawn_timer -= spawn_interval
		_spawn_coin()

	# Münzen aktualisieren (Despawn-Timer)
	var i: int = _active_coins.size() - 1
	while i >= 0:
		var coin: Dictionary = _active_coins[i]
		coin["lifetime"] -= delta
		if coin["lifetime"] <= 0.0:
			_active_coins.remove_at(i)
		i -= 1


func _spawn_coin() -> void:
	var is_star: bool = randf() < STAR_COIN_CHANCE
	var value: float = STAR_COIN_VALUE if is_star else COIN_VALUE
	var pos: Vector3 = Vector3(
		randf_range(-_arena_size * 0.5, _arena_size * 0.5),
		5.0,  # Fallhöhe
		randf_range(-_arena_size * 0.5, _arena_size * 0.5)
	)
	_active_coins.append({
		"position": pos,
		"value": value,
		"is_star": is_star,
		"lifetime": COIN_DESPAWN_TIME
	})


## Wird vom Framework aufgerufen, wenn ein Spieler eine Münze berührt
func collect_coin(player_id: int, coin_index: int) -> void:
	if coin_index < 0 or coin_index >= _active_coins.size():
		return
	var coin: Dictionary = _active_coins[coin_index]
	add_player_score(player_id, coin["value"])
	_active_coins.remove_at(coin_index)


func end_game() -> void:
	super.end_game()


func get_results() -> Array:
	return super.get_results()


func cleanup() -> void:
	_active_coins.clear()
	super.cleanup()
