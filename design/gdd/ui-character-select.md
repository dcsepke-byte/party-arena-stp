# UI-Character-Select — Party Arena Game Bible

> **Teil:** VII — UI/UX
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/ui-overview.md, design/gdd/characters-overview.md (geplant)

---

## 1. Overview

Dieses Kapitel spezifiziert den Charakter-Auswahl-Bildschirm (Screen `CharacterSelect`), der vor jedem Spielstart zwischen Lobby und BoardHUD liegt. Er zeigt die 8 spielbaren Arenians in einem 2-reihigen Raster (4 pro Reihe), die 8 "Player X"-Panels, die sequenzielle Auswahl-Mechanik (Spieler 1 wählt zuerst, dann Spieler 2, usw.), die Zufallsauswahl über den "?"-Slot, den Ready-Ablauf (Host drückt START, wenn alle gewählt haben), den 30-Sekunden-Timer pro Spieler und den Host-Back-Button zur Lobby. Das Kapitel definiert zusätzlich die visuelle Bestätigung bei jeder Wahl und die Deaktivierung gewählter Charaktere. Die Charakter-Daten (Namen, Heimat-Inseln, Beschreibungen, Portraits) stammen aus [characters-overview.md](characters-overview.md) und den Charakter-Kapiteln; dieses Kapitel beschreibt die Darstellung und Interaktion. Alle Regeln aus [ui-overview.md](ui-overview.md) gelten verbindlich.

## 2. Player Fantasy

Die Charakter-Auswahl soll sich anfühlen wie das **Aufstellen seines Spieler-Teams auf einer großen, bunten Bühne**: Jeder der 8 Arenians präsentiert sich in einem eigenen, sich drehenden Porträt, und die Auswahl ist ein kleiner feierlicher Moment — "Spieler 2 hat Nixie gewählt!" wird angekündigt, das gewählte Porträt leuchtet in der Spielerfarbe auf, und die Zuschauer sehen in den 8 Player-Panels, wie sich das Team formiert. Die Fantasy ist: **"Ich wähle meinen Champion für die Party"** — die Auswahl soll persönlich und klar sein, ohne dass man sich durch komplexe Menüs klickt. Für Familien am selben Bildschirm ist entscheidend, dass die Reihenfolge klar kommuniziert wird ("Jetzt ist Spieler 3 dran") und dass niemand versehentlich den Charakter eines anderen überschreibt. Ein Neuling versteht nach dem ersten Durchgang, wie die Auswahl funktioniert (2-Minuten-Test).

## 3. Detailed Rules

### 3.1 Screen-Aufbau

Der `CharacterSelect`-Screen besteht aus:

1. **Titel:** "WÄHLE DEINEN CHARAKTER" (`font_title`), oben zentriert.
2. **Charakter-Raster:** 2 Reihen × 4 Spalten = 8 Charakter-Slots, zentriert in der Bildschirmmitte.
3. **Player-Panels:** 8 "Player X"-Panels. Bei 2–8 Spielern werden nur so viele Panels sichtbar wie Spieler aktiv sind; die Panels liegen unterhalb des Rasters (bzw. am unteren Rand).
4. **Statuszeile:** Zeigt an, wer gerade wählt ("Spieler 3 ist dran!") und den Countdown (3.7).
5. **Hinweisleiste:** Unten: "A = Auswählen · START = Fertig (Host) · B = Zurück (Host)".

### 3.2 Charakter-Slots

Jeder der 8 Slots zeigt:

- **Charakter-Portrait:** 3D-Modell oder 2D-Illustration des Charakters, das sich langsam dreht (eine volle Drehung in 12 s; Formel 4.2). Dreht sich nur, wenn der Slot nicht deaktiviert ist.
- **Charakter-Name** (`font_button`)
- **Charakter-Heimat-Insel** (Icon, z. B. Sonnenstrand-Palme; Icon aus dem Insel-Vokabular, [world-overview.md](world-overview.md))
- **Charakter-Beschreibung** (genau 1 Satz, `font_caption`, `text_secondary`)

**Slot-Zustände:**

| Zustand | Darstellung |
|---------|-------------|
| Verfügbar | Portrait dreht sich, vollfarbig, Slot normal |
| Fokussiert (aktueller Wähler) | Fokus-Rahmen ([ui-overview](ui-overview.md) 3.7) + leichte Vergrößerung (105 %) |
| Gewählt (durch einen Spieler) | Slot ausgegraut (40 % Deckkraft), Portrait stoppt, Überlagerung "GEWÄHLT" + Spielerfarben-Rahmen des wählenden Spielers |
| Zufalls-Slot "?" | Porträt = großes "?" mit Würfel-Animation (leichte Rotation), Beschreibung = "Zufälliger Charakter" |

### 3.3 Player-Panels

- Für jeden aktiven Spieler gibt es ein "Player X"-Panel (X = Spielernummer 1–8, in Spielerfarbe).
- **Leerzustand:** Das Panel zeigt "WÄHLE CHARAKTER" mit einem leeren Portrait-Platzhalter.
- **Gewählt-Zustand:** Das Panel zeigt das Portrait des gewählten Charakters, den Charakternamen und eine Haken-Animation (200 ms).
- **Aktiver Wähler:** Das Panel des aktuell wählenden Spielers pulsiert (Rahmen-Opazität 0,6–1,0, 1 Hz; Formel 4.3) und zeigt "IST DRAN".
- Panels sind **nicht fokussierbar** (reine Anzeige).

### 3.4 Auswahl-Mechanik (sequenziell)

1. **Reihenfolge:** Die Spieler wählen nacheinander in Spieler-Reihenfolge (P1 zuerst, dann P2, …, dann P8; nur aktive Spieler).
2. **Steuerung des Cursors:** Nur der aktuell wählende Spieler steuert den Cursor (Gamepad des Spielers bzw. Tastatur). Die Cursor-Bewegung folgt den expliziten Fokus-Nachbarn ([ui-overview](ui-overview.md) 3.7).
3. **Auswahl:** `ui_accept` (A / X / A) auf einem verfügbaren Slot wählt den Charakter. Der Slot wird deaktiviert (grau, "GEWÄHLT"), das Player-Panel füllt sich, und die Bestätigung erscheint.
4. **Bestätigungs-Anzeige:** Über dem Raster erscheint zentral: "Spieler [N] hat [CHARAKTER] gewählt!" (`font_subtitle`), 2 s lang, mit ArenaStar-Kommentar ("[Charakter] — tolle Wahl!").
5. **Weiterschaltung:** Nach der Wahl wechselt die Auswahl automatisch zum nächsten aktiven Spieler (P2 …). Es gibt keine Möglichkeit, die Reihenfolge zu überspringen oder zurückzugehen.
6. **Zufalls-Slot "?":** Der "?"-Slot ist der 9. Slot, rechts neben dem Raster (bzw. nach Slot 8). Wählt ihn ein Spieler, wird ihm ein zufälliger noch verfügbarer Charakter zugewiesen (gleichverteilt über die verbleibenden Charaktere; Formel 4.1). Der Spieler sieht das Ergebnis sofort im Player-Panel.

### 3.5 Ready und Spielstart

- **Bedingung:** Das Spiel startet erst, wenn **alle aktiven Spieler** einen Charakter gewählt haben.
- **Host-Bestätigung:** Der Host drückt START (`ui_ready`), wenn alle gewählt haben, um in den BoardHUD zu wechseln. Der START-Hinweis erscheint erst, wenn alle gewählt haben; vorher zeigt die Statuszeile "Warte auf Spieler [N]".
- **Autostart nicht vorgesehen:** Es gibt keinen automatischen Start, sobald alle gewählt haben — der Host muss bestätigen (Kontrolle über den Startzeitpunkt).
- **Ready-Feedback:** Beim Drücken von START (wenn berechtigt) spielt `ui_click` und der Screen blendet 300 ms zum BoardHUD über.

### 3.6 Timer (30 Sekunden pro Spieler)

- **Zeitbudget:** Jeder aktive Spieler hat **30 s** für seine Auswahl (Countdown beginnt, sobald er an der Reihe ist; Formel 4.4).
- **Anzeige:** Ein Countdown-Ring oder -Zahl im Player-Panel des aktuellen Wählers; ab 10 s wird die Zahl rot und tickt hörbar (letzte 5 s: `ui_counter`-Ticks).
- **Zeitablauf:** Endet die Zeit, wird dem Spieler automatisch ein **zufälliger** noch verfügbarer Charakter zugewiesen (gleiche Verteilung wie beim "?"-Slot). Die Bestätigung erscheint mit dem Zusatz "(automatisch)".
- **Kein Abbruch:** Der Timer kann nicht angehalten oder zurückgesetzt werden; er läuft auch, wenn der Cursor auf einem gewählten (deaktivierten) Slot steht.

### 3.7 Zurück zur Lobby

- **Host:** Der Host kann mit `ui_cancel` (B) zur Lobby zurückkehren — aber nur, solange **noch nicht alle** gewählt haben und **kein Spiel gestartet** ist.
- **Nicht-Host:** Andere Spieler können nicht zurück; sie sehen nur den Hinweis, dass der Host zurückgehen kann.
- **Bestätigung:** `ui_cancel` öffnet einen `ConfirmDialog` "Zurück zur Lobby? Die Auswahl geht verloren." Erst die Bestätigung verlässt den Screen.
- **Nach Spielstart:** Ist das Spiel gestartet (BoardHUD aktiv), ist eine Rückkehr nicht mehr möglich (nur über Pause → Hauptmenü).

## 4. Formulas

### 4.1 Zufallsauswahl-Verteilung

`P(c) = 1 / R_verfügbar` für jeden noch verfügbaren Charakter `c`

- `R_verfügbar` = Anzahl der noch nicht gewählten Charaktere (8 − Anzahl der bereits gewählten).
- Beispiel: Vor der ersten Wahl `R_verfügbar = 8` → `P = 1/8` je Charakter; nach 3 Wahlen `R_verfügbar = 5` → `P = 1/5`.
- Akzeptanz: Die Zufallsauswahl wählt nie einen bereits gewählten Charakter; die Verteilung ist über die verfügbaren Charaktere gleichverteilt (statistische Prüfung über 100 Auswahl-Durchläufe, Toleranz ± 5 % je Charakter).

### 4.2 Portrait-Rotation

`θ(t) = 2π × (t / 12 s)`

- `θ(t)` = Drehwinkel des Charakter-Portraits (Radiant), eine volle Umdrehung pro 12 s.
- Akzeptanz: Drehung nur bei verfügbaren Slots; gewählte Slots stoppen die Drehung (fixiertes Standbild).

### 4.3 Aktiver-Wähler-Puls

`O_p(t) = 0,6 + 0,4 × (0,5 + 0,5 × sin(2π × 1,0 × t))`

- `O_p` = Opazität des Rahmens des aktiven Player-Panels (0,6–1,0), 1 Hz.
- Akzeptanz: Genau ein Player-Panel pulsiert; der Rahmen ist immer sichtbar (`O ≥ 0,6`).

### 4.4 Timer-Formel

`T_rest(t) = 30 s − (t − t_start)` mit `T_rest ≥ 0`

- `t_start` = Zeitpunkt, zu dem der Spieler an der Reihe ist, `t` = aktuelle Zeit.
- Akzeptanz: Bei `T_rest = 0` erfolgt automatisch die Zufallszuweisung (4.1); die Anzeige zeigt nie negative Werte.

## 5. Edge Cases

1. **Nur 2 Spieler:** Die Panels P1 und P2 sind aktiv; P3–P8 sind unsichtbar. Die Auswahl wechselt von P1 zu P2 und ist danach vollständig (der Timer für P2 startet nach P1s Wahl).
2. **Spieler wählt während des Timers eines anderen:** Der Timer läuft nur für den aktuellen Wähler; andere Spieler haben keine Eingabe (kein Parallel-Cursor). Wird ein zweites Gamepad gedrückt, während P1 wählt, hat das keine Wirkung (Eingaben von Nicht-Wählern werden verworfen).
3. **Letzter verfügbarer Charakter:** Ist nur noch ein Charakter übrig, kann der letzte Wähler nur diesen wählen (oder den "?"-Slot, der denselben Charakter liefert). Der Slot bleibt bis zur Wahl fokussierbar; die Bestätigung erscheint normal.
4. **Timer läuft ab, während der Cursor auf "GEWÄHLT"-Slot steht:** Die automatische Zufallszuweisung ignoriert die Cursor-Position; der Spieler erhält einen zufälligen verfügbaren Charakter, nicht den fokussierten (der ja gewählt sein kann).
5. **Host verlässt während laufender Auswahl:** Nur vor Abschluss aller Wahlen möglich (3.7). Bei Online-Spielen ([technical-multiplayer.md](technical-multiplayer.md)) wird das Spiel abgebrochen und die Lobby geschlossen; die anderen Spieler sehen den Verbindungs-Dialog.
6. **Charakter bereits von einem anderen gewählt (Online-Race):** In Online-Partien könnte ein anderer Spieler denselben Charakter anwählen. Die Zuweisung erfolgt serverseitig in Spieler-Reihenfolge; verliert ein Spieler das Rennen, erscheint der Hinweis "Dieser Charakter ist bereits gewählt!" und der Cursor bleibt auf dem Slot (kein automatisches Weiterspringen).
7. **Spieleranzahl ändert sich beim Zurückgehen zur Lobby:** Die Auswahl wird vollständig verworfen; beim erneuten Öffnen beginnt die Auswahl wieder bei P1 mit allen 8 Charakteren.
8. **Sehr lange Namen:** Charakternamen und Beschreibungen werden auf die Slot-Breite begrenzt (Beschreibung kürzt mit "…"); die vollständige Beschreibung erscheint als Tooltip beim Fokus des Slots (300 ms Verzögerung, [ui-board](ui-board.md)-Konvention).
9. **Zeitablauf in der letzten Sekunde:** Bei `T_rest ≤ 1 s` kann ein `ui_accept` noch ausgeführt werden, wenn es vor dem Ablauf registriert wird; ist die Wahl bereits automatisch erfolgt, wird der Tastendruck verworfen (kein Doppel-Charakter).
10. **Alle 8 Spieler wählen denselben Zufalls-Slot nacheinander:** Jede Zufallswahl konsumiert einen Charakter; nach der 8. Wahl sind alle Charaktere verteilt, es gibt keine Kollision.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `ui-character-select.md` | Art | Verwendung |
|-----------------------------------------|-----|------------|
| `design/gdd/ui-overview.md` | Dach | Liefert Tokens, Fokus-Regeln, ControlHelper, UI-Sound und Overlay-Ebenen. |
| `design/gdd/characters-overview.md` | Quelle | Liefert die 8 Charaktere (Namen, Heimat-Inseln, Beschreibungen, Portraits) und die Fähigkeiten-Philosophie (keine asymmetrischen Board-Vorteile). |
| `design/gdd/character-*.md` | Quelle | Liefert je Charakter die Portrait-Animation und Heimat-Insel-Icons. |
| `design/gdd/glossary.md` | Peer | Definiert Begriffe wie "Arenian", "Heimat-Insel", "Signaturfarbe". |
| `design/gdd/ui-hud.md` | Nachgeordnet | Übernimmt die gewählten Charaktere und Spielerfarben als Portrait-/Marker-Quelle. |
| `design/gdd/technical-multiplayer.md` | Nachgeordnet | Muss die sequenzielle Auswahl bei Online-Partien serverseitig absichern (Edge Case 6). |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `design/gdd/ui-hud.md` | Verwendet die gewählten Charaktere als Portraits und 3D-Marker. |
| `design/gdd/characters-overview.md` | Muss die Charakter-Daten so liefern, dass der Screen sie 1:1 darstellt (keine UI-seitige Definition von Charaktereigenschaften). |
| `design/gdd/core-loop.md` | Startet nach der Bestätigung des Hosts in den BoardHUD. |
| `design/gdd/audio-ui.md` / `audio-sfx.md` | Muss Auswahl-, Bestätigungs- und Timer-Sounds liefern. |

### 6.3 Bidirektionalität

Die Charakter-Auswahl hängt von den Charakter-Daten ab ([characters-overview.md](characters-overview.md)) und liefert dem Spiel die konkrete Spieler-Charakter-Zuordnung. Die Charakter-Kapitel müssen die Portraits und Dreh-Animationen spezifizieren, die hier angezeigt werden; umgekehrt muss dieser Screen jedes neue Charakter-Kapitel automatisch darstellen können (kein Hardcoding der 8 Slots).

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Timer pro Spieler | Gate | 10–90 s | 30 s | Zeitbudget pro Wahl; länger = entspannter, kürzer = zügiger |
| Portrait-Rotationsdauer | Feel | 6–24 s | 12 s | Drehgeschwindigkeit der Charakter-Portraits |
| Fokus-Vergrößerung | Feel | 100–115 % | 105 % | Hervorhebung des fokussierten Slots |
| Bestätigungs-Anzeigedauer | Feel | 1–4 s | 2 s | Dauer der "Spieler N hat X gewählt!"-Anzeige |
| Puls-Frequenz (aktiver Wähler) | Feel | 0,5–2,0 Hz | 1,0 Hz | Tempo des aktiven Player-Panel-Pulses |
| Puls-Minimum-Opazität | Feel | 0,4–0,8 | 0,6 | Sichtbarkeits-Untergrenze des aktiven Panels |
| Gewählt-Dimmung | Feel | 20–60 % Deckkraft | 40 % | Abdunklung gewählter Slots |
| Rot-Signal ab | Feel | 5–15 s | 10 s | Countdown-Schwelle, ab der die Zahl rot wird |

## 8. Acceptance Criteria

Ein QA-Tester kann folgende Prüfungen ausführen:

1. **Raster:** Das Raster zeigt 8 Charakter-Slots (2 × 4) plus den "?"-Slot; jeder Slot zeigt Portrait (drehend), Name, Heimat-Insel-Icon und 1-Satz-Beschreibung. PASS/FAIL.
2. **Player-Panels:** Für jede aktive Spielerzahl `P ∈ [2,8]` sind genau `P` Player-Panels sichtbar; leere zeigen "WÄHLE CHARAKTER", gewählte das Portrait + Namen. PASS/FAIL.
3. **Sequenzielle Auswahl:** Die Wahl erfolgt in Reihenfolge P1 → P2 → …; nur der aktuelle Wähler steuert den Cursor; nach der Wahl wechselt die Auswahl automatisch weiter; die Bestätigung "Spieler [N] hat [CHARAKTER] gewählt!" erscheint 2 s. PASS/FAIL.
4. **Slot-Deaktivierung:** Gewählte Charaktere werden ausgegraut (40 %), das Portrait stoppt, und die Überlagerung "GEWÄHLT" + Spielerfarben-Rahmen erscheint; sie sind nicht mehr wählbar. PASS/FAIL.
5. **Zufalls-Slot:** Der "?"-Slot weist einen gleichverteilten zufälligen, noch verfügbaren Charakter zu (statistische Prüfung über 100 Durchläufe, Toleranz ± 5 %); das Ergebnis erscheint sofort im Player-Panel. PASS/FAIL.
6. **Timer:** Jeder Wähler hat 30 s; ab 10 s wird der Countdown rot; bei 0 erfolgt automatische Zufallszuweisung mit dem Zusatz "(automatisch)". PASS/FAIL.
7. **Ready/Start:** START bewirkt erst etwas, wenn alle aktiven Spieler gewählt haben; vorher zeigt die Statuszeile "Warte auf Spieler [N]". PASS/FAIL.
8. **Zurück zur Lobby:** Nur der Host kann mit `ui_cancel` (mit ConfirmDialog) zurück, solange nicht alle gewählt haben und kein Spiel gestartet ist; Nicht-Hosts können nicht zurück. PASS/FAIL.
9. **Online-Race:** Bei Online-Partien wird ein doppelt gewählter Charakter serverseitig verhindert; der verlierende Spieler sieht "Dieser Charakter ist bereits gewählt!". PASS/FAIL.
10. **Erlebbar (Experiential):** Eine Testperson (Neuling) versteht nach einem eigenen Wahl-Durchgang die Reihenfolge und die Bestätigung ohne Anleitung; der 2-Minuten-Test ist bestanden. PASS/FAIL.
