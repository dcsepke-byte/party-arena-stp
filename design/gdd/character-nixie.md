# Nixie — Party Arena Game Bible

> **Teil:** V — Characters (5.3)
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** `design/gdd/game-concept.md`, `design/gdd/characters-overview.md`

---

## 1. Overview

Nixie ist das **Axolotl** vom Sonnenstrand — neugierig, wasseraffin und verspielt. Sie ist eine schlanke, fließende Figur mit großen Feder-Kiemen-Ästen am Kopf, die wie eine Krone wirken, und einem immer vorhandenen Wassertropfen auf dem Scheitel. Ihre Signaturfarbe ist Türkis (`#00f0ff`). Nixie "schwimmt" förmlich über das Board: Ihre Fortbewegung ist ein Gleiten, als würde sie durch Wasser ziehen, statt zu laufen. Wie alle Arenians hat sie keinerlei spielmechanische Vorteile — ihre Bewegungsart ist eine reine Animation, die auf dieselbe Feld-zu-Feld-Geschwindigkeit gemappt ist wie bei jedem anderen Charakter.

Dieses Kapitel spezifiziert Nixie vollständig: Identität, visuelles Design, alle 12 Pflichtanimationen, Porträt, Siegerpose, optionale Voice-Lines, Heimat-Bezug und Strategie-Tipp. Es ist an den Vertrag aus `characters-overview.md` gebunden.

| Kernfakt | Wert |
|----------|------|
| ID / Ordnername | `nixie` |
| Anzeigename | Nixie |
| Typ | Axolotl |
| Heimat-Insel | Sonnenstrand |
| Persönlichkeit | neugierig, wasseraffin, verspielt |
| Primärfarbe | Türkis `#00f0ff` |
| Silhouetten-Archetyp | stromlinienförmig, Kiemen als Krone, Schwanzspitze |
| Modellhöhe | 1,2 Einheiten (1,08–1,32) |
| Trefferbox | Zylinder oder Kapsel, Radius 0,6, Höhe 1,2 |

## 2. Player Fantasy

Nixie spielt sich wie der **freundliche Wirbelwind aus dem Wasser**: leicht, elegant und ständig in Bewegung. Wer Nixie wählt, fühlt sich verspielt und unaufhaltsam neugierig — jede neue Insel ist eine Entdeckung, jeder Würfelwurf ein kleines Abenteuer. Ihre Bewegung ist geschmeidig wie eine Welle, ihre Kiemen wogen bei jeder Emotion, und ihr Kichern blubbert wie Unterwasser-Gelächter. Die Fantasie dahinter lautet: **"Ich gleite durch die Arena, als ob das ganze Board mein Aquarium wäre."**

Design-Pillar-Bezug: **Sofort verständlich** — die Kiemen-Krone und die stromlinienförmige Silhouette machen Nixie auf einen Blick erkennbar. **Interaktiv wirkend** — ihre Kiemen reagieren sichtbar auf Emotionen (wogen bei Freude, hängen schlaff bei Trauer), das macht sie lebendig. **Wiedererkennbar** — die Türkis-Farbe und die Gleitbewegung sind einzigartig; keine andere Figur bewegt sich so. Nixie zeigt exemplarisch, wie ein Charakter rein über Animation und Pose Persönlichkeit transportiert, ohne einen einzigen Spielwert zu verändern.

## 3. Detailed Rules

### 3.1 Identität und Kernaussage

Nixie lebt am Sonnenstrand (`world-sonnenstrand.md`), wo das Wasser flach und warm ist. Sie ist eine junge Axolotl-Forscherin: Sie will jede Lagune, jede Brandung und jede Wasserpfütze der Arena sehen. Ihre Kernaussage: **"Alles ist interessant — und wenn nicht, mache ich es interessant."** Ihre Neugier steckt an; selbst ein langweiliges Glück/Pech-Feld ist für sie ein kleines Abenteuer.

### 3.2 Visuelles Design

1. **Modell:** Schlanke, fließende Axolotl-Form im Cartoon/Toy-Stil, hohe Sättigung. Der Körper ist weich und rundlich, aber langgestreckt; die Gliedmaßen sind zierlich mit kleinen, weichen "Finger"-Spitzen.
2. **Kiemen (Feder-Kiemen):** Drei Äste pro Kopfseite, die wie Federn/Kronen nach hinten und außen stehen. Sie sind das größte Einzelmerkmal und leicht durchscheinend in Türkis mit helleren Spitzen (`#a8f8ff`).
3. **Wassertropfen:** Auf dem Scheitel sitzt permanent ein kleiner, halbtransparenter Wassertropfen (`#d0faff`), der bei Bewegung leicht mitwippt, aber nie herunterfällt (rein visuelles Anhängsel, keine Kollision).
4. **Gesicht:** Große, runde, dunkle Augen (`#1a3a4a`) mit weißen Glanzpunkten; ein breites, lächelndes Maul. Nixie sieht immer ein bisschen so aus, als hätte sie gerade etwas Spannendes entdeckt.
5. **Schwanz:** Langes, flaches Schwanzende (Schwanzflosse) mit weicher Kante, das bei Bewegung mitschwingt.
6. **Textur:** Weiche, glatte Oberfläche mit dezentem Glanz (feuchter Look), hohe Sättigung, keine realistischen Schuppen.

### 3.3 Silhouette

- **Archetyp:** Stromlinienförmig; die Kiemen bilden eine **Krone**, der Schwanz eine auslaufende **Spitze**. Nixie wirkt horizontal gestreckt, aber aufrecht.
- **Erkennung:** Kiemen-Krone + Schwanzspitze + schlanker Körper sind ohne Farbe eindeutig. Im Vergleich zu Pip (klein, buschiger Schwanz) ist Nixie größer und "wasserpflanzenhaft"; im Vergleich zu Bloom (rund, Blumenkrone) sind ihre Kronen-Elemente zart und fedrig, nicht blütenförmig.
- **Dynamik:** Die Silhouette verändert sich stark mit der Emotion (Kiemen aufgestellt vs. hängend) — das ist ein gewolltes Erkennungs- und Stimmungsmerkmal.

### 3.4 Standardmaße und Kollision

- Modellhöhe `H = 1,2` (Toleranz 1,08–1,32). Die Kiemen und der Wassertropfen dürfen die Obergrenze überschreiten, solange sie nicht kollidieren (vertikale Anhängsel-Regel aus `characters-overview.md` 3.6.4).
- Trefferbox identisch zum Standard: Zylinder oder Kapsel, Radius 0,6, Höhe 1,2. Kiemen und Schwanz erzeugen keine Kollision.

### 3.5 Animationsvertrag (12 Animationen)

Nixies Bewegungssprache ist "Wasser": alles gleitet, wellt und schwingt. Schritte gibt es nicht — ihre Füße berühren den Boden kaum. Übergänge sind weich (kein abruptes Anhalten).

| # | Animation | Schleife | Dauer-Ziel | Posen- und Bewegungsbeschreibung |
|---|-----------|----------|------------|-----------------------------------|
| 1 | `idle` | ja | 2,6 s | Nixie schwebt/schwimmt leicht auf der Stelle, der Körper macht eine sanfte Wellenbewegung. Die Kiemen wogen rhythmisch; der Wassertropfen wippt. Kleine Blubber-Blasen steigen gelegentlich auf (Partikel). |
| 2 | `walk` | ja | 1,4 s pro Zyklus | Nixie gleitet über den Boden, als würde sie schwimmen: Der Körper wellt, die Füße berühren den Boden nur als Andeutung (kein Trittsound, stattdessen ein leises, nasse "Schnitt"-Geräusch). Der Schwanz zieht hinterher. |
| 3 | `run` | ja | 1,0 s pro Zyklus | Schnelles, flaches Gleiten mit stärkerer Wellung; der Körper senkt sich leicht, der Schwanz peitscht seitlich. Wassertropfen-Spritzer hinter ihr. |
| 4 | `punch` | nein | 0,7 s | Spielerischer, weiter Hieb mit der kleinen Hand; am Abschluss spritzen ein paar Wassertropfen zur Seite. Wirkt nie aggressiv, eher wie eine spielerische "Weg-da"-Bewegung. |
| 5 | `kick` | nein | 0,8 s | Kein Bein-Tritt, sondern ein **Schwanzschlag**: Nixie dreht sich halb und peitscht den Schwanz in einer flüssigen Welle nach vorne. Wasser-Bogen-Effekt. |
| 6 | `jump` | nein | 0,9 s | Nixie gleitet in einem hohen, weichen Bogen durch die Luft, der Körper bleibt gestreckt, die Kiemen legen sich zurück. Landung fast geräuschlos (weiches Aufsetzen). |
| 7 | `happy` | nein | 2,2 s | Nixie macht einen **Salto** in der Luft und landet fröhlich; dabei erscheinen Wasserblasen-Partikel um sie herum. Die Kiemen stehen maximal auf und wogen schnell. |
| 8 | `sad` | nein | 2,6 s | Die Kiemen hängen schlaff herab, der Körper senkt sich, Nixie lässt den Kopf hängen. Der Wassertropfen rutscht sichtbar und "fällt" von ihrem Scheitel (Tropfen-Partikel); danach bildet sich ein neuer. |
| 9 | `stun` | ja | 2,0 s | Nixie zittert, die Kiemen flattern unsynchron, kleine Blubber-Blasen steigen durcheinander auf. Sie wirkt desorientiert, aber niedlich. |
| 10 | `carry` | ja | 0,9 s | Nixie hält einen Gegenstand mit beiden Armen vor der Brust und gleitet vorsichtig weiter, der Schwanz balanciert. |
| 11 | `run-carry` | ja | 1,1 s | Schnelles Gleiten mit Gegenstand; sie klemmt ihn mit einem Arm fest, der andere rudert. Der Wassertropfen wackelt gefährlich. |
| 12 | `victory` | nein | 3,2 s | Nixie **surft auf einer Welle aus Sternenstaub**: Sie steht auf einer kleinen, leuchtenden Welle (Effekt-Node mit Sternen-Partikeln), reitet eine Kurve und hebt am Ende die Arme. Die Kiemen stehen auf, sie strahlt. |

**Audio je Animation (SFX):** `idle`/`walk`: leises, weiches Wassergeräusch (Blubbern/Schnitt). `run`: schnellere Spritzer. `punch`/`kick`: "Plitsch!"-Wassereffekt. `happy`: aufsteigendes Blubber-Glissando. `sad`: einzelner fallender Tropfen (deutlich hörbar). `victory`: rauschende, funkelnde Welle.

### 3.6 Porträt

- **`icon.png` (256×256):** Nixies Kopf mit Kiemen-Krone, zentriert. Kiemen und Wassertropfen müssen im Downscale erkennbar bleiben. Hintergrund: transparent oder türkis.
- **`splash.png` (1024×1024):** Nixie in Gleit-Haltung, umgeben von dezenten Wasserblasen und Lichtreflexen, vor weichem türkis-blauem Hintergrund. Hohe Sättigung, freundlicher, neugieriger Gesichtsausdruck.
- **Identität:** Porträt und 3D-Modell zeigen dieselbe Figur — Kiemen-Krone, Wassertropfen, Türkis `#00f0ff`, gleiche Augen.

### 3.7 Siegerpose

`victory` (3.5, Zeile 12): Nixie surft auf der Sternenstaub-Welle. Die Kamera folgt der Welle seitlich (Surf-Shot), dann schwenkt sie auf Nixies jubelndes Gesicht. Die Pose dauert 3,2 s und endet in einer gehaltenen Jubel-Pose (Arme hoch, Kiemen aufgestellt).

### 3.8 Voice & Audio (optional, budget-abhängig)

| Sample | Inhalt/Tonfall | Beschreibung |
|--------|----------------|--------------|
| `cheer` | Helles Kichern/Jubeln | Schnelles, glockenhelles "Jippi!" mit Blubber-Unterton. |
| `laugh` | Blubber-Kichern | Perlendes Unterwasser-Lachen, aufsteigende Blasen hörbar. |
| `ohno` | Erstauntes Blubbern | Überraschtes "Oh!?" mit Blubber-Geräusch, eher neugierig als verzweifelt. |
| `victory` | Triumph-Kichern | Helles, langes Jubel-Kichern mit Welle. |
| `sad` | Leises Blubbern | Enttäuschtes "Oh..." mit fallendem Blubber-Ton. |
| `item` | Neugieriges Blubbern | "Was ist das?" in verspieltem, fragendem Ton. |

Tonfall-Konvention: hell, schnell, blubbernd; niemals schrill oder unangenehm. Nixie klingt immer neugierig und freundlich.

### 3.9 Heimat-Insel und Weltbezug

Nixies Heimat ist der Sonnenstrand (`world-sonnenstrand.md`). In Flavor-Texten und Einleitungen wird sie als Lagunen-Entdeckerin gezeigt, die jede Insel nach versteckten Wasserstellen absucht. Rein narrativer Bezug — auf dem Sonnenstrand hat sie keinen Vor- oder Nachteil.

### 3.10 Strategie-Tipp (Ladebildschirm)

> "Nixie liebt die Münz-Magnet-Logik: Immer schön der Nase nach — die Münzen kommen von selbst!"

Hinweis: Der Tipp nennt den Münz-Magnet (Item) und ermuntert zu einem naiven, vorderen Spielstil. Er ist spielmechanisch neutral (Item für alle gleich), aber charakteristisch neugierig.

## 4. Formulas

### 4.1 Größen-Toleranz

`1,08 ≤ H ≤ 1,32` mit Ziel `H = 1,2`. Kiemen-Spannweite: `W_Kiemen ≤ 0,9` Einheiten (rein visuell, nicht kollidierend). Der höchste Kiemenpunkt darf `H + 0,25` überschreiten (Anhängsel-Regel).

### 4.2 Farbwerte

Primärfarbe `#00f0ff` → normalisiert `(r,g,b) = (0,000; 0,941; 1,000)`.

Sekundärfarben: Kiemen-Spitzen `#a8f8ff`, Augen `#1a3a4a`, Tropfen `#d0faff`.

Farbabstand zu allen anderen Primärfarben gemäß `characters-overview.md` 4.6: Nixie ist die einzige rein "kalte" Primärfarbe; alle Abstände `d ≥ 0,20` sind erfüllt (engster Abstand besteht zu Bolt `#3a86ff` mit `d ≈ 0,49`).

### 4.3 Animations-Zeitbudget

Summe der einmaligen Animationsdauern (punch + kick + jump + happy + sad + victory): `0,7 + 0,8 + 0,9 + 2,2 + 2,6 + 3,2 = 10,4 s`. Alle Werte innerhalb der Bereiche aus 3.5.

### 4.4 Gleit-Konstanz

Die Vorwärtsbewegung der `walk`-Animation muss bei allen Phasen des Zyklus eine konstante Geschwindigkeit liefern (`|Δv| ≤ 5 %` über den Zyklus), damit das Gleiten nicht "hüpft". Gemessen über die Root-Motion-Kurve der Animation.

## 5. Edge Cases

1. **Kiemen ragen in enge Passagen:** Kiemen und Schwanz kollidieren nie; sie können visuell durch Wände "hindurchragen", ohne zu stören. Das ist akzeptiert (Toy-Look), solange keine Kollision entsteht.
2. **`sad`-Tropfen-Neubildung:** Nach dem fallenden Tropfen muss sich ein neuer Wassertropfen auf dem Scheitel bilden, bevor `idle` wieder startet. Fehlt der Neubildungs-Frame, ist die Animation fehlerhaft.
3. **Nixie im Trockenen (Frostgipfel, Mechanik-Stadt):** Ihre Gleitbewegung und Blubber-Sounds sind auf allen Inseln identisch; kein thematischer Wechsel. Das ist gewollt (Konsistenz), keine Anpassung an die Insel nötig.
4. **`freeze_animation()` während des Salto (`happy`):** Die Pose friert in der Luft ein; `resume_animation()` setzt den Salto fort und beendet ihn regulär. Nixie darf nach dem Fortsetzen nie "in der Luft schwebend" stecken bleiben — das Board-System setzt sie nach Abschluss auf das Feld.
5. **Gleiten ohne Tritt-Sounds:** Fehlende Fuß-Sounds sind gewollt; es dürfen keine generischen Tritt-Sounds der anderen Charaktere zugespielt werden.
6. **Wassertropfen-Partikel bei deaktivierten Partikeln (Low-End):** Die Tropfen-/Blubber-Partikel sind optional; ohne sie muss die Figur vollständig funktional bleiben (nur Optik entfällt).

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `character-nixie.md` | Art | Verwendung |
|------------------------------------|-----|------------|
| `design/gdd/characters-overview.md` | Peer | Liefert den verbindlichen Vertrag: 12 Animationen, Maße, Trefferbox, Porträt, API. |
| `design/gdd/world-sonnenstrand.md` | Peer | Liefert die Heimat-Insel, Themen und Flavor-Kontext. |
| `design/gdd/game-concept.md` | Quelle | Liefert Kern-Daten (Name, Typ, Farbe, Persönlichkeit). |
| `design/gdd/ui-character-select.md`, `design/gdd/ui-hud.md` | Peer | Verwendung von Porträt, Name und Animationen. |
| `design/gdd/audio-voice.md` | Peer | Steuerung der optionalen Voice-Lines. |
| `common/scripts/character.gd` | Code | Basisklasse, die alle Animationen ansteuert. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `plugins/characters/nixie/` (Plugin) | Die konkreten Assets (Modell, Texturen, Animationen, Porträts, Voice) müssen exakt dieser Spezifikation entsprechen. |
| `design/gdd/characters-overview.md` | Referenziert Nixie im Roster (Sektion 1) und in den Formeln (4.6). |
| Ladebildschirm | Zeigt `splash.png` und den Strategie-Tipp (3.10). |
| Siegerehrung (`victory-conditions.md`) | Löst die `victory`-Animation aus. |

### 6.3 Bidirektionalität

`characters-overview.md` verweist auf dieses Kapitel (Roster), dieses Kapitel verweist auf `characters-overview.md` (Vertrag). `world-sonnenstrand.md` muss Nixie als Bewohnerin erwähnen; dieses Kapitel verweist auf die Insel. Wird Nixies Design geändert, müssen Plugin, Overview-Roster und Insel-Kapitel synchron aktualisiert werden.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Kiemen-Wog-Geschwindigkeit in `idle` | Feel | 1,5–4,0 s pro Wog-Zyklus | 2,6 s | Lebendigkeit der Wartepose; schneller = unruhiger, langsamer = ruhiger/elegant. |
| Blubber-Partikeldichte | Feel | 0–5 Partikel/s | 2 Partikel/s | Menge der aufsteigenden Blasen in `idle`. Nur Optik; bei 0 keine Partikel. |
| Kiemen-Spannweite `W_Kiemen` | Feel | 0,6–0,9 Einheiten | 0,8 | Größe der Kiemen-Krone. Rein visuell; größer = präsenter, darf nie kollidieren. |
| `walk`-Gleit-Konstanz | Feel | ±1 % – ±10 % Geschw.-Schwankung | ±5 % | Wie gleichmäßig das Gleiten wirkt (4.4). |
| `victory`-Wellenhöhe | Feel | 0,3–0,8 Einheiten | 0,5 | Höhe der Sternenstaub-Welle; höher = dramatischer Surf-Moment. |
| Wasser-Sound-Lautstärke | Feel | −12 bis −3 dB | −6 dB | Präsenz der Wasser-SFX relativ zur Musik. |

Kein Knob verändert Spielwerte; alle wirken nur auf Optik, Sound und Timing.

## 8. Acceptance Criteria

1. **Modell:** Das Plugin `plugins/characters/nixie/character.tscn` lädt in Godot 4.2 ohne Fehler; Root-Node hat `character.gd`. PASS/FAIL.
2. **Silhouette:** Nixie ist als Schattenriss von allen anderen 7 Arenians unterscheidbar (Kiemen-Krone + Schwanzspitze + Wassertropfen). PASS/FAIL.
3. **Farben:** Primärfarbe entspricht `#00f0ff`; Kiemen, Wassertropfen und Augen sind vorhanden und farblich korrekt. PASS/FAIL.
4. **Animationen:** Alle 12 Pflichtanimationen existieren mit den Namen aus 3.5; `play_animation("victory")` spielt die Surf-Pose. PASS/FAIL.
5. **Animations-Qualität:** `walk` ist ein konstantes Gleiten (4.4), kein Hüpfen; `happy` enthält den Salto mit Blasen; `sad` zeigt hängende Kiemen und den fallenden Tropfen mit Neubildung. PASS/FAIL.
6. **API:** `freeze_animation()` hält Nixie exakt (auch mitten im Salto); `resume_animation()` setzt an gleicher Stelle fort. PASS/FAIL.
7. **Maße:** `1,08 ≤ H ≤ 1,32`; Trefferbox Zylinder/Kapsel `r = 0,6`, `h = 1,2`, identisch zum Standard; Kiemen/Tropfen kollidieren nicht. PASS/FAIL.
8. **Balance:** Nixies exportierte Gameplay-Parameter sind identisch zu allen anderen Arenians. PASS/FAIL.
9. **Porträt:** `icon.png` (256×256) zeigt Kiemen-Krone + Tropfen, bei 32 px erkennbar; `splash.png` (1024×1024) zeigt Nixie in Gleit-Haltung; beide farbidentisch zum 3D-Modell. PASS/FAIL.
10. **Siegerpose:** Simulierter Spielgewinn löst `victory` aus (3,2 s, Sternenstaub-Welle, Kamera-Seitenschwenk); End-Pose wird ≥ 1,0 s gehalten. PASS/FAIL.
11. **Strategie-Tipp:** Der Ladebildschirm zeigt den Satz aus 3.10. PASS/FAIL.
12. **Voice (falls aktiv):** Alle 6 Samples aus 3.8 existieren, ≤ 1,5 s, Tonfall hell/blubbernd/freundlich. PASS/FAIL.
13. **Fehlerresistenz:** Aufruf einer nicht existierenden Animation crasht nicht, fällt auf `idle` zurück, loggt Fehler. PASS/FAIL.
