## MinigameBase — Basisklasse für alle Party-Arena-Minispiele
## Erbt von Node3D. Definiert den Schnittstellenvertrag zwischen
## Framework und Minigame-Plugin (minigame-architecture.md §3.2).
class_name MinigameBase
extends Node3D

## Signal: Minispiel fordert vorzeitiges Ende an (Sieg-/Eliminationsbedingung erreicht)
signal request_end()

## Anzahl teilnehmender Spieler (2–8), vom Framework vor _ready() gesetzt
var player_count: int = 0

## Spielerzustände in Spielernummer-Reihenfolge.
## Jeder Eintrag enthält mindestens: player_id, character, color, controller
var players: Array = []

## Spieldauer in Sekunden (aus minigame.json), Standard 30, hartes Maximum 30
var duration: int = 30

## Ergebnis-Modus: "by_points" (höherer score = besser) oder "by_position" (Reihenfolge)
var results_mode: String = "by_points"

## Ob höherer Score besser ist (Standard true; false z.B. für Distanz-/Fehlerwerte)
var higher_is_better: bool = true

## Team-Modus: "ffa" (Standard), "coop_all" (alle gemeinsam), "coop_teams" (2 Teams)
var team_mode: String = "ffa"

## Interne Flags für den Lebenszyklus
var _game_started: bool = false
var _game_ended: bool = false
var _requested_end: bool = false

## Spieler-Scores (player_id -> float), vom Minispiel in der Spielphase gefüllt
var _scores: Dictionary = {}

## Vergangene Spielzeit seit start_game()
var _elapsed: float = 0.0


## Wird vom Framework VOR dem Einfügen in den Szenenbaum aufgerufen.
## Übergibt Lobby-Referenz, Spielerzustände und optionale Parameter aus minigame.json.
func setup(p_lobby, p_players: Array, p_options: Dictionary = {}) -> void:
	players = p_players
	player_count = p_players.size()
	if p_options.has("duration"):
		duration = clampi(p_options["duration"], 10, 30)
	if p_options.has("results_mode"):
		results_mode = p_options["results_mode"]
	if p_options.has("higher_is_better"):
		higher_is_better = p_options["higher_is_better"]
	if p_options.has("team_mode"):
		team_mode = p_options["team_mode"]


## Wird vom Framework nach dem Countdown (LOS) aufgerufen.
## Initialisiert den Spielzustand; ab hier ist Input aktiv.
func start_game() -> void:
	_game_started = true
	_game_ended = false
	_requested_end = false
	_elapsed = 0.0
	for p in players:
		var pid: int = p.player_id
		_scores[pid] = 0.0


## Wird vom Framework bei Timer-Ablauf oder nach request_end() aufgerufen.
## Friert die finale Wertung ein; weitere Eingaben werden ignoriert.
func end_game() -> void:
	_game_ended = true
	_game_started = false


## Liefert die Ergebnisse als Array[Dictionary] mit je player_id und score.
## Wird vom Framework nach end_game() aufgerufen.
func get_results() -> Array:
	var results: Array = []
	for p in players:
		var pid: int = p.player_id
		var score: float = float(_scores.get(pid, 0.0))
		results.append({"player_id": pid, "score": score})
	return results


## Wird vom Framework vor dem Freigeben der Szene aufgerufen.
## Minigame-interne Timer, Signale und Ressourcen werden entfernt.
func cleanup() -> void:
	_scores.clear()
	players.clear()
	_game_started = false
	_game_ended = false
	_requested_end = false


## Hilfsmethode: Score für einen Spieler setzen
func set_player_score(player_id: int, score: float) -> void:
	_scores[player_id] = score


## Hilfsmethode: Score für einen Spieler erhöhen
func add_player_score(player_id: int, delta: float) -> void:
	var current: float = float(_scores.get(player_id, 0.0))
	_scores[player_id] = current + delta


## Hilfsmethode: Score eines Spielers abrufen
func get_player_score(player_id: int) -> float:
	return float(_scores.get(player_id, 0.0))


## Hilfsmethode: Prüft, ob das Spiel noch läuft
func is_game_running() -> bool:
	return _game_started and not _game_ended


## Hilfsmethode: Prüft, ob das Spiel beendet ist
func is_game_ended() -> bool:
	return _game_ended
