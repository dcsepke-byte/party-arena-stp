# Start-Feld — Party Arena Game Bible

> **Teil:** 2 — Board & Fields
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/game-bible-prompt.md

---

## 1. Overview

Das Start-Feld (Feldtyp START, Index 0) ist der Ursprung und das Ziel jeder Runde auf dem Board. Alle Spieler beginnen die Partie auf diesem Feld. Es ist zugleich der Runden-Marker der Schleife: Wer das Startfeld überquert oder exakt erreicht, hat eine komplette Runde (einen Lap) absolviert und erhält dafür einen Münz-Bonus. Das Startfeld ist bewusst „effektfrei" gegenüber Ereignis-Triggerlogik — es löst keine Feldtyp-Effekte aus, zählt nicht als Ziel für zufällige Feld-Auswahl und ist die Bühne für die Regelerklärung durch ArenaStar zu Spielbeginn. Pro Board existiert exakt ein Startfeld an Position 0.

## 2. Player Fantasy

Das Startfeld ist das große, immer wiederkehrende Portal/Tor der Insel: ein landmarkenhaftes, unverwechselbares Bauwerk im Insel-Thema (z. B. ein Muschel-Tor am Sonnenstrand), durch das jeder Umlauf führt. Es soll sich anfühlen wie „das Zuhause" der Partie: Hier geht die Reise los, hier wird jede Runde belohnt, hier wartet ArenaStar mit einem Willkommensgruß. Durchquert man das Tor, hat man sichtbar „eine Runde geschafft" — ein befriedigendes, kleines Erfolgserlebnis, das den Fortschritt über die 8–10 Runden spürbar macht.

## 3. Detailed Rules

### 3.1 Position und Zählung

- Das Startfeld ist Feld 0 (Index 0) und hat IMMER den Typ START.
- Es existiert genau 1 Startfeld pro Board.
- Das Startfeld ist Teil des Hauptpfads; `prev` von Feld 0 ist Feld 31 (letztes Hauptpfad-Feld), `next` von Feld 31 ist Feld 0 (Schleife). Feld 0 hat genau einen `next`-Eintrag (Feld 1).

### 3.2 Spielbeginn

- Alle Spieler starten auf Feld 0. Ihre Platzierung erfolgt nach dem Versatz-Schema aus board-architecture.md (3.9), deterministisch nach Sitzplatzindex.
- Die initiale Platzierung ist KEINE Landung: Sie löst weder Lap-Bonus noch Exakt-Landungs-Bonus noch irgendeinen Feld-Effekt aus.
- ArenaStar steht zu Spielbeginn auf dem Startfeld und erklärt die Regeln (einmalig pro Partie). Die Erklärung ist ein kurzer, überspringbarer Dialog.
- Der Rundenzähler beginnt bei Runde 1.

### 3.3 Lap-Definition

- Ein Lap (Umlauf) ist absolviert, wenn ein Spieler im Rahmen eines Würfelzugs Feld 0 überquert (Zwischenschritt) oder exakt erreicht (Landefeld).
- Voraussetzung: Der Spieler hat seit Partiebeginn mindestens einen Bewegungsschritt ausgeführt (die initiale Platzierung zählt nicht als Lap).
- Der Lap-Zähler `lapN(Spieler)` wird bei jeder Überquerung/Erreichung um 1 erhöht.

### 3.4 Lap-Bonus

- Beim Überqueren ODER exakten Erreichen des Startfeldes nach einem vollendeten Lap erhält der Spieler `COINS_LAP` Münzen (Standard 5).
- Der Bonus wird sofort bei der Überquerung gutgeschrieben (noch während der Bewegung), nicht erst am Zugende.
- Der Bonus wird pro Überquerung/Erreichung genau einmal gewährt — auch dann, wenn ein Würfelzug das Startfeld mehrfach passieren würde (bei Verdopplern: zählt weiterhin als 1 Bonus pro Lap).
- Der Bonus kann per Tuning auf 0 gesetzt werden (dann „passiert nichts" beim Überqueren).

### 3.5 Exakt-Landungs-Bonus

- Landet ein Spieler exakt auf Feld 0 (Feld 0 ist das letzte Feld seines Würfelzugs) UND hat mindestens einen Lap vollendet, erhält er zusätzlich zum Lap-Bonus `COINS_LAND_EXACT` Münzen (Standard 3).
- Gesamtbonus bei exakter Landung: `COINS_LAP + COINS_LAND_EXACT` (= 8 im Standard).

### 3.6 Startfeld als „Nicht-Feld" für Event-Trigger

- Das Startfeld löst bei Landung/Überquerung keinerlei Feldtyp-Effekte aus (kein Sternen-/Item-Shop, kein Ereignis, kein Glück/Pech, kein Münz-Bonus, keine Minispiel-Kategorie).
- Zufällige Feld-Auswahl (z. B. Münzsturm-Pickups, „zufälliges Feld" durch Effekte) schließt das Startfeld aus, sofern der Effekt nicht explizit das Startfeld nennt (z. B. das Ereignis „Rückruf").
- Das Startfeld kann niemals ein Münz-Pickup beherbergen.

### 3.7 Effekt-Platzierung auf das Startfeld

- Wird ein Spieler durch ein Item oder Ereignis auf Feld 0 platziert (z. B. „Rückruf", „Tausch-Basar", Rückwärtsbewegung), erhält er KEINEN Lap-Bonus und KEINEN Exakt-Landungs-Bonus (Regel: Effekt-Platzierung löst keine Feld-Effekte aus, board-architecture.md 3.11).
- Der Lap-Zähler wird durch eine Effekt-Platzierung NICHT erhöht.

### 3.8 Mehrere Spieler auf dem Startfeld

- Mehrere Spieler können gleichzeitig auf Feld 0 stehen; sie werden nach dem Versatz-Schema versetzt dargestellt (board-architecture.md 3.9).
- Es gibt keine Interaktion, keine Blockierung und keine Reihenfolge-Konflikte zwischen Spielern auf dem Startfeld.

### 3.9 Visuelle und auditive Darstellung

- Visual: großes Portal/Tor im Insel-Thema; klar erkennbar als „Anfang/Ziel" (Feld 0 trägt das Start-Icon).
- Beim Überqueren: kurze Durchschreite-Animation und ein „Runde geschafft"-Hinweis (non-blocking).
- ArenaStar: begrüßt beim ersten Überqueren jeder Partie mit einer kurzen Bemerkung; eine Wiederholung je Spieler ist optional (Tuning).
- Audio-Cue: Portal-/Fanfaren-Sound beim Überqueren (siehe audio-sfx.md, geplant).

## 4. Formulas

Variablendefinitionen:
- `COINS_LAP` — Münzbonus pro vollendetem Lap (Standard 5, Bereich 0–10).
- `COINS_LAND_EXACT` — Zusatzbonus bei exakter Landung auf Feld 0 nach mindestens 1 Lap (Standard 3, Bereich 0–5).
- `lapN(p)` — Lap-Zähler des Spielers p (Ganzzahl, startet bei 0).
- `coins(p)` — Münzstand des Spielers p.

Bonus-Formeln:
- Überquerung: `coins' = max(0, coins + COINS_LAP)`, `lapN += 1`.
- Exakte Landung nach ≥ 1 Lap: `coins' = max(0, coins + COINS_LAP + COINS_LAND_EXACT)`, `lapN += 1`.
- Exakte Landung beim Spielbeginn (Runde 1, keine Bewegung): keine Formel, keine Bonuszahlung.
- Effekt-Platzierung auf Feld 0: keine Bonuszahlung, `lapN` unverändert.

Erwartungswerte:
- Standard-Gesamtbonus bei exakter Landung: `5 + 3 = 8`.
- Über eine Partie mit 8 Runden erzielt ein Spieler typischerweise 8 × 5 = 40 Münzen aus Lap-Boni, zuzüglich Exakt-Landungs-Boni (Häufigkeit ca. 1/10 der Würfe → ca. 3–8 Münzen zusätzlich).

Beispielrechnung:
- Spieler mit 3 Münzen überquert Feld 0 im 3. Lap → `3 + 5 = 8`.
- Spieler mit 12 Münzen landet exakt auf Feld 0 im 2. Lap → `12 + 5 + 3 = 20`.
- Spieler mit 2 Münzen wird durch „Rückruf" auf Feld 0 platziert → `2` (keine Änderung).

## 5. Edge Cases

1. **Initiale Platzierung:** Löst keinerlei Bonus aus (weder Lap noch Exakt-Landung). Die Partie beginnt ohne Münzzahlung fürs „Stehen auf dem Start".
2. **Runde 1, exakte Landung auf Feld 0:** Ist mathematisch unmöglich (maximaler Würfelwert 10 < 40 Felder). Falls durch einen zukünftigen Effekt doch eintretbar: kein Bonus, da noch kein Lap vollendet.
3. **Effekt-Platzierung auf Feld 0:** Kein Lap-Bonus, kein Exakt-Landungs-Bonus, kein Feld-Effekt; `lapN` unverändert.
4. **Verdoppelter Würfel (Würfel-Verdoppler):** Verdoppelt die Schrittzahl, nicht den Lap-Bonus. Auch bei mehrfachem Passieren im selben Zug: genau 1 Lap-Bonus pro Lap.
5. **Mehrere Spieler überqueren Feld 0 in derselben Runde:** Jeder erhält unabhängig seinen Bonus in Zugreihenfolge.
6. **Landung auf Feld 0 durch Münzsturm-Pickup:** Start kann keine Pickups beherbergen; der Fall ist ausgeschlossen.
7. **Lap-Bonus und gleichzeitiges Überqueren eines anderen Feldes:** Der Lap-Bonus wird im Moment der Überquerung gewährt; der Lande-Effekt des Zielfeldes wird am Zugende separat aufgelöst (Reihenfolge board-architecture.md 3.11).
8. **AI-Spieler:** Dieselben Regeln; keine Sonderbehandlung.

## 6. Dependencies

### 6.1 Benötigt von `field-start.md`

| Kapitel/System | Art | Verwendung |
|---|---|---|
| `board-architecture.md` | Voraussetzung | Index 0, Schleife `M31 → M0`, Versatz-Schema, Lande-Regel. |
| `dice-movement.md` (geplant) | Quelle | Bewegungsablauf, in dem der Lap-Bonus ausgelöst wird. |
| `coin-economy.md` (geplant) | Quelle | Münz-Clamp (`max(0, …)`), Faucet-Bilanz. |
| `narrative-arena-star.md` (geplant) | Quelle | Regelerklärung und Begrüßungsdialoge. |
| Ereignis-System (`field-event.md`) | Abhängig | „Rückruf" zielt auf das Startfeld (muss die Bonus-Ausnahme kennen). |
| Sitzplatz-/Kamera-System | System | Versetzte Darstellung mehrerer Spieler auf Feld 0. |

### 6.2 Systeme, die von diesem Dokument abhängen

| Kapitel/System | Art der Abhängigkeit |
|---|---|
| `core-loop.md` (geplant) | Nutzt den Lap-Bonus als Runden-Rhythmus (Mikro-/Meso-Loop). |
| `ui-hud.md` (geplant) | Zeigt den Lap-Zähler / „Runde geschafft"-Hinweis. |
| `audio-sfx.md` (geplant) | Spielt Portal-/Fanfaren-Cue beim Überqueren. |
| `field-coin-bonus.md` | Konsistenz: Auch der Münz-Bonus gewährt bei Effekt-Platzierung nur halben Wert (gleiche Ausnahme-Logik). |

### 6.3 Bidirektionalität

`board-architecture.md` verweist auf dieses Kapitel (START-Feld, Lap-Bonus); dieses Kapitel verweist zurück auf `board-architecture.md`. Damit ist die Abhängigkeit wechselseitig abgedeckt.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|---|---|---|---|---|
| `COINS_LAP` | Kurve | 0–10 | 5 | Münz-Zufluss pro Umlauf; steuert Tempo der Stern-Ökonomie. |
| `COINS_LAND_EXACT` | Kurve | 0–5 | 3 | Belohnung für präzises Landen; Anreiz, den Würfelwurf zu planen. |
| Lap-Bonus aktiv | Gate | an/aus | an | Aus = Startfeld „passiert nichts" beim Überqueren. |
| Exakt-Landungs-Bonus aktiv | Gate | an/aus | an | Aus = nur noch Lap-Bonus. |
| ArenaStar-Begrüßung je Lap | Feel | nie / einmal pro Spieler / jede Runde | einmal pro Spieler | Präsenz des Moderators, Dialog-Dichte. |
| Begrüßungsmünze (Spielstart) | Kurve | 0–5 | 0 | Optionales Startgeld auf dem Startfeld (Standard: keine). |

## 8. Acceptance Criteria

Ein QA-Tester kann die folgenden Prüfungen ausführen:

1. **Spielbeginn:** Alle Spieler stehen zu Rundenbeginn auf Feld 0; die initiale Platzierung zahlt keine Münzen aus und zeigt keinen Bonus-Hinweis. PASS/FAIL.
2. **Überquerungs-Bonus:** Ein Spieler, der Feld 0 während eines Zuges überquert, erhält +5 Münzen und der Lap-Zähler erhöht sich um 1. PASS/FAIL.
3. **Exakt-Landungs-Bonus:** Ein Spieler, der exakt auf Feld 0 landet (nach ≥ 1 Lap), erhält +8 Münzen (5+3). PASS/FAIL.
4. **Kein Bonus bei Effekt-Platzierung:** „Rückruf" auf Feld 0 → keine Münzzahlung, Lap-Zähler unverändert. PASS/FAIL.
5. **Kein Ereignis-Trigger:** Eine Landung auf Feld 0 öffnet keinen Shop, löst kein Ereignis, kein Glück/Pech, keinen Münz-Bonus und keine Minispiel-Kategorie aus. PASS/FAIL.
6. **Zufalls-Auswahl ohne Startfeld:** Münzsturm platziert keine Pickups auf Feld 0; zufällige Feld-Auswahl liefert nie Feld 0 (außer explizit). PASS/FAIL.
7. **Mehrere Spieler:** 8 Spieler auf Feld 0 → alle werden gemäß Versatz-Schema dargestellt, keine Kollision. PASS/FAIL.
8. **Münz-Clamp:** Ein Spieler mit 0 Münzen erhält durch Lap-/Exakt-Bonus korrekt positive Münzen (kein negativer Stand möglich). PASS/FAIL.
