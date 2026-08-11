# Mini-Spiel-Feld — Party Arena Game Bible

> **Teil:** 2 — Board & Fields
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/game-bible-prompt.md

---

## 1. Overview

Das Mini-Spiel-Feld (Feldtyp MINISPIEL) ist der häufigste Feldtyp auf jedem Board (Restgröße, im Referenz-Layout 23 von 40 Feldern) und liegt auf Hauptpfad und Abzweigungen. Seine mechanische Funktion ist bewusst schlank: Es markiert den Spieler für das Minispiel am Rundenende und — entscheidend — es bestimmt die KATEGORIE (Schwierigkeits-Tier) des Minispiels, das nach dem letzten Spielerzug gespielt wird. WICHTIG (Game-Bible-Regel): An jedem Minispiel nehmen ALLE Spieler teil, unabhängig davon, auf welchen Feldern sie gelandet sind. Das Mini-Spiel-Feld bestimmt ausschließlich die Kategorie. Die Kategorie wird aus der Feld-Position abgeleitet: frühe Felder (kleine Loop-Distanz) → leichte Minispiele, spätere Felder → schwerere. Das Feld ersetzt die farbcodierten STP-Minispiel-Felder (BLUE/RED/GREEN/YELLOW), deren Farb-Kategorien entfallen.

## 2. Player Fantasy

Das Mini-Spiel-Feld ist das „?"-Feld des Boards: ein lila/blaues Feld mit Fragezeichen- oder Controller-Icon, das Abwechslung und Spannung verspricht. Es erinnert daran, dass nach jeder Runde ein kurzer, chaotischer Wettkampf wartet — der eigentliche Party-Höhepunkt. Die Position des Feldes gibt (für Kenner) einen Hinweis auf die Schwierigkeit des kommenden Minispiels: Wer auf einem frühen Feld landet, darf mit einem leichten Spiel rechnen, wer spät landet, mit einer größeren Herausforderung. Die Player Fantasy ist die eines Partygasts, der immer weiß: „Gleich wird gespielt!"

## 3. Detailed Rules

### 3.1 Anzahl

- `N_MINISPIEL = N_total − N_fixed = 40 − (1 + N_STERN_SHOP + 2 + N_EREIGNIS + 3 + 4) = 30 − N_STERN_SHOP − N_EREIGNIS`.
- Mit `N_STERN_SHOP ∈ {2,3}` und `N_EREIGNIS ∈ {5,6}` ergibt sich `N_MINISPIEL ∈ {21, 22, 23}`.
- Referenz-Layout: `N_MINISPIEL = 23` (Hauptpfad-Indizes 1, 4, 7, 9, 10, 11, 13, 16, 17, 19, 21, 22, 23, 24, 29, 30, 31 sowie Abzweigung A: 32, 34, 35 und Abzweigung B: 36, 38, 39).

### 3.2 Auslösung und Markierung

- Eine Landung (letztes Feld eines Würfelzugs) auf einem MINISPIEL-Feld markiert den Spieler für das Rundenende-Minispiel (Legacy-Markierung).
- In der Game Bible ist die Markierung ohne Wirkung auf die Teilnahme (alle spielen), behält aber ihre technische Existenz als Vorbereitung für den Tuning-Modus „nur Markierte" (Sektion 7).
- Überqueren und Effekt-Platzierung setzen KEINE Markierung und ändern die Kategorie NICHT.

### 3.3 Teilnahme (Game-Bible-Regel)

- ALLE Spieler nehmen an JEDEM Rundenende-Minispiel teil — unabhängig davon, auf welchen Feldern sie gelandet sind.
- Das Mini-Spiel-Feld bestimmt ausschließlich die Kategorie (Tier), nicht die Teilnahme.
- Ausnahme für zukünftige Tuning-Varianten: Siehe `TEILNAHME_MODUS` in Sektion 7. Der Bible-Standard ist `ALLE`.

### 3.4 Kategorie-Bestimmung (Tier)

- Jedes MINISPIEL-Feld besitzt eine feste Tier-Zuordnung, die aus der Loop-Distanz `LD(f)` abgeleitet wird (board-architecture.md 4):
  - LEICHT: `LD` 1–13,
  - MITTEL: `LD` 14–26,
  - SCHWER: `LD` 27–39.
- Abzweigungs-Felder verwenden ihre Loop-Distanz (Abzweigung A: LD 10–13 → LEICHT; Abzweigung B: LD 23–26 → MITTEL).
- Die Bandgrenzen sind pro Board über `minigame_tiers` im Manifest änderbar (Standard wie oben).
- Referenz-Tier-Verteilung: LEICHT 10, MITTEL 10, SCHWER 3 (Summe 23).

### 3.5 Minispiel-Auswahl am Rundenende

- Nach dem letzten Spielerzug wird die Kategorie des Rundenende-Minispiels bestimmt:
  1. Hat der zuletzt ziehende Spieler (letzter Zug der Runde) auf einem MINISPIEL-Feld gelandet, ist dessen Tier die Kategorie.
  2. Andernfalls: Tier des MINISPIEL-Feldes des letzten Spielers, der in dieser Runde auf einem MINISPIEL-Feld gelandet ist (bezogen auf die Zugreihenfolge).
  3. Falls in dieser Runde NIEMAND auf einem MINISPIEL-Feld gelandet ist: Fallback-Kategorie LEICHT.
- Aus der gewählten Tier-Gruppe wird das konkrete Minispiel gleichverteilt aus dem Minispiel-Pool des Tiers gezogen (minigame-architecture.md / minigame-categories.md, geplant).
- Die Ziehung erfolgt einmalig am Rundenende; die Reihenfolge der Markierungen innerhalb der Runde spielt keine Rolle (nur die „letzte" zählt).

### 3.6 Timing

- Das Minispiel startet NACH dem letzten Spielerzug (nach Auflösung aller Lande-Effekte) und VOR der Rundenende-Wartung (board-architecture.md 3.12.3).
- Nach dem Minispiel folgen Belohnung (minigame-rewards.md, geplant) und Rundenende-Wartung.

### 3.7 Visuelle und auditive Darstellung

- Visual: lila/blaues Feld mit „?"- oder Controller-Icon; Animation (leichtes Pulsieren) signalisiert „hier geht's gleich rund".
- Optional pro Tier eine dezente Farbnuance (LEICHT hell, MITTEL mittel, SCHWER dunkel), ZUSÄTZLICH zum Icon (niemals Farbe allein — vision-pillars.md).
- Audio-Cue: kurzer „Antippen"-Sound bei Landung, der zum Minispiel-Übergang führt.

### 3.8 Keine weiteren Effekte

- Das MINISPIEL-Feld hat KEINE weiteren Effekte: keine Münzen, keine Items, keine Ereignisse, kein Glück/Pech.
- Es ist bewusst das „neutrale" Füll-Feld des Boards.

## 4. Formulas

Variablendefinitionen:
- `N_total = 40`; `N_fixed = 1 + N_STERN_SHOP + 2 + N_EREIGNIS + 3 + 4`.
- `N_MINISPIEL = N_total − N_fixed = 30 − N_STERN_SHOP − N_EREIGNIS`.
- `LD(f)` — Loop-Distanz (kürzester Pfad vom Start zu f).
- `Tier(f)` — Kategorie eines Feldes: `LEICHT` (LD 1–13), `MITTEL` (LD 14–26), `SCHWER` (LD 27–39).

Auswahl-Formeln (Rundenende):
- `Tier_minispiel = Tier(landefeld(letzter Spieler))`, falls `typ(landefeld(letzter Spieler)) = MINISPIEL`.
- Sonst: `Tier_minispiel = Tier(landefeld(j))`, wobei j der letzte Spieler in Zugreihenfolge ist mit `typ(landefeld(j)) = MINISPIEL`.
- Sonst: `Tier_minispiel = LEICHT` (Fallback).
- Konkretes Minispiel: `Minispiel ~ Uniform(Pool(Tier_minispiel))`.

Erwartungswerte:
- Referenz: `N_MINISPIEL = 40 − (1 + 2 + 2 + 5 + 3 + 4) = 23`.
- Tier-Anteile (Referenz): LEICHT 10/23 ≈ 43 %, MITTEL 10/23 ≈ 43 %, SCHWER 3/23 ≈ 13 %.
- Praktische Kategorie-Wahrscheinlichkeit pro Runde hängt von den Landungen ab; ohne MINISPIEL-Landung in einer Runde fällt die Kategorie auf LEICHT zurück.

Beispielrechnung:
- Letzter Spieler landet auf Feld 29 (LD 29) → Kategorie SCHWER; Minispiel wird gleichverteilt aus dem SCHWER-Pool gezogen.
- Letzter Spieler landet auf Feld 12 (STERN_SHOP); vorheriger MINISPIEL-Lander war auf Feld 22 (LD 22) → Kategorie MITTEL.
- Niemand landet auf einem MINISPIEL-Feld → Kategorie LEICHT.

## 5. Edge Cases

1. **Keine MINISPIEL-Landung in einer Runde:** Fallback LEICHT; ALLE Spieler spielen trotzdem.
2. **Letzter Spieler landet nicht auf MINISPIEL:** Es zählt die letzte MINISPIEL-Landung der Runde in Zugreihenfolge.
3. **Mehrere MINISPIEL-Landungen mit unterschiedlichen Tiers:** Die Kategorie bestimmt ausschließlich der „letzte" relevante Spieler; es wird nicht gemischt.
4. **Alle Spieler auf MINISPIEL-Feldern, verschiedene Tiers:** Kategorie = Tier des letzten Zuges.
5. **Effekt-Platzierung auf ein MINISPIEL-Feld:** Keine Markierung, keine Kategorie-Änderung (board-architecture.md 3.11).
6. **Überqueren eines MINISPIEL-Feldes:** Keine Markierung, keine Kategorie-Änderung.
7. **2-Spieler-Partie:** Teilnahme-Regel unverändert (beide spielen).
8. **Tier-Bandgrenzen verschoben (Manifest):** Die Zuordnung folgt den Manifest-Werten; die Formel in 4 bleibt strukturell gleich.
9. **Markierungs-Modus (`TEILNAHME_MODUS = MARKIERT`, Tuning):** Nur Spieler mit Markierung spielen; die Kategorie-Bestimmung (3.5) bleibt unverändert.
10. **AI-Spieler:** Nehmen an Minispielen teil wie Menschen (Schwierigkeitsgrad steuert Leistung, nicht Teilnahme).

## 6. Dependencies

### 6.1 Benötigt von `field-minigame.md`

| Kapitel/System | Art | Verwendung |
|---|---|---|
| `board-architecture.md` | Voraussetzung | MINISPIEL-Typ, Loop-Distanz, Rundenablauf (Minispiel nach letztem Zug). |
| `minigame-architecture.md` (geplant) | Quelle | Plugin-Vertrag, Ladevorgang, Ergebnisübermittlung. |
| `minigame-categories.md` (geplant) | Quelle | Tier-Pools, Genre-Auswahl innerhalb des Tiers. |
| `minigame-rewards.md` (geplant) | Quelle | Belohnung nach Platzierung. |
| `dice-movement.md` (geplant) | Quelle | Zugreihenfolge für die Kategorie-Auflösung. |

### 6.2 Systeme, die von diesem Dokument abhängen

| Kapitel/System | Art der Abhängigkeit |
|---|---|
| `minigame-architecture.md` (geplant) | Muss das Rundenende-Minispiel auslösen und die Kategorie aus diesem Kapitel übernehmen. |
| `minigame-categories.md` (geplant) | Muss die Tiers (LEICHT/MITTEL/SCHWER) als Pools anbieten. |
| `core-loop.md` (geplant) | Meso-Loop: Spielerzüge → Minispiel → Wartung. |
| `ui-hud.md` (geplant) | Zeigt das kommende Minispiel / Kategorie-Hinweis. |
| `technical-fork-strategy.md` (geplant) | Migriert die farbcodierten STP-Minispiel-Felder zu MINISPIEL. |

### 6.3 Bidirektionalität

`board-architecture.md` verweist auf dieses Kapitel (Kategorie-Auflösung, Rundenablauf); dieses Kapitel verweist zurück. Wechselseitigkeit ist damit hergestellt.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|---|---|---|---|---|
| `TEILNAHME_MODUS` | Gate | `ALLE` / `MARKIERT` | `ALLE` | Bible-Standard: alle spielen; `MARKIERT` = nur gelandete Spieler (Zukunftsvariante). |
| Bandgrenzen (LEICHT/MITTEL/SCHWER) | Kurve | LD frei wählbar | 1–13 / 14–26 / 27–39 | Schwierigkeits-Progression. |
| Fallback-Kategorie | Gate | LEICHT / MITTEL | LEICHT | Was passiert ohne MINISPIEL-Landung. |
| `N_MINISPIEL` | Kurve | 21–23 (via N_STERN_SHOP, N_EREIGNIS) | 23 | Füllgrad des Boards. |
| Tier-Pools | Kurve | je Tier ≥ 1 Minispiel | je Tier ≥ 2 | Abwechslung innerhalb der Kategorie. |
| Tier-Farbnuance | Feel | an/aus | an (zusätzlich zum Icon) | Wiedererkennbarkeit der Kategorie. |

## 8. Acceptance Criteria

Ein QA-Tester kann die folgenden Prüfungen ausführen:

1. **Anzahl:** `N_MINISPIEL = 40 − N_fixed` für jedes Board; Referenz: 23. PASS/FAIL.
2. **Teilnahme (Bible-Regel):** In einer Runde, in der nur 1 von 4 Spielern auf einem MINISPIEL-Feld landet, spielen ALLE 4 das Minispiel. PASS/FAIL.
3. **Teilnahme ohne Markierung:** In einer Runde ohne MINISPIEL-Landung spielen trotzdem ALLE Spieler ein Minispiel (Fallback LEICHT). PASS/FAIL.
4. **Kategorie = letzter Zug:** Letzter Spieler landet auf Feld 29 (SCHWER) → Minispiel aus dem SCHWER-Pool. PASS/FAIL.
5. **Kategorie-Rückfall:** Letzter Spieler landet auf einem Nicht-MINISPIEL-Feld, letzte MINISPIEL-Landung war Feld 22 (MITTEL) → Minispiel aus dem MITTEL-Pool. PASS/FAIL.
6. **Tier-Zuordnung:** Alle MINISPIEL-Felder erfüllen die Bandgrenzen (Standard 1–13/14–26/27–39) anhand ihrer Loop-Distanz. PASS/FAIL.
7. **Keine Zusatzeffekte:** Eine MINISPIEL-Landung zahlt keine Münzen, gibt keine Items und löst kein Ereignis aus. PASS/FAIL.
8. **Effekt-Platzierung:** Tausch-Basar auf ein MINISPIEL-Feld ändert die Kategorie nicht und setzt keine Markierung. PASS/FAIL.
9. **Migration:** Kein Board verwendet mehr die farbcodierten STP-Typen BLUE/RED/GREEN/YELLOW für Minispiel-Kategorien. PASS/FAIL.
