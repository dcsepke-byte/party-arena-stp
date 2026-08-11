# Würfel & Bewegung — Party Arena Game Bible

> **Teil:** I — Core Game
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/bible-index.md

---

## 1. Overview

Dieses Kapitel spezifiziert das Würfel- und Bewegungssystem des Brettspiels: den Standard-Würfel (1–6), den Item-Würfel Glücks-Würfel (1–10), die Würfel-Animation durch ArenaStar, die Feld-für-Feld-Bewegung inklusive Tempo und Beschleunigung, die Pfadwahl an Abzweigungen und Kreuzungen, die Regeln für erzwungene Rückwärtsbewegung sowie das Verhalten am Startfeld (Umlauf-Zählung). Das System ist die mechanische Grundlage jedes Zugs im [Kern-Loop](core-loop.md): Das Wurfergebnis bestimmt die Schrittzahl, die Bewegung übersetzt sie in sichtbaren Fortschritt auf dem 40-Felder-Brett, und Pfadwahl gibt den Spielern Autonomie über ihre Route. Dieses Kapitel liefert die präzisen Regeln und Formeln, damit ein Programmierer Würfeln, Bewegung und Pfadwahl ohne Rückfragen implementieren kann. Die Feld-Effekte der Zielfelder selbst werden nicht hier, sondern in den Feld-Kapiteln ([board-architecture](board-architecture.md), `field-*.md`) definiert.

## 2. Player Fantasy

Der Würfelwurf ist das **Herzklopfen-Moment** der Partie (MDA: Sensation). Der Spieler drückt die Taste, ArenaStar wirft den Würfel, und für 2,5 Sekunden ist alles möglich — die Zahl bestimmt, ob man den Sternen-Shop erreicht, in ein Ereignis stolpert oder knapp am Item-Shop vorbeizieht. Die Bewegung erzeugt **sichtbare Kontrolle** (Autonomie): Der Charakter läuft Feld für Feld, und an Abzweigungen entscheidet der Spieler selbst, welchen Weg er nimmt — die Karte wird zur taktischen Entscheidung, nicht nur zum Zufalls-Pfad. Die Beschleunigungs-Taste gibt ein Gefühl von **Tempo und Können** (Kompetenz): Wer schnell entscheidet, hält das Spiel im Fluss. Der Glücks-Würfel (1–10) ist die **Wette** (Sensation + Challenge): Ein hoher Wurf katapultiert nach vorn, ein niedriger Wurf kostet eine wertvolle Runde — die Unsicherheit ist der Reiz, und genau deshalb kostet er Münzen im Item-Shop. Die zentrale emotionale Verheißung: **"Jeder Wurf könnte alles verändern"** — kombiniert mit der Gewissheit, dass die eigene Wege-Wahl den Zufall in eine Richtung lenkt.

## 3. Detailed Rules

### 3.1 Würfel-Arten

1. **Standard-Würfel:** Würfelt eine ganze Zahl aus der Gleichverteilung `{1, 2, 3, 4, 5, 6}`. Jeder Wert hat die Wahrscheinlichkeit 1/6. Dies ist der Default-Würfel jedes Zugs, sofern kein Item einen anderen Würfel vorgibt.
2. **Glücks-Würfel (Item):** Würfelt eine ganze Zahl aus der Gleichverteilung `{1, 2, ..., 10}`. Jeder Wert hat die Wahrscheinlichkeit 1/10. Er ersetzt für genau einen Zug den Standard-Würfel, wenn er vor dem Würfeln aktiviert wird (Item-Kosten: 5 Münzen; Details in [item-luckydice](item-luckydice.md)).
3. **Weitere Würfel-Modifikatoren:** Zukünftige Items (z. B. Additions- oder Fixwürfel) sind möglich, müssen aber denselben Vertrag erfüllen: Sie liefern ein Wurfergebnis aus einem definierten Intervall ganzer Zahlen und ersetzen bzw. modifizieren den Standard-Wurf für genau einen Zug. Sie sind in `item-*.md` zu spezifizieren.
4. **Kein Würfel im Spiel erlaubt ein Ergebnis von 0 oder negativ.** Das Minimum jedes zugelassenen Würfels ist 1.

### 3.2 Würfel-Animation und Ergebnis

1. Der aktive Spieler bestätigt den Wurf (Standard-Taste: Bestätigen/Springen). Vor dem Bestätigen kann ein Würfel-Item aktiviert werden (Nutzungs-Zeitpunkt "vor dem Würfeln", Vertrag in [item-system](item-system.md)).
2. **Ergebnis-Festlegung:** Sobald der Wurf bestätigt ist, legt der Spielleiter (Server; lokal der Host) das Ergebnis anhand der Würfel-Verteilung fest. Die Animation ist rein kosmetisch und kann das Ergebnis nicht mehr ändern.
3. **Ablauf:** ArenaStar führt eine Wurf-Animation aus (Dauer 2,5 s Standard): Er wirft den Würfel, der Würfel rollt/kullert sichtbar, dann bleibt er stehen. Das Ergebnis wird groß eingeblendet und von ArenaStar angesagt (z. B. "Vier!"). Während der Animation ist keine weitere Eingabe nötig; sie kann per Taste übersprungen werden (das Ergebnis steht fest).
4. Nach der Ansage beginnt automatisch die Bewegungs-Phase.

### 3.3 Bewegung: Feld für Feld

1. **Schritt-Prinzip:** Der Charakter bewegt sich in **Einzelschritten** (Feld für Feld) entlang der Kanten des Brett-Graphen. Es gibt kein "Springen" zum Zielfeld; jeder Schritt ist sichtbar.
2. **Schritt-Dauer:** Jeder Schritt dauert standardmäßig `t_Schritt = 0,3 s`. Der Spieler kann durch **Gedrückthalten der Beschleunigungs-Taste** (A/Enter bzw. Bestätigen) die Dauer auf `t_Schritt,beschl = 0,12 s` verkürzen. Die Beschleunigung wirkt für alle Schritte des Zugs, solange die Taste gehalten wird; sie hat keinen Einfluss auf Pfadwahl-Entscheidungen (diese können nicht "übersprungen" werden).
3. **Unterbrechung:** Die Bewegung kann vom Spieler nicht abgebrochen, angehalten oder vorzeitig beendet werden. Die volle gewürfelte Schrittzahl wird immer zurückgelegt (Ausnahme: erzwungene Stopps durch Felder/Items sind nicht vorgesehen; die Bewegung ist atomar).
4. **Richtung:** Die Bewegungsrichtung ist standardmäßig die Vorwärtsrichtung des Brett-Graphen (die Kanten sind gerichtet: jedes Feld hat eine Liste ausgehender Nachbarfelder). An Abzweigungen/Kreuzungen wählt der Spieler die Richtung (3.5).
5. **Zusammenstoß:** Es gibt keine Kollision zwischen Charakteren. Mehrere Charaktere können dasselbe Feld betreten und dort stehen.
6. **Ziel:** Nach exakt der gewürfelten Schrittzahl endet die Bewegung auf dem Zielfeld; danach wird dessen Feld-Effekt ausgelöst ([core-loop](core-loop.md) Abschnitt 3.3).

### 3.4 Startfeld und Umlauf

1. Das Startfeld (Feld 0) ist ein normales Feld: Es kann durchlaufen oder als Zielfeld erreicht werden. Beim Durchlaufen wird **nicht** angehalten.
2. **Umlauf-Zählung:** Überquert ein Charakter das Startfeld in Vorwärtsrichtung (d. h. von Feld 39 nach Feld 0 bzw. über die Umlauf-Grenze), wird der Umlauf-Zähler dieses Spielers um 1 erhöht. Der Zähler ist rein statistisch relevant (Statistik-Bildschirm, Bonus-Kategorie Vielläufer in [star-economy](star-economy.md) / [victory-conditions](victory-conditions.md)).
3. **Kein automatischer Umlauf-Bonus:** Das Überqueren des Startfelds vergibt standardmäßig keine Münzen (Design-Entscheidung; ein Umlauf-Bonus ist nur als Tuning-Knob in [core-loop](core-loop.md) vorgesehen).
4. **Rückwärts-Umlauf:** Bei erzwungener Rückwärtsbewegung (3.6) zählt das Rückwärts-Überqueren des Startfelds den Umlauf-Zähler **nicht** hoch (nur Vorwärts-Umläufe zählen).

### 3.5 Abzweigungen und Kreuzungen (Pfadwahl)

1. **Definition:** Eine **Abzweigung** ist ein Feld mit 2 ausgehenden Kanten; eine **Kreuzung** ein Feld mit 3 oder mehr ausgehenden Kanten. Die Kanten-Topologie wird pro Brett in den Brett-Daten definiert ([board-architecture](board-architecture.md)).
2. **Auslösung:** Erreicht der Charakter während der Bewegung ein Abzweigungs-/Kreuzungsfeld und sind noch Schritte übrig, **pausiert die Bewegung** und der Spieler wählt die Richtung:
   - Die gültigen Richtungen werden als Pfeile über den ausgehenden Kanten eingeblendet (UI-Vertrag in [ui-board](ui-board.md)).
   - Der Spieler wählt mit den Richtungstasten (Pfeiltasten/Stick) die gewünschte Kante und bestätigt mit der Bestätigungs-Taste.
   - **Timeout:** Trifft der Spieler innerhalb von `t_Timeout = 5 s` keine Wahl, wird der **Standard-Pfad** gewählt. Jedes Abzweigungs-/Kreuzungsfeld definiert in den Brett-Daten genau einen Standard-Pfad (die bevorzugte Route laut Board-Design). Der Standard-Pfad wird im UI dezent markiert.
3. **Lande-Effekt auf Abzweigung:** Wird ein Abzweigungs-/Kreuzungsfeld als **Zielfeld** erreicht (Schrittzahl erschöpft), wird zuerst der Feld-Effekt des Felds ausgelöst. Die Pfadwahl für den nächsten Zug ist **nicht** sofort fällig; sie wird beim nächsten Zug am Beginn der Bewegungs-Phase nachgeholt (3.5.4).
4. **Pfadwahl zu Zugbeginn:** Steht ein Spieler zu Beginn seiner Bewegungs-Phase auf einem Abzweigungs-/Kreuzungsfeld, erscheint zuerst die Richtungs-Wahl, danach bewegt er sich entlang der gewählten Kante um die gewürfelte Schrittzahl. Kann auf ein Abzweigungs-/Kreuzungsfeld nur mit 1 Schritt erreicht werden, wird ebenfalls erst gewählt und dann der Schritt ausgeführt.
5. **Mehrfach-Abzweigungen in einem Zug:** Passiert ein Zug mehrere Abzweigungen, wiederholt sich die Wahl bei jeder Abzweigung einzeln (Pause → Wahl → weiter). Jede Wahl ist unabhängig.
6. **Rückwärts an Abzweigungen:** Rückwärtsbewegung (3.6) folgt nie einer Spielerwahl; sie folgt der kanonischen Rückwärtskante des Felds.

### 3.6 Rückwärtsbewegung (nur erzwungen)

1. **Grundsatz:** Rückwärtsbewegung ist im Normalzustand **nicht** möglich. Sie tritt ausschließlich auf, wenn ein Ereignis oder Item sie explizit erzwingt (z. B. "Gehe 3 Felder zurück").
2. **Ausführung:** Rückwärtsbewegung ist ebenfalls Feld-für-Feld mit derselben Schritt-Dauer und Beschleunigungs-Option. Es gibt **keine** Pfadwahl: Jedes Feld definiert in den Brett-Daten genau eine kanonische Rückwärtskante (den "Haupt"-Vorgänger). Die Rückwärtskante ist eindeutig; bei Feldern mit mehreren möglichen Vorgängern legt das Board-Design die kanonische Kante fest.
3. **Umlauf:** Rückwärtsbewegung kann das Startfeld in Rückwärtsrichtung überqueren; dies zählt keinen Umlauf (3.4.4). Das 40-Felder-Brett ist ein Ring, es gibt kein "unter 0": Rückwärts von Feld 0 führt zu Feld 39.
4. **Zielfeld:** Die erzwungene Rückwärtsbewegung endet nach der angegebenen Schrittzahl auf einem Feld; der Feld-Effekt dieses Felds wird normal ausgelöst. Verbleibt die erzwungene Bewegung auf einem Abzweigungs-/Kreuzungsfeld, gilt 3.5.3 analog.

### 3.7 Item-Modifikationen

1. **Nutzungs-Zeitpunkt:** Würfel-modifizierende Items werden **vor** dem Würfeln aktiviert ([item-system](item-system.md)). Nach dem Wurf ist eine Aktivierung für denselben Zug nicht mehr möglich.
2. **Glücks-Würfel:** Ersetzt den Standard-Würfel für diesen Zug durch die Gleichverteilung 1–10 (3.1.2). Er wird beim Wurf verbraucht.
3. **Wechselwirkung:** Wirken mehrere Würfel-Modifikatoren gleichzeitig (nur durch Items möglich, die nicht verbraucht werden), gilt: Der zuletzt aktivierte Modifikator gewinnt. Es addieren sich keine Würfel (kein 2W6-System).
4. **Item-Kosten und Verfügbarkeit** sind in [coin-economy](coin-economy.md) und [item-system](item-system.md) definiert.

### 3.8 Timing und Eingabe

1. **Eingabe ohne harten Timer:** Im lokalen Spiel gibt es keinen Zwangs-Timer für Würfeln und Pfadwahl; die Spieler entscheiden in eigenem Tempo (Rücksicht auf Mitspieler ist sozialer Vertrag, kein System-Zwang).
2. **Optionaler Zug-Timer (Online):** Ist der Zug-Timer aktiv (Tuning-Knob in [core-loop](core-loop.md)), gilt: Nach Ablauf des Timers in der Roll-Phase wird automatisch mit dem Standard-Würfel gewürfelt; nach Ablauf bei einer Pfadwahl wird der Standard-Pfad gewählt. Der Timer läuft pro Zug, nicht pro Phase.
3. **Sprung über Animationen:** Würfel-, Bewegungs- und Pfadwahl-Animationen können übersprungen werden; der Spielzustand ändert sich dadurch nicht.

## 4. Formulas

### 4.1 Wurf-Verteilungen

**Standard-Würfel:** `X ~ U{1..6}`, diskrete Gleichverteilung.
- `P(X = k) = 1/6` für `k ∈ {1,...,6}`.
- Erwartungswert `E[X] = (1+6)/2 = 3,5`.
- Varianz `Var[X] = (6² - 1)/12 = 35/12 ≈ 2,917`; Standardabweichung `σ ≈ 1,708`.

**Glücks-Würfel:** `Y ~ U{1..10}`, diskrete Gleichverteilung.
- `P(Y = k) = 1/10` für `k ∈ {1,...,10}`.
- Erwartungswert `E[Y] = (1+10)/2 = 5,5`.
- Varianz `Var[Y] = (10² - 1)/12 = 99/12 = 8,25`; Standardabweichung `σ ≈ 2,872`.

**Vergleich:** Der Glücks-Würfel hat einen um 2,0 höheren Erwartungswert, aber eine deutlich höhere Streuung (`σ` um 68 % höher). Er lohnt sich, wenn der Spieler ein großes Feld vor sich hat (z. B. Sternen-Shop in 5–8 Feldern Entfernung) und Risiko eingehen will.

### 4.2 Bewegungs-Dauer

`T_Bewegung = X × t_Schritt + Σ_J t_Junction`

- `X` = Wurfergebnis.
- `t_Schritt` = 0,3 s (Standard) bzw. 0,12 s (mit Beschleunigung).
- `J` = Anzahl der in diesem Zug überquerten Abzweigungen/Kreuzungen.
- `t_Junction` = Entscheidungszeit je Abzweigung, `0–5 s` (Timeout), typisch 2 s.

**Beispiel:** Wurf 4, 1 Abzweigung, keine Beschleunigung: `T = 4 × 0,3 + 2 = 3,2 s`. Mit Beschleunigung: `T = 4 × 0,12 + 2 = 2,48 s`.

**Erwartungswert (Standard-Würfel, typisches Brett):** `E[T_Bewegung] = 3,5 × 0,3 + P_J × 2`, wobei `P_J` die Wahrscheinlichkeit ist, im Zug eine Abzweigung zu überqueren (boardspezifisch, typisch ≈ 0,3). → `E[T_Bewegung] ≈ 1,05 + 0,6 = 1,65 s`.

### 4.3 Wahrscheinlichkeit, den Sternen-Shop zu erreichen

Die Wahrscheinlichkeit, von einem Feld im Abstand `d` (1–6 Schritte, Standard-Würfel) den aktiven Sternen-Shop zu erreichen, ist:

`P(Erfolg | d) = Anzahl der Wurfergebnisse k ∈ {1..6} mit k = d, geteilt durch 6`.

- Bei `d ≤ 6`: genau 1 Treffer → `P = 1/6 ≈ 16,7 %`.
- Bei `d = 0` (bereits auf dem Feld): Kauf in der Feld-Effekt-Phase (Stern-Kauf-Regeln in [star-economy](star-economy.md)).
- Bei `d > 6`: `P = 0` (kein Standard-Wurf erreicht das Feld direkt); nur mit Glücks-Würfel möglich.

**Beispiel:** Der Sternen-Shop ist 5 Felder entfernt. Mit dem Standard-Würfel: `P = 1/6`. Mit dem Glücks-Würfel (1–10): `P = 1/10` für `k = 5`, aber zusätzlich kann ein höherer Wurf (6–10) den Shop überlaufen — der Shop wird nur bei exakter Landung erreicht (kein "Drüber-Zählen"). Die Gesamtwahrscheinlichkeit, den Shop exakt zu treffen, bleibt bei `1/10`; der Glücks-Würfel erhöht also die Reichweite, nicht die Trefferwahrscheinlichkeit auf kurze Distanz.

## 5. Edge Cases

1. **Wurf 1:** Der Charakter bewegt sich genau 1 Feld. Gilt 1.3.3: voller Schritt wird ausgeführt, Feld-Effekt des Zielfelds wird ausgelöst.
2. **Abzweigung als letztes Feld (Schritte erschöpft):** Feld-Effekt zuerst; Richtungswahl wird auf den nächsten Zug verschoben (3.5.3). Der Spieler wird beim nächsten Zug vor der Bewegung gefragt.
3. **Zwei Abzweigungen direkt hintereinander:** Nach der ersten Wahl läuft der Charakter 1 Schritt auf das nächste Abzweigungsfeld; falls noch Schritte übrig sind, folgt sofort die zweite Wahl (3.5.5).
4. **Spieler wählt bei Timeout nicht:** Standard-Pfad wird genommen (3.5.2). Der Standard-Pfad muss in den Brett-Daten für jedes Abzweigungs-/Kreuzungsfeld eindeutig definiert sein; ein Feld ohne Standard-Pfad ist ein Datenfehler (Blockierendes Acceptance-Criteria).
5. **Erzwungene Rückwärtsbewegung von Feld 0:** Führt zu Feld 39 (Ring); kein Unterlauf. Die Schrittzahl wird vollständig ausgeführt.
6. **Erzwungene Rückwärtsbewegung über eine Abzweigung:** Es gibt keine Wahl; die kanonische Rückwärtskante wird genommen. Falls die kanonische Rückwärtskante nicht definiert ist (Datenfehler), wird die Bewegung um 1 Schritt verkürzt und der Fehler ins Log geschrieben (Defensive; kein Spielabbruch).
7. **Glücks-Würfel aktiviert, aber Zug wird übersprungen (Item/Event):** Unwahrscheinlich, aber möglich (z. B. ein Ereignis überspringt den Zug). Der Glücks-Würfel gilt als verbraucht, sobald er aktiviert wurde, unabhängig davon, ob der Wurf ausgeführt wird (Verbrauchs-Regel in [item-luckydice](item-luckydice.md)).
8. **Beschleunigungs-Taste wird während Pfadwahl gehalten:** Kein Effekt auf die Wahl; die Beschleunigung gilt nur für die Schritt-Zeit, nicht für die Entscheidungszeit.
9. **Mehrere Spieler überqueren dieselbe Abzweigung im selben Zug:** Unabhängig voneinander; jede Pfadwahl gilt nur für den ziehenden Spieler. Keine Blockade.
10. **Würfelergebnis > verbleibende Felder bis Runden-Ende des Bretts (Umlauf):** Der Charakter läuft über den Ring weiter (Feld 39 → Feld 0); der Umlauf wird gezählt (3.4.2). Es gibt kein "Brett-Ende".
11. **Item-Würfel mit Intervall außerhalb 1–6:** Zukünftige Würfel-Items müssen ein Intervall ganzer Zahlen mit Minimum ≥ 1 definieren. Die Bewegungs-Engine ist intervall-agnostisch; nur die Balance-Formeln (4.1) sind je Würfel neu zu berechnen.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments (benötigte Systeme)

| System/Kapitel | Art | Status | Verwendung |
|---|---|---|---|
| `design/gdd/core-loop.md` | Peer | Geschrieben | Definiert die Zug-Phase (Roll → Move → Feld-Effekt), in die dieses System eingebettet ist. |
| `design/gdd/board-architecture.md` | Quelle | Geplant (noch nicht geschrieben) | Liefert die Feld-Verkettung, ausgehende Kanten, Abzweigungen, Kreuzungen und kanonische Rückwärtskanten. |
| `design/gdd/item-luckydice.md` | Quelle | Geplant (noch nicht geschrieben) | Definiert den Glücks-Würfel (1–10, Kosten 5 Münzen, Verbrauch). Dieses Kapitel übernimmt den Wurf-Vertrag. |
| `design/gdd/item-system.md` | Peer | Geplant (noch nicht geschrieben) | Definiert Nutzungs-Zeitpunkt ("vor dem Würfeln") und Verbrauch von Würfel-Items. |
| `design/gdd/ui-board.md` | Konsument | Geplant (noch nicht geschrieben) | Zeigt Richtungs-Pfeile, Standard-Pfad-Markierung und Würfel-Ergebnis. |
| `design/gdd/technical-multiplayer.md` | Konsument | Geplant (noch nicht geschrieben) | Synchronisiert den Server-entschiedenen Wurf und die Bewegungs-Schritte. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|---|---|
| `core-loop.md` | Zug-Dauer-Formeln (4.2) nutzen `t_Schritt` und Abzweigungs-Timeout dieses Dokuments. |
| `star-economy.md` | Treffer-Wahrscheinlichkeit für den Sternen-Shop (4.3) hängt von Würfel-Verteilungen ab. |
| `catch-up.md` | Nutzt die Distanz-/Umlauf-Zählung (z. B. Kategorie Vielläufer), um Aufhol-Bonus-Sterne zu vergeben. |
| `victory-conditions.md` | Statistik-Bildschirm zeigt zurückgelegte Felder und Umläufe aus diesem System. |
| `technical-data-structures.md` | Muss Wurf-Ergebnis, Pfad-Wahl und Bewegungs-Ziel persistieren können. |

### 6.3 Design-Entscheidungen (dokumentierte Klärungen)

1. **Glücks-Würfel-Klärung (5 / 1–10):** Das Game-Konzept notiert "Glücks-Würfel (5, 1–10)" und der bible-index `item-luckydice.md` präzisiert: **Kosten 5 Münzen, Wurfbereich 1–10**. Die Formulierung "5 fest, oder 1–10" wird daher als Kostenangabe (5) + Wurfbereich (1–10) interpretiert. Es gibt **keinen** separaten Fixwert-Würfel mit Ergebnis 5. Soll ein solcher später gewünscht sein, ist er als neues Item in `item-*.md` zu spezifizieren und hier zu ergänzen.
2. **Kein Drüber-Zählen:** Ein höheres Wurfergebnis als die Distanz zum Shop führt nicht zum "Drüber-Zählen" auf den Shop; nur exaktes Landen zählt (siehe [star-economy](star-economy.md) Abschnitt 3.2).
3. **Rückwärtskanten:** Jedes Feld braucht genau eine kanonische Rückwärtskante; dies ist eine harte Datenanforderung an `board-architecture.md`.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|---|---|---|---|---|
| Schritt-Zeit `t_Schritt` | Feel | 0,15–0,6 s | 0,3 s | Bewegungstempo; direkt sichtbar, starkes Feel-Signal. |
| Schritt-Zeit beschleunigt | Feel | 0,05–0,3 s | 0,12 s | Stärke der Beschleunigungs-Taste; muss deutlich schneller sein als Standard. |
| Würfel-Animation | Feel | 1,5–4,0 s | 2,5 s | Spannungsaufbau; zu lang = zäh, zu kurz = kein Kribbeln. |
| Abzweigungs-Timeout `t_Timeout` | Gate | 2–10 s | 5 s | Wartezeit vor Standard-Pfad; beeinflusst Partie-Pacing (mit core-loop abstimmen). |
| Standard-Würfel-Intervall | Kurve | `{1..6}` (Fix) | `{1..6}` | Grundverteilung; Änderung verschiebt alle Balance-Formeln (4.1, 4.3). Nicht ohne Design-Freigabe ändern. |
| Glücks-Würfel-Intervall | Kurve | `{1..8}` bis `{1..12}` | `{1..10}` | Risiko-Belohnung des Item-Würfels; mit [coin-economy](coin-economy.md) (Item-Preis 5) abstimmen. |
| Pfadwahl verfügbar | Gate | An/Aus | An | Bei "Aus" ignorieren Spieler Abzweigungen (Standard-Pfad); für Kinder-/Einfach-Modus gedacht. |
| Umlauf-Bonus | Kurve | 0–10 Münzen | 0 | Optionaler Anreiz pro Umlauf (abgestimmt mit core-loop-Knob). |

## 8. Acceptance Criteria

Ein QA-Tester oder CI-Hook kann die folgenden Prüfungen ausführen (PASS/FAIL):

1. **Verteilungen:** Über je 6000 Würfe (Standard- und Glücks-Würfel) weicht die relative Häufigkeit jedes Wertes um weniger als 10 % vom Erwartungswert ab (Standard: 1/6 ≈ 16,7 %; Glücks: 1/10 = 10 %). PASS/FAIL.
2. **Feld-für-Feld:** Die Bewegung zeigt jeden Einzelschritt an; es gibt keinen Sprung zum Zielfeld. PASS/FAIL (Sichtprüfung).
3. **Schrittzahl-Treue:** Nach einem Wurf `k` endet der Charakter exakt auf dem `k`-ten Feld entlang des gewählten Pfads (bei erzwungener Rückwärts: `k`-tes Feld entlang der Rückwärtskette). PASS/FAIL (Autotest mit definiertem Brett).
4. **Pfadwahl:** An jeder Abzweigung mit verbleibenden Schritten pausiert die Bewegung und die gewählte Richtung wird genommen. Bei Timeout (5 s) wird der Standard-Pfad gewählt. PASS/FAIL.
5. **Zugbeginn-Pfadwahl:** Steht ein Charakter zu Zugbeginn auf einer Abzweigung, erscheint die Wahl vor der Bewegung. PASS/FAIL.
6. **Rückwärtsbewegung:** Erzwungene Rückwärtsbewegung folgt immer der kanonischen Rückwärtskante, wählt nie selbst, und endet mit Feld-Effekt. Rückwärts von Feld 0 endet auf Feld 39. PASS/FAIL.
7. **Umlauf-Zählung:** Vorwärts-Überqueren des Startfelds erhöht den Umlauf-Zähler um 1; Rückwärts-Überqueren nicht. PASS/FAIL.
8. **Kein Drüber-Zählen:** Ein Wurf, der über das Ziel hinausgeht, endet auf dem Feld nach dem Ziel — nicht auf dem Ziel. Der Shop wird nur bei exakter Landung erreicht. PASS/FAIL.
9. **Beschleunigung:** Gedrückthalten der Taste verkürzt die Schritt-Dauer messbar auf den konfigurierten Wert; die zurückgelegte Strecke bleibt identisch. PASS/FAIL (Timer-Messung).
10. **Würfel-Item:** Nach Aktivierung des Glücks-Würfels liefert der nächste Wurf Werte aus {1..10} mit korrekter Verteilung; das Item wird genau einmal verbraucht. PASS/FAIL.
11. **Daten-Vollständigkeit:** Jedes Abzweigungs-/Kreuzungsfeld des Bretts hat genau einen definierten Standard-Pfad; jedes Feld hat genau eine kanonische Rückwärtskante. Ein Validierungs-Skript über die Brett-Daten meldet 0 Fehler. PASS/FAIL.
