# Münz-Ökonomie — Party Arena Game Bible

> **Teil:** I — Core Game
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/bible-index.md

---

## 1. Overview

Münzen sind die **Sekundärwährung** von Party Arena. Sie sind das Betriebsmittel der Partie: Spieler verdienen Münzen durch Minispiele, Felder, Glück und Ereignisse, geben sie im Sternen-Shop (20 Münzen pro Stern, siehe [star-economy](star-economy.md)) und im Item-Shop (4–10 Münzen pro Item) aus und verlieren sie durch Pech-Felder, den Dieb-Handschuh und kostenpflichtige Ereignisse. Dieses Kapitel definiert die vollständige Münz-Ökonomie: alle **Quellen (Faucets)** und **Senken (Sinks)**, die Auszahlungstabelle der Minispiele, das Startguthaben, die Regeln für das Münz-Minimum (0, kein negativer Stand) und -Limit (kein hartes Cap, Anzeige-Referenz 99), das Verhalten von Transfers (Dieb-Handschuh mit Münz-Erhaltung), die erwartete Münz-Inflation über die Runden sowie den Gesamt-Umlauf pro Partie. Ziel ist eine Ökonomie, in der ein Stern (20 Münzen) nach 3–4 Runden spürbar, aber nicht garantiert erreichbar ist, und in der der Münzbestand über die Partie hinweg von 5–15 (früh) auf 20–50 (spät) ansteigt. Die Catch-Up-Mechaniken aus [catch-up](catch-up.md) (Verlierer-Boost, Münz-Magnet) modifizieren einzelne Zuflüsse; sie sind hier als Modifikatoren referenziert.

## 2. Player Fantasy

Münzen sind der **Motor des Spiels** (MDA: Challenge + Sensation). Jedes Münzen-Sammeln erzeugt ein hör- und sichtbares Belohnungs-Klingeln; die Anzeige wächst und schrumpft sichtbar. Die zentrale emotionale Spannung ist das **"Fast genug für einen Stern"**-Gefühl: Bei 18 Münzen und dem Sternen-Shop in Sichtweite wird jede Münze wertvoll, und ein Pech-Feld bei 20 Münzen ist ein kleiner Schock. Der Dieb-Handschuh erzeugt **Schadenfreude und Vorsicht** (Fellowship im Wettbewerb): Wer viele Münzen hütet, wird Ziel; wer wenige hat, ist uninteressant. Das Münz-Minimum von 0 schützt vor dem Absturz ins Bodenlose — man kann nie bankrott "bestraft" werden, sondern startet den nächsten Verdienst-Zyklus von 0. Der Anstieg der Münzbestände über die Runden (5–15 früh, 20–50 spät) erzeugt das Gefühl von **Wachstum und Fortschritt** (Kompetenz): Früh kämpft man um jeden Münz-Bonus, später werden Items und sogar mehrere Sterne planbar. Die Ökonomie ist so ausgelegt, dass sie **fair und lesbar** bleibt: Jede Münz-Änderung hat eine sichtbare Ursache (Animation, Ansage), und keine Quelle oder Senke dominiert das Spiel allein.

## 3. Detailed Rules

### 3.1 Startguthaben

1. Jeder Spieler startet die Partie mit **10 Münzen**.
2. Das Startguthaben wird einmalig zu Partiebeginn (nach der Vorrunde, vor Runde 1) gutgeschrieben.
3. **Begründung:** 10 Münzen erlauben den ersten Item-Kauf oder den ersten ernsthaften Sparbeitrag zum Stern (20) ab Runde 2–3 und passen zur Ziel-Bandbreite "frühe Runden 5–15 Münzen" (siehe 3.7).

### 3.2 Quellen (Faucets)

Die folgenden Quellen erhöhen den Münzbestand eines Spielers:

| Quelle | Betrag | Details |
|---|---|---|
| Minispiel-Auszahlung | Siehe Tabelle 3.2.1 | Nach Platzierung; Basis jeder Runde. |
| Verlierer-Boost | +1 | Zusätzlich zur Minispiel-Auszahlung für den Letzten ([catch-up](catch-up.md)). |
| Münz-Bonus-Feld | 3–8 | Gleichverteilte ganze Zahl; modifiziert durch Münz-Magnet ([catch-up](catch-up.md)). |
| Glück/Pech-Feld (positiv) | 2–6 | Gewinn-Seite; modifiziert durch Münz-Magnet. |
| Ereignis-Feld | 0–10 | Betrag je Ereignis; rang-skaliert ([catch-up](catch-up.md)). |
| Münz-Magnet (passiv) | +50 % (gedeckelt) | Nur für "münz-arme" Spieler auf Feld- und Ereignis-Zuflüsse ([catch-up](catch-up.md) Abschnitt 3.8). |

**3.2.1 Minispiel-Auszahlungstabelle (verbindlich):**

| Platzierung | Auszahlung |
|---|---|
| 1. Platz | 10 Münzen |
| 2. Platz | 7 Münzen |
| 3. Platz | 5 Münzen |
| 4. Platz | 3 Münzen |
| 5.–8. Platz | 2 Münzen |

- Die Tabelle gilt unabhängig von der Spielerzahl: Bei 2 Spielern erhält Platz 1 = 10, Platz 2 = 7; bei 3 Spielern zusätzlich Platz 3 = 5; bei 4 Spielern zusätzlich Platz 4 = 3; bei 5–8 Spielern erhalten alle Plätze ab 5 exakt 2 Münzen.
- **Geteilte Plätze:** Endet ein Minispiel im Gleichstand, wird die Auszahlung der betroffenen Plätze addiert und gleichmäßig geteilt (abgerundet, Rest verfällt). Beispiel 4 Spieler: Platz 1 und 2 gleichauf → (10 + 7) / 2 = 8,5 → 8 Münzen je Spieler, 1 Münze verfällt. (Die detaillierte Gleichstands-Regel liegt in [minigame-rewards](minigame-rewards.md).)
- Die Tabelle ist die **Basis für alle Balance-Berechnungen** (Sektion 4).

### 3.3 Senken (Sinks)

Die folgenden Senken verringern den Münzbestand eines Spielers:

| Senke | Betrag | Details |
|---|---|---|
| Sternen-Shop | 20 pro Stern | Fixpreis; einzige Stern-Quelle ([star-economy](star-economy.md)). |
| Item-Shop | 4–10 pro Item | Fixpreise je Item: Glücks-Würfel 5, Münz-Magnet 4, Schutzschild 6, Stern-Teleporter 8, Dieb-Handschuh 10. Preise in den Item-Kapiteln ([item-system](item-system.md)). |
| Glück/Pech-Feld (negativ) | 2–6 | Verlust-Seite; kein Münz-Magnet-Schutz (Magnet wirkt nur auf Gewinne). |
| Ereignis-Feld (Kosten) | 0–10 | Kostenpflichtige Ereignisse; bei < Kosten ist die kostenpflichtige Option nicht wählbar. |
| Dieb-Handschuh | Transfer (5–10) | Entzieht dem Ziel Münzen; der Dieb erhält sie (keine Senke, siehe 3.5). |

### 3.4 Transfers (Dieb-Handschuh)

1. Der Dieb-Handschuh **überträgt** Münzen von einem Zielspieler zum auslösenden Spieler. Er ist **keine Senke** (Gesamtumlauf bleibt konstant).
2. **Betrag:** Der Handschuh spezifiziert einen Zielbetrag `D` (Standard: 5–10, Details in [item-thiefglove](item-thiefglove.md)).
3. **Erhaltung:** Der Dieb erhält exakt den Betrag, den das Ziel tatsächlich verliert. Hat das Ziel weniger als `D` Münzen, verliert es nur seinen gesamten Bestand (bis 0), und der Dieb erhält genau diesen Bestand. Es entstehen keine Münzen aus dem Nichts und es verschwinden keine.
4. **Beispiel:** Ziel hat 7 Münzen, `D = 10` → Ziel verliert 7, Dieb erhält 7. Ziel hat 0 → Verlust 0, Dieb erhält 0 (fehlgeschlagener Diebstahl zählt nicht als gewonnene PvP-Interaktion, siehe [star-economy](star-economy.md)).

### 3.5 Münz-Minimum (Floor 0)

1. Der Münzbestand eines Spielers kann **niemals negativ** werden. Der minimale Wert ist 0.
2. **Senken mit festem Betrag (Pech-Feld, Ereignis-Kosten, Item-Preis, Stern-Preis):** Der volle Betrag wird nur abgezogen, wenn er verfügbar ist. Reicht der Bestand nicht aus:
   - **Kauf-Optionen (Stern, Item):** Der Kauf wird verweigert (kein Teilkauf, kein Kredit).
   - **Verlust-Effekte (Pech-Feld, Ereignis):** Der Verlust wird auf den verfügbaren Bestand begrenzt: `Verlust = min(fester Betrag, aktueller Bestand)`. Bei Bestand 0 ist der Verlust 0.
3. **Kein Kredit-System:** Es gibt keine negativen Münzen, keine Schulden und keine Rückzahlungs-Mechanik.

### 3.6 Münz-Limit

1. **Kein hartes Spiel-Cap:** Der Münzbestand ist intern als vorzeichenlose Ganzzahl gespeichert und nicht nach oben begrenzt (Speichergrenze liegt weit über Spielwerten).
2. **Anzeige-Referenz 99:** Das UI ist für zweistellige Anzeige ausgelegt. Werte über 99 werden als "99+" angezeigt (Anzeige-Limit, kein Spiel-Limit). Die Balance zielt darauf ab, dass 99 im Normalbetrieb nicht überschritten wird (Erwartungs-Maximum pro Spieler liegt bei 50–70, siehe 3.7).
3. **Keine Abschöpfung:** Es gibt keine Steuer, keine Rundengebühr und keine Obergrenze, die Münzen bei Erreichen von 99 vernichtet.

### 3.7 Münz-Inflation über die Runden

Die Ökonomie ist so ausgelegt, dass die **typischen Münzbestände** (Holdings) über die Partie wie folgt ansteigen:

| Phase | Runden | Typischer Bestand pro Spieler |
|---|---|---|
| Früh | 1–3 | 5–15 Münzen |
| Mittel | 4–6 | 15–30 Münzen |
| Spät | 7–10 | 20–50 Münzen |

**Regeln daraus:**
1. Die Kurve ist eine **Richtlinie** (Balance-Ziel), kein Zwang. Einzelne Spieler können durch Pech oder Sparsamkeit abweichen (0 bis 70).
2. **Einkommens-Ziel:** Pro Spieler und Runde fließen durchschnittlich 6–8 Münzen zu (alle Quellen, über die Partie gemittelt). Damit ist ein Stern (20 Münzen) nach 3–4 Runden erreichbar, wenn der Spieler nicht ausgibt.
3. **Ausgaben-Ziel:** Ein Spieler gibt über die Partie typischerweise 20–60 Münzen aus (1–2 Sterne und/oder 1–3 Items), sodass der Endbestand im Band 20–50 liegt.
4. Die Kurve wird über die Tuning-Knobs (Sektion 7) und die Budget-Tabelle (Sektion 4.2) gesteuert.

### 3.8 Gesamt-Umlauf pro Partie

Der **Gesamtumlauf** (Summe aller jemals zugeflossenen Münzen, unabhängig vom Endbestand) soll pro Partie in einem Zielband liegen:

| Spielerzahl | Runden (Standard) | Ziel-Gesamtumlauf |
|---|---|---|
| 2 | 10 | ca. 150–240 Münzen |
| 4 | 9 | ca. 240–340 Münzen |
| 6–8 | 8 | ca. 320–400 Münzen |

- Der Gesamtumlauf ist die Summe aller Faucets (3.2) inklusive Startguthaben (3.1).
- **Umlauf vs. Bestand:** Der Endbestand aller Spieler zusammen ist der Gesamtumlauf minus aller Senken (Stern- und Item-Käufe). Die Differenz ist der "Münzverbrauch" der Partie.
- Abweichungen von mehr als ±20 % vom Zielband sind ein Balance-Signal (Acceptance Criteria).

## 4. Formulas

### 4.1 Minispiel-Auszahlungsfunktion

`P(rank, N)` = Auszahlung für Platz `rank` bei `N` Spielern:

- `rank = 1` → 10
- `rank = 2` → 7
- `rank = 3` → 5
- `rank = 4` → 3
- `rank ≥ 5` → 2 (nur für N ≥ 5)

**Beispiel:** N = 8: Plätze 1..8 → 10, 7, 5, 3, 2, 2, 2, 2. N = 2: 10, 7.

**Erwartungswert pro Minispiel (bei zufälliger Platzierung):**
- N = 4: `(10 + 7 + 5 + 3) / 4 = 25 / 4 = 6,25` Münzen pro Spieler und Minispiel.
- N = 8: `(10 + 7 + 5 + 3 + 2×4) / 8 = 33 / 8 ≈ 4,13`.
- N = 2: `(10 + 7) / 2 = 8,5`.

### 4.2 Budget-Tabelle (Balance-Modell, 4 Spieler, 9 Runden)

| Posten | Wert |
|---|---|
| Startguthaben je Spieler | 10 |
| Minispiele (9 × 6,25 Ø) | 56,25 |
| Münz-Bonus-Felder (≈ 4 Landungen × 5,5 Ø) | 22 |
| Glück/Pech positiv + Ereignis-Zuflüsse | 10–20 |
| Verlierer-Boost + Münz-Magnet | 5–10 |
| **Summe Zufluss je Spieler** | **≈ 100–120** |
| Ausgaben (Stern + Items) | 20–60 |
| **Endbestand je Spieler** | **≈ 20–50** |
| **Gesamtumlauf (4 Spieler)** | **≈ 240–340** |

Die Tabelle ist das Referenzmodell für die Acceptance-Criteria-Balance-Tests.

### 4.3 Einkommens-Zielgleichung

`Einkommen_pro_Runde(Spieler) = (Summe aller Zuflüsse des Spielers) / N_Runden`

- Zielwert: 6–8 Münzen pro Runde.
- Referenzrechnung (4 Spieler, 9 Runden): `≈ 110 / 9 ≈ 12,2` — **Anmerkung:** Der Wert 12,2 liegt über dem Zielband von 6–8. Das Zielband bezieht sich auf **mittlere Runden** nach Abzug der Start-/Spar-Phasen und berücksichtigt, dass frühe Runden wenig und späte Runden viel einbringen. Die Kontrollgröße ist die **Bestandskurve** (3.7), nicht das rohe Einkommen. **Korrekturbefehl:** Liegt der mittlere Endbestand über 60 oder unter 15, werden die Tuning-Knobs (Sektion 7) angepasst.

### 4.4 Zeit bis zum ersten Stern

`Runden_bis_Stern ≈ (20 - Startguthaben) / Einkommen_pro_Runde`

- Mit Startguthaben 10 und Einkommen 6–8/Runde: `≈ 10 / 7 ≈ 1,4` → nach 2–3 Runden ist ein erster Stern realistisch erreichbar, wenn der Spieler nicht ausgibt. Dies ist das Ziel.

### 4.5 Verlust-Begrenzung

`Verlust_effektiv = min(fester Betrag, aktueller Bestand)` für Verlust-Effekte (3.5.2).

- Beispiel: Bestand 3, Pech-Feld −5 → `min(5, 3) = 3` → Bestand 0.
- Beispiel: Bestand 0, Pech-Feld −5 → `min(5, 0) = 0` → Bestand bleibt 0.

## 5. Edge Cases

1. **Bestand 0, Stern-Kauf versucht:** Kauf-Option nicht verfügbar; kein Teilkauf, kein Kredit (3.5.2).
2. **Bestand 0, Pech-Feld:** Verlust 0 (3.5.2); der Spieler "leidet" nicht zusätzlich. Das Feld zählt für die Pechvogel-Kategorie weiterhin nur, wenn ein Verlust > 0 eintrat ([star-economy](star-economy.md) 3.5.1).
3. **Bestand 0, Dieb-Handschuh-Ziel:** Verlust 0, Dieb erhält 0 (3.4); zählt nicht als gewonnene PvP-Interaktion.
4. **Bestand 0, kostenpflichtiges Ereignis:** Die kostenpflichtige Option ist nicht wählbar; der Spieler wählt die kostenlose Alternative (oder die Ausweichwirkung). Ereignis-Details in [field-event](field-event.md).
5. **Minispiel-Gleichstand:** Auszahlung wird addiert und geteilt, Rest verfällt (3.2.1). Beispiel 3 Spieler, Plätze 1–3 gleichauf: `(10 + 7 + 5) / 3 = 22 / 3 = 7` je Spieler, 1 Münze verfällt.
6. **Verlierer-Boost bei 2 Spielern:** Letzter Platz = Platz 2 → Auszahlung 7 + 1 = 8. Der Boost greift in jeder Partie mit 2+ Spielern.
7. **Münz-Magnet auf Verlust-Effekte:** Wirkt nicht. Der Magnet modifiziert ausschließlich Gewinn-Zuflüsse ([catch-up](catch-up.md) Abschnitt 3.8).
8. **Anzeige über 99:** Intern unbegrenzt, Anzeige "99+". In der Balance unerwartet; wird gemeldet, damit die Bestandskurve (3.7) geprüft wird.
9. **Münz-Bonus-Feld mit Münz-Magnet:** Basis 3–8, Verstärkung `+ min(ceil(0,5 × Basis), 5)` (Formel in [catch-up](catch-up.md)). Beispiel Basis 5 → `5 + min(ceil(2,5), 5) = 5 + 3 = 8`.
10. **Rundung bei Transfers und geteilten Plätzen:** Immer **abrunden** (floor). Es werden keine Nachkomma-Münzen geführt.
11. **Münz-Quelle zahlt bei Bestand am Anzeige-Limit:** Da kein hartes Cap existiert, wird der volle Betrag gutgeschrieben; nur die Anzeige kappt bei "99+".
12. **Ereignis gewährt Münzen an "den Letzten" ([catch-up](catch-up.md)):** Zahlung erfolgt aus dem Nichts (Faucet), nicht vom Führenden (keine Umverteilung). Die Gesamtumlauf-Rechnung (3.8) zählt diese Zuflüsse als Faucet.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments (benötigte Systeme)

| System/Kapitel | Art | Status | Verwendung |
|---|---|---|---|
| `design/gdd/star-economy.md` | Peer | Geschrieben | Sternen-Shop als Senke (20 Münzen); Preis-Konsistenz. |
| `design/gdd/core-loop.md` | Peer | Geschrieben | Minispiel-Phase und Feld-Effekte sind die Auslöser der Münz-Bewegungen. |
| `design/gdd/catch-up.md` | Peer | Geschrieben | Verlierer-Boost und Münz-Magnet modifizieren Zuflüsse; Definition "münz-arm". |
| `design/gdd/item-system.md` + `item-*.md` | Quelle | Geplant (noch nicht geschrieben) | Item-Preise (4–10), Dieb-Handschuh-Transfer, Münz-Magnet-Effekt. |
| `design/gdd/field-*.md` (Münz-Bonus, Glück/Pech, Ereignis, Item-Shop) | Quelle | Geplant (noch nicht geschrieben) | Definieren die Beträge der Feld-Zuflüsse und -Abflüsse (Bereiche 3.2/3.3). |
| `design/gdd/minigame-rewards.md` | Quelle | Geplant (noch nicht geschrieben) | Präzisiert die Gleichstands-Auszahlung und Team-Boni; muss Tabelle 3.2.1 spiegeln. |
| `design/gdd/technical-data-structures.md` | Konsument | Geplant (noch nicht geschrieben) | Persistiert Münzbestand (vorzeichenlos, unbegrenzt) und Münz-Statistiken (Sparfuchs-Zähler). |
| `design/gdd/ui-hud.md` | Konsument | Geplant (noch nicht geschrieben) | Zeigt Münzbestand; Anzeige-Limit "99+". |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|---|---|
| `star-economy.md` | Stern-Kauf-Kosten (20) ist hier definiert; die Kauf-Fähigkeit hängt vom Münzbestand ab. |
| `catch-up.md` | Alle Münz-Modifikatoren (Boost, Magnet) müssen die Beträge und Grenzen dieses Dokuments respektieren. |
| `victory-conditions.md` | Tie-Breaker "Münzen" und Bonus-Kategorien "Reichster"/"Sparfuchs" lesen den Münzbestand/-statistiken. |
| `item-thiefglove.md` | Transfer-Regeln (3.4) und Bestand-Obergrenze (min) sind hier definiert. |
| `field-luck.md`, `field-coin-bonus.md` | Feld-Beträge müssen innerhalb der Bereiche aus 3.2/3.3 liegen. |
| `minigame-rewards.md` | Auszahlungstabelle 3.2.1 ist verbindlich; Abweichungen müssen hier gespiegelt werden. |

### 6.3 Design-Entscheidungen (dokumentierte Klärungen)

1. **Startguthaben 10:** Der bible-index listet "Startguthaben" als Münz-Quelle; das Konzept nennt keinen Betrag. Dieses Kapitel legt 10 fest (Begründung in 3.1.3).
2. **Kein hartes Cap, Anzeige-Referenz 99:** Die Formulierung "Maximum 99" wird als Anzeige-/Balance-Referenz interpretiert, nicht als Spiel-Cap (3.6).
3. **Transfers erhalten den Umlauf:** Der Dieb-Handschuh erzeugt/vernichtet keine Münzen (3.4); nur Faucets erhöhen den Gesamtumlauf.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|---|---|---|---|---|
| Startguthaben | Kurve | 0–20 | 10 | Verschiebt die gesamte Bestandskurve (3.7) und die Zeit bis zum ersten Stern (4.4). |
| Minispiel-Auszahlungen | Kurve | ±50 % je Platz | 10/7/5/3/2 | Zentraler Einkommens-Hebel; steuert Gesamtumlauf und Stern-Tempo. |
| Münz-Bonus-Feld-Spanne | Kurve | 2–12 | 3–8 | Feld-Einkommen; wirkt mit Münz-Magnet. |
| Glück/Pech-Spanne | Kurve | ±(2–10) | −6..+6 | Varianz des Feld-Zufalls; größere Spannen = mehr Pech-Schocks. |
| Item-Preise | Kurve | 2–15 | 4–10 (je Item) | Senken-Druck; definieren die Items in `item-*.md`. |
| Stern-Preis | Kurve | 15–30 | 20 | Primäre Senke; abgestimmt mit [star-economy](star-economy.md). |
| Verlierer-Boost | Kurve | 0–3 | +1 | Catch-Up-Stärke ([catch-up](catch-up.md)); erhöht Umlauf bei vielen Spielern. |
| Münz-Magnet-Faktor | Kurve | 0–1,0 (×) | 0,5 (×) | Catch-Up-Verstärkung; Cap 5 (siehe [catch-up](catch-up.md)). |
| Anzeige-Limit | Feel | 99 / 999 | 99 | Nur Darstellung; "99+" oberhalb. |

Alle Knobs liegen in externen Daten-Dateien (`assets/data/`). Jede Änderung erfordert eine Neuberechnung der Budget-Tabelle (4.2) und der Bestandskurve (3.7).

## 8. Acceptance Criteria

Ein QA-Tester oder CI-Hook kann die folgenden Prüfungen ausführen (PASS/FAIL):

1. **Startguthaben:** Jeder Spieler startet mit exakt 10 Münzen. PASS/FAIL.
2. **Auszahlungstabelle:** In Minispielen mit N = 2..8 Spielern werden die Münzen exakt nach Tabelle 3.2.1 vergeben (Stichprobe: je Spielerzahl 5 Minispiele). PASS/FAIL.
3. **Floor 0:** Nach jeder Münz-Änderung ist der Bestand jedes Spielers ≥ 0. Autotest: 100 simulierte Partien mit Zufalls-Events; niemals negativ. PASS/FAIL.
4. **Teilkauf-Verbot:** Stern- und Item-Käufe sind bei unzureichendem Bestand nicht durchführbar. PASS/FAIL.
5. **Verlust-Begrenzung:** Ein Verlust-Effekt (Pech-Feld −5) bei Bestand 3 reduziert auf 0, nicht auf −2. PASS/FAIL.
6. **Transfer-Erhaltung:** Beim Dieb-Handschuh ist `(Verlust des Ziels) = (Gewinn des Diebs)` für alle Bestände (0, 3, 20) und Zielbeträge (5, 10). PASS/FAIL (Autotest).
7. **Gleichstands-Auszahlung:** Geteilte Plätze werden addiert, geteilt, abgerundet; der Rest verfällt. PASS/FAIL (Testfall 3 Spieler gleichauf).
8. **Bestandskurve:** Über 5 Testpartien (4 Spieler, Standard) liegt der mittlere Endbestand je Spieler im Band 20–50; der mittlere Bestand nach Runde 2 im Band 5–15. PASS/FAIL.
9. **Gesamtumlauf:** Der gemessene Gesamtumlauf liegt für 4-Spieler-Partien im Band 240–340 (±20 %). PASS/FAIL.
10. **Erster Stern:** In mindestens 3 von 5 Testpartien kauft ein Spieler den ersten Stern innerhalb der Runden 2–4. PASS/FAIL.
11. **Kein hartes Cap:** Ein konstruierter Bestand von 150 Münzen (Cheat im Test) wird korrekt gespeichert und im UI als "99+" angezeigt; keine Spiel-Logik bricht. PASS/FAIL.
12. **Lesbarkeit:** Jede Münz-Änderung ist im Spiel sichtbar (Animation, Zahlen-Feedback, Ansage bei Minispielen). Manueller Playtest: Beobachter kann bei 10 zufällig gewählten Änderungen alle 10 korrekt benennen. PASS/FAIL.
