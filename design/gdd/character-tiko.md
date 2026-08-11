# Tiko — Party Arena Game Bible

> **Teil:** V — Characters (5.6)
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** `design/gdd/game-concept.md`, `design/gdd/characters-overview.md`

---

## 1. Overview

Tiko ist der **Vogel** (tukan-ähnlich) aus dem Dschungeltempel — chaotisch, laut und unwiderstehlich komisch. Sein Markenzeichen ist der übergroße, bunte Schnabel; sein Körper ist mit Regenbogen-Federn bedeckt, und hinter ihm fliegen immer ein paar Federn durch die Luft. Seine Signaturfarbe ist Grün (`#2bffb9`). Tiko stolziert mit hohen Schritten, klappert mit dem Schnabel, dreht den Kopf ruckartig und explodiert bei Freude geradezu in eine Feder-Wolke. Wie alle Arenians hat er keinerlei spielmechanische Vorteile — sein Chaos ist reine Inszenierung aus Animation, Partikeln und Sound, gemappt auf dieselbe Feld-zu-Feld-Geschwindigkeit wie bei allen anderen.

Dieses Kapitel spezifiziert Tiko vollständig: Identität, visuelles Design, alle 12 Pflichtanimationen, Porträt, Siegerpose, optionale Voice-Lines, Heimat-Bezug und Strategie-Tipp. Es ist an den Vertrag aus `characters-overview.md` gebunden.

| Kernfakt | Wert |
|----------|------|
| ID / Ordnername | `tiko` |
| Anzeigename | Tiko |
| Typ | Vogel (Tukan) |
| Heimat-Insel | Dschungeltempel |
| Persönlichkeit | chaotisch, lustig, Feder-Wirbel |
| Primärfarbe | Grün `#2bffb9` |
| Silhouetten-Archetyp | großer Schnabel als Markenzeichen, aufrechte Haltung |
| Modellhöhe | 1,2 Einheiten (1,08–1,32) |
| Trefferbox | Zylinder oder Kapsel, Radius 0,6, Höhe 1,2 |

## 2. Player Fantasy

Tiko spielt sich wie der **Partylärm in Person**: Wer Tiko wählt, ist laut, unberechenbar und immer für einen Auftritt zu haben. Er verwandelt jede ruhige Situation in ein Spektakel — Federn fliegen, der Schnabel klappert, und sein "Kraa!" ist nicht zu überhören. Die Fantasie dahinter lautet: **"Ich bin der Mittelpunkt — ob ihr wollt oder nicht."** Tikos Chaos ist dabei ansteckend fröhlich, niemals nervig-bösartig; er ist der Vogel, den man einfach gern haben muss.

Design-Pillar-Bezug: **Sofort verständlich** — der übergroße Schnabel ist das eindeutigste Einzelmerkmal aller Arenians. **Überzeichnet** — Tikos Emotionen sind Explosionen: Federn explodieren bei Freude, Federn fallen bei Trauer. **Interaktiv wirkend** — sein Feder-Schweif reagiert auf jede Bewegung, der Kopf dreht sich ruckartig wie bei einem echten, aufgeregten Vogel. **Wiedererkennbar** — Grün + Regenbogen-Federn + Riesen-Schnabel: Tiko ist auf jedem Bildschirm sofort zu finden. Er ist der Beweis, dass ein Charakter durch reine Performance ("Entertainer") auffällt, ohne Spielwert-Vorteile zu brauchen.

## 3. Detailed Rules

### 3.1 Identität und Kernaussage

Tiko lebt im Dschungeltempel (`world-dschungeltempel.md`), wo er zwischen goldenen Ruinen und dichtem Blattwerk seine Stimme trainiert — zum Entsetzen aller, die Ruhe suchen. Seine Kernaussage: **"Warum leise, wenn laut auch geht?"** Er ist der selbsternannte Zeremonienmeister des Tempels und nimmt sich selbst nie ernst.

### 3.2 Visuelles Design

1. **Modell:** Tukan-ähnlicher Vogel im Cartoon/Toy-Stil, hohe Sättigung, aufrechte Haltung (Vogelkörper auf zwei langen, dünnen Stelzenbeinen). Der Körper ist kompakt, die Flügel sind kurz.
2. **Schnabel:** Übergroß, etwa 0,5 Einheiten lang, bunt in Gelb-Orange-Tönen (`#ffb703`, `#fb8500`) mit dunkler Spitze. Das größte Einzelmerkmal; leicht geöffnet im Grundzustand.
3. **Federkleid:** Regenbogen-Farbverlauf über Brust und Rücken (Rot → Orange → Gelb → Grün → Blau), mit der Signaturfarbe Grün (`#2bffb9`) als dominierender Brustfarbe. Flügelaußenseiten in kräftigem Grün.
4. **Kopf:** Runde, große Augen (`#1a2a2a` mit Glanzpunkten) seitlich am Kopf; ein kleiner Feder-Schopf oben, der bei Emotionen aufgestellt werden kann.
5. **Feder-Schweif:** Hinter Tiko fliegen permanent 2–3 lose Federn mit (Partikel/Anhängsel), die seine Bewegung begleiten. Bei `happy` explodieren viele Federn, bei `sad` fallen welche zu Boden.
6. **Textur:** Glatte, glänzende Federn (Toy-Look, hohe Sättigung, weiche Schattierung). Keine realistischen Einzelfedern als Textur — stattdessen klare, bunte Flächen.

### 3.3 Silhouette

- **Archetyp:** Aufrechter Vogel auf Stelzenbeinen mit **übergroßem Schnabel** als dominanter Auskragung nach vorne.
- **Erkennung:** Der Schnabel ist das Markenzeichen — in der Silhouette ragt er deutlich über den Körper hinaus (Länge ca. 40 % der Höhe). Die Stelzenbeine und der aufrechte Stand unterscheiden Tiko von allen anderen.
- **Abgrenzung:** Anders als Pip (klein, buschiger Schwanz) ist Tiko groß, aufrecht und mit langem Schnabel; anders als Koko (Kugel) ist Tiko gestreckt und eckig im Kopfbereich.

### 3.4 Standardmaße und Kollision

- Modellhöhe `H = 1,2` (Toleranz 1,08–1,32). Der Schnabel ragt nach vorne, die Feder-Anhängsel nach hinten — beide nicht kollidierend.
- **Schnabellänge:** `L_Schnabel ≤ 0,6` Einheiten (visuell, nicht kollidierend).
- Trefferbox identisch zum Standard: Zylinder oder Kapsel, Radius 0,6, Höhe 1,2.

### 3.5 Animationsvertrag (12 Animationen)

Tikos Bewegungssprache ist "Vogel-Theater": ruckartige Kopfbewegungen, stolzierende Schritte, theatralische Posen und Feder-Effekte bei jeder Emotion.

| # | Animation | Schleife | Dauer-Ziel | Posen- und Bewegungsbeschreibung |
|---|-----------|----------|------------|-----------------------------------|
| 1 | `idle` | ja | 2,4 s | Tiko **klappert mit dem Schnabel** (einmal pro Zyklus) und dreht den Kopf ruckartig nach links, dann nach rechts (Vogel-Blick). Der Feder-Schopf zuckt; ein paar Federn schweben hinter ihm. |
| 2 | `walk` | ja | 1,3 s pro Zyklus | Tiko **stolziert mit hohen, übertriebenen Schritten**: Die Knie heben sich weit, der Kopf nickt bei jedem Schritt vor und zurück, der Schnabel weist stolz nach vorn. Wirkt wie ein Paradegang. |
| 3 | `run` | ja | 0,9 s pro Zyklus | Schnelles Laufen mit halb ausgebreiteten Flügeln, der Körper neigt sich vor, der Kopf bleibt hoch. Der Feder-Schweif fliegt deutlich hinterher. |
| 4 | `punch` | nein | 0,6 s | **Schnabel-Hieb**: Tiko stößt den Kopf nach vorne, sodass der Schnabel wie ein Speer wirkt. Ein schneller, kurzer Stoß; am Ende ein Schnabel-Klack. |
| 5 | `kick` | nein | 0,7 s | Hoher Tritt mit dem Stelzenbein, fast ein Spagat-Tritt; der Körper balanciert mit ausgebreiteten Flügeln. |
| 6 | `jump` | nein | 0,9 s | Kurzer **Aufflug**: Tiko schlägt kräftig mit den Flügeln, hebt einen kurzen Moment ab (Feder-Wirbel unter ihm) und setzt wieder auf. |
| 7 | `happy` | nein | 2,0 s | Tiko fliegt kurz auf und **Federn explodieren** um ihn herum (große Partikel-Wolke, 15–20 Federn). Er landet mit ausgebreiteten Flügeln und schreit triumphierend. |
| 8 | `sad` | nein | 2,4 s | Der Schnabel hängt nach unten, die Flügel sinken, und **Federn fallen aus** (einzelne Federn rieseln zu Boden). Der Feder-Schopf liegt flach. |
| 9 | `stun` | ja | 1,9 s | Tiko sträubt alle Federn (er wirkt doppelt so groß), taumelt seitlich, der Schnabel klappert unsynchron. Kleine Sterne kreisen. |
| 10 | `carry` | ja | 0,9 s | Tiko hält einen Gegenstand **im Schnabel** (Seitengriff), die Flügel balancieren leicht. Er stolziert vorsichtig, der Kopf ist angehoben, um das Objekt zu schonen. |
| 11 | `run-carry` | ja | 1,0 s | Laufen mit Objekt im Schnabel: Tiko flattert halb, der Kopf ist nach oben gereckt, das Objekt wackelt gefährlich. |
| 12 | `victory` | nein | 3,4 s | Tiko **sitzt auf einem Stapel goldener Münzen** (Requisit-Node, 3–4 Münz-Säulen) und reckt den Schnabel triumphierend in die Höhe. Er zwitschert ein melodisches Sieges-Trillern; Gold-Münzen glitzern. |

**Audio je Animation (SFX):** `idle`: Schnabel-Klappern ("klack-klack") mit hölzernem Ton. `walk`: hohe, stolzierende Trittsounds. `punch`: scharfer Schnabel-Klack. `happy`: explodierendes Feder-Rascheln + Triumph-Schrei. `sad`: leises, einzelnes Feder-Rascheln beim Fallen. `victory`: melodisches Glissando mit Münz-Klingeln.

### 3.6 Porträt

- **`icon.png` (256×256):** Tikos Kopf mit Schnabel und Feder-Schopf, zentriert. Der Schnabel muss auch im Downscale klar erkennbar sein. Hintergrund: transparent oder helles Grün.
- **`splash.png` (1024×1024):** Tiko in stolzierender Parade-Pose (Schnabel hoch, ein Flügel akzentuiert), umgeben von ein paar schwebenden Federn, vor weichem grün-goldenem Hintergrund. Hohe Sättigung, Regenbogen-Federkleid sichtbar.
- **Identität:** Porträt und 3D-Modell zeigen dieselbe Figur — Grün `#2bffb9`, Regenbogen-Federn, übergroßer Schnabel.

### 3.7 Siegerpose

`victory` (3.5, Zeile 12): Tiko sitzt auf dem Münzstapel und reckt den Schnabel hoch. Die Kamera zeigt ihn in leichter Untersicht, die Münzen glitzern. Die Pose dauert 3,4 s und endet in der gehaltenen Sitz-End-Pose (Schnabel hoch, Flügel leicht ausgebreitet).

### 3.8 Voice & Audio (optional, budget-abhängig)

| Sample | Inhalt/Tonfall | Beschreibung |
|--------|----------------|--------------|
| `cheer` | Lautes "Kraa!" | Kräftiges, triumphales "Kraa-haa!" mit Feder-Schwung. |
| `laugh` | Melodisches Trillern | Schnelles, rollendes Trillern wie ein Vogel-Gezwitscher-Lachen. |
| `ohno` | Erschrockenes "Kraa?!" | Überraschtes, hohes "Kraa!?" mit ruckartigem Kopf. |
| `victory` | Sieges-Trillern | Langes, melodisches Trillern mit finalem "Kraa!". |
| `sad` | Leises, tiefes Gurren | Betrübtes, leises "Gurr..." mit hängendem Ende. |
| `item` | Neugieriges Trillern | "Ooh, glänzt das?" in schnell-neugierigem Zwitscher-Ton. |

Tonfall-Konvention: laut, expressiv, vogel-artig; "Kraa!" darf kräftig, aber nie schmerzhaft-schrill sein. Tiko ist ein Entertainer, kein Schreihals.

### 3.9 Heimat-Insel und Weltbezug

Tikos Heimat ist der Dschungeltempel (`world-dschungeltempel.md`). In Flavor-Texten wird er als Wächter der Tempel-Akustik gezeigt, der seine Stimme an den goldenen Hallen testet. Rein narrativer Bezug — auf dem Dschungeltempel hat er keinen Vor- oder Nachteil.

### 3.10 Strategie-Tipp (Ladebildschirm)

> "Tiko ist laut, aber clever: Er hört genau hin, wann der Sternen-Shop wandert — und plant seine Route im Kopf."

Hinweis: Der Tipp ist ein spielmechanisch neutraler Ratschlag (Sternen-Shop-Wanderung gilt für alle gleich), der Tikos Chaotik eine clevere Seite gibt.

## 4. Formulas

### 4.1 Größen-Toleranz

`1,08 ≤ H ≤ 1,32` mit Ziel `H = 1,2`. Schnabellänge `L_Schnabel ≤ 0,6` Einheiten (visuell, nicht kollidierend). Schnabel-Auskragung: `L_Schnabel / H = 0,4–0,5` (40–50 % der Höhe), damit der Schnabel dominant bleibt.

### 4.2 Farbwerte

Primärfarbe `#2bffb9` → normalisiert `(r,g,b) = (0,169; 1,000; 0,725)`.

Sekundärfarben: Schnabel `#ffb703`/`#fb8500`, Regenbogen-Verlauf (Rot→Blau), Augen `#1a2a2a`.

Farbabstand zu allen anderen Primärfarben gemäß `characters-overview.md` 4.6: alle Abstände `d ≥ 0,20` erfüllt (engster Abstand zu Bloom `#7b2ff7` mit `d ≈ 0,57`).

### 4.3 Animations-Zeitbudget

Summe der einmaligen Animationsdauern (punch + kick + jump + happy + sad + victory): `0,6 + 0,7 + 0,9 + 2,0 + 2,4 + 3,4 = 10,0 s`. Alle Werte innerhalb der Bereiche aus 3.5.

### 4.4 Feder-Partikel-Dichten

- `idle`/`walk`/`run`: 2–3 konstant schwebende Federn als Anhängsel.
- `happy`: `F_explosion ≥ 15` Feder-Partikel in einem einzigen Ausbruch.
- `sad`: `F_fall ≥ 5` Feder-Partikel, die zu Boden fallen.
- Bei deaktivierten Partikeln (Low-End) entfallen die Effekte; die Animationen bleiben vollständig lesbar.

## 5. Edge Cases

1. **Schnabel ragt in enge Passagen:** Der Schnabel kollidiert nie; er darf visuell durch Wände ragen (Toy-Look). Keine Anpassung der Trefferbox.
2. **`carry` mit Objekt im Schnabel und `freeze_animation()`:** Frieren hält das Objekt im Schnabel; beim Fortsetzen läuft die Animation weiter. Das Objekt bleibt fest im Schnabel-Griff, kein Herunterfallen.
3. **Tiko auf dem Dschungeltempel (Heimat):** Kein spielmechanischer Effekt; nur narrative Flavor-Texte und mögliche ArenaStar-Dialoge.
4. **Regenbogen-Federkleid vs. Primärfarbe im HUD:** Das HUD/Icon nutzt die Signaturfarbe Grün `#2bffb9` als Rahmen/Farbcode; der Regenbogen ist ein Modell-Detail und darf die HUD-Farbcodierung nicht verwässern.
5. **`happy`-Feder-Explosion auf schwacher Hardware:** Ist die Partikelzahl nicht darstellbar, wird sie auf die Mindestanzahl reduziert (Sektion 7), niemals auf die Animation verzichtet.
6. **Tiko im Mini-Spiel "leise sein" (falls existent):** Tikos Sounds sind Teil seiner Identität, aber die Minispiel-Logik darf niemals von Tikos Lautstärke abhängen (kein versteckter Nachteil).

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `character-tiko.md` | Art | Verwendung |
|----------------------------------|-----|------------|
| `design/gdd/characters-overview.md` | Peer | Liefert den verbindlichen Vertrag: 12 Animationen, Maße, Trefferbox, Porträt, API. |
| `design/gdd/world-dschungeltempel.md` | Peer | Liefert die Heimat-Insel, Themen und Flavor-Kontext. |
| `design/gdd/game-concept.md` | Quelle | Liefert Kern-Daten (Name, Typ, Farbe, Persönlichkeit). |
| `design/gdd/ui-character-select.md`, `design/gdd/ui-hud.md` | Peer | Verwendung von Porträt, Name und Animationen. |
| `design/gdd/audio-voice.md` | Peer | Steuerung der optionalen Voice-Lines. |
| `common/scripts/character.gd` | Code | Basisklasse, die alle Animationen ansteuert. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `plugins/characters/tiko/` (Plugin) | Die konkreten Assets müssen exakt dieser Spezifikation entsprechen. |
| `design/gdd/characters-overview.md` | Referenziert Tiko im Roster (Sektion 1) und in den Formeln (4.6). |
| Ladebildschirm | Zeigt `splash.png` und den Strategie-Tipp (3.10). |
| Siegerehrung (`victory-conditions.md`) | Löst die `victory`-Animation aus. |

### 6.3 Bidirektionalität

`characters-overview.md` verweist auf dieses Kapitel (Roster), dieses Kapitel verweist auf `characters-overview.md` (Vertrag). `world-dschungeltempel.md` muss Tiko als Bewohner erwähnen (ebenso Bloom); dieses Kapitel verweist auf die Insel. Wird Tikos Design geändert, müssen Plugin, Overview-Roster und Insel-Kapitel synchron aktualisiert werden.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Schnabellänge `L_Schnabel` | Feel | 0,4–0,7 Einheiten | 0,6 | Dominanz des Schnabels. Rein visuell; darf nie kollidieren. |
| Schnabel-Klapper-Frequenz (`idle`) | Feel | 0,5–2,0 Klapper/s | 1 Klapper/s | Aufdringlichkeit des Klapperns. |
| Kopf-Ruck-Geschwindigkeit (`idle`) | Feel | 0,2–0,6 s pro Ruck | 0,4 s | Wie ruckartig/vogelhaft der Blickwechsel wirkt. |
| Feder-Partikel `F_explosion` (`happy`) | Feel | 8–30 Partikel | 15 | Wucht der Feder-Explosion. Bei Low-End automatisch auf Minimum. |
| Feder-Schweif-Anzahl | Feel | 1–5 Federn | 3 | Anzahl der konstant schwebenden Federn. |
| `victory`-Münzstapel-Höhe | Feel | 0,5–1,5 Einheiten | 1,0 | Größe des Münzstapels; höher = prahlerischer. |

Kein Knob verändert Spielwerte; alle wirken nur auf Optik, Sound und Timing.

## 8. Acceptance Criteria

1. **Modell:** Das Plugin `plugins/characters/tiko/character.tscn` lädt in Godot 4.2 ohne Fehler; Root-Node hat `character.gd`. PASS/FAIL.
2. **Silhouette:** Tiko ist als Schattenriss von allen anderen 7 Arenians unterscheidbar (Riesen-Schnabel + aufrechte Stelzenbeine). PASS/FAIL.
3. **Farben:** Primärfarbe entspricht `#2bffb9`; Regenbogen-Federkleid und bunter Schnabel sind vorhanden und farblich korrekt. PASS/FAIL.
4. **Animationen:** Alle 12 Pflichtanimationen existieren mit den Namen aus 3.5; `play_animation("victory")` spielt die Münzstapel-Pose. PASS/FAIL.
5. **Animations-Qualität:** `idle` enthält Schnabel-Klappern + ruckartige Kopfbewegung; `happy` erfüllt `F_explosion ≥ 15`; `sad` zeigt fallende Federn; `walk` ist ein stolzierender Paradegang. PASS/FAIL.
6. **API:** `freeze_animation()` hält Tiko exakt (auch mit Objekt im Schnabel); `resume_animation()` setzt an gleicher Stelle fort. PASS/FAIL.
7. **Maße:** `1,08 ≤ H ≤ 1,32`; `L_Schnabel ≤ 0,6`; Trefferbox identisch zum Standard (`r = 0,6`, `h = 1,2`); Schnabel/Federn kollidieren nicht. PASS/FAIL.
8. **Balance:** Tikos exportierte Gameplay-Parameter sind identisch zu allen anderen Arenians. PASS/FAIL.
9. **Porträt:** `icon.png` (256×256) zeigt Schnabel + Feder-Schopf, bei 32 px erkennbar; `splash.png` (1024×1024) zeigt Tiko in Parade-Pose; beide farbidentisch zum 3D-Modell. PASS/FAIL.
10. **Siegerpose:** Simulierter Spielgewinn löst `victory` aus (3,4 s, Münzstapel, Schnabel hoch); End-Pose wird ≥ 1,0 s gehalten. PASS/FAIL.
11. **Strategie-Tipp:** Der Ladebildschirm zeigt den Satz aus 3.10. PASS/FAIL.
12. **Voice (falls aktiv):** Alle 6 Samples aus 3.8 existieren, ≤ 1,5 s, Tonfall vogel-artig/laut/melodisch. PASS/FAIL.
13. **Fehlerresistenz:** Aufruf einer nicht existierenden Animation crasht nicht, fällt auf `idle` zurück, loggt Fehler. PASS/FAIL.
