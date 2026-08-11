# Minispiel-Template — Party Arena Game Bible

> **Teil:** IV — Minigames
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/minigame-architecture.md (Schnittstellenvertrag), design/gdd/minigame-categories.md (Kategorie-IDs), STP-Plugin-Konvention (`plugins/minigames/*`)

---

## 1. Overview

Dieses Kapitel ist die Bauanleitung für neue Minispiele in Party Arena. Es definiert die Ordnerstruktur und Namenskonvention, das `minigame.json`-Schema mit allen Pflicht- und optionalen Feldern, den Schnittstellenvertrag von `minigame.gd` (die Methoden, die jedes Minispiel implementieren MUSS), den Szenenvertrag von `minigame.tscn`, die verbindliche Design-Checkliste (9 Prüffragen mit konkreten PASS/FAIL-Kriterien) und die Test-Prozedur. Ein Minispiel ist dann "template-konform", wenn es alle Pflichtfelder erfüllt, die Design-Checkliste vollständig besteht und die Test-Prozedur ohne Blocker durchläuft. Ziel ist, dass ein neues Minispiel ohne Architektur-Wissen hinzugefügt werden kann: Die Dateien `minigame.gd`, `minigame.tscn` und `minigame.json` in einen Ordner unter `plugins/minigames/` legen, und der Loader nimmt es beim nächsten Start automatisch in den Pool auf.

## 2. Player Fantasy

Die Fantasie dieses Dokuments richtet sich an das **Entwickler-Team**, nicht an Spielende: Das Template soll sich anfühlen wie eine **klare Bauanleitung mit Qualitätsgarantie** — "Wenn ich mich an diese 9 Prüffragen halte, ist mein Minispiel garantiert ein gutes Party-Arena-Minispiel." Es nimmt dem Design die Angst vor dem leeren Blatt (jede Pflicht-Sektion ist vorgegeben), schützt vor den klassischen Fehlern (Minispiel zu lang, unfair, nicht für 8 Spieler, krankmachende Kamera) und macht die Qualität **prüfbar** statt gefühlt. Für das Team entsteht dadurch ein wiederholbarer, schneller Prozess: Vom Konzept zur spielbaren Plugin-Datei in einem Arbeitsschritt, ohne Rückfragen an das Framework. Die explizite Checkliste und die Test-Prozedur geben jedem Beteiligten (Design, Code, QA) dieselbe Sprache und dieselben Kriterien — ein Minispiel ist entweder konform oder nicht, und das ist objektiv feststellbar.

## 3. Detailed Rules

### 3.1 Ordnerstruktur und Namenskonvention

Jedes Minispiel lebt in einem eigenen Ordner unter `res://plugins/minigames/`.

```
plugins/minigames/<name>/
  minigame.gd          Pflicht — Minigame-Logik (erbt von MinigameBase)
  minigame.tscn        Pflicht — Root-Szene (Wurzelknoten Node3D mit minigame.gd)
  minigame.json        Pflicht — Metadaten (Schema 3.2)
  screenshot.png       Optional — Vorschau 512×288
  translations/        Optional — Lokalisierung (.po/.pot)
  assets/              Optional — minigame-eigene Assets
```

**Namenskonvention:** Der Ordnername ist `snake_case` (durchgehend klein, Unterstriche statt Leerzeichen, keine Umlaute, keine Sonderzeichen außer Unterstrich).

| Gültig | Ungültig |
|--------|----------|
| `muenzregen` | `muenzregen-minigame` (Bindestrich) |
| `balance_akt` | `BalanceAkt` (Großbuchstaben) |
| `sternen_labyrinth` | `sternälabyrinth` (Umlaut) |
| `knoepfchen_druecker` | `knöpfchen_drücker` (Umlaute) |

Der `name` in `minigame.json` muss identisch zum Ordnernamen sein. Diese Konvention ist eine **bewusste Ausnahme** zur GDD-Dateinamenskonvention (kebab-case, `bible-index.md` Abschnitt 3.2): GDD-Dokumente nutzen kebab-case, Minigame-Ordner nutzen snake_case, weil sie der bestehenden STP-Plugin-Struktur folgen und von Code-Tools (Loader, Dateisystem) verarbeitet werden.

### 3.2 `minigame.json` — Schema

Jede Minigame-Datei enthält die folgenden Felder. Das Schema ist die kanonische Struktur:

```json
{
  "name": "minispiel_name",
  "category": "geschicklichkeit|reaktion|puzzle|rechnen|kooperation",
  "players": {"min": 2, "max": 8},
  "duration": 30,
  "description": "Kurze Beschreibung",
  "instructions": "Wie spielt man?",
  "tags": ["tag1", "tag2"]
}
```

**Pflichtfelder:**

| Feld | Typ | Wertebereich | Beschreibung |
|------|-----|--------------|--------------|
| `name` | string | snake_case, 2–30 Zeichen | Eindeutiger Plugin-Name; identisch zum Ordnernamen. |
| `category` | string | `geschicklichkeit` \| `reaktion` \| `puzzle` \| `rechnen` \| `kooperation` | Kategorie-Zuordnung (Kategorien in `minigame-categories.md`). |
| `players.min` | int | 2–8 | Minimale Spielerzahl. |
| `players.max` | int | 2–8, ≥ `players.min` | Maximale Spielerzahl. |
| `duration` | int | 10–30 | Spieldauer der Spielphase in Sekunden; Standard 30, hartes Maximum 30 (Architektur 4.5). |
| `description` | string | 1–2 Sätze | Kurzbeschreibung für Auswahl-/Info-Screens (lokalisiert). |
| `instructions` | string | 1–3 Sätze | Spielanleitung, kindgerecht (lokalisiert); erscheint im Intro und im Info-Screen. |
| `tags` | string[] | 0–10 Einträge | Freie Schlagworte (z. B. `"bewegung"`, `"gedaechtnis"`, `"sammeln"`) für Filter und Balancing. |

**Optionale Erweiterungen (empfohlene Best-Practice-Felder):**

| Feld | Typ | Standard | Beschreibung |
|------|-----|----------|--------------|
| `display_name` | string | `name` | Lokalisierbarer Anzeigename (z. B. `"Münzregen"`). Wird in der UI statt `name` verwendet. |
| `results_mode` | string | `"by_points"` | `"by_points"` (Framework sortiert nach `score`, Gleichstand = gleicher Score) oder `"by_position"` (Minispiel liefert Reihenfolge selbst). Architektur 3.9. |
| `team_mode` | string | `"ffa"` | `"ffa"` (jeder gegen jeden) \| `"coop_all"` (alle gemeinsam) \| `"coop_teams"` (2 Teams). Steuert die Belohnungsart (rewards 3.6). |
| `higher_is_better` | bool | `true` | Ob ein höherer `score` besser ist. Bei `false` ist ein niedrigerer `score` besser (z. B. Distanz-/Fehlerwerte). |
| `controls` | Array | `[]` | Beschreibung der Aktionen für den Info-Screen, STP-kompatibel: `[{"actions": ["action1"], "text": "Beschreibung"}]`. Gültige Aktionen: `up`, `down`, `left`, `right`, `action1`–`action4`, `spacer`. |
| `icon_path` | string | — | Pfad zu einem Icon für die Minigame-Auswahl. |

**Validierungsregeln des Loaders** (Formeln 4.3): Fehlt ein Pflichtfeld oder ist ein Wert außerhalb des Bereichs, wird die Registrierung abgelehnt und das Minispiel erscheint nicht im Pool (Architektur 3.11).

### 3.3 `minigame.gd` — Schnittstellenvertrag

Das Skript erbt von der Minigame-Basisklasse (die von `Node3D` erbt). Das Framework ruft die Methoden in fester Reihenfolge auf (Architektur 3.2). **Jedes Minispiel MUSS die folgenden Methoden implementieren:**

| Methode | Aufruf durch Framework | Pflicht? | Verantwortung des Minispiels |
|---------|------------------------|----------|------------------------------|
| `_ready()` | Nach dem Einfügen in den Szenenbaum | ja | Szene aufbauen, Spawn-Punkte setzen, **alle** Spieler platzieren, Referenzen speichern. |
| `start_game()` | Nach dem Countdown (LOS) | ja | Spielzustand initialisieren, Spiel-Logik starten, anfängliche Ereignisse auslösen. Ab hier ist Input aktiv. |
| `end_game()` | Bei Timer-Ablauf oder `request_end()` | ja | Spiel beenden, finale Wertung einfrieren, weitere Eingaben ignorieren. |
| `get_results()` | Nach `end_game()` | ja | Liefert die Ergebnisse als `Array[Dictionary]` (Schema 4.1). |
| `cleanup()` | Vor dem Freigeben der Szene | ja | Minigame-interne Timer, Signale, Gruppen und Ressourcen entfernen. |

**Zusätzliche, optionale Methoden:**

| Methode | Zweck |
|---------|-------|
| `on_countdown_finish()` | Falls das Minispiel den Countdown-Abschluss für eigene Intro-Animationen braucht (zusätzlich zu `start_game()`). |
| `on_pause_changed(paused)` | Reaktion auf Pause/Resume (z. B. Töne pausieren). |

**Pflicht-Aufruf an das Framework:**

| Aufruf | Zeitpunkt | Zweck |
|--------|-----------|-------|
| `request_end()` | Wenn die Sieg-/Eliminationsbedingung erfüllt ist | Beendet die Spielphase vorzeitig; Framework ruft danach `end_game()` + `get_results()` auf. |

**Verboten für das Minispiel:** Framework-Timer manipulieren, Kamera wechseln, Countdown auslösen, Platzierungslogik überschreiben. Das Framework besitzt all diese Elemente.

**Lesbare Framework-Felder (gesetzt vor `_ready()`):** `player_count` (int, 2–8) und `players` (Array der Spielerzustände in Spielernummer-Reihenfolge; pro Eintrag mindestens `player_id`, `character`, `color`, `controller`).

### 3.4 `minigame.tscn` — Szenenvertrag

| Anforderung | Spezifikation |
|-------------|---------------|
| Wurzelknoten | `Node3D` mit `minigame.gd` als Skript. |
| Spieler-Platzierung | Das Minispiel platziert die Spieler in `_ready()` an eigenen Spawn-Punkten. Empfohlene Konvention: ein Knoten `SpawnPoints` (Node3D) mit Kind-`Marker3D`-Knoten (`Spawn1`, `Spawn2`, …). Das Framework erwartet **keine** festen Pfade; die Platzierung ist Minigame-Verantwortung. |
| Arena-Begrenzung | Die Arena muss eine klare Begrenzung (Wände/Abgrund) haben, damit Spieler nicht entkommen. Für die Vogelperspektive (5–8 Spieler) muss die gesamte Arena in einer Ansicht lesbar sein (Architektur 3.6). |
| Kein eigener Timer/Countdown | Countdown, Timer und Ergebnis-UI liefert das Framework als Overlay. Die `.tscn` enthält diese **nicht** (Ausnahme: Migrations-Minispiele aus STP, siehe 3.8). |
| Gruppen | Spieler-Charaktere in die Gruppe `"players"` aufnehmen, damit Framework- und Debug-Tools sie finden (STP-Konvention). |

### 3.5 Spieler-Integration

- Das Minispiel erhält alle `player_count` Spielerzustände und MUSS für jeden genau eine spielbare Figur erzeugen/platzieren. Fehlt ein Spieler, wird `get_results()` diese Lücke als Fehler melden (Architektur Edge Case 5).
- Jede Figur muss die Signaturfarbe des Spielers tragen (mindestens ein farbiger Ring/Leuchtmarker unter der Figur), damit sie bei 8 Spielern in der Vogelperspektive eindeutig zuordenbar ist (Pfeiler 4, `vision-pillars.md`).
- Die Figur liest Input ausschließlich über die benannten Aktionen `player<n>_up/down/left/right/action1…4` (Architektur 3.7). Keine rohen Geräte-Events.

### 3.6 Design-Checkliste (9 Prüffragen)

Jede Frage hat konkrete PASS/FAIL-Kriterien. Ein Minispiel ist erst dann "design-freigegeben", wenn alle 9 Fragen mit PASS beantwortet sind. Die Kriterien sind so formuliert, dass ein QA-Tester sie ohne Design-Wissen abprüfen kann.

**Frage 1 — Funktioniert mit 2–8 Spielern?**
- PASS, wenn: Das Minispiel mit der minimalen, einer mittleren und der maximalen Spielerzahl (aus `players`) vollständig spielbar ist; keine Spielerzahl zu Abstürzen, hängenden Platzierungen oder unspielbaren Zuständen führt; alle Spieler gleichzeitig teilnehmen (kein "Wartestellungs"-Design, in dem man zuschaut).
- FAIL, wenn: Bei irgendeiner gültigen Spielerzahl ein Spieler keine Rolle hat oder das Minispiel abstürzt.

**Frage 2 — Alle Input-Typen unterstützt?**
- PASS, wenn: Gamepad (Joypad 0–7) und Tastatur (Spieler 1–4 Cluster) für alle Aktionen funktionieren; das Minispiel nur Standard-Aktionen verwendet; die Aktionen im optionalen `controls`-Feld dokumentiert sind.
- FAIL, wenn: Eine Aktion nur per Gamepad oder nur per Tastatur möglich ist, oder eine benötigte Aktion nicht im Standard-Aktionsset existiert.

**Frage 3 — 30-Sekunden-Limit einhaltbar?**
- PASS, wenn: Das Spielziel innerhalb von `duration` Sekunden (Standard 30, max. 30) erreichbar oder entschieden ist; bei Timer-Ablauf eine sinnvolle, vollständige Platzierung aus dem aktuellen Spielstand ableitbar ist; die Spielphase sich nicht künstlich in die Länge zieht.
- FAIL, wenn: Ein Spieler bei Timer-Ablauf "mitten in der Aktion" ohne sinnvolle Platzierung steht, oder das Minispiel mehr als 30 s braucht, um überhaupt einen Zustand zu erreichen, aus dem Platzierungen ableitbar sind.

**Frage 4 — Klare Siegbedingung?**
- PASS, wenn: Ein eindeutiges, objektives Kriterium die Platzierung 1–n bestimmt (höchste Punktzahl, Reihenfolge, Überlebenszeit o. Ä.); zwei unabhängige Tester dieselbe Platzierung aus denselben Spielwerten ableiten; keine subjektive oder Jury-Bewertung vorkommt.
- FAIL, wenn: Die Siegbedingung schwammig ist ("wer am besten gespielt hat") oder Schiedsrichter-Entscheidungen nötig sind.

**Frage 5 — Fair für alle Startpositionen?**
- PASS, wenn: Alle Startpositionen symmetrisch gleichwertig sind (oder die Startreihenfolge zufällig und fair vergeben wird); in 5 Testläufen mit gleicher Spielerzahl keine Startposition statistisch signifikant besser abschneidet (erwartete Punktzahl ± 5 %); kein Spieler einen Vorteil durch Controller-Sitzplatz bekommt.
- FAIL, wenn: Eine Startposition nachweislich im Vorteil ist oder die Fairness nicht überprüfbar ist.

**Frage 6 — Zugänglich für Kinder (ab 6)?**
- PASS, wenn: Die Regel in einem Satz erklärbar ist; die Anleitung (`instructions`) von einem 6-Jährigen mit einmaligem Vorzeigen verstanden wird; die UI große Symbole statt Text verwendet; keine Lese-Pflicht besteht (Ausnahme: Kategorie `rechnen`, dort werden Zahlen groß und mit Symbolen gezeigt); die Schriftgrößen den Vorgaben aus `ui-accessibility.md` entsprechen.
- FAIL, wenn: Mehr als ein Satz Regel nötig ist oder ein 6-Jähriger im Test nach dem Intro nicht ohne Hilfe mitspielen kann.

**Frage 7 — Visuell im Cartoon/Toy-Stil?**
- PASS, wenn: Gesättigte Farben, runde Formen, keine fotorealistischen Texturen; negative Effekte slapstickhaft und komisch inszeniert sind (Staubwolke, Plötz-Geräusch), nie bedrohlich; das Minispiel den 4 Design-Pfeilern aus `vision-pillars.md` folgt.
- FAIL, wenn: Realistische Materialien, düstere Farben oder angsteinflößende Elemente auftauchen.

**Frage 8 — Keine Motion Sickness?**
- PASS, wenn: Keine schnellen Kamerafahrten oder heftiges Kamera-Wackeln vorkommen; die Spieler-Kamera weich nachführt (Ruckelfilter); die Vogelperspektive (5–8 Spieler) ruhig und weitwinklig ist; das Minispiel die "reduzierte Bewegung"-Option aus `ui-accessibility.md` unterstützt (keine zwingenden Kamera-Bewegungen).
- FAIL, wenn: In einem Test mit 5 Testpersonen (davon ≥ 1 anfällig für Kinetose) eine Person Übelkeit meldet.

**Frage 9 — Kamera für 2–4 (Split) und 5–8 (Overhead)?**
- PASS, wenn: Die Arena kompakt genug ist, um in der Vogelperspektive (5–8 Spieler) vollständig und gut lesbar zu sein; alle Spieler-Figuren in beiden Modi sichtbar und durch Farbe unterscheidbar sind; das Minispiel in beiden Modi sinnvoll spielbar ist (kein Design, das nur im Split-Screen funktioniert).
- FAIL, wenn: In der Vogelperspektive Elemente verdeckt oder unlesbar sind, oder das Minispiel bei 5–8 Spielern die Sicht auf das Wesentliche verliert.

### 3.7 Test-Prozedur

Nach der Implementierung durchläuft ein Minispiel zwei Teststufen:

**Stufe A — Unit-Test (automatisiert):**
1. `get_results()` liefert für konstruierte Spielzustände die erwarteten Scores (Schema 4.1); Platzierungsberechnung wird separat als Framework-Test abgedeckt.
2. Schema-Validierung von `minigame.json` (4.3) besteht ohne Warnungen.
3. `request_end()`-Pfad beendet die Spielphase korrekt (kein doppeltes `end_game()`).
4. `cleanup()` hinterlässt keine laufenden Timer oder offenen Verbindungen.

**Stufe B — Spieltest (manuell, min. 2 Personen + Moderator):**
1. **Test mit 2 Spielern:** Vollständiges Durchspielen; Dauer, Verständlichkeit, Fairness und Spaß werden auf einem 1–5-Bogen festgehalten.
2. **Test mit 8 Spielern:** Vollständiges Durchspielen in der Vogelperspektive; Sichtbarkeit aller Spieler, Lesbarkeit der Arena, Timer-Einhaltung.
3. **Checkliste-Abnahme:** Alle 9 Fragen aus 3.6 werden mit PASS/FAIL dokumentiert; jedes FAIL ist ein Blocker bis zur Behebung.
4. **Kinder-Test (falls verfügbar):** Mindestens 1 Kind (6–8 Jahre) spielt einmal mit; Verständlichkeit ohne Hilfe wird notiert (Frage 6).

Die Ergebnisse werden im Minigame-Ordner als `test_report.md` (optional) oder im Review-Log (`design/gdd/reviews/`) festgehalten.

### 3.8 Migration bestehender STP-Minispiele

Die 6 bestehenden STP-Minispiele (`plugins/minigames/*`) laufen mit dem alten Vertrag (eigener `$Countdown`, eigener `$EndTimer`, `$Screen/Time`, STP-`type`-Feld). Für die Aufnahme in Party Arena MUSS jedes Migrations-Minispiel:
1. Die neue `minigame.json`-Struktur (3.2) erhalten (inkl. `category`, `players`, `duration`).
2. Auf den neuen Schnittstellenvertrag (3.3) umgestellt werden (Framework-Countdown/Timer statt eigener Knoten) — oder explizit als "Legacy-Vertrag" deklariert und vom Framework kompatibel behandelt werden (Entscheidung in `technical-fork-strategy.md`).
3. Die Design-Checkliste (3.6) bestehen; nicht konforme Minispiele werden verworfen oder überarbeitet.

## 4. Formulas

### 4.1 Ergebnis-Schema (`get_results`)

`get_results()` liefert ein `Array[Dictionary]` mit genau `player_count` Einträgen:

| Schlüssel | Typ | Beschreibung |
|-----------|-----|--------------|
| `player_id` | int | Spielernummer (1–8). |
| `score` | float | Roh-Score des Spielers (bei `results_mode = "by_points"`; bei `"by_position"` optional, siehe unten). |

Beispiel für 4 Spieler:
`[{"player_id": 1, "score": 12.0}, {"player_id": 2, "score": 9.0}, {"player_id": 3, "score": 12.0}, {"player_id": 4, "score": 3.0}]`

Regeln:
- Jede `player_id` kommt genau einmal vor. Fehlt ein Spieler, ergänzt das Framework ihn mit dem letzten Platz (Architektur Edge Case 5).
- Bei `results_mode = "by_position"` kann `score` weggelassen werden; das Framework erwartet dann die Reihenfolge der Einträge als Platzierungsreihenfolge (Index 0 = Platz 1) und gruppiert **identische** `score`-Werte als Gleichstand, falls `score` doch geliefert wird.

### 4.2 Platzierungsberechnung aus Scores (Framework)

Gegeben Scores `S[i]` (i = 1…n), sortiert absteigend; identische Scores bilden eine Gruppe.

`Platz(g) = a + 1` für eine Gruppe, die die sortierten Indizes `[a, b]` belegt (0-basiert); die Gruppe belegt die Plätze `a+1 … b+1`.

Ausgabe: `[[IDs Platz 1], [IDs Platz 2], …]` (tie-gruppiert). Details und Beispiele in `minigame-architecture.md` Abschnitt 4.2.

### 4.3 Schema-Validierung (Loader)

Ein `minigame.json` ist gültig, wenn alle Bedingungen gelten:

1. `name` ist ein String, nicht leer, snake_case, identisch zum Ordnernamen.
2. `category ∈ {"geschicklichkeit", "reaktion", "puzzle", "rechnen", "kooperation"}`.
3. `players` ist ein Objekt mit `min` und `max`, beide ganzzahlig, `2 ≤ min ≤ max ≤ 8`.
4. `duration` ist ganzzahlig im Bereich `[10, 30]` (Werte außerhalb werden auf den Bereich gedeckelt und gewarnt; fehlendes `duration` → Standard 30).
5. `description` und `instructions` sind nicht-leere Strings.
6. `tags` ist (falls vorhanden) ein Array aus Strings; Einträge sind lowercase.
7. Optionale Felder (`results_mode`, `team_mode`, `higher_is_better`, `controls`) haben gültige Werte; `team_mode = "coop_teams"` erfordert `players.min ≥ 4`.

Erfüllt ein Dokument Bedingung 1–6 nicht, wird es abgelehnt (Architektur 3.11).

## 5. Edge Cases

1. **Fehlendes Pflichtfeld in `minigame.json`:** Loader lehnt ab, protokolliert den Fehler; das Minispiel fehlt im Pool. Kein Crash.
2. **`players.min > players.max`:** Validierungsfehler; Ablehnung.
3. **`name` ≠ Ordnername:** Validierungsfehler; Ablehnung (verhindert doppelte/verwechselbare Plugins).
4. **`team_mode = "coop_teams"` bei `players.min < 4`:** Validierungsfehler; Ablehnung (Team-Koop braucht 2v2 als Minimum).
5. **Fehlende `minigame.gd`-Pflichtmethoden:** Das Framework prüft beim Registrieren, ob `start_game`, `end_game`, `get_results` und `cleanup` existieren; fehlt eine, wird das Minispiel abgelehnt und protokolliert.
6. **`minigame.tscn`-Wurzel ist kein `Node3D`:** Ablehnung (Architektur 3.11).
7. **`get_results()` liefert doppelte `player_id`:** Der zweite Eintrag wird ignoriert, der erste zählt; Protokollierung.
8. **`get_results()` liefert `score = NaN`/`inf`:** Der Spieler wird letzter (Architektur Edge Case 6).
9. **Spawn-Punkt fehlt in der Szene:** Das Minispiel ist selbst für die Platzierung verantwortlich; fehlt ein Spawn-Punkt für einen Spieler, platziert das Minispiel ihn an der letzten bekannten gültigen Position oder meldet einen Fehler, den das Framework abfängt (Abbruch-Platzierung, Architektur 3.12).
10. **Minispiel ruft `request_end()` vor `start_game()`:** Wird ignoriert und protokolliert (Architektur Edge Case 7).
11. **Test ohne 8 Controller:** Die QA-Automation simuliert fehlende Geräte per Input-Injektion; die Tastatur-Cluster für Spieler 1–4 decken einen Teil ab, für 5–8 wird der Numpad-/Remap-Pfad genutzt (Architektur 3.7).
12. **Migrations-Minispiel mit altem Vertrag:** Muss 3.8 durchlaufen; wird es nicht migriert und nicht als Legacy deklariert, lehnt der Loader es ab.
13. **Minispiel mit `duration` = 20 (z. B. Wort-Puzzle):** Gültig; das Framework kürzt die Spielphase entsprechend. Alle anderen Regeln (hartes Max 30) bleiben.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `minigame-template.md` | Art | Verwendung |
|---------------------------------------|-----|------------|
| `design/gdd/minigame-architecture.md` | Peer | Liefert den Schnittstellenvertrag und Lebenszyklus, den das Template als Bauanleitung abbildet. |
| `design/gdd/minigame-categories.md` | Peer | Liefert die gültigen `category`-Werte und die Kategorie-Profile. |
| `design/gdd/minigame-rewards.md` | Peer | Definiert `team_mode`-Konsequenzen (Koop-Auszahlung), die das Template referenziert. |
| `design/gdd/vision-pillars.md` | Peer | Die 4 Design-Pfeiler, auf denen die Checkliste (3.6) aufbaut. |
| `design/gdd/ui-accessibility.md` | Nachgeordnet | Vorgaben zu Schriftgrößen, Farben und reduzierter Bewegung in der Checkliste. |
| `design/gdd/technical-fork-strategy.md` | Peer | Migrations-Regeln für die 6 STP-Minispiele (3.8). |
| `design/gdd/technical-multiplayer.md` | Nachgeordnet | Input-Injektion und Server-Autorität für den Test (Stufe A/B). |
| `.claude/rules/design-docs.md` | Regelwerk | 8-Sektionen-Standard. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `minigame-architecture.md` | Muss das JSON-Schema (3.2) als Validierungsvorschrift im Loader umsetzen. |
| `minigame-categories.md` | Muss die 12 Minispiele als template-konforme Beispiele beschreiben. |
| Alle neuen Minigame-Plugins (Code) | Jedes Plugin MUSS nach diesem Template gebaut sein (3.1–3.5) und die Checkliste (3.6) bestehen. |
| `technical-architecture.md` | Muss den Plugin-Ladevorgang entsprechend dem Szenenvertrag (3.4) einrichten. |
| `qa-lead` / Test-Automation | Nutzt die Test-Prozedur (3.7) und die Validierungsregeln (4.3). |

### 6.3 Bidirektionalität

Das Template ist der "Vertrag nach unten" (vom Framework zu den Plugins): Es übersetzt den Schnittstellenvertrag aus `minigame-architecture.md` in eine Bauanleitung, und jedes konforme Plugin liefert dem Framework die erwartete Schnittstelle zurück. Die Abhängigkeit zu `ui-accessibility.md` ist wechselseitig — die Checkliste erzwingt Zugänglichkeits-Vorgaben, und das Zugänglichkeits-Kapitel muss die Minigame-spezifischen Anforderungen (Bewegung, Lesen) als Pflicht führen.

## 7. Tuning Knobs

Das Template selbst enthält keine Spielbalance-Werte, sondern **Template-Konstanten**, die für alle Minispiele gelten und nur mit Framework-Freigabe geändert werden dürfen:

| Konstante | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|-----------|-----------|------------------|----------|------------|
| `duration`-Bereich | Gate | 10–30 s | 30 s | Erlaubte Spiellänge; entspricht dem harten Zeitlimit (Architektur 4.5). |
| Standard-Aktionsset | Gate | `up/down/left/right/action1–4` | fest | Verbindliche Input-Vokabular; kein Minispiel darf eigene Aktionen erfinden. |
| `players`-Bereich | Gate | min ≥ 2, max ≤ 8 | 2–8 | Gültige Spielerzahl-Deklaration. |
| Kategorie-IDs | Gate | 5 feste Werte | fest | Verhindert Tippfehler/Kategorien-Drift. |
| Mindest-Spielerzahl für `coop_teams` | Gate | ≥ 4 | 4 | Sichert 2v2 als Minimum für Team-Koop. |
| Checklisten-Schwellen (3.6) | Kurve | ± 5 % Fairness, 6-Jahre-Zugänglichkeit | fest | Objektive Abnahme-Kriterien; Änderungen nur mit Design-Freigabe. |

Die eigentlichen Balance-Werte eines Minispiels (Spielraten, Größen, Punktwerte) gehören in die jeweilige Minigame-Datenkonfiguration und die Tuning-Knobs der Kategorien (`minigame-categories.md` Abschnitt 7), nicht ins Template.

## 8. Acceptance Criteria

Ein QA-Tester (oder Review-Gate) kann für **jedes neue Minispiel** folgende Prüfungen ausführen:

1. **Ordnerstruktur:** Der Ordner liegt unter `plugins/minigames/`, heißt `snake_case`, und enthält `minigame.gd`, `minigame.tscn` und `minigame.json`. PASS/FAIL.
2. **Schema-Validierung:** `minigame.json` besteht die Validierungsregeln (4.3) ohne Fehler und ohne Warnungen; `name` == Ordnername. PASS/FAIL.
3. **Loader-Aufnahme:** Nach einem Spielstart erscheint das Minispiel im Pool (`get_count()` erhöht um 1) und ist in einem Test-Minispiel auswählbar. PASS/FAIL.
4. **Pflichtmethoden:** `_ready`, `start_game`, `end_game`, `get_results` und `cleanup` sind implementiert und werden in der korrekten Reihenfolge vom Framework aufgerufen (Spur/Log). PASS/FAIL.
5. **Ergebnis-Schema:** `get_results()` liefert für eine konstruierte Spielsituation ein `Array[Dictionary]` mit genau `player_count` eindeutigen `player_id`s und gültigen `score`s (kein `NaN`, kein `inf`). PASS/FAIL.
6. **Timer-Konformität:** Das Minispiel endet spätestens nach `duration` Sekunden; bei Timer-Ablauf ist eine vollständige Platzierung ableitbar. PASS/FAIL.
7. **Checkliste (3.6):** Alle 9 Prüffragen sind mit PASS dokumentiert; keine Frage ist offen oder FAIL. PASS/FAIL.
8. **Fairness-Messung:** 5 Testläufe mit gleicher Spielerzahl zeigen keine Startposition mit über ± 5 % Abweichung von der erwarteten Punktzahl. PASS/FAIL.
9. **Kinder-Test:** Mindestens 1 Kind (6–8 Jahre) kann nach einmaligem Intro ohne weitere Hilfe mitspielen (Frage 6). PASS/FAIL.
10. **Motion-Sickness-Screening:** 5 Testpersonen (≥ 1 kinetose-anfällig) melden keine Übelkeit (Frage 8). PASS/FAIL.
11. **Spieltest 2 und 8:** Jeweils ein vollständiger Durchlauf mit 2 und mit 8 Spielern erfolgreich; Dauer, Spaß und Verständlichkeit dokumentiert (1–5, Ziel Verständlichkeit ≥ 4). PASS/FAIL.
12. **Erlebbar (Experiential):** Das Minispiel fühlt sich nach Einschätzung von ≥ 80 % der Testgruppe (mindestens 4 Personen) "wie ein Party-Arena-Minispiel" an — kurz, verständlich, bunt, fair, allen Altersgruppen offen. PASS/FAIL.
