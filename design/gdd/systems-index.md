# Systemzerlegung — Party Arena Game Bible

> **Teil:** 0 — Meta & Vision
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/technical-architecture.md, design/gdd/technical-multiplayer.md, design/gdd/core-loop.md, design/gdd/bible-index.md

---

## 1. Overview

Die Systemzerlegung ist die vollstandige technische Landkarte von Party Arena. Sie listet jedes einzelne Softwaresystem des Spiels mit seiner eindeutigen Zustandigkeit, seiner Godot-Node/Scene-Zuordnung, seinem Fork-Status relativ zur Super-Tux-Party-Codebasis und seinen Abhangigkeiten zu anderen Systemen auf. Dieser Index dient als:

- **Navigationsinstrument** fur Entwickler: Welches `.gd`/`.tscn`-Paar implementiert welche Spiellogik?
- **Abhangigkeitsanalyse:** Welches System muss fertig sein, bevor ein anderes integriert werden kann?
- **Fork-Tracker:** Welche Systeme wurden unverandert aus STP ubernommen, welche modifiziert, welche komplett neu geschrieben?
- **Scope-Dokumentation:** Welche Systeme existieren, welche werden neu gebaut, welche wurden aus STP entfernt?

Die Systemzerlegung folgt dem Prinzip **ein System = eine klar abgrenzbare Verantwortlichkeit**. Systeme durfen sich uberschneiden (z. B. braucht der Item-Shop sowohl das Item-System als auch die Coin-Economy), aber jedes System hat genau einen Besitzer (die Datei/das Modul, das die Kernlogik implementiert).

### Status-Emoji-Legende

| Emoji | Bedeutung | Beschreibung |
|---|---|---|
| ✅ | STP ubernommen | Die Datei wurde unverandert oder mit minimalen Static-Typing-Fixes aus Super Tux Party ubernommen. |
| 🔧 | STP modifiziert | Die Datei stammt aus STP, wurde aber substanziell verandert (neue Konstanten, 8P-Erweiterung, neue Logik). |
| 🆕 | Neu | Die Datei existiert in STP nicht und wurde von Grund auf fur Party Arena entwickelt. |
| ❌ | STP entfernt | Dieses System oder diese Datei existierte in STP, wurde aber fur Party Arena ersatzlos gestrichen. |

---

## 2. Player Fantasy

Fur die Entwickler erfullt die Systemzerlegung die Rolle eines **technischen Kompass**: Beim Offnen des Projekts weiss man in wenigen Minuten, wo jedes System wohnt, wofur es zustandig ist und mit wem es reden darf. Ein neuer Programmierer kann sich anhand der Abhangigkeitsliste von System zu System hangeln und versteht die Architektur, ohne den gesamten Code gelesen zu haben. Fur den Technical Director ist sie das **Kontrollinstrument**: Jede neue Codeanderung kann gegen die definierten Zustandigkeiten gepruft werden ("Gehort diese Logik wirklich in den PlayerController oder doch in den BoardController?"), und der Fork-Status zeigt auf einen Blick, welche Systeme STP-Erbe sind und daher bei Upstream-Anderungen besonders beobachtet werden mussen. Die Systemzerlegung erzeugt **mentale Ordnung**: Aus einem Meer von `.gd`-Dateien wird eine uberschaubare Anzahl benannter, verantwortlicher Systeme mit klaren Schnittstellen.

---

## 3. Detailed Rules

### System 1: Core Loop / Game Controller

- **Kurzbeschreibung:** Zentraler Spielfluss-Manager, der den gesamten Rundenablauf (Zug-Phasen, Minispiel-Trigger, Stern-Phase, Spielende) orchestriert.
- **Zustandigkeiten:**
  - Verwaltung der Spielphasen (`ROLL`, `MOVE`, `EVENT`, `SHOP`, `MINIGAME`, `STAR`, `BONUS_STARS`, `VICTORY`)
  - Zug-Reihenfolge der 8 Spieler (nach Vorrunden-Wurfelreihenfolge)
  - Ubergang zwischen den Phasen (inkl. Timeout-Handling: 30s Wurfel-Timeout, 15s Shop-Timeout, 10s Pfadwahl-Timeout)
  - Aufruf der Subsysteme zur richtigen Zeit (Dice-System bei ROLL, Event-System bei EVENT, Minigame-Queue bei MINIGAME, Star-Economy bei STAR, Victory-System bei VICTORY)
  - Durchsetzung der Nicht-Unterbrechbarkeit eines laufenden Zuges
  - Runden-Zahler-Fortschritt (Runde N von MAX_TURNS, Ubergang zu Bonus-Sternen nach letzter Runde)
  - Timeout-Management: Wenn ein Spieler nicht innerhalb des Timeouts handelt, wird automatisch gewurfelt/gepasst
- **Godot-Node/Scene-Zuordnung:** `common/scenes/board_logic/controller/controller.tscn` + `controller.gd`
- **Status:** 🔧 STP modifiziert (kompletter Rewrite: Cookie/Cake → Munzen/Sterne, 4P → 8P, neue Phasen-Struktur, Stern-Wanderung, Bonus-Sterne, Catch-Up-Mechanik, kein Nolok/GNU/Duel)
- **Abhangigkeiten:** Dice System, Board Controller, NodeBoard, Player Controller, Coin Economy, Star Economy, Event System, Minigame Queue, Item System, Victory System, Catch-Up System, ArenaStar System

### System 2: Board Controller

- **Kurzbeschreibung:** Verwaltet die Board-Logik auf Strukturebene: Feld-Verkettung, Pfadfindung, Feld-Effekt-Dispatching und Validierung von Bewegungen.
- **Zustandigkeiten:**
  - Laden des Board-Plugins (via Board-Loader) und Aufbau des 40-Felder-Graphen im Speicher
  - Bereitstellung der next/prev-Verbindungen fur jedes Feld
  - Validierung von Pfad-Wahlen an Abzweigungen (ist der gewahlte Branch-Index gultig?)
  - Dispatching des Feld-Effekts beim Betreten eines Feldes (ruft NodeBoard.execute_field_event oder delegiert an Shop/Event-System)
  - Stern-Wanderung zwischen den 2–3 Sternen-Shop-Positionen (nach jedem Kauf)
  - Berechnung der nachsten Sternen-Shop-Position (Regel: nie das aktuelle, bevorzugt unbesetzt)
  - Pfad-Wahl-UI-Bereitstellung (welche Branch-Optionen hat der Spieler an dieser Abzweigung?)
- **Godot-Node/Scene-Zuordnung:** `common/scenes/board_logic/controller/controller.tscn` + `controller.gd` (Teil des Controller-Moduls, Board-spezifische Methoden)
- **Status:** 🔧 STP modifiziert (STP-Boardlogik mit Nolok/GNU entfernt, neu: Stern-Wanderung, neues Feldtyp-Enum, 8P-Layout)
- **Abhangigkeiten:** Board Loader, NodeBoard, Player Controller, Star Economy, Field-Daten (FieldData-Strukturen)

### System 3: NodeBoard (Feldtypen und Feld-Daten)

- **Kurzbeschreibung:** Definiert und verwaltet alle Feldtypen des Boards — ihre visuelle Reprasentation, ihre Daten (Feldtyp, next/prev, coin_bonus, event_pool) und ihr Verhalten bei Betreten.
- **Zustandigkeiten:**
  - Definition des Feldtyp-Enums: `START`, `STAR_SHOP`, `ITEM_SHOP`, `EVENT`, `LUCK`, `COIN_BONUS`, `MINIGAME`
  - Speicherung und Bereitstellung von FieldData pro Feld (index, type, next_indices, prev_indices, coin_bonus_value, event_pool, is_branch_decision, visual_position, visual_rotation)
  - Visuelle Indikatoren pro Feldtyp (Stern-Icon fur STAR_SHOP, Einkaufstasche fur ITEM_SHOP, Blitz fur EVENT, Kleeblatt fur LUCK, Munzstapel fur COIN_BONUS, Spiel-Controller-Icon fur MINIGAME)
  - Feld-Effekt-Dispatching: Je nach Feldtyp wird die entsprechende Logik aufgerufen (Shop offnen, Event auslosen, Munzen gutschreiben, Minispiel anfordern)
  - Abzweigungslogik: Wenn `next_indices.size() > 1`, wird der Pfadwahl-Dialog angeboten
  - Validierung der next/prev-Konsistenz (A.next enthalt B → B.prev enthalt A, kein Feld zeigt auf sich selbst)
- **Godot-Node/Scene-Zuordnung:** `common/scenes/board_logic/node/node.tscn` + `node.gd`
- **Status:** 🔧 STP modifiziert (STP-Enum BLUE/RED/GREEN/YELLOW/SHOP/NOLOK/GNU → komplett neues Enum, neue visuelle Indikatoren, neues Event-Dispatching)
- **Abhangigkeiten:** Board Controller, FieldData (Datenstruktur), Event System, Coin Economy, Star Economy, Item System, UI System (Pfadwahl-UI)

### System 4: Player Controller

- **Kurzbeschreibung:** Verwaltet die Darstellung und Bewegung der Spielerfiguren auf dem Board, ihre Zustande (idle, walking, jumping, celebrating, sad) und ihre visuelle Positionierung.
- **Zustandigkeiten:**
  - Bewegung der Spielfigur entlang des Pfades (Feld-fur-Feld-Animation, 0,3 s pro Schritt, 0,12 s mit Beschleunigung)
  - 8-Spieler-Positionierung: Offsets fur uberlappende Figuren auf demselben Feld (Kreis-Pattern, Radius 0,5 Einheiten)
  - Animationen: idle, walk, jump, celebrate, sad, taunt (via Charakter-Plugin-AnimationTree)
  - Splitscreen-Layouts: 2P (horizontaler Split), 3P (oben gross + zwei unten), 4P (2×2-Grid), 5–8P (Shared Screen)
  - Spieler-Farb-Indikatoren (farbige Umrandung, Namensschild, aktiver-Spieler-Hervorhebung)
  - Charakter-Modell-Laden und -Instanziierung (via Character-Loader)
  - LOD-Management: LOD0 (5000 Tris, Nahaufnahme) und LOD1 (1500 Tris, entfernte Charaktere)
- **Godot-Node/Scene-Zuordnung:** `common/scenes/board_logic/player_board/player_board.tscn` + `player_board.gd`
- **Status:** 🔧 STP modifiziert (PLAYER_TRANSLATION von 4 auf 8 erweitert, neue Arenian-Charaktere statt Tux, neue Farben, Splitscreen fur 8P, LOD-System)
- **Abhangigkeiten:** Character System, Character Loader, Board Controller, NodeBoard, UI System (HUD), Camera System, Input System

### System 5: Dice System

- **Kurzbeschreibung:** Verwaltet den Wurfelvorgang — vom Spieler-Input uber die Server-seitige Zufallszahl bis zur Client-seitigen Animation.
- **Zustandigkeiten:**
  - Entgegennahme des Wurfel-Requests vom Client (`_rpc_request_roll`)
  - Server-seitige Validierung: Ist der Spieler an der Reihe? Ist die Phase ROLL? Hat der Spieler noch nicht gewurfelt?
  - Generierung der Zufallszahl (`randi_range(DICE_MIN, DICE_MAX)` → 1–6)
  - Anwendung von Item-Modifikationen: Glucks-Wurfel → garantierte 5, andere Modifikatoren
  - Senden des Wurfel-Ergebnisses an alle Clients (`_rpc_dice_result`)
  - Client-seitige Wurfel-Animation (2,5 s Dauer, uberspringbar)
  - Ubergang zur MOVE-Phase nach der Animation
- **Godot-Node/Scene-Zuordnung:** Logik in `controller.gd` (Methode `_phase_roll()`), Animation als Teil des UI-Systems
- **Status:** 🔧 STP modifiziert (neue Item-Modifikationen, Wurfel-Timeout 30s, kein Cookie-Bezug mehr)
- **Abhangigkeiten:** Core Loop / Game Controller, Item System (Item-Effekte auf Wurfel), UI System (Wurfel-Animation), Network System (RPCs)

### System 6: Star Economy

- **Kurzbeschreibung:** Die komplette Stern-Wirtschaft: Stern-Kauf am aktiven Sternen-Shop (20 Munzen), Wanderung der Sternen-Statue nach jedem Kauf, Bonus-Sterne am Spielende.
- **Zustandigkeiten:**
  - Kauf-Logik: Spieler muss auf aktivem Sternen-Shop-Feld stehen, `coins >= 20`, `star_available == true`
  - Kauf-Abwicklung: 20 Munzen abziehen, Stern zum Spieler addieren, ArenaStar-Animation
  - Sternen-Statuen-Wanderung: Nach jedem Kauf → neue Position wahlen (nie das aktuelle Feld, bevorzugt unbesetzt)
  - Sonderfall Statuen-Ziel besetzt: Wenn Statue auf Feld mit Spieler wandert → einmalige Kaufgelegenheit in nachster Stern-Phase
  - Kauf-Fenster-Logik: Maximal ein Kauf pro Spieler und Runde (Schutz vor Kettenkaufen)
  - Bonus-Sterne am Spielende: 3 Kategorien aus 10er-Pool per Gleichverteilung ziehen, Gewinner pro Kategorie berechnen, +1 Stern pro Kategorie
  - Bonus-Stern-Kategorien: Munz-Konig (meiste Munzen gesamt), Minispiel-Meister (meiste Minispiel-Siege), Ereignis-Held (meiste Events ausgelost), Viellaufer (meiste Felder gereist), Pechvogel (haufigster Munzverlust), Kampfer (lange auf letztem Platz), Gluckspilz (haufigste Wurfel-Hochstwerte), Kaufer (meiste Items gekauft), Sammler (meiste verschiedene Items besessen), Sternen-Jager (am haufigsten am Sternen-Shop gelandet ohne zu kaufen)
- **Godot-Node/Scene-Zuordnung:** Logik in `controller.gd` (Methoden `_phase_star()`, `_handle_star_migration()`), Bonus-Sterne in `common/scripts/bonus_star.gd`, Sternen-Statue in `arena_star.gd`
- **Status:** 🆕 Neu (existiert in STP nicht in dieser Form — STP hatte Cakes als Siegwahrung mit fixem Shop ohne Wanderung und ohne Bonus-Sterne)
- **Abhangigkeiten:** Core Loop / Game Controller, Board Controller, Coin Economy, ArenaStar System, UI System (Runden-Zusammenfassung), Player Controller

### System 7: Coin Economy

- **Kurzbeschreibung:** Die gesamte Munz-Wirtschaft: alle Quellen (Faucets), alle Senken (Sinks) und alle Transaktionen, inklusive Validierung und Clamping.
- **Zustandigkeiten:**
  - Munz-Faucets (Quellen): Startguthaben (START_COINS=10), COIN_BONUS-Felder (3/5/8 Munzen), LUCK-Felder (positive Ereignisse), Events (positive Ausgange), Minispiel-Belohnungen (1. Platz: 10, 2. Platz: 5, 3. Platz: 3), Munz-Magnet-Bonus (+2 pro Feld)
  - Munz-Sinks (Senken): Stern-Kauf (20 Munzen), Item-Kauf (3–8 Munzen pro Item), LUCK-Felder (negative Ereignisse), Events (negative Ausgange), Diebhandschuh (gestohlene Munzen)
  - Transaktions-Validierung: Jede Munz-Anderung wird vom Server validiert (kein Client kann Munzen direkt andern)
  - Clamping: `coins = clamp(coins + amount, 0, 99)` — Munzen nie negativ, nie uber 99
  - UI-Display: Maximal 999 im HUD darstellbar (auch wenn Hard-Cap 99 ist)
  - Munz-Animation: Bei Gewinn/Verlust fliegen Munzen visuell vom Feld zum HUD
- **Godot-Node/Scene-Zuordnung:** Logik verteilt auf `controller.gd` (Phasen-Logik), `node.gd` (Feld-Effekte), `global.gd` (Konstanten), `shop.gd` (Kauf-Logik)
- **Status:** 🔧 STP modifiziert (Cookie→Munzen, neue Werte: START_COINS=10 statt 5, MÜNZEN_FÜR_STERN=20 statt COOKIES_FOR_CAKE=30, neue Minispiel-Auszahlungen, Munz-Magnet-Effekt, Hard-Cap 99)
- **Abhangigkeiten:** Core Loop / Game Controller, NodeBoard, Item System, Star Economy, Event System, UI System (HUD-Munz-Anzeige), Network System (RPC-Validierung)

### System 8: Item System

- **Kurzbeschreibung:** Definition, Inventar-Verwaltung, Aktivierung und Effekt-Anwendung aller 5 Items des Spiels.
- **Zustandigkeiten:**
  - Item-Definition: 5 Items mit ID, Preis, Effekttyp, Dauer, use_phase, Icon (via Plugin-Manifest `item_definition.json`)
  - Inventar-Verwaltung: Maximal 3 Items pro Spieler (`MAX_ITEMS=3`), Array-Speicherung, Kauf/Entfernen/Prufen
  - Item-Aktivierung: Spieler wahlt Item aus Inventar, Server validiert (Item im Inventar? Phase erlaubt? kein Cooldown?), Effekt wird ausgefuhrt
  - Item-Effekte (5 Typen):
    - `fixed_dice` (Glucks-Wurfel): Garantiert Wurfelwert LUCKY_DICE_VALUE=5, einmalig, use_phase=ROLL
    - `teleport_star` (Teleporter): Teleportiert zum nachsten Sternen-Shop-Feld, einmalig, use_phase=ROLL
    - `passive_shield` (Schutzschild): Blockt nachsten negativen Event/Diebstahl, bis zur Auslosung, passiv
    - `coin_multiplier` (Munz-Magnet): +2 Munzen pro betretenem Feld, Dauer 3 Zuge, passiv
    - `steal` (Diebhandschuh): Stiehlt zufalliges Item von zufalligem Gegner, einmalig, use_phase=ROLL
  - Item-Entfernung nach Verwendung/Ablauf
  - Kein Item-Handel zwischen Spielern
- **Godot-Node/Scene-Zuordnung:** Item-Definitionen in `plugins/items/*/`, Item-Loader in `common/scripts/loader/item_loader.gd`, Item-Logik in `controller.gd`, Inventar-UI in `player_info.gd` und `shop.gd`
- **Status:** 🆕 Neu (STP hatte Items nur rudimentar; Party Arena definiert 5 vollig neue Items mit eigenstandigen Effekten)
- **Abhangigkeiten:** Item Loader, Core Loop / Game Controller, Player Controller (Inventar-Display), UI System (Item-Shop-UI, Inventar-Anzeige), Coin Economy (Kaufpreise), Network System (Item-Validierung)

### System 9: Item Shop

- **Kurzbeschreibung:** Shop-UI und Kauf-Logik fur Items: Sortiment-Anzeige, Preis-Auszeichnung, Kauf-Bestatigung, Inventar-Limit-Prufung.
- **Zustandigkeiten:**
  - Shop-Offnung: Wenn Spieler auf ITEM_SHOP-Feld landet, wird der Shop-Dialog geoffnet
  - Sortiment: 3 Items pro Shop (2 Shops auf dem Board = 6 Item-Slots im Angebot, Item-IDs aus `item_shop_offers` im BoardData)
  - Preis-Anzeige: Item-Preis (3–8 Munzen) + Icon + Kurzbeschreibung
  - Kauf-Validierung: `player.coins >= item.price` AND `player.items.size() < MAX_ITEMS` AND `player.position in item_shop_positions`
  - Kauf-Abwicklung: Munzen abziehen, Item ins Inventar, Shop schliessen, Bestatigungs-Animation
  - Inventar-voll-Handling: Wenn `items.size() >= 3` → alle Items ausgegraut, Hinweis "Inventar voll"
  - Shop-Timeout: 15 Sekunden ohne Aktion → Auto-Pass
- **Godot-Node/Scene-Zuordnung:** `common/scenes/board_logic/controller/shop.tscn` + `shop.gd`, `common/scenes/board_logic/controller/shop_item.tscn` + `shop_item.gd`
- **Status:** 🔧 STP modifiziert (STP hatte Cookie-Shop; neue Items, neue Preise, 3-Slot-Inventar-Limit, neues UI-Design)
- **Abhangigkeiten:** Item System, Item Loader, Coin Economy, Player Controller, UI System, Network System (RPCs)

### System 10: Star Shop

- **Kurzbeschreibung:** Stern-Kauf-UI und Darstellung der wandernden Sternen-Statue auf dem Board.
- **Zustandigkeiten:**
  - Sternen-Statue-Visualisierung: 3D-Modell der goldenen Sternen-Statue auf dem aktiven Sternen-Shop-Feld, schwebend, drehend, mit Partikel-Effekt
  - Kauf-Dialog: Wenn Spieler auf akivem STAR_SHOP-Feld landet → "Stern kaufen fur 20 Munzen?" (Ja/Nein)
  - Preis-Anzeige: Stern-Icon + "20" Munz-Icon
  - Kauf-Bestatigung: ArenaStar-Ubergabe-Animation, Stern fliegt zum Spieler-HUD, Statue verschwindet und taucht an neuer Position auf
  - Wanderungs-Animation: Statue schrumpft/verschwindet am alten Ort, taucht am neuen Ort auf (ca. 2 s)
  - Nicht-kaufbar-Indikator: Wenn `star_available == false` oder Spieler hat &lt;20 Munzen → Option ausgegraut
- **Godot-Node/Scene-Zuordnung:** Teil von `shop.tscn` / `shop.gd`, Statuen-Modell in `arena_star.tscn` / `arena_star.gd`, Kauf-Logik in `controller.gd`
- **Status:** 🆕 Neu (STP hatte keinen wandernden Sternen-Shop; Cakes wurden an fixer Position gekauft)
- **Abhangigkeiten:** Star Economy, ArenaStar System, Coin Economy, Board Controller, UI System, Player Controller

### System 11: Event System

- **Kurzbeschreibung:** Verwaltet den Event-Pool pro Board, zieht Events beim Betreten von EVENT-Feldern, fuhrt sie aus und sendet Ergebnisse.
- **Zustandigkeiten:**
  - Event-Pool pro Board: Jedes EVENT-Feld hat einen eigenen `event_pool` (Array von Event-IDs)
  - Event-Auswahl: Per Gleichverteilung aus dem Pool, Regel "kein Event 2× hintereinander" (Event-History-Tracking)
  - Event-Kategorien: Positive Events (Munz-Regen, Item-Geschenk, Stern-Rabatt, Extra-Wurf), Negative Events (Munz-Verlust, Ruckwarts-Teleport, Item-Verlust, Uberspringen), Neutrale Events (Feld-Tausch, Farb-Wechsel, Nichts passiert)
  - Catch-Up-Skalierung: Events skalieren ihre Effekte basierend auf der Position des Spielers in der Rangliste (Verlierer bekommen grosszugigere Events)
  - Event-Ausfuhrung: Sofortige Anwendung des Effekts auf den Spieler (Munzen addieren/subtrahieren, Items geben/nehmen, Teleport)
  - Event-Moderation: ArenaStar kommentiert das Event (positiv: Jubel, negativ: Trost)
  - Event-History: Liste der vergangenen Events im `BoardData.event_history` fur die "kein 2× hintereinander"-Regel und fur Statistik-Tracking
- **Godot-Node/Scene-Zuordnung:** `common/scripts/event_system.gd` (neu), aufgerufen von `node.gd` und `controller.gd`
- **Status:** 🆕 Neu (STP hatte Nolok/GNU-Events mit festen Charakteren; Party Arena hat generisches Event-System mit thematisch passenden Effekten)
- **Abhangigkeiten:** Core Loop / Game Controller, NodeBoard, Coin Economy, Item System, Player Controller, ArenaStar System, Catch-Up System

### System 12: Minigame System

- **Kurzbeschreibung:** Plugin-basiertes Minispiel-Framework: Laden, Countdown, Input-Management, Scoring und Ergebnisubermittlung.
- **Zustandigkeiten:**
  - Minispiel-Plugins: 12 Minispiele in `plugins/minigames/*/`, jedes mit `minigame.tscn`, `minigame.gd`, `minigame.json`
  - Lade-Mechanismus: Alle Minigame-PCKs werden beim Spielstart in den RAM-Cache geladen (Preloading), Szene wird bei Trigger aus Cache instanziiert
  - Countdown: 3-2-1-GO-Animation vor Minispiel-Start (aus `common/scenes/countdown/`)
  - Input-Verarbeitung wahrend Minispiel: Client sendet Input-Stream (unreliable RPCs, alle 33ms), Server verarbeitet und sendet Sync-Updates (alle 50ms)
  - Scoring: Jedes Minispiel definiert eigene Score-Logik; Server normalisiert Scores fur Ranking
  - Ergebnis-Ermittlung: Sortierung nach Score (descending/ascending je nach Minispiel-Typ), Platzierung 1–8
  - Belohnungs-Berechnung: Platzierung → Munzen (1. Platz: 10, 2. Platz: 5, 3. Platz: 3, Rest: 0), Catch-Up-Bonus addition
  - Minispiel-Dauer: Standard 30 s (konfigurierbar pro Minispiel in minigame.json, 15–120 s)
- **Godot-Node/Scene-Zuordnung:** Minispiel-Logik in `server/minigame_queue.gd` und `server/game.gd`, Minispiel-Plugins in `plugins/minigames/*/`, Minispiel-Loader in `common/scripts/loader/minigame_loader.gd`, Countdown in `common/scenes/countdown/`
- **Status:** 🔧 STP modifiziert (STP-Minispiele entfernt, durch 12 neue ersetzt, neue Kategorien, 8P-Unterstutzung)
- **Abhangigkeiten:** Minigame Queue, Minigame Loader, Plugin Loader, Core Loop / Game Controller, Network System, UI System (Reward-Screen), Coin Economy, Input System

### System 13: Minigame Queue

- **Kurzbeschreibung:** Zentrale Minispiel-Auswahl-Logik: Verhindert Wiederholungen, gewichtet Kategorien, stellt sicher dass das ausgewahlte Minispiel die aktuelle Spielerzahl unterstutzt.
- **Zustandigkeiten:**
  - Minispiel-Pool: Alle 12 Minispiele, gefiltert nach Spielerzahl (min_players/max_players)
  - Wiederholungs-Verhinderung: Kein Minispiel wird 2× im selben Spiel gespielt (Tracking via `minigame_history`)
  - Kategorie-Gewichtung: Minispiele werden nicht rein zufallig gezogen, sondern gewichtet nach Kategorie (Geschicklichkeit, Reaktion, Puzzle/Logik, Rechnen/Wort, Kooperation), um Abwechslung zu garantieren
  - Turn-Tracker: Nach 3 Runden ohne Minispiel (weil niemand auf MINIGAME-Feld gelandet ist) → Minispiel wird in der nachsten Runde forciert (`minigame_turn_tracker >= 3`)
  - Auswahl-Algorithmus: Filtere Pool → entferne bereits gespielte → gewichte nach Kategorie → ziehe 1 per Gleichverteilung aus verbleibenden
  - Fallback: Wenn kein Minispiel mehr verfugbar (alle 12 bereits gespielt, extrem unwahrscheinlich bei 8–10 Runden) → Minispiel wird ubersprungen
- **Godot-Node/Scene-Zuordnung:** `server/minigame_queue.gd`
- **Status:** 🔧 STP modifiziert (STP hatte Minigame-Queue; fur 8P und neue Minispiele/Kategorien angepasst)
- **Abhangigkeiten:** Minigame System, Minigame Loader, Core Loop / Game Controller

### System 14: Character System

- **Kurzbeschreibung:** Charakter-Definition, Plugin-Ladeprozess, Animationsvertrag und Auswahl-Logik fur die 8 Arenians.
- **Zustandigkeiten:**
  - Charakter-Definition: 8 Arenians (Brix, Nixie, Koko, Pip, Zara, Flint, Luna, Momo — oder die in characters-overview.md definierten), jeder als Plugin in `plugins/characters/*/`
  - Charakter-Manifest: `character.json` mit ID, display_name, description, catchphrase, model_path, portrait_path, icon_path, voice_pack, stats (kosmetisch), animations
  - Plugin-Ladung: Character-Loader entdeckt alle Charakter-Plugins, parst Manifeste, stellt API bereit
  - Spielmechanische Gleichheit: Alle 8 Charaktere sind spielmechanisch vollstandig identisch (gleiche Trefferbox, gleiche Geschwindigkeit, gleiche Physik) — Unterschiede nur visuell/akustisch
  - Animationsvertrag: Jeder Charakter MUSS 6 Animationen bereitstellen: idle, walk, jump, celebrate, sad, taunt
  - Charakter-Auswahl: First-Come-First-Served in der Lobby, keine zwei Spieler mit demselben Arenian
  - Signaturfarben: Jeder Charakter hat eine dominante Farbe (Orange, Turkis, Rosa, Gelb, Lila, Blau, Grun, Pink)
- **Godot-Node/Scene-Zuordnung:** Charakter-Plugins in `plugins/characters/*/`, Loader in `common/scripts/loader/character_loader.gd`, Basisklasse in `common/scripts/character.gd`, Auswahl-UI in `client/menus/characters/character_select.tscn`
- **Status:** 🆕 Neu (STP-Charaktere Tux/KDE-Charaktere komplett entfernt, durch 8 neue Eigen-IP-Arenians ersetzt)
- **Abhangigkeiten:** Character Loader, Plugin Loader, Player Controller, Lobby System, UI System (Charakter-Auswahl, HUD-Portrats)

### System 15: Lobby System

- **Kurzbeschreibung:** Spieler-Beitritt, Charakter- und Board-Wahl, Ready-Status und Spielstart-Management vor einer Partie.
- **Zustandigkeiten:**
  - Lobby-Phasen: WAITING → CHARACTER_SELECT → BOARD_SELECT → READY → STARTING
  - Spieler-Beitritt: Bis zu 8 Spieler (LOBBY_SIZE=8), 9. wird abgewiesen ("Lobby voll")
  - Spieler-Daten: Name (max 16 Zeichen), Charakter-Wahl (First-Come-First-Served), Ready-Status
  - Charakter-Auswahl: Jeder Spieler wahlt einen von 8 Arenians; bei Konflikt (zwei wahlen denselben) gewinnt der erste RPC
  - Board-Auswahl: Host wahlt aus 8 Inseln; andere Spieler sehen Auswahl
  - Ready-Status: Jeder Spieler bestatigt Bereitschaft; Host sieht alle Status
  - Start-Bedingungen: Minimum 2 Spieler, Host druckt "Start"
  - Countdown: 5 Sekunden Countdown vor Spielstart (LOBBY_COUNTDOWN)
  - Online-Lobby: Server-Browser (lokales Netzwerk via UDP-Broadcast, direkte IP), Server-Info (Name, Spielerzahl, Board)
  - Disconnect in Lobby: Spieler wird aus Lobby entfernt, sein Charakter wird wieder frei
- **Godot-Node/Scene-Zuordnung:** Server-seitig: `server/lobby.tscn` + `server/lobby.gd`, Client-seitig: `client/lobby.tscn` + `client/lobby.gd`, Geteilte Basis: `common/lobby.gd`
- **Status:** 🔧 STP modifiziert (LOBBY_SIZE 4→8, neue Charaktere, neue Insel-Auswahl, neue Lobby-UI)
- **Abhangigkeiten:** Character System, Board Controller, Network System, UI System (Lobby-UI, Charakter-Auswahl, Board-Auswahl)

### System 16: Network System

- **Kurzbeschreibung:** Server/Client-Kommunikation via ENet, RPC-Infrastruktur, State-Synchronisation und Verbindungsmanagement.
- **Zustandigkeiten:**
  - Transport: ENet via `ENetMultiplayerPeer`, UDP, Port 10567, max 8 Clients, 3 Kanale (State, Input, Chat)
  - Server-Modus: Dedicated Server oder Host+Client (ein Spieler ist Server und Client zugleich)
  - Lokaler Multiplayer: `create_local_server()` — alle Clients im selben Prozess, kein Netzwerk-Overhead
  - RPC-System: `@rpc("authority")` fur Server→Client, `@rpc("any_peer")` fur Client→Server (mit Validierung), `@rpc("any_peer", "call_local")` fur Chat
  - RPC-Namenskonvention: `_rpc_<aktion>` (z.B. `_rpc_roll_dice`, `_rpc_buy_star`)
  - Server-Autoritat: Server ist einzige Quelle der Wahrheit, validiert jede Client-Aktion
  - State-Synchronisation: `_rpc_sync_game_state` sendet ServerUpdate-Dictionary an alle Clients
  - Verbindungsmanagement: `peer_connected`/`peer_disconnected` Signale, Heartbeat, Timeout-Erkennung
  - Disconnect-Handling: Client-Disconnect → KI ubernimmt, Server-Disconnect → alle Clients kehren zum Hauptmenu zuruck
  - Rate Limiting: Max 10 RPCs pro Sekunde pro Client
  - Cheat-Schutz: Jede Aktion wird server-seitig validiert (Munzen, Position, Items, Phase)
- **Godot-Node/Scene-Zuordnung:** `server/game.gd`, `client/game.gd`, `common/scripts/global.gd` (create_local_server, join_local_game)
- **Status:** 🔧 STP modifiziert (STP-ENet-Basis ubernommen, fur 8P erweitert, neue RPCs fur neue Systeme, angepasste Timeouts)
- **Abhangigkeiten:** Core Loop / Game Controller, Lobby System, Minigame System, alle Systeme die RPCs nutzen

### System 17: UI System

- **Kurzbeschreibung:** Samtliche Benutzeroberflachen: HUD im Spiel, Menus (Hauptmenu, Pause, Optionen, Sieg), Overlays (Shop, Belohnungen) und Screen-Fluss.
- **Zustandigkeiten:**
  - HUD im Board-Spiel: Spieler-Leiste (8 Spieler: Munzen, Sterne, Items, aktiver-Spieler-Markierung), Wurfel-Anzeige, Runden-Anzeige, Phasen-Indikator
  - Hauptmenu: Buttons fur "Lokales Spiel", "Online-Spiel", "Einstellungen", "Credits", "Beenden"
  - Pause-Menu: "Fortsetzen", "Einstellungen", "Spiel verlassen"
  - Optionen-Menu: Audio (Master, Musik, SFX, Stimme), Video (Auflosung, Vollbild, VSync, AA, Render-Skalierung), Sprache, Accessibility (Untertitel, Farbenblind-Modus, reduzierte Bewegung, hoher Kontrast), Steuerung
  - Shop-Overlay: Stern-Shop und Item-Shop mit Preisen, Icons, Kauf-Bestatigung
  - Belohnungs-Bildschirm: Minispiel-Ergebnisse (Platzierungen, Munz-Belohnungen, Catch-Up-Bonus), Runden-Zusammenfassung
  - Sieg-Bildschirm: Finale Rangliste 1–8, Bonus-Sterne-Detail, Siegerpose des Gewinners, Statistik-Ubersicht
  - Screen-Fluss: Hauptmenu → Lobby → Charakter-Auswahl → Board-Auswahl → Spiel → Sieg-Bildschirm → Hauptmenu
  - UI-Design-Tokens: Einheitliche Farbpalette, Typografie (1–2 Schriftarten), Abstande, Icon-Grossen
  - Controller- und Maus-Navigation: Alle UI-Elemente sind mit Gamepad UND Maus bedienbar
- **Godot-Node/Scene-Zuordnung:** `client/menus/main_menu.tscn`, `client/menus/pause_menu.tscn`, `client/menus/options_menu.tscn`, `client/menus/victory_screen/`, `client/rewardscreens/ffa/`, `common/scenes/board_logic/controller/player_info.tscn`, `common/scenes/board_logic/controller/shop.tscn`
- **Status:** 🔧 STP modifiziert (STP-Menus als Basis, komplett neues Design, Cartoon-Stil, 8P-Erweiterung, neue Menus: Charakter-/Board-Auswahl)
- **Abhangigkeiten:** Alle Systeme die UI benotigen (Core Loop, Player Controller, Star Economy, Coin Economy, Item System, etc.), Accessibility System, Localization System, Input System

### System 18: Audio System

- **Kurzbeschreibung:** Musik, Soundeffekte (SFX) und Sprachausgabe — Verwaltung der Audio-Assets, Bus-Struktur, Ducking und Lautstarke-Regelung.
- **Zustandigkeiten:**
  - Audio-Bus-Struktur: Master (0 dB) → Musik (-6 dB, Sidechain-Ducking), SFX (-3 dB), Stimme (-3 dB)
  - Musik: Insel-Themen (1 Track pro Board = 8 Tracks), Menu-Musik (2–3 Tracks), Minispiel-Musik (4–6 Tracks, geteilt), dynamische Ubergange (Crossfade 500ms)
  - SFX: UI-Sounds (Hover, Click, Back), Board-Sounds (Wurfeln, Bewegung Schritte, Munzen-Sammeln, Stern-Kauf), Item-Sounds (pro Item), Minispiel-Sounds (pro Minispiel)
  - Stimme: ArenaStar-Moderation (Regelerklarungen, Sieg/Niederlagen-Spruche), Arenian-Voice-Lines (kurze Ausrufe bei Jubel, Trauer, Item-Nutzung), Umfang ca. 50–80 Voice-Lines
  - Ducking: Musik wird um 6 dB abgesenkt, wenn SFX abgespielt werden
  - Lautstarke-Regler: Master (0–100%), Musik (0–100%), SFX (0–100%), Stimme (0–100%) — im Options-Menu einstellbar
  - Audio-Formate: OGG Vorbis (.ogg), Musik: 128 kbps Stereo, SFX: 64–96 kbps Mono, Stimme: 96 kbps Mono
  - Audio-Pooling: Haufig verwendete SFX werden im Speicher gehalten (nicht jedes Mal von Disk geladen)
- **Godot-Node/Scene-Zuordnung:** Godot AudioServer (integriert), Bus-Struktur in `default_env.tres`/`project.godot`, Audio-Manager-Skript (falls vorhanden in STP: `common/scripts/audio_manager.gd`)
- **Status:** 🔧 STP modifiziert (STP-Audio-Basis ubernommen, neue Audio-Assets, neue Bus-Namen, neue ArenaStar-Voice)
- **Abhangigkeiten:** UI System (UI-Sounds), Core Loop (Phasen-Sounds), ArenaStar System (Voice), Character System (Charakter-Sounds)

### System 19: Input System

- **Kurzbeschreibung:** Verwaltung von bis zu 8 gleichzeitigen Spieler-Eingaben uber Tastatur (P1, P2) und Gamepads (P1–P8), inklusive Input-Mapping und Gamepad-Konflikt-Erkennung.
- **Zustandigkeiten:**
  - InputMap: 10 Actions pro Spieler (move_left, move_right, move_up, move_down, confirm, cancel, use_item, taunt, accelerate, skip) × 8 Spieler = 80 Input-Eintrage in `project.godot`
  - Tastatur-Zuweisung: P1 = WASD + Enter/Space, P2 = IJKL + Right Shift, P3–P8 = keine Tastatur (nur Gamepad)
  - Gamepad-Zuweisung: P1–P8 = Gamepad 0–7
  - Gamepad-Konflikt-Erkennung: Zwei physische Gamepads mit gleicher Device-ID werden erkannt, zweiter Spieler wird mit Warnung abgewiesen
  - Input-Polling: Gameplay-Input wird im `_process()`-Loop gepollt (nicht `_input()` Events) — verhindert Input-Stau bei 8 gleichzeitigen Eingaben
  - UI-Navigation: `_input()` Events fur UI (unproblematisch, da nur ein Spieler gleichzeitig UI navigiert)
  - Minispiel-Input: Spezifische Input-Typen pro Minispiel (left_stick, right_stick, motion, button, touch), definiert in `minigame.json`
  - Remapping: Spieler konnen Tasten im Options-Menu neu belegen (pro Spieler gespeichert in `data.cfg`)
  - Deadzone: 0.2 fur analoge Sticks (Gamepad)
- **Godot-Node/Scene-Zuordnung:** `project.godot` (InputMap), `common/scripts/control_helper.gd` (UI-Input-Helfer), `common/scripts/global.gd` (Input-Polling)
- **Status:** 🔧 STP modifiziert (STP-InputMap hatte nur 4 Spieler; auf 8 erweitert, neue Actions hinzugefugt)
- **Abhangigkeiten:** Player Controller, UI System, Minigame System, Accessibility System (Remapping)

### System 20: Save System

- **Kurzbeschreibung:** Persistente Speicherung von Statistiken, Einstellungen, Freischaltungen und Spielstanden im `user://`-Verzeichnis.
- **Zustandigkeiten:**
  - Speicherort: `user://data.cfg` (Einstellungen + Statistiken), `user://savegames/save_<timestamp>.sav` (Spielstande)
  - Format: Godot ConfigFile (.cfg) fur beide Dateitypen
  - Einstellungen: Audio (Master, Musik, SFX, Stimme), Video (Auflosung, Vollbild, VSync, AA, Render-Skalierung), Sprache, Accessibility, Steuerung (Keybindings)
  - Statistiken: total_games_played, total_wins, total_coins_collected, total_stars_bought, total_minigames_played, total_minigames_won, favorite_character, favorite_island, total_playtime_seconds, etc.
  - Freischaltungen: unlocked_characters (Array von Charakter-IDs), unlocked_islands (Array von Insel-IDs)
  - Spielstand: Kompletter Game-State (PlayerData, BoardData, current_turn, round_phase, minigame_history) zur Fortsetzung
  - Speicher-Zeitpunkt: Statistiken nach jedem Spiel automatisch, Einstellungen bei Anderung sofort, Spielstand nur manuell (Pause-Menu)
  - Versionierung: Spielstand enthalt `version`-Feld; Laden aus inkompatibler Version zeigt Warnung/Konvertierung
  - Kein Client-seitiges Speichern wahrend des Spiels (nur Server speichert)
- **Godot-Node/Scene-Zuordnung:** `common/savegames/savegames.gd`
- **Status:** ✅ STP ubernommen (STP-Savegame-System als Basis; nur neue Keys/Werte fur PA)
- **Abhangigkeiten:** Core Loop / Game Controller (Spielstand-Daten), UI System (Options-Menu, Pause-Menu), Lobby System (Freischaltungen)

### System 21: Victory System

- **Kurzbeschreibung:** Berechnung der Endplatzierungen, Tie-Breaker-Logik, Sieger-Zeremonie und Statistik-Zusammenfassung nach der letzten Runde.
- **Zustandigkeiten:**
  - Ranglisten-Berechnung: 1. Kriterium = Sterne (absteigend), 2. Kriterium = Munzen (absteigend), 3. Kriterium = Minispiel-Siege (absteigend)
  - Bonus-Sterne-Anwendung: Die 3 gezogenen Bonus-Sterne werden auf die Spieler-Sterne addiert, Reranking danach
  - Tie-Breaker-Darstellung: Bei exaktem Gleichstand (selbe Sterne + selbe Munzen + selbe Minispiel-Siege) → geteilter Platz (z.B. zwei 3. Platze, dann nachster ist 5.)
  - Sieger-Zeremonie: Gewinner-Charakter in Siegerpose, ArenaStar uberreicht Trophae, Konfetti-Partikel, alle Platzierungen werden animiert eingeblendet
  - Statistik-Ubersicht: Pro Spieler: Sterne gesamt, Bonus-Sterne, Munzen gesamt, Minispiele gewonnen, Items verwendet, Events ausgelost, Felder gereist
  - Weiterleitung: Nach der Zeremonie → Hauptmenu (oder "Erneut spielen" mit denselben Einstellungen)
- **Godot-Node/Scene-Zuordnung:** `client/menus/victory_screen/victory_screen.tscn` + `victory_screen.gd`, Berechnungslogik in `controller.gd` (Methoden `_calculate_final_rankings()`, `_apply_bonus_stars()`)
- **Status:** 🔧 STP modifiziert (STP-Sieg-Logik hatte kein Bonus-Stern-System, kein 8P-Ranking, keine Tie-Breaker-Kette; alles neu)
- **Abhangigkeiten:** Star Economy (Bonus-Sterne), Player Controller (Charakter-Daten), UI System (Sieg-Bildschirm), Save System (Statistiken aktualisieren), Core Loop / Game Controller

### System 22: Catch-Up System

- **Kurzbeschreibung:** Fairness-Mechanismen die verhindern, dass schwachere Spieler komplett abgehangt werden: Verlierer-Boost, Event-Skalierung und Bonus-Stern-Kategorien.
- **Zustandigkeiten:**
  - Verlierer-Boost (Minispiele): Letzter Platz in einem Minispiel erhalt +3 zusatzliche Munzen, Vorletzter +1 Munze (nur bei 5+ Spielern; bei 2–4 Spielern: letzter +2)
  - Event-Skalierung: Events skalieren positive Effekte fur niedrig platzierte Spieler (z.B. Munz-Regen gibt +10 fur Rang 8, +5 fur Rang 4, +2 fur Rang 1)
  - Bonus-Stern-Kategorien: 3 von 10 Kategorien begunstigen haufig die schwacheren Spieler (Pechvogel, Kampfer, Sternen-Jager)
  - Aktivierungsschwelle: Catch-Up-Mechanismen sind immer aktiv (kein Ein-/Ausschalten)
  - Transparenz: Catch-Up-Effekte werden im UI visuell markiert ("Catch-Up Bonus: +3 Munzen")
  - Deckelung: Kein Catch-Up-Effekt kann einen Spieler auf Platz 1 katapultieren (maximaler Boost: +1 Stern-Aquivalent)
- **Godot-Node/Scene-Zuordnung:** Logik in `controller.gd` (Methode `_catch_up_reward()`), Event-Skalierung in `event_system.gd`
- **Status:** 🆕 Neu (STP hatte minimale Catch-Up-Mechanismen; Party Arena hat ein ausformuliertes System mit mehreren Ebenen)
- **Abhangigkeiten:** Core Loop / Game Controller, Event System, Minigame System, Coin Economy, Star Economy

### System 23: Camera System

- **Kurzbeschreibung:** Board-Kamera (Top-Down-Perspektive mit dynamischem Follow), Split-Screen-Kameras (bis zu 4 Viewports) und Minispiel-Kameras.
- **Zustandigkeiten:**
  - Board-Kamera (Single-Player / Shared Screen): Leicht erhohter Winkel (~60°), folgt dem aktiven Spieler mit weichem Tween (Lerp 0.1), Zoom je nach Board-Layout
  - Split-Screen (2–4 Spieler): Mehrere Kameras/Viewports, jeder folgt seinem Spieler, reduzierte Sichtweite (camera.far = 50.0)
  - Split-Layouts: 2P horizontal (je 960×1080), 3P (oben 1920×720 + unten zwei je 960×360), 4P 2×2 Grid (je 960×540)
  - Shared Screen (5–8 Spieler): Eine Kamera, folgt dem aktiven Spieler, alle Figuren sichtbar
  - Minispiel-Kamera: Wird vom Minispiel selbst definiert (jedes Minispiel hat eigene Kamera-Logik in `minigame.tscn`)
  - Kamera-Ubergange: Weicher Blend (0.5 s) beim Wechsel zwischen Board und Minispiel
  - Kameragrenzen: Kamera bleibt innerhalb der Board-Grenzen (Clamp an Board-Randern)
- **Godot-Node/Scene-Zuordnung:** Kamera-Setup in `client/game.gd` und `player_board.gd`
- **Status:** 🔧 STP modifiziert (STP-Kamera fur 4P; erweitert auf 8P mit Shared-Screen-Modus, neue Split-Layouts)
- **Abhangigkeiten:** Player Controller, UI System, Board Controller

### System 24: Plugin Loader

- **Kurzbeschreibung:** Generisches Plugin-System (.pck/.zip): Discovery, Laden und API fur Boards, Charaktere, Items und Minispiele.
- **Zustandigkeiten:**
  - Plugin-Discovery: Scannt `plugins/boards/*/`, `plugins/characters/*/`, `plugins/items/*/`, `plugins/minigames/*/` nach `plugin.json`-Manifesten
  - Plugin-Validierung: Pruft ob `plugin.json` existiert und alle Pflichtfelder enthalt; bei fehlendem/falschem Manifest → Plugin wird ubersprungen, Fehler-Log
  - Plugin-Ladung: Ladt `.pck` oder `.zip`-Datei, extrahiert Assets, stellt Szene/Resource bereit
  - Plugin-API: Abstrakte Basisklasse mit Standard-Methoden (load, unload, get_metadata, validate)
  - Plugin-Cache: Geladene Plugins werden im Speicher gehalten (kein wiederholtes Laden von Disk)
  - Plugin-Isolation: Plugins durfen NICHT auf Core-Code zugreifen (ausser explizit erlaubte APIs), keine `res://common/` Imports
  - Fehlertoleranz: Fehlerhaftes Plugin lasst das Spiel nicht absturzen; es wird deaktiviert und im Menu ausgegraut
- **Godot-Node/Scene-Zuordnung:** `common/scripts/loader/plugin_system.gd` (Basisklasse), `board_loader.gd`, `character_loader.gd`, `item_loader.gd`, `minigame_loader.gd`
- **Status:** ✅ STP ubernommen (STP-Plugin-System als Basis-Framework unverandert; die Loader selbst sind modifiziert)
- **Abhangigkeiten:** Alle Loader (Board, Character, Item, Minigame), alle Systeme die Plugins konsumieren

### System 25: ArenaStar System

- **Kurzbeschreibung:** Das Maskottchen und der Moderator: 3D-Modell auf dem Board, Animationen, Kommentare zu Spielereignissen, Tutorial-Hinweise und Belohnungs-Inszenierung.
- **Zustandigkeiten:**
  - ArenaStar-Prasenz: Schwebendes 3D-Modell uber dem aktiven Sternen-Shop-Feld (immer sichtbar, drehend, glitzernd)
  - Moderation: Kommentiert wichtige Spielmomente mit kurzen Text-/Voice-Lines: Runden-Beginn, Wurfel-Ergebnis, Stern-Kauf, Minispiel-Ankundigung, Event-Auslosung, Bonus-Stern-Vergabe, Siegerehrung
  - Tutorial-Hinweise: In den ersten 2 Runden gibt ArenaStar zusatzliche Kontext-Hinweise ("Du bist dran! Drucke A zum Wurfeln", "Du hast 20 Munzen — du kannst einen Stern kaufen!")
  - Belohnungs-Inszenierung: ArenaStar uberreicht Sterne, Munzen und Items mit charakteristischen Animationen
  - Emotionen: ArenaStar hat Zustande (happy, excited, sympathetic, dramatic) mit entsprechenden Animationen und Voice-Lines
  - Nicht-blockierend: ArenaStar-Kommentare laufen parallel zur nachsten Eingabemoglichkeit; maximale Blockierzeit: 3 Sekunden
  - Arena-Variante: ArenaStar kann als spielbarer Charakter in speziellen "Arena-Varianten" von Minispielen auftreten (optional, Post-Launch)
- **Godot-Node/Scene-Zuordnung:** `common/scenes/board_logic/controller/arena_star.tscn` + `arena_star.gd`
- **Status:** 🆕 Neu (STP hatte "Sara" als Moderatorin; komplett neuer Charakter, neue Animationen, neue Voice)
- **Abhangigkeiten:** Core Loop / Game Controller, Star Economy, Event System, Minigame System, Audio System, UI System

### System 26: Accessibility System

- **Kurzbeschreibung:** Barrierefreiheit-Features: Farbenblind-Modi, Text-Skalierung, Steuerungs-Remapping, reduzierte Bewegung, Untertitel, hoher Kontrast, Mono-Audio.
- **Zustandigkeiten:**
  - Farbenblind-Modi: Drei Modi (Protanopie, Deuteranopie, Tritanopie), angewendet als Post-Processing-LUT oder durch zusatzliche Symbol-Indikatoren auf Feldtypen
  - Text-Skalierung: UI-Textgrosse in 3 Stufen (Normal, Gross, Sehr Gross), betrifft alle UI-Texte (HUD, Menus, Dialoge)
  - Steuerungs-Remapping: Jeder Spieler kann seine Tasten im Options-Menu neu belegen (Ausnahme: P1/P2 Tastatur-Defaults bleiben als Fallback)
  - Reduzierte Bewegung: Deaktiviert/verkurzt Animationen (kein Screen-Shake, reduzierte Partikel, schnellere Ubergange), fur Spieler mit Motion Sickness
  - Untertitel: Alle Voice-Lines (ArenaStar, Arenians) werden als Untertitel eingeblendet (konfigurierbar: Aus, Kurz, Voll)
  - Hoher Kontrast: UI-Modus mit starkeren Farbkontrasten und dickeren Umrandungen (ersetzt das Standard-UI-Theme)
  - Mono-Audio: Alle Audio-Ausgabe auf einen Kanal (fur Spieler mit einseitiger Horfahigkeit)
  - Alle Einstellungen persistent in `data.cfg` gespeichert
- **Godot-Node/Scene-Zuordnung:** `client/menus/options_menu.gd` (Einstellungen-UI), Logik verteilt auf UI-Komponenten und Shader
- **Status:** 🆕 Neu (STP hatte minimale Accessibility; Party Arena baut ein vollstandiges System auf)
- **Abhangigkeiten:** UI System, Audio System, Input System, Camera System, Save System

### System 27: Localization System

- **Kurzbeschreibung:** Ubersetzungen und Sprachwechsel fur alle UI-Texte, Dialoge, Item-Beschreibungen und Minispiel-Anleitungen.
- **Zustandigkeiten:**
  - Sprachen: Deutsch (Primarsprache), Englisch, Franzosisch, Spanisch, Japanisch, Chinesisch (vereinfacht)
  - Ubersetzungsdateien: `.po`-Format (GNU gettext), eine Datei pro Sprache in `translations/`
  - Ubersetzungsumfang: Alle UI-Texte, Item-Beschreibungen, Minispiel-Anleitungen, Event-Texte, ArenaStar-Dialoge, Charakter-Beschreibungen, Sieges-Texte, Fehlermeldungen
  - Sprachwechsel: Zur Laufzeit via Options-Menu (sofortige Aktualisierung aller UI-Texte ohne Neustart)
  - Fallback: Deutsch als Default-Sprache; fehlende Ubersetzungen zeigen deutschen Text
  - Plural-Unterstutzung: Korrekte Pluralformen pro Sprache (Gottes ngettext)
  - Schriftart-Unterstutzung: UI-Fonts mussen alle Zielsprachen abdecken (inkl. CJK fur Japanisch/Chinesisch, Sonderzeichen fur Franzosisch/Spanisch)
  - Voice-Lokalisierung: ArenaStar-Voice wird pro Sprache separat aufgenommen (nicht maschinell ubersetzt)
- **Godot-Node/Scene-Zuordnung:** `translations/*.po`, Godot's integriertes `TranslationServer`-Singleton
- **Status:** 🆕 Neu (STP hatte nur Englisch; Party Arena baut ein vollstandiges Lokalisierungs-System mit 6 Sprachen auf)
- **Abhangigkeiten:** UI System, Audio System (Voice-Lokalisierung), Save System (Sprach-Einstellung), Alle Systeme mit Textausgabe

---

## 4. Formulas

### 4.1 System-Interaktionsmatrix

Die Abhangigkeiten zwischen Systemen lassen sich als gerichteter Graph darstellen. Die Formel beschreibt die Komplexitat der Integration:

`I(S) = d_ein(S) + d_aus(S)`

wobei:
- `d_ein(S)` = Anzahl der Systeme, von denen System S abhangt (eingehende Kanten)
- `d_aus(S)` = Anzahl der Systeme, die von System S abhangen (ausgehende Kanten)

Beispiele:
- Core Loop / Game Controller: `d_ein = 11` (Dice, Board, NodeBoard, Player, CoinEcon, StarEcon, Event, MinigameQ, Item, Victory, CatchUp), `d_aus = 12` (umgekehrt) → `I = 23` (hochst-integriertes System, legitim als zentraler Orchestrator)
- ArenaStar System: `d_ein = 5` (CoreLoop, StarEcon, Event, Minigame, Audio), `d_aus = 1` (UI) → `I = 6` (moderat, primar Darstellung)
- Accessibility System: `d_ein = 5` (UI, Audio, Input, Camera, Save), `d_aus = 0` → `I = 5` (reiner Konsument, korrekt so)

Interpretation:
- `I > 15`: Hochintegriertes Kernsystem. Jede Anderung muss gegen alle Abhangigkeiten getestet werden. Prioritat in Code-Reviews.
- `5 <= I <= 15`: Mittleres System. Anderungen haben lokalisierte Auswirkungen.
- `I < 5`: Gering integriertes System. Kann weitgehend isoliert entwickelt und getestet werden.

### 4.2 Fork-Status-Verteilung

`F = (A, B, C, D)` wobei:
- `A` = Anzahl Systeme mit Status ✅ (STP ubernommen)
- `B` = Anzahl Systeme mit Status 🔧 (STP modifiziert)
- `C` = Anzahl Systeme mit Status 🆕 (Neu)
- `D` = Anzahl Systeme mit Status ❌ (STP entfernt)

Aktuelle Verteilung (27 Systeme total):
- `A = 2` (Plugin Loader, Save System) → 7,4 %
- `B = 13` (CoreLoop, Board, NodeBoard, Player, Dice, CoinEcon, ItemShop, Minigame, MinigameQ, Lobby, Network, UI, Audio, Input, Camera, Victory) → 48,1 %
- `C = 12` (StarEcon, Item, StarShop, Event, Character, CatchUp, ArenaStar, Accessibility, Localization) → 44,4 %
- `D = 0` (Keine Systeme komplett entfernt)

Interpretation: ~55 % der Systeme haben STP-Erbe (A+B), ~44 % sind komplett neu (C). Dies bestatigt den "harten Fork"-Charakter: genug STP-Basis fur Zeitersparnis, genug Neues fur Eigenstandigkeit.

### 4.3 Entwicklungs-Reihenfolge (Topologische Sortierung)

Die Abhangigkeiten erzwingen eine Entwicklungs-Reihenfolge (System X muss vor System Y fertig sein, wenn Y von X abhangt):

1. **Fundament (Woche 1–2):** Plugin Loader, Save System, Network System, Input System (✅+🔧, STP-Basis steht)
2. **Core (Woche 3–5):** Core Loop, Board Controller, NodeBoard, Player Controller, Dice System, Coin Economy (🔧 modifiziert)
3. **Erweiterungen (Woche 6–8):** Star Economy, Item System, Item Shop, Star Shop, Event System, Catch-Up System (🆕 neu)
4. **Inhalte (Woche 9–12):** Character System, Minigame System, Minigame Queue (🆕 + 🔧)
5. **Prasentation (Woche 10–13):** Lobby System, UI System, Audio System, Camera System, ArenaStar System (🆕 + 🔧)
6. **Politur (Woche 13–14):** Victory System, Accessibility System, Localization System (🔧 + 🆕)

---

## 5. Edge Cases

1. **Systemuberschneidung Core Loop vs. Board Controller:** Der Core Loop steuert die Phasen (ROLL, MOVE, EVENT, etc.), der Board Controller steuert die Feld-Logik und Stern-Wanderung. Wenn eine Feld-Aktion eine Phasenanderung auslost (z.B. MINIGAME-Feld lost Minispiel-Phase aus), wer ist zustandig? **Regel:** Der Core Loop ist immer der Phasen-Manager. Der Board Controller signalisiert "Feld X wurde betreten, Typ = MINIGAME", und der Core Loop entscheidet, ob und wann die MINIGAME-Phase gestartet wird. Der Board Controller lost NIE selbstandig Phasenanderungen aus.
2. **Item-Effekt uberschreibt Core-Loop-Entscheidung:** Ein Item (z.B. Teleporter) andert die Spieler-Position wahrend der ROLL-Phase. **Regel:** Item-Effekte werden VOR der Bewegungs-Phase ausgefuhrt. Wenn ein Item die Position andert, wird die Bewegung ab der neuen Position fortgesetzt. Der Core Loop delegiert die Item-Ausfuhrung an das Item System, akzeptiert das Ergebnis und fahrt mit der nachsten logischen Phase fort.
3. **Network System fallt aus wahrend Event-Ausfuhrung:** Ein Client disconnected, wahrend der Server ein Event ausfuhrt. **Regel:** Das Event wird fur alle verbundenen Clients normal ausgefuhrt. Der disconnectete Spieler wird von der KI ubernommen, die das Event-Ergebnis empfangt, sobald die Verbindung wiederhergestellt ist (oder das nachste Full-State-Update).
4. **Zwei Systeme beanspruchen dieselbe Godot-Datei:** Der Player Controller und der Character Loader verwenden beide `character.gd`. **Regel:** Zustandigkeit wird nach primarer Verantwortung vergeben. `character.gd` gehort zum Character System (es definiert die Charakter-API). Der Player Controller ist ein Konsument (er nutzt die API, besitzt sie aber nicht). Anderungen an `character.gd` werden vom Character-System-Besitzer verantwortet.
5. **Neues Feature passt in kein bestehendes System:** **Regel:** Neues Feature → neues System oder Erweiterung eines bestehenden Systems. Die Entscheidung wird nach dem Kriterium "Eigenstandige Verantwortlichkeit" getroffen: Hat das Feature eine klar abgrenzbare Zustandigkeit, die nicht in ein bestehendes System integriert werden kann? Wenn ja → neues System, neuer Eintrag in diesem Index. Wenn nein → Erweiterung des nachstliegenden bestehenden Systems.
6. **STP-System existiert, ist aber im Index nicht gelistet:** **Regel:** STP-Systeme, die nicht im Index gelistet sind, wurden entweder entfernt (Nolok/GNU, Sara-Moderation, Duel-System) oder in andere Systeme integriert (STP's `tracking_manager.gd` → optional, nicht als eigenes System gefuhrt). Entwickler durfen keine Logik zu nicht gelisteten Systemen hinzufugen, ohne den Index vorher zu aktualisieren.

---

## 6. Dependencies

### 6.1 Abhangigkeiten dieses Dokuments

| Benotigt von `systems-index.md` | Art | Verwendung |
|---|---|---|
| `design/gdd/technical-architecture.md` | Quelle | Liefert die Ordnerstruktur, Node-Zuordnung und Architekturmuster. |
| `design/gdd/technical-multiplayer.md` | Quelle | Definiert das Network System und seine RPCs. |
| `design/gdd/core-loop.md` | Quelle | Spezifiziert den Spielfluss, den der Core Loop implementiert. |
| `design/gdd/technical-fork-strategy.md` | Peer | Definiert, welche Dateien ubernommen/modifiziert/neu sind. |
| `.claude/rules/design-docs.md` | Regelwerk | Definiert den 8-Sektionen-Standard. |

### 6.2 Systeme, die von diesem Dokument abhangen

| System | Art der Abhangigkeit |
|---|---|
| Alle 27 gelisteten Systeme | Jedes System MUSS seine Zustandigkeiten, Godot-Zuordnung und Abhangigkeiten gemass diesem Index implementieren. |
| `technical-architecture.md` | Der Index konkretisiert die Architektur auf System-Ebene. |
| `bible-index.md` | Der systems-index ist das Bindeglied zwischen Design-Kapiteln und technischer Implementierung. |
| `README.md` | Verweist auf diesen Index fur Entwickler. |
| CI / Code-Review | Der Fork-Status und die Zustandigkeiten dienen als Review-Checkliste. |

---

## 7. Tuning Knobs

| Knob | Kategorie | Gultiger Bereich | Standard | Auswirkung |
|---|---|---|---|---|
| Anzahl der Systeme | Gate | 27 (fest, nur nach Freigabe anderbar) | 27 | Anderung erfordert Update aller Abhangigkeitsgraphen. |
| System-Integrationskomplexitat I(S) | Kurve | 0–30 | variiert | Zeigt an, welche Systeme bei Anderungen besondere Vorsicht erfordern. |
| Fork-Status | Gate | ✅, 🔧, 🆕, ❌ | variiert | Bestimmt die Entwicklungs- und Teststrategie (STP-ubernommen = Regression-Tests, Neu = Unit-Tests). |
| Entwicklungsphase | Kurve | 1–6 | 1 | Steuert die Reihenfolge der Implementierung (siehe Formel 4.3). |

---

## 8. Acceptance Criteria

1. **Vollstandigkeit:** Der Index listet exakt 27 Systeme auf. Jedes System hat Name, Kurzbeschreibung, 3–5 Zustandigkeiten, Godot-Node/Scene-Zuordnung, Status-Emoji und Abhangigkeitsliste. PASS/FAIL.
2. **Node-Zuordnung:** Jedes System verweist auf mindestens eine konkrete `.gd`- oder `.tscn`-Datei im Projekt (kein System ohne Datei). PASS/FAIL.
3. **Abhangigkeitskonsistenz:** Wenn System A in seiner Abhangigkeitsliste System B nennt, muss System B existieren und seinerseits eine relevante Schnittstelle zu A bereitstellen. Keine zirkularen Abhangigkeiten. PASS/FAIL.
4. **Fork-Status-Korrektheit:** Der Status jedes Systems stimmt mit `technical-fork-strategy.md` uberein (✅ = Kat A, 🔧 = Kat B/C, 🆕 = Kat D, ❌ = in STP aber nicht PA). PASS/FAIL.
5. **Kein verwaistes System:** Jedes System hat mindestens eine eingehende ODER ausgehende Abhangigkeit (kein vollstandig isoliertes System). Ausnahme: rein optionale Systeme (z.B. Accessibility — korrekt, da es nur von keiner Spielmechanik gebraucht wird). PASS/FAIL.
6. **Topologische Sortierbarkeit:** Die Abhangigkeiten aller 27 Systeme ergeben einen azyklischen Graphen (keine Zirkelschlusse). PASS/FAIL.
7. **Erlebbar (Experiential):** Ein neuer Entwickler findet in unter 2 Minuten heraus, welche Datei er andern muss, um eine bestimmte Spielfunktion zu modifizieren. PASS/FAIL (Protokoll).
