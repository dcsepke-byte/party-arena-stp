## Wort-Puzzle — Rechnen/Wort (minigame-categories.md §3.5.3)
## Aus den gezeigten Buchstaben das längste gültige Wort bilden.
extends MinigameBase

const VOWELS: Array = ["A", "E", "I", "O", "U"]
const CONSONANTS: Array = ["B", "C", "D", "F", "G", "H", "K", "L", "M", "N", "P", "R", "S", "T", "W", "Z"]

var _letters: Array = []  # Verfügbare Buchstaben
var _submissions: Dictionary = {}  # player_id -> {word: String, length: int, time: float}
var _best_word: Dictionary = {}    # player_id -> {word: String, length: int}


func _ready() -> void:
	results_mode = "by_points"
	duration = clampi(duration, 10, 20)


func start_game() -> void:
	super.start_game()
	_submissions.clear()
	_best_word.clear()
	_generate_letters()

	for p in players:
		var pid: int = p.player_id
		_best_word[pid] = {"word": "", "length": 0}
		_scores[pid] = 0.0


func _generate_letters() -> void:
	# L(n) = 6 + floor((n-2)/2)
	var letter_count: int = 6 + int(float(player_count - 2) / 2.0)
	_letters.clear()

	# Mischung aus Vokalen und Konsonanten (mind. 2 Vokale)
	var vowel_count: int = maxi(2, letter_count / 3)
	for i in range(vowel_count):
		_letters.append(VOWELS[randi() % VOWELS.size()])

	var remaining: int = letter_count - vowel_count
	for i in range(remaining):
		_letters.append(CONSONANTS[randi() % CONSONANTS.size()])

	_letters.shuffle()


func _process(delta: float) -> void:
	if not is_game_running():
		return

	_elapsed += delta

	# Prüfe ob alle Spieler eingereicht haben
	if _submissions.size() >= player_count:
		request_end.emit()


## Wort-Einreichung eines Spielers (vom Input-Handler aufgerufen)
func submit_word(player_id: int, word: String) -> void:
	if not is_game_running():
		return

	var word_len: int = word.length()
	if word_len < 2:
		return  # Zu kurz

	# Prüfe ob das Wort aus den verfügbaren Buchstaben gebildet werden kann
	# (Jeder Buchstabe nur einmal verwendbar)
	var available: Array = _letters.duplicate()
	for ch in word:
		var idx: int = available.find(ch.to_upper())
		if idx < 0:
			return  # Buchstabe nicht verfügbar
		available.remove_at(idx)

	# Beste Einreichung für diesen Spieler aktualisieren
	var best_len: int = _best_word.get(player_id, {}).get("length", 0)
	if word_len > best_len:
		_best_word[player_id] = {"word": word, "length": word_len}

	_submissions[player_id] = {
		"word": word,
		"length": word_len,
		"time": _elapsed
	}


func end_game() -> void:
	for p in players:
		var pid: int = p.player_id
		var best_len: int = _best_word.get(pid, {}).get("length", 0)
		_scores[pid] = float(best_len)
	super.end_game()


func get_results() -> Array:
	return super.get_results()


func cleanup() -> void:
	_letters.clear()
	_submissions.clear()
	_best_word.clear()
	super.cleanup()
