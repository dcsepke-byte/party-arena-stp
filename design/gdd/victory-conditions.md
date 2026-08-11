# Siegbedingungen — Party Arena Game Bible

> **Teil:** I — Core Game
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/bible-index.md

---

## 1. Overview

Dieses Kapitel definiert, wie eine Partie Party Arena endet und wer gewinnt. Nach der letzten Runde (Rundenanzahl laut [core-loop](core-loop.md)) folgt die **Bonus-Stern-Phase** (3 Kategorien aus dem Pool der [star-economy](star-economy.md)), danach die **Endabrechnung**: Gewinner ist, wer die meisten Sterne besitzt. Bei Gleichstand greift eine feste **Tie-Breaker-Hierarchie** — Sterne → Münzen → Minispiel-Siege — und erst wenn diese nicht entscheidet, ein **Sudden-Death-Minispiel** oder ein **geteilter Sieg**. Das Kapitel spezifiziert die Reihenfolge des Spielendes, die Ranglisten-Anzeige (alle 2–8 Plätze, geteilte Ränge), die Siegerehrung durch ArenaStar inklusive Siegerpose sowie den **Statistik-Bildschirm** mit allen gemessenen Werten (Laufstrecke, Minispiel-Platzierungen, gekaufte/genutzte Items, ausgelöste Events, Umläufe, Münz-Statistiken). Es liefert die präzisen Regeln und Formeln, damit ein Programmierer Spielende, Tiebreak und Zeremonie vollständig implementieren kann.

## 2. Player Fantasy

Das Spielende ist der **krönende Höhepunkt** der Arena-Show (MDA: Challenge + Sensation + Fantasy). Die Bonus-Stern-Phase ist der **letzte Nervenkitzel**: Kategorie für Kategorie wird aufgedeckt, und wer bis dahin abgeschlagen war, kann durch Pechvogel oder Vielläufer noch Sterne sammeln — die Rangfolge kann sich in Sekunden verschieben. Die Endabrechnung erzeugt **Anspannung und Ehrgeiz**: Jeder Stern zählt, und ein Münz-Tiebreak kann über Sieg oder Niederlage entscheiden. Das Sudden-Death-Minispiel ist das **Duell auf Messers Schneide** (Challenge + Sensation): Zwei gleichauf liegende Spieler messen sich in einer einzigen Geschicklichkeits-Aufgabe — der ultimative Beweis, dass am Ende Können zählt. Die Siegerehrung liefert das **Belohnungs-Gefühl** (Fantasy + Fellowship): ArenaStar krönt den Sieger mit einer Fanfare, der Charakter spielt seine Siegerpose, und alle Plätze werden gefeiert. Der Statistik-Bildschirm schließlich gibt jedem Spieler **Anerkennung für seine persönlichen Leistungen** (Kompetenz): Auch wer nicht gewonnen hat, sieht seine Stärken ("meiste zurückgelegte Felder", "beste Minispiel-Bilanz"). Die emotionale Verheißung: **"Jede Partie endet mit einem großen, verdienten Finale — und einem Moment für jeden."**

## 3. Detailed Rules

### 3.1 Ablauf des Spielendes (verbindliche Sequenz)

Nach dem Ende der letzten Runde (nach der Stern-Phase der Runde N) läuft exakt diese Sequenz ab:

1. **Ankündigung:** ArenaStar erklärt das Ende der Runden ("Das war die letzte Runde! Jetzt werden die Bonus-Sterne vergeben.").
2. **Bonus-Stern-Phase:** 3 Kategorien werden aus dem Pool gezogen ([star-economy](star-economy.md) 3.5), nacheinander angekündigt und vergeben (Dauer ca. 30–45 s). Nach jeder Kategorie wird der aktuelle Spielstand kurz eingeblendet.
3. **Endabrechnung:** Die finalen Sterne werden berechnet (gekaufte + Bonus-Sterne). Die Rangfolge wird ermittelt (3.4). Etwaige Tie-Breaker werden aufgelöst (3.5, 3.6).
4. **Ranglisten-Anzeige:** Alle Plätze 1 bis N werden als Podium/Liste gezeigt (3.7).
5. **Siegerehrung:** ArenaStar krönt den Sieger; Siegerpose; Konfetti/Fanfare (3.8).
6. **Statistik-Bildschirm:** Alle Spielerstatistiken werden angezeigt (3.9). Von hier führt der Weg zurück ins Menü (oder zur nächsten Partie).

Zwischen den Schritten gibt es **keine** Unterbrechung durch Spielereingaben (außer "Überspringen"-Taste für Animationen). Das Spielende ist nicht abbrechbar.

### 3.2 Bonus-Stern-Phase

1. Die 3 Kategorien werden **vor** der ersten Vergabe gezogen und angekündigt (Reihenfolge der Ankündigung = Reihenfolge der Vergabe).
2. Pro Kategorie: ArenaStar nennt die Kategorie, blendet die Messwerte ein, nennt den/die Sieger und vergibt den Bonus-Stern. Bei Gleichstand erhalten alle Gleichaufstehenden je 1 Stern ([star-economy](star-economy.md) 3.5.2).
3. Die Kategorie-Degenerations-Korrektur (Messwert 0 → Neuauslosung, [star-economy](star-economy.md) Edge Case 9) wird angewendet, **bevor** die Kategorie angekündigt wird — eine nachträgliche Korrektur während der Zeremonie ist nicht zulässig (kein "Ups, neu ziehen" vor Publikum). Die Neuauslosung erfolgt also unmittelbar nach der Ziehung und vor der ersten Ankündigung; wird eine gezogene Kategorie als unerfüllt erkannt, wird sie sofort ersetzt.

### 3.3 Endabrechnung

`Sterne_final(Spieler) = Sterne_gekauft + Sterne_bonus`

- `Sterne_gekauft` = Anzahl der im Spielverlauf gekauften Sterne ([star-economy](star-economy.md) 3.2).
- `Sterne_bonus` = Anzahl der in der Bonus-Stern-Phase erhaltenen Sterne (3.2).

Es gibt keine weiteren Quellen oder Abzüge. Der Stern-Bestand kann nicht sinken ([star-economy](star-economy.md) 3.6).

### 3.4 Rangfolge und Tie-Breaker-Hierarchie

Die Rangfolge wird durch die **Standings-Metrik** bestimmt (identisch zur Metrik in [catch-up](catch-up.md) 3.2):

1. **Sterne** (höher = besser),
2. **Münzen** (höher = besser),
3. **Minispiel-Siege** (höher = besser),
4. **Spieler-Index** (niedriger = besser; deterministischer Tiebreaker aus der Zug-Reihenfolge).

Diese Hierarchie gilt **für alle Plätze**, nicht nur für den Sieg.

**Verbleibender Gleichstand nach Stufe 3:** Haben zwei oder mehr Spieler nach Sterne, Münzen und Minispiel-Siegen exakt denselben Wert, gilt:

- **Für den 1. Platz:** Sudden-Death-Minispiel (3.5), falls möglich; sonst geteilter Sieg (3.6).
- **Für alle anderen Plätze:** Geteilter Rang (3.7), **kein** Sudden-Death.

### 3.5 Sudden-Death-Minispiel

1. **Auslöser:** Exakt zwei oder mehr Spieler sind nach Sterne → Münzen → Minispiel-Siegen auf **Rang 1** gleichauf, und mindestens ein Minispiel aus dem Pool unterstützt die Anzahl der Gleichaufstehenden.
2. **Auswahl:** Aus dem Minispiel-Pool werden nur Minispiele berücksichtigt, die:
   - die Kategorie **Geschicklichkeit** besitzen ([minigame-categories](minigame-categories.md)),
   - eine **eindeutige Siegermöglichkeit** haben (keine Kooperations-Spiele, keine Spiele, die strukturell Gleichstand erzwingen),
   - die **Anzahl der Gleichaufstehenden** als Teilnehmerzahl unterstützen (2–8).
3. **Zufall:** Aus der verbleibenden Menge wird **genau ein** Minispiel per Gleichverteilung gezogen. Die Ziehung erfolgt sichtbar (ArenaStar).
4. **Teilnahme:** Nur die Gleichaufstehenden spielen. Alle anderen Spieler schauen zu (Zuschauer-Modus). Die Platzierung im Sudden-Death-Spiel bestimmt: Der/die Beste wird **Sieger**; die übrigen Teilnehmer behalten die Reihenfolge ihrer Sudden-Death-Platzierung.
5. **Münzen im Sudden-Death:** Das Sudden-Death-Minispiel vergibt **keine** Münzen (keine Auswirkung auf die Ökonomie; es entscheidet nur den Titel).
6. **Erneuter Gleichstand im Sudden-Death:** Endet das Sudden-Death-Spiel selbst mit Gleichstand auf Platz 1 (z. B. bei 3+ Teilnehmern, zwei erreichen dieselbe Höchstleistung), gilt: **geteilter Sieg** zwischen den Besten des Sudden-Death-Spiels (3.6). Es wird **kein zweites** Sudden-Death gespielt.

### 3.6 Geteilter Sieg

1. Ein geteilter Sieg tritt ein, wenn:
   - das Sudden-Death-Spiel nicht möglich ist (kein geeignetes Minispiel für die Teilnehmerzahl oder keine Geschicklichkeits-Spiele im Pool), oder
   - das Sudden-Death-Spiel mit Gleichstand auf Platz 1 endet (3.5.6).
2. Bei geteiltem Sieg werden **alle** gleichauf liegenden Spieler als Sieger geführt (Rang 1 für alle, angezeigt als "Platz 1 — Gleichstand"). Die Krönung erfolgt für alle (3.8).
3. Ein geteilter Sieg ist **kein** Fehlerzustand, sondern ein explizit unterstütztes Ergebnis.

### 3.7 Ranglisten-Anzeige (geteilte Ränge)

1. Die Rangliste zeigt alle Plätze 1 bis N (2–8 Spieler) in absteigender Reihenfolge.
2. **Geteilte Ränge (Standard-Wettbewerbsrangfolge):** Gleichauf liegende Spieler erhalten denselben Rang; der nächste Rang überspringt entsprechend viele Positionen. Beispiel: Rang 1, 2, 2, 4 (zwei Spieler auf Rang 2, niemand auf Rang 3).
3. Geteilte Ränge können bei jedem Platz auftreten (auch bei 1). Die Anzeige stellt Gleichstände optisch klar dar (gleiche Podium-Höhe / gleiche Rangnummer).

### 3.8 Siegerehrung

1. **Ablauf:** ArenaStar verkündet den/die Sieger, spielt eine Krönungs-Animation (Krone erscheint auf dem Charakter), Konfetti und Fanfare folgen.
2. **Siegerpose:** Der/die Sieger-Charakter spielt seine **Siegerpose** (charakterspezifische Animation; Vertrag in [characters-overview](characters-overview.md)).
3. **Dauer:** 5–8 s, per Taste überspringbar.
4. **Mehrfach-Sieger (geteilter Sieg):** Die Zeremonie läuft für alle Sieger nacheinander (jeder erhält Krone und Pose), Dauer entsprechend länger (max. 10 s).
5. **Verlierer-Reaktionen:** Die übrigen Charaktere zeigen eine kurze Reaktion (Applaus/konsterniert), keine Strafe, kein Spott.

### 3.9 Statistik-Bildschirm

Nach der Siegerehrung wird ein Statistik-Bildschirm angezeigt (eine Seite, scrollbar/umblätterbar), der **je Spieler** folgende Werte zeigt:

| Kategorie | Messwert |
|---|---|
| Sterne gesamt | Gekauft + Bonus, aufgeschlüsselt |
| Münz-Bilanz | Start + Einnahmen − Ausgaben = Endbestand; Einnahmen und Ausgaben getrennt |
| Laufstrecke | Zurückgelegte Felder gesamt, Umläufe |
| Minispiele | Siege (Platz 1), Platzierungen (Anzahl je Platz), Durchschnittsplatz |
| Items | Gekaufte Items, genutzte Items, nach Item-Typ |
| Felder | Betretene Ereignis-Felder, Glück/Pech-Felder (positiv/negativ), Münz-Bonus-Felder, verschiedene Felder besucht |
| Events | Ausgelöste Ereignisse (durch Landen) |
| PvP | Gewonnene PvP-Interaktionen ([star-economy](star-economy.md) 3.5.1) |
| Catch-Up | Verlierer-Boosts erhalten, Münz-Magnet-Zuschläge ([catch-up](catch-up.md)) |

1. Die Werte werden aus den Partie-Statistiken gespeist ([technical-data-structures](technical-data-structures.md)); die Bonus-Kategorien-Zähler sind eine Teilmenge davon.
2. Der Bildschirm dient der **Anerkennung** (siehe Player Fantasy) und wird nicht für die Rangfolge neu berechnet — die Rangfolge steht bereits fest (3.4).
3. Am Ende führt ein "Weiter"-Button ins Menü (oder zur nächsten Partie in der Lobby).

## 4. Formulas

### 4.1 Finale Sterne

`Sterne_final(i) = Sterne_gekauft(i) + Sterne_bonus(i)` für Spieler `i`.

- Bereich: `0 ≤ Sterne_final ≤ 99` (Anzeige-Grenze; real ≤ 10).
- Der Sieger ist `argmax_i Sterne_final(i)`.

### 4.2 Rangfolge (Standings-Metrik)

Sortierung absteigend nach Tupel: `(Sterne, Münzen, Minispiel_Siege, -Index)`, wobei `-Index` bedeutet: kleinerer Index gewinnt.

- Deterministisch für jede Partie; kein Zufall in der Rangfolge (Zufall nur bei Bonus-Kategorien und Sudden-Death-Auswahl).

### 4.3 Sudden-Death-Verfügbarkeit

`SD_möglich ⇔ |T| ≥ 2 und |{m ∈ M_skill : Spielerzahl(m) = |T|}| ≥ 1`

- `T` = Menge der Gleichaufstehenden auf Rang 1.
- `M_skill` = Menge der Geschicklichkeits-Minispiele mit eindeutiger Siegermöglichkeit.
- Gilt `SD_möglich = falsch` → geteilter Sieg (3.6).

### 4.4 Geteilte Ränge

Rangzuweisung (Standard-Wettbewerbsrangfolge): Spieler auf gleichem Wert erhalten denselben Rang `r`; der nächste Wert erhält Rang `r + k`, wobei `k` = Anzahl der Spieler mit Rang `r`.

- Beispiel: 4 Spieler, Werte 3 / 2 / 2 / 1 → Ränge 1, 2, 2, 4.

### 4.5 Bonus-Stern-Erwartung

`E[Bonus-Sterne eines Spielers] = Σ_{c ∈ 3 gezogenen} P(Spieler gewinnt Kategorie c)`.

- Ohne Gleichstände: genau 3 Bonus-Sterne insgesamt vergeben; jeder Spieler hat pro Kategorie die Chance `1/N`.
- Mit Gleichständen steigt die Gesamtzahl (max. `3 × N`, [star-economy](star-economy.md) 4.2).

## 5. Edge Cases

1. **Niemand hat Sterne (alle 0):** Die Rangfolge fällt auf Münzen zurück (3.4). Der Spieler mit den meisten Münzen gewinnt. Sind auch Münzen und Minispiel-Siege gleich, gilt Sudden-Death (bei 2+ auf Rang 1) bzw. geteilter Sieg.
2. **3+ Spieler auf Rang 1:** Sudden-Death wird mit allen Gleichaufstehenden gespielt (wenn ein geeignetes Minispiel existiert). Endet es mit zwei Besten gleichauf, ist der Sieg zwischen diesen beiden geteilt (3.5.6); die übrigen Teilnehmer folgen nach ihrer Sudden-Death-Platzierung.
3. **Kein Geschicklichkeits-Minispiel im Pool:** `SD_möglich = falsch` → geteilter Sieg (3.6). Ein Pool ohne Geschicklichkeits-Spiele ist ein Inhalts-Mangel; das Spielende funktioniert trotzdem.
4. **Sudden-Death-Minispiel unterstützt die Teilnehmerzahl nicht (z. B. 7 Gleichaufstehende):** `SD_möglich = falsch` → geteilter Sieg. Alternativ kann die Auswahl auf Minispiele mit Mindest-/Höchstteilnehmerzahl zurückgreifen; ist keine gültig, teilen.
5. **Bonus-Kategorie mit Messwert 0 (alle Spieler):** Neuauslosung vor der Ankündigung (3.2.3, [star-economy](star-economy.md) Edge Case 9). Verhindert, dass "niemand hat etwas getan" allen Sterne schenkt.
6. **Disconnect während der Zeremonie:** Der getrennte Spieler wird in der Rangliste weitergeführt (mit seinem eingefrorenen Stand). Die Siegerehrung zeigt seinen Charakter; der Bot übernimmt keine weiteren Aktionen, da das Spiel vorbei ist.
7. **Geteilter Sieg bei 2 Spielern:** Beide erhalten Rang 1, beide werden gekrönt. Es gibt keinen "besseren" Sieger.
8. **Münz-Gleichstand bei Rang-Nicht-Sieg:** Beispiel: Platz 2 und 3 haben gleiche Sterne und Münzen → beide erhalten Rang 2, der nächste erhält Rang 4 (4.4). Kein Sudden-Death für Nicht-Platz-1.
9. **Spieler-Index als letzter Tiebreaker:** Kann nur dann greifen, wenn Sterne, Münzen UND Minispiel-Siege identisch sind. Da der Index deterministisch ist, gibt es nach Stufe 3 immer eine totale Ordnung — die Frage ist nur, ob für Platz 1 ein Sudden-Death gespielt wird (3.4: bei Gleichstand nach Stufe 3, **bevor** der Index entscheidet). **Präzisierung:** Für Platz 1 wird Sudden-Death **vor** Anwendung des Index-Tiebreakers geprüft; scheitert oder bringt es keinen Sieger hervor, entscheidet der Index (geteilter Sieg tritt nur ein, wenn der Index **keine** Trennung vornimmt — was er immer tut). Daher: **Sudden-Death findet nur statt, wenn nach Stufe 3 Gleichstand besteht und der Index nicht sofort trennen soll.** Für den 1. Platz gilt: Bei Gleichstand nach Stufe 3 wird immer Sudden-Death versucht (3.5); nur wenn es nicht möglich ist oder erneut gleich endet, entscheidet der Index bzw. wird geteilt.
10. **Statistik-Werte bei vorzeitigem Disconnect:** Die Statistiken des getrennten Spielers werden bis zum Disconnect-Zeitpunkt eingefroren und normal angezeigt (kein "leerer" Eintrag).
11. **Partie mit 2 Spielern und Sudden-Death:** 2 Gleichaufstehende → Sudden-Death mit 2 Spielern (falls ein 2-Spieler-Geschicklichkeits-Spiel existiert). Endet das Spiel gleich (sehr selten bei 2 Spielern), teilen sie sich den Sieg.
12. **Überspringen der Zeremonie:** Alle Zeremonie- und Statistik-Animationen sind überspringbar; das **Ergebnis** (Rangliste, Sieger) wird dabei trotzdem vollständig gezeigt. Das Überspringen ändert nie das Ergebnis.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments (benötigte Systeme)

| System/Kapitel | Art | Status | Verwendung |
|---|---|---|---|
| `design/gdd/star-economy.md` | Peer | Geschrieben | Bonus-Stern-Pool, Kategorien, Gleichstands- und Neuauslosungs-Regeln (3.2, 3.5). |
| `design/gdd/coin-economy.md` | Peer | Geschrieben | Münz-Endbestand und Münz-Statistiken für Tie-Breaker und Statistik-Bildschirm. |
| `design/gdd/core-loop.md` | Peer | Geschrieben | Rundenanzahl N und Übergang vom Runden-Loop zum Spielende. |
| `design/gdd/catch-up.md` | Peer | Geschrieben | Rang-Metrik (identische Standings-Definition) und Catch-Up-Statistiken. |
| `design/gdd/minigame-categories.md` | Quelle | Geplant (noch nicht geschrieben) | Definiert die Kategorie "Geschicklichkeit" und die Anforderungen für Sudden-Death-Auswahl. |
| `design/gdd/minigame-architecture.md` | Quelle | Geplant (noch nicht geschrieben) | Unterstützt Zuschauer-Modus und Teilnehmerzahl-Validierung für Sudden-Death. |
| `design/gdd/characters-overview.md` | Quelle | Geplant (noch nicht geschrieben) | Siegerpose-Vertrag für die Zeremonie. |
| `design/gdd/narrative-arena-star.md` | Quelle | Geplant (noch nicht geschrieben) | Moderations-Dialoge für Ankündigung, Krönung, Statistik. |
| `design/gdd/ui-overview.md`, `ui-hud.md` | Konsument | Geplant (noch nicht geschrieben) | Ranglisten- und Statistik-Bildschirm, Podium, Krönungs-UI. |
| `design/gdd/technical-data-structures.md` | Konsument | Geplant (noch nicht geschrieben) | Persistiert alle Statistik-Zähler und das Spielende-Ergebnis (Savegame). |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|---|---|
| `star-economy.md` | Die Bonus-Stern-Phase (3.2) wird hier ausgeführt; Kategorien werden hier konsumiert. |
| `catch-up.md` | Die Standings-Metrik dieses Kapitels (3.4) ist die verbindliche Definition; catch-up nutzt sie. |
| `core-loop.md` | Der Runden-Loop übergibt nach Runde N an dieses Kapitel (Spielende-Übergang). |
| `minigame-architecture.md` | Muss Sudden-Death (ohne Münzen, Zuschauer) als Sondermodus unterstützen. |
| `technical-multiplayer.md` | Muss das deterministische Spielende-Ergebnis über alle Clients synchronisieren. |

### 6.3 Design-Entscheidungen (dokumentierte Klärungen)

1. **Sudden-Death nur für Platz 1:** Tie-Breaker für andere Plätze sind rein deterministisch (geteilte Ränge). Sudden-Death ist dem Titel vorbehalten (3.4, 3.5).
2. **Kein zweites Sudden-Death:** Ein erneuter Gleichstand im Sudden-Death führt zum geteilten Sieg (3.5.6). Das verhindert Endlos-Schleifen und hält die Zeremonie kurz.
3. **Standard-Wettbewerbsrangfolge (1,2,2,4):** Geteilte Ränge überspringen Positionen; dies spiegelt wider, dass ein Gleichstand einen Platz "konsumiert".
4. **Index als letzter Tiebreaker:** Für Nicht-Platz-1 entscheidet der Spieler-Index deterministisch; für Platz 1 wird vorher Sudden-Death versucht (Edge Case 9). Der Index verhindert, dass die Rangfolge jemals undefiniert bleibt.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|---|---|---|---|---|
| Tie-Breaker-Reihenfolge | Gate | fest (Sterne → Münzen → Siege) | fest | Die Reihenfolge ist designfest; Änderung wäre ein Design-Eingriff. Als Knob nur dokumentiert. |
| Sudden-Death aktiv | Gate | An/Aus | An | Bei "Aus": Gleichstand auf Platz 1 → geteilter Sieg ohne Duell. |
| Sudden-Death-Kategorien | Kurve | Teilmenge von Geschicklichkeit | Geschicklichkeit | Erlaubte Minispiel-Kategorien für das Duell. |
| Sudden-Death-Münzen | Kurve | 0–10 | 0 | Ob das Duell Münzen vergibt (Standard: 0, reiner Titelentscheid). |
| Zweites Sudden-Death | Gate | An/Aus | Aus | Erlaubt ein zweites Duell bei erneutem Gleichstand (Standard: geteilter Sieg). |
| Zeremonie-Dauer | Feel | 3–15 s | 5–8 s | Länge der Krönung; überspringbar. |
| Bonus-Kategorien-Anzahl | Gate | 2–5 | 3 | Anzahl der vergebenen Bonus-Sterne (abgestimmt mit [star-economy](star-economy.md)). |
| Statistik-Umfang | Feel | Minimal/Voll | Voll | Grad der Statistik-Anzeige (Zugänglichkeits-Einstellung). |

## 8. Acceptance Criteria

Ein QA-Tester oder CI-Hook kann die folgenden Prüfungen ausführen (PASS/FAIL):

1. **Sequenz:** Nach Runde N läuft exakt die Sequenz 3.1 (Ankündigung → Bonus-Sterne → Endabrechnung → Rangliste → Siegerehrung → Statistik) ab; keine Phase fehlt oder doppelt. PASS/FAIL.
2. **Bonus-Auswahl vor Ankündigung:** Die 3 Kategorien werden vor der ersten Ankündigung gezogen; die Degenerations-Korrektur ersetzt unerfüllte Kategorien **vor** der Zeremonie. PASS/FAIL (Testfall: Partie ohne Pech-Felder, Pechvogel in Ziehung).
3. **Stern-Berechnung:** `Sterne_final = gekauft + bonus` wird korrekt berechnet; der Stern-Bestand sinkt nie. PASS/FAIL (Referenzprotokoll).
4. **Tie-Breaker-Hierarchie:** Bei konstruierten Gleichständen (gleiche Sterne → Münzen → Siege) entscheidet exakt die Hierarchie 3.4. PASS/FAIL (Autotest mit 6 konstruierten Endständen).
5. **Sudden-Death nur Platz 1:** Bei Gleichstand auf Platz 2 oder tiefer wird kein Sudden-Death gespielt; die Spieler teilen den Rang (1,2,2,4). PASS/FAIL.
6. **Sudden-Death-Auswahl:** Das gezogene Minispiel ist aus der Geschicklichkeits-Kategorie, hat eindeutige Siegermöglichkeit und unterstützt die Teilnehmerzahl. PASS/FAIL (Autotest über die Minispiel-Datenbank).
7. **Sudden-Death ohne Münzen:** Das Duell verändert den Münzbestand keines Spielers. PASS/FAIL.
8. **Geteilter Sieg:** Tritt ein, wenn kein geeignetes Minispiel existiert oder das Duell gleich endet; alle Betroffenen werden als Sieger angezeigt und gekrönt. PASS/FAIL (Testfall 3 Gleichaufstehende, Duell endet gleich).
9. **Rangliste:** Alle N Plätze werden angezeigt; geteilte Ränge folgen der Standard-Wettbewerbsrangfolge (1,2,2,4). PASS/FAIL (Testfall mit konstruiertem Tie).
10. **Siegerehrung:** Der Sieger (oder alle geteilten Sieger) erhält die Krone und spielt die Siegerpose; Dauer 5–8 s (bzw. max. 10 s bei geteiltem Sieg); überspringbar. PASS/FAIL (Sichtprüfung).
11. **Statistik-Korrektheit:** Alle in 3.9 gelisteten Werte stimmen mit dem Partie-Verlauf überein (Stichproben-Vergleich gegen Referenz-Protokoll einer Testpartie). PASS/FAIL.
12. **Determinismus:** Bei identischem Partie-Verlauf (gleicher Seed) erzeugen zwei Läufe dasselbe Spielende-Ergebnis inkl. Rangfolge (Sudden-Death-Ziehung ausgenommen, die sichtbar zufällig ist). PASS/FAIL (Autotest).
13. **Erlebbar (Experiential):** In einem Playtest fühlt sich das Spielende als Höhepunkt an (Fragebogen: ≥ 80 % der Spieler bewerten die Siegerehrung als "zufriedenstellend" oder besser); Spieler ohne Siegchance nennen den Statistik-Bildschirm als "wertschätzend". PASS/FAIL.
