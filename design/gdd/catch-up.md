# Catch-Up-Mechaniken — Party Arena Game Bible

> **Teil:** I — Core Game
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/bible-index.md

---

## 1. Overview

Catch-Up-Mechaniken halten eine Partie Party Arena bis zur letzten Runde spannend, ohne den Vorsprung des Führenden zu entwerten. Sie wirken ausschließlich auf die **Sekundärwährung Münzen**, auf die **Verfügbarkeit von Items** und auf **Bonus-Sterne am Spielende** — nie auf Bewegung, Würfel oder Sterne im Spielverlauf. Konkret definiert dieses Kapitel: den **Verlierer-Boost** bei Minispielen (+1 Münze für den Letzten), **rang-bezogene Ereignis-Felder** (z. B. "Der letzte Spieler erhält 5 Münzen"), die **Aufhol-Bonus-Sterne** (Pechvogel, Vielläufer, Entdecker), die **erhöhte Glücks-Würfel-Verfügbarkeit** im Item-Shop für münz-arme Spieler und den passiven **Münz-Magnet** (mehr Münz-Zufluss bei niedrigem Bestand). Das Kapitel legt außerdem die formale **Rang-Metrik** fest, die alle rang-abhängigen Effekte verwenden, definiert den Begriff **"münz-arm"**, setzt ein **Budget-Oberlimit** für die Gesamtstärke aller Catch-Up-Mechaniken und dokumentiert die Anti-Patterns (kein Rubber-Band bei Bewegung, keine Stern-Manipulation). Ziel: Das Spiel bleibt spannend, aber Können wird belohnt — "kein Mario-Kart-Bullshit" (keine künstliche Gleichmacherei der Geschwindigkeit).

## 2. Player Fantasy

Der Rückstand soll sich **hoffnungsvoll, aber nicht beschämend** anfühlen (MDA: Challenge + Fellowship). Der Spieler auf dem letzten Platz erlebt: "Ich bin hinten, aber das Spiel gibt mir Werkzeuge" — ein Extramünzchen im Minispiel, ein freundliches Ereignis, ein günstigerer Glücks-Würfel, ein Münz-Magnet, der aus jedem Feld mehr herausholt. Das erzeugt **Kompetenz durch Perspektive** (SDT): Der Rückstand ist ein Problem, das man mit den richtigen Entscheidungen (Sparsamkeit, Item-Nutzung, Routenwahl) aktiv bearbeiten kann — nicht eine Strafe, die man passiv erleidet. Der Führende wiederum spürt **Ansporn statt Bedrohung**: Sein Vorsprung bleibt bestehen, aber er darf nicht nachlassen, denn die Bonus-Sterne am Ende können das Blatt noch wenden. Die explizite Anti-Regel "kein Extrawürfel für den Letzten" schützt das **Fairness-Gefühl der Bewegung**: Jeder Wurf zählt gleich, und ein Sieg durch reine Würfel-Geschenke wäre unbefriedigend. Die emotionale Verheißung: **"Bis zum letzten Stern ist alles möglich — aber wer besser spielt, gewinnt häufiger."**

## 3. Detailed Rules

### 3.1 Designprinzipien und Anti-Patterns

1. **Prinzip Münz-fokussiert:** Alle aktiven Catch-Up-Mechaniken (während der Partie) wirken auf Münzen oder Item-Verfügbarkeit. Sterne im Spielverlauf sind tabu ([star-economy](star-economy.md) Abschnitt 3.6).
2. **Prinzip Können-zuerst:** Minispiele bleiben reine Leistungssysteme. Der Verlierer-Boost ist ein kleiner Trostpflaster-Zuschlag, kein Ausgleich der Platzierung.
3. **Anti-Pattern A — Kein Bewegungs-Rubber-Band:** Der Würfel, die Bewegungsschritte, die Pfadwahl und die Zug-Reihenfolge werden **niemals** durch den aktuellen Rang modifiziert. Es gibt keinen Extrawürfel, keine verkürzten Distanzen, keine Bonus-Schritte für den Letzten. Verstöße sind Design-Fehler.
4. **Anti-Pattern B — Keine Stern-Manipulation:** Kein Catch-Up-Effekt entzieht, schenkt oder verschiebt Sterne während der Partie (nur die Endwertung vergibt Bonus-Sterne).
5. **Anti-Pattern C — Kein "Führender wird bestraft":** Es gibt keine Mechanik, die dem Führenden Münzen wegnimmt, nur weil er führt (keine "Führungs-Steuer"). Der Münz-Magnet hilft dem Armen, er schadet dem Reichen nicht.

### 3.2 Rang-Metrik (verbindlich für alle rang-abhängigen Effekte)

Die **Standings** ordnen alle Spieler pro Zeitschritt streng. Sortier-Schlüssel (absteigend):

1. Sterne (höher = besser),
2. Münzen (höher = besser),
3. Minispiel-Siege (höher = besser),
4. Spieler-Index (niedriger = besser; deterministischer Tiebreaker aus der Zug-Reihenfolge).

- **Rang 1** = führender Spieler, **Rang N** = letzter Spieler (N = Spielerzahl).
- Die Standings werden **neu berechnet** bei jedem Münz-, Stern- oder Sieg-Update und gelten für alle Effekte im selben Moment. Ein Effekt liest die Standings **zum Zeitpunkt seiner Auslösung** (nicht am Rundenende).
- **"Letzter Spieler"** im Sinne dieses Kapitels = Spieler mit Rang N.
- **"Münz-arm"** (3.3) verwendet eine eigene Metrik (nur Münzen).

### 3.3 Definition "münz-arm"

Ein Spieler ist **münz-arm**, wenn sein **Münz-Rang** (nur nach Münzen sortiert, Tiebreak: Spieler-Index) in der unteren Hälfte liegt:

- `münz-arm ⇔ Münz-Rang ≥ ceil((N + 1) / 2)`
- Beispiele: N = 2 → Münz-Rang 2 (der Ärmere). N = 4 → Münz-Ränge 3 und 4. N = 8 → Münz-Ränge 5 bis 8.
- Diese Definition gilt für den Münz-Magnet (3.8) und die Item-Shop-Verfügbarkeit (3.7).

### 3.4 Verlierer-Boost (Minispiel)

1. **Regel:** In jedem Minispiel, das Münzen nach Platzierung vergibt ([coin-economy](coin-economy.md) 3.2.1), erhält der Spieler auf dem **letzten Platz** zusätzlich zur Platzierungs-Auszahlung **+1 Münze**.
2. **Gleichstand auf dem letzten Platz:** Sind mehrere Spieler auf dem letzten Platz gleichauf, erhalten **alle** diese Spieler +1 Münze.
3. **Reihenfolge:** Der Boost wird **nach** der Platzierungs-Auszahlung addiert und ist in der Ergebnis-Anzeige separat ausgewiesen ("+1 Trostbonus").
4. **Anwendbarkeit:** Greift bei 2–8 Spielern. Bei 2 Spielern ist der Letzte = Platz 2 (erhält 7 + 1 = 8).
5. **Kein Sonderfall Minispiel-Typ:** Der Boost gilt für alle Minispiel-Kategorien, auch Kooperations-Spiele (sofern dort Einzel-Platzierungen vergeben werden; Team-Minisiege sind in [minigame-rewards](minigame-rewards.md) gesondert geregelt).

### 3.5 Rang-bezogene Ereignis-Felder

1. **Vertrag:** Das Ereignis-System ([field-event](field-event.md)) darf die Standings (3.2) abfragen und Effekte rang-abhängig gestalten. Dieses Kapitel definiert die zwei zulässigen Archetypen:
   - **Archetyp "Ziel auf Letzten":** Ein Ereignis wählt den Spieler mit Rang N als Ziel aus (z. B. "Der letzte Spieler erhält 5 Münzen"). Das ist die häufigste, einfachste Form.
   - **Archetyp "Rang-skaliert":** Ein Ereignis gewährt dem auslösenden Spieler einen Betrag, der mit seinem Rückstand wächst (Formel in 4.2). Typisch für Ereignisse, die der Spieler selbst auslöst.
2. **Obergrenze:** Ein einzelnes Ereignis darf durch Rang-Skalierung höchstens **8 Münzen** über dem Basiswert vergeben (Cap). Der Gesamtbetrag eines Ereignisses (Basis + Skalierung) liegt innerhalb der in [coin-economy](coin-economy.md) definierten Ereignis-Spanne 0–10, soweit nicht das Cap mehr zulässt — das Cap gewinnt.
3. **Kein Zwang:** Nicht jedes Ereignis muss rang-bezogen sein. Die Mehrheit der Ereignisse ist rang-unabhängig; rang-bezogene Ereignisse sind eine Teilmenge (Ziel: 20–40 % der Ereignis-Kartei).
4. **Messzeitpunkt:** Die Standings werden beim Auslösen des Ereignisses gelesen (3.2).

### 3.6 Aufhol-Bonus-Sterne

1. Der Bonus-Stern-Pool ([star-economy](star-economy.md) 3.5) enthält mehrere Kategorien mit **Aufhol-Charakter**, die statistisch häufiger an zurückliegende Spieler gehen:
   - **Pechvogel** (meiste Glück/Pech-Felder mit negativem Ergebnis),
   - **Vielläufer** (meiste zurückgelegte Felder),
   - **Entdecker** (meiste verschiedene Felder besucht),
   - **Reichster** (meiste Münzen bei Spielende — begünstigt indirekt Spieler, die **keine** Sterne gekauft und daher Münzen behalten haben).
2. **Keine Gewichtung der Auswahl:** Die 3 von 10 Kategorien werden weiterhin rein zufällig und gleichverteilt gezogen ([star-economy](star-economy.md) 3.5). Es gibt **keine** erhöhte Zieh-Wahrscheinlichkeit für Aufhol-Kategorien — die Spannung der zufälligen Auswahl ist gewollt und verhindert berechenbare "Aufhol-Garantien".
3. **Wirkung:** Wenn Aufhol-Kategorien gezogen werden, profitieren überproportional die Spieler, die im Stern-Ranking hinten liegen. Die Zufälligkeit hält es spannend; die Kategorien machen es möglich.

### 3.7 Item-Shop: erhöhte Glücks-Würfel-Verfügbarkeit für münz-arme Spieler

1. **Regel:** Ist ein Spieler **münz-arm** (3.3), wird bei der **Erzeugung des Item-Shop-Sortiments für diesen Spieler** das Gewicht des Glücks-Würfels im Vergleich zu den anderen Items **verdoppelt**.
   - Ohne Modifikator haben alle 5 Items das gleiche Basisgewicht (1,0) — vorbehaltlich der Sortiments-Logik in [field-item-shop](field-item-shop.md).
   - Für münz-arme Spieler: `Gewicht(Glücks-Würfel) = 2,0`, alle anderen Items bleiben 1,0. Die Zieh-Wahrscheinlichkeit des Glücks-Würfels steigt damit von 1/5 auf 2/6 = 1/3.
2. **Geltungsbereich:** Die Erhöhung gilt pro **Kauf- oder Besuchs-Ereignis** neu (sie wird bei jeder Sortiments-Erzeugung neu ausgewertet). Ist der Spieler beim Betreten des Item-Shops nicht mehr münz-arm (weil er inzwischen Münzen erhielt), entfällt der Bonus.
3. **Kein Preisrabatt (Standard):** Der Glücks-Würfel kostet weiterhin 5 Münzen. Ein Rabatt ist nur als Tuning-Knob vorgesehen (Standard 0 %).
4. **Sichtbarkeit:** Die erhöhte Verfügbarkeit wird dem Spieler **nicht** als "Rabatt" verkauft, sondern erscheint natürlich als Sortiment. Es gibt keinen Hinweis "weil du arm bist" (würde stigmatisieren).

### 3.8 Münz-Magnet (passiv)

1. **Regel:** Ein **münz-armer** Spieler (3.3) erhält auf **Gewinn-Zuflüsse vom Brett** einen Aufschlag:
   - Betroffen: Münz-Bonus-Felder, positive Glück/Pech-Felder, Münz-Zuflüsse von Ereignis-Feldern.
   - **Nicht** betroffen: Minispiel-Auszahlungen (inkl. Verlierer-Boost), Item-Effekte (z. B. Dieb-Handschuh-Gewinn), das Startguthaben.
2. **Formel:** `Zuschlag = min(ceil(0,5 × Basis), 5)`; Auszahlung = `Basis + Zuschlag`. (Details in Sektion 4.1.)
3. **Wirkungsdauer:** Passiv und permanent, solange der Spieler münz-arm ist. Wird er durch die Zuflüsse nicht mehr münz-arm (Münz-Rang steigt über die Schwelle), entfällt der Magnet für die nächste Auszahlung automatisch (Neuberechnung pro Auszahlung).
4. **Kein Schutz vor Verlusten:** Der Magnet verstärkt nur Gewinne; Verluste (Pech-Felder, Ereignis-Kosten) werden nicht abgeschwächt.

### 3.9 Budget-Obergrenze (Gesamtstärke der Catch-Up-Mechaniken)

1. **Zielwert:** Die Summe aller aktiven Catch-Up-Zuflüsse über eine gesamte Partie soll für einen durchgehend letzten Spieler **höchstens ca. 30 Münzen** betragen (≈ 1,5 Stern-Äquivalente). Darunter bleiben die Mechaniken spürbar, ohne den Könnens-Vorsprung zu egalisieren.
2. **Zusammensetzung (Richtwerte für eine 9-Runden-Partie, 4 Spieler):**
   - Verlierer-Boost: ≈ 8–10 Münzen (bei häufigem letzten Platz).
   - Münz-Magnet: ≈ 8–15 Münzen.
   - Rang-bezogene Ereignisse: ≈ 5–8 Münzen.
   - **Summe: ≈ 20–30 Münzen.**
3. **Kontrollgröße:** Die Summe wird im Playtest gemessen (Statistik "Catch-Up-Zufluss" je Spieler). Übersteigt sie 30 Münzen im Mittel über 5 Partien, sind die Tuning-Knobs (Sektion 7) zu senken.
4. **Keine Kompensation nach oben:** Erreicht der Letzte das Budget-Limit, greifen die Mechaniken trotzdem weiter (es gibt keinen Einzel-Cap pro Spieler) — das Limit ist ein Balance-Ziel, kein System-Stopp.

## 4. Formulas

### 4.1 Münz-Magnet

`Auszahlung = Basis + min(ceil(0,5 × Basis), 5)`, gültig für münz-arme Spieler auf Brett-Zuflüsse.

- `Basis` = ursprünglicher Zufluss (3–8 Münz-Bonus, 2–6 Glück, 0–10 Ereignis).
- `Zuschlag` = `min(ceil(0,5 × Basis), 5)`.

| Basis | Zuschlag | Auszahlung |
|---|---|---|
| 3 | min(ceil(1,5), 5) = 2 | 5 |
| 5 | min(ceil(2,5), 5) = 3 | 8 |
| 8 | min(4, 5) = 4 | 12 |
| 10 | min(5, 5) = 5 | 15 |

- Erwartungswerte: Der Magnet erhöht kleine Zuflüsse prozentual stärker (Basis 3 → +67 %) als große (Basis 10 → +50 %).

### 4.2 Rang-Skalierung von Ereignissen

`Betrag = Basis + k × (N - Rang)`, gedeckelt: `Betrag ≤ Basis + 8`.

- `Basis` = ereignisdefinierter Grundbetrag (0–10, siehe [coin-economy](coin-economy.md) 3.3).
- `k` = Skalierungsfaktor des Ereignisses (Standard 1,0 Münze pro Rang-Abstand).
- `N` = Spielerzahl; `Rang` = Standings-Rang des auslösenden Spielers (1 = Führender).
- `(N - Rang)` = Rang-Abstand zum letzten Platz (0 für den Letzten, N−1 für den Führenden).
- Cap: Der Zuschlag `k × (N - Rang)` wird bei 8 gekappt.

**Beispiel:** N = 4, k = 1, Basis = 3.
- Führender (Rang 1): `3 + 1 × 3 = 6` (Abstand 3).
- Letzter (Rang 4): `3 + 1 × 0 = 3` → **Achtung:** Hier erhält der Letzte **weniger**. Rang-Skalierung mit `(N - Rang)` belohnt den Führenden — das ist der **falsche** Archetyp für Catch-Up. Korrekte Aufhol-Skalierung:

`Betrag_aufhol = Basis + k × (Rang - 1)`, gedeckelt `≤ Basis + 8`.

- Führender (Rang 1): `3 + 1 × 0 = 3`.
- Letzter (Rang 4): `3 + 1 × 3 = 6`.
- Beispiel: Letzter, Basis 5, N = 8, Rang 8 → `5 + 1 × 7 = 12`, gedeckelt auf `5 + 8 = 13`? Nein: `min(12, 13) = 12`. (Cap wirkt erst bei sehr großem Rang-Abstand.)

**Verbindliche Formel für Aufhol-Archetyp:** `Betrag = min(Basis + k × (Rang - 1), Basis + 8)`.

### 4.3 Verlierer-Boost

`Auszahlung_letzter = P(N, N) + 1`, wobei `P` die Minispiel-Auszahlungstabelle ist ([coin-economy](coin-economy.md) 3.2.1).

- N = 2: `7 + 1 = 8`. N = 4: `3 + 1 = 4`. N = 8: `2 + 1 = 3`.
- Erwartungswert des Boosts über eine Partie (9 Runden, konstant Letzter): `9 × 1 = 9` Münzen.

### 4.4 Item-Shop-Gewicht

`P(Glücks-Würfel im Sortiment) = Gewicht_GL / Σ Gewichte`.

- Standard: `1/5 = 20 %`. Münz-arm: `2/6 ≈ 33,3 %` (Verdopplung des Gewichts, 3.7).

### 4.5 Catch-Up-Budget

`C_U = Σ (Verlierer-Boost + Münz-Magnet-Zuschläge + Ereignis-Aufhol-Zuschläge)` pro Spieler über die Partie.

- Ziel: `C_U ≤ 30` (3.9) für einen durchgehend letzten Spieler. Messung im Playtest (Statistik-Eintrag).

## 5. Edge Cases

1. **Münz-arm wird durch die Auszahlung selbst beendet:** Der Magnet wird pro Auszahlung neu ausgewertet (3.8.3). Erreicht der Spieler durch den Zufluss einen Münz-Rang oberhalb der Schwelle, greift der Magnet bei der **nächsten** Auszahlung nicht mehr.
2. **Letzter Platz im Minispiel mit mehreren Gleichständen:** Alle Letztplatzierten erhalten +1 (3.4.2). Beispiel 8 Spieler, Plätze 6–8 gleichauf: alle drei erhalten 2 + 1 = 3.
3. **Kooperations-Minispiel mit Team-Wertung:** Einzel-Platzierungen entfallen; der Verlierer-Boost entfällt für dieses Minispiel (Team-Boni in [minigame-rewards](minigame-rewards.md)). Das Spiel meldet "keine Einzelplatzierung" an die Ökonomie.
4. **Ereignis "Ziel auf Letzten", aber der Letzte ist der Auslösende selbst:** Zulässig; er erhält den Betrag (z. B. "Der letzte Spieler erhält 5 Münzen" beim eigenen Landen). Keine Rekursion (das Ereignis endet nach der Auszahlung).
5. **Münz-Magnet auf Ereignis mit Rang-Skalierung:** Beide Modifikatoren sind kombinierbar: Zuerst wird die Ereignis-Skalierung (4.2) berechnet, danach der Magnet-Aufschlag (4.1) auf das skalierte Ergebnis. Beispiel: Letzter, Basis 5, k=1, N=8 → 12; münz-arm → `12 + min(ceil(6), 5) = 12 + 5 = 17`. Das Cap von 8 (Ereignis) gilt nur für die Ereignis-Skalierung; der Magnet ist separat gedeckelt (5).
6. **Alle Spieler münz-arm (Gleichstand bei wenigen Münzen):** Bei N = 2 und gleichem Münzbestand sind beide münz-arm (Münz-Rang 1 und 2, Schwelle = 2). Beide erhalten Magnet-Boni — das ist zulässig und selten.
7. **Münz-Rang-Tiebreak:** Bei gleichem Münzbestand entscheidet der Spieler-Index (3.3). Dies ist deterministisch und für Effekte reproduzierbar.
8. **Verlierer-Boost bei Minispiel mit nur 2 Teilnehmern (8 Spieler, Team-Spiel):** Siehe Edge Case 3; Einzel-Platzierungen entscheiden.
9. **Catch-Up-Budget wird überschritten:** Kein System-Stopp; die Balance-Kontrolle (3.9.3) meldet den Wert in den Playtest-Statistiken. Ein Überschreiten ist kein Fehler, sondern ein Tuning-Signal.
10. **Item-Shop-Besuch als Nicht-Münzarmer nach Verarmung:** Wird der Spieler erst nach Betreten des Shops münz-arm (durch einen vorherigen Effekt im selben Feld-Aufenthalt), gilt das Sortiment des Besuchs (einmal erzeugt). Der Bonus greift beim **nächsten** Besuch.
11. **Führender mit Rang-Skalierungs-Ereignis:** Der Führende erhält den Basiswert ohne Zuschlag (`Rang - 1 = 0`). Kein Nachteil, nur kein Aufhol-Vorteil.
12. **Partie mit 2 Spielern:** Alle Mechaniken greifen; die Münz-arm-Schwelle (Münz-Rang 2) macht den Zweiten immer münz-arm, solange er weniger Münzen hat. Der Verlierer-Boost ist bei 2 Spielern strukturell stark (Platz 2 = 8 Münzen). Dies ist gewollt, da der Zweite in 2-Partien keine weiteren "Hintermänner" hat.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments (benötigte Systeme)

| System/Kapitel | Art | Status | Verwendung |
|---|---|---|---|
| `design/gdd/coin-economy.md` | Peer | Geschrieben | Münz-Beträge, Minispiel-Auszahlungen, Floors; alle Catch-Up-Zuflüsse sind Münz-Faucets. |
| `design/gdd/star-economy.md` | Peer | Geschrieben | Bonus-Stern-Kategorien (Pechvogel, Vielläufer, Entdecker, Reichster); Anti-Regel "keine Stern-Manipulation". |
| `design/gdd/core-loop.md` | Peer | Geschrieben | Minispiel-Phase (Verlierer-Boost) und Runden-Struktur; Messzeitpunkte. |
| `design/gdd/victory-conditions.md` | Peer | Geschrieben | Endabrechnung mit Bonus-Sternen; die Aufhol-Bonus-Sterne fließen dort ein. |
| `design/gdd/dice-movement.md` | Peer | Geschrieben | Liefert Distanz-/Umlauf-Zählung für Vielläufer/Entdecker; bestätigt "kein Bewegungs-Rubber-Band". |
| `design/gdd/field-event.md` | Quelle | Geplant (noch nicht geschrieben) | Implementiert die rang-bezogenen Ereignis-Archetypen (3.5); muss Formel 4.2 nutzen. |
| `design/gdd/field-item-shop.md` | Quelle | Geplant (noch nicht geschrieben) | Implementiert die Sortiments-Gewichtung (3.7); muss die münz-arm-Definition übernehmen. |
| `design/gdd/item-luckydice.md` | Quelle | Geplant (noch nicht geschrieben) | Glücks-Würfel-Verfügbarkeit; Preis 5 bleibt unverändert (kein Rabatt im Standard). |
| `design/gdd/minigame-rewards.md` | Quelle | Geplant (noch nicht geschrieben) | Liefert die Platzierungs-Auszahlung, auf die der Verlierer-Boost aufschlägt. |
| `design/gdd/technical-data-structures.md` | Konsument | Geplant (noch nicht geschrieben) | Persistiert die Catch-Up-Statistik (C_U, Zähler für Bonus-Kategorien). |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|---|---|
| `coin-economy.md` | Muss die Catch-Up-Zuflüsse als Faucets in der Budget-Tabelle (4.2) führen. |
| `star-economy.md` | Bonus-Kategorien mit Aufhol-Charakter sind Teil des Pools (3.5). |
| `field-event.md` | Ereignis-Kartei muss die Archetypen und Formeln dieses Kapitels einhalten. |
| `field-item-shop.md` | Sortiments-Erzeugung muss die münz-arm-Gewichtung anwenden. |
| `victory-conditions.md` | Statistik-Bildschirm zeigt den Catch-Up-Zufluss (optional) und die Bonus-Kategorien. |

### 6.3 Design-Entscheidungen (dokumentierte Klärungen)

1. **Keine Kategorie-Gewichtung:** Aufhol-Bonus-Sterne werden nicht häufiger gezogen (3.6.2). Die Aufhol-Wirkung entsteht über die Kategorien selbst, nicht über manipuliertes Ziehen.
2. **Münz-Magnet als passives System, nicht als Item:** Der bible-index führt `item-coinmagnet.md` als **Item** (Kosten 4, doppelte Erträge für N Felder). Dieses Kapitel definiert den **passiven Catch-Up-Münz-Magnet** (3.8) als **eigenständige Mechanik**. Das Item und der passive Magnet koexistieren; das Item ist in [item-coinmagnet](item-coinmagnet.md) zu spezifizieren. **Abstimmungsbedarf:** Bei Aktivierung des Items erhält ein münz-armer Spieler potenziell beide Effekte (Item ×2 und Magnet +50 %); die Stapelung wird in [item-coinmagnet](item-coinmagnet.md) geregelt.
3. **Korrektur der Skalierungs-Formel:** Rang-Skalierung für Aufhol-Effekte verwendet `(Rang - 1)` (Führender = 0), nicht `(N - Rang)` (4.2). Die falsche Variante würde den Führenden belohnen.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|---|---|---|---|---|
| Verlierer-Boost | Kurve | 0–3 Münzen | +1 | Direkte Stärke des Minispiel-Trostes; wirkt auf den Gesamtumlauf. |
| Münz-Magnet-Faktor | Kurve | 0,0–1,0 | 0,5 | Aufschlag-Prozentsatz auf Brett-Zuflüsse; 0 = deaktiviert. |
| Münz-Magnet-Cap | Kurve | 2–10 | 5 | Maximale Obergrenze des Magnet-Zuschlags pro Auszahlung. |
| Ereignis-Skalierungsfaktor `k` | Kurve | 0–2 | 1 | Stärke der Rang-Skalierung pro Rang-Abstand. |
| Ereignis-Aufhol-Cap | Kurve | 3–12 | 8 | Maximale Obergrenze des Ereignis-Zuschlags. |
| Glücks-Würfel-Gewicht (münz-arm) | Kurve | 1,0–4,0 | 2,0 | Verfügbarkeits-Boost im Item-Shop; 1,0 = deaktiviert. |
| Münz-arm-Schwelle | Kurve | untere 25–75 % | untere 50 % | Wie viele Spieler als münz-arm gelten; 50 % = untere Hälfte. |
| Rabatt für münz-arme Spieler | Kurve | 0–50 % | 0 % | Optionaler Preisrabatt im Item-Shop (Standard: keine Preisänderung). |
| Catch-Up-Budget `C_U` | Gate | 15–50 | 30 | Kontrollgröße der Gesamtstärke; Überschreitung löst Tuning aus (3.9). |
| Aufhol-Kategorie-Anteil | Kurve | 0–100 % | 20–40 % | Anteil rang-bezogener Ereignisse an der Ereignis-Kartei (Richtwert). |

## 8. Acceptance Criteria

Ein QA-Tester oder CI-Hook kann die folgenden Prüfungen ausführen (PASS/FAIL):

1. **Verlierer-Boost:** Der Letztplatzierte eines Minispiels erhält exakt `P(N,N) + 1` Münzen; bei Mehrfach-Gleichstand auf dem letzten Platz erhalten alle diesen Betrag. PASS/FAIL (Test je Spielerzahl).
2. **Kein Bewegungs-Rubber-Band:** Ein Spieler mit Rang 1 und einer mit Rang N erhalten bei gleichem Würfelwurf exakt dieselbe Bewegung (Schrittzahl, Pfadwahl, Tempo). Autotest: Vergleich zweier identischer Züge bei unterschiedlichem Rang. PASS/FAIL.
3. **Rang-Metrik:** Die Standings sortieren korrekt nach Sterne → Münzen → Minispiel-Siege → Index. Ein Effekt liest die Standings zum Auslösezeitpunkt. PASS/FAIL (Referenzprotokoll).
4. **Münz-arm-Definition:** Für N = 2, 4, 8 werden exakt die erwarteten Spieler als münz-arm klassifiziert (3.3). PASS/FAIL.
5. **Münz-Magnet-Formel:** Für Basen 3, 5, 8, 10 liefert der Magnet exakt die Tabelle aus 4.1; er greift nur bei münz-armen Spielern und nur auf Brett-Zuflüsse. PASS/FAIL.
6. **Ereignis-Skalierung:** Ein Test-Ereignis (Basis 3, k = 1, N = 8) zahlt dem Letzten `min(3+7, 3+8) = 10` und dem Führenden 3. Das Cap greift bei großem Abstand. PASS/FAIL.
7. **Item-Shop-Gewichtung:** Ein münz-armer Spieler sieht den Glücks-Würfel in 1/3 der Sortiments-Erzeugungen (über 60 Testbesuche, Toleranz ±20 %); ein nicht-münz-armer in 1/5. PASS/FAIL.
8. **Bonus-Kategorien:** Pechvogel, Vielläufer und Entdecker werden in der Endwertung korrekt gemessen und vergeben (Testpartie mit bekannten Zählern). PASS/FAIL.
9. **Keine Stern-Manipulation:** Kein Catch-Up-Effekt ändert den Stern-Bestand während der Partie (Skript-Scan + Playtest). PASS/FAIL.
10. **Catch-Up-Budget:** In 5 Testpartien (4 Spieler, 9 Runden) liegt der gemittelte `C_U` eines simulierten konstant letzten Spielers bei ≤ 30 Münzen. PASS/FAIL.
11. **Führender nicht bestraft:** Ein Spieler mit Rang 1 verliert durch keine Catch-Up-Mechanik Münzen oder Ressourcen allein wegen seines Rangs. PASS/FAIL (Autotest: keine "Führungs-Steuer" in Effekt-Datenbank).
12. **Erlebbar (Experiential):** In einem Playtest mit gemischtem Können enden Partien spürbar häufiger knapp (Stern-Abstand zwischen Platz 1 und 2 ≤ 1 Stern in mindestens 4 von 5 Partien), ohne dass der bessere Spieler seinen Vorsprung durch Zufall verliert (der Spieler mit den meisten Minispiel-Siegen gewinnt in ≥ 60 % der Partien). PASS/FAIL.
