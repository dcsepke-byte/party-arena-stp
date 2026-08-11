# Minispiel-Kategorien — Party Arena Game Bible

> **Teil:** IV — Minigames
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md (Abschnitt "Minispiele"), design/gdd/minigame-architecture.md

---

## 1. Overview

Dieses Kapitel definiert die 5 Minispiel-Kategorien von Party Arena — **Geschicklichkeit, Reaktion, Puzzle/Logik, Rechnen/Wort und Kooperation** — und spezifiziert die 12 geplanten Minispiele (3+3+2+2+2) in für Implementierung und Balancing ausreichender Detailtiefe. Für jede Kategorie wird festgelegt, was sie spielerisch besonders macht, für welche Spielertypen sie gedacht ist und wie sie mit der Spielerzahl (2–8) skaliert. Für jedes einzelne Minispiel werden Ziel, Siegbedingung, Kernmechanik, Steuerung, Früh-Ende-Regel und Skalierung definiert. Die Kategorien decken bewusst unterschiedliche Fähigkeiten ab (Motorik, Reflexe, Gedächtnis, Rechnen/Sprache, Teamarbeit), damit jede Spielerin und jeder Spieler in einer Partie mindestens eine Kategorie findet, in der sie oder er glänzen kann (Kompetenz-Erlebnis nach Self-Determination Theory). Alle Minispiele folgen dem Rahmen aus `minigame-architecture.md`: 2–8 Spieler gleichzeitig, Spielphase mit hartem 30-s-Limit, Platzierung 1–n. Die Kategorie ist ein Pflichtfeld in `minigame.json` (`category`).

## 2. Player Fantasy

Der Kategorien-Mix erzeugt über eine Partie hinweg einen wechselnden Gefühlsrhythmus — kein Minispiel fühlt sich wie das vorherige an, und jede Runde spricht andere Stärken an:

- **Geschicklichkeit** fühlt sich an wie ein **tobender Spielplatz**: Man bewegt sich, wirft, balanciert und spürt den eigenen Körper in der Steuerung (MDA-Aesthetics "Sensation" und "Challenge"). Für aktive Spieler, die Action und Bewegung lieben.
- **Reaktion** erzeugt **Herzklopfen und Lachen**: Blitze, Befehle, aufleuchtende Knöpfe — man muss schneller sein als der Reflex, und wer zögert, fliegt raus ("Excitement", "Challenge"). Die einfachsten Regeln des Spiels, ideal für die jüngsten Mitspieler.
- **Puzzle/Logik** ist die **ruhige Denk-Pause**: Gedächtnis und Orientierung statt Tempo; man spielt parallel gegen sich selbst, nicht gegeneinander ("Discovery", "Challenge"). Für Denker und Tüftler, die Strategie über Schnelligkeit stellen.
- **Rechnen/Wort** verbindet **Spiel mit Kopfrechnen und Sprache**: Man zählt blitzschnell Münzen oder bildet Wörter — ein spielerischer Kompetenz-Moment für alle, die gerne kniffeln ("Challenge", "Expression").
- **Kooperation** ist das **Gemeinschafts-Erlebnis**: Alle gewinnen oder verlieren zusammen, man hilft sich, statt sich zu bekämpfen ("Fellowship", Relatedness). Wirkt nach kompetitiven Runden als versöhnlicher Höhepunkt, besonders in Familien.

Über alle Kategorien gilt: **Jede Runde ist eine kleine Überraschung.** Niemand kann vorhersagen, welche Fähigkeit als Nächstes gefordert wird — das hält die Partie für Großeltern, Eltern und Kinder gleichermaßen spannend und verhindert, dass sich ein einzelner Spielertyp durchsetzt. Die Kategorien sind zugleich die Zugänglichkeits-Matrix: Wer eine Kategorie nicht mag oder kann, bekommt in den anderen ihre Chancen.

## 3. Detailed Rules

### 3.1 Kategorien-Überblick

| Kategorie | ID (`category`-Wert) | Minispiele | Anzahl |
|-----------|----------------------|------------|--------|
| Geschicklichkeit | `geschicklichkeit` | Münzregen, Balance-Akt, Zielwurf | 3 |
| Reaktion | `reaktion` | ArenaStar sagt, Blitz-Fangen, Knöpfchen-Drücker | 3 |
| Puzzle/Logik | `puzzle` | Sternen-Labyrinth, Insel-Memory | 2 |
| Rechnen/Wort | `rechnen` | Münz-Zähler, Wort-Puzzle | 2 |
| Kooperation | `kooperation` | Sternen-Brücke, Schatz-Trage | 2 |

Gemeinsame Rahmenregeln (aus `minigame-architecture.md`):
- Jedes Minispiel läuft mit 2–8 Spielern gleichzeitig; `players.min`/`players.max` steht in `minigame.json`.
- Die Spielphase endet nach `duration` Sekunden (Standard 30, hart max. 30) oder bei `request_end()`.
- Die Platzierung folgt dem Ergebnis-Modus (`by_points` oder `by_position`).
- Alle Minispiele sind für Kinder ab 6 Jahren zugänglich (Regeln in einem Satz erklärbar, Symbole statt Text).

### 3.2 Geschicklichkeit (3 Minispiele)

#### 3.2.1 Kategorie-Profil

- **Was macht sie besonders?** Kontinuierliche, körperbetonte Action: Die Spieler bewegen sich permanent durch die Arena, müssen Position, Timing und Zielgenauigkeit koordinieren. Anders als bei "Reaktion" gibt es hier keine zentralen Reiz-Events, sondern freies, selbstgesteuertes Spiel in einer lebendigen Umgebung.
- **Für welche Spieler?** Aktive Spieler und Action-Liebhaber (Bartle-Typ "Achiever"/"Competitor", Quantic-Foundry-Motiv "Action/Destruction"). Auch für Kinder, die Bewegung in der Steuerung brauchen, um Spaß zu haben.
- **Schwierigkeits-Skalierung mit Spielerzahl:** Die Arena-Fläche und die Ressourcen-Menge (Münzen, Bälle) wachsen mit der Spielerzahl, sodass die Ressourcen-Dichte (Ressourcen pro Fläche) annähernd konstant bleibt. Mehr Spieler erhöhen die Konkurrenz und das Chaos, nicht die Leere. Formeln in 4.1.

#### 3.2.2 Minispiel "Münzregen" (`muenzregen`)

| Aspekt | Spezifikation |
|--------|---------------|
| Ziel | In 30 s so viele Münzen wie möglich einsammeln. |
| Siegbedingung | Höchste Münzsumme nach Ablauf → Platz 1. `results_mode = "by_points"`. |
| Kernmechanik | Münzen regnen vom Himmel und fallen an zufälligen Positionen in die Arena. Sie liegen kurz (6 s) am Boden und verschwinden dann. Spieler sammeln durch Berühren. |
| Münzwerte | Normale Münze = 1 Punkt; seltene Sternmünze (10 % der Spawns) = 5 Punkte. Sternmünzen glitzern und sind größer (Wiedererkennbarkeit, Pfeiler 4). |
| Steuerung | Bewegung (`up/down/left/right`). Keine Aktionstaste nötig; Sammeln ist automatisch. |
| Früh-Ende | Keines — das Minispiel läuft immer die volle `duration`. |
| Skalierung | Arena-Fläche `A(n)` und Spawn-Rate `r(n)` (Formeln 4.1.1/4.1.2). |
| Fairness | Spawn-Positionen gleichverteilt über die Arena, nie direkt auf einem Spieler (Mindestabstand 1,5 m), keine toten Winkel. |

#### 3.2.3 Minispiel "Balance-Akt" (`balance_akt`)

| Aspekt | Spezifikation |
|--------|---------------|
| Ziel | Als letzte(r) auf der Kugel balancieren. |
| Siegbedingung | Eliminationsreihenfolge: Wer als Letzter übrig ist, gewinnt. Platzierung = umgekehrte Eliminationsreihenfolge (früher gefallen = schlechterer Platz). `results_mode = "by_position"`. |
| Kernmechanik | Jeder Spieler steht auf einer eigenen Kugel in einem eigenen, kleinen Balance-Bereich. Gewichtsverlagerung kippt die Kugel; wer das Gleichgewicht verliert, rutscht ab und fällt auf den Boden. Ab dem Moment des Bodenkontakts (0,5 s ununterbrochen) gilt der Spieler als eliminiert. |
| Instabilitäts-Kurve | Die Kugeln werden über die Zeit unruhiger: In 4 Stufen (Start, +10 s, +20 s, +26 s) steigt die Wackel-Amplitude und -Frequenz. Die Stufen sind für alle Spieler synchron. |
| Steuerung | Gewichtsverlagerung über Bewegung (`up/down/left/right`). Sensitive, aber weiche Steuerung (kein Überschwingen). |
| Früh-Ende | `request_end()`, sobald nur noch 1 Spieler balanciert. |
| Skalierung | Keine Arena-Skalierung (jede Kugel ist unabhängig). Bei mehr Spielern sinkt die individuelle Gewinnwahrscheinlichkeit natürlich; die Runden dauern im Schnitt etwas länger, weil mehr Spieler umkippen müssen. `duration` = 30 s hart; ein voller Durchlauf ist auch bei 8 Spielern in 30 s möglich (alle fallen in der Regel vorher aus). |
| Fairness | Alle Kugeln sind identisch konfiguriert; die Instabilitäts-Stufen sind global synchron, nicht pro Spieler. |

#### 3.2.4 Minispiel "Zielwurf" (`zielwurf`)

| Aspekt | Spezifikation |
|--------|---------------|
| Ziel | In 30 s die meisten Treffer auf Gegner erzielen. |
| Siegbedingung | Höchste Trefferzahl nach Ablauf → Platz 1. `results_mode = "by_points"`. |
| Kernmechanik | Alle Spieler sind gleichzeitig Werfer und Ziel. Jeder Spieler hat eine Wurf-Figur mit bis zu 3 farbigen Bällen im Gepäck. Ein Ball fliegt in die Blickrichtung des Charakters; ein Treffer auf einen Gegner zählt 1 Punkt für den Werfer. Der getroffene Spieler verliert **keine** Punkte und scheidet **nicht** aus — er bekommt einen kurzen, slapstickhaften Effekt (Staubwolke, "Plötz"-Sound) und ist 0,5 s unverwundbar (kein Treffer-Spam). Verbrauchte Bälle landen am Boden und können von jedem aufgehoben werden (Aufheben = darüberlaufen). |
| Munitionsregel | Maximal 3 Bälle gleichzeitig im Besitz; leere Hände müssen erst einen Boden-Ball aufheben. Es liegen immer `3·n` Bälle im Umlauf. |
| Steuerung | Bewegung (`up/down/left/right`) + Wurf (`action1`) in Blickrichtung; Blickrichtung folgt der letzten Bewegungsrichtung. |
| Früh-Ende | Keines — volle `duration`. |
| Skalierung | Arena-Fläche `A(n)` und Bälle `B(n)` (Formeln 4.1.3/4.1.4). |
| Fairness | Gleich viele Bälle im Umlauf pro Spieler (3); die Spawn-Positionen der Bälle sind gleichverteilt; kein Spieler startet in Ballnähe-Vorteil (Startpositionen symmetrisch). |

### 3.3 Reaktion (3 Minispiele)

#### 3.3.1 Kategorie-Profil

- **Was macht sie besonders?** Blitzschnelle Entscheidungen auf zentrale Reize. Die Regeln sind die einfachsten des Spiels (ein Satz), die Spannung ist am höchsten: Wer zögert oder falsch reagiert, wird bestraft — meist durch Ausscheiden.
- **Für welche Spieler?** Alle, besonders jüngere Kinder (ab 6) und Spieler, die Wettbewerb und Nervenkitzel mögen (Bartle "Competitor", Quantic-Foundry "Excitement"). Ideal für den Einstieg, weil keine Vorkenntnisse nötig sind.
- **Schwierigkeits-Skalierung mit Spielerzahl:** Die Frequenz der Ereignisse (Blitze, Befehle, aufleuchtende Knöpfe) wächst mit der Spielerzahl; bei Ausscheidungsspielen wächst die Runden-/Ausscheidungszahl, damit die Rangfolge bei 8 Spielern fein genug aufgelöst wird. Formeln in 4.2.

#### 3.3.2 Minispiel "ArenaStar sagt" (`arena_star_sagt`)

| Aspekt | Spezifikation |
|--------|---------------|
| Ziel | Als letzte(r) die Befehle von ArenaStar korrekt befolgen. |
| Siegbedingung | Ausscheidungsreihenfolge; letzte(r) Überlebende gewinnt. `results_mode = "by_position"`. |
| Kernmechanik | Simon-Says mit ArenaStar als Ansagerin. ArenaStar zeigt (Icon + Geste + kurzer Zuruf) eines von 4 Kommandos: Springen, Drehen, Winken, Hinhocken. Wird das Kommando mit "ArenaStar sagt …" eingeleitet, müssen alle es ausführen; ohne die Einleitung darf es **nicht** ausgeführt werden. Wer ein verbotenes Kommando ausführt oder ein erlaubtes auslässt, scheidet aus. |
| Kommando-Anzeige | Großes Icon auf dem Bildschirm + ArenaStar-Animation + kurzer Zuruf (lokalisiert). Das Icon ist das primäre Signal (Pfeiler 1: Symbole statt Text). |
| Runden | Das Minispiel läuft in Runden; pro Runde genau ein Kommando. Anzahl der Runden `R(n)` (Formel 4.2.1). Das Tempo (Zeit bis zum nächsten Kommando) steigt pro Runde (Faktor `t(r)`, Formel 4.2.2). |
| Steuerung | 4 Aktionsknöpfe (`action1` = Springen, `action2` = Drehen, `action3` = Winken, `action4` = Hinhocken). Jede Aktion hat ein großes Icon auf dem Bildschirm. |
| Früh-Ende | `request_end()`, sobald nur noch 1 Spieler übrig ist. |
| Skalierung | Runden `R(n)` (4.2.1) und Tempo-Faktor `t(r)` (4.2.2). |
| Fairness | Kommando-Reihenfolge ist zufällig; "ArenaStar sagt"-Kommandos und reine Kommandos sind gemischt (Verhältnis etwa 60/40 zugunsten der "sagt"-Kommandos, damit nicht übermäßig viele Spieler früh ausscheiden). |

#### 3.3.3 Minispiel "Blitz-Fangen" (`blitz_fangen`)

| Aspekt | Spezifikation |
|--------|---------------|
| Ziel | Den Blitzen von ArenaStar so lange wie möglich ausweichen. |
| Siegbedingung | Überlebensdauer; bei Timer-Ablauf entscheidet die Anzahl der verbleibenden Herzen. `results_mode = "by_points"` mit `score` = Überlebenszeit in Sekunden (bei Gleichstand der Herzen: zuerst erreichte Zeit gewinnt; siehe 4.2.3). |
| Kernmechanik | ArenaStar schleudert Blitze in die Arena. Jeder Blitz **telegrafiert** zuerst: 1 s lang leuchtet ein Kreis an der Einschlagstelle auf, dann schlägt der Blitz ein (kurze Lichtsäule). Ein Spieler im Einschlagkreis verliert 1 Herz. Jeder Spieler hat 3 Herzen; bei 0 Herzen scheidet er aus (wird mit einem komischen "gerösteten"-Effekt aus der Arena getragen). |
| Herz-Anzeige | 3 Herz-Icons über jedem Charakter (bei Split-Screen im eigenen Viewport, bei Vogelperspektive über dem Charakter). |
| Steuerung | Bewegung (`up/down/left/right`). |
| Früh-Ende | `request_end()`, sobald nur noch 1 Spieler übrig ist. |
| Skalierung | Blitz-Frequenz `f(n)` (Formel 4.2.4); Vorwarnzeit konstant 1 s. |
| Fairness | Einschlagstellen werden gleichverteilt gewählt, nie direkt auf einem Spieler (Mindestabstand 1 m zur Vorwarnzeit); die Vorwarnung ist für alle gleich lang. |

#### 3.3.4 Minispiel "Knöpfchen-Drücker" (`knoepfchen_druecker`)

| Aspekt | Spezifikation |
|--------|---------------|
| Ziel | In 30 s so viele aufleuchtende Knöpfe wie möglich drücken. |
| Siegbedingung | Höchste korrekte Drück-Zahl nach Ablauf. `results_mode = "by_points"`. |
| Kernmechanik | Jeder Spieler hat ein eigenes Panel mit 4 großen, farbigen Knöpfen (Rot, Blau, Gelb, Grün). Leuchtet ein Knopf auf, muss er gedrückt werden. Nach korrektem Drücken erlöscht er, und nach kurzer Pause (0,3 s) leuchtet der nächste. Pro korrektem Drücken = 1 Punkt. Falscher Knopf (Drücken eines nicht leuchtenden) gibt keine Punkte und verursacht einen kleinen Ruckel-Effekt, kostet aber keine Punkte. |
| Parallele Wertung | Da jeder Spieler sein eigenes Panel hat, ist die Aufgabe perfekt parallel und fair — die Panel-Logik ist pro Spieler unabhängig (jeder bekommt dieselbe Reiz-Menge, aber unterschiedliche zufällige Reihenfolgen). |
| Steuerung | 4 Aktionsknöpfe (`action1`–`action4`) ODER Richtungstasten (als 4-Knopf-Raster). Beides wird unterstützt; das Panel zeigt die Zuordnung als Farbe + Taste. |
| Früh-Ende | Keines — volle `duration`. |
| Skalierung | Keine n-Skalierung nötig (pro Spieler unabhängig). Die Schwierigkeit liegt in der Reaktionsgeschwindigkeit, nicht in der Spielerzahl. |
| Fairness | Identische Panel-Konfiguration und Reiz-Häufigkeit für alle; Reihenfolge pro Spieler zufällig. |

### 3.4 Puzzle/Logik (2 Minispiele)

#### 3.4.1 Kategorie-Profil

- **Was macht sie besonders?** Ruhige, denkende Minispiele: Gedächtnis und räumliche Planung statt Tempo. Die Spieler spielen **parallel gegen sich selbst** — das Minispiel bestraft nicht die anderen, sondern belohnt die eigene Leistung. Das verlangsamt das Runden-Tempo angenehm und gibt der Gruppe eine Verschnaufpause.
- **Für welche Spieler?** Denker, Tüftler und Sammler (Bartle "Achiever"/"Explorer", Quantic-Foundry "Mastery/Strategy", "Achievement/Completion"). Ideal für Spieler, die bei Reaktionsspielen abgehängt werden.
- **Schwierigkeits-Skalierung mit Spielerzahl:** Die Aufgabenkomplexität (Labyrinth-Größe) wächst mit der Spielerzahl; Memory bleibt bewusst konstant (Feldgröße 4×4), weil die Schwierigkeit hier über die Zeit knapp wird, nicht über die Größe. Formeln in 4.3.

#### 3.4.2 Minispiel "Sternen-Labyrinth" (`sternen_labyrinth`)

| Aspekt | Spezifikation |
|--------|---------------|
| Ziel | Als erste(r) durch das Labyrinth zum Zielstern gelangen. |
| Siegbedingung | Ziel-Ankunftsreihenfolge: Die ersten 3 im Ziel erhalten einen Bonus (siehe `minigame-rewards.md` Abschnitt 3.6). Wer das Ziel nicht erreicht, wird nach erreichter Wegstrecke platziert. `results_mode = "by_position"` (für Zielankunft) kombiniert mit Strecken-Score für Nicht-Angekommene (Framework mischt: Angekommene vor Nicht-Angekommenen, innerhalb der Gruppen nach Reihenfolge bzw. Strecke). |
| Kernmechanik | Jeder Spieler löst **dasselbe** Labyrinth in seinem eigenen Viewport (bei 2–4 Split-Screen, bei 5–8 … siehe Edge Case 4). Startposition und Ziel sind identisch; das Layout ist pro Spieler zufällig gespiegelt/rotiert (Spiegelung/4-fache Rotation), damit Abschauen über den Nachbar-Viewport nicht hilft, aber die Lösungsstruktur identisch bleibt (Fairness). |
| Labyrinth-Erzeugung | Prozedural: perfektes Labyrinth (keine Zyklen, genau ein Pfad Start→Ziel) mit Seitenlänge `s(n)` (Formel 4.3.1). |
| Steuerung | Bewegung (`up/down/left/right`) — nur orthogonal, keine Diagonalen, Kollision mit Wänden. |
| Früh-Ende | `request_end()`, sobald alle Spieler das Ziel erreicht haben; läuft bis `duration`, wenn nicht alle ankommen. |
| Skalierung | Seitenlänge `s(n)` (4.3.1). |
| Fairness | Identische Lösungsstruktur (nur gespiegelt/rotiert), identische Start-/Zielposition relativ zum Layout. |

#### 3.4.3 Minispiel "Insel-Memory" (`insel_memory`)

| Aspekt | Spezifikation |
|--------|---------------|
| Ziel | In 30 s die meisten Kartenpaare finden. |
| Siegbedingung | Höchste Paar-Zahl nach Ablauf. `results_mode = "by_points"`. |
| Kernmechanik | Jeder Spieler hat ein eigenes Kartenfeld (4×4 = 8 Paare) mit Insel-Motiv-Karten (je 2× Sonnenstrand, Zuckerwald, Wolkenwerk, Frostgipfel, Dschungeltempel, Mechanik-Stadt, Sternenzitadelle, ArenaStar). Zwei Karten aufdecken (`action1`); ein Paar bleibt offen und zählt 1 Punkt, ein Nicht-Paar wird wieder zugedeckt. |
| Karten-Anordnung | Pro Spieler zufällig und unabhängig gemischt (jeder hat eine andere Anordnung). |
| Steuerung | Cursor über das eigene Feld bewegen (Richtungstasten), Karte aufdecken (`action1`). |
| Früh-Ende | Keines — volle `duration`. |
| Skalierung | Keine (Feld konstant 4×4, 8 Paare). Bei mehr Spielern bleibt die Aufgabe gleich; der Wettbewerb entsteht über die Parallele. |
| Fairness | Identische Feldgröße und Karten-Satz für alle; unabhängige Mischung verhindert Abschauen. |

### 3.5 Rechnen/Wort (2 Minispiele)

#### 3.5.1 Kategorie-Profil

- **Was macht sie besonders?** Kognitive, bildungsnahe Herausforderung: schnelles Kopfrechnen und Sprachspiel. Die Interaktion ist präziser und langsamer als bei den Aktions-Kategorien; die Spannung entsteht aus der **inneren** Rechen-/Denkzeit, nicht aus Reflexen.
- **Für welche Spieler?** Ältere Kinder, Erwachsene und sprachstarke Spieler (Bartle "Achiever", Quantic-Foundry "Mastery/Strategy", "Achievement/Power"); gut für Schulkinder, die ihr Können zeigen wollen.
- **Zugänglichkeits-Hinweis:** Lesen/Schreiben ist erst ab etwa 6–7 Jahren voll entwickelt; das Wort-Puzzle gilt deshalb als das anspruchsvollste Minispiel für jüngere Kinder. Es bleibt im Pool (Vielfalt), wird aber in `ui-accessibility.md` als Kategorie mit erhöhtem Lese-Bedarf markiert.
- **Schwierigkeits-Skalierung mit Spielerzahl:** Der Zahlen- bzw. Buchstabenbereich wächst mit der Spielerzahl, damit die Streuung der Antworten und damit der Wettbewerb erhalten bleibt. Formeln in 4.4.

#### 3.5.2 Minispiel "Münz-Zähler" (`muenz_zaehler`)

| Aspekt | Spezifikation |
|--------|---------------|
| Ziel | Die von ArenaStar kurz gezeigte Münzmenge möglichst genau schätzen. |
| Siegbedingung | Höchste Punktzahl über 5 Runden; pro Runde erhält der/die Nächstliegende 3 Punkte, die/der Zweitnächste 2, die/der Drittnächste 1. `results_mode = "by_points"` mit `score` = Rundensumme. |
| Kernmechanik | 5 Runden à ca. 5–6 s. Pro Runde zeigt ArenaStar 2 s lang einen Haufen aus Münzen (z. B. 18 Stück) in der Arena-Mitte; danach wird der Haufen verdeckt. Jeder Spieler tippt seine Schätzung ein. Nach Ablauf der Eingabezeit (3 s) wird aufgedeckt; die Nächstliegenden erhalten Rundenpunkte. |
| Eingabe | Zahl wählen über Hoch/Runter (Richtungstasten) im Bereich 0–99 + Bestätigen (`action1`). Die gewählte Zahl ist groß im eigenen Viewport sichtbar. |
| Gleichstand in der Distanz | Zwei Spieler mit identischer Distanz zur richtigen Zahl teilen sich die Rundenpunkte der betroffenen Plätze (Mittelung, ganzzahlig). |
| Früh-Ende | Keines — läuft über die 5 Runden (Gesamtdauer ≈ `duration` = 30 s). |
| Skalierung | Zahlenbereich `[lo(n), hi(n)]` (Formeln 4.4.1/4.4.2). |
| Fairness | Alle sehen denselben Münzhaufen gleich lange; die Eingabezeit ist für alle gleich; die Reihenfolge der Eingabe spielt keine Rolle (parallele Abgabe). |

#### 3.5.3 Minispiel "Wort-Puzzle" (`wort_puzzle`)

| Aspekt | Spezifikation |
|--------|---------------|
| Ziel | Aus den gezeigten Buchstaben das längste gültige Wort der Spielsprache bilden. |
| Siegbedingung | Längstes gültiges Wort gewinnt; bei gleicher Länge gewinnt die frühere Bestätigung (Zeitstempel). `results_mode = "by_position"` mit Zeitstempel-Tiebreak. |
| Kernmechanik | ArenaStar zeigt eine Auswahl von Buchstaben-Kacheln (z. B. 8 Kacheln). Jeder Spieler wählt Kacheln aus (Cursor + `action1`) und setzt sie zu einem Wort zusammen; jedes Zeichen ist nur einmal verwendbar. Mit `action2` wird das Wort eingereicht. Nur Wörter, die im Wörterbuch der aktuellen Spielsprache existieren, sind gültig; ungültige Einreichungen zählen 0 Punkte (Spieler können bis zum Timer-Ende neu einreichen, die beste gültige Einreichung zählt). |
| Wörterbuch | Das Wörterbuch der Spielsprache wird mitgeliefert (Basissatz für Kinder: Wörter ab 3 Buchstaben). Sprache = aktuelle Spielsprache (lokalisiert). |
| Dauer | `duration = 20` s (kürzer als Standard; erlaubt laut `minigame-architecture.md` Abschnitt 4.5). |
| Steuerung | Cursor (`up/down/left/right`) + Buchstabe wählen (`action1`) + einreichen (`action2`). |
| Früh-Ende | `request_end()`, sobald alle Spieler eine gültige Einreichung abgegeben haben. |
| Skalierung | Buchstaben-Anzahl `L(n)` (Formel 4.4.3). |
| Fairness | Alle sehen dieselbe Buchstaben-Auswahl; die Anordnung der Kacheln ist pro Spieler zufällig (aber gleiche Buchstaben-Menge), damit Abschauen nicht hilft. |

### 3.6 Kooperation (2 Minispiele)

#### 3.6.1 Kategorie-Profil

- **Was macht sie besonders?** Alle Spieler verfolgen ein gemeinsames Ziel; es gibt keine Verlierer im klassischen Sinn — die Gruppe wird gemeinsam belohnt. Wirkt als "Versöhnungs-Minispiel" nach kompetitiven Runden und stärkt das Gemeinschaftsgefühl (Relatedness).
- **Für welche Spieler?** Familien, Socializer (Bartle "Socializer", Quantic-Foundry "Social/Community") und jüngere Kinder, die Wettbewerb als unangenehm empfinden.
- **Schwierigkeits-Skalierung mit Spielerzahl:** Der Aufgabenumfang wächst mit der Spielerzahl, sodass der Pro-Kopf-Arbeitsanteil konstant bleibt (Brücke: 1 Segment pro Spieler). Bei Team-Koop wächst die Teamgröße; die Belohnung folgt dem Team-Ergebnis. Formeln in 4.5.
- **Belohnung:** Koop-Minispiele zahlen allen eine Basis von 5 Münzen plus einen Leistungs-Bonus (Details in `minigame-rewards.md` Abschnitt 3.6).

#### 3.6.2 Minispiel "Sternen-Brücke" (`sternen_bruecke`)

| Aspekt | Spezifikation |
|--------|---------------|
| Ziel | Gemeinsam eine Brücke über eine Schlucht bauen. |
| Siegbedingung | Keine Einzelplatzierung: Der **Fortschritt** (Anteil der gesetzten Segmente) bestimmt den Bonus für ALLE. `team_mode = "coop_all"`. |
| Kernmechanik | Am Rand liegen Brücken-Segmente (Bretter). Jeder Spieler hebt ein Segment auf (`action1`), trägt es zur Lücke und setzt es ein (`action1` an der Einbauposition). Segmente müssen in Reihenfolge von der eigenen Seite her eingebaut werden. Es gibt keine Gegner, keine Hindernisse, keinen Zeitdruck außer dem Timer. |
| Fortschritt | `Fortschritt = gesetzte_Segmente / M(n)` (in %). Je höher der Fortschritt bei Timer-Ende, desto höher der Bonus (Formel in `minigame-rewards.md` Abschnitt 4.4). |
| Steuerung | Bewegung (`up/down/left/right`) + Aufheben/Einsetzen (`action1`). |
| Früh-Ende | `request_end()`, sobald die Brücke vollständig ist (100 %). |
| Skalierung | Segmentanzahl `M(n)` (Formel 4.5.1). |
| Fairness | Kein Wettbewerb; alle können gleichzeitig tragen; Segmente sind überall gleich weit entfernt von der Einbauposition (symmetrische Anordnung der Segment-Stapel). |

#### 3.6.3 Minispiel "Schatz-Trage" (`schatz_trage`)

| Aspekt | Spezifikation |
|--------|---------------|
| Ziel | Als Team den Schatz schneller als das andere Team durch die Hindernisstrecke ins Ziel tragen. |
| Siegbedingung | Team-Platzierung: Siegerteam erhält den Team-Bonus, Verliererteam den Trost-Bonus (Details `minigame-rewards.md` Abschnitt 3.6). `team_mode = "coop_teams"`. |
| Kernmechanik | 2 gleich große Teams (2v2, 3v3 oder 4v4). Jedes Team trägt eine Schatztruhe gemeinsam über eine Strecke mit Hindernissen (Hügel, enge Passagen, schwingende Pendel). Die Truhe bewegt sich nur, wenn **alle** Teammitglieder in Trage-Reichweite (2 m) sind und sich in dieselbe Richtung bewegen; verlässt jemand den Radius, stoppt die Truhe (kurze Aufforderung "Hilf mit!"). Erreicht ein Team das Ziel, gewinnt es; das andere Team wird nach zurückgelegter Strecke platziert. |
| Team-Bildung | Deterministisch nach Spielernummer: Team A = ungerade Nummern (1,3,5,7), Team B = gerade Nummern (2,4,6,8). Dadurch sind die Teams bei Sitzordnung und Controller-Verteilung zufällig fair. |
| Spielerzahl | `players.min = 4` (2v2). Bei n = 3, 5, 7 ist das Minispiel nicht im Pool (ungerade Teams nicht zulässig). |
| Steuerung | Bewegung (`up/down/left/right`); Tragen ist automatisch (Nähe). |
| Früh-Ende | `request_end()`, sobald ein Team das Ziel erreicht. |
| Skalierung | Teamgröße `g(n)` (Formel 4.5.2); Streckenlänge und Hindernisdichte konstant (50 m, 3 Hindernistypen). |
| Fairness | Beide Strecken sind identisch (parallele, gespiegelte Bahnen); beide Teams starten gleichzeitig nach dem Countdown. |

## 4. Formulas

### 4.1 Geschicklichkeit

Sei `n` die Spielerzahl (2–8).

**4.1.1 Münzregen — Arena-Fläche:** `A(n) = 36 + 8·(n − 2)` m²

- Beispiel: n=2 → 36 m², n=8 → 84 m². Die Dichte bleibt ähnlich; mehr Spieler brauchen mehr Raum, damit die Konkurrenz nicht erdrückend wird.

**4.1.2 Münzregen — Spawn-Rate:** `r(n) = 0,8 + 0,15·n` Münzen pro Sekunde

- Beispiel: n=2 → 1,1/s (≈ 33 über 30 s), n=8 → 2,0/s (≈ 60 über 30 s).
- Sternmünzen-Anteil: 10 % der Spawns (Wert 5, siehe 3.2.2).
- Erwartete Gesamtpunkte über 30 s bei n Spielern: `≈ 30 · r(n) · (0,9·1 + 0,1·5) = 30 · r(n) · 1,4`. Für n=8: `30 · 2,0 · 1,4 = 84` Punkte im Umlauf — bei 8 Spielern im Schnitt 10,5 Punkte pro Spieler, genug Streuung für eine klare Rangfolge.

**4.1.3 Zielwurf — Arena-Fläche:** `A(n) = 49 + 10·(n − 2)` m²

- Beispiel: n=2 → 49 m² (7×7), n=8 → 109 m². Größere Arena = mehr Ausweichraum bei mehr Werfern.

**4.1.4 Zielwurf — Bälle im Umlauf:** `B(n) = 3·n`

- Beispiel: n=2 → 6 Bälle, n=8 → 24 Bälle. Konstant 3 Bälle pro Spieler im Umlauf (siehe 3.2.4).

### 4.2 Reaktion

**4.2.1 ArenaStar sagt — Runden:** `R(n) = ceil(n/2) + 2`

- Beispiel: n=2 → 3 Runden, n=4 → 4 Runden, n=8 → 6 Runden. Genug Runden, damit die Rangfolge bei 8 Spielern aufgelöst wird, ohne die 30 s zu sprengen.

**4.2.2 ArenaStar sagt — Tempo-Faktor:** `t(r) = 1 + 0,15·(r − 1)` für Runde r (r = 1…R)

- Kommando-Intervalle (Zeit von Kommando-Anzeige bis zum nächsten Kommando) starten bei 3,0 s und schrumpfen: `Intervall(r) = 3,0 / t(r)`. Beispiel: Runde 1 → 3,0 s, Runde 4 → 3,0/1,45 ≈ 2,07 s, Runde 6 → 3,0/1,75 ≈ 1,71 s. Das Tempo steigt spürbar, aber kontrolliert.

**4.2.3 Blitz-Fangen — Score-Definition:** `score(i) = Überlebenszeit_i` in Sekunden; bei identischer Überlebenszeit entscheidet `Herzen_i` (höher besser); das Framework sortiert absteigend nach `(Überlebenszeit, Herzen)`.

- Damit sind "länger überlebt" und "bei Timer-Ende mehr Herzen" korrekt abgebildet.

**4.2.4 Blitz-Fangen — Blitz-Frequenz:** `f(n) = 0,8 + 0,1·n` Blitze pro Sekunde

- Beispiel: n=2 → 1,0/s, n=8 → 1,6/s (≈ 48 Blitze über 30 s). Bei 8 Spielern ist die Arena voller Einschlagkreise → höhere Ausweich-Herausforderung, aber jeder Kreis ist telegrafiert (1 s Vorwarnung).

### 4.3 Puzzle/Logik

**4.3.1 Sternen-Labyrinth — Seitenlänge:** `s(n) = 4 + ceil(n/2)` Zellen

- Beispiel: n=2 → 5 (25 Zellen), n=4 → 6 (36 Zellen), n=8 → 8 (64 Zellen). Zellenzahl: `Z(n) = s(n)²`.

**4.3.2 Insel-Memory — Feldgröße:** konstant 4×4 = 16 Karten = 8 Paare, unabhängig von n. Keine Formel.

### 4.4 Rechnen/Wort

**4.4.1 Münz-Zähler — Bereichs-Untergrenze:** `lo(n) = 3 + 2·(n − 2)`

- Beispiel: n=2 → 3, n=8 → 15. Die kleinsten Mengen wachsen mit der Spielerzahl, damit die Aufgabe nie trivial wird.

**4.4.2 Münz-Zähler — Bereichs-Obergrenze:** `hi(n) = 10 + 5·(n − 2)`

- Beispiel: n=2 → 10, n=4 → 20, n=8 → 40. Der Zählbereich wird bei mehr Spielern größer → mehr Streuung der Schätzungen, feinere Rangfolge.

**4.4.3 Wort-Puzzle — Buchstaben-Anzahl:** `L(n) = 6 + floor((n − 2)/2)`

- Beispiel: n=2 → 6, n=4 → 7, n=6 → 8, n=8 → 9. Mehr Buchstaben erlauben längere Wörter; die maximale Wortlänge (und damit der Schwierigkeitsgrad) wächst leicht mit n.

### 4.5 Kooperation

**4.5.1 Sternen-Brücke — Segmente:** `M(n) = n`

- Beispiel: n=2 → 2 Segmente, n=8 → 8 Segmente. Jede Person trägt im Schnitt 1 Segment; der Pro-Kopf-Arbeitsanteil ist konstant.
- Fortschritt: `Fortschritt = gesetzte_Segmente / M(n) × 100` (%).

**4.5.2 Schatz-Trage — Teamgröße:** `g(n) = n/2`

- Beispiel: n=4 → 2v2, n=6 → 3v3, n=8 → 4v4. Nur gerade n ≥ 4 gültig (3.6.3).

### 4.6 Beispielrechnung: 8-Spieler-Partie

- Kategorie Geschicklichkeit (Münzregen): Arena 84 m², Spawn-Rate 2,0/s, ~84 Punkte im Umlauf.
- Kategorie Reaktion (Blitz-Fangen): 1,6 Blitze/s, 3 Herzen je Spieler, Vorwarnung 1 s.
- Kategorie Puzzle (Sternen-Labyrinth): 8×8-Zellen-Labyrinth.
- Kategorie Rechnen (Münz-Zähler): Zählbereich 15–40.
- Kategorie Kooperation (Sternen-Brücke): 8 Segmente.

Alle Werte sind über die Tuning-Knobs (Abschnitt 7) anpassbar; die Formeln definieren die Standard-Kurven.

## 5. Edge Cases

1. **Sternen-Labyrinth bei 5–8 Spielern:** Es gibt keinen Split-Screen. Lösung: Das Labyrinth wird bei n ≥ 5 nicht pro Spieler als eigener Viewport gelöst, sondern **nacheinander sichtbar**: Jeder Spieler löst sein (gespiegeltes) Labyrinth im Vollbild, und die Spieler starten zeitversetzt (Staffel-Start: Spieler 2 startet 1 s nach Spieler 1 usw.), während die bisherigen Läufe als Mini-Vorschau in einer Leiste laufen. Alternativ wird die Ziel-Position pro Spieler durch eine eigene Markierungsfarbe im gemeinsamen Vollbild angezeigt, wenn das Labyrinth in der Vogelperspektive für alle gleich bleibt. **Entscheidung:** Bei n ≥ 5 gilt die Staffel-Variante; sie wird in `minigame-template.md` als Referenzlösung für "nicht parallelisierbare" Minispiele dokumentiert. (Design-Entscheidung, dokumentiert gemäß bible-index.md Regel 3.1.2.)
2. **Balance-Akt — alle fallen gleichzeitig:** Zwei oder mehr Spieler berühren gleichzeitig den Boden. Sie teilen sich den Platz (Gleichstand, Mittelung in `minigame-rewards.md`).
3. **ArenaStar sagt — alle scheiden in derselben Runde aus:** Es gibt keinen Platz 1. Die Ausgeschiedenen teilen sich den letzten gemeinsamen Platz; niemand erhält den Siegerplatz. Framework-Handling: `request_end()` bei 0 verbleibenden Spielern nach der Runde.
4. **Blitz-Fangen — alle auf 0 Herzen gleichzeitig:** Wie Fall 2 — geteilte Platzierung nach gleicher Überlebenszeit.
5. **Zielwurf — kein Treffer in den ersten 10 s:** Tuning-Fall; die Treffer-Erwartung pro Spieler muss bei ca. 0,5 Treffern pro 5 s liegen. Falls im Playtest die Trefferquote zu niedrig ist, wird der Ball-Durchmesser oder die Ballgeschwindigkeit erhöht (Knob 7.5).
6. **Münz-Zähler — gleiche Distanz zweier Antworten:** Beide teilen sich die Rundenpunkte der betroffenen Plätze (Mittelung). Beispiel: richtig = 18, Antworten 16 und 20 (beide Distanz 2) für Platz 1/2 → beide erhalten (3+2)/2 = 2,5 → kaufmännisch 3 Rundenpunkte (siehe `minigame-rewards.md` Abschnitt 4.2).
7. **Wort-Puzzle — kein gültiges Wort gefunden:** Einreichung zählt 0 Punkte; der Spieler wird nach Wortlänge 0 platziert (bei mehreren mit 0 entscheidet die frühere (ungültige) Einreichung nicht — alle 0er teilen sich den Platz).
8. **Wort-Puzzle — Kinder können nicht lesen:** Die Kacheln zeigen zusätzlich ein Bild-Symbol pro Buchstaben? Nein — stattdessen gilt: Das Minispiel hat `players.min` keine Alterssperre, aber die UI zeigt eine "Wörterbuch-Hilfe" (kurze Wörter ab 3 Buchstaben werden hervorgehoben). In `ui-accessibility.md` wird die Kategorie als leseintensiv markiert.
9. **Sternen-Brücke — niemand hilft:** Fortschritt 0 %, alle erhalten nur die Koop-Basis (5 Münzen) ohne Bonus (rewards Abschnitt 3.6).
10. **Sternen-Brücke — ein Spieler trägt allein:** Möglich; der Pro-Kopf-Anteil ist nicht erzwingbar. Der Bonus ist gruppenweit, daher besteht kein Anreiz, andere auszuschließen (alle profitieren).
11. **Schatz-Trage — Truhe bleibt stecken (Team verstreut):** Die Truhe stoppt; die UI zeigt "Hilf mit!" an den entfernten Spieler. Läuft der Timer ab, ohne dass ein Team das Ziel erreicht, wird nach zurückgelegter Strecke platziert (beide Teams nach Distanz).
12. **Schatz-Trage — ein Teammitglied disconnected:** Die Truhe kann sich nicht mehr bewegen (nicht alle in Reichweite). Regel: Ab 1 fehlendem Teammitglied gilt das Team als disqualifiziert (letzter Platz); das andere Team gewinnt, sobald es das Ziel erreicht oder der Timer abläuft.
13. **Ungerade Spielerzahl bei Schatz-Trage:** Minispiel nicht im Pool (min 4); die Selektion filtert es (Architektur Edge Case 4).
14. **Alle Spieler einer Runde eliminieren sich gleichzeitig (Balance-Akt, ArenaStar sagt):** Rahmen-Regel: Es gibt immer mindestens einen Platz 1. Sind alle eliminiert, gilt die Eliminations-Zeitreihenfolge (Millisekunden-Auflösung); bei exakt identischer Zeit teilen sich alle Platz 1 (Mittelung).

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `minigame-categories.md` | Art | Verwendung |
|-----------------------------------------|-----|------------|
| `design/gdd/minigame-architecture.md` | Peer | Definiert Rahmen (Lebenszyklus, Timer, Kamera, Input), den alle Kategorien einhalten. |
| `design/gdd/minigame-rewards.md` | Nachgeordnet | Setzt die in 3.6 erwähnten Koop- und Bonus-Regeln konkret um. |
| `design/gdd/minigame-template.md` | Nachgeordnet | Müssen die 12 Minispiele als Vorlagen-konforme Plugins beschrieben sein. |
| `design/gdd/game-concept.md` | Quelle | 5 Kategorien, ~30 s, 2–8 Spieler. |
| `design/gdd/glossary.md` | Peer | Begriffe wie "Telegrafieren", "Eliminationsreihenfolge", "Koop-Basis". |
| `design/gdd/ui-accessibility.md` | Nachgeordnet | Markiert die Kategorien mit erhöhtem Lese-/Altersbedarf (Rechnen/Wort). |
| `design/gdd/audio-sfx.md` | Nachgeordnet | Benötigt kategoriespezifische Sounds (Münz-Sammeln, Blitz, Countdown-Tick). |
| `.claude/rules/design-docs.md` | Regelwerk | 8-Sektionen-Standard. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `minigame-architecture.md` | Muss die in 3.2–3.6 beschriebenen Minispiele mit dem Schnittstellenvertrag (dort 3.2) ladbar halten (results_mode, team_mode). |
| `minigame-rewards.md` | Muss für `coop_all`/`coop_teams` (Sternen-Brücke, Schatz-Trage) die Auszahlung nach diesen Regeln berechnen. |
| `minigame-template.md` | Muss die Kategorie-IDs (`geschicklichkeit`, `reaktion`, `puzzle`, `rechnen`, `kooperation`) als gültige `category`-Werte führen. |
| `technical-fork-strategy.md` | Muss die 6 STP-Minispiele auf diese 5 Kategorien abbilden (oder abstoßen). |
| `technical-performance.md` | Muss die Arena-Größen (4.1–4.5) im Performance-Budget (Viewport-Kosten, Objektzahlen) berücksichtigen. |

### 6.3 Bidirektionalität

Die Kategorien sind die inhaltliche Füllung des Frameworks: `minigame-architecture.md` definiert den Container, dieses Kapitel die Inhalte. Die Abhängigkeit zu `minigame-rewards.md` ist wechselseitig — die Kategorien definieren die Koop-Modi, die Belohnungen definieren die Auszahlung dafür. Die Abhängigkeit zu `technical-fork-strategy.md` ist eine Migrations-Spiegelung: Die Zuordnung der bestehenden STP-Minispiele zu den Kategorien muss dort beschrieben sein.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Arena-Flächen-Baseline und -Wachstum (4.1.1, 4.1.3) | Kurve | Baseline 25–60, Wachstum 5–15 | 36/8 bzw. 49/10 | Raumgefühl und Ausweichmöglichkeiten. |
| Münz-Spawn-Rate `r(n)` (4.1.2) | Kurve | 0,5–3,0 Münzen/s | 0,8 + 0,15·n | Punkte-Dichte und Sammel-Erfolgserlebnis. |
| Sternmünzen-Anteil | Kurve | 0–20 % | 10 % | Spannung durch Sonderpunkte. |
| Bälle pro Spieler (4.1.4) | Kurve | 2–5 | 3 | Wurf-Frequenz und Munitionsdruck. |
| Ball-Treffer-Erwartung (Zielwurf) | Feel | 0,3–0,8 Treffer/5 s/Spieler | 0,5 | Steuert, ob Treffer selten (Jubel) oder häufig (Fluss) sind. |
| Blitz-Frequenz `f(n)` (4.2.4) | Kurve | 0,5–2,5 Blitze/s | 0,8 + 0,1·n | Bedrohungsdichte; zu hoch = unfair, zu niedrig = langweilig. |
| Blitz-Vorwarnzeit | Feel | 0,5–2,0 s | 1,0 s | Fairness der Ausweichbarkeit. |
| ArenaStar-sagt-Runden `R(n)` (4.2.1) | Kurve | 3–10 | ceil(n/2)+2 | Auflösung der Rangfolge vs. Rundendauer. |
| Kommando-Tempo-Start und -Wachstum (4.2.2) | Kurve | Start 2–4 s, Wachstum 0,1–0,25 | 3,0 s / 0,15 | Schwierigkeitsanstieg über die Runden. |
| Labyrinth-Seitenlänge `s(n)` (4.3.1) | Kurve | 4–10 | 4 + ceil(n/2) | Lösungsdauer und Kopfbeschäftigung. |
| Memory-Feldgröße | Gate | 4×4 (8 Paare) oder 4×3 (6 Paare) | 4×4 | Spieldichte; 4×3 für jüngere Zielgruppen. |
| Münz-Zähler-Bereich `lo/hi` (4.4.1/4.4.2) | Kurve | lo 3–15, hi 10–40 | 3+2(n−2), 10+5(n−2) | Schwierigkeit des Kopfrechnens. |
| Münz-Zähler-Runden | Gate | 3–7 | 5 | Wie oft gezählt wird; bestimmt die Gesamtdauer. |
| Wort-Puzzle-Buchstaben `L(n)` (4.4.3) | Kurve | 5–12 | 6 + floor((n−2)/2) | Maximale Wortlänge und Schwierigkeit. |
| Wort-Puzzle-Dauer | Gate | 15–30 s | 20 s | Denk- und Tipp-Zeit. |
| Brücken-Segmente `M(n)` (4.5.1) | Kurve | 1–2·n | n | Pro-Kopf-Arbeitslast. |
| Schatz-Trage-Streckenlänge | Gate | 30–70 m | 50 m | Rundenlänge und Team-Synchronisation. |
| Trage-Reichweite | Feel | 1–3 m | 2 m | Wie streng die Team-Synchronisation ist. |

Alle Knobs liegen in externen Datenquellen (`assets/data/minigame_*.cfg`), nie im Code.

## 8. Acceptance Criteria

Ein QA-Tester kann folgende Prüfungen ausführen:

1. **Kategorie-Validierung:** Jedes der 12 Minispiele trägt in `minigame.json` genau einen gültigen `category`-Wert aus `geschicklichkeit`, `reaktion`, `puzzle`, `rechnen`, `kooperation`; die Verteilung ist 3/3/2/2/2. PASS/FAIL.
2. **Spielbarkeit 2–8:** Jedes Minispiel ist mit 2, 4 und 8 Spielern spielbar und produziert eine vollständige Platzierung 1–n ohne Absturz. PASS/FAIL.
3. **Dauer:** Kein Minispiel überschreitet das harte 30-s-Limit (Wort-Puzzle deklariert 20 s); alle enden spätestens bei Timer-Ablauf. PASS/FAIL.
4. **Eindeutige Siegbedingung:** Für jedes Minispiel kann ein Tester die Siegbedingung in einem Satz nennen und am Spielende die Platzierung aus den angezeigten Werten nachvollziehen. PASS/FAIL.
5. **Skalierungsformeln:** Für jedes Minispiel wird die Skalierung bei n=2 und n=8 anhand der Formeln in Abschnitt 4 berechnet und im Spiel nachgemessen (z. B. Arena-Fläche, Spawn-Rate, Labyrinth-Größe). PASS/FAIL.
6. **Fairness Startpositionen:** Bei 5 Testläufen mit jeweils gleicher Spielerzahl starten Spieler in symmetrischen Positionen; kein Startpunkt erzeugt einen statistisch signifikanten Vor-/Nachteil (erwartete Punktzahl ± 5 %). PASS/FAIL.
7. **Koop-Modi:** Sternen-Brücke zahlt bei 100 % Fortschritt den vollen Bonus an alle; Schatz-Trage zahlt Sieger- und Verlierer-Bonus korrekt an die Team-Mitglieder (Abgleich mit `minigame-rewards.md`). PASS/FAIL.
8. **Team-Bildung:** Bei 4, 6 und 8 Spielern bildet Schatz-Trage korrekt 2v2, 3v3, 4v4 nach ungerade/gerade Spielernummer; bei n=3, 5, 7 ist das Minispiel nicht im Pool. PASS/FAIL.
9. **Zugänglichkeit (ab 6):** In einem Playtest mit mindestens 2 Kindern (6–8 Jahre) verstehen sie nach dem einmaligen Intro jedes der 12 Minispiele und können ohne weitere Hilfe mitspielen (2-Minuten-Test-Analogie aus `vision-pillars.md`). PASS/FAIL.
10. **Kategorien-Mix:** Über 12 aufeinanderfolgende Minispiel-Runden (mit n ≥ 4) erscheint jede der 5 Kategorien mindestens einmal (Selektion ohne Gewichtung; reine Zufalls-Schwankung toleriert, bei Verfehlung wird der Seed geprüft). PASS/FAIL.
11. **Erlebbar (Experiential):** In einem Playtest mit 8 Spielern gibt mindestens die Hälfte der Teilnehmer an, eine Kategorie zu haben, in der sie sich stark fühlen (Selbsteinschätzung nach der Partie, 1–5-Skala, Ziel ≥ 4). PASS/FAIL.
