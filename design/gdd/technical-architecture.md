# Technische Architektur — Party Arena

> **Status:** Proposed  
> **Version:** 2.0.0  
> **Letzte Änderung:** 2026-08-11  
> **Abhängigkeiten:** game-concept.md, vision-pillars.md

---

## 1. Overview

Party Arena ist ein harter Fork von Super Tux Party (STP), einem rundenbasierten Party-Brettspiel. Die technische Architektur beschreibt die Engine, das Architekturmuster, die Ordnerstruktur und die Systeme, die dem Spiel zugrunde liegen. Die Architektur folgt dem Prinzip eines **server-autoritativen Multiplayer-Spiels** mit einem **Plugin-System** für austauschbare Inhalte (Boards, Charaktere, Items, Minispiele).

### Kernentscheidungen

| Entscheidung | Wert | Begründung |
|---|---|---|
| Engine | Godot 4.2.x (exakt, nicht 4.3+) | STP läuft auf Godot 4.2; Upgrade auf 4.3+ birgt Breaking Changes in GDScript, Rendering und Networking ohne Mehrwert für dieses Projekt. |
| Sprache | GDScript mit Static Typing | STP-Codebasis ist GDScript. Static Typing (`:Typ` statt `:=`) wurde via Skill Pitfall #1 flächendeckend fixiert. |
| Renderer | Forward+ (Desktop), Forward Mobile (Mobile) | Godot 4 Default. Forward+ liefert gute Performance für Cartoon-Stil ohne teure Screen-Space-Effekte. |
| Physik | GodotPhysics (Default) | Komplexe Physik nur in Minispielen; Jolt-Integration nicht nötig. |
| Multiplayer | ENet via ENetMultiplayerPeer, Server-Authoritativ | Siehe technical-multiplayer.md. |

### Warum Godot 4.2 und nicht 4.3+?

Godot 4.3 führte signifikante Änderungen ein:
- **GDScript:** Neue Annotationen (`@export_custom`, geändertes `@onready`-Verhalten), die STP-Code brechen.
- **Networking:** `ENetMultiplayerPeer`-API-Änderungen in 4.3 (geänderte `create_server`-Signatur, neue `peer_connected`-Signale).
- **Rendering:** `Forward+`-Standard-Pipeline in 4.3 mit geänderten Shader-Preprocessor-Direktiven.

Das Projekt friert auf **Godot 4.2.2** ein (letzter stabiler Patch). Ein Upgrade auf 4.3+ wird als separates Projekt evaluiert, frühestens nach dem ersten stabilen Release von Party Arena.

### Architekturmuster: Server-Authoritativ

```
┌──────────────────────────────────────────────────────┐
│                   SERVER (Host)                       │
│  ┌─────────────────────────────────────────────────┐ │
│  │           Spiel-Logik (Controller.gd)            │ │
│  │  - Runden-Logik                                 │ │
│  │  - Würfeln, Bewegung, Events, Stern-Kauf        │ │
│  │  - Bonus-Sterne-Berechnung                      │ │
│  │  - Item-Effekte                                 │ │
│  │  - Minispiel-Ergebnisse                         │ │
│  └──────────────┬──────────────────────────────────┘ │
│                 │ State Updates (Broadcast)           │
│  ┌──────────────▼──────────────────────────────────┐ │
│  │         ENetMultiplayerPeer                      │ │
│  │  - Server-Authoritativ                          │ │
│  │  - RPC: @rpc("authority") / @rpc("any_peer")    │ │
│  └──────────────┬──────────────────────────────────┘ │
└─────────────────┼────────────────────────────────────┘
                  │
    ┌─────────────┼──────────────┬─────────────┐
    │             │              │             │
┌───▼───┐   ┌─────▼────┐   ┌────▼────┐   ┌───▼───┐
│Client 1│   │Client 2  │   │Client 3 │   │Client 8│
│Render  │   │Render    │   │Render   │   │Render  │
│Input   │   │Input     │   │Input    │   │Input   │
│Audio   │   │Audio     │   │Audio    │   │Audio   │
└────────┘   └──────────┘   └─────────┘   └────────┘
```

**Server-Autoritativ bedeutet konkret:**
- Der Server ist die einzige Quelle der Wahrheit für alle Spielzustände (Münzen, Sterne, Positionen, Items).
- Clients senden **nur** Spieler-Input (Würfeln, Item-Auswahl, Shop-Kauf, Pfad-Wahl).
- Der Server validiert jeden Input (z.B. "Hat der Spieler genug Münzen für diesen Kauf?", "Ist dieses Item im Inventar?").
- Der Server berechnet das Ergebnis und sendet es als autoritative State-Update an alle Clients.
- Clients rendern ausschließlich den empfangenen State; sie führen keine Spiel-Logik aus.

---

## 2. Player Fantasy

Die technische Architektur ist für den Spieler unsichtbar — sie soll ein reibungsloses, verzögerungsfreies Erlebnis ermöglichen, bei dem das Spiel "einfach funktioniert".

### Was der Spieler erlebt

- **Sofortiges Feedback:** Würfeln, Bewegung, Item-Effekte — alle Aktionen fühlen sich direkt an (<100ms Verzögerung).
- **Kein Cheating:** Spieler können nicht schummeln (Münzen manipulieren, Items duplizieren). Der Server kontrolliert alles.
- **Stabilität:** Das Spiel läuft flüssig, keine Ruckler oder Frame-Einbrüche, selbst bei 8 Spielern auf dem Board.
- **Splitscreen:** Bis zu 4 Spieler spielen bequem am gleichen Bildschirm; jeder hat seinen eigenen Viewport.
- **Schnelle Ladezeiten:** Minispiele laden in <2 Sekunden.

### Was der Entwickler erlebt

- **Plugin-System:** Neue Boards, Charaktere, Items und Minispiele können ohne Änderung am Core-Code hinzugefügt werden.
- **Klare Trennung:** Server-Logik, Client-Rendering und geteilte Logik sind strikt getrennt — kein versehentliches Ausführen von Server-Code auf dem Client.
- **Static Typing:** Alle GDScript-Funktionen haben deklarierte Rückgabetypen und Parameter-Typen. Autocomplete funktioniert zuverlässig.

---

## 3. Detailed Rules

### 3.1 Ordnerstruktur — Vollständig

```
/opt/data/SuperTuxParty/
├── client/                    # Client-spezifischer Code
│   ├── game.tscn              # Client Game Szene (Hauptszene)
│   ├── game.gd                # Client Game Manager
│   ├── lobby.tscn             # Client Lobby Szene
│   ├── lobby.gd               # Client Lobby Logik
│   ├── websocket/             # WebSocket Client (optional, für Server-Browser)
│   ├── menus/                 # UI-Menüs
│   │   ├── main_menu.tscn     # Hauptmenü Szene
│   │   ├── main_menu.gd       # Hauptmenü Logik
│   │   ├── lobby/             # Lobby-Menüs
│   │   │   ├── servermenu.tscn
│   │   │   ├── servermenu.gd
│   │   │   ├── lobby_menu.tscn
│   │   │   ├── lobby_menu.gd
│   │   │   ├── character_menu.tscn
│   │   │   └── character_menu.gd
│   │   ├── characters/        # [NEU] Character-Auswahl
│   │   │   ├── character_select.tscn
│   │   │   └── character_select.gd
│   │   ├── boards/             # [NEU] Board-Auswahl
│   │   │   ├── board_select.tscn
│   │   │   └── board_select.gd
│   │   ├── pause_menu.tscn
│   │   ├── pause_menu.gd
│   │   ├── options_menu.tscn
│   │   ├── options_menu.gd
│   │   └── victory_screen/    # Sieger-Bildschirm
│   │       ├── victory_screen.tscn
│   │       └── victory_screen.gd
│   └── rewardscreens/          # Belohnungs-Bildschirme
│       ├── ffa/                # Free-For-All
│       │   ├── ffa_rewardscreen.tscn
│       │   └── ffa_rewardscreen.gd
│       └── duel/               # [ENTFERNEN — kein Duel in PA]
│
├── server/                    # Server-Code
│   ├── game.tscn              # Server Game Szene
│   ├── game.gd                # Server Game Manager
│   ├── server.tscn             # Dedicated Server Szene
│   ├── lobby.tscn             # Server Lobby Szene
│   ├── lobby.gd               # Server Lobby Logik
│   ├── minigame_queue.gd      # Minispiel-Warteschlange
│   ├── api/                   # HTTP API (Server-Browser, Statistiken)
│   └── websocket/             # WebSocket Server
│
├── common/                    # Geteilte Logik (Server + Client)
│   ├── lobby.gd               # Geteilte Lobby Basis-Klasse
│   ├── scenes/
│   │   ├── board_logic/       # Board-Logik
│   │   │   ├── controller/    # Spiel-Fluss Controller
│   │   │   │   ├── controller.tscn
│   │   │   │   ├── controller.gd       # [REWRITE]
│   │   │   │   ├── player_info.tscn    # Spieler-HUD
│   │   │   │   ├── player_info.gd      # Spieler-HUD Logik
│   │   │   │   ├── shop.tscn           # Shop-UI
│   │   │   │   ├── shop.gd             # Shop-Logik
│   │   │   │   ├── shop_item.tscn      # Shop-Item
│   │   │   │   ├── shop_item.gd        # Shop-Item Logik
│   │   │   │   ├── duelselection.tscn  # [ENTFERNEN]
│   │   │   │   ├── duelselection.gd    # [ENTFERNEN]
│   │   │   │   ├── arena_star.gd       # [NEU] ArenaStar Controller
│   │   │   │   └── arena_star.tscn     # [NEU] ArenaStar Szene
│   │   │   ├── node/           # Feldtypen
│   │   │   │   ├── node.tscn
│   │   │   │   └── node.gd             # [REWRITE — neues Enum]
│   │   │   └── player_board/   # Spieler-Darstellung auf Board
│   │   │       ├── player_board.tscn
│   │   │       └── player_board.gd     # [MODIFIZIEREN — 8P]
│   │   ├── countdown/          # Countdown-Animation
│   │   ├── sound_button/       # UI Sound Button
│   │   └── ...                 # Weitere UI-Komponenten
│   ├── scripts/
│   │   ├── global.gd           # Globaler State, Konstanten
│   │   ├── utility.gd          # Hilfsfunktionen (Math, Array, RNG)
│   │   ├── control_helper.gd   # Input-Helfer für UI
│   │   ├── character.gd        # Charakter Basis-API
│   │   ├── event_system.gd     # [NEU] Ereignis-System
│   │   ├── bonus_star.gd       # [NEU] Bonus-Stern-Berechnung
│   │   ├── loader/             # Plugin-Loader
│   │   │   ├── plugin_system.gd
│   │   │   ├── board_loader.gd
│   │   │   ├── character_loader.gd
│   │   │   ├── item_loader.gd
│   │   │   └── minigame_loader.gd
│   │   └── tracking_manager.gd # Analyse-Tracking (optional)
│   └── savegames/              # Speicher-System
│       └── savegames.gd
│
├── plugins/                   # Plugin-System (austauschbare Inhalte)
│   ├── boards/                # Board-Plugins
│   │   ├── sonnenstrand/      # [NEU]
│   │   ├── korallenriff/      # [NEU]
│   │   ├── vulkaninsel/       # [NEU]
│   │   ├── nebelwald/         # [NEU]
│   │   ├── kristallhoehle/    # [NEU]
│   │   ├── wolkenreich/       # [NEU]
│   │   ├── zeitgarten/        # [NEU]
│   │   └── schattenarchipel/  # [NEU]
│   ├── characters/            # Charakter-Plugins
│   │   ├── brix/              # [NEU]
│   │   ├── nixie/             # [NEU]
│   │   ├── koko/              # [NEU]
│   │   ├── pip/               # [NEU]
│   │   ├── zara/              # [NEU]
│   │   ├── flint/             # [NEU]
│   │   ├── luna/              # [NEU]
│   │   └── momo/              # [NEU]
│   ├── items/                 # Item-Plugins
│   │   ├── glueckswuerfel/    # [NEU]
│   │   ├── schutzschild/      # [NEU]
│   │   ├── muenzmagnet/       # [NEU]
│   │   ├── teleporter/        # [NEU]
│   │   └── diebhandschuh/     # [NEU]
│   └── minigames/             # Minispiel-Plugins
│       ├── muenzregen/        # [NEU]
│       ├── schildkrötenrennen/# [NEU]
│       ├── kokosnuss_werfen/  # [NEU]
│       ├── krabben_jagd/      # [NEU]
│       ├── muschel_memory/    # [NEU]
│       ├── wellen_reiten/     # [NEU]
│       ├── perlen_tauchen/    # [NEU]
│       ├── vulkan_ausbruch/   # [NEU]
│       ├── laternen_flug/     # [NEU]
│       ├── brücken_bau/       # [NEU]
│       ├── nebel_irrgarten/   # [NEU]
│       └── schatz_trage/      # [NEU]
│
├── assets/                    # [NEU AUFBAUEN]
│   ├── models/                # 3D-Modelle (.glb/.gltf)
│   │   ├── characters/        # Charakter-Modelle (8 Arenians)
│   │   ├── boards/            # Insel-Board-Teile
│   │   ├── items/             # Item-Modelle
│   │   └── props/             # Dekorationen, ArenaStar
│   ├── textures/              # Texturen
│   │   ├── characters/        # Charakter-Texturen
│   │   ├── boards/            # Board-Texturen
│   │   ├── ui/                # UI-Texturen
│   │   └── effects/           # Partikel-Texturen
│   ├── sounds/                # Soundeffekte (.ogg)
│   │   ├── ui/                # UI-Sounds
│   │   ├── board/             # Board-Sounds
│   │   ├── items/             # Item-Sounds
│   │   └── minigames/         # Minispiel-Sounds
│   ├── music/                 # Musik (.ogg)
│   │   ├── menu/              # Menü-Musik
│   │   ├── boards/            # Board-Musik (pro Insel)
│   │   └── minigames/         # Minispiel-Musik
│   └── fonts/                 # Schriftarten
│       ├── ui/                # UI-Fonts (.ttf/.otf)
│       └── effects/           # Effekt-Fonts (Titel, Scores)
│
├── addons/                    # Godot Addons (unverändert von STP)
│   └── ...                    # ggf. godot-sqlite, etc.
│
├── translations/              # [NEU / ERWEITERN]
│   ├── de.po                  # Deutsch (Primär)
│   ├── en.po                  # Englisch
│   ├── fr.po                  # Französisch
│   ├── es.po                  # Spanisch
│   ├── ja.po                  # Japanisch
│   └── zh.po                  # Chinesisch
│
├── project.godot              # Projekt-Konfiguration [MODIFIZIEREN]
├── default_env.tres           # Default-Umgebung
├── icon.webp                  # Projekt-Icon [NEU]
└── export_presets.cfg         # Export-Voreinstellungen [NEU]
```

### 3.2 Engine-Systeme im Detail

#### Render-Pipeline

- **Renderer:** Forward+ (Desktop), Forward Mobile (Mobile). Dies ist der Godot 4 Default und der performanteste Renderer für unseren Cartoon-Stil.
- **Kein:** Forward+ Clustered Rendering, Mobile Renderer auf Desktop, Raytracing (Vulkan RT), SDFGI (Signed Distance Field Global Illumination).
- **Beleuchtung:** DirectionalLight3D (Sonne) + bis zu 8 OmniLight3D (Lampen, Fackeln pro Board). Keine dynamischen Schatten jenseits von DirectionalLight (Performance).
- **Post-Processing:**
  - Color Grading via LUT-Textur (32×32×32, neutrales LUT als Basis)
  - Leichte Vignette (Intensity 0.3, Opacity 0.5)
  - **Kein:** SSAO, SSR, SSIL, Glow (Bloom), DOF (Depth of Field), Motion Blur — alle deaktiviert für konsistenten Cartoon-Look und Performance.
- **Anti-Aliasing:** Godot's TAA (Temporal Anti-Aliasing) mit Default-Einstellungen. Alternativ: MSAA 2× oder 4× (konfigurierbar in Video-Optionen).
- **Auflösungs-Skalierung:** Godot's `scaling_3d_scale` (0.5–1.0, konfigurierbar) für Performance-Skalierung.

#### Physik

- **Engine:** GodotPhysics (Default in Godot 4). Kein Jolt, kein Bullet.
- **Nutzung:** Nur in Minispielen, die Physik erfordern (z.B. "Kokosnuss Werfen" mit RigidBody3D).
- **Board:** Keine Physik-Simulation auf dem Board. Bewegung ist rein kinematisch (Tween-Animationen entlang Pfaden).
- **Physics Ticks:** Default 60 Hz (`physics_ticks_per_second = 60`).

#### Input-System

- **InputMap:** Godot's Projekt-Einstellungen → Input Map. Actions werden mit Suffix `_p1` bis `_p8` definiert.
- **Actions (pro Spieler, p1–p8):**
  - `move_left_pN`, `move_right_pN`, `move_up_pN`, `move_down_pN` (Gameplay)
  - `confirm_pN`, `cancel_pN` (Menü-Navigation)
  - `use_item_pN` (Item verwenden)
  - `taunt_pN` (Emote)
- **Zuweisung:**
  - P1: Tastatur (WASD/Arrow Keys + Enter/Space) + Gamepad 0
  - P2: Tastatur (alternative Keys: IJKL + Shift) + Gamepad 1
  - P3–P8: Gamepad 2–7 (nur Gamepad, keine Tastatur)
- **Input-Polling:** Gameplay-Input wird im `_process()`-Loop gepollt (nicht `_input()` Events), um Input-Stau bei 8 gleichzeitigen Eingaben zu vermeiden. UI-Navigation verwendet das `_input()` Event-System (unproblematisch, da nur ein Spieler gleichzeitig UI navigiert).

#### Audio-System

- **Engine:** Godot AudioServer mit 4 Audio-Bussen.
- **Bus-Struktur:**
  ```
  Master (0 dB)
  ├── Musik (-6 dB, Sidechain-Ducking via SFX)
  ├── SFX (-3 dB)
  └── Stimme (-3 dB, priorisiert)
  ```
- **Effekte pro Bus:**
  - Master: Limiter (Ceiling -0.2 dB), optionaler Compressor
  - Musik: EQ (Low-Shelf +2 dB @ 100 Hz für Bass-Boost)
  - SFX: Reverb (Send, wet 15%, Room Size 0.6)
  - Stimme: Compressor (Threshold -12 dB, Ratio 4:1)
- **Lautstärke-Regler:**
  - Master: 0%–100% (Standard 100%)
  - Musik: 0%–100% (Standard 80%)
  - SFX: 0%–100% (Standard 100%)
  - Stimme: 0%–100% (Standard 90%)
- **Audio-Formate:** OGG Vorbis (`.ogg`)
  - Musik: 128 kbps, Stereo, 44100 Hz
  - SFX: 64 kbps, Mono, 44100 Hz
  - Stimme: 96 kbps, Mono, 44100 Hz (Sprachausgabe für Arenians)

#### Speicher-System

- **Speicherort:** `user://data.cfg` (Godot's User-Datenverzeichnis)
- **Format:** ConfigFile (`.cfg`), wie in STP. Sektionen:
  ```ini
  [settings]
  audio_master=100
  audio_music=80
  audio_sfx=100
  audio_voice=90
  video_resolution=1920x1080
  video_fullscreen=true
  video_vsync=true
  video_aa=2
  video_scale_3d=1.0
  language=de
  accessibility_subtitles=true
  accessibility_colorblind_mode=false
  accessibility_reduce_motion=false

  [statistics]
  total_games_played=0
  total_games_won=0
  total_coins_collected=0
  total_stars_collected=0
  total_minigames_won=0
  favorite_character=brix
  favorite_island=sonnenstrand
  total_playtime_seconds=0

  [unlocks]
  unlocked_characters=["brix","nixie","koko","pip","zara","flint","luna","momo"]
  unlocked_islands=["sonnenstrand","korallenriff","vulkaninsel","nebelwald","kristallhoehle","wolkenreich","zeitgarten","schattenarchipel"]

  [controls]
  # Player-spezifische Keybindings (falls abweichend von Defaults)
  ```

#### Logging

- **Mechanismus:** `print()` für Debug-Logs, `push_error()` für Fehler, `push_warning()` für Warnungen.
- **Kein externes Logging-Framework** (kein Log4j-Port, kein File-Logger). Godot's interne Log-Engine reicht für unser Scope.
- **Log-Levels (Konvention):**
  - `print("[INFO] ...")` — Normale Ereignisse (Spielstart, Rundenwechsel)
  - `print("[DEBUG] ...")` — Debug-Informationen (State-Dumps, RPC-Aufrufe), nur im Debug-Build
  - `push_warning("[WARN] ...")` — Unerwartete aber nicht-kritische Zustände
  - `push_error("[ERROR] ...")` — Kritische Fehler (Netzwerkabbruch, Datei nicht gefunden)

---

## 4. Formulas

### 4.1 Projekt-Konfiguration (project.godot — Schlüsselwerte)

```
[application]
config/name = "Party Arena"
config/version = "2.0.0"
run/main_scene = "res://client/menus/main_menu.tscn"
config/icon = "res://icon.webp"

[autoload]
Global = "*res://common/scripts/global.gd"
# ... weitere Autoloads (Loader, AudioManager, etc.)

[input]
move_left_p1 = { "deadzone": 0.2, "events": [Object(InputEventKey,"resource_local_to_scene":false,"resource_name":"","device":0,"window_id":0,"alt_pressed":false,"shift_pressed":false,"ctrl_pressed":false,"meta_pressed":false,"pressed":false,"keycode":65,"physical_keycode":0,"key_label":0,"unicode":97,"echo":false,"script":null), Object(InputEventKey,"resource_local_to_scene":false,"resource_name":"","device":0,"window_id":0,"alt_pressed":false,"shift_pressed":false,"ctrl_pressed":false,"meta_pressed":false,"pressed":false,"keycode":4194319,"physical_keycode":0,"key_label":0,"unicode":0,"echo":false,"script":null)] }
# ... (analog für alle 8 Spieler, insgesamt 10 Actions × 8 Spieler = 80 Input-Einträge)
```

### 4.2 Konstanten (common/scripts/global.gd)

```
VERSION = "2.0.0"
GAME_NAME = "Party Arena"
MÜNZEN_FÜR_STERN = 20        # War COOKIES_FOR_CAKE = 30 in STP
MAX_TURNS = 10                # Unverändert
MAX_ITEMS = 3                 # Max Items pro Spieler
MAX_PLAYERS = 8               # War 4 in STP
START_COINS = 10              # Start-Münzen (STP hatte 5)
DICE_MIN = 1
DICE_MAX = 6                  # Standard-Würfel
LUCKY_DICE_VALUE = 5          # Glücks-Würfel garantiert eine 5
COIN_MAGNET_DURATION = 3      # Münz-Magnet hält 3 Züge
EVENT_BONUS_COINS = 10        # Standard-Bonus bei Glücks-Events
MINIGAME_WINNER_COINS = 10    # Coins für Minispiel-Sieger
MINIGAME_2ND_COINS = 5        # Coins für 2. Platz
MINIGAME_3RD_COINS = 3        # Coins für 3. Platz
BOARD_FIELDS = 40             # Felder pro Board (Standard)
MAX_TURN_TIMEOUT = 30         # Sekunden bis Auto-Würfel
MINIGAME_DURATION_DEFAULT = 30 # Sekunden (kann pro Minispiel abweichen)
```

---

## 5. Edge Cases

### 5.1 Godot-Version weicht ab

**Situation:** Ein Entwickler öffnet das Projekt mit Godot 4.3+ oder 4.1.

**Verhalten:** Das Projekt enthält einen Pre-Script-Check in `project.godot`, der die Engine-Version prüft. Falls nicht 4.2.x:
- Eine Dialog-Warnung wird angezeigt: "Party Arena benötigt Godot 4.2.x. Installierte Version: X.Y.Z."
- Das Projekt wird im abgesicherten Modus geöffnet (keine Szenen geladen, nur Editor).
- Das Build-Script (`build.sh`) prüft ebenfalls und bricht den Build ab.

**Implementierung:** Ein `EditorPlugin`-Script (`addons/version_check/`) prüft `Engine.get_version_info()` beim Editor-Start.

### 5.2 Static Typing — Unbehandelte Rückgabetypen

**Situation:** Ein Entwickler schreibt eine neue Funktion ohne Rückgabetyp-Deklaration (`func foo():` statt `func foo() -> void:`).

**Verhalten:**
- Godot 4.2 gibt **keinen** Compiler-Fehler bei fehlendem Rückgabetyp (nur Warnung mit `--debug`).
- **Team-Regel:** Jede neue Funktion MUSS einen Rückgabetyp haben. Code-Review blockt PRs ohne Typ-Deklarationen.
- CI-Script prüft via Regex: `func [a-zA-Z_][a-zA-Z0-9_]*\(.*\)\s*:` ohne `->` → CI-Fehler.

### 5.3 Plugin-Loader findet kein Plugin

**Situation:** Ein Plugin-Ordner existiert nicht oder das Plugin-Manifest (`plugin.json`) fehlt.

**Verhalten:**
- `board_loader.gd` / `character_loader.gd` / `item_loader.gd` / `minigame_loader.gd` prüft mit `DirAccess.dir_exists()`.
- Falls nicht vorhanden: `push_error("[ERROR] Plugin-Verzeichnis nicht gefunden: res://plugins/boards/XYZ/")`, das Plugin wird übersprungen.
- Falls `plugin.json` fehlt: `push_error("[ERROR] plugin.json fehlt in Plugin: XYZ")`, das Plugin wird übersprungen.
- Das Spiel wird trotzdem gestartet (fehlertolerant), aber das fehlende Plugin ist nicht verfügbar.
- Im Lobby-Menü wird das fehlende Board/Charakter ausgegraut dargestellt.

### 5.4 Splitscreen — Ein Spieler verlässt das Spiel

**Situation:** Im Splitscreen-Modus (2–4 Spieler, lokaler Multiplayer) verlässt ein Spieler das Spiel (ESC → Leave).

**Verhalten:**
- Der Spieler wird aus der Spieler-Liste entfernt.
- Sein Charakter wird von einer einfachen KI übernommen (Auto-Würfel, Auto-Pass).
- Der Splitscreen wird neu angeordnet: Von 4-Split auf 3-Split, von 3-Split auf 2-Split, von 2-Split auf Fullscreen.
- Das Spiel läuft weiter mit den verbleibenden Spielern.

### 5.5 GodotPhysics vs Jolt — Performance-Problem

**Situation:** Ein Minispiel mit vielen RigidBody3D-Objekten (>50) verursacht Frame-Drops.

**Verhalten:**
- **Erste Maßnahme:** Reduziere die Anzahl gleichzeitiger Physik-Objekte (Objekt-Pooling, max 30 aktive).
- **Zweite Maßnahme:** Reduziere Physics Ticks auf 30 Hz für dieses Minispiel (temporär).
- **Dritte Maßnahme:** Evaluierung von Jolt-Integration als Addon (nicht im initialen Scope, aber technisch möglich via `addons/godot-jolt/`).

### 5.6 8 Spieler Input — Gamepad-Konflikt

**Situation:** Zwei physische Gamepads melden sich mit der gleichen Device-ID (`InputEvent.device`).

**Verhalten:**
- Beim Join prüft das Lobby-System, ob die Device-ID bereits verwendet wird.
- Falls ja: `push_warning("[WARN] Gamepad-Konflikt: Device %d bereits von Spieler %d verwendet.")` und der zweite Spieler wird abgewiesen.
- Lösung für den Spieler: Gamepad neu verbinden (andere ID) oder Tastatur verwenden.

---

## 6. Dependencies

### 6.1 Interne Abhängigkeiten

| Komponente | Abhängig von | Beschreibung |
|---|---|---|
| `client/game.gd` | `common/scripts/global.gd`, `server/game.gd` (via RPC) | Client Game Manager empfängt State vom Server |
| `server/game.gd` | `common/scenes/board_logic/controller/controller.gd` | Server orchestriert Controller |
| `controller.gd` | `node.gd`, `player_board.gd`, `event_system.gd`, `bonus_star.gd` | Spielfluss hängt von allen Subsystemen ab |
| `event_system.gd` | `node.gd` (Feldtyp-Prüfung) | Events werden nur auf EVENT-Feldern ausgelöst |
| `player_board.gd` | `common/scripts/character.gd` | Spieler-Darstellung nutzt Charakter-API |
| `board_loader.gd` | `plugin_system.gd` | Board-Loader nutzt Plugin-System-Basis |
| Alle Loader | `plugin_system.gd` | Plugin-Infrastruktur |
| `project.godot` | Alle Ordner (res://) | Projekt-Konfiguration referenziert alle Pfade |

### 6.2 Externe Abhängigkeiten

| Abhängigkeit | Version | Zweck | Kategorie |
|---|---|---|---|
| Godot Engine | 4.2.2 | Spiel-Engine | Build |
| ENetMultiplayerPeer | Godot-integriert | Networking | Runtime |
| AudioServer | Godot-integriert | Audio | Runtime |
| GDScript | Godot-integriert | Skriptsprache | Runtime |
| Vulkan SDK | 1.3.x (System) | Rendering (Desktop) | Build |
| OpenGL ES 3.0 | System-Treiber | Rendering (Mobile Fallback) | Runtime |
| Freetype | Godot-integriert | Font-Rendering | Runtime |

### 6.3 Optionale / Geplante Abhängigkeiten

| Abhängigkeit | Zweck | Status |
|---|---|---|
| Godot Jolt | Alternative Physik-Engine | Evaluierung (Post-Launch) |
| godot-sqlite | Statistik-Datenbank | Optional (Post-Launch) |
| godot-steam | Steam-Integration (Achievements, Multiplayer) | Optional (Post-Launch) |
| godot-switch | Nintendo Switch 2 Export | Optional (Post-Launch) |

---

## 7. Tuning Knobs

### 7.1 Engine-Tuning (project.godot)

| Parameter | Dateipfad | Standard | Bereich | Beschreibung |
|---|---|---|---|---|
| `rendering/renderer/rendering_method` | `project.godot` | `forward_plus` | `forward_plus`, `mobile` | Render-Methode |
| `rendering/anti_aliasing/quality/msaa_2d` | `project.godot` | `2` | `0, 1, 2, 4, 8` | MSAA für 2D (UI) |
| `rendering/anti_aliasing/quality/msaa_3d` | `project.godot` | `2` | `0, 1, 2, 4, 8` | MSAA für 3D |
| `rendering/quality/3d/scaling_3d_scale` | Runtime (Video-Einstellungen) | `1.0` | `0.5–1.0` in 0.1 Schritten | Auflösungs-Skalierung |
| `physics/common/physics_ticks_per_second` | `project.godot` | `60` | `30, 60` | Physik-Ticks |
| `display/window/size/viewport_width` | `project.godot` | `1920` | `1280–3840` | Fenster-Breite |
| `display/window/size/viewport_height` | `project.godot` | `1080` | `720–2160` | Fenster-Höhe |
| `application/run/main_scene` | `project.godot` | `res://client/menus/main_menu.tscn` | String | Start-Szene |

### 7.2 Audio-Tuning

| Parameter | Speicherort | Standard | Bereich | Beschreibung |
|---|---|---|---|---|
| `audio_master` | `data.cfg` | `100` | `0–100` | Master-Lautstärke |
| `audio_music` | `data.cfg` | `80` | `0–100` | Musik-Lautstärke |
| `audio_sfx` | `data.cfg` | `100` | `0–100` | SFX-Lautstärke |
| `audio_voice` | `data.cfg` | `90` | `0–100` | Stimmen-Lautstärke |
| Musik-ducking | Audio-Bus-Layout | `-6 dB` | `-12 dB – 0 dB` | Musik-Absenkung bei SFX |

### 7.3 Zugänglichkeits-Tuning

| Parameter | Speicherort | Standard | Bereich | Beschreibung |
|---|---|---|---|---|
| `accessibility_subtitles` | `data.cfg` | `true` | `true/false` | Untertitel für Minispiele |
| `accessibility_colorblind_mode` | `data.cfg` | `false` | `true/false` | Farbenblinden-Modus (Symbol-basierte Indikatoren) |
| `accessibility_reduce_motion` | `data.cfg` | `false` | `true/false` | Reduzierte Animationen |
| `accessibility_high_contrast` | `data.cfg` | `false` | `true/false` | Erhöhter UI-Kontrast |

### 7.4 Developer-Tuning (Debug-Flags, nicht im Release)

| Parameter | Beschreibung |
|---|---|
| `--debug-net` | Zeige alle RPC-Aufrufe in der Konsole (Command-Line-Flag) |
| `--debug-state` | Dump Game State jede Runde in die Konsole |
| `--skip-minigames` | Minispiele überspringen (automatisches Ergebnis) |
| `--god-mode` | Unendlich Münzen + Sterne (Test-Modus) |

---

## 8. Acceptance Criteria

### 8.1 Engine & Build

- [ ] **AC-TA-001:** Das Projekt öffnet sich ohne Fehler in Godot 4.2.2 (`Editor → Open Project`).
- [ ] **AC-TA-002:** `project.godot` enthält `config/name = "Party Arena"` und `config/version = "2.0.0"`.
- [ ] **AC-TA-003:** Alle `.gd`-Dateien haben Static Typing (`func foo() -> void:` nicht `func foo():`). CI-Script prüft dies erfolgreich.
- [ ] **AC-TA-004:** Der Projekt-Ordner enthält alle in Abschnitt 3.1 definierten Verzeichnisse (`client/`, `server/`, `common/`, `plugins/`, `assets/`, `addons/`, `translations/`).
- [ ] **AC-TA-005:** `common/scripts/global.gd` enthält `VERSION = "2.0.0"`, `MÜNZEN_FÜR_STERN = 20`, `MAX_PLAYERS = 8`.

### 8.2 Plugin-System

- [ ] **AC-TA-006:** `board_loader.gd` lädt alle Boards aus `plugins/boards/*/` ohne STP-spezifische Prüfungen.
- [ ] **AC-TA-007:** `character_loader.gd` lädt alle Charaktere aus `plugins/characters/*/`.
- [ ] **AC-TA-008:** `item_loader.gd` lädt alle Items aus `plugins/items/*/`.
- [ ] **AC-TA-009:** `minigame_loader.gd` lädt alle Minispiele aus `plugins/minigames/*/`.
- [ ] **AC-TA-010:** Fehlende `plugin.json` führt zu überspringbarem Fehler (Spiel läuft weiter, fehlendes Plugin ist inaktiv).

### 8.3 Rendering

- [ ] **AC-TA-011:** Forward+ Renderer ist aktiv (`rendering/renderer/rendering_method = forward_plus`).
- [ ] **AC-TA-012:** Keine Raytracing- oder SDFGI-Einstellungen in `project.godot`.
- [ ] **AC-TA-013:** Post-Processing: Nur Color-Grading (LUT) + Vignette. SSAO/SSR/Glow/DOF sind deaktiviert.
- [ ] **AC-TA-014:** Toon-Shader ist auf Charakter-Modellen aktiv (Cel-Shading mit 2–3 Tönen, sichtbare Ramp-Textur).

### 8.4 Input

- [ ] **AC-TA-015:** InputMap enthält Actions für 8 Spieler (`move_left_p1` bis `move_left_p8`, `confirm_p1` bis `confirm_p8`, etc.).
- [ ] **AC-TA-016:** Tastatur ist P1 und P2 zugewiesen (P1: WASD + Enter, P2: IJKL + Shift).
- [ ] **AC-TA-017:** Gamepads 0–7 sind P1–P8 zugewiesen.
- [ ] **AC-TA-018:** Gamepad-Konflikt (zwei gleiche Device-IDs) wird erkannt und mit Warnung abgewiesen.

### 8.5 Audio

- [ ] **AC-TA-019:** Audio-Bus-Layout: Master, Musik, SFX, Stimme sind konfiguriert.
- [ ] **AC-TA-020:** Lautstärke-Regler im Options-Menü steuern die 4 Busse (0%–100%).
- [ ] **AC-TA-021:** Musik-Ducking: Musik wird um 6 dB abgesenkt, wenn SFX abgespielt werden.

### 8.6 Speicher

- [ ] **AC-TA-022:** `data.cfg` wird im `user://` Verzeichnis gespeichert.
- [ ] **AC-TA-023:** `data.cfg` enthält Sektionen: `[settings]`, `[statistics]`, `[unlocks]`, `[controls]`.
- [ ] **AC-TA-024:** Statistiken werden nach jedem Spiel aktualisiert (`total_games_played`, etc.).

### 8.7 Logging

- [ ] **AC-TA-025:** Alle Fehler verwenden `push_error()`, keine `print()` für Fehler.
- [ ] **AC-TA-026:** Debug-Logs sind mit `[DEBUG]` prefixiert und nur im Debug-Build aktiv (`OS.is_debug_build()`).

### 8.8 Performance (Siehe auch technical-performance.md)

- [ ] **AC-TA-027:** Desktop: 60 FPS auf 1920×1080, Hardware: Intel i5 (8th Gen), 8GB RAM, Intel UHD 620.
- [ ] **AC-TA-028:** RAM-Nutzung: < 1.5 GB bei 8 Spielern auf dem Board.
- [ ] **AC-TA-029:** Minispiel-Ladezeit: < 2 Sekunden von Trigger bis Spielbar.

---

> **Nächste Datei:** `technical-multiplayer.md` — Multiplayer-Architektur  
> **Referenz:** `technical-fork-strategy.md` — Was bleibt, was wird neu  
> **Referenz:** `technical-data-structures.md` — Datenstrukturen  
> **Referenz:** `technical-performance.md` — Performance-Ziele
