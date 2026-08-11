# Glück/Pech-Feld — Party Arena Game Bible

> **Teil:** 2 — Board & Fields
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/game-bible-prompt.md

---

## 1. Overview

Das Glück/Pech-Feld (Feldtyp GLUECK_PECH) ist ein reines Risiko-Feld: Beim Landen wird ein zufälliger Münz-Effekt ausgelöst — mit 60 % Wahrscheinlichkeit Glück (Gewinn), 30 % Pech (Verlust) und 10 % neutral (kein Effekt oder +1 Münze). Jedes Board besitzt exakt 3 solcher Felder. Wichtig: Der Ausgang ist durch Items NICHT beeinflussbar — ein Schutzschild schützt nicht vor Pech, ein Münz-Magnet verdoppelt keine Glücks-Gewinne. Münzen können nie unter 0 fallen. ArenaStar kommentiert das Ergebnis („Glück gehabt!", „Pech gehabt!"). Das Feld übernimmt die Risiko-Funktion der entfernten STP-Feldtypen RED und YELLOW.

## 2. Player Fantasy

Das Glück/Pech-Feld ist der „Einarmige Bandit" des Boards: ein kurzer, spannender Moment des Zufalls, der überall im Pfad lauert. Man hofft auf Goldmünzen-Regen und fürchtet rote Blitze. Weil keine Ausrüstung hilft, fühlt sich der Ausgang „ehrlich zufällig" an — schicksalhaft und unterhaltsam. Die Player Fantasy ist die eines Glücksritters, der dem Zufall ein Lächeln abtrotzt: mal Jubel, mal Achselzucken, aber immer ein kommentierter Moment von ArenaStar.

## 3. Detailed Rules

### 3.1 Anzahl und Position

- Pro Board existieren exakt 3 GLUECK_PECH-Felder.
- Platzierungsregeln (board-architecture.md 3.3): nicht in den ersten 3 Feldern (Indizes 1–3); Abstand entlang des Pfades zueinander ≥ 3 Felder.
- Referenz-Layout: Indizes 5, 15, 27.

### 3.2 Auslösung

- Der Münz-Effekt wird beim LANDEN (letztes Feld eines Würfelzugs) ausgelöst — nicht beim Überqueren und nicht bei Effekt-Platzierung (board-architecture.md 3.11).
- Jede Landung löst eine unabhängige Ziehung aus.

### 3.3 Ziehung und Ergebnisse

Kategorie-Wahrscheinlichkeiten:

| Kategorie | Wahrscheinlichkeit | Effekt |
|---|---|---|
| Glück | 60 % | +3, +5, +8 oder +10 Münzen (gleichverteilt) |
| Pech | 30 % | −3, −5 oder −8 Münzen (gleichverteilt) |
| Neutral | 10 % | 0 oder +1 Münze (gleichverteilt) |

- Glück-Subziehung: `X ~ Uniform({3, 5, 8, 10})`.
- Pech-Subziehung: `Y ~ Uniform({3, 5, 8})` (als Verlust).
- Neutral-Subziehung: `Z ~ Uniform({0, 1})`.

### 3.4 Münz-Clamp

- Münzen können nie unter 0 fallen: `coins' = max(0, coins + Δ)`.
- Ein Verlust wird also abgeschnitten, wenn der Spieler weniger Münzen besitzt als der Verlustwert.

### 3.5 Keine Beeinflussung durch Items

- Der Ausgang des Glück/Pech-Feldes ist durch Items NICHT beeinflussbar:
  - Ein aktives Schutzschild blockiert Pech NICHT (es verbraucht sich nicht, es schützt nicht).
  - Ein aktiver Münz-Magnet verdoppelt Glücks-Gewinne NICHT.
- Es gibt keine Ausnahme; diese Regel ist explizit und wird gegen item-system.md und item-shield.md geprüft (siehe Dependencies).

### 3.6 ArenaStar-Kommentar

| Ergebnis | Kommentar (Beispiel) |
|---|---|
| Glück | „Glück gehabt!" |
| Pech | „Pech gehabt!" |
| Neutral (0) | „Diesmal ist nichts passiert." |
| Neutral (+1) | „Immerhin ein Münzchen." |

Die Kommentare werden als kurze Einblendung gezeigt; exakte Wortwahl regelt narrative-arena-star.md (geplant).

### 3.7 Visuelle und auditive Darstellung

- Glück: Goldmünzen-Regen (Fall-Partikel, warmer Glanz).
- Pech: Rote Blitze (Blitz-VFX, kurzer Donner-Sound).
- Neutral: dezentes Funkeln, kein markantes VFX.
- Feld-Icon: zwei Gesichter (lächelnd/finster) oder Münze mit Blitz — Silhouette eindeutig (vision-pillars.md).

## 4. Formulas

Variablendefinitionen:
- `P_G = 0,60`, `P_P = 0,30`, `P_N = 0,10` — Kategoriewahrscheinlichkeiten.
- `X ~ Uniform({3, 5, 8, 10})` — Glücks-Gewinn.
- `Y ~ Uniform({3, 5, 8})` — Pech-Verlust.
- `Z ~ Uniform({0, 1})` — Neutral-Ergebnis.
- `Δ` — Netto-Änderung: `+X`, `−Y` oder `+Z`.

Ergebnis-Formel:
- `coins' = max(0, coins + Δ)`.

Erwartungswert:
- `E[X] = (3+5+8+10)/4 = 6,5`; `E[Y] = (3+5+8)/3 = 5,333`; `E[Z] = 0,5`.
- `E[Δ] = 0,60 · 6,5 + 0,30 · (−5,333) + 0,10 · 0,5 = 3,90 − 1,60 + 0,05 = +2,35` Münzen pro Landung (netto positiv).

Beispielrechnung:
- Spieler mit 2 Münzen, Pech mit Y=5 → `max(0, 2 − 5) = 0` (Verlust abgeschnitten).
- Spieler mit 4 Münzen, Glück mit X=8 → `4 + 8 = 12`.
- Spieler mit 0 Münzen, Neutral mit Z=0 → `0`.

## 5. Edge Cases

1. **Verlust bei geringem Kontostand:** Verlust wird auf 0 abgeschnitten; es entstehen keine Schulden.
2. **Aktiver Schutzschild + Pech:** Pech trifft trotzdem; das Schutzschild bleibt unverbraucht. PASS-Kriterium in Sektion 8.
3. **Aktiver Münz-Magnet + Glück:** Keine Verdopplung; Gewinn bleibt nominal.
4. **Mehrere Spieler auf demselben Glück/Pech-Feld in derselben Runde:** Jede Landung zieht unabhängig.
5. **Effekt-Platzierung auf ein Glück/Pech-Feld (Tausch-Basar, Rückruf etc.):** Kein Münz-Effekt (Regel board-architecture.md 3.11).
6. **Überqueren eines Glück/Pech-Feldes:** Kein Effekt.
7. **Neutral mit Z=0:** Es passiert sichtbar nichts; der ArenaStar-Kommentar erklärt das Ergebnis.
8. **AI-Spieler:** Dieselben Regeln.

## 6. Dependencies

### 6.1 Benötigt von `field-luck.md`

| Kapitel/System | Art | Verwendung |
|---|---|---|
| `board-architecture.md` | Voraussetzung | GLUECK_PECH-Typ, Lande-Regel, Platzierungsregeln. |
| `coin-economy.md` (geplant) | Quelle | Münz-Clamp, Faucet/Sink-Bilanz. |
| `narrative-arena-star.md` (geplant) | Quelle | Kommentare (Glück/Pech/Neutral). |
| `item-shield.md` (geplant) | Gegenreferenz | Muss explizit festhalten: kein Schutz gegen Glück/Pech. |
| `item-coinmagnet.md` (geplant) | Gegenreferenz | Muss explizit festhalten: kein Verdoppeln von Glück/Pech. |

### 6.2 Systeme, die von diesem Dokument abhängen

| Kapitel/System | Art der Abhängigkeit |
|---|---|
| `item-shield.md` (geplant) | Schutzschild-Definition muss die Nicht-Anwendbarkeit auf Glück/Pech bestätigen. |
| `item-coinmagnet.md` (geplant) | Münz-Magnet-Definition muss die Nicht-Anwendbarkeit bestätigen. |
| `coin-economy.md` (geplant) | Bilanziert den erwarteten Netto-Zufluss (+2,35 pro Landung). |
| `ui-hud.md` (geplant) | Zeigt Ergebnis-Einblendung und ArenaStar-Kommentar. |

### 6.3 Bidirektionalität

`board-architecture.md` verweist auf dieses Kapitel; dieses Kapitel verweist auf `board-architecture.md`. Wechselseitigkeit ist damit hergestellt.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|---|---|---|---|---|
| `P_G`, `P_P`, `P_N` | Kurve | Summe 1,0; je 0–1 | 0,60 / 0,30 / 0,10 | Netto-Risiko des Feldes (Erwartungswert). |
| Glücks-Werte `{3,5,8,10}` | Kurve | 1–20 | {3,5,8,10} | Höhe der Gewinne. |
| Pech-Werte `{3,5,8}` | Kurve | 1–20 | {3,5,8} | Höhe der Verluste. |
| Neutral-Zusammensetzung | Kurve | Z ∈ {0,1} | gleichverteilt | Häufigkeit des „+1"-Trösterchens. |
| Anzahl Felder `N_GLUECK_PECH` | Kurve | 2–5 | 3 | Häufigkeit des Zufalls-Moments. |
| Netz-Effekt | Kurve | negativ–positiv | +2,35/Landung | Soll netto leicht positiv bleiben (fairer Spaß). |

## 8. Acceptance Criteria

Ein QA-Tester kann die folgenden Prüfungen ausführen:

1. **Verteilung (statistisch):** Über 1000 Landungen liegen die Kategorieanteile innerhalb ±3 %-Punkten von 60/30/10. PASS/FAIL.
2. **Wertebereiche:** Alle Glück-Ergebnisse ∈ {3,5,8,10}, alle Pech-Ergebnisse ∈ {3,5,8}, alle Neutral-Ergebnisse ∈ {0,1}. PASS/FAIL.
3. **Clamp:** Kein Spieler fällt unter 0 Münzen, auch bei Pech −8 mit Kontostand 2. PASS/FAIL.
4. **Schutzschild-Wirkungslosigkeit:** Spieler mit aktivem Schutzschild verliert bei Pech trotzdem Münzen; das Schutzschild wird nicht verbraucht. PASS/FAIL.
5. **Münz-Magnet-Wirkungslosigkeit:** Spieler mit aktivem Münz-Magnet erhält bei Glück den nominalen Gewinn (kein Faktor 2). PASS/FAIL.
6. **Anzahl/Position:** Jedes Board hat exakt 3 GLUECK_PECH-Felder; keines in den Indizes 1–3; Abstände ≥ 3. PASS/FAIL.
7. **Effekt-Platzierung:** Tausch-Basar auf ein Glück/Pech-Feld löst keinen Münz-Effekt aus. PASS/FAIL.
8. **Unabhängigkeit:** Zwei Landungen auf demselben Feld in derselben Runde erzeugen zwei unabhängige Ergebnisse (Protokoll über 50 Versuche: nicht deterministisch gekoppelt). PASS/FAIL.
9. **ArenaStar-Kommentar:** Jede Landung zeigt einen passenden Kommentar (Glück/Pech/Neutral). PASS/FAIL.
