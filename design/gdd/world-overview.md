# Welt-Übersicht: Aethonia — Party Arena Game Bible

> **Teil:** 6 — World
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md (Abschnitt "Welt: Aethonia"), design/gdd/bible-index.md (Teil VI)

---

## 1. Overview

Dieses Kapitel definiert die Welt Aethonia als spielbare Insel-Welt von Party Arena. Aethonia ist ein magischer Kontinent aus **7 schwebenden Inseln plus der Sternenzitadelle**, die als separates Final-Board darüber schwebt. Jede Insel ist genau ein Board mit **40 Feldern**, eigenem Thema, eigener visueller Identität, eigener Musik und eigener Feld-Verteilung. Das Kapitel legt die verbindlichen Rahmenregeln fest, die für alle Insel-Kapitel (`world-sonnenstrand.md` bis `world-sternenzitadelle.md`) gelten: die Schwierigkeits-Rampe von Insel 1 bis 7, die Inselfreischaltung, die Board-Auswahl durch den Host, das 5-Sekunden-Insel-Intro, die 40-Felder-Struktur (Hauptpfad 32 + 2 Abzweigungen je 4), das Board-Dateiformat (`board.tscn`, `board.gd`, `board.json`) und die Ablösung der STP-Legacy-Boards (KDEValley, Test-Board). Jede einzelne Insel wird in ihrem eigenen Kapitel vollständig spezifiziert; dieses Kapitel ist die Dach-Spezifikation und die Konfliktinstanz bei Widersprüchen.

## 2. Player Fantasy

Die Welt Aethonia erzeugt das Gefühl einer **Urlaubsreise durch ein Spielzeug-Paradies**: Der Spieler startet am warmen, entspannten Sonnenstrand und arbeitet sich über den verspielten Zuckerwald, die schwebenden Himmel von Wolkenwerk, den frostigen Frostgipfel, die geheimnisvollen Dschungelruinen und die dröhnende Mechanik-Stadt bis hinauf zur goldenen Sternenzitadelle vor. Jede Insel ist eine neue, sofort erkennbare "Folge" derselben Show: gleiche Regeln, neue Bühne. Das Versprechen ist **Orientierung durch Wiedererkennbarkeit** (jede Insel unterscheidet sich auf einen Blick durch Farbpalette, Formsprache und Musik) und **Fortschritt durch Freischaltung** (neue Inseln sind sichtbare Belohnung für gespielte Partien). Der Host ist der Reiseleiter: Er wählt die Insel aus, und vor jeder Partie fliegt die Kamera in einer 5-Sekunden-Einblendung über die Insel, um die neue Bühne zu präsentieren. Wer alle sieben Inseln bereist und dort Siege errungen hat, öffnet sich den Zugang zur Sternenzitadelle — der Moment soll sich wie das Betreten der letzten, großartigsten Bühne eines Arena-Spektakels anfühlen.

## 3. Detailed Rules

### 3.1 Weltgeographie

1. Aethonia besteht aus 7 Inseln, die im Kreis um eine zentrale, höher schwebende Zitadelle angeordnet sind. Die Inseln sind nummeriert 1–7 in aufsteigender Schwierigkeit; die Sternenzitadelle ist Insel 7 in der Spielreihenfolge, wird aber als eigenständiges Final-Board geführt ("7+1").
2. Jede Insel ist ein Board mit exakt 40 Feldern. Es gibt keine zwei Boards mit identischer Feld-Verteilung.
3. Insel 7 (Sternenzitadelle) wird in der Menü-Darstellung optisch über den anderen Inseln schwebend dargestellt und nur angezeigt, wenn sie freigeschaltet ist.

### 3.2 Insel-Übersichtstabelle

| # | Datei | Insel | Thema | Schwierigkeit | Farbpalette | Musik-Stil | BPM / Tonleiter |
|---|-------|-------|-------|---------------|-------------|------------|-----------------|
| 1 | `world-sonnenstrand.md` | Sonnenstrand | Urlaub & Wasser | ★☆☆☆☆ | Türkis `#00f0ff`, Sandgelb `#f4d58d`, Korallenrot `#ff6b6b` | Steel Drums, Ukulele | 110, Dur, entspannt |
| 2 | `world-zuckerwald.md` | Zuckerwald | Süßigkeiten | ★★☆☆☆ | Rosa `#ff4d6d`, Schokobraun `#8b4513`, Mintgrün `#98ff98` | Glockenspiel, Fagott | 120, Dur, verspielt |
| 3 | `world-wolkenwerk.md` | Wolkenwerk | Schwebende Himmel | ★★★☆☆ | Hellblau `#87ceeb`, Weiß `#ffffff`, Regenbogen (multi) | Harfe, Flöte | 100, Lydisch, schwebend |
| 4 | `world-frostgipfel.md` | Frostgipfel | Eis & Schnee | ★★★☆☆ | Eisblau `#a8d8ea`, Weiß `#f0f0f0`, Violett `#9b59b6` | Celesta, Tremolo-Strings | 90, Moll, kristallin |
| 5 | `world-dschungeltempel.md` | Dschungeltempel | Ruinen | ★★★★☆ | Dschungelgrün `#2d6a4f`, Gold `#ffd700`, Braun `#8b4513` | Marimba, Bongos | 130, Phrygisch, geheimnisvoll |
| 6 | `world-mechanik-stadt.md` | Mechanik-Stadt | Spielzeug-Technik | ★★★★☆ | Silber `#c0c0c0`, Orange `#ff6a00`, Gelb `#ffd34e` | Marimba/Xylophon, Tuba | 140, Mixolydisch, mechanisch |
| 7 | `world-sternenzitadelle.md` | Sternenzitadelle | Finale | ★★★★★ | Gold `#ffd700`, Tiefblau `#1a1a4e`, Magenta `#ff00ff` | Volle Orchester, Chor | 80–160 dynamisch, heroisch |

Zusätzlich hat jede Insel: eine visuelle Besonderheit (siehe Insel-Kapitel), eine Feld-Verteilung (siehe 3.8), ein Event-Theme (siehe 3.11) und Meilenstein-Felder (Landmarken, siehe Insel-Kapitel).

### 3.3 Schwierigkeits-Rampe

Der Schwierigkeitsgrad steigt von Insel 1 bis 7 über **fünf Rampen-Levers** an. Diese Levers sind in den Insel-Kapiteln konkret ausgestaltet:

1. **Abzweigungs-Komplexität:** Einfache Inseln haben gleichlange Abzweigungen ohne Sonderregeln; höhere Inseln haben Abkürzungen, Umwege und Sonderregeln (Floß-Fahrt, Zufalls-Teleport, Geister-Felder).
2. **Ereignis-Dichte und -Schwere:** Anzahl der Ereignis-Felder (5–6) und die Höhe der Münz-Strafen bzw. negativen Effekte steigen.
3. **Item-Preisstufe:** Siehe 3.10 — Items werden auf höheren Inseln teurer.
4. **Glück/Pech-Spanne:** Pech-Strafen steigen von −2 auf −3 Münzen; Bonus-Felder liegen auf höheren Inseln strategisch riskanter.
5. **Stern-Shop-Anzahl und -Position:** 2–3 Stern-Shops auf normalen Inseln, 4 auf der Sternenzitadelle; ab Insel 3 liegen Stern-Shops zunehmend am Ende von Abzweigungen (Risiko-Belohnung).

### 3.4 Inselfreischaltung

Die Freischaltung wird **pro lokalem Profil** gespeichert (Konto-Speicherstand, nicht pro Partie). Als "gespieltes Spiel" zählt jede abgeschlossene Partie (Sieger wurde ermittelt) mit mindestens einem menschlichen Spieler; abgebrochene Partien zählen nicht.

| Insel | Freischalt-Bedingung |
|-------|----------------------|
| Sonnenstrand (1) | Sofort verfügbar |
| Zuckerwald (2) | Sofort verfügbar |
| Wolkenwerk (3) | Sofort verfügbar |
| Frostgipfel (4) | Nach 10 gespielten Spielen |
| Dschungeltempel (5) | Nach 10 gespielten Spielen |
| Mechanik-Stadt (6) | Nach 25 gespielten Spielen |
| Sternenzitadelle (7) | Nach 50 gespielten Spielen ODER wenn alle 7 Inseln je 1× gewonnen wurden |

Regeln:

1. **"Insel gewonnen"** bedeutet: Der Profil-Inhaber hat auf dieser Insel eine Partie gewonnen (meiste Sterne nach der letzten Runde, siehe `victory-conditions.md`). Für die Zitadellen-Freischaltung müssen die Siege auf den Inseln 1–6 UND ein Sieg auf Insel 6 nicht zwingend vorliegen — es genügen Siege auf den Inseln 1–7, sobald Insel 6 erreichbar ist; faktisch sind Siege auf Insel 6 und 7 erst nach 25 Spielen möglich, da die Inseln erst dann freigeschaltet sind. Die Zitadelle selbst kann nicht über "alle gewonnen" vor Insel-6-Freischaltung erreicht werden, da ein Sieg auf Insel 6 einen gespielten Sieg auf Insel 6 voraussetzt, die erst ab 25 Spielen wählbar ist.
2. **Anzeige:** Gesperrte Inseln werden im Auswahl-Bildschirm als Silhouette mit Schloss-Icon und verbleibender Spiel-Anzahl dargestellt (z. B. "Noch 4 Spiele"). Die konkrete Zahl wird live aus dem Speicherstand berechnet.
3. **Host-Berechtigung:** Freigeschaltet sind immer die Inseln des lokalen Profils des Hosts. In Online-Lobbys (falls später implementiert) gilt: Es wird die Schnittmenge aller freigeschalteten Inseln der menschlichen Spieler verwendet; ist die Schnittmenge leer, wird die Partie auf Sonnenstrand erzwungen.

### 3.5 Board-Auswahl

1. Die Insel-Auswahl erfolgt **vor Spielstart** in der Lobby durch den Host (Spieler 1).
2. Der Host wählt aus den freigeschalteten Inseln (siehe 3.4). Danach folgt die Charakter-Auswahl; ein Inselwechsel ist bis zum Partie-Start möglich.
3. Das gewählte Board wird als Plugin geladen (`plugins/boards/INSELNAME/`), siehe 3.12.

### 3.6 Insel-Intro (Kamera-Flug)

1. Vor jedem Partie-Start spielt das Spiel ein **5-Sekunden-Insel-Intro**: Eine Kamera fliegt in einer festen Spline über das Board, zeigt Startpunkt, zentrale Landmarken (Meilenstein-Felder) und mindestens einen Stern-Shop, und endet auf der Startposition von Spieler 1.
2. Das Intro ist **überspringbar** (Taste A / Klick / Button "Überspringen"). Die Dauer beträgt exakt 5 Sekunden; die Überspring-Funktion ist ab Sekunde 1 aktiv.
3. Das Intro wird von einem kurzen Insel-Titel-Einblender begleitet (Inselname + Schwierigkeitssterne), passend zur Musik des Boards.
4. Für die Sternenzitadelle dauert das Intro ebenfalls 5 Sekunden, endet aber mit einem langsameren Kamera-Zoom auf das Sternenportal (zusätzliche 2 Sekunden, aber Teil desselben Intro; Gesamtdauer 7 Sekunden, überspringbar).

### 3.7 Board-Struktur: 40 Felder

Jedes Board folgt verbindlich dieser Struktur:

1. **Hauptpfad:** 32 Felder, nummeriert 1–32 in Laufreihenfolge. Feld 1 ist das Startfeld. Feld 32 ist das letzte Feld vor dem Loop zurück zu Feld 1.
2. **Zwei Abzweigungen:** Je 4 Felder, global nummeriert 33–40 (Abzweigung A = 33–36, Abzweigung B = 37–40). Jede Abzweigung verbindet zwei Felder des Hauptpfads (Einstieg X, Ausstieg Y). Wer an X ankommt, wählt zwischen Hauptpfad und Abzweigung.
3. **Junction-Differenz:** Die Längendifferenz Δ zwischen Abzweigung und Hauptpfad-Segment ist pro Insel spezifiziert (Formel 4.3). Δ < 0 = Abkürzung, Δ > 0 = Umweg, Δ = 0 = gleich lang.
4. **Feld-Typen:** Jedes der 40 Felder hat genau einen Typ aus: Start, Stern-Shop, Item-Shop, Ereignis, Glück/Pech, Münz-Bonus, Minispiel. Meilenstein-Felder sind keine eigene Kategorie, sondern visuelle Landmarken auf einem Feld beliebigen Typs.
5. **Feld-Verkettung:** Jedes Feld kennt genau einen Folge-Nachbarn (Loop) plus ggf. einen Abzweig-Nachbarn an den Junction-Feldern. Die Verkettung ist azyklisch mit genau einer Schleife (Feld 32 → Feld 1).
6. **Sichtbarkeit:** Alle Felder sind zu jeder Zeit sichtbar (keine verdeckten Felder), außer explizit spezifizierten Sonderfällen (z. B. Eis-Höhlen-Dunkelheit auf Frostgipfel, siehe `world-frostgipfel.md`).

### 3.8 Feld-Verteilung pro Insel

Die Feld-Verteilung variiert **pro Insel** (nicht jedes Board ist identisch). Die gültigen Bereiche sind: Stern-Shops 2–4, Item-Shops genau 2, Ereignis 5–6, Glück/Pech genau 3, Münz-Bonus genau 4, Minispiel = Rest, Start genau 1.

| Insel | Start | Stern | Item | Ereignis | Glück/Pech | Münz-Bonus | Minispiel | Summe |
|-------|------:|------:|-----:|---------:|-----------:|-----------:|----------:|------:|
| Sonnenstrand | 1 | 3 | 2 | 6 | 3 | 4 | 21 | 40 |
| Zuckerwald | 1 | 3 | 2 | 5 | 3 | 4 | 22 | 40 |
| Wolkenwerk | 1 | 3 | 2 | 6 | 3 | 4 | 21 | 40 |
| Frostgipfel | 1 | 3 | 2 | 5 | 3 | 4 | 22 | 40 |
| Dschungeltempel | 1 | 3 | 2 | 6 | 3 | 4 | 21 | 40 |
| Mechanik-Stadt | 1 | 3 | 2 | 6 | 3 | 4 | 21 | 40 |
| Sternenzitadelle | 1 | 4 | 2 | 6 | 3 | 4 | 20 | 40 |

Hinweis: Die Sternenzitadelle überschreitet mit 4 Stern-Shops bewusst den Normalbereich 2–3 (Sonderregel des Final-Boards, siehe `world-sternenzitadelle.md`).

### 3.9 Abzweigungs-Konventionen

1. **Wahlmechanik:** Ein Spieler, der auf einem Junction-Feld X landet (oder es über Bewegung passiert und genau dort stehen bleibt), muss sich bei der Fortsetzung seines Zugs für Hauptpfad oder Abzweigung entscheiden. Die Entscheidung wird als Pfadwahl-Pfeil dargestellt (siehe `ui-board.md`). Passiert ein Spieler das Junction-Feld ohne anzuhalten, wird die Wahl automatisch auf den Hauptpfad gesetzt.
2. **Längenbilanz:** Jede Abzweigung ist in den Insel-Kapiteln mit Einstieg X, Ausstieg Y und Differenz Δ spezifiziert. Die Summe aus Abzweigungs- und Hauptpfad-Feldern bleibt immer 40.
3. **Sonderregeln:** Ab Insel 2 dürfen Abzweigungen eigene Sonderregeln besitzen (Floß-Fahrt, Zuckerwatte-Bonus-Minispiel, Windkanal-Zufallsrichtung, Eis-Höhlen-Dunkelheit, Rohrpost-Teleport, Kosmische Drift, Geister-Felder). Jede Sonderregel ist in ihrem Insel-Kapitel vollständig spezifiziert und muss die Basismechanik (Würfeln–Ziehen–Feld-Effekt) nicht erweitern, sondern nur lokal überlagern.
4. **Mindestabstand:** Zwei Junction-Felder liegen auf dem Hauptpfad mindestens 5 Felder auseinander (Einstieg B liegt mindestens 5 Felder nach Ausstieg A), damit Abzweigungen nicht ineinandergreifen.

### 3.10 Item-Preisstufen

Die Preise der 5 Standard-Items (Glücks-Würfel, Stern-Teleporter, Schutzschild, Münz-Magnet, Dieb-Handschuh) sind auf höheren Inseln teurer. Basis-Preise stammen aus `item-system.md`; pro Insel gilt eine Preisstufe:

| Preisstufe | Inseln | Glücks-Würfel | Stern-Teleporter | Schutzschild | Münz-Magnet | Dieb-Handschuh |
|-----------|--------|--------------:|-----------------:|-------------:|------------:|---------------:|
| 0 | 1–2 (Sonnenstrand, Zuckerwald) | 5 | 8 | 6 | 4 | 10 |
| 1 | 3–4 (Wolkenwerk, Frostgipfel) | 6 | 9 | 7 | 5 | 11 |
| 2 | 5–6 (Dschungeltempel, Mechanik-Stadt) | 7 | 10 | 8 | 6 | 12 |
| 3 | 7 (Sternenzitadelle) | 8 | 11 | 9 | 7 | 13 |

Sonderangebote (z. B. Ereignis "Erfindermesse" auf Mechanik-Stadt) dürfen Preise temporär reduzieren, nie unter 1 Münze.

### 3.11 Ereignis-Theme und Schweregrad

Jede Insel besitzt ein eigenes Event-Theme (Ereignis-Kartei) mit 3–4 Ereignissen, die gewichtet ausgelost werden (Wahrscheinlichkeiten je Insel-Kapitel). Die Schwere der negativen Effekte steigt mit der Schwierigkeitsstufe:

| Insel | Event-Theme | Ereignisse | Negative Schwere |
|-------|-------------|-----------|------------------|
| Sonnenstrand | Wetter & Meer | Springflut, Muschel-Suche, Quallen-Schwarm | −3 Münzen |
| Zuckerwald | Süßigkeiten-Magie | Klebriger Boden, Zucker-Rausch, Keks-Regen | Wurf-Modifikator −1 |
| Wolkenwerk | Himmelsdynamik | Turbulenz, Aufwind, Regenbogen-Schatz | Positions-Tausch (alle) |
| Frostgipfel | Wetter & Licht | Schneesturm, Eisglätte, Nordlicht | 1 Runde aussetzen (2 Spieler) |
| Dschungeltempel | Fluch & Gold | Fluch des Tempels, Goldrausch, Lianen-Schwung | −5 Münzen für Führenden |
| Mechanik-Stadt | Technik-Pannen | Zahnrad-Stau, Erfindermesse, Dampf-Explosion | 1 Runde aussetzen |
| Sternenzitadelle | Kosmisch | Sternen-Regen, Zeit-Verzerrung, ArenaStars Segen, Schwarzes Loch | Item-Haltbarkeit −1, Richtungs-Würfel |

Alle Ereignis-IDs, Auslöse-Bedingungen und exakten Effekte stehen in den Insel-Kapiteln (Sektion 3, Unterabschnitt "Ereignis-Kartei").

### 3.12 Board-Dateiformat

Jede Insel wird als eigenständiges Plugin unter `plugins/boards/INSELNAME/` abgelegt. Ein Board besteht aus genau drei Dateien:

1. **`board.tscn`** — 3D-Szene des Boards: Feld-Modelle (40 Felder + Junction-Pfeile), Deko (Meilenstein-Landmarken, visuelle Besonderheiten), Kamera-Spline für das Insel-Intro, Licht- und Umgebungs-Setup. Die Szene referenziert die Feld-Positionen als benannte Marker (Feld 1 bis Feld 40) und die Junction-Wahlpunkte.
2. **`board.gd`** — Event-Logik des Boards: Feld-Effekte, Ereignis-Kartei (Auslosung mit Gewichten), Abzweigungs-Sonderregeln, Meilenstein-Trigger. `board.gd` implementiert die Board-Schnittstelle, die in `technical-architecture.md` spezifiziert ist (Methoden für Feld-Auflösung, Ereignis-Auslosung, Shops, Minispiel-Trigger). Enthält keinen Präsentations-Code (keine UI, kein Rendering).
3. **`board.json`** — Metadaten im kebab-case: `id` (Inselname), `name_de`, `theme`, `difficulty` (1–5 Sterne), `colors` (3 Hex-Werte), `music` (Stil, BPM, Tonleiter), `field_distribution` (Typ-Zählungen, muss Formel 4.1 genügen), `branches` (Einstieg/Ausstieg je Abzweigung), `event_pool` (Ereignis-IDs mit Gewichten), `item_price_tier` (0–3), `intro_duration` (Sekunden), `milestones` (Feld-Nummern der Landmarken), `special_rules` (Liste der aktiven Sonderregeln). `board.json` ist die Single Source of Truth für die Menü-Anzeige (Auswahl-Bildschirm) und für automatische Validierungs-Checks.

### 3.13 Ablösung der STP-Legacy-Boards

1. Die Legacy-Boards **KDEValley** und **Test-Board** aus Super Tux Party werden entfernt und **müssen durch die neuen Insel-Boards ersetzt** werden. Es existiert kein Fallback auf ein Legacy-Board.
2. Die Ablösung erfolgt im Zuge der Migration in `technical-fork-strategy.md`. KDEValley wird funktional durch Sonnenstrand (Einsteiger-Board) ersetzt; das Test-Board entfällt ersatzlos.
3. Nach der Migration darf keine Partie mehr auf einem Legacy-Board startbar sein; die Insel-Auswahl (3.5) listet ausschließlich die 7+1 Insel-Boards.
4. Die Legacy-Begriffe (Cookie, Cake, Sara, Nolok, GNU, BLUE/RED/GREEN-Felder) werden in keinem Insel-Kapitel als aktive Fachbegriffe verwendet (Rebranding-Prüfung, siehe `glossary.md`).

## 4. Formulas

### 4.1 Feldverteilungs-Gleichung

Für jedes Board gilt: `S + ST + IT + E + L + C + M = 40`, wobei:
- `S` = Anzahl Startfelder = 1,
- `ST` = Anzahl Stern-Shops ∈ [2, 3] (Ausnahme Zitadelle: 4),
- `IT` = Anzahl Item-Shops = 2,
- `E` = Anzahl Ereignis-Felder ∈ [5, 6],
- `L` = Anzahl Glück/Pech-Felder = 3,
- `C` = Anzahl Münz-Bonus-Felder = 4,
- `M` = Anzahl Minispiel-Felder.

Erwartungswerte: `M = 40 − (S + ST + IT + E + L + C) = 30 − ST − E`.
Beispiel Sonnenstrand: `M = 30 − 3 − 6 = 21`. Beispiel Sternenzitadelle: `M = 30 − 4 − 6 = 20`.
Validierung: Für jedes Insel-Kapitel muss die Gleichung aufgehen; `board.json` wird automatisch gegen 4.1 geprüft.

### 4.2 Hauptpfad- und Abzweigungs-Anteile

`Hauptpfad = 32` Felder, `Abzweigungen = 8` Felder (2 × 4). Es gilt `32 + 8 = 40`. Die Abzweigungs-Felder sind global 33–40 nummeriert.

### 4.3 Junction-Differenz Δ

`Δ = 5 − (Y − X)`, wobei:
- `X` = Einstiegs-Feld der Abzweigung (Hauptpfad),
- `Y` = Ausstiegs-Feld der Abzweigung (Hauptpfad, Y > X),
- `5` = Länge des Abzweigungs-Pfads in Zügen (4 Abzweigungs-Felder + 1 Ausstiegs-Zug),
- `(Y − X)` = Länge des Hauptpfad-Segments in Zügen.

Bedeutung: `Δ < 0` = Abkürzung (Abzweigung ist kürzer als das Hauptpfad-Segment), `Δ = 0` = gleich lang, `Δ > 0` = Umweg.
Beispiel Mechanik-Stadt, Abzweigung B: `X = 25, Y = 30` → `Δ = 5 − 5 = 0` (gleich lang, aber Rohrpost-Teleport macht sie faktisch kürzer). Beispiel Sternenzitadelle, Abzweigung A: `X = 17, Y = 24` → `Δ = 5 − 7 = −2` (Abkürzung um 2 Züge).
Gültigkeitsbereich: `Δ ∈ [−3, +3]` für alle Boards; Werte außerhalb sind ein Design-Fehler.

### 4.4 Freischalt-Schwellen

`Schwelle(Insel n)`, n ∈ {1..6}: Inseln 1–3 Schwelle 0, Inseln 4–5 Schwelle 10, Inseln 6 Schwelle 25, Insel 7 (Zitadelle) Schwelle 50 oder Sieg auf allen Inseln 1–7.
Formal: `freigeschaltet(n) = (gespielteSpiele ≥ Schwelle(n)) ∨ (n = 7 ∧ alleInselnGewonnen)`, mit `gespielteSpiele` = abgeschlossene Partien im lokalen Profil (siehe 3.4).

### 4.5 Item-Preisstufe

`Preis(item, Insel) = BasisPreis(item) + Preisstufe(Insel)`, wobei:
- `BasisPreis(item)` = Preis aus `item-system.md` (Würfel 5, Teleporter 8, Schild 6, Magnet 4, Handschuh 10),
- `Preisstufe(Insel)` = 0 für Inseln 1–2, 1 für Inseln 3–4, 2 für Inseln 5–6, 3 für Insel 7.

Beispiel: Schutzschild auf Dschungeltempel: `6 + 2 = 8` Münzen. Untergrenze: kein Item-Preis unter 1 (Sonderangebote gedeckelt).

### 4.6 Schwierigkeits-Score

`D = (ST − 2) · 2 + (E − 5) · 1 + Preisstufe + Σ_Rampe`, wobei `Σ_Rampe` die Summe der Sonderregel-Gewichte der Abzweigungen ist (je Sonderregel +1, definiert in den Insel-Kapiteln).
Erwartungswerte: Sonnenstrand `D = (3−2)·2 + (6−5)·1 + 0 + 0 = 3`; Sternenzitadelle `D = (4−2)·2 + (6−5)·1 + 3 + 2 = 10`. Der Score dient der internen Balance-Prüfung (monoton nicht-fallend von Insel 1 bis 7; Inseln gleicher Schwierigkeitsstufe dürfen denselben Score haben) und wird in den Insel-Kapiteln ausgewiesen; er ist kein Spielwert.

## 5. Edge Cases

1. **Freischalt-Schwelle erreicht mitten in der Lobby:** Wird die Schwelle während der Lobby erreicht (z. B. nach einer Partie, ohne die Lobby zu verlassen), wird die Insel-Liste sofort aktualisiert; die neue Insel ist ab der nächsten Partie wählbar, nicht in der laufenden Auswahl.
2. **Schnittmenge leer (Online-Lobby):** Haben Host und Gäste keine gemeinsame freigeschaltete Insel, wird die Partie auf Sonnenstrand erzwungen und ein Hinweis eingeblendet. Es wird keine Partie mit einer für einen Spieler gesperrten Insel gestartet.
3. **Abgebrochene Partie:** Eine Partie, die vor der Siegerehrung abgebrochen wird, zählt nicht als "gespieltes Spiel" und nicht als "Insel gewonnen" (verhindert Freischalt-Farming durch Abbruch).
4. **Sieg-Freischaltung der Zitadelle vor 50 Spielen:** Ein Spieler gewinnt auf allen 7 Inseln, bevor 50 Spiele erreicht sind → die Zitadelle wird sofort freigeschaltet (Oder-Verknüpfung). Der Fortschrittszähler für die 50-Spiele-Schwelle läuft trotzdem weiter; ein Rücksetzen ist ausgeschlossen.
5. **Datenfehler in `board.json`:** Summiert die Feld-Verteilung nicht auf 40 (Formel 4.1), oder zeigt `branches` ungültige Einstiege/Ausstiege (X ≥ Y oder Δ außerhalb [−3, +3]), wird das Board beim Laden abgelehnt und in der Insel-Auswahl als "Nicht verfügbar" markiert. Ein Validierungs-Log-Eintrag wird geschrieben. Die Partie kann nicht auf einem defekten Board starten.
6. **Fehlende Board-Datei:** Existiert `board.gd`, `board.tscn` oder `board.json` nicht vollständig, gilt das Board als nicht ladbar und wird aus der Auswahl ausgeblendet. Ein leeres Plugin-Verzeichnis wird ignoriert.
7. **Insel-Intro bei abgeschlossener Migration:** Während des Ladens eines Boards darf das Insel-Intro nicht starten, bevor die 3D-Szene vollständig instanziiert ist. Ist die Szene nach 10 Sekunden nicht bereit, wird das Intro übersprungen und die Partie startet direkt (Timeout-Regel).
8. **Host wechselt nach Board-Wahl:** Wechselt die Host-Rechte während der Lobby, bleibt die bereits gewählte Insel aktiv, sofern sie für den neuen Host freigeschaltet ist. Ist sie es nicht, wird auf die höchste gemeinsame freigeschaltete Insel zurückgefallen (Standard: Sonnenstrand).
9. **Widerspruch zwischen Insel-Kapitel und `board.json`:** Bei Abweichungen (z. B. Ereignis-Gewichte) gilt das Insel-Kapitel der Game Bible als maßgeblich; `board.json` wird korrigiert und ein Review-Log-Eintrag erstellt (Konfliktregel aus `bible-index.md`, Regel 3.1.2).

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `world-overview.md` | Art | Verwendung |
|-----------------------------------|-----|------------|
| `design/gdd/game-concept.md` | Quelle | Liefert die Insel-Liste, Feld-Typen und die 40-Felder-Struktur. |
| `design/gdd/bible-index.md` | Regelwerk | Definiert den 8-Sektionen-Standard und die Kapitelstruktur (Teil VI). |
| `design/gdd/vision-pillars.md` | Peer | Farb-/Silhouetten-Regeln (Pfeiler 4) gelten für alle Insel-Identitäten. |
| `design/gdd/board-architecture.md` | Peer | Spezifiziert die Feld-Verkettung (next/prev), die dieses Kapitel als Rahmen referenziert. |
| `design/gdd/item-system.md` | Peer | Liefert die Basis-Item-Preise für die Preisstufen (3.10). |
| `design/gdd/victory-conditions.md` | Peer | Definiert "Insel gewonnen" für die Zitadellen-Freischaltung. |
| `design/gdd/technical-architecture.md` | Nachgeordnet | Muss die Board-Schnittstelle definieren, die `board.gd` implementiert. |
| `design/gdd/technical-fork-strategy.md` | Nachgeordnet | Muss die Legacy-Ablösung (3.13) als Migrationsschritt aufnehmen. |
| `design/gdd/ui-mainmenu.md` | Nachgeordnet | Muss die Insel-Auswahl mit Sperr-Anzeige (3.4) umsetzen. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| Alle Insel-Kapitel (`world-sonnenstrand.md` … `world-sternenzitadelle.md`) | Müssen die Rahmenregeln (3.1–3.13) und Formeln (4.1–4.6) erfüllen und ihre Feld-Verteilung aus 3.8 übernehmen. |
| `design/gdd/audio-music.md` | Muss die Insel-Musik-Stile aus 3.2 als Musik-Tracks umsetzen. |
| `design/gdd/ui-board.md` | Muss Junction-Pfeile und Pfadwahl (3.9) darstellen. |
| `design/gdd/narrative-flavor.md` | Muss Insel-Einleitungstexte und Ereignis-Flavortexte passend zu den Event-Themes (3.11) formulieren. |
| `design/gdd/technical-data-structures.md` | Muss das `board.json`-Schema (3.12) als Datenstruktur abbilden. |
| Plugin-Verzeichnis `plugins/boards/` | Muss die Dateikonvention (3.12) und Validierung (5.5) implementieren. |

### 6.3 Bidirektionalität

Die Abhängigkeiten sind wechselseitig: Dieses Kapitel setzt den Rahmen für die Insel-Kapitel, und die Insel-Kapitel liefern die konkreten Werte (Feld-Verteilungen, Junctions, Event-Gewichte), die dieses Kapitel in den Tabellen 3.2 und 3.8 referenziert. Ändert ein Insel-Kapitel seine Feld-Verteilung, muss Tabelle 3.8 hier aktualisiert werden; ändert dieses Kapitel einen Rahmen (z. B. Preisstufen), müssen alle betroffenen Insel-Kapitel geprüft werden. Der Bible-Index (`bible-index.md`) listet alle 8 Kapitel dieses Teils und erzwingt den gemeinsamen Standard.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Freischalt-Schwelle Inseln 4–5 | Kurve | 0–30 Spiele | 10 | Steuert, wie schnell die mittleren Inseln erreichbar sind (Tempo der Welt-Rampe). |
| Freischalt-Schwelle Inseln 6 | Kurve | 10–50 Spiele | 25 | Steuert den Zugang zur Mechanik-Stadt. |
| Freischalt-Schwelle Zitadelle | Kurve | 25–100 Spiele | 50 | Steuert den Zugang zum Final-Board (neben der Sieg-Alternative). |
| Insel-Intro-Dauer | Feel | 3–8 s | 5 s (Zitadelle 7 s) | Länge des Kamera-Flugs vor Partiebeginn; zu lang bricht den Flow. |
| Intro-Timeout | Gate | 5–15 s | 10 s | Maximale Ladezeit, nach der das Intro übersprungen wird. |
| Item-Preisstufe je Insel-Gruppe | Kurve | 0–4 | 0/1/2/3 | Höhe des Preisaufschlags; steuert den Schwierigkeits-Lever 3. |
| Δ-Gültigkeitsbereich | Gate | [−3, +3] | [−3, +3] | Grenzt zulässige Abzweigungs-Längen ein; verhindert extrem lange Umwege. |
| Ereignis-Feld-Bereich | Kurve | 5–6 | 5–6 | Anzahl der Ereignis-Felder pro Insel (Rampen-Lever 2). |
| Stern-Shop-Bereich | Kurve | 2–4 | 2–3 (Zitadelle 4) | Anzahl der Stern-Shops; mehr Shops = mehr Stern-Kaufgelegenheiten pro Runde. |

Alle Knobs wirken auf die gefühlte Welt-Progression und die Partien-Langlebigkeit. Änderungen erfordern die Aktualisierung der Insel-Kapitel (Feld-Verteilungen, Preise) und einen Review-Log-Eintrag.

## 8. Acceptance Criteria

Ein QA-Tester (oder CI-Hook) kann folgende Prüfungen ausführen:

1. **7+1 Boards vorhanden:** Unter `plugins/boards/` existieren exakt 7 Insel-Boards plus Sternenzitadelle, jeweils mit `board.tscn`, `board.gd` und `board.json`. PASS/FAIL.
2. **Keine Legacy-Boards:** KDEValley und Test-Board sind nicht mehr in der Insel-Auswahl vorhanden und nicht startbar. PASS/FAIL.
3. **Feldverteilung:** Für jede Insel summiert die Feld-Verteilung auf 40 und entspricht exakt Tabelle 3.8 (Formel 4.1). PASS/FAIL.
4. **Junction-Validität:** Jede Abzweigung hat gültige Einstiege/Ausstiege mit Δ ∈ [−3, +3] (Formel 4.3). PASS/FAIL.
5. **Freischaltung:** Mit einem frischen Profil sind genau Inseln 1–3 wählbar; nach 10 abgeschlossenen Partien zusätzlich 4–5; nach 25 zusätzlich 6; nach 50 oder Sieg auf allen 7 Inseln die Zitadelle. PASS/FAIL.
6. **Sperr-Anzeige:** Gesperrte Inseln zeigen Silhouette, Schloss und verbleibende Spiel-Anzahl. PASS/FAIL.
7. **Host-Wahl:** Der Host kann vor Spielstart ausschließlich freigeschaltete Inseln wählen; die Wahl übernimmt die geladene Board-Plugin-Szene. PASS/FAIL.
8. **Insel-Intro:** Vor jeder Partie läuft das Insel-Intro (5 s; 7 s auf der Zitadelle), ist ab Sekunde 1 überspringbar und endet an der Startposition von Spieler 1. PASS/FAIL.
9. **Item-Preise:** Die Item-Shop-Preise jeder Insel entsprechen ihrer Preisstufe (3.10). PASS/FAIL.
10. **Rebranding:** In keinem Insel-Kapitel und keinem Board-Plugin treten Legacy-Begriffe als aktive Fachbegriffe auf. PASS/FAIL.
11. **Erlebbar (Experiential):** Eine Testperson kann nach 2 Minuten Beobachtung jede der 7 Inseln an Farbpalette, Musik und Formsprache eindeutig zuordnen (Silhouetten-/Farbtest, mindestens 3 von 3 richtigen Zuordnungen pro Insel). PASS/FAIL.


