# Item-Shop — Party Arena Game Bible

> **Teil:** 2 — Board & Fields
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/game-bible-prompt.md

---

## 1. Overview

Der Item-Shop (Feldtyp ITEM_SHOP) ist die Verkaufsstelle für Items auf dem Board. Jedes Board besitzt exakt 2 Item-Shop-Felder an festen Positionen auf dem Hauptpfad. Jeder Shop bietet pro Runde 3 zufällige Items aus dem Item-Pool (5 Standard-Items) zu festen Preisen an. Das Angebot rotiert NICHT innerhalb einer Runde — es bleibt für alle Spieler identisch, bis es in der Rundenende-Wartung neu generiert wird. Beim Betreten präsentiert ArenaStar (in Händler-Rolle; inselspezifisch auch ein eigener Shop-Charakter möglich) die drei Items mit Icons und Preisen. Der Spieler wählt genau 1 Item oder keins. Kaufbedingungen: genug Münzen und weniger als 3 Items im Inventar. Maximal 3 Items gleichzeitig im Inventar.

## 2. Player Fantasy

Der Item-Shop ist der „Ausrüstungs-Stopp" der Partie: ein einladender Marktstand mit drei glänzend präsentierten Gegenständen, deren Icons sofort verraten, was sie tun. Hier entsteht die strategische Tiefe des Spiels: „Kaufe ich den Glücks-Würfel für mehr Tempo, den Schutzschild als Versicherung oder spare ich für den Stern?" Da das Angebot die ganze Runde für alle gleich bleibt, kann man Preise und Sortiment mit den Mitspielern teilen und planen. Die Player Fantasy ist die eines cleveren Einkäufers, der aus begrenzten Mitteln und einem begrenzten Inventar (3 Slots) das Beste macht.

## 3. Detailed Rules

### 3.1 Anzahl und Position

- Pro Board existieren exakt 2 ITEM_SHOP-Felder.
- Die Positionen sind fest und liegen IMMER auf dem Hauptpfad (nie auf Abzweigungen).
- Referenz-Layout: Index 8 und Index 28 (alternative Beispielposition im Konzept: ebenfalls 8, 28).

### 3.2 Item-Pool und Preise

Der Item-Shop zieht aus dem Pool der 5 Standard-Items zu festen Preisen:

| Item | Preis (Münzen) |
|---|---|
| Glücks-Würfel | 5 |
| Teleporter (Stern-Teleporter) | 8 |
| Schutzschild | 6 |
| Münz-Magnet | 4 |
| Dieb-Handschuh | 10 |

Die Preise sind pro Item fix und werden nicht zufällig variiert. Details zur Wirkung der Items regeln die jeweiligen Item-Kapitel (item-*.md, geplant).

### 3.3 Angebots-Generierung

- Zu Beginn jeder Runde (Rundenende-Wartung der Vorrunde, board-architecture.md 3.12.4c) generiert jeder Item-Shop ein neues Angebot: 3 verschiedene Items, zufällig und ohne Zurücklegen aus dem 5er-Pool.
- Beide Shops generieren unabhängig voneinander (die Angebote dürfen überlappen).
- Das Angebot ist für die gesamte Runde statisch und für ALLE Spieler identisch: Es rotiert weder pro Spieler noch pro Besuch.
- Ein gekauftes Item wird NICHT aus dem Angebot entfernt; jeder Spieler kann dieselben 3 Items kaufen.

### 3.4 Einkaufs-Ablauf

- Landet ein Spieler per Würfelzug auf einem ITEM_SHOP-Feld, präsentiert der Shop-Charakter (Standard: ArenaStar) die 3 Items mit Icons und Preisen.
- Der Spieler wählt genau 1 Item oder „Nichts kaufen".
- Nach dem Kauf (oder der Ablehnung) verlässt der Spieler den Shop; ein erneuter Besuch in derselben Runde ist durch Effekt-Platzierung nicht möglich (diese öffnet keinen Shop).

### 3.5 Kaufbedingungen

Ein Kauf ist gültig, wenn BEIDE Bedingungen erfüllt sind:
1. `coins(p) ≥ preis(item)`, und
2. `inventar_groesse(p) < 3`.

Nach dem Kauf: `coins' = coins − preis(item)`; `inventar_groesse' = inventar_groesse + 1`; das Item wird dem Inventar hinzugefügt.

### 3.6 Inventar-Limit

- Maximal 3 Items gleichzeitig im Inventar.
- Ist das Inventar voll, sind ALLE Käufe deaktiviert; der Shop zeigt eine entsprechende Meldung („Dein Inventar ist voll!"), der Spieler kann nur noch ablehnen.
- Doppelte Items sind erlaubt (bis zur Kapazitätsgrenze); jedes Exemplar zählt als eigener Slot. Die Nutzung eines Items verbraucht genau ein Exemplar.

### 3.7 Unzureichende Münzen

- Kann sich der Spieler KEINES der angebotenen Items leisten, zeigt der Shop eine Meldung; der Spieler verlässt den Shop ohne Kauf. Das Angebot bleibt für die nächsten Besucher bestehen.

### 3.8 Angebots-Rotation

- Innerhalb einer Runde: KEINE Rotation (statisch).
- In der Rundenende-Wartung: Beide Shops generieren ein neues, zufälliges Angebot (3 aus 5, ohne Zurücklegen).

### 3.9 Visuelle und auditive Darstellung

- Visual: Marktstand/Regal mit 3 Item-Icons und Preisschildern; Icons sind eindeutig (Silhouetten-Test, vision-pillars.md).
- Der Shop-Charakter (ArenaStar in Händler-Rolle) zeigt auf die Items; optional pro Insel ein eigener Shop-Charakter (Board-Manifest-Flag).
- Audio-Cue: Kassen-/Kauf-Sound, positiver Bestätigungs-Sound (audio-sfx.md, geplant).

## 4. Formulas

Variablendefinitionen:
- `Pool = {Glücks-Würfel, Teleporter, Schutzschild, Münz-Magnet, Dieb-Handschuh}` (5 Items).
- `preis(item)`: G=5, T=8, S=6, M=4, H=10.
- `Angebot(j, runde)` = Zufallsstichprobe von 3 verschiedenen Items aus Pool, ohne Zurücklegen, gleichverteilt; unabhängig für Shop j.
- `inventar_groesse(p)` — Anzahl der Items im Inventar (0–3).
- `coins(p)` — Münzstand.

Angebots-Formel:
- `Angebot(j, runde) = sample_ohne_zuruecklegen(Pool, 3)`, gleichverteilt über alle `C(5,3) = 10` möglichen 3er-Kombinationen.

Kauf-Formel:
- Kauf gültig ⇔ `coins(p) ≥ preis(item)` UND `inventar_groesse(p) < 3`.
- Nach Kauf: `coins' = coins − preis(item)`; `inventar_groesse' = inventar_groesse + 1`.

Erwartungswerte:
- Preisspanne der Angebote: 4–10 Münzen (je nach gewürfelten Items).
- Durchschnittlicher Angebotspreis (3 Items): `(5+8+6+4+10)/5 = 6,6` Münzen pro Item; erwartete Ausgabe bei „kauf das günstigste" = 4–6 Münzen.

Beispielrechnung:
- Angebot = {Schutzschild (6), Glücks-Würfel (5), Dieb-Handschuh (10)}. Spieler hat 7 Münzen und 2 Items → er kann Schutzschild (→ 1 Münze übrig) oder Glücks-Würfel (→ 2 Münzen übrig) kaufen, nicht den Handschuh.
- Spieler hat 9 Münzen und 3 Items → KEIN Kauf möglich (Inventar voll).

## 5. Edge Cases

1. **Inventar voll:** Alle Käufe deaktiviert; Meldung „Dein Inventar ist voll!"; nur „Nichts kaufen" möglich.
2. **Exakt preiswert:** Kauf gelingt; Münzstand wird 0 (kein negativer Stand).
3. **Beide Shops bieten dasselbe Item an:** Zulässig (unabhängige Ziehung); ein Spieler kann dasselbe Item in beiden Shops kaufen.
4. **Doppelte Items:** Erlaubt bis Slot-Limit; jede Nutzung verbraucht ein Exemplar.
5. **Item-Kauf und volles Inventar durch Ereignis (Item-Regen):** Füllt das Inventar auf 3; danach ist der Shop-Kauf blockiert, bis ein Item genutzt/verloren wurde.
6. **Überqueren eines ITEM_SHOP-Feldes:** Kein Effekt; nur Landungen öffnen den Shop.
7. **Effekt-Platzierung auf ein ITEM_SHOP-Feld (Tausch-Basar etc.):** Kein Shop-Besuch (Regel board-architecture.md 3.11).
8. **AI-Spieler:** Kaufen nach derselben Regel; Entscheidung folgt der AI-Logik (Schwierigkeit), nicht den Menschen-Regeln.
9. **Angebot kurz vor Rundenende:** Das Angebot bleibt bis zur Rundenende-Wartung gültig; ein Spieler, der in der letzten Runde kauft, kauft aus dem aktuellen Angebot.
10. **Kein Item im Angebot erschwinglich:** Spieler verlässt den Shop ohne Kauf; Angebot bleibt bestehen.

## 6. Dependencies

### 6.1 Benötigt von `field-item-shop.md`

| Kapitel/System | Art | Verwendung |
|---|---|---|
| `board-architecture.md` | Voraussetzung | ITEM_SHOP-Typ, Hauptpfad-Platzierung, Rundenende-Wartung (Angebots-Neuauslosung). |
| `item-system.md` (geplant) | Quelle | Item-Definitionen, Inventar, Nutzungslogik. |
| `coin-economy.md` (geplant) | Quelle | Münz-Clamp, Sink-Bilanz (Items als mittlere Sink). |
| `narrative-arena-star.md` (geplant) | Quelle | Shop-Charakter-Dialoge (ArenaStar in Händler-Rolle). |
| `ui-shop.md` (geplant) | System | Angebots-UI, Icons, Preise, Kaufbestätigung. |

### 6.2 Systeme, die von diesem Dokument abhängen

| Kapitel/System | Art der Abhängigkeit |
|---|---|
| `item-luckydice.md`, `item-teleporter.md`, `item-shield.md`, `item-coinmagnet.md`, `item-thiefglove.md` (geplant) | Items werden hier verkauft; Preise und Pool sind Referenz. |
| `field-event.md` | Ereignis „Item-Regen" ergänzt das Inventar und kann den Shop-Kauf blockieren. |
| `coin-economy.md` (geplant) | Bilanziert die Item-Ausgaben als Sink. |
| `ui-board.md` (geplant) | Zeigt Shop-Positionen auf dem Board. |

### 6.3 Bidirektionalität

`board-architecture.md` und `field-event.md` verweisen auf dieses Kapitel; dieses Kapitel verweist zurück. Wechselseitigkeit ist damit hergestellt.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|---|---|---|---|---|
| Preise der 5 Items | Kurve | 2–15 | G5/T8/S6/M4/H10 | Attraktivität und Sink-Bilanz der Items. |
| Angebotsgröße | Kurve | 2–4 | 3 | Auswahl-Fülle, Planbarkeit. |
| Inventar-Limit | Kurve | 1–5 | 3 | Macht der Items, Shop-Umsatz. |
| Angebot pro Runde statisch | Gate | an/aus | an | aus = Rotation pro Spieler (verwirft Planbarkeit). |
| Doppelte Items erlaubt | Gate | an/aus | an | aus = jede Item-Sorte nur einmal im Inventar. |
| Kauf-Limit je Spieler pro Runde | Gate | kein / 1 / 2 | kein | Begrenzt Item-Hortung. |
| Shop-Charakter | Feel | ArenaStar / eigener NPC | ArenaStar | Insel-Flavor, Markenpräsenz. |

## 8. Acceptance Criteria

Ein QA-Tester kann die folgenden Prüfungen ausführen:

1. **Anzahl/Position:** Jedes Board hat exakt 2 ITEM_SHOP-Felder auf dem Hauptpfad (Referenz: 8, 28). PASS/FAIL.
2. **Angebot:** Jeder Shop bietet zu Rundenbeginn 3 verschiedene Items aus dem 5er-Pool an (C(5,3) = 10 mögliche Kombinationen). PASS/FAIL.
3. **Statisches Angebot:** Zwei Spieler, die in derselben Runde denselben Shop besuchen, sehen dasselbe Angebot zu denselben Preisen. PASS/FAIL.
4. **Kauf:** Spieler mit 7 Münzen und 2 Items kauft den Glücks-Würfel (5) → 2 Münzen übrig, 3 Items im Inventar. PASS/FAIL.
5. **Inventar voll:** Spieler mit 3 Items kann keine Items kaufen; Meldung erscheint. PASS/FAIL.
6. **Kein Münzabzug ohne Kauf:** Ablehnung oder „Nichts kaufen" verändert Münzen und Inventar nicht. PASS/FAIL.
7. **Angebots-Rotation:** Nach der Rundenende-Wartung ist das Angebot beider Shops neu gezogen (ggf. identisch möglich, aber Neuauslosung nachweisbar). PASS/FAIL.
8. **Preise:** Angezeigte Preise entsprechen exakt der Tabelle in 3.2. PASS/FAIL.
9. **Effekt-Platzierung:** Tausch-Basar auf ein ITEM_SHOP-Feld öffnet keinen Shop. PASS/FAIL.
10. **Doppelte Items:** Ein Spieler kann dieselbe Item-Sorte zweimal besitzen (2 Slots); Nutzung verbraucht genau ein Exemplar. PASS/FAIL.
