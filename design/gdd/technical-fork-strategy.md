# Technische Fork-Strategie — Party Arena

> **Status:** Proposed
> **Version:** 2.0.0
> **Letzte Anderung:** 2026-08-11
> **Abhangigkeiten:** technical-architecture.md, game-concept.md, vision-pillars.md

---

## 1. Overview

Party Arena ist ein **harter Fork** von Super Tux Party (STP). Das bedeutet: Der STP-Code wird als Basis ubernommen, aber **aggressiv und irreversibel modifiziert**. Es ist kein Upstream-Merge geplant, und STP wird nicht als Abhangigkeit gepflegt. Party Arena ist ein eigenstandiges Projekt mit eigener Identitat, eigenen Assets und eigenen Mechaniken.

### Strategische Begrundung

| Grund | Erlauterung |
|---|---|
| **Zeitersparnis** | STP liefert ein funktionierendes Multiplayer-Party-Spiel mit Godot 4.2 — Lobby, Networking, Plugin-System, Board-Logik. Dies von Grund auf neu zu entwickeln wurde ~500+ Stunden kosten. |
| **Technische Basis** | STP's Server-Autoritativ-Architektur, Plugin-System und ENet-Networking sind genau das, was Party Arena braucht. |
| **Divergenz** | Party Arena weicht so stark von STP ab (8 Spieler, neue Wahrung, neue Charaktere, keine KDE/Tux-Referenzen), dass ein Soft-Fork oder Feature-Branches nicht praktikabel sind. |
| **Eigenstandigkeit** | Party Arena soll als eigenstandiges Spiel wahrgenommen werden, nicht als "STP-Reskin". Ein harter Fork unterstreicht diese Eigenstandigkeit. |
| **Kein Upstream-Druck** | STP wird separat weiterentwickelt. Wir wollen nicht gezwungen sein, STP-Anderungen nachzuziehen oder Konflikte zu losen. |

### Was "Harter Fork" konkret bedeutet

1. **Git:** Neues Repository. Kein `git remote` auf STP. Kein `git merge` von STP.
2. **Code:** STP-Code wird kopiert, dann modifiziert. Keine Rucksicht auf STP-Kompatibilitat.
3. **Assets:** Alle STP-Assets werden ersetzt. Keine Tux, KDE, GNU-Referenzen.
4. **Branding:** Alles wird zu "Party Arena" umbenannt. Keine "Super Tux Party" Strings.
5. **Lizenz:** Neue Lizenz-Datei. STP-Lizenz wird entfernt. Credit an STP in `CREDITS.md`.

### Vier Kategorien des Forks

Jede Datei im Projekt gehort zu genau einer von vier Kategorien:

| Kategorie | Bedeutung | Anteil an Codebasis | Geschatzter Aufwand |
|---|---|---|---|
| **A — DIREKT UBERNEHMEN** | Unverandert aus STP kopiert. Keine Anderungen notig. | ~15 % | 0 h |
| **B — MODIFIZIEREN** | STP-Code als Basis, substanzielle Anderungen (8P, neue Konstanten, neues Branding). | ~40 % | ~40 h |
| **C — KOMPLETT NEU SCHREIBEN** | STP-Code dient als Referenz fur Struktur/APIs, aber die Logik wird komplett ersetzt. | ~15 % | ~80 h |
| **D — KOMPLETT NEU** | Existiert in STP nicht. Wird von Grund auf neu entwickelt. | ~30 % | ~200 h |

### Migrations-Roadmap (5 Phasen)

```
Phase 1: Fork erstellen         Phase 2: Kategorie A+B       Phase 3: Kategorie C
(STP kopieren, Git aufraumen) → (Ubernehmen + Modifizieren) → (Core-Logik neuschreiben)
     ↓                              ↓                              ↓
   1 Tag                          2 Wochen                       3 Wochen

Phase 4: Kategorie D            Phase 5: Polish & QA
(Neue Plugins + Assets)      → (Bugfixes, Balancing, Loc)
     ↓                              ↓
   6 Wochen                       2 Wochen
```

---

## 2. Player Fantasy

Die Fork-Strategie ist fur den Spieler vollstandig unsichtbar — und das ist beabsichtigt. Der Spieler soll Party Arena als ein **eigenstandiges, neues Spiel** erleben, nicht als Mod oder total conversion.

### Was der Spieler NICHT merken soll

- Keine "Super Tux Party" Schriftzuge in Fehlermeldungen oder Logs.
- Keine Tux-Pinguine, KDE-Drachen oder GNU-Gnus in Assets oder Code.
- Keine "Cookies" oder "Cakes" — es gibt nur "Munzen" und "Sterne".
- Keine Referenzen auf Linux/Kernel/Open-Source-Kultur.
- Keine STP-spezifischen UI-Elemente (alte Icons, alte Farben, alte Layouts).
- Keine STP-Minispiele (Kernel-Compiling, etc.).
- Kein STP-Charakter im Charakter-Auswahl-Screen.

### Was der Spieler merken SOLL

- **Eigenstandigkeit:** Party Arena hat eine eigene visuelle Identitat (Cartoon-Stil, Insel-Thema, Arenians).
- **Polished Experience:** Das Spiel fuhlt sich "fertig" an, nicht wie ein Work-in-Progress-Fork.
- **Konsistenz:** Alle Texte, Menus, Sounds und Charaktere passen thematisch zusammen. Ein einziger, durchgehender Look & Feel.
- **Mehr Spieler:** 8 Spieler statt 4 — das ist ein Quantensprung fur Party-Abende.
- **Neue Mechaniken:** Stern-Wanderung, Bonus-Sterne, Catch-Up-System — all das gab es in STP nicht.

### Was der Entwickler merken soll

- **Klare Trennung:** Jede Datei gehort zu einer der vier Kategorien (A, B, C, D). Kein "Weiss nicht, ob ich das andern darf".
- **Minimale Uberraschungen:** Die Fork-Strategie dokumentiert STP-spezifische Elemente, die entfernt werden mussen, bevor sie zu Bugs werden.
- **Saubere Codebasis:** Nach der Migration gibt es keinen toten Code, keine auskommentierten STP-Referenzen, keine verwaisten Assets.

---

## 3. Detailed Rules

### 3.1 Kategorie A — DIREKT UBERNEHMEN (keine oder minimale Anderungen)

Diese Dateien werden aus dem STP-Fork **unverandert ubernommen**. Sie enthalten allgemeine Hilfsfunktionen, UI-Komponenten und Infrastruktur, die unabhangig vom Spiel-Thema sind.

#### A1: Hilfsfunktionen

| Datei | Inhalt | Grund fur Ubernahme |
|---|---|---|
| `common/scripts/utility.gd` | Math-, Array-, RNG-Hilfsfunktionen | Generisch, kein STP-Bezug. `randi_range`, `clamp`, Array-Shuffle, Gewichtete-Zufallsauswahl, String-Helfer. |
| `common/scripts/control_helper.gd` | UI-Navigation: Focus-Management, Button-Gruppen, Tabbing | Generisch, kein STP-Bezug. Wird fur alle Menus gebraucht. |
| `common/scripts/tracking_manager.gd` | Analyse-Tracking (optional, nur Debug-Build) | Generisch, kein STP-Bezug. Optionaler Telemetrie-Service. |

#### A2: UI-Basiskomponenten

| Datei | Inhalt | Grund fur Ubernahme |
|---|---|---|
| `common/scenes/sound_button/` | UI-Button mit integriertem Sound-Feedback (Hover, Click) | Generisch, kein STP-Bezug. Button-Logik unabhangig vom Theme. Texturen werden in Kat B ausgetauscht. |
| `common/scenes/countdown/` | 3-2-1-GO Countdown-Animation (visuell + Audio) | Generisch. Logik bleibt gleich. Texturen/Sounds werden in Kat B auf PA-Theme aktualisiert. |
| `common/scenes/overlay/` | Overlay-Container fur modale Dialoge (falls vorhanden) | Generisch. Container-Logik unabhangig vom Inhalt. |

#### A3: Plugin-Infrastruktur

| Datei | Inhalt | Grund fur Ubernahme |
|---|---|---|
| `common/scripts/loader/plugin_system.gd` | Plugin-Basisklasse: Discovery (`DirAccess`), `plugin.json`-Parser, Plugin-Ladung (.pck/.zip), Plugin-Cache, Plugin-API | Kern des Plugin-Systems. Komplett generisch — es scannt Ordner, liest JSON, ladt Ressourcen. Kein STP-Bezug. |
| `common/scripts/loader/board_loader.gd` | Board-Plugin-Loader (Basis) | Basis-Logik generisch. **ABER:** STP-spezifische Board-Enum-Prufung muss entfernt werden (Kategorie-B-Anderung an derselben Datei). |
| `common/scripts/loader/character_loader.gd` | Charakter-Plugin-Loader (Basis) | Basis-Logik generisch. Erbt von `plugin_system.gd`. |
| `common/scripts/loader/item_loader.gd` | Item-Plugin-Loader (Basis) | Basis-Logik generisch. Erbt von `plugin_system.gd`. |
| `common/scripts/loader/minigame_loader.gd` | Minispiel-Plugin-Loader (Basis) | Basis-Logik generisch. Erbt von `plugin_system.gd`. |

#### A4: Speicher-System

| Datei | Inhalt | Grund fur Ubernahme |
|---|---|---|
| `common/savegames/savegames.gd` | SaveGame-Klasse: Serialisierung (ConfigFile/Dictionary), Datei-I/O, Versionierung, Migration alter Savegames | Komplett generisch. Wird fur PA-Spielstande konfiguriert (andere Keys, aber gleiche Mechanik). |

#### A5: Addons

| Datei | Inhalt | Grund fur Ubernahme |
|---|---|---|
| `addons/*` | Godot-Addons (z.B. godot-sqlite, eventuell gdUnit4 fur Testing) | Unverandert von STP. Keine STP-spezifischen Addons. |

#### A6: Weitere generische Dateien

| Datei | Inhalt | Grund fur Ubernahme |
|---|---|---|
| `default_env.tres` | Default WorldEnvironment (Himmel, Umgebungslicht) | Generisch, wird in Kat B mit PA-Farben uberschrieben. |
| `export_presets.cfg` | Godot-Export-Voreinstellungen | Generisch. PA-Pfade in Kat B aktualisiert. |
| `export_presets_ci.cfg` | CI-Export-Voreinstellungen | Generisch. Gleiche Aktualisierung wie `export_presets.cfg`. |

#### A7: Container-Szenen (leere Node-Strukturen)

Alle `.tscn`-Dateien, die nur Container/Node-Struktur ohne STP-spezifische Texturen/Scripts sind. Die Struktur bleibt erhalten, Inhalte (Texturen, Scripts) werden in Kat B ausgetauscht.

### 3.2 Kategorie B — MODIFIZIEREN (an 8 Spieler und neue Mechaniken anpassen)

Diese Dateien werden **modifiziert**, aber nicht komplett neu geschrieben. Die Grundstruktur bleibt, aber Konstanten, Limits, Referenzen und UI werden erweitert.

#### B1: Globale Konstanten und State — `common/scripts/global.gd`

| Anderung | Vorher (STP) | Nachher (PA) |
|---|---|---|
| `VERSION` | `"1.x"` | `"2.0.0"` |
| `GAME_NAME` | `"Super Tux Party"` | `"Party Arena"` |
| `COOKIES_FOR_CAKE` | `30` | Entfernt. Neu: `MUENZEN_FUER_STERN = 20` |
| `MAX_TURNS` | `10` | `10` (bleibt) |
| `MAX_ITEMS` | Nicht definiert (implizit unbegrenzt) | `3` |
| `MAX_PLAYERS` | Nicht definiert (implizit 4) | `8` |
| `LOBBY_SIZE` | `4` | `8` |
| `START_COINS` | `5` | `10` |
| `DICE_MIN` | `1` | `1` (bleibt) |
| `DICE_MAX` | `6` | `6` (bleibt) |
| `LUCKY_DICE_VALUE` | Nicht definiert | `5` |
| `COIN_MAGNET_DURATION` | Nicht definiert | `3` |
| `EVENT_BONUS_COINS` | Nicht definiert | `10` |
| `MINIGAME_WINNER_COINS` | `10` | `10` (bleibt) |
| `MINIGAME_2ND_COINS` | `5` | `5` (bleibt) |
| `MINIGAME_3RD_COINS` | Nicht definiert | `3` |
| `MINIGAME_DURATION_DEFAULT` | Nicht definiert | `30` |
| `BOARD_FIELDS` | `40` | `40` (bleibt) |
| `MAX_TURN_TIMEOUT` | Nicht definiert | `30` |
| `SHOP_TIMEOUT` | Nicht definiert | `15` |
| `PATH_CHOICE_TIMEOUT` | Nicht definiert | `10` |
| `MINIGAME_LOAD_TIMEOUT` | Nicht definiert | `10` |
| `SERVER_PORT` | `10567` | `10567` (bleibt) |
| `PLAYER_TRANSLATION` | Array mit 4 Vector2-Eintragen | Array mit 8 Eintragen |
| `PLAYER_COLORS` | 4 Farben | 8 Farben (Rot, Blau, Grun, Gelb, Orange, Lila, Cyan, Pink) |
| Autoload-Liste | STP-spezifische Autoloads | PA-spezifische Autoloads (neue hinzufugen: EventSystem, BonusStar) |
| Strings | "Cookies"/"Cakes"/"Sara"/"Nolok"/"GNU" | "Munzen"/"Sterne"/"ArenaStar" — alle String-Literale ersetzen |

#### B2: Player-Board (Spieler-Darstellung) — `common/scenes/board_logic/player_board/player_board.gd`

| Anderung | Beschreibung |
|---|---|
| `PLAYER_TRANSLATION` Array | Von 4 auf 8 Positionen erweitert. Berechnung: Kreis-Pattern (Winkel = `player_id * (2*PI/8)`, Radius = 0.5) oder Grid-Pattern (4×2). |
| `_get_player_translation(player_id)` | Unterstutzt jetzt IDs 1–8. Gultigkeitsprufung: `player_id < 1 or player_id > 8` → Fehler. |
| Splitscreen-Layout | 2×2 fur 2–4 Spieler, Shared Screen fur 5–8. Neue Viewport-Logik. |
| Charakter-Referenz | Nicht mehr STP-Charaktere (Tux, etc.), sondern Arenians. Alle Pfade auf `plugins/characters/<arenian>/` umleiten. |
| Spieler-Farben | 8 unterscheidbare Farben: Rot `#ff3333`, Blau `#3366ff`, Grun `#33ff66`, Gelb `#ffe633`, Orange `#ff8c33`, Lila `#b333ff`, Cyan `#33ffee`, Pink `#ff33a8`. |
| Animations-Speed | Fur entfernte Charaktere: Reduzierte Animations-Framerate (15 FPS statt 30 FPS) via Animations-LOD. |
| Figuren-Offset bei Uberlappung | Wenn >1 Spieler auf demselben Feld: Kreis-Pattern um die Feld-Position, Radius 0.5 Einheiten, Winkel basierend auf player_id. Maximal 8 Spieler auf einem Feld. |
| Hover-Nameplate | Namensschild uber jedem Charakter, zeigt Spielername + aktiver-Spieler-Indikator (pulsierend). |

#### B3: Client Game Manager — `client/game.gd`

| Anderung | Beschreibung |
|---|---|
| 8P Splitscreen-Setup | Viewport-Container fur bis zu 8 Spieler (max 4 Split-Views). Neue Layouts: 2P horizontal, 3P mixed, 4P 2×2 Grid. 5–8P: Shared Screen (eine Kamera). |
| ArenaStar-Integration | Referenz auf `arena_star.gd` und `arena_star.tscn`. ArenaStar-Node in Szene einfugen. |
| UI-Referenzen | Neue UI-Pfade: Character Select, Board Select, neue Victory-Screen-Pfade, neue Reward-Screen-Pfade. |
| HUD-Update | 8 Spieler-Info-Panels statt 4. Player-Info-Array/Dictionary fur 8 Eintrage. |
| Minispiel-Lade-Bildschirm | Neue Assets (Loading-Spinner, "Minispiel wird geladen"-Text), neues Artwork. |
| Game-State-Empfang | `_rpc_sync_game_state`-Handler fur 8 PlayerData-Eintrage und neues BoardData-Format. |
| Disconnect-Indikator | Anzeige fur disconnectete Spieler (grau/transparent, KI-Icon). |
| Screen-Shake-Manager | Globaler Screen-Shake (einstellbar in Accessibility: reduziert/aus). |

#### B4: Client Lobby — `client/lobby.gd`

| Anderung | Beschreibung |
|---|---|
| `LOBBY_SIZE` | `8` (Konstante). Alle Arrays/Dictionaries fur 8 Spieler. |
| Lobby-UI | 8 Spieler-Slots (statt 4). Jeder Slot: Name, Charakter-Portrat, Ready-Indikator. |
| Charakter-Auswahl-Integration | Verweis auf `client/menus/characters/character_select.tscn`. Offnet Character-Select-Screen bei Klick auf Slot. |
| Board-Auswahl-Integration | Verweis auf `client/menus/boards/board_select.tscn`. Host-button offnet Board-Select-Screen. |
| Ready-Status-Anzeige | 8 Ready-Indikatoren (leer = nicht bereit, Haken = bereit). |
| Server-Browser (optional) | Liste verfugbarer Server im lokalen Netzwerk (UDP-Broadcast). Anzeige: Server-Name, Spielerzahl (z.B. "3/8"), Board, Ping. |

#### B5: Client Menus — Alle Dateien in `client/menus/`

| Datei | Anderung |
|---|---|
| `main_menu.tscn` + `main_menu.gd` | Neues Cartoon-Design. Buttons: "Lokales Spiel", "Online-Spiel", "Einstellungen", "Credits", "Beenden". ArenaStar schwebt im Hintergrund. Keine STP-Referenzen. |
| `lobby/servermenu.tscn` + `servermenu.gd` | 8P-Lobby: Server-Liste zeigt Spielerzahl 1/8 bis 8/8. "Server erstellen"-Button mit Board-Auswahl. |
| `lobby/lobby_menu.tscn` + `lobby_menu.gd` | 8P-Lobby-UI: 8 Slots, Chat-Fenster, Start-Button (nur Host). |
| `lobby/character_menu.tscn` + `character_menu.gd` | Neue Charakter-Menu-Integration: Verlinkt auf externen Character-Select-Screen. |
| `pause_menu.tscn` + `pause_menu.gd` | Neues Design. Optionen: "Fortsetzen", "Einstellungen", "Spiel speichern", "Spiel verlassen". |
| `options_menu.tscn` + `options_menu.gd` | Neue Optionen: Audio (Master, Musik, SFX, Stimme), Video (Auflosung, Vollbild, VSync, AA, Render-Skalierung, Schatten, Textur-Qualitat, Partikel), Sprache (DE, EN, FR, ES, JA, ZH), Accessibility (Untertitel, Farbenblind-Modus, reduzierte Bewegung, hoher Kontrast, Mono-Audio), Steuerung (Remapping pro Spieler). |
| `victory_screen/victory_screen.tscn` + `victory_screen.gd` | 8P Victory: Platzierungen 1–8 als animierte Liste, Bonus-Sterne-Detail (zeige welche Kategorie welcher Spieler gewonnen hat), Siegerpose des 1. Platzes, Statistik-Ubersicht pro Spieler, "Erneut spielen" + "Hauptmenu" Buttons. |
| `rewardscreens/ffa/ffa_rewardscreen.tscn` + `.gd` | 8P FFA Rewards. War 4P. Neue Munz-Verteilung: 1. Platz +10, 2. Platz +5, 3. Platz +3, Rest +0. Catch-Up-Bonus-Anzeige. |
| `rewardscreens/duel/` | **ENTFERNEN** — Kein Duel-Modus in Party Arena. Kompletter Ordner wird geloscht. |

#### B6: Server Game Manager — `server/game.gd`

| Anderung | Beschreibung |
|---|---|
| 8P Initialisierung | `MAX_PLAYERS = 8`, Arrays/Dictionaries fur 8 Spieler. Player-Slots 1–8. |
| Neue Spiel-Logik | Stern-Kauf (`MUENZEN_FUER_STERN = 20`), Bonus-Sterne (Aufruf von `bonus_star.gd`), Catch-Up-Mechanik (Bonus-Munzen fur letzte Platze). |
| Minispiel-Queue | 8P Minigame-Queue: Nur Minispiele die 8P unterstutzen (`max_players >= 8`). |
| Disconnect-Handling | KI fur bis zu 7 disconnectete Spieler (STP: 3). Auto-Wurfel nach 5s (statt 30s fur normale Spieler). Auto-Pass bei Shops. Zufallige Pfadwahl. Letzter Platz in Minispielen. |
| RPC-Validierung | Jede Client-Aktion wird gegen Server-State validiert (Munzen, Position, Phase, Items). Neue Validierungen fur PA-Mechaniken. |
| RPCs fur neue Systeme | Neue RPCs: `_rpc_buy_star`, `_rpc_buy_item`, `_rpc_use_item`, `_rpc_choose_path`, `_rpc_minigame_result`, `_rpc_bonus_stars`, `_rpc_star_migration`. |

#### B7: Server Lobby — `server/lobby.gd`

| Anderung | Beschreibung |
|---|---|
| `LOBBY_SIZE` | `8` (Konstante). Max Clients: 8. |
| `MIN_PLAYERS_TO_START` | `2` (bleibt). |
| Charakter-Auswahl-Logik | First-Come-First-Served fur 8 Arenians. Server validiert: Charakter existiert? Bereits gewahlt? |
| Board-Auswahl-Logik | 8 Inseln zur Auswahl. Host wahlt Board. Server validiert: Board existiert als Plugin? |
| Lobby-RPCs | `_rpc_lobby_player_joined`, `_rpc_lobby_player_left`, `_rpc_lobby_character_changed`, `_rpc_lobby_board_changed`, `_rpc_lobby_player_ready`, `_rpc_lobby_start_countdown`. |

#### B8: Minispiel-Queue — `server/minigame_queue.gd`

| Anderung | Beschreibung |
|---|---|
| Spielerzahl-Prufung | Minispiele mit `max_players >= active_player_count` auswahlen (nicht `>= 4` wie in STP). |
| Kategorie-Gewichtung | 5 PA-Kategorien (Geschicklichkeit, Reaktion, Puzzle/Logik, Rechnen/Wort, Kooperation). Gewichtung nach Abwechslung (nicht zwei Gleiche hintereinander). |
| Turn-Tracker | Nach 3 Runden ohne Minispiel → Minispiel wird forciert. |

#### B9: Weitere Modifikationen

| Datei | Anderung |
|---|---|
| `player_info.tscn` + `player_info.gd` | 8 Spieler-HUD-Elemente statt 4. Neue Anzeige: Munzen, Sterne, Items (Icons), Schild-Indikator, Munz-Magnet-Indikator. |
| `shop.tscn` + `shop.gd` | Zwei Shop-Typen: Stern-Shop + Item-Shop. Neue Preise: Stern = 20 Munzen, Items = 3–8 Munzen. Neue Shop-UI (Cartoon-Stil). |
| `shop_item.tscn` + `shop_item.gd` | Neue Item-Icons, Beschreibungen, Preise. Drei Items pro Shop. |
| `project.godot` | `config/name = "Party Arena"`, `config/version = "2.0.0"`, `run/main_scene = "res://client/menus/main_menu.tscn"`, InputMap: 10 Actions × 8 Spieler = 80 Eintrage, neue Autoloads (EventSystem, BonusStar), Fenster-Icon: `icon.webp` (neu). |
| `assets/defaults/default_theme.tres` | Neuer Cartoon-Theme: Fonts (1–2 Schriftarten), Farben (helle Pastell-Basis + satte Akzente), Button-Styles (abgerundet, mit Schatten, Hover-Vergrosserung), Panel-Styles (abgerundet, mit Umrandung). |
| `export_presets.cfg` | Neue Export-Presets: Windows Desktop (64-bit), Linux (64-bit), macOS (Universal). Keine mobilen Presets in v2.0.0. |

### 3.3 Kategorie C — KOMPLETT NEU SCHREIBEN (STP-Code als Referenz, Kern-Logik ersetzt)

Diese Dateien werden **komplett neu geschrieben**. Der alte STP-Code dient als Referenz fur Struktur und APIs, aber die Logik wird vollstandig ersetzt.

#### C1: Board Controller (Kern-Spielfluss) — `common/scenes/board_logic/controller/controller.gd`

**Warum Rewrite:** Der STP-Controller ist tief mit 4-Spieler-Logik, Cookie/Cake-Wahrung, Nolok/GNU-Events und STP-spezifischen Mechaniken verwoben. Ein Rewrite ist sauberer als inkrementelle Anderungen — das Risiko, eine STP-Abhangigkeit zu ubersehen und einen subtilen Bug zu produzieren, ist zu hoch.

**STP Phasen-Struktur (alt):**
- `ROLL` → Spieler wurfelt
- `MOVE` → Figur bewegt sich
- `SHOP` → Cookie-Shop an fixer Position
- `NOLOK_EVENT` → Nolok-Event (falls auf Nolok-Feld gelandet)
- `GNU_EVENT` → GNU-Event (falls auf GNU-Feld gelandet)
- `DUEL` → Duel-Minispiel (falls auf Duel-Feld gelandet)
- `MINIGAME` → Normales Minispiel

**PA Phasen-Struktur (neu):**
- `ROLL` → Spieler wurfelt (mit Item-Modifikationen)
- `MOVE` → Figur bewegt sich (mit Pfadwahl an Abzweigungen)
- `EVENT` → Feld-Ereignis auslosen (START/STAR_SHOP/ITEM_SHOP/EVENT/LUCK/COIN_BONUS/MINIGAME)
- `SHOP` → Shop-Interaktion (Stern-Kauf, Item-Kauf)
- `MINIGAME` → Minispiel (immer am Runden-Ende, nicht nur bei MINIGAME-Feld)
- `STAR` → Stern-Wanderung prufen, Stern-Phase
- `BONUS_STARS` → Bonus-Sterne berechnen (nur nach letzter Runde)
- `VICTORY` → Sieger-Zeremonie (nur nach Bonus-Sternen)

**Neue Controller-Struktur (konzeptionell):**

Der Controller implementiert einen endlichen Automaten mit Zustanden (Phasen) und definierten Ubergangen. Der aktive Spieler wird aus der Zug-Reihenfolge (einmalig vor Runde 1 per Vorrunden-Wurfel bestimmt, fur gesamte Partie fixiert) ermittelt. Jede Phase lauft vollstandig ab, bevor die nachste betreten wird.

*Runden-Hauptschleife:*
1. Fur jeden Spieler in Zug-Reihenfolge: `_process_turn(player)`
2. `_phase_roll(player)` — Spieler wurfelt (mit Timeout 30s, Auto-Wurfel bei Timeout). Item-Modifikationen werden vor der Zufallszahl-Generierung gepruft.
3. `_phase_move(player, dice_value)` — Figur bewegt sich Feld fur Feld um `dice_value` Schritte. Bei Abzweigungen: Pfadwahl-Dialog (Timeout 10s, Auto-Wahl erster Pfad). Bei Uberschreiten des Startfelds: Umlauf-Zahler erhohen.
4. `_phase_event(player, target_field)` — Ziel-Feld auswerten:
   - `START`: Kein Effekt.
   - `STAR_SHOP`: Stern-Kauf-Prufung (genug Munzen? Stern verfugbar?).
   - `ITEM_SHOP`: Item-Kauf-Prufung (Inventar voll? genug Munzen?).
   - `EVENT`: Zufalliges Event aus `event_pool` des Feldes ziehen und ausfuhren.
   - `LUCK`: Glucks-Event (Munz-Gewinn oder -Verlust, 50/50-Chance, Betrag 3–8).
   - `COIN_BONUS`: Fixer Munz-Bonus gutschreiben (Wert aus Feld-Daten).
   - `MINIGAME`: Marker setzen (Minispiel wird NACH allen Spielerzugen ausgelost, nicht sofort).
5. Nach dem letzten Spieler: `_phase_minigame()` — Minispiel aus Minigame-Queue auswahlen und starten. Minispiel-Ergebnisse verarbeiten, Munz-Belohnungen verteilen, Catch-Up-Bonus anwenden.
6. `_phase_star()` — Stern-Kauf-Fenster fur berechtigte Spieler. Stern-Wanderung nach jedem Kauf. Runden-Zusammenfassung anzeigen.
7. Runden-Zahler erhohen. Wenn letzte Runde → `_calculate_bonus_stars()` → `_calculate_final_rankings()` → `_phase_victory()`.

#### C2: Node-Board (Feldtypen) — `common/scenes/board_logic/node/node.gd`

**Warum Rewrite:** Das STP-Node-System hat harte Referenzen auf Nolok/GNU und verwendet ein komplett anderes Feldtyp-Enum. Die visuelle Reprasentation, die Event-Logik und die Shop-Logik sind alle STP-spezifisch.

**STP Feldtyp-Enum (alt — wird KOMPLETT ERSETZT):**
- `BLUE` — Normales Feld (gibt Cookies)
- `RED` — Gefahren-Feld (verliert Cookies)
- `GREEN` — Glucks-Feld
- `YELLOW` — Bonus-Feld
- `SHOP` — Cookie-Shop
- `NOLOK` — Nolok-Event
- `GNU` — GNU-Event

**PA Feldtyp-Enum (neu):**
- `START` — Startfeld (kein aktiver Effekt). Nur 1× pro Board (Index 0). Alle Spieler starten hier. Visuell: Arena-Tor oder Bogen.
- `STAR_SHOP` — Sternen-Shop (Stern kaufen fur 20 Munzen). 2–3× pro Board. Nur das aktive Feld hat die Sternen-Statue sichtbar. Visuell: Goldene Saule mit Stern-Symbol.
- `ITEM_SHOP` — Item-Shop (Items kaufen fur 3–8 Munzen). 2× pro Board (fixe Positionen, wandern nicht). Visuell: Bunter Marktstand mit Geschenkbox-Icon.
- `EVENT` — Zufalls-Event aus `event_pool`. 5–8× pro Board. Visuell: Leuchtendes "?"-Feld mit pulsierendem Farbwechsel.
- `LUCK` — Glucks-Feld (Munzen +/- nach Zufall). 3–4× pro Board. Visuell: Kleeblatt (grun) oder Wolke mit Blitz (grau), je nach Ausgang.
- `COIN_BONUS` — Munz-Bonus (fixer Betrag). 4× pro Board. Visuell: Goldene Munz-Haufen mit leuchtendem Wert (3, 5, oder 8).
- `MINIGAME` — Minispiel-Trigger. 4–6× pro Board. Visuell: Arena-Banner mit Spiel-Controller-Icon. Lost KEIN sofortiges Minispiel aus (das kommt am Runden-Ende), sondern dient als Marker.

**Neue Node-Struktur (konzeptionell):**

Jedes Node-Board-Feld halt folgende Daten und Methoden:
- `field_type: String` — Einer der 7 Typen (START, STAR_SHOP, etc.)
- `field_index: int` — Eindeutiger Index (0–39)
- `next_indices: Array[int]` — 1–3 nachste Felder (1 = kein Abzweigung, >1 = Abzweigung)
- `prev_indices: Array[int]` — 1–3 vorherige Felder
- `is_branch_decision: bool` — true wenn `next_indices.size() > 1`
- `coin_bonus_value: int` — Munz-Bonus (nur fur COIN_BONUS, sonst 0)
- `event_pool: Array[String]` — Event-IDs (nur fur EVENT, sonst leeres Array)
- `minigame_tier: String` — "LEICHT"/"MITTEL"/"SCHWER" (nur fur MINIGAME)
- `branch_labels: Array[String]` — UI-Labels fur Abzweigungen (z.B. ["Sonnenpfad", "Schattenweg"])
- `visual_position: Vector3` — 3D-Position des Feldes
- `visual_rotation: float` — Rotation des Feldes in Grad
- `execute_field_event(player: PlayerData) -> void` — Fuhrt den Feld-Effekt basierend auf `field_type` aus
- `get_visual_indicator() -> Node3D` — Gibt den visuellen Indikator zuruck (Stern-Saule, Shop-Stand, Event-"?", etc.)

#### C3: Server Game Logic (Teile) — `server/game.gd` (partieller Rewrite)

Die grundlegende Server-Struktur bleibt erhalten (Kategorie B), aber spezifische Logik-Teile werden neu geschrieben:

- **Stern-Kauf-Logik:** Pruft `player.coins >= 20`, `player.position == active_star_shop_index`, `star_available == true`. Zieht 20 Munzen ab, erhoht `player.stars`, lost Stern-Wanderung aus.
- **Stern-Wanderungs-Logik:** Wahlt neues Sternen-Shop-Feld aus `star_shop_positions` (nie das aktuelle, bevorzugt unbesetzt). Bei besetztem Ziel: Registriert Kauf-Fenster B fur den dortigen Spieler.
- **Bonus-Sterne-Berechnung:** Ruft `bonus_star.gd` auf. 3 Kategorien aus 10er-Pool ziehen. Pro Kategorie alle Spieler auswerten, Gewinner ermitteln (+1 Stern). Bei Gleichstand: Mehrere Gewinner (alle +1 Stern).
- **Catch-Up-Mechanik:** Letzter Platz in Minispielen erhalt +3 Munzen, Vorletzter +1 (bei 5+ Spielern). Event-Skalierung: Positive Events geben mehr fur niedrig platzierte Spieler.
- **Spiel-Ende-Logik:** Finale Rankings berechnen (1. Sterne, 2. Munzen, 3. Minispiel-Siege). Bonus-Sterne anwenden. Reranking. Sieger ermitteln. Sieges-Nachricht an alle Clients.

### 3.4 Kategorie D — KOMPLETT NEU (existiert in STP nicht)

Diese Dateien existieren in STP uberhaupt nicht und werden von Grund auf neu entwickelt.

#### D1: Neue Plugins

| Plugin-Typ | Anzahl | Ordner | Beschreibung |
|---|---|---|---|
| Insel-Boards | 8 | `plugins/boards/<name>/` | Sonnenstrand, Korallenriff, Vulkaninsel, Nebelwald, Kristallhohle, Wolkenreich, Zeitgarten, Schattenarchipel. Jedes Board enthalt: `plugin.json` (Manifest), `board.tscn` (40-Felder-Layout), `fields.json` (FieldData-Array), Texturen/Modelle (.glb, .webp), Board-Musik (.ogg). |
| Arenian-Charaktere | 8 | `plugins/characters/<name>/` | Brix (Stein-Golem), Nixie (Axolotl), Koko (Panda), Pip (Flughornchen), Zara, Flint, Luna, Momo. Jeder Charakter enthalt: `character.json` (Manifest), `model.glb` (3D-Modell mit Rig), `portrait.webp` (Portrat), `icon.webp` (Mini-Icon), `voice/` (Voice-Lines), AnimationTree-Konfiguration. |
| Items | 5 | `plugins/items/<name>/` | Glucks-Wurfel, Schutzschild, Munz-Magnet, Teleporter, Diebhandschuh. Jedes Item enthalt: `item_definition.json` (Manifest), `model.glb` (3D-Modell), `icon.webp` (Icon), `sfx_use.ogg` (Verwendungs-Sound). |
| Minispiele | 12 | `plugins/minigames/<name>/` | Munzregen, Schildkrotenrennen, Kokosnuss Werfen, Krabben Jagd, Muschel Memory, Wellen Reiten, Perlen Tauchen, Vulkan Ausbruch, Laternen Flug, Brucken Bau, Nebel Irrgarten, Schatz Trage. Jedes Minispiel enthalt: `minigame.json` (Manifest), `minigame.tscn` (Szene), `minigame.gd` (Logik), Texturen/Modelle/Sounds. |

#### D2: Neue Core-Systeme

| Datei | Beschreibung |
|---|---|
| `common/scenes/board_logic/controller/arena_star.gd` | ArenaStar Controller: 3D-Modell-Instanziierung, schwebende Animation (sanftes Auf-und-Ab, Rotation, Glitzern), Positions-Tracking (uber dem aktiven Sternen-Shop), Sternen-Statue-Visualisierung, Wanderungs-Animation (Verschwinden/Auftauchen mit Partikel-Effekt), Verfugbarkeits-Indikator (leuchtend = Stern verfugbar, grau = bereits gekauft). |
| `common/scenes/board_logic/controller/arena_star.tscn` | ArenaStar 3D-Modell + Partikel-Effekte + Licht-Quelle. Textur: goldener Stern mit Krone, Cartoon-Style. Animationen: idle (schweben + glitzern), celebrate (wirbeln + Stern-Regen), sad (sacken + dimmen), dramatic (vergro"sern + Spot-Licht). |
| `common/scripts/event_system.gd` | Event-System: Definition aller Events (ca. 20 Events: 8 positive, 8 negative, 4 neutrale). Pro Event: ID, Beschreibung, Effekt-Typ (add_coins, remove_coins, add_item, remove_item, teleport_random, teleport_star, skip_turn, extra_roll, shield_grant, coin_multiplier_grant). Event-Pool-Zuordnung pro Board und Feld. Auswahl-Algorithmus (Gleichverteilung aus Pool, Regel "kein 2× hintereinander"). Catch-Up-Skalierung (Event-Starke skaliert mit Ruckstand in der Rangliste). Event-Ausfuhrung (sofortige Anwendung, ArenaStar-Kommentar). |
| `common/scripts/bonus_star.gd` | Bonus-Stern-System: 10 Kategorien definiert. Pro Kategorie: Name, Messkriterium, Berechnungslogik. Auswahl von 3 Kategorien per Gleichverteilung am Spielende. Berechnung: Fur jede Kategorie alle Spieler auswerten, Spieler mit hochstem Wert erhalt +1 Stern. Bei Gleichstand: Alle Gleichstandigen erhalten +1 Stern. Kategorien: Munz-Konig (meiste Munzen gesamt uber alle Runden), Minispiel-Meister (meiste 1. Platze in Minispielen), Ereignis-Held (meiste Events ausgelost), Viellaufer (meiste Felder gereist), Pechvogel (haufigster Munz-Netto-Verlust durch Events), Kampfer (meiste Runden auf dem letzten Platz verbracht), Gluckspilz (hochster durchschnittlicher Wurfel-Wert), Kaufer (meiste Items gekauft), Sammler (gro"ste Item-Vielfalt im Inventar uber alle Runden), Sternen-Jager (am haufigsten auf Sternen-Shop-Feld gelandet ohne zu kaufen). |

#### D3: Neue Menu-Szenen

| Datei | Beschreibung |
|---|---|
| `client/menus/characters/character_select.tscn` | Charakter-Auswahl-Screen: 8 Arenians in 2 Reihen zu je 4. Jeder Slot: 3D-Modell-Vorschau (drehend), Name, Heimat-Insel-Icon, Kurzbeschreibung, Signaturfarbe-Indikator. Auswahl per Klick/Gamepad. Bestatigung: "Bereit" Button. First-Come-First-Served: Bereits gewahlte Charaktere sind ausgegraut und mit Spielername des Wahlers markiert. |
| `client/menus/characters/character_select.gd` | Charakter-Auswahl-Logik: Slot-Navigation (Gamepad: D-Pad/Stick, Maus: Klick), Auswahl-Hervorhebung (Leucht-Umrandung), Bestatigung (RPC an Server), Konflikt-Erkennung (falls Charakter inzwischen vergeben), 3D-Modell-Rotation (langsame Y-Achsen-Drehung). |
| `client/menus/boards/board_select.tscn` | Insel-Auswahl-Screen: 8 Inseln in 2 Reihen zu je 4. Jeder Slot: Board-Vorschau-Bild (Thumbnail), Insel-Name, Schwierigkeits-Indikator (Sterne: 1–5), Event-Haufigkeit (Balken: wenige/mittel/viele Events), Mini-Map des Board-Layouts. Host-beschrankt: Nur der Host kann auswahlen, andere sehen Vorschau passiv. |
| `client/menus/boards/board_select.gd` | Insel-Auswahl-Logik: Host-exklusive Interaktion (andere Spieler sehen nur), Auswahl-Hervorhebung, Bestatigung (RPC an Server), Board-Preview-Animation (Kamera-Flug uber das Mini-Board). |

#### D4: Neue Assets

| Ordner | Inhalt | Geschatzter Umfang |
|---|---|---|
| `assets/models/characters/` | 8 Arenian 3D-Modelle (.glb), LOD0 (5000 Tris) + LOD1 (1500 Tris). Inkl. Rig (Standard-Skelett mit 6 Animationen) und Inverted-Hull-Outlines. | 8 Dateien, ~40 MB |
| `assets/models/boards/` | 8 Insel-Board-Modelle (.glb). 40 Felder + Startbereich + Dekoration. Max 20000 Tris pro komplettem Board. | 8 Dateien, ~80 MB |
| `assets/models/items/` | 5 Item-Modelle (.glb). Glucks-Wurfel, Schutzschild, Munz-Magnet, Teleporter-Wirbel, Diebhandschuh. Max 500 Tris pro Item. | 5 Dateien, ~5 MB |
| `assets/models/props/` | ArenaStar (2000 Tris), Dekorationen (Palmen, Fackeln, Steine, Blumen, Wasserfalle, Laternen, Brucken, Schatztruhen). | ~20 Dateien, ~30 MB |
| `assets/textures/characters/` | 8 Charakter-Texturen (Diffuse, 1024×1024, BC7-komprimiert). Cartoon-Style, High Saturation. | 8 Dateien, ~20 MB |
| `assets/textures/boards/` | Board-Texturen (Diffuse, 2048×2048, BC7) + Tiling-Texturen (512×512). Pro Insel: 1 Haupt-Textur + 3–5 Tiling-Texturen (Sand, Gras, Lava, Eis, Wolken, etc.). | ~50 Dateien, ~100 MB |
| `assets/textures/ui/` | UI-Texturen: Buttons (Normal/Hover/Pressed), Icons (Munzen, Sterne, Items, Feld-Typen), Hintergrunde, Ladebildschirm, Logo. | ~100 Dateien, ~30 MB |
| `assets/textures/effects/` | Partikel-Texturen: Stern-Funken, Munz-Glitzern, Konfetti, Rauch-Wolken, Wasser-Spritzer. 128×128, Flipbook-Texturen. | ~20 Dateien, ~5 MB |
| `assets/sounds/ui/` | UI-Sounds: Hover (weiches Klicken), Click (helles Bestatigungs-Klack), Back (dumpfes Zuruck), Error (sanftes Ablehnungs-Summ). | ~10 Dateien, <1 MB |
| `assets/sounds/board/` | Board-Sounds: Wurfeln (rasseln + aufkommen), Bewegung (Schritte je nach Untergrund: Sand, Stein, Holz, Gras, Eis, Wolke), Munzen (klimpern, sammeln), Stern (Fanfare, uberreicht), Event (positiv/negativ/neutral). | ~40 Dateien, ~5 MB |
| `assets/sounds/items/` | Item-Sounds pro Item: Glucks-Wurfel (wurfeln + magisches Klingeln), Schutzschild (energiegeladener Summton + aktivieren), Munz-Magnet (anziehendes Surren), Teleporter (Wirbel + Plopp), Diebhandschuh (schnelles Greifen + erschrockener Ausruf). | ~10 Dateien, ~2 MB |
| `assets/sounds/minigames/` | Minispiel-Sounds: Countdown (3-2-1-GO), Start-Signal (Trompete), Zeitablauf (Glocke), Sieg (Fanfare), Niederlage (trauriges Posaunen). Pro Minispiel: 2–5 spezifische Sounds. | ~50 Dateien, ~8 MB |
| `assets/music/menu/` | Menu-Musik: 2–3 Tracks. Frohlich, cartoonesk, instrumental. 3–4 Minuten pro Track. OGG 128kbps Stereo. | ~3 Dateien, ~10 MB |
| `assets/music/boards/` | Board-Musik: 1 Track pro Insel (8 Tracks). Thema passend zur Insel (Sonnenstrand = karibisch, Frostgipfel = glitzernd, Vulkaninsel = treibend). 3–5 Minuten, loopbar. OGG 128kbps Stereo. | 8 Dateien, ~30 MB |
| `assets/music/minigames/` | Minispiel-Musik: 4–6 Tracks (geteilt zwischen Minispielen). Schneller, treibender, 1–2 Minuten, loopbar. OGG 96kbps Stereo. | ~6 Dateien, ~10 MB |
| `assets/fonts/ui/` | UI-Fonts: 1–2 Schriftarten (.ttf/.otf). Eine fur Flie"stext/Menus (gut lesbar, rund), eine fur Titel/Scores (fett, auffallig). Mussen CJK + Sonderzeichen abdecken. | 2–3 Dateien, ~5 MB |
| `assets/fonts/effects/` | Effekt-Fonts: Titel-Font (gross, dekorativ), Score-Font (digital/monospace-artig), ArenaStar-Speech-Font (handschriftlich/comic-artig). | 3 Dateien, ~3 MB |

#### D5: Neue Ubersetzungen

| Datei | Sprache | Status |
|---|---|---|
| `translations/de.po` | Deutsch | Primarsprache. Alle Strings werden zuerst auf Deutsch verfasst und dann ubersetzt. |
| `translations/en.po` | Englisch | Ubersetzung aus dem Deutschen. Ziel: Native-Speaker-Qualitat. |
| `translations/fr.po` | Franzosisch | Ubersetzung aus dem Deutschen. |
| `translations/es.po` | Spanisch | Ubersetzung aus dem Deutschen. |
| `translations/ja.po` | Japanisch | Ubersetzung aus dem Deutschen. Besondere Aufmerksamkeit: CJK-Schriftart-Unterstutzung, kulturelle Anpassung von Witzen. |
| `translations/zh.po` | Chinesisch (vereinfacht) | Ubersetzung aus dem Deutschen. Besondere Aufmerksamkeit: CJK-Schriftart, vereinfachte Zeichen. |

### 3.5 STP-spezifische Elemente — Vollstandige Entfernungsliste

Diese Elemente mussen **vollstandig und ruckstandslos** aus dem Code entfernt werden. Keine auskommentierten Referenzen, keine ungenutzten Assets.

#### 3.5.1 Strings und Konstanten — Suchmatrix

| STP-String | Ersatz in PA | Suchmuster (grep/regex) | Betroffene Dateitypen |
|---|---|---|---|
| `"Cookies"`, `"cookies"`, `"COOKIES"`, `"Cookie"` | `"Munzen"`, `"coins"`, `"MUENZEN"`, `"Muenze"` | `[Cc]ookies?`, `COOKIES?` | `.gd`, `.tscn`, `.tres`, `.po`, `.json`, `.cfg` |
| `"Cakes"`, `"cakes"`, `"CAKES"`, `"Cake"` | `"Sterne"`, `"stars"`, `"STERNE"`, `"Stern"` | `[Cc]akes?`, `CAKES?` | `.gd`, `.tscn`, `.tres`, `.po`, `.json`, `.cfg` |
| `"COOKIES_FOR_CAKE"` | `"MUENZEN_FUER_STERN"` | `COOKIES_FOR_CAKE` | `.gd` |
| `"Sara"`, `"sara"`, `"SARA"` | `"ArenaStar"`, `"arena_star"` | `[Ss]ara`, `SARA` | `.gd`, `.tscn`, `.po`, `.json` |
| `"Nolok"`, `"nolok"`, `"NOLOK"` | Entfernen (kein Ersatz) | `[Nn]olok`, `NOLOK` | `.gd`, `.tscn`, `.tres`, `.po` |
| `"GNU"`, `"Gnu"`, `"gnu"` | Entfernen (kein Ersatz) | `[Gg][Nn][Uu]` | `.gd`, `.tscn`, `.tres`, `.po` |
| `"Super Tux Party"`, `"SuperTuxParty"` | `"Party Arena"` | `Super\s*Tux\s*Party` | `.gd`, `.tscn`, `.tres`, `.po`, `.cfg`, `.md` |
| `"Tux"`, `"tux"`, `"TUX"` | Entfernen (ersetzt durch Arenians) | `[Tt]ux`, `TUX` | `.gd`, `.tscn`, `.tres`, `.po`, alle Assets |
| `"KDE"`, `"Kde"`, `"kde"` | Entfernen | `[Kk][Dd][Ee]` | `.gd`, `.tscn`, `.tres`, `.po`, alle Assets |
| `"STP"` (als Code-Name) | `"PA"` | `\bSTP\b` | `.gd`, `.md` (ausser `CREDITS.md`) |

#### 3.5.2 Node-Typen (Entfernung aus Code)

| STP Node-Typ | Aktion | Betroffene Dateien |
|---|---|---|
| `NOLOK` | Aus Enum entfernen. Alle Code-Pfade, die auf NOLOK prufen, loschen. NOLOK-Events aus Event-Pool loschen. | `node.gd`, `controller.gd`, `board_loader.gd` |
| `GNU` | Aus Enum entfernen. Alle Code-Pfade, die auf GNU prufen, loschen. GNU-Events aus Event-Pool loschen. | `node.gd`, `controller.gd`, `board_loader.gd` |
| `DUEL` (Duel-Feldtyp) | Aus Enum entfernen. Duel-Logik komplett loschen. | `node.gd`, `controller.gd`, `duelselection.gd` (entfernen) |

#### 3.5.3 Minispiele (Entfernung)

| STP Minispiel | Aktion | Begrundung |
|---|---|---|
| Kernel-Compiling | Komplett loschen aus `plugins/minigames/` | Passt nicht zum Toy/Cartoon-Stil. Linux-Insider-Witz. |
| Alle STP-Minispiele | Komplett loschen aus `plugins/minigames/` | Werden durch 12 neue PA-Minispiele ersetzt. Kein einziges STP-Minispiel ubernehmen. |

#### 3.5.4 Rewardscreens (Entfernung)

| STP Reward | Aktion | Begrundung |
|---|---|---|
| Gnu Coop Rewardscreen | Kompletter Ordner loschen | GNU-Charakter existiert nicht mehr. |
| Nolok Coop Rewardscreen | Kompletter Ordner loschen | Nolok-Charakter existiert nicht mehr. |
| Duel Rewardscreen | Kompletter Ordner loschen | Kein Duel-Modus in Party Arena. |
| Solo Rewardscreen (falls vorhanden) | Kompletter Ordner loschen | Kein Solo-Modus (PA ist immer Multiplayer, min. 2P). |

#### 3.5.5 Boards und Charaktere (Entfernung)

| STP-Element | Aktion | Begrundung |
|---|---|---|
| KDE Valley Board | Komplett loschen aus `plugins/boards/` | KDE-Branding/IP. |
| Alle STP-Boards | Komplett loschen | Werden durch 8 neue Insel-Boards ersetzt. |
| Tux-Charakter | Komplett loschen aus `plugins/characters/` | Tux ist Linux-Maskottchen (Tux-IP). |
| KDE-Dragon-Charakter | Komplett loschen | KDE-IP. |
| Alle STP-Charaktere | Komplett loschen | Werden durch 8 Arenians ersetzt. |

#### 3.5.6 Assets und Branding (Entfernung)

| STP-Element | Aktion |
|---|---|
| Alle 3D-Modelle (.glb, .gltf) | Loschen. Ersetzt durch neue PA-Modelle. |
| Alle Texturen (ausser generische UI-Basis) | Loschen. Ersetzt durch neue PA-Texturen. |
| Alle Sounds/Musik | Loschen. Ersetzt durch neue PA-Audio-Assets. |
| Tux-Modell, KDE-Dragon-Modell, GNU-Modell | Loschen. Keine Referenz behalten. |
| `icon.webp` (Tux-Icon) | Ersetzen durch PA-Icon (ArenaStar oder Logo). |
| Splash-Screen (STP-Logo) | Ersetzen durch PA-Logo-Splash. |
| Fenster-Titel "Super Tux Party" | Andern zu "Party Arena" in `project.godot` und `export_presets.cfg`. |
| `CREDITS.md` | Neu schreiben: Credit an STP ("Party Arena basiert auf Super Tux Party. Dank an die STP-Entwickler."), primar PA-Credits. |
| `LICENSE` | Neue Lizenz-Datei (AGPL v3 oder MIT, TBD). STP-Lizenz entfernen. |

---

## 4. Formulas

### 4.1 Geschatzte Aufwande (Entwicklungs-Stunden)

| Kategorie | Beschreibung | Geschatzte Stunden | Basis fur Schatzung |
|---|---|---|---|
| A | Direkt ubernehmen | **0 h** | Keine Anderungen notig. Nur Identifikation und Dokumentation. |
| B | Modifizieren | **~40 h** | ~20 Dateien. Pro Datei: Konstanten andern (0,5 h), 8P-Erweiterung (1 h), UI-Updates (0,5 h), Test & Integration (0,5 h). Puffer: 20 %. |
| C | Neu schreiben | **~80 h** | controller.gd (30 h) — komplexe Zustandsmaschine, 8 Phasen, 8P. node.gd (15 h) — neues Enum, 7 Feldtypen, visuelle Indikatoren. server game logic (20 h) — Stern-Kauf, Bonus-Sterne, Catch-Up. Integration & Test (15 h). |
| D | Neu entwickeln | **~200 h** | 8 Boards (40 h — 5 h pro Board inkl. Layout + Assets), 8 Charaktere (32 h — 4 h pro Charakter), 5 Items (15 h), 12 Minispiele (60 h — 5 h pro Minispiel), Neue Systeme (25 h — arena_star.gd 8 h, event_system.gd 10 h, bonus_star.gd 7 h), Menus (20 h), Ubersetzungen (8 h). |
| **Summe Code** | | **~320 h** | Ca. 8 Wochen fur 2 Vollzeit-Entwickler. |

### 4.2 Asset-Creation (separate Schatzung, nicht in Entwicklungs-Stunden)

| Asset-Typ | Anzahl | Geschatzte Zeit (extern / Artist) | Notizen |
|---|---|---|---|
| 3D Charakter-Modelle (inkl. Rigging, Textur, 6 Animationen) | 8 | ~80 h (10 h pro Charakter) | Benotigt erfahrenen 3D-Character-Artist. Cartoon-Stil vereinfacht (keine realistischen Details). |
| 3D Board-Modelle (40 Felder + Dekoration) | 8 | ~160 h (20 h pro Board) | Umfangreichster Asset-Block. Tiling-Texturen reduzieren Aufwand. |
| 3D Item-Modelle | 5 | ~15 h (3 h pro Item) | Kleine, einfache Modelle. |
| 3D ArenaStar + Props/Dekoration | ~20 | ~50 h | ArenaStar ist zentral (hohe Qualitat). Props sind einfacher. |
| Texturen (UI, Effekte, Ramp-Textur, LUTs) | ~50 | ~30 h | UI-Design: 1 Set, konsistent. |
| Soundeffekte | ~100 | ~40 h | Kann teilweise von Stock-Libraries kommen. |
| Musik (Tracks) | ~17 | ~40 h | 8 Board + 3 Menu + 6 Minispiel = 17 Tracks. Komponist benotigt. |
| UI-Design (Konzept, Iteration, alle Screens) | 1 Set | ~40 h | UI-Designer benotigt. |
| Voice-Aufnahmen (ArenaStar, pro Sprache) | 6 Sprachen | ~60 h (10 h pro Sprache) | Sprecher + Studio. Pro Sprache: ~80 Voice-Lines. |
| **Summe Asset-Creation** | | **~515 h** | Ca. 13 Wochen fur 2 Vollzeit-Artists + 1 Komponist. |

### 4.3 Gesamtprojekt-Schatzung

| Bereich | Stunden |
|---|---|
| Entwicklung (Kategorie B+C+D) | 320 h |
| 3D-Assets (Charaktere, Boards, Items, Props) | 305 h |
| 2D-Assets (UI, Texturen, Effekte) | 70 h |
| Audio (Musik, SFX, Voice) | 140 h |
| **Gesamt** | **~835 h** |

Bei 2 Entwicklern + 2 Artists + 1 Audio-Designer (5 Personen Vollzeit): ca. 10–12 Wochen bis zur Beta.

### 4.4 Fork-Tiefe (Prozentuale Anderung gegenuber STP)

```
Fork-Tiefe = (Kat_B_Zeilen_geandert + Kat_C_Zeilen_neu + Kat_D_Zeilen_neu) / Gesamtzeilen_Projekt × 100
```

Geschatzte Werte:
- Kat A: ~5.000 Zeilen (unverandert)
- Kat B: ~8.000 Zeilen (davon ~3.000 geandert)
- Kat C: ~5.000 Zeilen (komplett neu)
- Kat D: ~15.000 Zeilen (komplett neu)
- Gesamt: ~33.000 Zeilen

Fork-Tiefe ≈ (3.000 + 5.000 + 15.000) / 33.000 × 100 ≈ **69,7 %**

Rund 70 % der Codebasis sind gegenuber STP geandert oder neu. Dies rechtfertigt den harten Fork und die Eigenstandigkeit des Projekts.

### 4.5 Entfernungs-Vollstandigkeit (String-Scan)

```
Vollstandigkeit = (Treffer_nach_Bereinigung) / (Treffer_vor_Bereinigung) × 100
```

Ziel: `Vollstandigkeit = 0 %` (keine STP-Strings mehr im Code, ausser `CREDITS.md`).

Die String-Suche (Abschnitt 3.5.1) wird vor jedem Release ausgefuhrt. Treffer > 0 sind ein Release-Blocker (ausser bewusst dokumentierte Ausnahmen).

---

## 5. Edge Cases

1. **STP-Updates wahrend der Entwicklung:** Das originale STP-Projekt erhalt Updates (neue Features, Bugfixes), wahrend wir an Party Arena arbeiten. **Entscheidung:** Wir mergen KEINE STP-Updates. Ausnahme: Kritische Sicherheits-Updates (z.B. eine Schwachstelle in ENet, die in Godot 4.2.x gepatcht wird). In diesem Fall: Anderung manuell analysieren, nur sicherheitsrelevanter Teil portieren, als separaten Commit dokumentieren.

2. **Entwickler verwendet versehentlich STP-Namen:** Ein Entwickler schreibt `COOKIES_FOR_CAKE` statt `MUENZEN_FUER_STERN` in neuem Code. **Pravention:** CI-Script scannt nach verbotenen Strings (Suchmatrix in 3.5.1). Code-Review-Checkliste enthalt Punkt "Keine STP-Strings". Bei Fund: Build schlagt fehl.

3. **Versehentliches Commit von STP-Assets:** Ein Entwickler committet aus Versehen ein STP-Asset (z.B. alte Tux-Textur). **Pravention:** `.gitignore` blockt bekannte STP-Asset-Pfade. CI-Script pruft Datei-Namen auf STP-Schlusselworter: `git diff --name-only HEAD~1 | grep -iE "tux|nolok|gnu|sara" → Fehler`.

4. **Plugin aus Kategorie D uberschreibt Kategorie-C-Logik:** Ein neues Minispiel (Kategorie D) implementiert eigene Spiel-Logik, die mit der Controller-Logik (Kategorie C) kollidiert. **Regel:** Minispiel-Plugins durfen NUR innerhalb ihres eigenen Ordners agieren. Kein Zugriff auf `common/`-Code. Kommunikation nur uber die Plugin-API. Code-Review pruft Imports.

5. **Inkomplette Entfernung von STP-Inhalten:** Nach Phase 7 (Polish) wird ein STP-String in einem versteckten Asset oder einer seltenen UI entdeckt. **Ma"snahmen:** Vor jedem Release: Vollstandiger Text-Scan uber alle `.gd`, `.tscn`, `.tres`, `.po`, `.json`, `.cfg` Dateien. Gefundene Referenzen: Fixen oder bewusste Ausnahme in `CREDITS.md` dokumentieren.

6. **Board-Loader findet STP-Board-Enum nicht mehr:** Nach der Entfernung des STP-Board-Enums (Kat B, board_loader.gd) muss der Loader ohne Enum-Prufung auskommen. **Losung:** Der Loader pruft nur noch auf Existenz von `plugin.json` und `fields.json`. Keine Typprufung gegen festes Enum — alle Feldtypen sind als String definiert und werden zur Laufzeit validiert.

7. **Datei gehort zu zwei Kategorien:** Eine Datei wird teilweise ubernommen (Kat A), aber einige Zeilen mussen geandert werden (Kat B). **Regel:** Die Datei wird als Kat B klassifiziert (die hohere Kategorie). Die unveranderten Teile werden als "STP-Basis" dokumentiert, die Anderungen als "PA-Modifikation".

8. **STP-Lizenz-Konflikt:** STP steht unter der GPL. Party Arena braucht eine eigene Lizenz. **Regel:** Da Party Arena ein harter Fork mit >50 % neuem/geandertem Code ist, kann eine neue Lizenz gewahlt werden. Credit an STP muss in `CREDITS.md` erhalten bleiben. Rechtsberatung vor finaler Lizenzwahl empfohlen.

---

## 6. Dependencies

### 6.1 Interne Abhangigkeiten (Phasen-Abhangigkeiten)

```
Phase 1 (Fork erstellen)        # Keine Abhangigkeiten. Eingabe: STP-Repository.
    ↓
Phase 2 (STP-Inhalte entfernen)  # Abhangig von Phase 1. Entfernt Kategorie-Elemente, Nolok/GNU, STP-Plugins.
    ↓
Phase 3 (Kategorie A+B)         # Abhangig von Phase 2 (Codebasis ist sauber von STP-Referenzen).
    ↓
Phase 4 (Kategorie C)           # Abhangig von Phase 3 (neue Konstanten, Limits, APIs definiert).
    ↓
Phase 5 (Kategorie D)           # Abhangig von Phase 4 (Core-Logik existiert, Plugins werden eingehangt).
    ↓
Phase 6 (Polish & QA)           # Abhangig von Phase 5 (alle Systeme integriert).
```

### 6.2 Externe Abhangigkeiten

| Abhangigkeit | Benotigt fur | Status | Version |
|---|---|---|---|
| Git | Versionskontrolle | Installiert | 2.x |
| Godot 4.2.2 | Entwicklung, Export | Installiert | 4.2.2 |
| STP-Repository | Phase 1 (Fork-Quelle) | Benotigt Zugriff auf STP-Repo | Commit: letzter stabiler Stand |
| Blender | 3D-Modelling (Charaktere, Boards, Items) | Empfohlen | 4.x |
| Audacity / Reaper | Audio-Erstellung und -Bearbeitung | Empfohlen | Beliebig |
| Aseprite / GIMP / Photoshop | 2D-Assets (Texturen, UI) | Empfohlen | Beliebig |
| Poedit | Ubersetzungs-Management (.po-Dateien) | Empfohlen | 3.x |

### 6.3 Keine Abhangigkeiten

- **Kein** Godot 4.3+ (Projekt ist auf 4.2.2 fixiert).
- **Kein** Jolt-Physics (GodotPhysics Default reicht).
- **Kein** Steamworks SDK (nicht im initialen Scope).
- **Kein** Docker (optional, Godot-Docker-Image hatte Mismatch, CI nutzt natives Godot).

---

## 7. Tuning Knobs

### 7.1 Fork-Tiefe (Wie aggressiv wird geforkt?)

| Parameter | Wert | Beschreibung |
|---|---|---|
| Git-Historie | Nicht ubernommen | STP Git-Historie wird verworfen. Sauberer Start mit einem Initial Commit. |
| Lizenz | Neu | Neue Lizenz-Datei (AGPL v3 oder MIT, TBD). STP-Lizenz wird entfernt. |
| Credit | `CREDITS.md` | Enthalt: "Party Arena basiert auf Super Tux Party (https://github.com/supertuxparty/supertuxparty). Dank an die STP-Entwickler." |
| CI-String-Scan | Aktiviert | Blockt Commits mit STP-Strings (Suchmatrix 3.5.1). |
| STP-Merge | Deaktiviert | Kein `git remote` auf STP. `git merge` von STP ist technisch unmoglich. |

### 7.2 Migrationstempo

| Parameter | Dauer | Beschreibung |
|---|---|---|
| Phase 1 (Fork) | 1 Tag | Fork + Git-Init. Muss schnell gehen. |
| Phase 2 (Entfernen) | 3 Tage | Alle STP-Strings und -Assets loschen. Automatisierbar via Script. |
| Phase 3 (Kat A+B) | 2 Wochen | Ubernahme + Modifikation. Gro"ste Code-Anderungsdichte. |
| Phase 4 (Kat C) | 3 Wochen | Rewrite der Core-Logik. Kritischster Pfad. |
| Phase 5 (Kat D) | 6 Wochen | Neuentwicklung. Parallelisierbar (mehrere Entwickler). |
| Phase 6 (Polish) | 2 Wochen | Feature-Freeze, nur Bugfixes und Balancing. |

### 7.3 Code-Review-Prioritat (nach Kategorie)

| Kategorie | Review-Prioritat | Begrundung |
|---|---|---|
| C | Hochste | Core-Logik. Fehler hier brechen das gesamte Spiel. Pflicht: 2 Reviewer. |
| B | Hoch | Modifikationen an bestehenden Systemen. Risiko: Regression. Pflicht: 1 Reviewer. |
| D | Mittel | Neue Systeme. Konnen isoliert getestet werden. Pflicht: 1 Reviewer. |
| A | Niedrig | Keine Anderungen. Nur formale Prufung auf STP-Referenzen. |

### 7.4 Risiko-Management

| Risiko | Wahrscheinlichkeit | Auswirkung | Mitigation |
|---|---|---|---|
| STP-Code enthalt unentdeckte Bugs | Mittel | Mittel | Phase 2: Code-Audit der ubernommenen Dateien. Unit-Tests fur kritische Pfade. |
| Controller-Rewrite (Kat C) dauert langer | Hoch | Hoch | Puffer: 50 % Zeitaufschlag (80 h + 40 h Puffer). Notfallplan: Controller in kleinere Module aufteilen, parallel entwickeln. |
| Asset-Creation verzogert Entwicklung | Mittel | Mittel | Trennung von Code und Assets. Entwicklung mit Platzhalter-Assets (farbige Wurfel, Kapseln statt Charaktere). |
| 8P-Performance reicht nicht | Mittel | Hoch | Fruhzeitiges Performance-Testing (Phase 4, nicht erst Phase 6). Low-Quality-Fallback-Modus. |
| STP-Strings nach Migration ubersehen | Niedrig | Mittel | Automatisierter CI-Scan. Release-Blocker bei Treffern. |

---

## 8. Acceptance Criteria

### 8.1 Fork-Integritat

- [ ] **AC-FS-001:** Keine `git remote` Verbindung zum STP-Repository. `git remote -v` zeigt nur PA-Origin.
- [ ] **AC-FS-002:** `project.godot` enthalt `config/name = "Party Arena"` (nicht "Super Tux Party").
- [ ] **AC-FS-003:** `project.godot` enthalt `config/version = "2.0.0"`.
- [ ] **AC-FS-004:** Keine STP-Assets im `assets/` Ordner (verifiziert via Dateigrossenvergleich und Sichtprufung).
- [ ] **AC-FS-005:** Keine STP-Plugins in `plugins/` (alle alten Boards, Charaktere, Items, Minispiele entfernt).

### 8.2 String-Ersetzung

- [ ] **AC-FS-006:** Suche nach "Cookie", "Cake", "Cookies", "Cakes" (case-insensitive) in allen `.gd`, `.tscn`, `.tres`, `.po`, `.json`, `.cfg` Dateien liefert NULL Treffer (ausser bewusst dokumentierte Ausnahmen in `CREDITS.md`).
- [ ] **AC-FS-007:** Suche nach "Sara", "sara" (case-insensitive) liefert NULL Treffer.
- [ ] **AC-FS-008:** Suche nach "Nolok", "GNU", "Gnu" (case-insensitive) liefert NULL Treffer.
- [ ] **AC-FS-009:** Suche nach "Tux", "KDE" (case-insensitive) liefert NULL Treffer in Code-Dateien.
- [ ] **AC-FS-010:** Suche nach "Super Tux Party" (case-insensitive) liefert NULL Treffer in Code-Dateien. Erlaubt nur in `CREDITS.md`.
- [ ] **AC-FS-011:** `COOKIES_FOR_CAKE` existiert nicht im Code. Stattdessen: `MUENZEN_FUER_STERN = 20`.
- [ ] **AC-FS-012:** `START_COINS = 10` (nicht `5` wie in STP).

### 8.3 Kategorie-Zuordnung

- [ ] **AC-FS-013:** Jede Datei im Projekt kann einer der vier Kategorien (A, B, C, D) zugeordnet werden. Keine Datei ohne Kategorie.
- [ ] **AC-FS-014:** Kategorie-A-Dateien sind unverandert gegenuber STP (ausser automatischer Static-Typing-Fixes: `:=` → `:Typ`).
- [ ] **AC-FS-015:** Kategorie-B-Dateien haben mindestens eine substanzielle Modifikation (8P, neue Konstanten, neue Referenzen, neues Branding).
- [ ] **AC-FS-016:** Kategorie-C-Dateien sind ein vollstandiger Rewrite. Kein Copy-Paste von STP-Logik (ausser rein strukturelle Patterns).
- [ ] **AC-FS-017:** Kategorie-D-Dateien existieren in STP nicht. Verifiziert gegen STP-Repository (Dateiliste von STP-Commit).

### 8.4 Plugin-System

- [ ] **AC-FS-018:** `board_loader.gd` ladt PA-Boards ohne STP-spezifische Enum-Prufungen. Board-Typen werden als String validiert (nicht gegen festes Enum).
- [ ] **AC-FS-019:** `character_loader.gd` ladt Arenians, nicht STP-Charaktere. Ordner-Scan findet nur Arenian-Plugins.
- [ ] **AC-FS-020:** `item_loader.gd` unterstutzt PA-Item-Typen (Glucks-Wurfel, Schutzschild, Munz-Magnet, Teleporter, Diebhandschuh).
- [ ] **AC-FS-021:** `minigame_loader.gd` ladt PA-Minispiele (12 neue), nicht STP-Minispiele.
- [ ] **AC-FS-022:** Fehlende `plugin.json` fuhrt zu uberspringbarem Fehler (Push-Warnung, Plugin deaktiviert, Spiel lauft weiter).

### 8.5 Menus und UI

- [ ] **AC-FS-023:** Hauptmenu enthalt KEINE STP-Referenzen (Button-Texte, Hintergrund, Logo, Farben, Sounds).
- [ ] **AC-FS-024:** Character-Select-Screen zeigt 8 Arenians (nicht Tux/KDE-Charaktere).
- [ ] **AC-FS-025:** Board-Select-Screen zeigt 8 Inseln (nicht KDE Valley/STP-Boards).
- [ ] **AC-FS-026:** Pause-Menu, Options-Menu, Victory-Screen enthalten keine STP-Referenzen.
- [ ] **AC-FS-027:** Alle Menu-Buttons verwenden den neuen Cartoon-Theme (nicht STP-Theme).

### 8.6 Wahrung

- [ ] **AC-FS-028:** Alle Wahrungs-Strings im Code und UI sind "Munzen" / "Sterne" (de) bzw. "Coins" / "Stars" (en). Nicht "Cookies" / "Cakes".
- [ ] **AC-FS-029:** Stern kostet 20 Munzen (`MUENZEN_FUER_STERN = 20`). Nicht 30 Cookies.
- [ ] **AC-FS-030:** Start-Munzen: 10 (`START_COINS = 10`). Nicht 5.

### 8.7 8-Spieler-Unterstutzung

- [ ] **AC-FS-031:** `MAX_PLAYERS = 8` in `global.gd`.
- [ ] **AC-FS-032:** `LOBBY_SIZE = 8` in `common/lobby.gd`.
- [ ] **AC-FS-033:** `PLAYER_TRANSLATION` Array hat 8 Eintrage (Vector2 oder Vector3).
- [ ] **AC-FS-034:** Lobby unterstutzt 8 Spieler (8 Slots im UI, Server akzeptiert 8 Clients).
- [ ] **AC-FS-035:** InputMap enthalt 80 Input-Eintrage (10 Actions × 8 Spieler).

### 8.8 Entfernte Features

- [ ] **AC-FS-036:** Nolok/GNU-Events existieren nicht (keine Node-Typen, keine Controller-Logik, keine Rewards).
- [ ] **AC-FS-037:** Duel-Modus existiert nicht (keine `duelselection.gd`, keine Duel-Rewards, kein Duel-Feldtyp).
- [ ] **AC-FS-038:** Kernel-Compiling Minispiel existiert nicht.
- [ ] **AC-FS-039:** Keine STP-Charaktere in `plugins/characters/`.

### 8.9 Git und Build

- [ ] **AC-FS-040:** Projekt kompiliert fehlerfrei in Godot 4.2.2 (Editor → Run).
- [ ] **AC-FS-041:** `.gitignore` blockt STP-Asset-Pfade und Build-Artefakte.
- [ ] **AC-FS-042:** `CREDITS.md` enthalt Credit an STP, aber primar PA-Credits.
- [ ] **AC-FS-043:** CI-Script scannt erfolgreich auf verbotene STP-Strings (Build schlagt bei Treffern fehl).

### 8.10 Phasen-Erfullung

- [ ] **AC-FS-044:** Phase 1 (Fork) abgeschlossen: Sauberes Git-Repo, ein Initial Commit, keine STP-Remotes.
- [ ] **AC-FS-045:** Phase 2 (Entfernen) abgeschlossen: Keine STP-Strings/Assets mehr im Projekt.
- [ ] **AC-FS-046:** Phase 3–5 (Implementierung) abgeschlossen: Alle Systeme aus `systems-index.md` implementiert, getestet und integriert.
- [ ] **AC-FS-047:** Phase 6 (Polish) abgeschlossen: Alle Acceptance Criteria dieses Dokuments und aller anderen Kapitel erfullt.

---

> **Nachste Datei:** `technical-data-structures.md` — Datenstrukturen und Speicherformate
> **Referenz:** `technical-architecture.md` — Gesamtarchitektur
> **Referenz:** `technical-multiplayer.md` — Multiplayer-Architektur
> **Referenz:** `technical-performance.md` — Performance-Ziele
> **Referenz:** `systems-index.md` — Systemzerlegung
