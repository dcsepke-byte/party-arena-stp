# Technische Multiplayer-Architektur — Party Arena

> **Status:** Proposed  
> **Version:** 2.0.0  
> **Letzte Änderung:** 2026-08-11  
> **Abhängigkeiten:** technical-architecture.md, game-concept.md

---

## 1. Overview

Die Multiplayer-Architektur von Party Arena basiert auf dem **server-autoritativen** Modell von Super Tux Party, erweitert für **8 Spieler** (STP: 4). Der Server (Host) ist die einzige Quelle der Wahrheit für alle Spielzustände. Clients sind "dumb" — sie rendern nur und senden Input. Die Kommunikation erfolgt über **ENet** via Godots `ENetMultiplayerPeer` mit **RPCs** (Remote Procedure Calls).

### Kernentscheidungen

| Entscheidung | Wert | Begründung |
|---|---|---|
| Protokoll | ENet (ENetMultiplayerPeer) | Von STP übernommen. Bewährt, zuverlässig, UDP-basiert mit optionaler Reihenfolge-Garantie. |
| Topologie | Server-Authoritativ (Client-Server) | Verhindert Cheating, zentralisiert die Spiel-Logik. |
| Lokaler Multiplayer | `create_local_server()` in Global.gd | Single-PC: Server und alle Clients in einem Prozess. |
| Online-Multiplayer | Dedicated Server ODER Host+Client | Host = ein Spieler ist Server + Client zugleich. Dedicated Server für Turniere/Streamer. |
| 8-Spieler-Erweiterung | LOBBY_SIZE=8, 8 Input-Slots, 8 Player-IDs | STP unterstützte nur 4. Alle Referenzen auf "4" wurden auf "8" erhöht. |
| Latenz-Strategie | Keine Input-Prediction, 30s Timeout | Turn-basiertes Spiel: Latenz unkritisch. Minispiele kurz (30s), kleine Verzögerung akzeptabel. |
| Cheat-Schutz | Server validiert jede Aktion | Client kann Münzen/Items nicht manipulieren. |

### Netzwerk-Architektur Übersicht

```
┌──────────────────────────────────────────────────────────────┐
│                        SERVER (Host)                          │
│                                                               │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │                  Server Game Manager                     │ │
│  │  - Runden-Logik                                         │ │
│  │  - State-Validierung                                    │ │
│  │  - Autoritative Antworten                               │ │
│  └────────────┬────────────────────────────────────────────┘ │
│               │                                               │
│  ┌────────────▼────────────────────────────────────────────┐ │
│  │              ENetMultiplayerPeer (Server)               │ │
│  │  - Port: 10567 (UDP)                                    │ │
│  │  - Max Clients: 8                                       │ │
│  │  - Reliable: Ja (für State-Updates)                     │ │
│  │  - Unreliable: Optional (für Input-Stream)              │ │
│  └────────────┬────────────────────────────────────────────┘ │
└───────────────┼──────────────────────────────────────────────┘
                │  ENet UDP
    ┌───────────┼───────────┬───────────┬───────────┐
    │           │           │           │           │
┌───▼───┐  ┌────▼────┐ ┌────▼────┐ ┌───▼───┐  ┌───▼───┐
│Client 1│  │Client 2 │ │Client 3 │ │  ...  │  │Client 8│
│Render  │  │Render   │ │Render   │ │       │  │Render  │
│Input   │  │Input    │ │Input    │ │       │  │Input   │
│Audio   │  │Audio    │ │Audio    │ │       │  │Audio   │
└────────┘  └─────────┘ └─────────┘ └───────┘  └────────┘
```

---

## 2. Player Fantasy

### Was der Spieler merkt

- **Nahtloser Multiplayer:** Egal ob lokal (Couch-Coop mit bis zu 8 Freunden) oder online — das Spielerlebnis ist identisch. Kein Unterschied in Latenz oder Input-Responsivität spürbar.
- **Fairness:** Kein Spieler kann schummeln. Der Server kontrolliert alles. Selbst wenn jemand seinen Client modifiziert, hat das keine Auswirkung.
- **Keine Wartezeit:** Wenn ein Spieler trödelt (AFK), wird nach 30 Sekunden automatisch gewürfelt. Das Spiel kommt nicht zum Stillstand.
- **Stabilität:** Disconnects sind ärgerlich, aber nicht spielentscheidend. Der disconnectete Spieler wird von einer rudimentären KI übernommen.
- **Einfaches Joinen:** IP eingeben oder Server im lokalen Netzwerk finden. Fertig.

### Was der Entwickler merkt

- **Klare RPC-Konventionen:** `@rpc("authority")` für Server-Aufrufe, `@rpc("any_peer")` für Client-Input. Keine Verwechslung.
- **Server-Validierung:** Jede Client-Aktion wird vom Server validiert. Ein zentraler Validierungspunkt — kein verteilter Cheat-Schutz.
- **Testbarkeit:** Lokaler Multiplayer (`create_local_server()`) erlaubt vollständige Multiplayer-Tests ohne Netzwerk.

---

## 3. Detailed Rules

### 3.1 Protokoll: ENet (ENetMultiplayerPeer)

- **Bibliothek:** Godot-integriertes ENet (kein externes Plugin).
- **Transport:** UDP.
- **Port:** 10567 (Standard). Im Options-Menü konfigurierbar (1024–65535).
- **Verbindungsmodi:**
  - **Reliable:** Für State-Updates, Rundenwechsel, Item-Effekte. Garantiert Zustellung und Reihenfolge.
  - **Unreliable (optional):** Für Input-Stream während Minispielen (niedrigere Latenz, toleriert Paketverlust).
- **Kanal-Anzahl:** 3 (Kanal 0: State, Kanal 1: Input, Kanal 2: Chat/Emotes).
- **Max Clients:** 8 (in `server/game.gd`: `peer.create_server(10567, 8)`).
- **Verbindungsaufbau:**
  1. Server startet: `ENetMultiplayerPeer.create_server(port, max_clients)`.
  2. Client verbindet: `ENetMultiplayerPeer.create_client(ip, port)`.
  3. Verbindung bestätigt: `peer_connected` Signal wird emittiert.
  4. Client authentifiziert: Spieler-Name, optionales Passwort (für private Lobbys) werden gesendet.
  5. Lobby-Beitritt: Client erhält Lobby-State (Charaktere, Board, Spieler).

### 3.2 RPC-System (Remote Procedure Calls)

#### RPC-Typen und Verwendung

| RPC-Annotation | Aufrufer | Ausführender | Verwendung |
|---|---|---|---|
| `@rpc("authority")` | Nur Server | Alle Clients | State-Updates, Animations-Auslöser, Minispiel-Start |
| `@rpc("any_peer")` | Jeder Peer | Server (validiert) | Spieler-Input (Würfeln, Item, Shop, Pfad-Wahl) |
| `@rpc("any_peer", "call_local")` | Jeder Peer | Alle Peers (inkl. Aufrufer) | Chat-Nachrichten, Emotes |

#### RPC-Konventionen

- **Namenskonvention:** `_rpc_<aktion>` für RPC-Funktionen (z.B. `_rpc_roll_dice`, `_rpc_buy_star`).
- **Parameter:** Alle RPC-Parameter müssen `@rpc`-kompatibel sein (Variant-Typen: int, float, String, Dictionary, Array, bool, Vector2, Vector3).
- **Keine Objekte:** Godot-Objekte (Nodes, Resources) können NICHT per RPC gesendet werden. Nur primitive Typen und Dictionaries.
- **Validierung:** Jede `@rpc("any_peer")` Funktion MUSS mit einer Server-Validierung beginnen (siehe Abschnitt 4).

#### RPC-Beispiel (Spielfluss)

```
Client will würfeln:
  1. Client ruft auf: rpc_id(1, "_rpc_request_roll")  # ID 1 = Server
  2. Server validiert: Ist der Spieler an der Reihe? Ist die Phase "ROLL"?
  3. Wenn ja: Server würfelt (randi_range(1,6)), aktualisiert State, sendet Broadcast:
     rpc("_rpc_dice_result", player_id, dice_value)
  4. Alle Clients empfangen _rpc_dice_result, spielen Würfel-Animation ab, bewegen Figur.
```

### 3.3 Spielfluss-Networking (Detailliert)

Das Spiel läuft in Phasen ab. Jede Phase hat spezifische RPCs:

#### Phase 1: Runden-Start
- **Server:** Ermittelt aktuellen Spieler (PlayerBoard.get_current_player()), sendet `_rpc_turn_start(player_id)`.
- **Client:** Zeigt "Spieler X ist dran" Banner, aktiviert UI für diesen Spieler.

#### Phase 2: Würfeln (ROLL)
- **RPC (Client → Server):** `_rpc_request_roll()` — `@rpc("any_peer")`
- **Server-Validierung:** `current_player == sender_id` AND `round_phase == "ROLL"` AND `player_has_not_rolled`
- **Server-Logik:** `dice_value = randi_range(DICE_MIN, DICE_MAX)`, speichert Wert, setzt `round_phase = "MOVE"`.
- **RPC (Server → Alle):** `_rpc_dice_result(player_id, dice_value)` — `@rpc("authority")`
- **Client:** Würfel-Animation abspielen, Figur bewegen.

#### Phase 3: Bewegung (MOVE)
- **Server-Logik:** `player.position += dice_value`, prüft Board-Grenzen, löst Feld-Effekte aus.
- **RPC (Server → Alle):** `_rpc_player_move(player_id, from_field, to_field, path)` — `@rpc("authority")`
- **Client:** Animiert Figur entlang `path` zu `to_field`.
- **Pfad-Wahl (Abzweigung):** `_rpc_request_path_choice(player_id, chosen_branch_index)` — `@rpc("any_peer")`
- **Server-Validierung:** Aktuelles Feld hat mehrere `next`-Indizes, `chosen_branch_index` ist gültig.

#### Phase 4: Feld-Ereignis (EVENT)
- **Server:** Prüft `node.gd` Feld-Typ:
  - `STAR_SHOP`: Stern-Kauf-Dialog
  - `ITEM_SHOP`: Item-Kauf-Dialog
  - `EVENT`: Zufälliges Event aus `event_pool` des Feldes
  - `LUCK`: Glücks-Event (Münzen gewinnen/verlieren)
  - `COIN_BONUS`: Münz-Bonus
  - `MINIGAME`: Minispiel auslösen
- **RPC (Server → Alle):** `_rpc_trigger_event(player_id, field_index, field_type, event_data)` — `@rpc("authority")`

#### Phase 5: Shop (SHOP)
- **Stern-Kauf:**
  - **RPC (Client → Server):** `_rpc_request_buy_star()` — `@rpc("any_peer")`
  - **Server-Validierung:** `player.coins >= MÜNZEN_FÜR_STERN` AND `player.position == active_star_shop` AND `star_available == true`
  - **RPC (Server → Alle):** `_rpc_star_purchased(player_id, new_star_count, star_cost)` — `@rpc("authority")`
- **Item-Kauf:**
  - **RPC (Client → Server):** `_rpc_request_buy_item(item_id)` — `@rpc("any_peer")`
  - **Server-Validierung:** `player.coins >= item.price` AND `player.items.size() < MAX_ITEMS` AND `player.position in item_shop_positions`
  - **RPC (Server → Alle):** `_rpc_item_purchased(player_id, item_id, new_coin_count)` — `@rpc("authority")`

#### Phase 6: Minispiel (MINIGAME)
- Siehe Abschnitt 3.4.

#### Phase 7: Runden-Ende
- **Server:** `current_player += 1`, wenn letzter Spieler: `current_turn += 1`, `_rpc_turn_end(turn_number)`.
- Wenn `current_turn > MAX_TURNS`: Bonus-Sterne berechnen, Sieger ermitteln.
- **RPC (Server → Alle):** `_rpc_game_end(rankings, bonus_stars)` — `@rpc("authority")`

### 3.4 Minispiel-Networking

Minispiele sind die einzigen Echtzeit-Elemente im Spiel (30 Sekunden Dauer). Das Networking ist hier anders als im Board-Modus:

#### Pre-Minigame (Synchronisation)
1. **Server:** Wählt Minispiel aus (Minigame-Queue), sendet `_rpc_minigame_start(minigame_name, seed)` — `@rpc("authority")`.
2. **Alle Clients:** Laden Minispiel-Plugin (`plugins/minigames/<name>/`), instanziieren Szene mit `seed`.
3. **Server:** Wartet bis alle Clients `_rpc_minigame_ready()` gesendet haben (max 5 Sekunden Timeout).
4. **Server:** Sendet Countdown `_rpc_minigame_countdown(3, 2, 1, "GO!")` — `@rpc("authority")`.

#### Während des Minispiels (Input-Stream)
- **Client → Server:** Input-Stream im `_process()` Loop (ca. alle 50ms = 20× pro Sekunde):
  ```gdscript
  @rpc("any_peer", "unreliable")
  func _rpc_minigame_input(player_id: int, input_vector: Vector2, action_pressed: String):
      if not _validate_sender(player_id): return
      minigame_instance.process_input(player_id, input_vector, action_pressed)
  ```
- **Verwendung von "unreliable":** Input-Stream toleriert Paketverlust — der nächste Input überschreibt den vorherigen. Keine Notwendigkeit, jeden einzelnen Input zuzustellen.
- **Server:** Berechnet Spielzustand des Minispiels (Positionen, Scores, Kollisionen). Sendet periodische Sync-Updates:
  ```gdscript
  @rpc("authority", "unreliable")
  func _rpc_minigame_sync(player_positions: Dictionary, scores: Dictionary, time_remaining: float):
      pass  # Client updated seinen lokalen State
  ```

#### Post-Minigame (Ergebnisse)
1. **Server:** Minispiel beendet (Zeit abgelaufen oder Bedingung erfüllt). Berechnet Rankings.
2. **RPC (Server → Alle):** `_rpc_minigame_result(rankings: Array[Dictionary], coin_rewards: Dictionary)` — `@rpc("authority")`.
3. **Client:** Zeigt Reward-Screen mit Platzierungen und Münz-Belohnungen.

### 3.5 Lobby-System (Vor dem Spiel)

Das Lobby-System von STP (`server/lobby.gd`, `client/lobby.gd`, `common/lobby.gd`) wird für 8 Spieler angepasst.

#### Server-Lobby
- **Max Spieler:** 8 (STP: 4). Konstante `LOBBY_SIZE = 8` in `common/lobby.gd`.
- **Spieler-Tracking:** Dictionary `lobby_players: Dictionary[int, LobbyPlayerData]` mit ID 1–8.
- **Charakter-Auswahl:** Jeder Spieler wählt einen Arenian (8 verfügbar, First-Come-First-Served).
- **Board-Auswahl:** Host wählt Board aus 8 Inseln.
- **Start-Bedingung:** Host drückt "Start". Minimum 2 Spieler müssen verbunden sein.
- **Lobby-Phasen:**
  1. `WAITING`: Server wartet auf Verbindungen.
  2. `CHARACTER_SELECT`: Spieler wählen Charaktere.
  3. `BOARD_SELECT`: Host wählt Board.
  4. `READY`: Alle Spieler bereit, Countdown läuft.
  5. `STARTING`: Übergang zum Spiel.

#### Client-Lobby
- **UI:** Spieler-Liste (1–8 Slots), Charakter-Anzeige, Board-Vorschau, Chat.
- **Charakter-Wechsel:** Client sendet `_rpc_request_character(character_name)` — Server prüft ob Charakter verfügbar.
- **Ready-Status:** Client sendet `_rpc_set_ready(true/false)`. Host sieht Ready-Status aller Spieler.

#### Lobby-RPCs
- `_rpc_lobby_player_joined(player_data: Dictionary)` — `@rpc("authority")`
- `_rpc_lobby_player_left(player_id: int)` — `@rpc("authority")`
- `_rpc_lobby_character_changed(player_id: int, character_name: String)` — `@rpc("authority")`
- `_rpc_lobby_board_changed(board_name: String)` — `@rpc("authority")`
- `_rpc_lobby_player_ready(player_id: int, ready: bool)` — `@rpc("authority")`
- `_rpc_lobby_start_countdown(seconds: int)` — `@rpc("authority")`

### 3.6 8-Spieler-Erweiterung (von STP: 4)

#### Änderungen an STP-Systemen

| STP-System | STP-Wert | PA-Wert | Änderungsort |
|---|---|---|---|
| `LOBBY_SIZE` | 4 | 8 | `common/lobby.gd` |
| `PLAYER_TRANSLATION` Array | `[Vector2(0,0), Vector2(0,1), Vector2(1,0), Vector2(1,1)]` | `[Vector2(0,0), Vector2(0,0.333), Vector2(0,0.666), Vector2(0.5,0), Vector2(0.5,0.333), Vector2(0.5,0.666), Vector2(0,0), Vector2(0,0)]` (8 Positionen als Teil-Transparenz-Overlay) | `common/scenes/board_logic/player_board/player_board.gd` |
| Input Actions | `_p1` bis `_p4` | `_p1` bis `_p8` | `project.godot` InputMap |
| Gamepad Slots | 0–3 | 0–7 | `common/scripts/global.gd` |
| Player-IDs | 1–4 | 1–8 | Alle Systeme |
| Splitscreen | 2×2 (max 4) | 2×2 (max 4), kein Split für 5–8 | `client/game.gd` |
| Player-Info HUD | 4 Slots | 8 Slots | `common/scenes/board_logic/controller/player_info.gd` |

#### Splitscreen-Strategie

- **2 Spieler:** Horizontaler Split (links/rechts), je 960×1080.
- **3 Spieler:** Ein großer Viewport oben (1920×720) + zwei kleine unten (je 960×360).
- **4 Spieler:** 2×2 Grid, je 960×540.
- **5–8 Spieler:** Kein Splitscreen. Shared Screen — alle Spieler teilen sich einen Viewport. Kamera folgt dem aktiven Spieler. Die anderen Spieler sind auf dem Board sichtbar.

#### Input-Mapping für 8 Spieler

| Spieler | Tastatur | Gamepad |
|---|---|---|
| P1 | WASD + Enter/Space | Gamepad 0 |
| P2 | IJKL + Right Shift | Gamepad 1 |
| P3 | — | Gamepad 2 |
| P4 | — | Gamepad 3 |
| P5 | — | Gamepad 4 |
| P6 | — | Gamepad 5 |
| P7 | — | Gamepad 6 |
| P8 | — | Gamepad 7 |

### 3.7 Lokaler Multiplayer

Lokaler Multiplayer bedeutet: Ein PC, alle Spieler im gleichen Raum, ein Bildschirm.

- **Initialisierung:** `Global.create_local_server()` in `common/scripts/global.gd`.
  ```gdscript
  func create_local_server():
      var peer = ENetMultiplayerPeer.new()
      peer.create_server(10567, MAX_PLAYERS)
      multiplayer.multiplayer_peer = peer
      # Server-seitige Szene laden (server/game.tscn)
  ```
- **Client-Beitritt (gleicher Prozess):**
  ```gdscript
  func join_local_game(player_id: int):
      var peer = ENetMultiplayerPeer.new()
      peer.create_client("127.0.0.1", 10567)
      multiplayer.multiplayer_peer = peer
      # Client-seitige Szene laden (client/game.tscn)
  ```
- **Prozess-Modell:** Ein Godot-Prozess. Server und alle Clients laufen im gleichen Prozess. `multiplayer_peer` und `multiplayer.multiplayer_peer` werden pro Node unterschieden.
- **Vorteil:** Kein Netzwerk-Overhead, Tests ohne zweites Gerät möglich.

### 3.8 Online-Multiplayer

#### Dedicated Server
- **Start:** `godot --headless --path /path/to/server server/server.tscn` (Command-Line, Headless).
- **Szene:** `server/server.tscn` — Enthält nur Server-Logik, kein Rendering.
- **Kein Spieler:** Der Server spielt nicht mit (kein Host-as-Player).
- **Verwendung:** Turniere, Streamer-Events, öffentliche Server.

#### Host + Clients (Peer-to-Peer via Server)
- **Start:** Spieler erstellt Lobby (wird Host). Host = Server + Client (ein Spieler).
- **Clients:** Verbinden via IP/Port des Hosts.
- **NAT-Traversal:** Nicht implementiert. Spieler müssen im gleichen Netzwerk sein oder Port-Forwarding einrichten. Für Online-Spiele über das Internet: Dedicated Server empfohlen.

#### Server-Browser
- **Lokales Netzwerk:** UDP-Broadcast auf Port 10568. Server antwortet mit Server-Info (Name, Spielerzahl, Board).
- **Direkt-IP:** Spieler gibt IP-Adresse manuell ein.
- **Kein Matchmaking:** Kein zentraler Master-Server. Nicht im Scope für erste Version.

### 3.9 Disconnect-Handling

#### Spieler-Disconnect (Client verliert Verbindung)

1. **Server erkennt Disconnect:** `peer_disconnected` Signal wird emittiert.
2. **Server-Reaktion:**
   - Setze `player.is_connected = false`.
   - Sende `_rpc_player_disconnected(player_id)` an verbleibende Clients — `@rpc("authority")`.
   - Der disconnectete Spieler wird von einer **rudimentären KI** übernommen:
     - **Würfeln:** Auto-Würfel nach 5 Sekunden (kürzer als normaler Timeout).
     - **Shop:** Auto-Pass (kein Kauf).
     - **Pfad-Wahl:** Zufällig (random choice).
     - **Item-Nutzung:** Keine (KI nutzt keine Items).
     - **Minispiel:** Spieler wird automatisch Letzter (Platz 8) mit 0 Score.
3. **Client-Reaktion:** Zeigt Disconnect-Symbol neben Spieler-HUD. KI-Spieler wird visuell markiert (grau/transparent).

#### Server-Disconnect (Host verliert Verbindung oder stürzt ab)

1. **Client erkennt Disconnect:** `server_disconnected` Signal wird emittiert.
2. **Alle Clients:**
   - Spiel wird unterbrochen.
   - Dialog: "Verbindung zum Server verloren."
   - Button: "Zurück zum Hauptmenü".
   - **Kein Host-Migration** (übernimmt kein anderer Client den Server). Dies ist eine bewusste Entscheidung: Host-Migration ist komplex und fehleranfällig, und die Spiele sind kurz (10 Runden, ~30–45 Minuten).

#### Reconnect (Optional, Post-Launch)

- **Nicht im initialen Scope.**
- **Zukünftiges Feature:** Spieler kann innerhalb von 60 Sekunden reconnecten. Server speichert Player-State und setzt `is_connected = true`. KI wird deaktiviert.

### 3.10 Latenz & Lag

#### Latenz-Anforderungen

| Spielphase | Latenz-Toleranz | Begründung |
|---|---|---|
| Board (Würfeln, Bewegung, Shop) | < 500ms | Turn-basiert, kein Zeitdruck. |
| Board (Pfad-Wahl) | < 1000ms | Spieler braucht Zeit zum Entscheiden. |
| Minispiel (Echtzeit) | < 150ms | Echtzeit-Gameplay. 150ms = ca. 10 Frames bei 60fps. |
| Lobby | < 500ms | Keine Echtzeit-Anforderung. |

#### Timeout-Strategie

| Timeout | Dauer | Aktion |
|---|---|---|
| `TURN_TIMEOUT` | 30 Sekunden | Wenn Spieler nicht würfelt → Auto-Würfel (Server würfelt zufällig) |
| `SHOP_TIMEOUT` | 15 Sekunden | Wenn Spieler nicht kauft → Auto-Pass (kein Kauf) |
| `PATH_CHOICE_TIMEOUT` | 10 Sekunden | Wenn Spieler keinen Pfad wählt → Auto-Wahl (erster Pfad) |
| `MINIGAME_LOAD_TIMEOUT` | 10 Sekunden | Wenn Client Minispiel nicht lädt → Client wird als disconnected markiert |
| `INPUT_ACK_TIMEOUT` | 5 Sekunden | Wenn Client keinen Input sendet → Letzter bekannter Input wird wiederholt |

#### Keine Input-Prediction

Für Minispiele verzichten wir auf Client-seitige Input-Prediction. Begründung:
- Minispiele sind kurz (30s). Selbst bei 150ms Latenz ist das Spielerlebnis akzeptabel.
- Input-Prediction erfordert deterministische Spiel-Logik auf Client UND Server → hohe Komplexität, hohes Bug-Risiko.
- Server-Autoritativ ohne Prediction ist das einfachste Modell und passt zum Casual/Party-Genre.

#### Lag-Ausgleich (Minispiele)

Falls ein Spieler hohe Latenz hat (>200ms) und andere niedrige (<50ms):
- **Server-seitige Entprellung:** Server wartet maximal 50ms auf Inputs aller Spieler bevor er den nächsten Frame berechnet (Frame-Delay).
- **Visuelle Indikatoren:** Verbindungsqualität wird im HUD angezeigt (grün/gelb/rot).

### 3.11 Sicherheit (Cheat-Schutz)

#### Grundprinzip: Server-Autoritativ

Der Server validiert JEDE Client-Aktion. Keine Ausnahmen.

#### Validierungs-Checkliste pro Aktion

| Aktion | Validierung |
|---|---|
| Würfeln | `current_player == sender` AND `phase == "ROLL"` AND `player_has_not_rolled` AND `is_connected` |
| Stern kaufen | `player.coins >= MÜNZEN_FÜR_STERN` AND `player.position == active_star_shop_index` AND `star_available` AND `phase == "SHOP"` |
| Item kaufen | `player.coins >= item.price` AND `player.items.size() < MAX_ITEMS` AND `player.position in item_shop_positions` AND `phase == "SHOP"` |
| Item benutzen | `item_id in player.items` AND `phase == "ROLL" or phase == "MOVE"` (je nach Item) AND `item_not_on_cooldown` |
| Pfad wählen | `field.next.size() > 1` AND `chosen_index in [0, 1, 2]` AND `chosen_path_exists` |

#### Zusätzliche Schutzmaßnahmen

- **Rate Limiting:** Maximal 10 RPCs pro Sekunde pro Client. Bei Überschreitung → Client wird gekickt.
- **State-Integritäts-Check (optional, Debug):** Server kann periodisch einen Hash des gesamten Spielzustands berechnen und mit Clients vergleichen. Bei Abweichung → Client wird synchronisiert.
- **Kein Client-seitiges Speichern:** Alle persistenten Daten (Statistiken, Freischaltungen) werden NUR vom Server gespeichert. Clients haben keine Schreibrechte auf `data.cfg` während des Spiels.

---

## 4. Formulas

### 4.1 RPC-Validierung (Standard-Template)

Jede `@rpc("any_peer")` Funktion MUSS dieses Validierungs-Muster implementieren:

```
func _rpc_request_<aktion>(...):
    # Schritt 1: Validierung — Server-Prüfung
    if not multiplayer.is_server():
        push_error("[ERROR] _rpc_request_<aktion> vom Nicht-Server aufgerufen!")
        return

    # Schritt 2: Sender-Validierung
    var sender_id = multiplayer.get_remote_sender_id()
    if sender_id < 1 or sender_id > MAX_PLAYERS:
        push_error("[ERROR] Ungültige sender_id: %d" % sender_id)
        return

    # Schritt 3: Spielzustands-Validierung
    if not _validate_action(sender_id, <aktions-spezifische Parameter>):
        push_warning("[WARN] Aktion von Spieler %d abgelehnt: <grund>" % sender_id)
        return

    # Schritt 4: Aktion ausführen
    _execute_action(sender_id, <parameter>)

    # Schritt 5: Ergebnis broadcasten
    _broadcast_result.rpc(<ergebnis>)
```

### 4.2 Dice-Wert-Berechnung (Server-seitig)

```
func _calculate_dice_value(player_id: int) -> int:
    var base_value = randi_range(DICE_MIN, DICE_MAX)  # 1–6

    # Item-Effekte prüfen (Reihenfolge wichtig!)
    if "glueckswuerfel" in players[player_id].items:
        base_value = LUCKY_DICE_VALUE  # 5
        _remove_item(player_id, "glueckswuerfel")

    return base_value
```

### 4.3 Minispiel-Score-Normalisierung

Minispiele liefern Roh-Scores in unterschiedlichen Einheiten (Münzen gesammelt, Zeit, Entfernung). Der Server normalisiert diese Scores für die Rangliste:

```
func _normalize_scores(raw_scores: Dictionary) -> Array:
    # raw_scores: {player_id: float} — Roh-Score pro Spieler
    # Rückgabe: Array[{player_id: int, score: float, placement: int}] sortiert

    var rankings = []
    for player_id in raw_scores:
        rankings.append({"player_id": player_id, "score": raw_scores[player_id]})

    # Sortieren: Höchster Score zuerst (außer bei "Zeit"-basierten Minispielen)
    if minigame.sort_order == "ascending":  # Niedrigster Score gewinnt (z.B. Zeit)
        rankings.sort_custom(func(a, b): return a.score < b.score)
    else:  # Höchster Score gewinnt (Standard)
        rankings.sort_custom(func(a, b): return a.score > b.score)

    # Platzierungen zuweisen (1, 2, 3, ...)
    for i in range(rankings.size()):
        rankings[i]["placement"] = i + 1

    return rankings
```

### 4.4 Münz-Belohnungen (Minispiel)

```
func _calculate_coin_rewards(rankings: Array) -> Dictionary:
    var rewards = {}
    for rank in rankings:
        match rank.placement:
            1: rewards[rank.player_id] = MINIGAME_WINNER_COINS   # 10
            2: rewards[rank.player_id] = MINIGAME_2ND_COINS       # 5
            3: rewards[rank.player_id] = MINIGAME_3RD_COINS       # 3
            _: rewards[rank.player_id] = 0
    return rewards
```

---

## 5. Edge Cases

### 5.1 Alle 8 Spieler verbinden gleichzeitig

**Situation:** 8 Clients senden gleichzeitig `create_client()` an den Server.

**Verhalten:**
- ENet verarbeitet `peer_connected` Signale sequenziell (pro Frame ein Signal).
- Server akzeptiert max 8 Verbindungen. Der 9. Verbindungsversuch wird mit `CONNECTION_REFUSED` abgelehnt.
- Lobby-HUD aktualisiert sich nach jedem Join (kein Race-Condition, da Signale im Main-Thread verarbeitet werden).

### 5.2 Spieler disconnected während Minispiel

**Situation:** Ein Spieler verliert die Verbindung mitten im Minispiel (z.B. Sekunde 15 von 30).

**Verhalten:**
- Server markiert `player.is_connected = false`.
- Der disconnectete Spieler verbleibt im Minispiel-Scoreboard mit seinem aktuellen Score (falls > 0).
- Falls der Score 0 ist, wird er auf den letzten Platz gesetzt.
- Das Minispiel läuft normal weiter für die verbleibenden Spieler.
- Nach dem Minispiel: KI übernimmt den disconnecteten Spieler für den Rest des Spiels.

### 5.3 Server stürzt während Minispiel ab

**Situation:** Der Host-PC stürzt ab (Bluescreen, Stromausfall, Prozess-Kill).

**Verhalten:**
- Alle Clients detektieren `server_disconnected`.
- Kein Client kann das Minispiel fortsetzen (kein Server = keine Logik).
- Alle Clients zeigen Dialog: "Verbindung zum Server verloren. Zurück zum Hauptmenü."
- Das Spielergebnis ist verloren (kein persistentes Save-Game während Minispiel).

### 5.4 Client lädt Minispiel-Plugin nicht (korrupte Datei)

**Situation:** Ein Client hat ein beschädigtes Minispiel-Plugin (fehlende `.pck` oder beschädigte `minigame.tscn`).

**Verhalten:**
- Client detektiert Fehler beim `ResourceLoader.load()` und sendet `_rpc_minigame_load_failed(error_message)`.
- Server erhält die Fehlermeldung, markiert den Spieler als "nicht bereit".
- Server startet Minispiel NACH Timeout (10s). Der fehlerhafte Client wird Letzter.
- Nach dem Minispiel: Server sendet `_rpc_kick_player(player_id, "Minispiel konnte nicht geladen werden.")` und der Spieler wird aus dem Spiel entfernt (KI übernimmt).

### 5.5 Lobby voll (8/8), weiterer Spieler versucht zu joinen

**Situation:** Lobby hat bereits 8 Spieler. Ein 9. Client sendet `create_client()`.

**Verhalten:**
- Server lehnt Verbindung ab: `peer.create_server(10567, 8)` akzeptiert nur 8 Clients.
- Der 9. Client erhält einen Verbindungsfehler (`connection_failed` Signal).
- Client zeigt Fehlermeldung: "Lobby ist voll (max. 8 Spieler)."

### 5.6 Host-Spieler trennt Verbindung

**Situation:** Im Host+Client-Modus (ein Spieler ist Server + Client) verlässt der Host das Spiel.

**Verhalten:**
- Server-Prozess wird beendet (Host = Server).
- Alle anderen Clients: `server_disconnected` Signal.
- Keine Host-Migration (bewusste Entscheidung, siehe Abschnitt 3.9).
- Alle Clients kehren zum Hauptmenü zurück.

### 5.7 Netzwerk-Latenz-Spike während RPC

**Situation:** Ein RPC kommt aufgrund von Netzwerkproblemen verzögert an (z.B. 2 Sekunden statt 50ms).

**Verhalten:**
- ENet (Reliable-Modus) stellt die Nachricht garantiert zu, sobald die Verbindung wiederhergestellt ist.
- Server puffert State-Updates. Bei Wiederherstellung werden alle ausstehenden Updates in einem Batch gesendet.
- Client "springt" visuell (keine Smooth-Interpolation für State-Updates) — das ist akzeptabel für ein Turn-basiertes Spiel.
- Minispiel: Unreliable Inputs werden verworfen. Server interpoliert den letzten bekannten Input für 500ms.

### 5.8 Zwei Spieler wählen denselben Charakter

**Situation:** Beide Spieler senden fast gleichzeitig `_rpc_request_character("brix")`.

**Verhalten:**
- Server verarbeitet RPCs sequenziell. Der erste RPC gewinnt.
- Der zweite RPC wird abgelehnt: `push_warning("[WARN] Charakter 'brix' bereits von Spieler %d gewählt." % existing_player_id)`.
- Server sendet `_rpc_character_rejected(character_name, "Bereits gewählt")` an den zweiten Spieler.
- Client zeigt "Charakter bereits gewählt" und öffnet erneut die Charakter-Auswahl.

---

## 6. Dependencies

### 6.1 Interne Abhängigkeiten

| Komponente | Abhängig von | Beschreibung |
|---|---|---|
| `server/game.gd` | `ENetMultiplayerPeer` (Godot) | Server-seitiges Multiplayer-Setup |
| `client/game.gd` | `ENetMultiplayerPeer` (Godot) | Client-seitiges Multiplayer-Setup |
| `server/lobby.gd` | `common/lobby.gd` | Lobby Basis-Klasse |
| `client/lobby.gd` | `common/lobby.gd` | Lobby Basis-Klasse |
| `server/minigame_queue.gd` | `minigame_loader.gd` | Minispiel-Auswahl |
| Alle `.gd` mit RPCs | `multiplayer` (Godot Singleton) | RPC-Infrastruktur |
| `controller.gd` | `server/game.gd` (RPCs) | Server-Spielfluss |
| `player_board.gd` | `client/game.gd` (RPC-Empfänger) | Client-seitige Animationen |

### 6.2 Externe Abhängigkeiten

| Abhängigkeit | Version | Zweck |
|---|---|---|
| ENet | Godot-integriert (enet 1.3.17) | UDP-Netzwerk-Transport |
| ENetMultiplayerPeer | Godot 4.2.2 integriert | Multiplayer-Abstraktion |

### 6.3 Keine Abhängigkeiten

- **Kein WebSocket** für Spiel-Logik (WebSocket nur für optionalen Server-Browser, nicht für In-Game-Kommunikation).
- **Kein Steamworks** (Steam Networking nicht im initialen Scope).
- **Kein Photon / Mirror / andere Networking-Bibliotheken** (ENet reicht).

---

## 7. Tuning Knobs

### 7.1 Netzwerk-Parameter

| Parameter | Ort | Standard | Bereich | Beschreibung |
|---|---|---|---|---|
| `port` | `server/game.gd`, `common/scripts/global.gd` | `10567` | `1024–65535` | Server-Port |
| `max_clients` | `server/game.gd` | `8` | `2–8` | Maximale Clients |
| `connection_timeout` | ENet-Parameter | `5000` ms | `1000–15000` | Verbindungs-Timeout |
| `reliable_channel` | RPC-Default | Kanal 0 | `0, 1, 2` | Reliable Kanal |
| `unreliable_channel` | RPC-Parameter | Kanal 1 | `0, 1, 2` | Unreliable Kanal |
| `max_rpc_per_second` | `server/game.gd` | `10` | `5–30` | Rate Limiting |

### 7.2 Timeout-Parameter

| Parameter | Ort | Standard | Bereich | Beschreibung |
|---|---|---|---|---|
| `TURN_TIMEOUT` | `common/scripts/global.gd` | `30` s | `10–60` | Würfel-Timeout |
| `SHOP_TIMEOUT` | `common/scripts/global.gd` | `15` s | `5–30` | Shop-Timeout |
| `PATH_CHOICE_TIMEOUT` | `common/scripts/global.gd` | `10` s | `5–20` | Pfad-Wahl-Timeout |
| `MINIGAME_LOAD_TIMEOUT` | `common/scripts/global.gd` | `10` s | `5–20` | Minispiel-Lade-Timeout |
| `INPUT_ACK_TIMEOUT` | `server/game.gd` | `5` s | `2–10` | Input-Bestätigungs-Timeout |

### 7.3 Minispiel-Parameter

| Parameter | Ort | Standard | Bereich | Beschreibung |
|---|---|---|---|---|
| `MINIGAME_SYNC_INTERVAL` | `server/game.gd` | `50` ms | `16–100` | Sync-Intervall während Minispiel |
| `MINIGAME_INPUT_INTERVAL` | `client/game.gd` | `33` ms | `16–66` | Input-Sende-Intervall |
| `MINIGAME_LAG_COMPENSATION` | `server/game.gd` | `50` ms | `0–100` | Frame-Delay für Lag-Ausgleich |

### 7.4 Lobby-Tuning

| Parameter | Ort | Standard | Bereich | Beschreibung |
|---|---|---|---|---|
| `LOBBY_SIZE` | `common/lobby.gd` | `8` | `2–8` | Maximale Spieler in Lobby |
| `MIN_PLAYERS_TO_START` | `common/lobby.gd` | `2` | `1–8` | Minimum Spieler zum Starten |
| `LOBBY_COUNTDOWN` | `common/lobby.gd` | `5` s | `3–10` | Countdown vor Spielstart |

---

## 8. Acceptance Criteria

### 8.1 Verbindungsaufbau

- [ ] **AC-MP-001:** Server startet auf Port 10567 mit `ENetMultiplayerPeer.create_server(10567, 8)` und akzeptiert bis zu 8 Clients.
- [ ] **AC-MP-002:** Client verbindet sich mit `ENetMultiplayerPeer.create_client(ip, port)` und erhält `peer_connected` Signal.
- [ ] **AC-MP-003:** 9. Verbindungsversuch wird abgelehnt (ENet lehnt ab, Client zeigt "Lobby voll").

### 8.2 RPC-System

- [ ] **AC-MP-004:** Alle `@rpc("authority")` Funktionen werden nur vom Server aufgerufen. Client-seitiger Aufruf führt zu Fehler (Godot verweigert).
- [ ] **AC-MP-005:** Alle `@rpc("any_peer")` Funktionen validieren den Sender und die Spielaktion bevor sie ausgeführt werden.
- [ ] **AC-MP-006:** Rate Limiting: Mehr als 10 RPCs/Sekunde von einem Client führen zu Kick.

### 8.3 Spielfluss (Board)

- [ ] **AC-MP-007:** Würfel-Request: Client sendet `_rpc_request_roll()`, Server validiert, würfelt, sendet `_rpc_dice_result()` an alle. Client zeigt Würfel-Animation.
- [ ] **AC-MP-008:** Stern-Kauf: Client sendet `_rpc_request_buy_star()`, Server prüft `coins >= 20` und `position == star_shop`, sendet `_rpc_star_purchased()`.
- [ ] **AC-MP-009:** Item-Kauf: Client sendet `_rpc_request_buy_item(item_id)`, Server prüft `coins >= price` und `items.size() < 3`, sendet `_rpc_item_purchased()`.
- [ ] **AC-MP-010:** Pfad-Wahl: Client sendet `_rpc_request_path_choice(index)`, Server prüft ob Feld mehrere `next`-Indizes hat, sendet Bewegungspfad.

### 8.4 Minispiel

- [ ] **AC-MP-011:** Server sendet `_rpc_minigame_start(name, seed)` an alle. Alle Clients laden Minispiel innerhalb von 10 Sekunden.
- [ ] **AC-MP-012:** Während Minispiel: Client sendet Input-Stream (unreliable, ca. alle 33ms). Server berechnet und sendet Sync-Updates (alle 50ms).
- [ ] **AC-MP-013:** Minispiel-Ende: Server sendet `_rpc_minigame_result(rankings, coin_rewards)`. Clients zeigen Reward-Screen.
- [ ] **AC-MP-014:** Client der Minispiel nicht laden kann → disconnect nach 10s Timeout.

### 8.5 Lobby

- [ ] **AC-MP-015:** Lobby unterstützt 8 Spieler (1–8 Slots sichtbar, Charakter-Auswahl für alle 8).
- [ ] **AC-MP-016:** Host wählt Board aus 8 Inseln. Board-Auswahl wird an alle Clients broadcasted.
- [ ] **AC-MP-017:** Charakter-Konflikt: Zwei Spieler können nicht denselben Arenian wählen. Zweite Wahl wird abgelehnt.
- [ ] **AC-MP-018:** Host startet Spiel. Minimum 2 Spieler müssen verbunden sein.

### 8.6 8-Spieler-Erweiterung

- [ ] **AC-MP-019:** `PLAYER_TRANSLATION` Array hat 8 Einträge (nicht 4).
- [ ] **AC-MP-020:** InputMap enthält Actions für 8 Spieler (`_p1` bis `_p8`).
- [ ] **AC-MP-021:** Splitscreen: 2–4 Spieler = 2×2 Split. 5–8 Spieler = Shared Screen (kein Split).

### 8.7 Lokaler Multiplayer

- [ ] **AC-MP-022:** `Global.create_local_server()` startet Server und akzeptiert lokale Verbindungen auf `127.0.0.1:10567`.
- [ ] **AC-MP-023:** 8 lokale Clients können simultan verbunden sein und spielen.

### 8.8 Disconnect

- [ ] **AC-MP-024:** Spieler-Disconnect: Server markiert `is_connected = false`, KI übernimmt. Verbleibende Clients sehen Disconnect-Indikator.
- [ ] **AC-MP-025:** Server-Disconnect: Alle Clients zeigen "Verbindung verloren" Dialog und kehren zum Hauptmenü zurück.
- [ ] **AC-MP-026:** Disconnect während Minispiel: Betroffener Spieler wird Letzter. Minispiel läuft normal weiter.

### 8.9 Timeout

- [ ] **AC-MP-027:** Nach 30s ohne Würfel-Input: Auto-Würfel.
- [ ] **AC-MP-028:** Nach 15s ohne Shop-Aktion: Auto-Pass.
- [ ] **AC-MP-029:** Nach 10s ohne Pfad-Wahl: Auto-Wahl (erster Pfad).

### 8.10 Sicherheit

- [ ] **AC-MP-030:** Client kann Münzen NICHT direkt ändern (kein RPC dafür, Server validiert alle Münz-Änderungen).
- [ ] **AC-MP-031:** Server validiert alle Käufe (Stern, Item) — prüft `coins >= price`, `position`, `star_available`.
- [ ] **AC-MP-032:** Client kann Items nicht duplizieren oder verwenden, die nicht im Inventar sind.

---

> **Nächste Datei:** `technical-fork-strategy.md` — Fork-Strategie  
> **Referenz:** `technical-architecture.md` — Gesamtarchitektur  
> **Referenz:** `technical-data-structures.md` — Datenstrukturen  
> **Referenz:** `technical-performance.md` — Performance-Ziele
