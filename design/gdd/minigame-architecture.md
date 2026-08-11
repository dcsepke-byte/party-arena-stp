# Minigame-Architektur — Party Arena Game Bible

> **Teil:** IV — Minigames
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md (Abschnitt "Minispiele"), STP-Plugin-Architektur (`common/scripts/loader/minigame_loader.gd`, `common/scenes/countdown/countdown.gd`, `common/scenes/split_screen/split_screen.gd`, `server/lobby.gd`, `plugins/minigames/*`)

---

## 1. Overview

Dieses Kapitel definiert das Minispiel-Framework von Party Arena: das Plugin-System, über das alle Minispiele eingebunden werden, den verbindlichen Lebenszyklus einer Minispiel-Runde, das Kamera-System (Split-Screen und Vogelperspektive), das 8-Spieler-Input-Mapping, die Platzierungs- und Gleichstandslogik sowie die Minispiel-Auswahl und den Ladevorgang. Jedes Minispiel ist ein eigenständiger Plugin-Ordner unter `plugins/minigames/` mit genau drei Pflichtdateien (`minigame.gd`, `minigame.tscn`, `minigame.json`); die Basisklasse erbt von `Node3D` und definiert die Schnittstelle zwischen Framework und Minispiel. Das Framework besitzt die globale Steuerung (Countdown, Timer, Kamera, Platzierung, Belohnungs-Übergabe) und behandelt Sonderfälle wie Disconnects, Zeitüberschreitung und Fehler. Alle 2–8 Spieler nehmen an jedem Minispiel teil, unabhängig davon, auf welchem Feld sie am Board stehen. Das Kapitel ist die Grundlage für `minigame-categories.md` (die 12 konkreten Minispiele), `minigame-rewards.md` (Münz-Auszahlung) und `minigame-template.md` (Bauanleitung für neue Minispiele).

## 2. Player Fantasy

Der Übergang vom Board zum Minispiel ist der spannendste Moment einer Runde: Nach dem gemächlichen Würfel-Takt am Board springt die ganze Gruppe gleichzeitig in ein kurzes, lautes, überzeichnetes Spielzeug-Abenteuer. Das zentrale Versprechen lautet: **"Jetzt sind wir alle gleichzeitig dran — und jeder hat eine echte Chance."** Niemand schaut zu, niemand wartet; alle 8 Spieler steuern gleichzeitig, alle sehen denselben Countdown, alle erleben dieselbe Spannung in den letzten Sekunden, wenn der Timer rot wird. Der Countdown ("3, 2, 1, LOS!") erzeugt einen kollektiven Atem-Moment, der die Gruppe als Einheit fühlen lässt, bevor der Wettbewerb entbrennt. Die zwei Kamera-Modi sichern die beiden Kern-Erlebnisse: Bis 4 Spieler hat jeder seinen eigenen Bildausschnitt (Autonomie, klare eigene Perspektive, kein Abschauen nötig); ab 5 Spieler entsteht durch die gemeinsame Vogelperspektive ein Stadion-Gefühl — man sieht alle gleichzeitig kämpfen und fiebert gemeinsam (Fellowship). Der sichtbare Timer baut Druck und Vorfreude auf (MDA-Aesthetic "Challenge"), und die harte 30-Sekunden-Grenze garantiert, dass der Spannungsbogen nie zäh wird: Jede Minispiel-Runde ist ein kurzer, intensiver Burst, der nach dem Belohnungs-Screen wieder in den ruhigen Board-Fluss übergeht. Für die Zielgruppe (Kinder ab 6, Familien) ist die Fantasie zudem eine der **Fairness**: Kein Minispiel erfordert Vorwissen oder Übung, alle Startbedingungen sind gleichwertig, und Gleichstände werden großzügig gemittelt, damit sich niemand ungerecht behandelt fühlt.

## 3. Detailed Rules

### 3.1 Plugin-Struktur

Jedes Minispiel ist ein eigener Plugin-Ordner unter `res://plugins/minigames/`. Der Ordnername ist `snake_case` (klein, keine Umlaute, keine Leerzeichen), z. B. `muenzregen` oder `balance_akt`. Die Ordnerkonvention folgt der bestehenden STP-Struktur (`plugins/minigames/boat_rally`, `plugins/minigames/bowling`, …).

Pflichtdateien je Plugin:

| Datei | Zweck |
|-------|-------|
| `minigame.gd` | Minigame-Logik. Erbt von der Minigame-Basisklasse (siehe 3.2). |
| `minigame.tscn` | Root-Szene des Minispiels. Wurzelknoten ist ein `Node3D` mit `minigame.gd` als Skript. Enthält Arena, Spawn-Punkte und Minigame-spezifische Assets. |
| `minigame.json` | Metadaten: Name, Kategorie, Spielerzahl-Bereich, Dauer, Beschreibung, Anleitung, Tags. Schema in `minigame-template.md` Abschnitt 3.2. |

Optionale Elemente je Plugin:

| Element | Zweck |
|---------|-------|
| `translations/` | Lokalisierungsdateien (`.po`/`.pot`) für Regeltexte und UI des Minispiels. |
| `screenshot.png` | Vorschau-Bild (512×288) für Auswahl- und Info-Screens. |
| `assets/` | Minigame-eigene Texturen, Modelle, Sounds (falls nicht in der `.tscn` referenziert). |

Das Framework enthält **keine** minigame-spezifische Logik. Ein Minispiel kann hinzugefügt oder entfernt werden, ohne das Framework zu ändern; die einzige Anbindung ist der Schnittstellenvertrag aus 3.2 und das JSON-Schema.

### 3.2 Basisklasse MinigameBase (Schnittstellenvertrag)

Die Basisklasse erbt von `Node3D`. Sie definiert die Aufruf-Reihenfolge des Frameworks, die Pflicht-Methoden, die ein Minispiel implementieren MUSS, sowie die vom Framework bereitgestellten Hilfsmittel. Die Aufruf-Reihenfolge ist verbindlich und wird vom Framework garantiert:

1. `setup(lobby, players, options)` — Framework übergibt Kontext, **bevor** die Szene in den Baum eingefügt wird: Lobby-Referenz, Array aller teilnehmenden Spielerzustände (mindestens `player_id`, `character`, `color`, `controller`), und optionale, minigame-spezifische Parameter aus dem JSON.
2. `_ready()` — Minispiel baut die Szene auf und platziert alle Spieler an ihren Spawn-Positionen (siehe 3.5).
3. `start_game()` — Wird aufgerufen, sobald der Countdown beendet ist. Ab hier ist Input aktiv; das Minispiel initialisiert seinen Spielzustand. Die Spieldauer wird vom Framework-Timer bestimmt, nicht vom Minispiel.
4. (Spielphase — der Framework-Timer zählt herunter; das Minispiel aktualisiert seine Logik in `_process()`.)
5. `end_game()` — Wird vom Framework aufgerufen, wenn (a) der Timer abgelaufen ist oder (b) das Minispiel `request_end()` aufgerufen hat. Das Minispiel friert seine finale Wertung ein.
6. `get_results() -> Array[Dictionary]` — Wird nach `end_game()` aufgerufen. Liefert je Spieler einen Eintrag `{"player_id": int, "score": float}`. Das Framework berechnet daraus die Platzierung (siehe 4.2).
7. `cleanup()` — Wird aufgerufen, bevor das Framework die Szene freigibt. Minigame-interne Timer, Signale und Ressourcen werden entfernt.

Pflicht-Signale und -Aufrufe des Minispiels:

| Element | Richtung | Zweck |
|---------|----------|-------|
| `request_end()` | Minispiel → Framework | Fordert ein vorzeitiges Ende an (Sieg-/Eliminationsbedingung erreicht, z. B. letzter Spieler auf der Kugel). Das Framework ruft danach `end_game()` und `get_results()` auf. |
| `finish` | Framework → Minispiel (über den bereitgestellten Countdown-Knoten) | Signalisiert das Ende des Countdowns. Das Minispiel darf es ignorieren, weil das Framework danach `start_game()` aufruft. |

Pflichtfelder, die das Minispiel während `_ready()` lesen darf (vom Framework gesetzt):

| Feld | Typ | Bedeutung |
|------|-----|-----------|
| `player_count` | int | Tatsächliche Anzahl teilnehmender Spieler (2–8). |
| `players` | Array | Spielerzustände in der Reihenfolge der Spielernummer (1–n). |

Das Minispiel **darf nicht**: den Framework-Timer manipulieren, die Kamera wechseln, den Countdown auslösen oder die Platzierungslogik überschreiben. Diese Elemente gehören dem Framework (Ausnahme: Minispiel wählt `results_mode`, siehe 3.9).

### 3.3 Lebenszyklus einer Minispiel-Runde

Das Framework führt jede Minispiel-Runde durch die folgenden Zustände. Ein Zustandsübergang ist nur durch das Framework erlaubt.

| Zustand | Dauer | Beschreibung |
|---------|-------|--------------|
| 1. LOADING | variabel (Ladezeit) | Framework instanziiert die Plugin-Szene, ruft `setup()` auf, fügt die Szene in den Baum ein. Lade-Screen mit Spielname und ArenaStar-Vorschau. |
| 2. INTRO (Countdown) | 3 s | Overlay zeigt "3, 2, 1, LOS!" (lokalisiert) mit Tick-Sounds. Input ist gesperrt. ArenaStar nennt in 1 Satz das Ziel (optional, parallel zum Countdown). |
| 3. PLAYING | bis zu `duration` s (Standard 30, hartes Maximum 30) | Spielphase. Timer ist sichtbar. Das Framework ruft `start_game()` auf und ruft bei Ablauf `end_game()` auf. |
| 4. RESULTS | 5 s | Platzierungen werden berechnet und angezeigt (Rangliste 1–n). ArenaStar ruft die Top-3-Namen auf (narrative-arena-star.md). |
| 5. REWARDS | variabel | Belohnungs-Screen: Münzen werden ausbezahlt (minigame-rewards.md), ArenaStar kommentiert die Top 3. |
| 6. UNLOAD | variabel | `cleanup()` wird aufgerufen, die Szene wird freigegeben, das Spiel kehrt zum Board zurück. |

Zeitbudget-Formeln in Abschnitt 4.1. Die Lifecycle-Angabe "Spielphase ~25 s" ist ein Designziel für die *effektive* Spieldauer (frühe Enden und kürzere `duration`-Werte inklusive), nicht ein fester Wert; das harte Zeitlimit ist 30 s.

### 3.4 Countdown

- Der Countdown ist ein Framework-Element (STP-Komponente `common/scenes/countdown/countdown.gd`), das über jeder Minigame-Szene liegt. Standarddauer: 3 s.
- Ablauf: Anzeige "3" (1 s), "2" (1 s), "1" (1 s), dann "LOS!" mit Start-Sound. Jede Zahl hat einen Tick-Sound; "LOS!" einen hellen Start-Jingle.
- Während des Countdowns ist die gesamte Minigame-Interaktion gesperrt (Prozess-Modus des Minigame-Knotens deaktiviert). Bewegungen, Würfe oder Tastendrücke haben keine Wirkung. Dadurch ist der Start für alle Spieler garantiert fair.
- Nach dem letzten Tick setzt das Framework `start_game()` auf.
- Der Countdown ist für alle Spieler gleichzeitig sichtbar (Overlay im Vollbild; bei Split-Screen zentriert über beiden/allen Viewports).

### 3.5 Spielphase und Zeitlimit

- Die Spieldauer `duration` steht in `minigame.json` (Standard 30, erlaubter Bereich 10–30). Das Framework startet bei `start_game()` einen Timer mit `duration` Sekunden.
- **Hartes Zeitlimit: 30 s.** Werte über 30 in `minigame.json` werden vom Loader auf 30 gedeckelt und als Validierungswarnung protokolliert.
- Der Timer basiert auf der **Wanduhr** (`Time.get_ticks_msec()`), nicht auf Frame-Zählung; Frame-Drops verfälschen die Spieldauer nicht.
- Timer-Anzeige: groß, oben mittig, als Sekunden-Zahl (z. B. "30", "12", "3"). Ab ≤ 10 s färbt sich die Anzeige orange, ab ≤ 5 s rot und pulsiert. Das entspricht Pfeiler 3 (Interaktiv wirkend): Der Zeitdruck wird sichtbar und hörbar (Ticken in der letzten Sekunde).
- Bei Ablauf (Timer = 0) ruft das Framework zwingend `end_game()` auf, unabhängig vom Minigame-Zustand. Ein Minispiel, das nicht von selbst endet, wird also immer sauber beendet.
- Vorzeitiges Ende: Ruft das Minispiel `request_end()` auf, beendet das Framework die Spielphase sofort (führt `end_game()` aus), auch wenn der Timer noch läuft.
- Pause-Menü: Während das Pause-Menü geöffnet ist, pausiert der Framework-Timer (das Spiel ist angehalten). Dies gilt lokal und online konsistent.

### 3.6 Kamera

Das Framework besitzt die Kamera. Es gibt genau zwei Modi, abhängig von der Spielerzahl:

| Spielerzahl | Modus | Layout |
|-------------|-------|--------|
| 2 | Split-Screen, 1×2 | Spieler 1 links, Spieler 2 rechts (nebeneinander, volle Höhe). |
| 3 | Split-Screen, 2×2 | Spieler 1 oben-links, Spieler 2 oben-rechts, Spieler 3 unten-links; unten-rechts zeigt die gemeinsame Vogelperspektive der Arena. |
| 4 | Split-Screen, 2×2 | Spieler 1 oben-links, 2 oben-rechts, 3 unten-links, 4 unten-rechts. |
| 5–8 | Freie Vogelperspektive | Eine Vollbild-Kamera von oben (Free-for-all-Kamera), die die gesamte Arena zeigt. |

- Der Split-Screen nutzt die bestehende STP-Mechanik (`common/scenes/split_screen/split_screen.gd`, `split_screen_camera.gd`): Je Spieler ein `SplitScreenCamera`-Knoten mit eigenem `SubViewport`; die Viewports werden auf ein TextureRect-Raster gelegt.
- Jede Spieler-Kamera folgt ihrem zugeordneten Charakter (weiche Nachführung, Ruckelfilter). Bei der 3-Spieler-Anordnung ist der vierte (unten-rechte) Viewport eine feste Vogelperspektive, damit der leere Quadrant nicht tot wirkt.
- Die Vogelperspektive für 5–8 Spieler ist eine einzelne Kamera, die die Arena von oben und leicht schräg zeigt; sie folgt keinem einzelnen Spieler, sondern rahmt die ganze Arena ein. Sie darf während des Minispiels leicht zoomen (z. B. auf die aktivste Region), muss aber **jederzeit alle aktiven Spieler** im Bild behalten.
- Konsequenz für das Minigame-Design (verbindliche Einschränkung): Die Arena muss kompakt genug sein, um in einer Vollbild-Vogelperspektive vollständig und gut lesbar zu sein. Arenen, die nur im Split-Screen funktionieren, sind nicht zulässig (Checkliste in `minigame-template.md` Abschnitt 3.6).
- Zwischen Board-Phase und Minispiel blendet das Framework mit einer kurzen Überblendung (Standard 1 s) um.

### 3.7 Input

- Alle 8 Spieler steuern gleichzeitig. Das Framework verwendet pro Spieler einen eigenen Aktionssatz nach STP-Konvention: `player1_…` bis `player8_…` mit den Aktionen `up`, `down`, `left`, `right`, `action1`, `action2`, `action3`, `action4`, `spacer` (vgl. `_ACTIONS` in `minigame_loader.gd`).
- Das Minispiel liest Eingaben **ausschließlich** über diese benannten Aktionen. Es verarbeitet keine rohen Geräte-Events und kümmert sich nicht um Device-Zuordnung.
- Geräte-Zuordnung (Lobby setzt sie beim Join): Spieler n ist an Gerät `n-1` gebunden.

| Spieler | Gamepad | Tastatur-Standard (Bewegung / action1) |
|---------|---------|----------------------------------------|
| 1 | Joypad 0 | W A S D / Leertaste |
| 2 | Joypad 1 | Pfeiltasten ↑ ← ↓ → / Enter |
| 3 | Joypad 2 | T F G H / R |
| 4 | Joypad 3 | I J K L / U |
| 5 | Joypad 4 | Numpad-Diamant (KP8 KP4 KP5 KP6) / KP0 — Best-Effort, Empfehlung Gamepad |
| 6 | Joypad 5 | keine Tastatur-Standardbelegung — Gamepad empfohlen oder Remapping |
| 7 | Joypad 6 | keine Tastatur-Standardbelegung — Gamepad empfohlen oder Remapping |
| 8 | Joypad 7 | keine Tastatur-Standardbelegung — Gamepad empfohlen oder Remapping |

- Für Spieler 1–4 ist die Tastatur voll unterstützt (physisch sinnvolle Cluster). Für Spieler 5–8 ist die Tastatur nur über den Control-Remapper (`client/menus/control_remapping/`) oder den Numpad-Diamanten verfügbar; der Ziel-Input für 5–8 Spieler ist das Gamepad. Diese Grenze wird in `ui-accessibility.md` als dokumentierte Einschränkung geführt.
- Zusätzliche Aktionen (`action2`–`action4`) sind optional und werden in `minigame.json` über das optionale Feld `controls` beschrieben (siehe `minigame-template.md` Abschnitt 3.2).
- Die Zuordnung Tastatur → Spieler ist im Control-Remapper frei änderbar; die Defaults oben sind Ausgangswerte.

### 3.8 Teilnahme und Spielerzustand

- **Alle** 2–8 Spieler nehmen an jedem Minispiel teil — auch diejenigen, die in dieser Runde kein Minigame-Feld betreten haben. Es gibt keine Zuschauer und keine Nicht-Teilnehmer.
- Das Framework übergibt dem Minispiel die Spielerzustände in der Reihenfolge der Spielernummer. Ein Spielerzustand enthält mindestens: `player_id` (1–8), `character` (Arenian-Typ), `color` (Signaturfarbe), `controller` (Geräte-Index).
- Das Minispiel erzeugt oder erhält pro Spieler eine spielbare Figur (typischerweise den Charakter in der Minigame-tauglichen Form). Die Wiederverwendung der Board-Charaktere ist empfohlen (Wiedererkennbarkeit, Pfeiler 4), aber nicht erzwungen.

### 3.9 Scoring und Platzierung

- Das Minispiel liefert in `get_results()` je Spieler einen Roh-Score (`score`). Die Interpretation übernimmt das Framework.
- Zwei Ergebnis-Modi, wählbar über das optionale JSON-Feld `results_mode`:

| Modus | Bedeutung | Gleichstand |
|-------|-----------|-------------|
| `by_points` (Standard) | Höherer `score` = besser. Das Framework sortiert absteigend und gruppiert **gleiche Scores** zu Gleichstands-Gruppen. | Automatisch, über identischen Score. |
| `by_position` | Das Minispiel liefert die Endreihenfolge selbst (z. B. Zielankunft). Das Framework erzeugt daraus die Platzierung; Gleichstände muss das Minispiel durch identische Platzierung signalisieren. | Vom Minispiel gemeldet. |

- Ausgabe der Platzierung: ein Array von Arrays, aufsteigend nach Platz — `[[Spieler-IDs auf Platz 1], [Spieler-IDs auf Platz 2], …]` (gleiche Struktur wie `minigame_summary.placement` in STP). Beispiel: `[[2], [1, 5], [3], [4, 6, 7], [8]]` bedeutet: Platz 1 = Spieler 2; Platz 2 = Spieler 1 und 5 (geteilt); Platz 3 = Spieler 3; Platz 4 = Spieler 4, 6 und 7; Platz 5 = Spieler 8.
- Die Platzierung wird an das Belohnungssystem übergeben (`minigame-rewards.md`), das daraus Münzen berechnet. Gleichstände führen zur Mittelung (dort Abschnitt 3.5).
- Formel der Platzierungsberechnung in Abschnitt 4.2.

### 3.10 Minigame-Selektion

- Die Selektion erfolgt zufällig und gleichverteilt aus dem Pool der Minispiele, die für die aktuelle Spielerzahl gültig sind (Bedingung `players.min ≤ n ≤ players.max` aus `minigame.json`).
- **Kein Minispiel zweimal hintereinander:** Das zuletzt gespielte Minispiel ist von der Auswahl ausgeschlossen (Ausschluss-Gedächtnis = 1). Wird der Pool dadurch leer, fällt der Ausschluss weg (siehe Edge Cases).
- Die Auswahl findet statt, wenn am Rundenende das Minigame-Feld auslöst (siehe 3.13). Das gewählte Minispiel wird aus der Kandidatenmenge entfernt; nach dem Minispiel ist es wieder verfügbar (Ausnahme: Ausschluss in der Folgerunde).
- Der Zufallsgenerator wird pro Partie geseedet; die Auswahl ist serverautoritär (siehe `technical-multiplayer.md`).
- Kategorie-Gewichtung: keine. Alle gültigen Minispiele haben die gleiche Wahrscheinlichkeit. Eine Gewichtung ist als Tuning-Knob vorgesehen, aber standardmäßig aus (Knob in Abschnitt 7).

### 3.11 Minigame-Loader

- Der Loader (Erweiterung des STP-`minigame_loader.gd`) scannt beim Start alle `res://plugins/minigames/*/minigame.json` über `PluginSystem.load_files_from_path`.
- Für jede gefundene JSON-Datei: Schema-Validierung (Regeln in `minigame-template.md` Abschnitt 4.3). Bei Validierungsfehler wird der Fehler protokolliert und das Minispiel **übersprungen** (es erscheint nicht im Pool).
- Registrierung: Das Minispiel wird in den Gesamtpool und in den Kategorie-Pool seiner `category` einsortiert.
- Doppelte Namen (zwei Minispiele mit identischem `name`): Das zuletzt geladene gewinnt; eine Warnung wird protokolliert.
- Fehlende Szene oder falscher Wurzelknoten (`minigame.tscn` ohne `Node3D`-Wurzel mit Basisklassen-Skript): Registrierung schlägt fehl, Fehler wird protokolliert.
- Der Loader exponiert nach dem Scan: `get_all()`, `get_valid(player_count)`, `get_random(player_count, exclude_last)`, `get_by_category(category)`, `get_count()`. Diese API ist der einzige Zugriffspunkt des Frameworks auf den Pool.

### 3.12 Fehlerbehandlung und Abbruch

- **Laufzeitfehler im Minigame-Skript** (z. B. Fehler in `_process()`): Das Framework fängt den Fehler, bricht die Spielphase ab, ruft `end_game()` + `get_results()` auf (falls möglich) und übergibt eine "Abbruch-Platzierung": Alle noch nicht platzierten Spieler erhalten den letzten Platz. Der Fehler wird protokolliert.
- **Kann `get_results()` nicht aufgerufen werden** (Minispiel hängt): Alle Spieler erhalten den letzten Platz (bei 8 Spielern: alle Platz 8, gleiche Auszahlung). Protokollierung als Blocker für das nächste Minigame-Review.
- **Disconnect eines Spielers** während einer Minispiel-Runde: Der Spieler gilt ab sofort als nicht mehr teilnehmend. Seine Figur wird entfernt (oder einfriert an Ort und Stelle). Bei der Platzierungsberechnung erhält der Spieler den **letzten Platz** (bei n Spielern: Platz n). Die Auszahlung folgt dem letzten Platz (siehe `minigame-rewards.md`).
- **Disconnect während Countdown, RESULTS oder REWARDS:** Gleiche Regel — der Spieler belegt den letzten Platz. Bereits begonnene Auszahlungen an seinen Spielerzustand bleiben gültig.
- **Nur noch 1 Spieler aktiv** (alle anderen disconnected): Das Minispiel wird sofort beendet; der verbleibende Spieler erhält Platz 1.
- **Pause/Esc während des Minispiels:** Öffnet das Pause-Menü, Timer pausiert (siehe 3.5).
- **Versuchs-Modus (Try):** Existiert der STP-Versuchmodus (`minigame_state.is_try`), läuft das Minispiel ohne Belohnung und ohne Statistik; es dient nur der Vorschau. Die Auszahlung wird vollständig übersprungen.

### 3.13 Einbettung in den Rundenablauf

- Der Rundenablauf (siehe `core-loop.md`): Alle Spieler würfeln und ziehen → **Minispiel-Phase** → Stern-Phase → nächste Runde.
- Die Minispiel-Phase wird am Ende der Zugreihenfolge ausgelöst (nicht zwingend durch ein Minigame-Feld — in Party Arena spielt **jede** Runde ein Minispiel, die Feld-Typen steuern nur den Board-Teil). Dies ist eine bewusste Design-Entscheidung gegenüber STP, wo nur ein Minigame-Feld ein Minispiel auslöst; sie ist in `field-minigame.md` gespiegelt.
- Ablauf: ArenaStar kündigt das Minispiel an (kurze Intro-Szene mit Spielname) → LOADING → INTRO → PLAYING → RESULTS → REWARDS → zurück zum Board (nächste Runde).
- Nach dem Minispiel kehren alle Spieler an ihre Board-Positionen zurück; die Münz-Kontostände wurden durch den Reward-Screen aktualisiert.

## 4. Formulas

### 4.1 Zeitbudget einer Minispiel-Runde

`T_gesamt = T_laden + T_countdown + T_spiel + T_results + T_rewards`

| Variable | Definition | Standard | Bereich |
|----------|-----------|----------|---------|
| `T_laden` | Ladezeit der Plugin-Szene | variabel | — |
| `T_countdown` | Countdown-Dauer | 3 s | 1–5 s (Knob) |
| `T_spiel` | Effektive Spielphase | 25 s (Ziel) | `min(duration, 30)` |
| `T_results` | Ergebnis-Anzeige | 5 s | 3–8 s (Knob) |
| `T_rewards` | Belohnungs-Screen | variabel (Nutzerbestätigung) | — |

`duration` kommt aus `minigame.json` (Standard 30, gültig 10–30). **Hartes Maximum: 30 s.**

Beispiel (Standard-Minispiel, volle Dauer): `T_gesamt = 0 + 3 + 30 + 5 + T_rewards ≈ 38 s + T_rewards` von Szenen-Load bis Board-Rückkehr. Ein frühes Ende (z. B. Balance-Akt nach 18 s) verkürzt `T_spiel` entsprechend.

### 4.2 Platzierungsberechnung aus Scores

Gegeben: Scores `S[i]` für Spieler `i` (i = 1..n). Sortierung absteigend nach `S`; Spieler mit identischem `S` bilden eine Gruppe.

Für eine Gruppe `g`, die in der sortierten Reihenfolge die Indizes `[a, b]` belegt (0-basiert):

`Platz(g) = a + 1` und die Gruppe belegt die Plätze `a+1 … b+1`.

Ausgabe: `Platzierung = [[IDs Platz 1], [IDs Platz 2], …]`.

Beispiel: Scores `{1: 12, 2: 9, 3: 12, 4: 3, 5: 9, 6: 9, 7: 3, 8: 3}` → sortiert: Gruppe {1,3} (12), Gruppe {2,5,6} (9), Gruppe {4,7,8} (3) → `[[1,3],[2,5,6],[4,7,8]]`.

Bei `results_mode = "by_position"` liefert das Minispiel die Gruppen direkt; das Framework prüft nur, dass alle Spieler genau einmal vorkommen.

### 4.3 Kamerazuordnung

Für `n` Spieler und Spieler-Index `i` (0-basiert, i = 0..n−1):

| n | Viewport von Spieler i | leerer Viewport |
|---|------------------------|-----------------|
| 2 | `i = 0` → links, `i = 1` → rechts | — |
| 3 | `i = 0` → oben-links, `i = 1` → oben-rechts, `i = 2` → unten-links | unten-rechts = Vogelperspektive |
| 4 | `i = 0` → oben-links, `1` → oben-rechts, `2` → unten-links, `3` → unten-rechts | — |
| 5–8 | kein eigener Viewport; eine gemeinsame Vogelperspektive | — |

### 4.4 Selektion

Sei `V` die Menge der für `n` gültigen Minispiele (`players.min ≤ n ≤ players.max`), `L` das zuletzt gespielte Minispiel.

`V' = V \ {L}`

- Falls `|V'| ≥ 1`: `P(x) = 1/|V'|` für alle `x ∈ V'`, `P(L) = 0`.
- Falls `|V'| = 0` (nur `L` ist gültig): `P(L) = 1`; eine Warnung wird protokolliert (Wiederholung erlaubt).

Beispiel: 12 Minispiele im Pool, alle gültig für n = 4, zuletzt gespielt "Münzregen" → `|V'| = 11`, jedes Minispiel außer Münzregen hat `P = 1/11 ≈ 9,1 %`.

### 4.5 Validierung von `duration`

`duration_gültig = clamp(duration, 10, 30)`

- `duration < 10` → Warnung, Wert wird auf 10 gesetzt.
- `duration > 30` → Warnung, Wert wird auf 30 gedeckelt.
- Immer ganzzahlig (Sekunden).

## 5. Edge Cases

1. **Disconnect während des Countdowns:** Der Spieler gilt als nicht angetreten; er belegt den letzten Platz. Das Minispiel startet mit den verbleibenden Spielern.
2. **Alle bis auf einen Spieler disconnected:** Das Minispiel wird sofort beendet; der verbleibende Spieler erhält Platz 1 (siehe 3.12).
3. **Spielerzahl unter `players.min` gefallen:** Die Selektion filtert nach der aktuellen Spielerzahl. Ist kein Minispiel mehr gültig, greift ein Notfall-Pool aus allen Minispielen (unabhängig vom `min`-Feld); es wird eine Warnung protokolliert.
4. **Ungerade Spielerzahl bei Team-Minispielen:** Minispiele mit `team_mode = "coop_teams"` (z. B. Schatz-Trage) deklarieren `players.min = 4` und sind bei n = 3, 5, 7 nicht im Pool (Konsequenz aus `minigame-categories.md` Abschnitt 3.6).
5. **`get_results()` liefert nicht alle Spieler:** Fehlende Spieler werden mit dem letzten Platz ergänzt; Protokollierung.
6. **`score` enthält `NaN` oder `inf`:** Der Spieler wird als letzter platziert; der Score wird auf den niedrigsten endlichen Wert gesetzt.
7. **Minispiel ruft `request_end()` vor `start_game()` auf:** Der Aufruf wird ignoriert und protokolliert.
8. **Minispiel ruft `request_end()` mehrfach:** Nur der erste Aufruf wirkt; weitere werden ignoriert.
9. **Laufzeitfehler im Minigame-Skript:** Abbruch mit letzter Platzierung für alle Betroffenen (siehe 3.12); der Fehler wird als Blocker für das nächste Minigame-Review protokolliert.
10. **Fehlerhafte `minigame.json`:** Loader überspringt das Minispiel (3.11); der Pool läuft ohne es weiter.
11. **Doppelter Name:** Das zuletzt geladene Minispiel gewinnt; die frühere Registrierung wird verworfen (3.11).
12. **Nur ein gültiges Minispiel im Pool:** Ausschluss-Regel greift nicht; das Minispiel kann zweimal hintereinander erscheinen (4.4, Formel-Notfallfall).
13. **Frame-Einbrüche (Performance):** Der Timer ist wanduhrbasiert; ein Frame-Drop verlängert die Spielphase nicht. Bei dauerhaft niedriger Framerate greift `technical-performance.md` (Budget 30 FPS Minimum).
14. **Pause-Menü offen:** Timer pausiert; die Spielphase wird nicht abgezogen. Das Minispiel muss Pause-Zustände sauber handhaben (keine Fortschritts-Berechnung in `_physics_process` während Pause).
15. **3-Spieler-Split-Screen:** Der vierte Viewport zeigt die Vogelperspektive; das Minispiel muss nicht wissen, welcher Viewport leer ist (Framework-Handling).
16. **Input-Konflikt durch Control-Remapping:** Zwei Spieler auf dasselbe Gerät gemappt: Die Lobby verhindert das beim Join (doppelte Device-Zuordnung wird abgelehnt); wird es durch Remapping während des Spiels erzeugt, werden beide Spieler-Aktionen mit demselben Event gespeist (geduldet, dokumentiert in `ui-accessibility.md`).
17. **Versuch-Modus:** Keine Auszahlung, keine Statistik, keine Selektion (3.12).

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `minigame-architecture.md` | Art | Verwendung |
|------------------------------------------|-----|------------|
| `design/gdd/game-concept.md` | Quelle | Liefert die Kernwerte (2–8 Spieler, ~30 s Dauer, 5 Kategorien, 12 Minispiele). |
| `design/gdd/minigame-template.md` | Nachgeordnet | Definiert das JSON-Schema und den Methodenvertrag, den dieses Kapitel referenziert (3.2, 3.9). |
| `design/gdd/minigame-rewards.md` | Nachgeordnet | Berechnet aus der Platzierung (3.9) die Münz-Auszahlung. |
| `design/gdd/minigame-categories.md` | Nachgeordnet | Liefert die 12 konkreten Minispiele, die der Loader registriert. |
| `design/gdd/core-loop.md` | Peer | Bestimmt, wann die Minispiel-Phase im Rundenablauf ausgelöst wird (3.13). |
| `design/gdd/field-minigame.md` | Peer | Muss die Entscheidung spiegeln, dass jede Runde ein Minispiel spielt (3.13). |
| `design/gdd/technical-multiplayer.md` | Nachgeordnet | Serverautoritäre Selektion, RPC-Verträge, Synchronisation der Spielphase. |
| `design/gdd/technical-fork-strategy.md` | Peer | Migriert die 6 bestehenden STP-Minispiele auf den neuen Vertrag. |
| `common/scripts/loader/minigame_loader.gd` | Bestand | Wird erweitert (Schema-Validierung, Kategorie-Pools). |
| `common/scenes/countdown/countdown.gd`, `common/scenes/split_screen/split_screen.gd` | Bestand | Werden als Framework-Komponenten wiederverwendet. |
| `.claude/rules/design-docs.md` | Regelwerk | 8-Sektionen-Standard. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `minigame-categories.md` | Jede Kategorie/Minigame-Spezifikation muss den Lebenszyklus, die Kamera-Modi und den Input-Vertrag einhalten. |
| `minigame-rewards.md` | Konsumiert die Platzierungs-Struktur aus 3.9/4.2. |
| `minigame-template.md` | Muss den Schnittstellenvertrag (3.2) exakt als Bauanleitung abbilden. |
| `technical-architecture.md` | Muss das Framework in den Godot-Knotenbaum einordnen (MinigameRoot, Viewports, HUD-Overlay). |
| `technical-performance.md` | Muss das 30-Sekunden-Budget und die Split-Screen-Viewport-Kosten berücksichtigen. |
| `ui-hud.md` | Muss den Timer, den Countdown und die Ergebnis-Rangliste als Framework-UI spezifizieren. |
| `audio-sfx.md` | Muss Countdown-Ticks, Start-Jingle und Timer-Warnung als Pflicht-Sounds führen. |
| `narrative-arena-star.md` | Muss die Moderation in INTRO, RESULTS und REWARDS übernehmen (3.3, 3.13). |

### 6.3 Bidirektionalität

Dieses Kapitel definiert den Vertrag, den alle Minigame-Kapitel (4.1–4.4) erfüllen; diese wiederum liefern dem Framework die konkreten Instanzen und Deckungsfälle. Die Abhängigkeit von `core-loop.md` ist wechselseitig: Der Core Loop löst die Minispiel-Phase aus, und die Minispiel-Phase ist fester Bestandteil des Rundenablaufs. Die Abhängigkeit von `field-minigame.md` ist eine Design-Spiegelung: Dieses Kapitel legt fest, dass das Minispiel am Rundenende läuft, das Feld-Kapitel muss denselben Ablauf beschreiben, damit keine Widersprüche entstehen (bible-index.md Regel 3.1.2).

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| `T_countdown` | Feel | 1–5 s | 3 s | Gefühlte Vorbereitung und Spannung vor dem Start. |
| `T_results` | Feel | 3–8 s | 5 s | Zeit, die die Rangliste sichtbar bleibt; zu lang bremst den Rundenfluss. |
| Hartes Zeitlimit `duration_max` | Gate | 20–30 s | 30 s | Obergrenze aller Minispiel-Spielphasen; schützt das Gesamtspieltempo. |
| Mindestdauer `duration_min` | Gate | 5–15 s | 10 s | Untergrenze für kürzere Minispiele (z. B. Wort-Puzzle 20 s). |
| Ausschluss-Gedächtnis | Kurve | 0–3 | 1 | Wie viele zuletzt gespielte Minispiele von der Auswahl ausgeschlossen sind (0 = Wiederholung erlaubt). |
| Timer-Warnschwelle | Feel | 3–8 s | 5 s | Ab wann die Timer-Anzeige rot pulsiert. |
| Kamera-Überblendung | Feel | 0,5–2 s | 1 s | Dauer des Übergangs Board → Minispiel. |
| Kategorie-Gewichtung | Kurve | 0 (aus) oder Gewichte | aus | Erlaubt, Kategorien zu gewichten (z. B. Kooperation seltener); Standard: gleichverteilt. |
| Abbruch-Platzierung | Gate | letzter Platz oder geteilt | letzter Platz | Platzierung bei Framework-Abbruch (3.12); Alternative: alle teilen sich die mittlere Platzierung. |

Alle Knobs liegen in einer externen Datenquelle (`assets/data/minigame_framework.cfg` bzw. Tuning-Datei), nie hart im Code.

## 8. Acceptance Criteria

Ein QA-Tester kann folgende Prüfungen ausführen (automatisiert oder manuell):

1. **Loader-Registrierung:** Bei Spielstart registriert der Loader alle 12 Party-Arena-Minispiele; `get_count()` = 12 (bzw. die Zahl der gültigen Plugins im Repo). PASS/FAIL.
2. **Schema-Validierung:** Eine absichtlich fehlerhafte `minigame.json` (fehlendes `category`) führt zu einer Fehlermeldung und das Minispiel fehlt im Pool. PASS/FAIL.
3. **Spielerzahl-Filter:** Bei 3 Spielern enthält der Pool kein Minispiel mit `players.min > 3` (z. B. Schatz-Trage bei min 4). PASS/FAIL.
4. **Keine Wiederholung:** Über 30 simulierte Auswahlen bei konstantem n erscheint kein Minispiel unmittelbar zweimal hintereinander (außer im Notfall-Fall mit nur einem gültigen Minispiel). PASS/FAIL.
5. **Lebenszyklus:** Für jedes der 12 Minispiele durchläuft eine Test-Runde alle 6 Zustände (LOADING → INTRO → PLAYING → RESULTS → REWARDS → UNLOAD) in korrekter Reihenfolge; Countdown zeigt 3-2-1-LOS. PASS/FAIL.
6. **Timer-Hartstopp:** Ein Minispiel, das nie `request_end()` aufruft, wird bei Sekunde 30 zwingend beendet; `end_game()` und `get_results()` werden aufgerufen. PASS/FAIL.
7. **Wanduhr-Unabhängigkeit:** Bei künstlich reduzierter Framerate (Performance-Drosselung) endet die Spielphase dennoch nach `duration` Wanduhr-Sekunden (Toleranz ±0,1 s). PASS/FAIL.
8. **Kamera-Modi:** Bei 2, 3, 4 und 8 Spielern erscheinen die korrekten Layouts (1×2, 2×2 mit Vogelquadrant, 2×2, Vollbild-Vogelperspektive); jede Spieler-Kamera folgt ihrem Charakter; in der Vogelperspektive sind alle aktiven Spieler sichtbar. PASS/FAIL.
9. **Input-Mapping:** Alle 8 Spieler können gleichzeitig über Gamepad (Joypad 0–7) steuern; Spieler 1–4 zusätzlich über die Tastatur-Defaults. Jede Aktion wird dem richtigen Spieler zugeordnet. PASS/FAIL.
10. **Platzierung und Gleichstand:** Ein konstruiertes Score-Set mit Gleichständen (z. B. `{1:12, 2:9, 3:12, …}`) erzeugt die korrekte Gruppen-Platzierung `[[1,3],[2,5,6],[4,7,8]]`. PASS/FAIL.
11. **Disconnect:** Bricht Spieler 4 während der Spielphase ab, belegt er den letzten Platz; die übrigen Platzierungen sind unverändert korrekt. PASS/FAIL.
12. **Minispiel-Fehler:** Ein Minispiel mit absichtlich ausgelöstem Laufzeitfehler wird abgebrochen, alle betroffenen Spieler erhalten die Abbruch-Platzierung, das Spiel kehrt zum Board zurück (kein Absturz). PASS/FAIL.
13. **Pause:** Bei geöffnetem Pause-Menü pausiert der Timer; nach Schließen läuft die Restzeit weiter. PASS/FAIL.
14. **Erlebbar (Experiential):** In einem Playtest mit 8 Spielern (gemischte Altersgruppen ab 6) bestätigen ≥ 80 % der Teilnehmer, dass sie während der Spielphase jederzeit wussten, was zu tun ist und wohin sie schauen mussten. PASS/FAIL.
