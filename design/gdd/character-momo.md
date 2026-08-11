# Momo — Party Arena Game Bible

> **Teil:** V — Characters (5.9)
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** `design/gdd/game-concept.md`, `design/gdd/characters-overview.md`

---

## 1. Overview

Momo ist der **Waschbär** vom Frostgipfel — clever, trickreich und immer auf Schabernack aus. Er trägt eine übergroße "Diebes"-Maske (seine natürliche Gesichtszeichnung), einen gestreiften Schwanz und eine kleine Umhängetasche. Seine Signaturfarbe ist Pink (`#ff3cac`). Momo schleicht, plant, reibt sich die Pfoten und zwinkert verschwörerisch — er ist der Schelm der Arena, der aus jedem Zug ein kleines Manöver macht. Wie alle Arenians hat er keinerlei spielmechanische Vorteile; seine "Trickreichheit" ist reine Persönlichkeitsinszenierung aus Animation, Sound und Pose, gemappt auf dieselbe Feld-zu-Feld-Geschwindigkeit wie bei allen anderen.

Dieses Kapitel spezifiziert Momo vollständig: Identität, visuelles Design, alle 12 Pflichtanimationen, Porträt, Siegerpose, optionale Voice-Lines, Heimat-Bezug und Strategie-Tipp. Es ist an den Vertrag aus `characters-overview.md` gebunden.

| Kernfakt | Wert |
|----------|------|
| ID / Ordnername | `momo` |
| Anzeigename | Momo |
| Typ | Waschbär |
| Heimat-Insel | Frostgipfel |
| Persönlichkeit | clever, trickreich, Schabernack |
| Primärfarbe | Pink `#ff3cac` |
| Silhouetten-Archetyp | gestreifter Schwanz als Erkennungszeichen, spitze Ohren, Maske |
| Modellhöhe | 1,2 Einheiten (1,08–1,32) |
| Trefferbox | Zylinder oder Kapsel, Radius 0,6, Höhe 1,2 |

## 2. Player Fantasy

Momo spielt sich wie der **kleine Gauner mit dem großen Herzen**: Wer Momo wählt, fühlt sich einen Tick schlauer als alle anderen — und genießt es. Er schleicht durchs Spiel, als hätte er einen Plan, zwinkert bei jedem gelungenen Zug und zieht im Sieg einen Stern aus seiner Tasche, als hätte er ihn die ganze Zeit dort versteckt. Die Fantasie dahinter lautet: **"Ich gewinne nicht durch Glück. Ich gewinne durch ... nennen wir es Voraussicht."** Momos Schabernack ist dabei nie gemein — er ist der liebenswerte Trickser, der am Ende trotzdem alle mit einem Grinsen entwaffnet.

Design-Pillar-Bezug: **Sofort verständlich** — die übergroße Maske, die spitzen Ohren und der gestreifte Schwanz machen Momo sofort als "Waschbär-Dieb" lesbar. **Überzeichnet** — sein Schleichen, das Pfotenreiben und die verschwörerischen Blicke sind übertrieben theaterhaft. **Interaktiv wirkend** — seine Tasche ist ein Requisit mit Leben (er zieht Gegenstände daraus), die Maske verrutscht bei Trauer. **Wiedererkennbar** — Pink + gestreifter Schwanz + Maske: Momo ist auf jedem Bildschirm, in jedem Icon und in jeder Ecke des Boards erkennbar. Er beweist, dass ein "schlauer" Charakter rein über Performance wirkt, ohne einen Spielwert-Vorteil zu besitzen.

## 3. Detailed Rules

### 3.1 Identität und Kernaussage

Momo lebt auf dem Frostgipfel (`world-frostgipfel.md`), wo er gelernt hat, sich leise durch Schnee und Eis zu bewegen. Er sammelt glitzernde Dinge — nicht aus Gier, sondern aus purer Freude am "Entdecken". Seine Kernaussage: **"Teilen ist schön. Behalten ist schöner. Zurückgeben ist ... Verhandlungssache."** Seine Streiche sind harmlos und enden immer mit einem Zwinkern.

### 3.2 Visuelles Design

1. **Modell:** Schlanker, beweglicher Waschbär im Cartoon/Toy-Stil, hohe Sättigung. Aufrechte, leicht vorgebeugte Haltung (als würde er gleich losschleichen).
2. **Maske:** Die natürliche Gesichtszeichnung ist zu einer **übergroßen "Diebes"-Maske** stilisiert: eine kräftige, dunkel-pink/schwarze Augenbinde, die fast das ganze obere Gesicht bedeckt und an den Seiten spitz ausläuft. Darunter leuchten helle, wachsame Augen (`#ffe89b`).
3. **Schwanz:** Lang, buschig, mit **kräftigen Streifen** (abwechselnd Pink `#ff3cac` und dunkles Violett `#4a1a2a`). Der Schwanz ist das wichtigste Silhouetten-Merkmal und wird wie eine Fahne getragen.
4. **Umhängetasche:** Eine kleine, braun-pinke Tasche an einem Riemen über der Schulter, die bei `victory` den Stern enthält. Sie wippt bei Bewegung mit.
5. **Ohren:** Spitz, aufgestellt, mit hellen Innenflächen; sie können bei Emotionen anlegen (sad) oder aufstellen (happy).
6. **Textur:** Weiches, flauschiges Fell (Toy-Look, hohe Sättigung, weiche Schattierung). Klare, abgesetzte Fellflächen, keine realistischen Haarbüschel.

### 3.3 Silhouette

- **Archetyp:** Schlanker, vorgebeugter Räuber mit **gestreiftem Schwanz**, spitzen Ohren und markanter Maske.
- **Erkennung:** Der gestreifte Schwanz ist das eindeutigste Erkennungsmerkmal (auch von hinten). Die spitzen Ohren und die Masken-Kontur machen den Kopf unverwechselbar.
- **Abgrenzung:** Anders als Pip (klein, buschiger Rund-Schwanz) ist Momo größer und trägt den Schwanz **hängend mit Streifen** statt buschig-gewölbt. Anders als Koko (rund, Ohren) ist Momo schlank, spitz und vorgebeugt.

### 3.4 Standardmaße und Kollision

- Modellhöhe `H = 1,2` (Toleranz 1,08–1,32). Der Schwanz darf seitlich/hinten über die Trefferbox ragen, ohne zu kollidieren; die Ohren dürfen die Obergrenze überschreiten (Anhängsel-Regel).
- **Schwanzlänge:** `L_Schwanz ≤ 0,8` Einheiten (visuell, nicht kollidierend).
- Trefferbox identisch zum Standard: Zylinder oder Kapsel, Radius 0,6, Höhe 1,2.

### 3.5 Animationsvertrag (12 Animationen)

Momos Bewegungssprache ist "Schleichen mit Grinsen": Alles ist kontrolliert, leise und ein kleines bisschen übertrieben geheimnisvoll. Er macht nie laute, schwere Bewegungen; seine Schritte sind betont vorsichtig.

| # | Animation | Schleife | Dauer-Ziel | Posen- und Bewegungsbeschreibung |
|---|-----------|----------|------------|-----------------------------------|
| 1 | `idle` | ja | 2,6 s | Momo **putzt sich** kurz (wischt sich mit der Pfote über die Maske), dann **schaut er sich verschwörerisch um** — der Kopf dreht sich langsam nach links, dann nach rechts, die Augen verengen sich. Der Schwanz zuckt einmal pro Zyklus. |
| 2 | `walk` | ja | 1,5 s pro Zyklus | Momo **schleicht**: niedrige, vorsichtige Schritte mit aufgesetzter Sohle, der Oberkörper bleibt vorgebeugt, der Kopf wendet sich prüfend zur Seite. Die Tasche wippt leise. |
| 3 | `run` | ja | 1,0 s pro Zyklus | Schnelles, geschmeidiges Schlängeln: Momo läuft in einer leichten Zickzack-Linie, der Körper bleibt tief, der Schwanz zieht als Streifen-Fahne hinterher. |
| 4 | `punch` | nein | 0,6 s | **Schneller Pfoten-Hieb**: Momo sticht mit der Pfote blitzschnell nach vorn (wie ein kurzer Griff-Versuch) und zieht sie zurück, als hätte er etwas "geschnappt". |
| 5 | `kick` | nein | 0,7 s | Ein **Dreh-Tritt**: Momo dreht sich um 90° und tritt mit dem Hinterbein, der Schwanz peitscht als Gegengewicht mit. |
| 6 | `jump` | nein | 0,8 s | **Federnder Satz**: Momo springt mit angezogenen Beinen und gestrecktem Schwanz, in der Luft dreht er den Kopf suchend. Die Landung ist leise und bereit. |
| 7 | `happy` | nein | 2,0 s | Momo **reibt sich die Pfoten** und grinst breit (die Maske betont das Grinsen); er macht einen kleinen, hüpfenden Freudentanz, die Ohren sind aufgestellt, der Schwanz steht freudig aufgerichtet. |
| 8 | `sad` | nein | 2,4 s | Die **Maske verrutscht** (sie kippt schief), der **Schwanz hängt** schlaff herab, die Ohren legen sich an. Momo sieht aus, als hätte man ihm seinen Plan verdorben — aber immer noch niedlich. |
| 9 | `stun` | ja | 1,9 s | Momo schwankt benommen, die Augen werden zu Kreisen, der Schwanz zuckt unkontrolliert. Er greift kurz nach seiner Tasche, als wollte er sie schützen. |
| 10 | `carry` | ja | 1,0 s | Momo hält einen Gegenstand in **beiden Pfoten vor der Brust** und schleicht weiter; die Augen sind auf den Gegenstand geheftet, als wäre er ein Schatz. |
| 11 | `run-carry` | ja | 1,1 s | Schnelles Schlängeln mit Gegenstand: Momo klemmt das Objekt unter einen Arm und flitzt, der Schwanz balanciert. |
| 12 | `victory` | nein | 2,6 s | Momo **zieht einen kleinen, leuchtenden Stern aus seiner Umhängetasche** (Requisit-Node erscheint aus der Tasche), hält ihn triumphierend in die Höhe und **zwinkert** der Kamera zu. Der gestreifte Schwanz steht freudig auf. |

**Audio je Animation (SFX):** `walk`: leise, vorsichtige "Tip-tip"-Schritte (bewusst leiser als andere Charaktere). `run`: schnelles, weiches Scharren. `punch`: kurzes "Schnapp". `happy`: schnelles, zufriedenes Pfotenreiben + Kichern. `sad`: einzelner, weicher "Plopp". `victory`: funkelndes Glissando + ein "Plopp" aus der Tasche.

### 3.6 Porträt

- **`icon.png` (256×256):** Momos Kopf mit Maske, spitzen Ohren und einem Stück gestreiftem Schwanz über der Schulter, zentriert. Maske und Ohren müssen im Downscale erkennbar sein. Hintergrund: transparent oder helles Pink.
- **`splash.png` (1024×1024):** Momo in schlauer Pose (eine Pfote an der Tasche, die andere in einer "Ich-hab-einen-Plan"-Geste, Zwinkern), vor weichem pink-violettem Hintergrund mit dezenten Schnee-/Frostgipfel-Elementen. Hohe Sättigung.
- **Identität:** Porträt und 3D-Modell zeigen dieselbe Figur — Pink `#ff3cac`, Maske, spitze Ohren, Streifen-Schwanz, Umhängetasche.

### 3.7 Siegerpose

`victory` (3.5, Zeile 12): Momo zieht den Stern aus der Tasche und hält ihn hoch. Die Kamera zeigt ihn in leichter Untersicht, sein Zwinkern geht direkt in die Linse. Die Pose dauert 2,6 s und endet in der gehaltenen End-Pose (Stern in der Höhe, Schwanz aufgestellt).

### 3.8 Voice & Audio (optional, budget-abhängig)

| Sample | Inhalt/Tonfall | Beschreibung |
|--------|----------------|--------------|
| `cheer` | Verschwörerisches Kichern | "Hehe-he! Gelungen!" mit zufriedenem, leisem Kichern. |
| `laugh` | Kichern "Hehe!" | Schnelles, leises "Hehe-hehe!" — klingt wie ein gelungener Streich. |
| `ohno` | Erstauntes Kichern | Überraschtes "Oh-ho!" mit einem Hauch von "Das war NICHT mein Plan". |
| `victory` | Triumph-Kichern | Langes, zufriedenes "Hehe-hehe-he!" mit Zwinker-Ton. |
| `sad` | Leises, verlegenes Kichern | Enttäuschtes "Heh..." mit hängendem, kleinlautem Ende. |
| `item` | Neugierig-verschwörerisches Kichern | "Oh, das kommt in die Tasche." in schelmischem Ton. |

Tonfall-Konvention: leise, kichernd, schelmisch; niemals laut oder aggressiv. Momo klingt, als würde er dir gerade einen Plan verraten.

### 3.9 Heimat-Insel und Weltbezug

Momo lebt auf dem Frostgipfel (`world-frostgipfel.md`). In Flavor-Texten wird er als Sammler gezeigt, der im Schnee glitzernde Eiskristalle "findsam" aufhebt und sie gegen Lutscher oder Münzen eintauscht. Rein narrativer Bezug — auf dem Frostgipfel hat er keinen Vor- oder Nachteil.

### 3.10 Strategie-Tipp (Ladebildschirm)

> "Momo hat immer einen Plan B: Der Dieb-Handschuh holt sich, was das Glück verweigert — gut gezielt, gut gewonnen!"

Hinweis: Der Tipp nennt den Dieb-Handschuh (Item, siehe `item-thiefglove.md`) und ermuntert zu gezieltem Einsatz; er ist spielmechanisch korrekt und für alle gleich, passt aber perfekt zu Momos trickreicher Persönlichkeit.

## 4. Formulas

### 4.1 Größen-Toleranz

`1,08 ≤ H ≤ 1,32` mit Ziel `H = 1,2`. Schwanzlänge `L_Schwanz ≤ 0,8` Einheiten (visuell, nicht kollidierend). Ohren-Überhöhe bis `H + 0,15` erlaubt (Anhängsel-Regel).

### 4.2 Farbwerte

Primärfarbe `#ff3cac` → normalisiert `(r,g,b) = (1,000; 0,235; 0,675)`.

Sekundärfarben: Streifen `#4a1a2a`, Maske (dunkel) `#2a1020`, Augen `#ffe89b`, Tasche Braun-Pink `#c96a8a`.

Farbabstand zu allen anderen Primärfarben gemäß `characters-overview.md` 4.6: alle Abstände `d ≥ 0,20` erfüllt (engster Abstand zu Koko `#ff4d6d` mit `d ≈ 0,42`).

### 4.3 Animations-Zeitbudget

Summe der einmaligen Animationsdauern (punch + kick + jump + happy + sad + victory): `0,6 + 0,7 + 0,8 + 2,0 + 2,4 + 2,6 = 9,1 s`. Alle Werte innerhalb der Bereiche aus 3.5.

### 4.4 Schleichtritt-Lautstärke

Die `walk`-Trittsounds müssen im Pegel mindestens `6 dB` leiser sein als die Standard-Trittsounds der anderen Charaktere (gemessen im selben Audio-Bus, identische Quelle). Zweck: Momo "schleicht" auch akustisch. Die tatsächliche Fortbewegungszeit bleibt identisch (2,4 s/Feld).

### 4.5 Streifen-Sichtbarkeit

Der Schwanz muss mindestens `4` klar abgesetzte Streifen-Paare (Pink/Dunkel) aufweisen. Im `icon.png` bei 32 px muss mindestens ein Streifen-Muster als Hell/Dunkel-Wechsel erkennbar sein.

## 5. Edge Cases

1. **Momo "schleicht" leiser als andere:** Rein akustische Inszenierung (4.4); die Fortbewegungszeit und alle Gameplay-Parameter sind identisch. Kein versteckter Vorteil in Minispielen mit Geräusch-Aspekten — Minispiel-Logik darf nie von Charakter-Lautstärke abhängen.
2. **Maske verrutscht in `sad`:** Die Maske kippt schief, fällt aber nie vom Gesicht. Nach `sad` richtet sie sich beim Übergang zu `idle` automatisch wieder auf.
3. **`victory`-Stern aus der Tasche bei `freeze_animation()`:** Frieren hält den Moment "Stern halb aus der Tasche" exakt; `resume_animation()` führt das Herausziehen zu Ende. Der Stern darf nie im Taschen-Zwischenzustand "stecken bleiben" (nach Animationsende in den Händen, nicht in der Tasche).
4. **Momo auf dem Frostgipfel (Heimat):** Kein spielmechanischer Effekt; nur narrative Flavor-Texte.
5. **Tasche bei `run-carry`:** Trägt Momo bereits einen Gegenstand und die Tasche, darf es keine visuelle Kollision/Überschneidung geben; die Tasche bleibt geschlossen und wippt, der getragene Gegenstand wird unter dem anderen Arm gehalten.
6. **Pink vs. Koko-Rosa Verwechslung:** Momo (`#ff3cac`) und Koko (`#ff4d6d`) sind farblich nah, aber durch Silhouette (Maske/Streifen vs. Kugel/Ohren) eindeutig unterscheidbar. Der Farbabstand `d ≈ 0,42` erfüllt den Zielwert (4.2).
7. **Momo im Character-Select:** Die Auswahl-Vorschau zeigt `idle` (Putzen + verschwörerischer Blick); das Zwinkern aus `victory` ist nicht Teil der Vorschau.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `character-momo.md` | Art | Verwendung |
|-----------------------------------|-----|------------|
| `design/gdd/characters-overview.md` | Peer | Liefert den verbindlichen Vertrag: 12 Animationen, Maße, Trefferbox, Porträt, API. |
| `design/gdd/world-frostgipfel.md` | Peer | Liefert die Heimat-Insel, Themen und Flavor-Kontext. |
| `design/gdd/game-concept.md` | Quelle | Liefert Kern-Daten (Name, Typ, Farbe, Persönlichkeit). |
| `design/gdd/item-thiefglove.md` | Peer | Der Strategie-Tipp referenziert den Dieb-Handschuh. |
| `design/gdd/ui-character-select.md`, `design/gdd/ui-hud.md` | Peer | Verwendung von Porträt, Name und Animationen. |
| `design/gdd/audio-voice.md` | Peer | Steuerung der optionalen Voice-Lines. |
| `common/scripts/character.gd` | Code | Basisklasse, die alle Animationen ansteuert. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `plugins/characters/momo/` (Plugin) | Die konkreten Assets müssen exakt dieser Spezifikation entsprechen. |
| `design/gdd/characters-overview.md` | Referenziert Momo im Roster (Sektion 1) und in den Formeln (4.6). |
| Ladebildschirm | Zeigt `splash.png` und den Strategie-Tipp (3.10). |
| Siegerehrung (`victory-conditions.md`) | Löst die `victory`-Animation aus. |

### 6.3 Bidirektionalität

`characters-overview.md` verweist auf dieses Kapitel (Roster), dieses Kapitel verweist auf `characters-overview.md` (Vertrag). `world-frostgipfel.md` muss Momo als Bewohner erwähnen; dieses Kapitel verweist auf die Insel. Wird Momos Design geändert, müssen Plugin, Overview-Roster und Insel-Kapitel synchron aktualisiert werden.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Schleichtritt-Lautstärke (relativ) | Feel | −12 bis −3 dB gegenüber Standard | −6 dB | Wie leise Momo akustisch schleicht (4.4). |
| `idle`-Putzen-Intervall | Feel | 1,5–4,0 s pro Zyklus | 2,6 s | Wie oft Momo sich putzt; häufiger = eitler, seltener = wachsamer. |
| Schwanzlänge `L_Schwanz` | Feel | 0,6–0,9 Einheiten | 0,8 | Präsenz des Streifen-Schwanzes. Rein visuell; darf nie kollidieren. |
| Streifen-Anzahl | Feel | 3–6 Paare | 4 Paare | Anzahl der Streifen; mehr = detaillierter, weniger = klarer im Icon. |
| Masken-Größe | Feel | 0,8–1,2 × Kopfbreite | 1,0 × Kopfbreite | Übergröße der Diebes-Maske. Größer = dramatischer, darf die Augen nie verdecken. |
| Zickzack-Amplitude (`run`) | Feel | 0–0,3 Einheiten | 0,2 | Seitlicher Versatz der Schlängel-Linie; größer = trickreicher, kleiner = gerader. |
| `victory`-Stern-Größe | Feel | 0,2–0,5 Einheiten | 0,35 | Größe des aus der Tasche gezogenen Sterns. |

Kein Knob verändert Spielwerte; alle wirken nur auf Optik, Sound und Timing.

## 8. Acceptance Criteria

1. **Modell:** Das Plugin `plugins/characters/momo/character.tscn` lädt in Godot 4.2 ohne Fehler; Root-Node hat `character.gd`. PASS/FAIL.
2. **Silhouette:** Momo ist als Schattenriss von allen anderen 7 Arenians unterscheidbar (Maske + spitze Ohren + gestreifter Schwanz). PASS/FAIL.
3. **Farben:** Primärfarbe entspricht `#ff3cac`; Maske, Streifen-Schwanz und Umhängetasche sind vorhanden und farblich korrekt. PASS/FAIL.
4. **Animationen:** Alle 12 Pflichtanimationen existieren mit den Namen aus 3.5; `play_animation("victory")` spielt die Stern-aus-der-Tasche-Pose. PASS/FAIL.
5. **Animations-Qualität:** `walk` ist ein Schleichen mit deutlich leiseren Tritten (4.4, ≥ 6 dB Pegeldifferenz); `happy` zeigt Pfotenreiben + Grinsen; `sad` zeigt verrutschte Maske + hängenden Schwanz; `idle` zeigt Putzen + verschwörerischen Blick. PASS/FAIL.
6. **API:** `freeze_animation()` hält Momo exakt (auch mitten im Stern-Herausziehen); `resume_animation()` setzt an gleicher Stelle fort. PASS/FAIL.
7. **Maße:** `1,08 ≤ H ≤ 1,32`; Trefferbox identisch zum Standard (`r = 0,6`, `h = 1,2`); Schwanz/Ohren kollidieren nicht. PASS/FAIL.
8. **Balance:** Momos exportierte Gameplay-Parameter sind identisch zu allen anderen Arenians. PASS/FAIL.
9. **Porträt:** `icon.png` (256×256) zeigt Maske + spitze Ohren + Streifen-Schwanz, bei 32 px mit erkennbarem Streifen-Muster; `splash.png` (1024×1024) zeigt Momo in schlauer Pose; beide farbidentisch zum 3D-Modell. PASS/FAIL.
10. **Siegerpose:** Simulierter Spielgewinn löst `victory` aus (2,6 s, Stern aus der Tasche + Zwinkern); End-Pose wird ≥ 1,0 s gehalten. PASS/FAIL.
11. **Strategie-Tipp:** Der Ladebildschirm zeigt den Satz aus 3.10. PASS/FAIL.
12. **Voice (falls aktiv):** Alle 6 Samples aus 3.8 existieren, ≤ 1,5 s, Tonfall leise/kichernd/schelmisch. PASS/FAIL.
13. **Fehlerresistenz:** Aufruf einer nicht existierenden Animation crasht nicht, fällt auf `idle` zurück, loggt Fehler. PASS/FAIL.
