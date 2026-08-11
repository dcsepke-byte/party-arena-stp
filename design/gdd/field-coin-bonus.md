# Münz-Bonus-Feld — Party Arena Game Bible

> **Teil:** 2 — Board & Fields
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/game-bible-prompt.md

---

## 1. Overview

Das Münz-Bonus-Feld (Feldtyp MUENZ_BONUS) ist eine sichere, garantierte Münzquelle: Beim Landen erhält der Spieler einen festen Bonus von 3, 5 oder 8 Münzen — ohne Zufall. Jedes Board besitzt exakt 4 solcher Felder an festen Positionen auf geraden Streckenabschnitten (Hauptpfad-Segmente ohne Abzweigung oder Abzweigungs-Spuren). Der Bonus-Wert wird pro Feld vom Board-Designer festgelegt (3, 5 oder 8). Wird ein Feld in derselben Runde mehrfach betreten (durch Effekt-Platzierung von Ereignissen/Items), erhält der Spieler nur den halben Bonus (abgerundet). Das Feld ist das zentrale Instrument für strategische Routenwahl: „Nehme ich die Abzweigung mit dem Münz-Bonus?".

## 2. Player Fantasy

Das Münz-Bonus-Feld ist der „sichere Hafen" der Partie: ein glitzernder Münz-Haufen, der immer zahlt. Es gibt ein Gefühl von Planbarkeit und Kompetenz — wer die Route mit den Münz-Haufen kennt, kann sein Münzkonto kontrolliert aufbauen und für den Stern sparen. Die Abzweigungen mit Münz-Bonus laden zum Abwägen ein: ein verlässlicher Gewinn gegen eine ungewisse Ereignis-Route. Die Player Fantasy ist die eines klugen Pfadfinders, der die Insel kennt und die sicheren Erträge mitnimmt.

## 3. Detailed Rules

### 3.1 Anzahl und Position

- Pro Board existieren exakt 4 MUENZ_BONUS-Felder.
- Platzierungsregeln (board-architecture.md 3.3): auf geraden Streckenabschnitten; Abstand zu Entscheidungs-/Zusammenführungspunkten ≥ 2 Felder; nicht benachbart zueinander.
- Referenz-Layout: Index 3 (Wert 5), Index 20 (Wert 8), Index 33 (Wert 5, Abzweigung A2), Index 37 (Wert 3, Abzweigung B2).

### 3.2 Bonus-Werte

- Der Bonus-Wert jedes Feldes ist fest im Board-Manifest (`coin_bonus_values`) hinterlegt.
- Zulässige Werte: 3, 5 oder 8 Münzen.
- Der Wert ist pro Feld konstant über die gesamte Partie (kein Zufall, keine Änderung durch Ereignisse/Items).

### 3.3 Auslösung

- Vollbonus: Landet ein Spieler per Würfelzug auf einem MUENZ_BONUS-Feld (erste Landung der Runde auf diesem Feld), erhält er den vollen Bonus `v`.
- Garantiert: Der Bonus wird IMMER ausgezahlt, unabhängig von Münz-Magnet, Glück/Pech oder anderen Modifikatoren (kein Zufall, keine Beeinflussung).
- Überqueren löst KEINEN Bonus aus.

### 3.4 Mehrfach-Betreten in einer Runde (halber Bonus)

- Besuchszähler: Pro Spieler, pro Feld und pro Runde wird gezählt, wie oft er das Feld „betreten" hat (Landung oder Effekt-Platzierung).
- Erste Landung per Würfelzug in der Runde: voller Bonus `v`.
- Jede weitere Landung/Platzierung in derselben Runde: halber Bonus `floor(v/2)`.
- Da ein Spieler pro Runde nur einen Würfelzug hat, entstehen weitere Besuche in derselben Runde ausschließlich durch Effekt-Platzierung (z. B. Tausch-Basar, Rückruf, Item-Effekte).
- Ausnahme-Regel (board-architecture.md 3.11): Effekt-Platzierung auf ein MUENZ_BONUS-Feld löst im Gegensatz zu allen anderen Feldtypen einen (halben) Bonus aus. Wird ein Spieler per Effekt platziert, ohne das Feld zuvor in der Runde per Würfelzug betreten zu haben, gilt ebenfalls `floor(v/2)`.

### 3.5 Zähler-Reset

- Die Besuchszähler werden in der Rundenende-Wartung zurückgesetzt (board-architecture.md 3.12.4d).
- Zu Beginn jeder neuen Runde gilt für jedes Feld wieder: erste Landung = voller Bonus.

### 3.6 Strategische Routenwahl

- Das Feld ist bewusst „langweilig-sicher": keine negativen Effekte, kein Zufall.
- Abzweigungen können Münz-Bonus-Felder enthalten (Referenz: 33, 37), wodurch die Pfadwahl eine echte Abwägung wird (sicherer Bonus vs. 1 Schritt längerer Weg bzw. andere Feldtypen).
- Board-Designer platzieren die 4 Felder so, dass mindestens ein Bonus-Feld auf einem strategischen Entscheidungsweg liegt (Empfehlung, keine Pflicht).

### 3.7 Visuelle und auditive Darstellung

- Visual: Münz-Haufen in Feldgröße mit Glitzer-Partikeln; Größe des Haufens korreliert mit dem Wert (3/5/8).
- Bei Auszahlung: Münz-Zähl-Animation und Klingel-Sound.
- Bei halbem Bonus: dezente Animation, deutlich kleinerer Partikel-Ausstoß (Feedback für „halber Ertrag").

## 4. Formulas

Variablendefinitionen:
- `v ∈ {3, 5, 8}` — fester Bonus-Wert des Feldes (aus `coin_bonus_values`).
- `besuche(p, f)` — Anzahl der Betretungen von Feld f durch Spieler p in der aktuellen Runde.
- `viaWuerfelzug` — wahr, wenn der Besuch durch die Landung des Würfelzugs erfolgt.

Bonus-Formel:
- `bonus = v`, falls `besuche = 1` (also erste Betretung) UND `viaWuerfelzug`.
- `bonus = floor(v/2)`, falls `besuche > 1` ODER `viaWuerfelzug = false` (Effekt-Platzierung).
- `coins' = coins + bonus`.
- Nach jeder Betretung: `besuche' = besuche + 1`.

Erwartungswerte:
- `floor(3/2) = 1`, `floor(5/2) = 2`, `floor(8/2) = 4`.

Beispielrechnung:
- Feld mit v = 5: erste Würfel-Landung → +5. Später in derselben Runde per Tausch-Basar platziert → +2. Gesamt +7 in der Runde.
- Feld mit v = 8: erste Landung → +8; zweite Platzierung → +4; dritte Platzierung → +4 (jede weitere Platzierung halbiert, nicht erneut).

## 5. Edge Cases

1. **Zweite Effekt-Platzierung in derselben Runde:** Auch die zweite Platzierung gibt `floor(v/2)` (kein weiteres Halbieren). `floor(v/2)` ist die Untergrenze pro Besuch.
2. **Effekt-Platzierung vor der Würfel-Landung:** Wird ein Spieler zuerst platziert (halber Bonus) und landet später per Würfelzug auf demselben Feld, ist die Würfel-Landung die zweite Betretung → `floor(v/2)`.
3. **Überqueren:** Kein Bonus (nur Landungen/Platzierungen zählen als Betreten).
4. **Besuchszähler über Runden:** Reset in der Rundenende-Wartung; die erste Landung der neuen Runde gibt wieder den vollen Bonus.
5. **Münz-Magnet:** Verdoppelt den Münz-Bonus NICHT (keine Beeinflussung, analog zu field-luck.md).
6. **Schutzschild:** Hat keinen Effekt auf den Münz-Bonus (nur Gewinn, nichts zu blocken).
7. **Zwei Münz-Bonus-Felder benachbart:** Durch Platzierungsregel ausgeschlossen.
8. **AI-Spieler:** Dieselben Regeln.
9. **Effekt-Platzierung durch Rückruf:** Rückruf zielt auf das Startfeld; trifft also nie ein Münz-Bonus-Feld. Tausch-Basar und zukünftige Effekte können Spieler auf Münz-Bonus-Felder setzen → halber Bonus.

## 6. Dependencies

### 6.1 Benötigt von `field-coin-bonus.md`

| Kapitel/System | Art | Verwendung |
|---|---|---|
| `board-architecture.md` | Voraussetzung | MUENZ_BONUS-Typ, Platzierungsregeln, Rundenende-Reset (3.12.4d), Effekt-Platzierungs-Ausnahme (3.11). |
| `field-event.md` | Abhängig | Tausch-Basar/Rückruf erzeugen Effekt-Platzierungen, die den halben Bonus auslösen. |
| `coin-economy.md` (geplant) | Quelle | Münz-Clamp (nur Gewinne), Faucet-Bilanz. |
| `item-coinmagnet.md` (geplant) | Gegenreferenz | Muss explizit festhalten: kein Verdoppeln des Münz-Bonus. |
| Board-Manifest | System | `coin_bonus_values` (v pro Feld). |

### 6.2 Systeme, die von diesem Dokument abhängen

| Kapitel/System | Art der Abhängigkeit |
|---|---|
| `field-event.md` | Effekt-Platzierungen müssen die halbe-Bonus-Regel kennen. |
| `item-coinmagnet.md` (geplant) | Münz-Magnet-Definition muss die Nicht-Anwendbarkeit bestätigen. |
| `coin-economy.md` (geplant) | Bilanziert die sicheren Erträge (4 Felder, Werte 3/5/8). |
| `ui-board.md` (geplant) | Zeigt Münz-Bonus-Felder und Werte auf dem Board. |

### 6.3 Bidirektionalität

`board-architecture.md` und `field-event.md` verweisen auf dieses Kapitel; dieses Kapitel verweist zurück. Wechselseitigkeit ist damit hergestellt.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|---|---|---|---|---|
| Anzahl Felder `N_MUENZ_BONUS` | Kurve | 3–6 | 4 | Menge der sicheren Münzquellen. |
| Wert-Menge | Kurve | {2,3,4,5,6,8,10} | {3,5,8} | Erträge der sicheren Quellen. |
| Wert je Feld (`coin_bonus_values`) | Kurve | 3/5/8 je Feld | Referenz: 5/8/5/3 | Strategische Attraktivität einzelner Routen. |
| Halbierung | Gate | floor / round / voll | floor | Strenge der Mehrfach-Besuchs-Regel. |
| Effekt-Platzierung zahlt | Gate | nichts / halb / voll | halb | Ausnahme-Regel (board-architecture.md 3.11). |

## 8. Acceptance Criteria

Ein QA-Tester kann die folgenden Prüfungen ausführen:

1. **Anzahl/Position:** Jedes Board hat exakt 4 MUENZ_BONUS-Felder; keines benachbart zu einem Entscheidungs-/Zusammenführungspunkt (Abstand ≥ 2); keine zwei benachbart. PASS/FAIL.
2. **Werte:** Alle `coin_bonus_values` ∈ {3, 5, 8}; Anzeige entspricht dem Wert. PASS/FAIL.
3. **Vollbonus:** Erste Würfel-Landung auf ein Feld mit v=5 → +5 Münzen. PASS/FAIL.
4. **Halber Bonus:** Zweite Betretung in derselben Runde (z. B. Tausch-Basar) → +floor(5/2)=2 Münzen. PASS/FAIL.
5. **Effekt-Platzierung ohne vorherige Landung:** Spieler wird per Tausch-Basar auf ein Feld mit v=8 gesetzt → +4 Münzen. PASS/FAIL.
6. **Reset:** In der Folgerunde gibt die erste Landung wieder den vollen Bonus. PASS/FAIL.
7. **Keine Beeinflussung:** Aktiver Münz-Magnet verdoppelt den Bonus nicht. PASS/FAIL.
8. **Kein Zufall:** 50 Landungen auf dasselbe Feld ergeben immer denselben Bonus (kein Zufallswert). PASS/FAIL.
9. **Überqueren:** Durchqueren eines Münz-Bonus-Feldes zahlt nichts und erhöht den Besuchszähler nicht. PASS/FAIL.
