# Glücks-Würfel

**Status:** Final (v1.0)
**Gültig für:** Party Arena (PA), Godot 4.2, 2–8 Spieler
**Teil der Game Bible:** Teil III — Items
**Rahmenkapitel:** `item-system.md` (verbindliche Grundregeln für Inventar, Kauf, Phasen, HUD)

---

## 1. Overview

Der **Glücks-Würfel** ist ein sofort wirksames (`immediate`) Item zum Preis von **5 Münzen**. Er ersetzt den normalen Würfelwurf (1–6) durch einen **festen Wurf von 5 Feldern**. Damit wird der Zufall des Würfelns für einen Zug vollständig durch Planung ersetzt.

**TUNING-ENTSCHEIDUNG (diese Version):** Der Glücks-Würfel würfelt **fest 5** — sicher, ohne Risiko. Es gibt in dieser Version **keine** Risiko-Option. Eine alternative Variante (Wahl zwischen "sicher 5" und "Risiko 1–10") ist dokumentiert, aber **nicht** aktiv (siehe §4, F2 und §7 K5).

Der Glücks-Würfel ist das preisgünstigste Werkzeug für **präzises Positionieren**: Er eignet sich ideal, um den **Sternen-Shop** oder den **Item-Shop** exakt zu erreichen, wenn diese 5 Felder entfernt liegen.

---

## 2. Player Fantasy

**"Ich kontrolliere den Zufall."** Der Glücks-Würfel bedient die Fantasie des berechnenden Planers. Während normale Würfe Unsicherheit erzeugen, verwandelt der Glücks-Würfel den Zug in ein sicheres Manöver. Der Spieler erlebt:

- **Vorhersagbarkeit:** Das eigene Ergebnis ist garantiert; keine böse Überraschung durch eine 1.
- **Cleverness:** Den Wurf für das exakte Erreichen eines Schlüssel-Feldes (Sternen-Shop, Item-Shop) einplanen und sich innerlich dafür belohnen.
- **Überlegenheit gegenüber dem Brett:** Während andere würfeln und hoffen, marschiert der Glücks-Würfel-Spieler zielgerichtet.

Die Fantasie ist bewusst **dezent**: kein spektakulärer Effekt, sondern das ruhige, sichere Gefühl von Kontrolle — passend zum günstigen Preis.

---

## 3. Detailed Rules

### 3.1 Preis und Erwerb

- **Preis:** 5 Münzen im Item-Shop (Sortiment und Kauf siehe `item-system.md` §3.2).
- **Erwerb zusätzlich möglich:** durch Events (Event-Grants, siehe `item-system.md` §3.6).

### 3.2 Aktivierung

- **Aktivierungsphase:** Phase 0 (Item-Aktivierung **vor dem Würfeln**).
- **Effekt:** Der normale Würfelwurf (1–6) wird durch den festen Wert **5** ersetzt.
- **Wirkung:** Der Spieler würfelt nicht physisch; die Bewegung in Phase 3 beträgt exakt 5 Felder (bzw. 10 bei aktivem Würfel-Verdoppler, siehe 3.5).
- **Verbrauch:** Das Item wird bei Aktivierung aus dem Inventar entfernt.

### 3.3 Stacking- und Kombinationsregeln

| Kombination | Erlaubt? | Verhalten |
|---|---|---|
| Zweiter Glücks-Würfel im selben Zug | **Nein** | Nur **1 Glücks-Würfel pro Zug** einsetzbar. Der zweite bleibt im Inventar. |
| Glücks-Würfel + Stern-Teleporter | **Nein** | Beide ersetzen den Würfelwurf; sie schließen sich in Phase 0 gegenseitig aus. |
| Glücks-Würfel + andere Würfel-Modifikatoren (Items) | **Nein** | Kein Item darf den Wurfwert zusätzlich verändern (z. B. +N-Würfel-Items existieren nicht; wären aber gesperrt). |
| Glücks-Würfel + Münz-Magnet | **Ja** | Münz-Magnet ist kein Würfel-Modifikator. Beide können in Phase 0 aktiviert werden. |
| Glücks-Würfel + Würfel-Verdoppler-Event | **Ja (Sonderfall)** | Der Verdoppler ist ein Event-Multiplikator auf das Endergebnis: Wurf wird **10**. Siehe 3.5. |
| Glücks-Würfel + Dieb-Handschuh | **Ja** | Dieb-Handschuh liegt in Phase 2 (nach dem Würfeln); beide können im selben Zug verwendet werden. |

### 3.4 Animation

1. Der Charakter zieht einen **goldenen Würfel mit einer Krone** aus der Hand.
2. Der Würfel wird geworfen und zeigt immer **fünf Augen**, die kurz golden aufleuchten.
3. Eine Pfadanzeige markiert die 5 Felder (bzw. 10 Felder bei Verdoppler), die der Charakter ziehen wird.
4. Das Item-Icon erlischt (Verbrauch).

**Zeitbudget:** Effektphase ≤ 2 Sekunden.

### 3.5 Würfel-Verdoppler-Event (Sonderfall)

- Ist zum Zeitpunkt der Aktivierung das Event **"Würfel-Verdoppler"** aktiv (ein aktives Event, das Würfelergebnisse verdoppelt), beträgt das Ergebnis des Glücks-Würfels **5 × 2 = 10**.
- Der Spieler bewegt sich dann **10 Felder** (nicht 5). Die Bewegung über 10 Felder muss vom Bewegungs- und Feld-System unterstützt werden (siehe Dependencies).
- Begründung: Der Verdoppler ist kein Würfel-Modifikator-Item, sondern ein Event-Multiplikator auf das finale Wurfergebnis. Er wird daher nicht von der "keine Würfel-Modifikatoren"-Regel gesperrt.

### 3.6 Feld-Effekte nach der Bewegung

- Der Glücks-Würfel ersetzt nur den **Wurf**. Die Bewegung und der **Feld-Effekt des Zielfeldes** laufen normal ab (Phase 3 und 4 des Zugablaufs, siehe `item-system.md` §3.4).
- Landet der Spieler auf einem Münz-Bonus-Feld und ist ein Münz-Magnet aktiv, wird der Bonus normal verdoppelt (unabhängig vom Glücks-Würfel).

---

## 4. Formulas

### F1 — Wurfergebnis des Glücks-Würfels

**Benannter Ausdruck:**

```
result = base * (1 + is_doubled)
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| base | int | 5 (fix) | Fester Wurfwert des Glücks-Würfels |
| is_doubled | bool | {0, 1} | 1, wenn das Würfel-Verdoppler-Event aktiv ist; sonst 0 |
| result | int | {5, 10} | Endgültige Bewegungsschritte des Spielers in Phase 3 |

**Ausgabebereich:** Ergebnis ist exakt 5 (Standard) oder 10 (bei aktivem Verdoppler). Es gibt keine Zwischenwerte. Der Wert ist deterministisch — kein Zufall.

**Arbeitsbeispiel 1 (Standard):** Kein Verdoppler aktiv. `result = 5 × (1 + 0) = 5`. Der Spieler zieht exakt 5 Felder.

**Arbeitsbeispiel 2 (Verdoppler):** Würfel-Verdoppler-Event aktiv. `result = 5 × (1 + 1) = 10`. Der Spieler zieht 10 Felder.

### F2 — Alternative Variante "Sicher vs. Risiko" (NICHT aktiv, Dokumentation)

Falls das Tuning K5 umgestellt wird, gilt:

**Benannter Ausdruck:**

```
result = player_choice == "sicher" ? 5 : U{1, ..., 10}
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| player_choice | enum | {"sicher", "risiko"} | Vom Spieler gewählter Modus |
| U{1,...,10} | int | 1–10 | Gleichverteilte Zufallszahl (Risiko-Wurf) |
| result | int | 5 (sicher) oder 1–10 (Risiko) | Bewegungsschritte |

**Ausgabebereich:** Bei "sicher" exakt 5; bei "risiko" ganzzahlig 1–10, jede Zahl mit Wahrscheinlichkeit 1/10.

**Arbeitsbeispiel:** Spieler wählt "risiko" → gewürfelt wird z. B. 7 → Bewegung 7 Felder. Die Risiko-Option hat einen Erwartungswert von 5,5, ist also im Mittel leicht besser als die sichere 5, aber stark streuend (Varianz 8,25).

### F3 — Strategischer Nutzen: Erreichbarkeit eines Schlüsselfeldes

**Benannter Ausdruck:**

```
reachable = (distance_to_target == 5) OR (distance_to_target == 10 AND is_doubled)
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| distance_to_target | int | 0–39 | Felderabstand (vorwärts) zum Ziel-Feld auf dem 40er-Pfad |
| is_doubled | bool | {0, 1} | Verdoppler-Event aktiv |
| reachable | bool | {0, 1} | Ziel exakt erreichbar |

**Ausgabebereich:** Bool. Der Glücks-Würfel garantiert exakte Landung nur, wenn die Distanz 5 (bzw. 10) beträgt.

**Arbeitsbeispiel:** Der Sternen-Shop ist 5 Felder voraus → `reachable = (5 == 5) OR ... = wahr`. Der Spieler kann den Stern garantiert erreichen. Ist der Shop 4 Felder entfernt, ist er mit dem Glücks-Würfel **nicht** exakt erreichbar (dann wäre ein normaler Wurf nötig).

---

## 5. Edge Cases

| # | Fall | Konkretes Verhalten |
|---|---|---|
| E1 | Würfel-Verdoppler-Event aktiv | Ergebnis 10 statt 5; Spieler zieht 10 Felder. |
| E2 | Spieler besitzt zwei Glücks-Würfel | Pro Zug ist nur 1 einsetzbar. Der zweite bleibt im Inventar und kann in einem späteren Zug verwendet werden. |
| E3 | Spieler versucht Glücks-Würfel + Teleporter im selben Zug | Beide sind würfelersetzend; der zweite wird in Phase 0 blockiert (Meldung "Ein würfelersetzendes Item ist bereits aktiv"). |
| E4 | Glücks-Würfel + Münz-Magnet kombiniert | Erlaubt. Bewegung 5 Felder; falls das Zielfeld Münzen bringt, greift die Magnet-Verdopplung. |
| E5 | Ziel-Distanz ungleich 5 (bzw. 10) | Der Glücks-Würfel garantiert keine exakte Landung; der Spieler kann das Ziel nicht mit Sicherheit erreichen. Das Item wird trotzdem normal verbraucht. |
| E6 | Aktivierung außerhalb von Phase 0 | Blockiert; Item bleibt im Inventar. |
| E7 | Spielende vor der Aktivierung | Ungenutzter Glücks-Würfel verfällt ersatzlos. |
| E8 | Verdoppler-Event + Risiko-Variante (falls K5 aktiv) | Risiko-Wurf 1–10 würde ebenfalls verdoppelt (Ergebnis 2–20). In der aktiven Version (fest 5) nicht relevant. |
| E9 | Pfad ist kürzer als 5 Felder zum Ziel (Rundenende, Startüberquerung) | Bewegung erfolgt über die volle Distanz auf dem zyklischen 40er-Pfad; Feld-Effekte nur auf dem Zielfeld. Startüberquerung zählt normal. |

---

## 6. Dependencies

**Der Glücks-Würfel ist abhängig von:**

| System | Art der Abhängigkeit |
|---|---|
| `item-system.md` | Kauf, Inventar (max 3), Phasen (Phase 0), HUD (Slot 1–3, Taste 1), Verbrauch. |
| `dice-movement.md` | Ersetzt den Würfelwurf; Bewegung um 5 (oder 10) Felder muss unterstützt werden; Zugphasen. |
| `field-event.md` | Würfel-Verdoppler-Event (verdoppelt das Ergebnis auf 10). |
| `field-star-shop.md` / `field-item-shop.md` | Strategische Ziel-Felder (exakte Erreichbarkeit). |
| `coin-economy.md` | Kaufpreis (5 Münzen). |
| `technical-data-structures.md` | Item-Datenstruktur (`item_id = luckydice`, `item_effect_type = immediate`). |
| `audio-overview.md` / `audio-sfx.md` | Würfel- und Aktivierungs-Sounds. |

**Gegenrichtung (müssen in ihren Kapiteln auf den Glücks-Würfel verweisen):**

- `dice-movement.md` → Der Glücks-Würfel kann den Wurf auf einen festen Wert (5, ggf. 10) setzen.
- `field-event.md` → Das Würfel-Verdoppler-Event interagiert mit dem Glücks-Würfel (10er-Ergebnis).
- `item-system.md` → listet den Glücks-Würfel als eines der 5 aktiven Items.
- `field-item-shop.md` → verkauft den Glücks-Würfel für 5 Münzen.

---

## 7. Tuning Knobs

| Knopf | Standard | Sicherer Bereich | Beeinflusste Gameplay-Größe |
|---|---|---|---|
| K1 Fester Wurfwert (`base`) | 5 | 3–7 | Welche Felder exakt erreichbar sind; zu hohe Werte (≥6) machen den Sternen-Shop zu oft sicher erreichbar. |
| K2 Preis | 5 | 4–7 | Kaufhäufigkeit und Wirtschaftsdruck. |
| K3 Anzahl pro Zug | 1 | 1–2 | Verhindert Serien von Festwürfen; bei 2 wird kontrolliertes Vorrücken deutlich stärker. |
| K4 Verdoppler-Interaktion | an | an / aus | Macht das Item situationsabhängig stärker (10er-Wurf); "aus" reduziert die maximale Reichweite auf 5. |
| K5 Alternative Variante (sicher/risiko) | **fest 5** (aus) | fest 5 / Wahl-Modus | "Wahl-Modus" fügt Risiko-Belohnung hinzu (Erwartungswert 5,5 bei Varianz 8,25); erhöht Spannung und Entscheidungsfreiheit, aber auch Rechenkomplexität für Neueinsteiger. |
| K6 Preis-Leistung vs. Teleporter | Preis 5 vs. 8 | — | Abstand zum Teleporter (8) muss fühlbar bleiben: Der Glücks-Würfel ist günstig, aber abhängig von Distanz und Stern-Verfügbarkeit. |

---

## 8. Acceptance Criteria

| ID | Kriterium | Pass-Bedingung |
|---|---|---|
| AC1 | Fester Wurf | Nach Aktivierung in Phase 0 bewegt sich der Spieler exakt **5 Felder**, ohne zu würfeln. |
| AC2 | Verdoppler-Sonderfall | Bei aktivem Würfel-Verdoppler-Event bewegt sich der Spieler exakt **10 Felder**. |
| AC3 | Kein Zufall | Das Ergebnis ist in 50 Testläufen ohne Verdoppler immer 5 (0 Streuung). |
| AC4 | Einmal pro Zug | Ein zweiter Glücks-Würfel kann im selben Zug nicht aktiviert werden und bleibt im Inventar. |
| AC5 | Keine Kombination mit Teleporter | Bei bereits aktiviertem Teleporter ist die Aktivierung blockiert und umgekehrt. |
| AC6 | Kombination mit Münz-Magnet | Beide Items können in Phase 0 aktiviert werden; ein Münz-Bonus des Zielfelds wird korrekt verdoppelt. |
| AC7 | Verbrauch | Nach der Aktivierung ist der Glücks-Würfel aus dem Inventar entfernt. |
| AC8 | Animation | Der goldene Würfel mit Krone erscheint und zeigt exakt 5 (bzw. 10) leuchtende Augen. |
| AC9 | Blockade in falscher Phase | Aktivierungsversuch in Phase 2 oder 3 ist wirkungslos; Item bleibt erhalten. |
| AC10 | Preis | Der Kaufpreis im Item-Shop beträgt exakt 5 Münzen. |
