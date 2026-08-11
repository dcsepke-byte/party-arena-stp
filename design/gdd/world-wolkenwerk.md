# Insel 3: Wolkenwerk — Party Arena Game Bible

> **Teil:** 6 — World
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/world-overview.md (3.2, 3.8)

---

## 1. Overview

Wolkenwerk ist die **dritte Insel** von Aethonia und das erste Board der mittleren Schwierigkeitsstufe (★★★☆☆). Thema ist „Schwebende Himmel": eine Wolkenstadt mit Ballon-Startplattformen, schwebenden Windmühlen, Regenbögen, Wolken-Thronen und Luftströmungen. Das Board führt die mittlere Stufe der Rampen-Levers ein: **Item-Preisstufe 1** (alle Items +1 Münze), **Pech-Strafen von −3 Münzen**, **Ereignisse mit Positions-Effekten** (Turbulenz-Tausch, Windstoß für alle) und **zwei Abzweigungen mit Sonderregeln** (Windkanal-Express mit Zufallsrichtung, Regenbogen-Rutsche als längerer Münz-Pfad). Die geschätzte Spieldauer beträgt 25–35 Minuten (8–10 Runden). Wolkenwerk ist die Heimat des Charakters Pip (Flughörnchen); die Insel ist die dritte Stufe der Schwierigkeits-Rampe und das erste Board, auf dem Abzweigungen echte „Wetten" sind: kurze Risiko-Route vs. lange Belohnungs-Route.

## 2. Player Fantasy

Wolkenwerk fühlt sich an wie **ein fliegender Jahrmarkt über den Wolken**: Man hüpft von Wattewolke zu Wattewolke, gleitet über Regenbögen, wird von Windmühlen angesaugt und durch Kanäle gepustet. Die Fantasie ist „leicht und luftig" — negative Effekte sind niemals böse, sondern slapstickhaft (ein Fallwind raubt Münzen, eine Nebelbank vernebelt den Würfel). Neu gegenüber den ersten beiden Inseln ist das **Risiko-Bewusstsein durch Pfadwahl**: Der Windkanal ist eine verlockende Abkürzung, aber sein Ausgang weht in eine zufällige Richtung; die Regenbogen-Rutsche ist länger, zahlt aber Münzen. ArenaStar schwebt als Ballonpilot über der Startplattform und erklärt die Windkanal-Regel einmalig per Beispiel. Wer hier spielt, soll sich wie ein Wolkensegler fühlen, der den Wind taktisch nutzt — und die erste „richtige" Entscheidung zwischen Schnelligkeit und Sicherheit treffen muss.

## 3. Detailed Rules

### 3.1 Board-Layout und Feld-Tabelle

Feld-Nummerierung: Die 40 Felder bilden eine **geschlossene Schleife** (Feld 0 → Feld 1 → … → Feld 39 → Feld 0). Die Loop-Distanz (LD) eines Feldes ist gleich seinem Index. Abzweigungen sind alternative Routen zwischen zwei Junction-Feldern; ihre Felder tragen die angegebenen Indizes und liegen innerhalb der Schleife (Abweichung von der älteren „Hauptpfad 1–32 / Abzweigung 33–40"-Konvention, siehe 6.3).

Abkürzungen: S = Start, M = Minispiel, C = Münz-Bonus, L = Glück/Pech, E = Ereignis, ST = Stern-Shop, IT = Item-Shop, MS = Meilenstein, J = Junction (Einstieg/Ausstieg).

| Feld | Typ | Beschreibung |
|-----:|-----|--------------|
| 0 | S | Ballon-Startplattform; ArenaStar als Ballonpilot |
| 1 | M | Minispiel (LEICHT) |
| 2 | M | Minispiel (LEICHT) |
| 3 | C | Münz-Bonus +5 (Schäfchenwolken-Bank) |
| 4 | E | Ereignis — **Turbulenz** (gebunden) |
| 5 | M | Minispiel (LEICHT) |
| 6 | M | Minispiel (LEICHT) |
| 7 | L | Pech: Fallwind (−3 Münzen) |
| 8 | M | Minispiel (LEICHT) |
| 9 | IT | Windmühlen-Item-Shop (Preisstufe 1) — **Einstieg Abzweigung A** |
| 10 | M | Abzweigung A: Windkanal-Station 1 (LEICHT) |
| 11 | M | Abzweigung A: Windkanal-Station 2 (LEICHT) |
| 12 | E | Abzweigung A: Windkanal-Station 3 — **Aufwind** (gebunden) |
| 13 | M | Abzweigung A: Windkanal-Station 4 (LEICHT) — **Ausstieg Abzweigung A** |
| 14 | ST | Wolken-Thron (Stern-Shop) |
| 15 | M | Minispiel (MITTEL) — **MS Ballon-Station** |
| 16 | C | Münz-Bonus +3 |
| 17 | M | Minispiel (MITTEL) |
| 18 | L | Glück: Aufwind-Beutel (+5 Münzen) |
| 19 | M | Minispiel (MITTEL) |
| 20 | E | Ereignis — **Regenbogen-Schatz** (gebunden) |
| 21 | M | Minispiel (MITTEL) — **Einstieg Abzweigung B** |
| 22 | M | Abzweigung B: Regenbogen-Rutsche, Regenbogen-Pad 1 (Rutsche: +5 Münzen; sonst Minispiel MITTEL) |
| 23 | M | Abzweigung B: Regenbogen-Rutsche (MITTEL) |
| 24 | M | Abzweigung B: Regenbogen-Rutsche, Regenbogen-Pad 2 (Rutsche: +8 Münzen; sonst Minispiel MITTEL) |
| 25 | IT | Windmühlen-Item-Shop (Preisstufe 1) — **Ausstieg Abzweigung B** |
| 26 | C | Münz-Bonus +8 (Regenbogen-Kaskade) |
| 27 | M | Minispiel (SCHWER) — **MS Regenbogen-Plaza** |
| 28 | ST | Wolken-Thron (Stern-Shop) |
| 29 | M | Minispiel (SCHWER) |
| 30 | E | Ereignis — **Nebelbank** (gebunden) |
| 31 | M | Minispiel (SCHWER) |
| 32 | L | Glück: Sternschnuppen-Fang (+5 Münzen) |
| 33 | M | Minispiel (SCHWER) |
| 34 | M | Minispiel (SCHWER) |
| 35 | C | Münz-Bonus +5 |
| 36 | E | Ereignis — **Windstoß** (gebunden) |
| 37 | M | Minispiel (SCHWER) |
| 38 | ST | Wolken-Thron (Stern-Shop) |
| 39 | M | Minispiel (SCHWER); Loop zu Feld 0 |

Kontrollsummen: START 1, STERN_SHOP 3, ITEM_SHOP 2, EREIGNIS 5, GLUECK_PECH 3, MUENZ_BONUS 4, MINISPIEL 22 → Summe **40**. Minispiel-Tier-Verteilung (Bandgrenzen LD 1–13 LEICHT, 14–26 MITTEL, 27–39 SCHWER, gemäß `field-minigame.md`): LEICHT 8, MITTEL 7, SCHWER 7.

### 3.2 Junctions

| Abzweigung | Felder | Einstieg X | Ausstieg Y | Δ | Charakter |
|-----------|--------|-----------:|-----------:|:--|-----------|
| A — Windkanal | 10–13 | 9 | 13 | −3 | Express-Abkürzung mit Zufallsrichtung am Ende |
| B — Regenbogen-Rutsche | 22–24 | 21 | 25 | +2 | Längerer Umweg mit 2 Münz-Bonus-Erlebnissen |

1. **Windkanal (A, Sonderregel `windkanal_express`):** Wer auf Feld 9 (Junction) landet und den Windkanal wählt, wird in **genau 1 Zug** durch die 4 Stationen (Felder 10–13) von Feld 9 zu Feld 13 getragen. Die Zwischenstationen werden nicht einzeln betreten; ihre Lande-Effekte (Minispiel-Markierung, Ereignis auf Feld 12) entfallen für diesen Durchgang. **Zufallsrichtung am Ende:** Unmittelbar nach dem Auswurf wird eine Richtung gewürfelt: 50 % Auswurf vorwärts auf Feld 14, 50 % Rückwind auf Feld 10. Die Versetzung ist Teil desselben Zugs (keine zusätzlichen Schritte, keine Feld-Effekte an den Auswurf-Feldern — Regel der Effekt-Platzierung, `board-architecture.md` 3.11). Wer den Kanal nicht nimmt, läuft den Hauptpfad normal (Feld 10 → 11 → 12 → 13 mit allen Lande-Effekten).
2. **Regenbogen-Rutsche (B, Sonderregel `regenbogen_gleitfahrt`):** Wer auf Feld 21 (Junction) landet und die Rutsche wählt, gleitet in **6 Zügen** über Feld 22 → 23 → 24 → Regenbogen-Schleife (2 Züge ohne Landung) → Feld 25. Die Rutsche ist damit 2 Züge länger als der Hauptpfad (21 → 25 direkt über 22–24, 4 Züge). **Regenbogen-Pads:** Auf der Rutsche zahlen die Felder 22 (+5 Münzen) und 24 (+8 Münzen) eine Regenbogen-Prämie; die Minispiel-Markierung entfällt auf diesen beiden Feldern während der Rutsche. Feld 23 bleibt ein normales Minispiel-Feld. Die Prämien gelten als Münz-Erträge (keine Verdopplung durch Münz-Magnet, analog `field-coin-bonus.md`).
3. Beide Junctions haben einen **Standard-Pfad** (Hauptpfad) für den Timeout-Fall (5 s, `dice-movement.md` 3.5.2): Standard ist jeweils der Hauptpfad, nicht die Abzweigung.

### 3.3 Feld-Typen und Insel-Besonderheiten

1. **Startfeld (0):** Ballon-Startplattform mit verankertem ArenaStar-Ballon. Lap-Bonus +5, Exakt-Landungs-Bonus +3 (Standard, `field-start.md`).
2. **Stern-Shops (14, 28, 38):** Wolken-Throne auf schwebenden Wolken-Inseln. Preis 20 Münzen (Standard), Statuen-Reihenfolge 14 → 28 → 38 → 14.
3. **Item-Shops (9, 25):** Windmühlen mit Verkaufsladen. **Preisstufe 1** (`world-overview.md` 3.10): Glücks-Würfel 6, Stern-Teleporter 9, Schutzschild 7, Münz-Magnet 5, Dieb-Handschuh 11. Inventar-Limit 3.
4. **Münz-Bonus:** Werte 3, 5 und 8 (Feld 16 = +3, Felder 3/35 = +5, Feld 26 = +8). Erste Landung voll, jede weitere Betretung in derselben Runde halb (`field-coin-bonus.md`).
5. **Glück/Pech (7, 18, 32):** Fest zugeordnete Beträge statt gewichteter Ziehung: Feld 7 = Pech −3, Feld 18 = Glück +5, Feld 32 = Glück +5. Münz-Clamp bei 0 (`field-luck.md`); Schutzschild und Münz-Magnet wirken nicht.
6. **Minispiel-Felder (22):** Kategorie-Bestimmung per Loop-Distanz (`field-minigame.md` 3.5): Die Kategorie des Runden-Minispiels ist das Tier des letzten MINISPIEL-Landefeldes der Runde in Zugreihenfolge; ohne Minispiel-Landung Fallback LEICHT.
7. **Meilenstein-Felder:** Feld 15 (Ballon-Station, ein Luftschiff-Anleger mit rotierendem Propeller) und Feld 27 (Regenbogen-Plaza, ein Platz aus mehreren sich bewegenden Regenbögen). Beide lösen beim ersten Erreichen jeder Partie einen Kamera-Schwenk (≤ 3 s) und einen Vogelschwarm aus; danach normale Felder.

### 3.4 Ereignis-Kartei

Alle 5 Ereignis-Felder (4, 12, 20, 30, 36) sind **fest gebunden** (deterministisch, 1:1 laut Insel-Vorgabe). Eine gewichtete Auslosung ist auf dieser Insel nicht vorgesehen; die Gewichte in `board.json` dienen als Pool-Beschreibung für zukünftige ungebundene Ziehungen und müssen 1,00 ergeben.

| Feld | Ereignis-ID | Effekt (exakt) | Gewicht |
|-----:|-------------|----------------|---------|
| 4 | `turbulenz` | Alle Spieler tauschen ihre Board-Positionen zufällig untereinander (Permutation ohne Fixpunkt; bei genau 2 Spielern tauschen die beiden). Die Versetzung löst keine Feld-Effekte aus. | 0,15 |
| 12 | `aufwind` | Aktiver Spieler wird 5 Felder vorwärts versetzt (auf dem aktuell gewählten Pfad; an Junctions zählt der Hauptpfad). Die Versetzung löst keine Feld-Effekte aus (Effekt-Platzierung). | 0,20 |
| 20 | `regenbogen_schatz` | Aktiver Spieler erhält +8 Münzen. | 0,25 |
| 30 | `nebelbank` | Der nächste Würfelwurf des aktiven Spielers wird um −2 reduziert (Minimum 1). Mehrere Nebelbank-Effekte addieren sich; der Modifikator wird beim nächsten Wurf verbraucht und wirkt auch auf den Glücks-Würfel (1–10), Minimum bleibt 1. | 0,20 |
| 36 | `windstoss` | Alle Spieler werden 2 Felder vorwärts versetzt (eigener Pfad, an Junctions Hauptpfad). Die Versetzung löst keine Feld-Effekte aus. | 0,20 |

Hinweis: `aufwind`, `windstoss` und `turbulenz` sind Bewegungs-/Platzierungs-Ereignisse. Gemäß `board-architecture.md` 3.11 lösen Effekt-Platzierungen grundsätzlich keine Feld-Effekte aus (keine Läden, keine Ereignisse, kein Glück/Pech, keine Minispiel-Markierung); einzige Ausnahme: MUENZ_BONUS halber Bonus. ArenaStar kommentiert jedes Ereignis in einem Popup (Name, Beschreibung, Kommentar; Dauer ≤ 2,5 s).

### 3.5 Shops

1. **Stern-Shops (14, 28, 38):** Standard-Kaufregeln (`field-star-shop.md`): Preis 20, genau 1 Stern pro Shop, Statue wandert 14 → 28 → 38 → 14, Auffüllen in der Rundenende-Wartung. Der Wolken-Thron ist optisch ein erhöhter Sockel, zu dem ein schwebender Treppen-Bogen führt; der Stern rotiert über dem Thron.
2. **Item-Shops (9, 25):** Standard-Angebot (3 aus 5, ohne Zurücklegen), statisch pro Runde, Preisstufe 1 (3.3.3).

### 3.6 Musik und Audio-Cues

1. **Musik:** Harfe und Flöte, BPM 100, **Lydische Tonleiter** (schwebender, „heller" Klang), Charakter „schwebend". Loop-Länge **120 Sekunden**.
2. **Audio-Cues (Pflicht):** Leichtes Windrauschen als Ambiente (−12 dB unter Musik); Harfen-Glissando beim Betreten einer Abzweigung; „Schwupp"-Sound im Windkanal; Regenbogen-Klingeln auf den Rutsche-Pads (22, 24); Glockenspiel beim Stern-Kauf; „Nebelhorn"-Ton bei Nebelbank.
3. **Dynamik:** Ab Runde 6 (von 8–10) wird eine zweite Flöten-Stimme plus ein leichter Luft-Percussion-Effekt addiert (Übergang ≥ 3 s). Insel-Intro: eigenes 5-Sekunden-Arrangement (Harfen-Arpeggio + Flöten-Motiv über den Wolken).

### 3.7 Visuelle Besonderheiten

1. **Farbwelt:** Hellblau `#87ceeb` (Himmel), Weiß `#ffffff` (Wolken), Regenbogen-Multicolor (Deko, Rutsche, Plaza). Farbabstand ΔHue ≥ 30° erfüllt (`vision-pillars.md`).
2. **Parallax-Wolken:** 3 Ebenen vorbeiziehender Wolken (langsam/mittel/schnell) als Hintergrund-Parallax; die Ebenen liegen unterhalb der Spiel-Ebene und interagieren nicht mit Feldern.
3. **Animierte Regenbögen:** Regenbögen als gebogene Meshes mit Shader-Farbverlauf und sanfter Wellen-Animation; auf der Regenbogen-Rutsche als aktive Gleitfläche.
4. **Brief-Vögel:** 4–6 Vögel fliegen auf geschlossenen Splines; zwei tragen sichtbar Briefe (rote und blaue Briefumschläge) — reine Deko, keine Interaktion.
5. **Ballon-Deko:** Jeder zweite Feld-Rand trägt einen kleinen Helium-Ballon, der beim Landen eines Spielers leicht schwingt (Mikro-Interaktion).
6. **Spielzeug-Ästhetik:** Wolken aus glänzendem, plastikartigem Material mit weichen Kanten; keine fotorealistischen Texturen.
7. **Silhouetten-Test:** Die Windmühle (schmale Rotorblätter) und der Wolken-Thron (breiter Sockel mit Stern) sind in Miniatur (≤ 64 px) eindeutig unterscheidbar.

### 3.8 Board-Dateien

1. **`board.tscn`:** 3D-Szene mit 40 Feld-Markern (Feld 0–39), Junction-Pfeilen an 9 und 21, Kamera-Spline für das Insel-Intro (Start über der Startplattform → Ballon-Station → Regenbogen-Plaza → zurück zu Feld 0), Parallax-Wolken, Regenbogen-Meshes, Windmühlen-, Thron- und Ballon-Instanzen.
2. **`board.gd`:** Feld-Auflösung (alle 40 Felder), gebundene Ereignis-Zuordnung (3.4), Shop-Logik (3.5), Meilenstein-Trigger (15, 27), Abzweigungs-Sonderregeln `windkanal_express` und `regenbogen_gleitfahrt` (3.2).
3. **`board.json`:** `id: "wolkenwerk"`, `difficulty: 3`, `colors: ["#87ceeb","#ffffff","#ffd700"]`, `field_distribution: {start:1, star:3, item:2, event:5, luck:3, coin:4, minigame:22}`, `branches: [{id:"A", entry:9, exit:13, fields:[10,11,12,13], delta:-3, rule:"windkanal_express"}, {id:"B", entry:21, exit:25, fields:[22,23,24], delta:2, rule:"regenbogen_gleitfahrt"}]`, `event_pool` (3.4, Gewichte summiert 1,00), `item_price_tier: 1`, `intro_duration: 5`, `milestones: [15, 27]`, `special_rules: ["windkanal_express", "regenbogen_gleitfahrt"]`.

## 4. Formulas

### 4.1 Feldverteilungs-Prüfung

`S + ST + IT + E + L + C + M = 1 + 3 + 2 + 5 + 3 + 4 + 22 = 40` — erfüllt (Formel 4.1 in `world-overview.md`). `M = 30 − ST − E = 30 − 3 − 5 = 22`.

### 4.2 Junction-Differenzen

Formel: `Δ = L_Abzweigung − (Y − X)`, wobei `L_Abzweigung` die Zugzahl der Abzweigung und `(Y − X)` die Zugzahl des Hauptpfad-Segments ist.

- Abzweigung A: `Δ = 1 − (13 − 9) = 1 − 4 = −3` (Express-Abkürzung um 3 Züge; das Zufalls-Ende ist eine Versetzung, kein zusätzlicher Zug).
- Abzweigung B: `Δ = 6 − (25 − 21) = 6 − 4 = +2` (Umweg um 2 Züge).
Beide Werte liegen in `[−3, +3]`.

### 4.3 Minispiel-Tier-Verteilung

Tier(f) = LEICHT für LD 1–13, MITTEL für LD 14–26, SCHWER für LD 27–39. Verteilung der 22 Minispiel-Felder: LEICHT 8 (36,4 %), MITTEL 7 (31,8 %), SCHWER 7 (31,8 %). Kategorie-Wahrscheinlichkeit pro Runde folgt `field-minigame.md` 3.5 (letzte Landung; Fallback LEICHT).

### 4.4 Ereignis-Erwartungswert (aktivierender Spieler)

Da die Ereignisse gebunden sind, ist der Erwartungswert je Ereignis-Feld deterministisch. Über alle 5 Ereignis-Felder gemittelt (aktiver Spieler, Münz-Effekt; Bewegungs-Effekte ohne Münzwert):

`E[ΔMünzen je Ereignis-Landung] = (0 + 0 + 8 + 0 + 0) / 5 = +1,60` Münzen.

Zusätzlich versetzen `aufwind` und `windstoss` Spieler (Tempo), `turbulenz` mischt Positionen (Chaos), `nebelbank` schwächt den nächsten Wurf. Der Erwartungswert ist leicht positiv — passend zur mittleren Schwierigkeitsstufe (negative Ereignisse sind mild).

### 4.5 Schwierigkeits-Score

`D = (ST − 2)·2 + (E − 5)·1 + Preisstufe + Σ_Rampe = (3−2)·2 + (5−5)·1 + 1 + 2 = 5` (Σ_Rampe = 2 Sonderregel-Abzweigungen). D = 5 ist der gemeinsame Wert der mittleren Stufe (Inseln 3 und 4) und liegt monoton über Sonnenstrand (3) und Zuckerwald.

## 5. Edge Cases

1. **Windkanal mit verbleibenden Schritten:** Entscheidet sich ein Spieler auf Feld 9 für den Windkanal, während sein Zug noch Schritte hätte (er steht dort nur als Zwischenschritt), ist die Wahl trotzdem gültig (`dice-movement.md` 3.5). Der Express ersetzt den Rest des Zugs: Der Spieler endet nach dem Kanal-Durchgang, überschüssige Schritte verfallen.
2. **Windkanal-Zufallsrichtung auf Feld 14 (Wolken-Thron):** Die Versetzung auf Feld 14 löst KEINEN Shop-Besuch aus (Effekt-Platzierung). Der Spieler kann dort erst beim nächsten normalen Zug kaufen, wenn er erneut landet.
3. **Windkanal-Zufallsrichtung auf Feld 10:** Feld 10 wird nicht als Minispiel-Landung gewertet (keine Markierung, keine Kategorie-Änderung).
4. **Regenbogen-Pads und Münz-Magnet:** Die Prämien auf den Pads 22/24 werden durch den Münz-Magnet NICHT verdoppelt (analog `field-coin-bonus.md`); sie sind aber normale Münz-Erträge für die Münz-Bilanz.
5. **Regenbogen-Rutsche bei vollem Wurf:** Überschreitet ein Wurf die Rutsche (Landung hinter Feld 25), gelten die Pad-Prämien nicht (man muss auf den Pads landen); die Rutsche selbst ist nur bei aktiver Wahl und verbleibender Schrittzahl betretbar.
6. **Turbulenz bei 2 Spielern:** Die beiden Spieler tauschen ihre Positionen. Bei Effekt-Platzierung werden keine Feld-Effekte ausgelöst.
7. **Turbulenz bei 8 Spielern:** Zufällige Permutation ohne Fixpunkt; jeder Spieler landet auf der Position eines anderen Spielers. Es gibt keine Kollision oder Blockierung (`board-architecture.md` 3.9).
8. **Nebelbank gestapelt:** Zwei Nebelbank-Effekte vor demselben Wurf → Wurf −4 (Minimum 1). Der Glücks-Würfel (1–10) wird ebenfalls reduziert; das Minimum 1 bleibt (`dice-movement.md` 3.1.4).
9. **Nebelbank und ausgesetzter Zug:** Wird der Zug des Spielers vor dem Würfeln übersprungen (z. B. Item/Event), verfällt der Nebelbank-Modifikator nicht; er bleibt bis zum nächsten tatsächlichen Würfelwurf aktiv.
10. **Windstoß über Feld 39 hinaus:** Die Versetzung loop über Feld 39 → 0 → 1; der Lap-Bonus beim Überqueren von Feld 0 wird NICHT gewährt (Effekt-Platzierung, `field-start.md` 3.7).
11. **Ereignis auf dem Windkanal-Feld 12:** Betritt ein Spieler Feld 12 auf dem Hauptpfad (nicht über den Kanal), löst das Ereignis `aufwind` normal aus.
12. **Minispiel-Kategorie durch Rutsche:** Landet der letzte Spieler der Runde auf Feld 23 (Rutsche, Minispiel MITTEL), bestimmt dieses Tier das Runden-Minispiel — identisch zur normalen Regel.
13. **Stern-Shop 38 übersprungen:** Ein großer Wurf über Feld 38 hinaus erlaubt keinen Kauf (kein Drüber-Zählen, `dice-movement.md` 4.3); die Statue wandert erst nach einem tatsächlichen Kauf.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `world-wolkenwerk.md` | Art | Verwendung |
|-------------------------------------|-----|------------|
| `design/gdd/world-overview.md` | Quelle | Rahmenregeln, Preisstufe 1, Junction-Konventionen, Schwierigkeits-Score. |
| `design/gdd/board-architecture.md` | Peer | Feldtypen-Enum, Landen-vs.-Überqueren (3.11), Effekt-Platzierung, Minispiel-Bänder. |
| `design/gdd/field-event.md` | Peer | Ereignis-Popups, Effekt-Platzierungs-Regel, gebundene Ereignis-Konvention. |
| `design/gdd/field-coin-bonus.md` | Peer | Halbierung bei Mehrfach-Besuch, keine Münz-Magnet-Verdopplung. |
| `design/gdd/field-minigame.md` | Peer | Kategorie-Bestimmung per Loop-Distanz, Teilnahme-Regel (alle spielen). |
| `design/gdd/field-start.md` | Peer | Lap-Bonus +5, Exakt-Landungs-Bonus +3. |
| `design/gdd/field-star-shop.md` | Peer | Sternpreis 20, Statuen-Wanderung, Refill. |
| `design/gdd/field-item-shop.md` | Peer | Angebot (3 aus 5), Inventar-Limit 3. |
| `design/gdd/dice-movement.md` | Peer | Pfadwahl-Timeout, Standard-Pfad, kein Drüber-Zählen. |
| `design/gdd/audio-music.md` | Nachgeordnet | Muss das Harfe/Flöte-Theme (120 s Loop, Lydisch) umsetzen. |
| `design/gdd/narrative-flavor.md` | Nachgeordnet | Liefert Insel-Einleitungstext und Ereignis-Flavortexte. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `world-overview.md` | Referenziert Wolkenwerk in Tabelle 3.2/3.8 (Feld-Verteilung; **Hinweis:** Tabelle 3.8 listet aktuell Ereignis 6 / Minispiel 21 — muss auf 5 / 22 korrigiert werden, siehe 6.3). |
| `design/gdd/ui-board.md` | Muss Junction-Pfeile an 9 und 21 sowie die Windkanal-/Rutsche-Wahl darstellen. |
| `design/gdd/technical-data-structures.md` | Muss das `board.json`-Schema mit `fields`/`branches`/`delta` abbilden. |
| `design/gdd/catch-up.md` | Muss die milden Aufhol-Effekte (Regenbogen-Schatz, Glück-Felder) in die Bilanz einrechnen. |
| `character-pip.md` | Pip (Flughörnchen) hat Heimat-Bezug zu Wolkenwerk (Deko/Auftritte). |

### 6.3 Bidirektionalität und dokumentierte Design-Entscheidungen

1. **Nummerierungs-Konvention (Design-Entscheidung):** Dieses Kapitel nummeriert die 40 Felder als geschlossene Schleife 0–39 mit Inline-Abzweigungen (Felder 10–13 bzw. 22–24). Das weicht von `world-overview.md` 3.7 und `board-architecture.md` 3.3 ab (dort: Hauptpfad 1–32 / 0–31, Abzweigungen global 33–40). Die Abweichung ist gewollt (aktuelle Insel-Vorgabe) und muss bei einer späteren Konsolidierung auf die übrigen Insel-Kapitel übertragen werden.
2. **Ereignis-Bindung:** Alle Ereignis-Felder sind fest gebunden (3.4); die ältere gewichtete Auslosung (`field-event.md` 3.4) kommt auf dieser Insel nicht zum Einsatz.
3. **Feld-Verteilung vs. `world-overview.md` Tabelle 3.8:** Wolkenwerk hat 5 Ereignis- und 22 Minispiel-Felder (statt 6/21). Tabelle 3.8 in `world-overview.md` ist entsprechend zu korrigieren (Konfliktregel `bible-index.md` 3.1.2: das Insel-Kapitel ist maßgeblich).
4. **Abzweigungs-Länge vs. Δ-Formel:** Die allgemeine Δ-Formel aus `world-overview.md` 4.3 setzt 4-Felder-Abzweigungen voraus; dieses Kapitel nutzt die verallgemeinerte Form `Δ = L_Abzweigung − (Y − X)` (4.2).

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Windkanal-Auswurf-Wahrscheinlichkeit | Kurve | 50/50 bis 80/20 (vorwärts/rückwärts) | 50/50 | Risiko der Abkürzung; 80/20 macht den Kanal deutlich attraktiver. |
| Windkanal-Rückwind-Ziel | Kurve | Feld 10 bis Feld 12 | Feld 10 | Härte des Fehlschlags (weiter zurück = riskanter). |
| Rutsche-Länge (Schleifen-Züge) | Kurve | 0–3 Extrazüge | 2 | Umweg-Kosten; 0 = gleich lang (Pad-Prämien werden dann deutlich stärker). |
| Regenbogen-Pad-Werte | Kurve | +3 bis +8 | 22:+5, 24:+8 | Attraktivität der Rutsche; mit `coin-economy.md` abstimmen. |
| Pech-Betrag Glück/Pech | Kurve | −2 bis −4 | −3 | Höhe der Fallwind-Strafe (mittlere Stufe). |
| Glück-Betrag Glück/Pech | Kurve | +3 bis +8 | +5 | Belohnungshöhe der Glück-Felder. |
| Nebelbank-Malus | Kurve | −1 bis −3 | −2 | Stärke des Wurf-Modifikators (Minimum 1). |
| Musik-Steigerung ab Runde | Feel | Runde 4–8 | 6 | Zeitpunkt der zweiten Flöten-Stimme. |
| Meilenstein-Kamera-Dauer | Feel | 1–5 s | ≤ 3 s | Länge des Kamera-Schwenks (Flow-Budget). |

## 8. Acceptance Criteria

Ein QA-Tester kann folgende Prüfungen ausführen:

1. **Feldverteilung:** Die 40 Felder entsprechen exakt Tabelle 3.1 (1 Start, 3 Stern-Shops, 2 Item-Shops, 5 Ereignis, 3 Glück/Pech, 4 Münz-Bonus, 22 Minispiel). PASS/FAIL.
2. **Junctions:** An Feld 9 und 21 erscheint eine Pfadwahl; der Windkanal (9→13) kostet 1 Zug und endet mit 50/50 auf Feld 14 oder 10; die Rutsche (21→25) kostet 6 Züge und zahlt auf den Pads 22 (+5) und 24 (+8). PASS/FAIL.
3. **Ereignis-Bindung:** Jedes der 5 Ereignis-Felder löst exakt das in 3.4 gebundene Ereignis aus (4→Turbulenz, 12→Aufwind, 20→Regenbogen-Schatz, 30→Nebelbank, 36→Windstoß). PASS/FAIL.
4. **Stern-Shops:** Auf 14, 28 und 38 kann ein Stern für 20 Münzen gekauft werden; die Statue wandert 14 → 28 → 38 → 14. PASS/FAIL.
5. **Item-Preise:** Windmühlen (9, 25) verkaufen zu Preisstufe 1 (6/9/7/5/11). PASS/FAIL.
6. **Meilensteine:** Beim ersten Erreichen von Feld 15 (Ballon-Station) und 27 (Regenbogen-Plaza) läuft ein Kamera-Schwenk ≤ 3 s. PASS/FAIL.
7. **Audio:** Musik ist Harfe/Flöte, 100 BPM, Lydisch; Loop 120 s; ab Runde 6 zweite Flöten-Stimme. PASS/FAIL.
8. **Visuals:** Parallax-Wolken (3 Ebenen), animierte Regenbögen, Brief-Vögel; Farbpalette `#87ceeb`/`#ffffff`/Regenbogen. PASS/FAIL.
9. **Sonderregeln:** `board.json` führt `special_rules: ["windkanal_express", "regenbogen_gleitfahrt"]`; beide Regeln sind in 3.2 vollständig spezifiziert. PASS/FAIL.
10. **Effekt-Platzierung:** Windkanal-Auswurf, `aufwind`, `windstoss` und `turbulenz` lösen an den Zielfeldern keine Feld-Effekte aus (Autotest mit definiertem Brett). PASS/FAIL.
11. **Erlebbar (Experiential):** Der 2-Minuten-Test aus `vision-pillars.md` (Szenarien A und B) besteht; Wolkenwerk ist an Farbpalette und Musik eindeutig von Sonnenstrand/Zuckerwald unterscheidbar. PASS/FAIL.
