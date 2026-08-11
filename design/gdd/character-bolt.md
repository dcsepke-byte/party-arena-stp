# Bolt — Party Arena Game Bible

> **Teil:** V — Characters (5.7)
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** `design/gdd/game-concept.md`, `design/gdd/characters-overview.md`

---

## 1. Overview

Bolt ist der **Roboter** aus der Mechanik-Stadt — logisch, präzise und heimlich liebenswert. Er ist ein Spielzeug-Roboter mit sichtbaren Nieten und Zahnrädern, einem rechteckigen Kopf mit Antenne und bewusst leicht rostigen Stellen. Seine Signaturfarbe ist Blau (`#3a86ff`). Bolt bewegt sich mechanisch: klackende Schritte, vibrierendes Idle, drehende Zahnräder im Rücken. Er ist der ruhige, berechenbare Gegenpol zum Chaos der anderen Arenians — und genau das macht ihn liebenswert: Er versucht, das Unberechenbare (Würfel, Party, Freude) zu berechnen und scheitert daran auf charmante Weise. Wie alle Arenians hat er keinerlei spielmechanische Vorteile — seine Präzision ist reine Inszenierung aus Animation, Sound und Pose.

Dieses Kapitel spezifiziert Bolt vollständig: Identität, visuelles Design, alle 12 Pflichtanimationen, Porträt, Siegerpose, optionale Voice-Lines, Heimat-Bezug und Strategie-Tipp. Es ist an den Vertrag aus `characters-overview.md` gebunden.

| Kernfakt | Wert |
|----------|------|
| ID / Ordnername | `bolt` |
| Anzeigename | Bolt |
| Typ | Roboter |
| Heimat-Insel | Mechanik-Stadt |
| Persönlichkeit | logisch, präzise, liebenswert |
| Primärfarbe | Blau `#3a86ff` |
| Silhouetten-Archetyp | kantig, Antenne, Zahnrad-Rücken |
| Modellhöhe | 1,2 Einheiten (1,08–1,32) |
| Trefferbox | Zylinder oder Kapsel, Radius 0,6, Höhe 1,2 |

## 2. Player Fantasy

Bolt spielt sich wie der **netter Roboter, der alles im Griff hat — bis er es nicht hat**: Wer Bolt wählt, fühlt sich methodisch und überlegen, aber auf eine warmherzige, fast rührende Art. Er berechnet Würfelwahrscheinlichkeiten im Kopf, nickt zufrieden bei jedem logischen Zug — und freut sich dann wie ein Kind, wenn der Zufall ihn doch überrascht. Die Fantasie dahinter lautet: **"Ich habe einen Plan. Der Plan ist gut. Moment — ich hatte einen Plan."**

Design-Pillar-Bezug: **Sofort verständlich** — kantige Silhouette + Antenne + Zahnräder sagen sofort "Roboter". **Überzeichnet** — seine mechanischen Bewegungen (Vibration, klackende Schritte, Dampf bei Trauer) sind komisch übertrieben. **Interaktiv wirkend** — Zahnräder drehen, die Antenne leuchtet bei Freude und fährt bei Trauer ein: Bolt ist ein wandelndes Status-Display. **Wiedererkennbar** — Blau + Antenne + Zahnrad-Rücken sind unverwechselbar. Bolt zeigt, wie ein "rationaler" Charakter rein über Animation und Sound Charme gewinnt, ohne einen Spielwert-Vorteil zu besitzen.

## 3. Detailed Rules

### 3.1 Identität und Kernaussage

Bolt wurde in der Mechanik-Stadt (`world-mechanik-stadt.md`) als Spielzeug-Roboter gebaut — eines von vielen, aber das einzige mit einer "Persönlichkeits-Beta-Firmware". Seine Kernaussage: **"Ich analysiere das Problem. Dann analysiere ich es noch einmal. Dann handle ich — meistens."** Er nimmt die Welt ernst, aber nie sich selbst.

### 3.2 Visuelles Design

1. **Modell:** Spielzeug-Roboter im Cartoon/Toy-Stil, hohe Sättigung, klare geometrische Formen. Rechteckiger Rumpf, kugelige Gelenke, runde Füße.
2. **Kopf:** Rechteckig, mit abgerundeten Ecken; oben eine **Antenne** mit kleiner Kugelspitze, die bei Emotionen leuchtet und einfährt. Das Gesicht ist ein einfaches Display mit zwei runden Augen (`#eaf4ff`) und einem kleinen, geraden Mund (kein realistisches Gesicht).
3. **Nieten & Schrauben:** Sichtbare Nieten an den Rumpfecken und Schrauben an den Gelenken (Gold/Silber `#d4d4d4`), als spielzeugtypische Details.
4. **Zahnrad-Rücken:** Auf dem Rücken sitzen 2–3 sichtbare Zahnräder (Gold `#ffb703`), die sich in `idle` langsam drehen. Das zentrale Silhouetten-Detail von hinten.
5. **Rost:** Bewusst leicht rostige Stellen (`#a4603a`) an Rumpfunterkante und Gelenken — gewollter Toy-Charme, kein Defekt-Look.
6. **Textur:** Glänzendes, glattes Blech (hohe Sättigung, Cartoon-Schattierung). Keine realistischen Kratzer oder Dreck-Texturen.

### 3.3 Silhouette

- **Archetyp:** Kantig, rechteckig, mit aufragender **Antenne** und markantem **Zahnrad-Rücken**.
- **Erkennung:** Die Antenne ist das eindeutigste Einzelmerkmal; die kantigen, eckigen Konturen unterscheiden Bolt von allen runden Arenians. Von hinten ist der Zahnrad-Rücken unverkennbar.
- **Abgrenzung:** Anders als Brix (breit, quadratisch, aber **rundkantig-organisch** mit Felsstruktur) ist Bolt **geometrisch-präzise**: klare Kanten, symmetrische Flächen, metallischer Glanz. Brix ist massiv-organisch, Bolt ist konstruiert.

### 3.4 Standardmaße und Kollision

- Modellhöhe `H = 1,2` (Toleranz 1,08–1,32). Die Antenne darf die Obergrenze überschreiten, solange sie nicht kollidiert (Anhängsel-Regel).
- **Rumpfbreite:** `W_Rumpf ≤ 0,6` Einheiten (visuell, nicht kollidierend über die Standard-Trefferbox hinaus).
- Trefferbox identisch zum Standard: Zylinder oder Kapsel, Radius 0,6, Höhe 1,2.

### 3.5 Animationsvertrag (12 Animationen)

Bolts Bewegungssprache ist "Mechanik mit Herz": Jede Bewegung hat einen klaren Anfang, eine präzise Mitte und ein definiertes Ende. Servo-artige Rucke sind gewollt; alles wirkt berechnet, aber niemals kalt.

| # | Animation | Schleife | Dauer-Ziel | Posen- und Bewegungsbeschreibung |
|---|-----------|----------|------------|-----------------------------------|
| 1 | `idle` | ja | 2,2 s | Bolt **vibriert leicht** (feiner, gleichmäßiger Motor-Buzz); die Zahnräder am Rücken drehen langsam; der Kopf macht kleine, präzise Suchbewegungen. Gelegentlich ein kurzer "Blip". |
| 2 | `walk` | ja | 1,3 s pro Zyklus | **Mechanische Schritte** mit hörbarem "klack-klack": Die Beine heben sich in präzisem Rhythmus, die Arme pendeln wie fest eingestellte Hebel, der Oberkörper bleibt fast waagerecht. |
| 3 | `run` | ja | 0,9 s pro Zyklus | Schnelles, maschinelles Laufen: Die Schritte werden kürzer und schneller, der Oberkörper neigt sich in einem festen Winkel, die Arme pumpen wie Kolben. |
| 4 | `punch` | nein | 0,6 s | **Kolben-Schlag**: Der rechte Arm schießt wie ein Stempel nach vorn und fährt wieder ein. Ein präziser, fast geräuschloser Stoß mit einem dumpfen "Zisch" am Ende. |
| 5 | `kick` | nein | 0,7 s | Mechanischer Tritt: Das Bein fährt in einem festen Bogen aus und ein; das Hüftgelenk macht einen hörbaren "Klick". |
| 6 | `jump` | nein | 0,8 s | Bolt springt mit einem kleinen **Düsen-Stoß** an den Fußsohlen (kurzer Partikel-Blitz), bleibt in der Luft leicht steif und landet präzise auf beiden Füßen. |
| 7 | `happy` | nein | 2,0 s | Die **Antenne leuchtet** hell auf (Emissive-Puls), und Bolt macht einen kleinen **Freudentanz**: kurze, ruckartige Hüpfer mit seitlich angewinkelten Armen — wie ein programmierter Roboter-Tanz. |
| 8 | `sad` | nein | 2,4 s | Die **Antenne fährt ein** (sie sinkt in den Kopf), aus einer Rumpffuge **entweicht Dampf** (Partikel). Bolt hängt die Schultern, die Zahnräder stoppen. |
| 9 | `stun` | ja | 2,0 s | Bolt zittert stark, die Augen flackern (Display-Flackern), aus dem Rücken steigt Qualm, kleine Funken fliegen. Er taumelt seitlich. |
| 10 | `carry` | ja | 0,9 s | Bolt hält einen Gegenstand mit beiden **mechanischen Armen vor sich ausgestreckt** (als würde er eine Wertsache transportieren), die Schritte bleiben präzise. |
| 11 | `run-carry` | ja | 1,0 s | Schnelles Laufen mit ausgestreckten Armen; der Gegenstand wackelt, Bolt kompensiert mit kurzen, berechneten Schrittkorrekturen. |
| 12 | `victory` | nein | 3,0 s | Bolt **transformiert kurz in eine kleine Stern-Rakete**: Der Körper klappt zu einer Raketenform zusammen (einfache, lesbare Transformation aus 2–3 Teilen), zündet einen kleinen Partikel-Schweif und dreht eine Siegesschleife. Danach klappt er wieder in den Roboter-Stand und die Antenne leuchtet. |

**Audio je Animation (SFX):** `idle`: leiser, gleichmäßiger Motor-Buzz. `walk`/`run`: klare "klack-klack"-Metallschritte. `punch`: kurzes "Zisch" (Druckluft). `jump`: "Psst!"-Düsenstoß. `happy`: fröhliche "Blip"-Melodie. `sad`: zischender Dampf. `stun`: elektronisches Flackern + Knistern. `victory`: Raketen-Zischen + triumphale "Boop"-Fanfare.

### 3.6 Porträt

- **`icon.png` (256×256):** Bolts Kopf mit Antenne und Schulterpartie (Zahnrad-Andeutung), zentriert. Antenne und Augen müssen im Downscale erkennbar sein. Hintergrund: transparent oder helles Blau.
- **`splash.png` (1024×1024):** Bolt in stolzer Roboter-Pose (Arme verschränkt oder Sieger-Haltung), vor weichem blau-grauem Hintergrund mit dezenten Zahnrad-Elementen. Hohe Sättigung, leicht rostige Details sichtbar.
- **Identität:** Porträt und 3D-Modell zeigen dieselbe Figur — Blau `#3a86ff`, Antenne, Zahnräder, Nieten, Rost-Akzente.

### 3.7 Siegerpose

`victory` (3.5, Zeile 12): Bolt transformiert in die Stern-Rakete, fliegt eine Schleife und landet als Roboter. Die Kamera folgt der Schleife dynamisch. Die Pose dauert 3,0 s und endet in der Stand-End-Pose mit leuchtender Antenne.

### 3.8 Voice & Audio (optional, budget-abhängig)

| Sample | Inhalt/Tonfall | Beschreibung |
|--------|----------------|--------------|
| `cheer` | Bleeper-Jubel | "Boop-boop-BOOOP!" mit aufsteigender, triumphaler Melodie. |
| `laugh` | Bleeper-Kichern | Schnelle, mechanische "Boop-boop-bo-boop!"-Folge, die wie Lachen klingt. |
| `ohno` | Tiefer Bleeper | Erschrockenes "Boop...?" mit abfallendem Ton. |
| `victory` | Fanfare | Lange, siegreiche "Boop-booop-BOOOP!"-Fanfare. |
| `sad` | Leiser Bleeper | Enttäuschtes, leises "Boop..." mit hängendem Ende. |
| `item` | Neugieriger Bleeper | Fragendes "Boop-boop?" in neutral-neugierigem Ton. |

Tonfall-Konvention: synthetisch, klar, "Boop"-basiert; niemals unangenehm schrill. Bolt klingt wie ein freundlicher kleiner Rechner.

### 3.9 Heimat-Insel und Weltbezug

Bolts Heimat ist die Mechanik-Stadt (`world-mechanik-stadt.md`) — dieselbe Insel wie Brix. In Flavor-Texten wird Bolt als der "Rechner" der Stadt gezeigt, der neben Brix wohnt und dessen Tollpatschigkeit voraussagt (aber nie verhindern kann). Rein narrativer Bezug — auf der Mechanik-Stadt hat er keinen Vor- oder Nachteil.

### 3.10 Strategie-Tipp (Ladebildschirm)

> "Bolt rechnet mit: Der Glücks-Würfel hat einen größeren Erwartungswert — aber auch ein größeres Risiko. Wähle weise!"

Hinweis: Der Tipp nennt den Glücks-Würfel (Item) und dessen Erwartungswert-Eigenschaft (siehe `item-luckydice.md`); er ist spielmechanisch korrekt und für alle gleich, passt aber zu Bolts analytischer Persönlichkeit.

## 4. Formulas

### 4.1 Größen-Toleranz

`1,08 ≤ H ≤ 1,32` mit Ziel `H = 1,2`. Rumpfbreite `W_Rumpf ≤ 0,6` Einheiten (visuell, nicht kollidierend). Antennen-Überhöhe: Spitze bis `H + 0,25` erlaubt (Anhängsel-Regel).

### 4.2 Farbwerte

Primärfarbe `#3a86ff` → normalisiert `(r,g,b) = (0,227; 0,525; 1,000)`.

Sekundärfarben: Zahnräder/Nieten `#ffb703`/`#d4d4d4`, Rost `#a4603a`, Antennenlicht `#eaf4ff`.

Farbabstand zu allen anderen Primärfarben gemäß `characters-overview.md` 4.6: alle Abstände `d ≥ 0,20` erfüllt (engster Abstand zu Nixie `#00f0ff` mit `d ≈ 0,49`).

### 4.3 Animations-Zeitbudget

Summe der einmaligen Animationsdauern (punch + kick + jump + happy + sad + victory): `0,6 + 0,7 + 0,8 + 2,0 + 2,4 + 3,0 = 9,5 s`. Alle Werte innerhalb der Bereiche aus 3.5.

### 4.4 Zahnrad-Drehgeschwindigkeit

In `idle` müssen die Rücken-Zahnräder mit konstanter Winkelgeschwindigkeit `ω = 30–60 °/s` drehen (`|Δω| ≤ 5 %` über den Zyklus). In `sad` stoppen sie vollständig (`ω = 0`).

### 4.5 Antennen-Emissive

Leuchtstärke der Antenne in `happy`/`victory`: `E ≥ 0,9` (Standard-Material-Emission, 0–1). In `sad`/`stun`: `E ≤ 0,1` bzw. Flackern zwischen 0 und 0,5.

## 5. Edge Cases

1. **Antenne ragt über die Obergrenze:** Erlaubt, solange sie nicht kollidiert. Beim Einfahren (`sad`) bleibt die Trefferbox unverändert.
2. **`victory`-Transformation mitten in `freeze_animation()`:** Frieren während der Raketen-Transformation hält Bolt im Zwischenzustand (halbe Rakete). Beim Fortsetzen läuft die Transformation regulär zu Ende; ein Steckenbleiben im Zwischenzustand ist ein Fehler.
3. **Bolt auf der Mechanik-Stadt (Heimat):** Kein spielmechanischer Effekt; nur narrative Flavor-Texte. Bolt und Brix teilen die Insel, ohne sich gegenseitig zu beeinflussen.
4. **Rost-Optik als "Defekt"-Missverständnis:** Der Rost ist gewollter Toy-Charme. In Porträt und Modell muss er als stilisiertes Detail erkennbar sein, nicht als kaputtes Asset (keine realistischen Abplatzungen).
5. **Zahnräder in `stun`:** In `stun` dürfen die Zahnräder ruckeln (unsynchron), aber nicht aus dem Rücken fallen oder sich lösen (keine animierte "Zerstörung" — Bolt bleibt ein Spielzeug, kein Wrack).
6. **Tiko vs. Bolt Lärmpegel:** Bolts "klack"-Schritte und Bleeps sind Teil seiner Identität; wie bei Tiko darf Minispiel-Logik nie von der Charakter-Lautstärke abhängen (kein versteckter Vor-/Nachteil).

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `character-bolt.md` | Art | Verwendung |
|-----------------------------------|-----|------------|
| `design/gdd/characters-overview.md` | Peer | Liefert den verbindlichen Vertrag: 12 Animationen, Maße, Trefferbox, Porträt, API. |
| `design/gdd/world-mechanik-stadt.md` | Peer | Liefert die Heimat-Insel, Themen und Flavor-Kontext. |
| `design/gdd/game-concept.md` | Quelle | Liefert Kern-Daten (Name, Typ, Farbe, Persönlichkeit). |
| `design/gdd/item-luckydice.md` | Peer | Der Strategie-Tipp referenziert den Glücks-Würfel-Erwartungswert. |
| `design/gdd/ui-character-select.md`, `design/gdd/ui-hud.md` | Peer | Verwendung von Porträt, Name und Animationen. |
| `design/gdd/audio-voice.md` | Peer | Steuerung der optionalen Voice-Lines. |
| `common/scripts/character.gd` | Code | Basisklasse, die alle Animationen ansteuert. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `plugins/characters/bolt/` (Plugin) | Die konkreten Assets müssen exakt dieser Spezifikation entsprechen. |
| `design/gdd/characters-overview.md` | Referenziert Bolt im Roster (Sektion 1) und in den Formeln (4.6). |
| Ladebildschirm | Zeigt `splash.png` und den Strategie-Tipp (3.10). |
| Siegerehrung (`victory-conditions.md`) | Löst die `victory`-Animation aus. |

### 6.3 Bidirektionalität

`characters-overview.md` verweist auf dieses Kapitel (Roster), dieses Kapitel verweist auf `characters-overview.md` (Vertrag). `world-mechanik-stadt.md` muss Bolt als Bewohner erwähnen (ebenso Brix); dieses Kapitel verweist auf die Insel. Wird Bolts Design geändert, müssen Plugin, Overview-Roster und Insel-Kapitel synchron aktualisiert werden.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Zahnrad-Winkelgeschwindigkeit `ω` (`idle`) | Feel | 20–80 °/s | 45 °/s | Betriebsamkeit des Rücken-Details; schneller = aktiver, langsamer = ruhiger. |
| Vibrations-Amplitude (`idle`) | Feel | 0,1–0,5 Einheiten Versatz | 0,3 | Stärke des Motor-Buzz; größer = komischer, darf nie die Position auf dem Feld verschieben. |
| Antennen-Leuchtstärke `E` | Feel | 0–1 | 0,95 (happy) | Sichtbarkeit der Emotion; in `sad`/`stun` automatisch reduziert. |
| Schritt-"Klack"-Lautstärke | Feel | −12 bis −3 dB | −6 dB | Präsenz der Metallschritte relativ zur Musik. |
| `victory`-Raketen-Schweiflänge | Feel | 0,2–0,6 Einheiten | 0,4 | Größe des Partikel-Schweifs der Stern-Rakete. |
| Dampf-Dichte (`sad`/`stun`) | Feel | 0–5 Partikel/s | 3 Partikel/s | Menge des Dampfs/Qualms. Bei Low-End automatisch reduziert. |

Kein Knob verändert Spielwerte; alle wirken nur auf Optik, Sound und Timing.

## 8. Acceptance Criteria

1. **Modell:** Das Plugin `plugins/characters/bolt/character.tscn` lädt in Godot 4.2 ohne Fehler; Root-Node hat `character.gd`. PASS/FAIL.
2. **Silhouette:** Bolt ist als Schattenriss von allen anderen 7 Arenians unterscheidbar (kantig + Antenne + Zahnrad-Rücken). PASS/FAIL.
3. **Farben:** Primärfarbe entspricht `#3a86ff`; Zahnräder, Nieten und Rost-Akzente sind vorhanden und farblich korrekt. PASS/FAIL.
4. **Animationen:** Alle 12 Pflichtanimationen existieren mit den Namen aus 3.5; `play_animation("victory")` spielt die Raketen-Transformation. PASS/FAIL.
5. **Animations-Qualität:** `idle` zeigt Vibration + konstant drehende Zahnräder (4.4); `happy` zeigt Antennen-Leuchten + Freudentanz; `sad` zeigt eingefahrene Antenne + Dampf; `walk` erzeugt "klack"-Metallschritte. PASS/FAIL.
6. **API:** `freeze_animation()` hält Bolt exakt (auch mitten in der Transformation); `resume_animation()` setzt an gleicher Stelle fort und beendet die Transformation regulär. PASS/FAIL.
7. **Maße:** `1,08 ≤ H ≤ 1,32`; Trefferbox identisch zum Standard (`r = 0,6`, `h = 1,2`); Antenne/Zahnräder kollidieren nicht. PASS/FAIL.
8. **Balance:** Bolts exportierte Gameplay-Parameter sind identisch zu allen anderen Arenians. PASS/FAIL.
9. **Porträt:** `icon.png` (256×256) zeigt Kopf + Antenne + Zahnrad-Andeutung, bei 32 px erkennbar; `splash.png` (1024×1024) zeigt Bolt in Roboter-Siegerpose; beide farbidentisch zum 3D-Modell. PASS/FAIL.
10. **Siegerpose:** Simulierter Spielgewinn löst `victory` aus (3,0 s, Stern-Rakete + Schleife + Rück-Transformation); End-Pose wird ≥ 1,0 s gehalten. PASS/FAIL.
11. **Strategie-Tipp:** Der Ladebildschirm zeigt den Satz aus 3.10. PASS/FAIL.
12. **Voice (falls aktiv):** Alle 6 Samples aus 3.8 existieren, ≤ 1,5 s, Tonfall synthetisch/"Boop"-basiert/freundlich. PASS/FAIL.
13. **Fehlerresistenz:** Aufruf einer nicht existierenden Animation crasht nicht, fällt auf `idle` zurück, loggt Fehler. PASS/FAIL.
