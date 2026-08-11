# Insel 1: Sonnenstrand — Party Arena Game Bible

> **Teil:** 6 — World
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/world-overview.md (3.2, 3.8)

---

## 1. Overview

Sonnenstrand ist die **erste Insel** von Aethonia und das offizielle Einsteiger-Board (Schwierigkeit ★☆☆☆☆). Thema ist Urlaub & Wasser: ein tropischer Strand mit kristallklarem Wasser, Korallenriffen, Holzstegen, einem großen Wasserfall und einem Leuchtturm. Das Board vermittelt alle Kern-Mechaniken von Party Arena (Würfeln, Ziehen, Feld-Effekte, Shops, Minispiele, Ereignisse) ohne Sonderregeln: Es gibt keine Abzweigungs-Sonderregeln, keine Item-Preisaufschläge (Preisstufe 0) und nur sanfte negative Effekte. Die geschätzte Spieldauer beträgt 20–30 Minuten (8–10 Runden). Sonnenstrand ist die Default-Insel für neue Profile, für Online-Lobbys ohne gemeinsame Freischaltungen und der funktionale Ersatz des STP-Legacy-Boards KDEValley.

## 2. Player Fantasy

Das Gefühl von Sonnenstrand ist **entspannter Urlaub mit leichter Spannung**: warme Sandfarben, türkises Wasser, Steel-Drum-Musik, Möwen und Krabben. Jeder negative Effekt wird slapstickhaft inszeniert (ein Quallenschwarm zwickt, man watschelt triefnass weiter) statt bedrohlich. Der Spieler soll sich vom ersten Moment wohl und sicher fühlen: Die Wege sind klar, die Abzweigungen gleichwertig, die Ereignisse mild. Die Insel ist die "Willkommensbühne", auf der ArenaStar als Rettungsschwimmer in der Strand-Hütte am Startfeld die Regeln freundlich erklärt. Wer hier gewinnt, soll Lust auf die nächste Insel bekommen — nicht auf Wiedergutmachung.

## 3. Detailed Rules

### 3.1 Board-Layout und Feld-Tabelle

Feld-Nummerierung: Hauptpfad 1–32, Abzweigung A 33–36, Abzweigung B 37–40. Abkürzungen: S = Start, M = Minispiel, C = Münz-Bonus, L = Glück/Pech, E = Ereignis, ST = Stern-Shop, IT = Item-Shop, MS = Meilenstein.

| Feld | Typ | Beschreibung |
|-----:|-----|--------------|
| 1 | S | Strand-Hütte mit ArenaStar als Rettungsschwimmer |
| 2 | M | Minispiel |
| 3 | C | Münz-Bonus +5 |
| 4 | M | Minispiel |
| 5 | M | Minispiel |
| 6 | L | Pech: Quallen-Zwicken (−2 Münzen) |
| 7 | M | Minispiel |
| 8 | IT | Strand-Markt (Item-Shop, Preisstufe 0) |
| 9 | M | Minispiel |
| 10 | M | Minispiel |
| 11 | M | Minispiel |
| 12 | ST | Stern-Shop auf Insel im Wasser |
| 13 | M | Minispiel |
| 14 | C | Münz-Bonus +8 (Muschel-Bank) |
| 15 | M | Minispiel |
| 16 | E | Ereignis — **Einstieg Abzweigung A** (Korallenriff) |
| 17 | M | Minispiel |
| 18 | L | Glück: Bernstein-Fund (+5 Münzen) |
| 19 | C | Münz-Bonus +5 |
| 20 | M | Minispiel + **MS Wasserfall** — **Ausstieg Abzweigung A** |
| 21 | E | Ereignis |
| 22 | M | Minispiel |
| 23 | M | Minispiel |
| 24 | ST | Stern-Shop auf Insel im Wasser |
| 25 | M | Minispiel |
| 26 | E | Ereignis — **Einstieg Abzweigung B** (Klippen) |
| 27 | M | Minispiel |
| 28 | IT | Strand-Markt (Item-Shop) |
| 29 | M | Minispiel |
| 30 | M | Minispiel + **MS Leuchtturm** |
| 31 | M | Minispiel |
| 32 | M | Minispiel — **Ausstieg Abzweigung B**; Loop zu Feld 1 |
| 33 | L | Abzweigung A: Pech (Strömung −2 Münzen) |
| 34 | C | Abzweigung A: Münz-Bonus +8 (Belohnung Korallenriff) |
| 35 | E | Abzweigung A: Ereignis (Quallen-Schwarm gebunden) |
| 36 | ST | Abzweigung A: Stern-Shop auf Insel im Wasser (Ende der Abzweigung) |
| 37 | E | Abzweigung B: Ereignis (Springflut gebunden) |
| 38 | E | Abzweigung B: Ereignis (Muschel-Suche gebunden) |
| 39 | M | Abzweigung B: Minispiel |
| 40 | M | Abzweigung B: Minispiel |

### 3.2 Junctions

| Abzweigung | Felder | Einstieg X | Ausstieg Y | Δ | Charakter |
|-----------|--------|-----------:|-----------:|:--|-----------|
| A — Korallenriff | 33–36 | 16 | 20 | +1 | Umweg (1 Zug länger) mit Risiko-Belohnung |
| B — Klippen | 37–40 | 26 | 32 | −1 | Abkürzung (1 Zug kürzer), ereignisreich |

1. **Korallenriff (A):** Führt durch das Riff über Holzstege. Risiko: Pech-Feld 33 (Strömung −2). Belohnung: Münz-Bonus 34 (+8) und Stern-Shop 36 am Ende. Wer den Umweg nimmt, tauscht einen zusätzlichen Zug gegen eine Stern-Kauf-Gelegenheit und +8 Münzen.
2. **Klippen (B):** Kürzer als der Hauptpfad, dafür mit zwei Ereignis-Feldern (37, 38). Wer die Klippen nimmt, spart einen Zug, riskiert aber negative Ereignisse (Quallen-Schwarm, Springflut). Der Leuchtturm (MS 30) wird auf dieser Route übersprungen, bleibt aber als Landmarke sichtbar.
3. Beide Junctions sind **ohne Sonderregeln** (einfachste Stufe der Rampen-Levers): keine verdeckten Felder, keine Zufallsteleporte, keine Zusatz-Minispiele.

### 3.3 Feld-Typen und Insel-Besonderheiten

1. **Startfeld (1):** Alle Spieler starten vor der Strand-Hütte. ArenaStar steht als Rettungsschwimmer auf dem Hüttendach und moderiert die ersten beiden Runden mit zusätzlichen Hinweisen (Einführungs-Moderation).
2. **Münz-Bonus:** Sonnenstrand nutzt nur positive Beträge (+5 und +8). Der +8-Bonus (Feld 14 und 34) ist die größte Münz-Belohnung der Insel und markiert "lohnende" Bereiche.
3. **Glück/Pech:** Beträge sind mild: Glück +5, Pech −2 (statt −3 auf späteren Inseln). Bei 0 Münzen verliert der Spieler keine Münzen und erhält stattdessen einen Trost-Sound (siehe 5.2).
4. **Minispiel-Felder:** 21 Minispiel-Felder (höchste Dichte des Spiels zusammen mit der mittleren Gruppe). Jedes Minispiel-Feld markiert das Runden-Minispiel; es wird nach allen Spielerzügen gespielt (siehe `field-minigame.md`).
5. **Meilenstein-Felder:** Feld 20 (großer Wasserfall mit Regenbogen) und Feld 30 (Leuchtturm mit rot-weißem Streifenmuster). Beide lösen beim ersten Vorbeiziehen jeder Partie einen kurzen Kamera-Schwenk (≤ 3 s) und ein Möwen-Kräuschen aus; danach sind sie normale Felder mit ihrem Feldtyp.

### 3.4 Ereignis-Kartei

Alle Ereignis-Felder (16, 21, 26, 35, 37, 38) losen aus dieser Kartei aus. Die gebundenen Felder 35, 37, 38 erzwingen das genannte Ereignis; die übrigen Felder gewichten nach Tabelle.

| Ereignis-ID | Effekt (exakt) | Gewicht |
|-------------|----------------|---------|
| `springflut` | Alle Spieler rücken 3 Felder vor (auf dem aktuell gewählten Pfad; an Junctions wird der Hauptpfad gewählt). | 40 % |
| `muschel_suche` | Aktiver Spieler erhält +5 Münzen. Zusätzlich erhält der Spieler mit dem höchsten Explorations-Wert +3 Münzen. Explorations-Wert = Anzahl verschiedener Felder, auf denen der Spieler in dieser Partie gelandet ist. Gleichstand: keiner erhält die Zusatz-Münzen. | 35 % |
| `quallen_schwarm` | Aktiver Spieler verliert 3 Münzen (Floor 0; bei 0 Münzen stattdessen komische "Zwick"-Animation, kein Münzabzug). | 25 % |

Die gebundene Zuordnung lautet: Feld 35 → `quallen_schwarm`, Feld 37 → `springflut`, Feld 38 → `muschel_suche`. Die Auslosung auf ungebundenen Feldern erfolgt gleichverteilt nach Gewicht, ohne Wiederholungssperre (ein Ereignis kann mehrfach in Folge auftreten).

### 3.5 Shops

1. **Stern-Shops (Feld 12, 24, 36):** Auf Inseln im Wasser stehend, erreichbar über Holzstege. Kaufpreis 20 Münzen (Standard, siehe `star-economy.md`). Die Sternen-Statue wandert nach jedem Kauf auf den nächsten Stern-Shop der Insel (Reihenfolge: 12 → 24 → 36 → 12).
2. **Item-Shops (Feld 8, 28):** Der Strand-Markt verkauft die 5 Standard-Items zur Preisstufe 0 (Würfel 5, Teleporter 8, Schild 6, Magnet 4, Handschuh 10). Inventar-Limit und Ersetzungs-Regel gemäß `field-item-shop.md`.
3. Der Stern-Shop auf Feld 36 liegt am Ende der Korallenriff-Abzweigung: Wer den Umweg nimmt, erhält eine zusätzliche Stern-Kauf-Gelegenheit pro Runde.

### 3.6 Musik und Audio-Cues

1. **Musik:** Steel Drums und Ukulele, BPM 110, Dur-Tonleiter, entspannt. Loop-Länge ca. 60 Sekunden.
2. **Audio-Cues (Pflicht):** Wellenrauschen als ambientes Grundrauschen (leise, −12 dB unter Musik); Möwen-Geschrei als punktuelle Cues an den Meilenstein-Feldern 20 und 30; Glockenspiel-Glissando bei Stern-Kauf; "Platsch"-Sound bei Pech (Quallen-Zwicken) und beim Verlassen der Holzstege.
3. **Dynamik:** Ab Runde 6 (von 8–10) wird die Musik um eine Percussion-Schicht (zusätzliche Congas) angereichert, um die Endphase spannender zu machen (Übergang ≥ 3 s, nicht abrupt). Insel-Intro: eigenes 5-Sekunden-Intro-Arrangement (Ukulele-Arpeggio + Steel-Drum-Motiv).

### 3.7 Visuelle Besonderheiten

1. **Farbwelt:** Türkis `#00f0ff` (Wasser und Himmel), Sandgelb `#f4d58d` (Strand und Stege), Korallenrot `#ff6b6b` (Deko, Riffe, Leuchtturm-Streifen). Die Farben erfüllen den Farbabstand ΔHue ≥ 30° (siehe `vision-pillars.md`).
2. **Animierte Wellen:** Shader-Animation auf allen Wasserflächen; Wellenhöhe und -geschwindigkeit sind dezent (unterhalb der aktiven Spiel-Ebene).
3. **Fliegende Möwen:** 5–8 Möwen fliegen auf einer geschlossenen Spline über das Board; sie weichen nicht der Kamera aus, sind reine Deko.
4. **Krabben an Feldrändern:** An jedem zweiten Feld sitzt eine animierte Krabbe, die beim Landen eines Spielers auf ihrem Feld kurz zur Seite wackelt (Mikro-Interaktion).
5. **Spielzeug-Ästhetik:** Wasserflächen aus glänzendem, plastikartigem Material; Strand mit glatten Sand-Wellen; keine fotorealistischen Texturen.
6. **Silhouetten-Test:** Der Leuchtturm (rot-weiß, schlank) und die Strand-Hütte (breit, mit Stern-Wetterfahne) sind in Miniatur (≤ 64 px) eindeutig unterscheidbar.

### 3.8 Board-Dateien

1. **`board.tscn`:** 3D-Szene mit 40 Feld-Markern (Feld 1–40), Junction-Pfeilen an 16 und 26, Kamera-Spline für das Insel-Intro (Start über dem Wasserfall → Schwenk zum Leuchtturm → Ende auf Feld 1), Wasser-Shader-Flächen, Strand-Hütte, Leuchtturm, Möwen-/Krabben-Instanzen.
2. **`board.gd`:** Implementiert Feld-Auflösung (alle 40 Felder), Ereignis-Kartei mit Gewichten (3.4), Shop-Logik (3.5), Meilenstein-Trigger (20, 30). Keine Sonderregeln für Junctions.
3. **`board.json`:** `id: "sonnenstrand"`, `difficulty: 1`, `colors: ["#00f0ff","#f4d58d","#ff6b6b"]`, `field_distribution: {start:1, star:3, item:2, event:6, luck:3, coin:4, minigame:21}`, `branches: [{id:"A", entry:16, exit:20, fields:[33,34,35,36]}, {id:"B", entry:26, exit:32, fields:[37,38,39,40]}]`, `event_pool` (3.4), `item_price_tier: 0`, `intro_duration: 5`, `milestones: [20, 30]`, `special_rules: []`.

## 4. Formulas

### 4.1 Feldverteilungs-Prüfung

`S + ST + IT + E + L + C + M = 1 + 3 + 2 + 6 + 3 + 4 + 21 = 40` — erfüllt (Formel 4.1 in `world-overview.md`). `M = 30 − ST − E = 30 − 3 − 6 = 21`.

### 4.2 Junction-Differenzen

- Abzweigung A: `Δ = 5 − (Y − X) = 5 − (20 − 16) = 5 − 4 = +1` (Umweg).
- Abzweigung B: `Δ = 5 − (32 − 26) = 5 − 6 = −1` (Abkürzung).
Beide Werte liegen in `[−3, +3]`.

### 4.3 Ereignis-Wahrscheinlichkeiten

Auf ungebundenen Ereignis-Feldern: `P(springflut) = 0,40`, `P(muschel_suche) = 0,35`, `P(quallen_schwarm) = 0,25`. Die Summe ist 1,00. Erwartungswert des Münz-Effekts für den aktiven Spieler auf einem ungebundenen Ereignis-Feld: `E = 0,40·0 + 0,35·5 + 0,25·(−3) = 0 + 1,75 − 0,75 = +1,00` Münze (netto leicht positiv, einsteigerfreundlich).

### 4.4 Schwierigkeits-Score

`D = (ST − 2)·2 + (E − 5)·1 + Preisstufe + Σ_Rampe = (3−2)·2 + (6−5)·1 + 0 + 0 = 2 + 1 = 3`. Keine Sonderregeln, daher `Σ_Rampe = 0`. D ist der niedrigste Wert aller Inseln (monoton steigende Rampe beginnt hier).

## 5. Edge Cases

1. **Springflut an der Junction:** Bewegt "Springflut" einen Spieler über ein Junction-Feld, wird automatisch der Hauptpfad gewählt; es erscheint keine Pfadwahl-Abfrage.
2. **Springflut über Feld 32 hinaus:** Rücken alle Spieler 3 Felder vor, wird über Feld 32 → 1 → 2 geloopt; der Loop zählt normal (siehe `dice-movement.md`).
3. **Muschel-Suche bei Gleichstand:** Höchster Explorations-Wert mehrfach vergeben → die Zusatz-Münzen entfallen; der Basis-Bonus (+5) wird immer gezahlt.
4. **Quallen-Schwarm bei 0 Münzen:** Kein Abzug, stattdessen Trost-Animation; der Kontostand wird nie negativ (Floor 0).
5. **Stern-Shop 36 über die Abzweigung verpasst:** Ein Spieler, der Feld 36 durch Überspringen (großer Wurf) passiert, kann dort nicht kaufen; die Sternen-Statue wandert erst nach einem tatsächlichen Kauf. Der nächste Kaufpunkt ist Feld 12.
6. **Klippen-Abkürzung überspringt Leuchtturm:** Der Meilenstein-Trigger von Feld 30 wird nur ausgelöst, wenn ein Spieler auf Feld 30 anhält oder es passiert (passieren genügt für den visuellen Trigger). Nimmt ein Spieler die Klippen, sieht er den Leuchtturm als Landmarke, der Kamera-Schwenk entfällt für diesen Durchlauf.
7. **Münz-Magnet auf Sonnenstrand:** Der Münz-Magnet verdoppelt Münz-Bonus- und Glück-Erträge gemäß `item-coinmagnet.md`; die +8-Boni von Feld 14 und 34 zählen als Münz-Erträge (verdoppelbar).
8. **Ereignis-Wiederholung:** Ein ungebundenes Feld kann zweimal in Folge dasselbe Ereignis auslösen; das ist erlaubt (keine Wiederholungssperre), die Auslosung erfolgt jedes Mal unabhängig.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `world-sonnenstrand.md` | Art | Verwendung |
|---------------------------------------|-----|------------|
| `design/gdd/world-overview.md` | Quelle | Rahmenregeln, Feld-Verteilung (3.8), Preisstufe 0, Junction-Konventionen. |
| `design/gdd/star-economy.md` | Peer | Sternpreis 20, wandernde Statue, Kaufreihenfolge. |
| `design/gdd/item-system.md` | Peer | Basis-Preise und Inventarregeln der 5 Standard-Items. |
| `design/gdd/field-minigame.md` | Peer | Minispiel-Trigger nach allen Spielerzügen. |
| `design/gdd/dice-movement.md` | Peer | Loop über Feld 32, Bewegungsregeln an Junctions. |
| `design/gdd/audio-music.md` | Nachgeordnet | Muss das Steel-Drum/Ukulele-Theme und die Runde-6-Percussion umsetzen. |
| `design/gdd/narrative-flavor.md` | Nachgeordnet | Liefert Insel-Einleitungstext und Ereignis-Flavortexte. |
| `design/gdd/technical-fork-strategy.md` | Nachgeordnet | KDEValley-Ersatz (Übergang). |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `world-overview.md` | Referenziert Sonnenstrand in Tabelle 3.2/3.8 (Feld-Verteilung 3/6/21). |
| `design/gdd/ui-board.md` | Muss Junction-Pfeile an 16 und 26 darstellen. |
| `design/gdd/technical-data-structures.md` | Muss das `board.json`-Schema für Sonnenstrand abbilden. |
| `design/gdd/catch-up.md` | Muss die milden Aufhol-Effekte (Ereignisse) in die Catch-up-Bilanz einrechnen. |

### 6.3 Bidirektionalität

Sonnenstrand ist das Referenz-Board für die Einsteiger-Stufe: `world-overview.md` definiert den Rahmen, dieses Kapitel die konkreten Werte. Jede Änderung der Feld-Verteilung erfordert die Aktualisierung von Tabelle 3.8 in `world-overview.md`. Der Bible-Index listet das Kapitel als `world-sonnenstrand.md`.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Pech-Betrag Glück/Pech | Kurve | −2 bis −3 | −2 | Milde Strafe; höhere Werte machen die Insel schwerer. |
| Glück-Betrag Glück/Pech | Kurve | +3 bis +8 | +5 | Belohnungshöhe der Glück-Felder. |
| Münz-Bonus-Beträge | Kurve | +3 bis +10 | +5 / +8 | Höhe der Münz-Boni; steuert das Münz-Tempo der Insel. |
| Ereignis-Gewichte | Kurve | Summe = 1,00 | 40/35/25 | Verteilung der Ereignis-Kartei; je negativer das Ereignis, desto niedriger das Gewicht. |
| Explorations-Bonus | Kurve | 0–5 Münzen | 3 | Zusatz-Belohnung für den "Entdecker"; belohnt häufiges Landen. |
| Wohlfühl-Schwelle Runde 6 (Musik-Percussion) | Feel | Runde 4–8 | 6 | Zeitpunkt der Musik-Steigerung; beeinflusst die Spannungskurve. |
| Meilenstein-Kamera-Dauer | Feel | 1–5 s | ≤ 3 s | Länge des Kamera-Schwenks; zu lang bricht den Flow (Budget-Regel). |

## 8. Acceptance Criteria

Ein QA-Tester kann folgende Prüfungen ausführen:

1. **Feldverteilung:** Die 40 Felder entsprechen exakt Tabelle 3.1 (1 Start, 3 Stern-Shops, 2 Item-Shops, 6 Ereignis, 3 Glück/Pech, 4 Münz-Bonus, 21 Minispiel). PASS/FAIL.
2. **Junctions:** An Feld 16 und 26 erscheint eine Pfadwahl; die Abzweigungen A (16→20) und B (26→32) sind 4 Felder lang und führen wie in 3.2 spezifiziert wieder auf den Hauptpfad. PASS/FAIL.
3. **Ereignis-Kartei:** Alle 6 Ereignis-Felder lösen ein Ereignis aus 3.4 aus; die gebundenen Felder 35/37/38 erzwingen das richtige Ereignis; die Gewichte summieren sich zu 1,00. PASS/FAIL.
4. **Stern-Shops:** Auf 12, 24 und 36 kann ein Stern für 20 Münzen gekauft werden; die Statue wandert 12 → 24 → 36 → 12. PASS/FAIL.
5. **Item-Preise:** Strand-Markt (8, 28) verkauft zu Preisstufe 0 (5/8/6/4/10). PASS/FAIL.
6. **Meilensteine:** Beim ersten Erreichen von Feld 20 (Wasserfall) und 30 (Leuchtturm) läuft ein Kamera-Schwenk ≤ 3 s. PASS/FAIL.
7. **Audio:** Musik ist Steel Drums/Ukulele, 110 BPM, Dur; ab Runde 6 kommt eine Percussion-Schicht hinzu. PASS/FAIL.
8. **Visuals:** Wellen animiert, Möwen fliegen, Krabben reagieren; Farbpalette exakt `#00f0ff`/`#f4d58d`/`#ff6b6b`. PASS/FAIL.
9. **Sonderregeln:** `board.json` führt `special_rules: []`; es gibt keine Abzweigungs-Sonderregeln. PASS/FAIL.
10. **Erlebbar (Experiential):** Der 2-Minuten-Test aus `vision-pillars.md` (Szenarien A und B) besteht mit einer Testperson ohne Vorkenntnisse. PASS/FAIL.

