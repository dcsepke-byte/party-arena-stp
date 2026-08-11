# Bloom — Party Arena Game Bible

> **Teil:** V — Characters (5.8)
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** `design/gdd/game-concept.md`, `design/gdd/characters-overview.md`

---

## 1. Overview

Bloom ist der **Kaktus** aus dem Dschungeltempel (Oasen-Rand) — ruhig, humorvoll und mit Stacheln, die nur Deko sind. Er ist ein runder Kaktus mit einer Blume auf dem Kopf, zwei kurzen Armen und Stacheln aus weichem Stoff (Plüsch). Er hat kein Gesicht auf dem Kopf, sondern trägt seine Augen direkt auf dem "Körper". Seine Signaturfarbe ist Lila (`#7b2ff7`). Blooms Markenzeichen ist seine Fortbewegung: Er **rollt wie eine Kugel**, statt zu laufen — einzigartig in der Arena. Wie alle Arenians hat er keinerlei spielmechanische Vorteile; sein Rollen ist eine reine Animations-Inszenierung, gemappt auf dieselbe Feld-zu-Feld-Geschwindigkeit wie bei allen anderen.

Dieses Kapitel spezifiziert Bloom vollständig: Identität, visuelles Design, alle 12 Pflichtanimationen, Porträt, Siegerpose, optionale Voice-Lines, Heimat-Bezug und Strategie-Tipp. Es ist an den Vertrag aus `characters-overview.md` gebunden.

| Kernfakt | Wert |
|----------|------|
| ID / Ordnername | `bloom` |
| Anzeigename | Bloom |
| Typ | Kaktus |
| Heimat-Insel | Dschungeltempel (Oasen-Rand) |
| Persönlichkeit | ruhig, humorvoll, Stacheln nur Deko |
| Primärfarbe | Lila `#7b2ff7` |
| Silhouetten-Archetyp | rund mit Blumenkrone, zwei kurze Arme |
| Modellhöhe | 1,2 Einheiten (1,08–1,32) |
| Trefferbox | Zylinder oder Kapsel, Radius 0,6, Höhe 1,2 |

## 2. Player Fantasy

Bloom spielt sich wie die **ruhige, trockene Seele der Party**: Wer Bloom wählt, ist gelassen, beobachtet das Chaos der anderen mit einem humorvollen Augenzwinkern und schlägt nur gelegentlich — aber treffsicher — zu. Er ist der "Kaktus an der Bar": Er wirkt stoisch, hat aber immer einen lockeren Spruch auf Lager. Seine Blume auf dem Kopf ist sein Stimmungsbarometer: Sie öffnet sich bei Freude, welkt bei Trauer. Die Fantasie dahinter lautet: **"Ich habe keine Eile. Ihr könnt euch ruhig beeilen."**

Design-Pillar-Bezug: **Sofort verständlich** — die runde Form mit Blumenkrone und die zwei kurzen Arme sind unverwechselbar. **Überzeichnet** — Bloom **rollt** statt zu gehen, das ist die komischste Fortbewegung der Arena. **Interaktiv wirkend** — die Blume reagiert sichtbar auf jede Emotion (blüht auf, welkt, wird zum Stern). **Wiedererkennbar** — Lila + Blumenkrone + rollende Bewegung: Bloom ist auf jedem Bildschirm eindeutig. Er beweist, dass auch ein "ruhiger" Charakter durch Bewegungschoreografie maximal auffallen kann — ganz ohne Spielwert-Vorteil.

## 3. Detailed Rules

### 3.1 Identität und Kernaussage

Bloom lebt am Oasen-Rand des Dschungeltempels (`world-dschungeltempel.md`), wo die Wüste in den Dschungel übergeht. Er hat gelernt, mit wenig Wasser und viel Gelassenheit zu leben. Seine Kernaussage: **"Stacheln sind nur Deko — die Ruhe ist echt."** Er nimmt die Welt, wie sie kommt, und kommentiert sie mit trockenem Humor.

### 3.2 Visuelles Design

1. **Modell:** Runder, fast kugelförmiger Kaktus im Cartoon/Toy-Stil, hohe Sättigung. Der Körper ist eine weiche, gleichmäßige Kugel mit leicht abgeflachter Unterseite.
2. **Blume auf dem Kopf:** Eine große, freundliche Blume (ähnlich einer Gänseblümchen-/Sonnenblumen-Hybride) mit lila-rosa Blütenblättern (`#ff4d6d` bis `#7b2ff7`) und gelber Mitte (`#ffd34e`). Sie öffnet und schließt sich im `idle` und ist das zentrale Stimmungsorgan.
3. **Augen auf dem "Körper":** Bloom hat **kein Gesicht auf dem Kopf**; seine zwei großen, runden Augen (`#eae0ff` mit dunklen Pupillen) sitzen direkt auf der Kugelfläche, mittig. Dazu ein kleiner, ruhiger Mund. Die Augen können blinzeln und sich bei Emotionen verändern.
4. **Arme:** Zwei kurze, runde Arme seitlich am Körper; sie enden in kleinen, weichen "Handschuhen". Sie sind zu kurz zum Umfassen großer Dinge — was Bloom komisch macht, wenn er etwas trägt.
5. **Stacheln:** Aus **weichem Stoff (Plüsch)** — kleine, abgerundete, gekräuselte Plüsch-Stacheln, die sich bei Berührung nicht "böse" anfühlen (rein visuell, keine Kollision, keine Physik). Sie sind dezent lila-dunkler als der Körper (`#5a1fd0`).
6. **Textur:** Weiche, matte Kugeloberfläche (Toy-Look, hohe Sättigung, weiche Schattierung). Keine realistischen Kaktus-Rillen.

### 3.3 Silhouette

- **Archetyp:** Rund mit **Blumenkrone** auf dem Kopf und zwei **kurzen Armen** an den Seiten.
- **Erkennung:** Die Kugelform mit der Blume oben ist ohne Farbe eindeutig. In Bewegung (Rollen) wird die Silhouette zur rotierenden Kugel mit Blumen-Aufsatz — unverwechselbar.
- **Abgrenzung:** Anders als Koko (Kugel mit **Ohren**, stabiler Stand) hat Bloom die **Blume** als Kopf-Aufsatz und **rollt** statt zu watscheln. Anders als Nixie (Kiemen-Krone) ist Blooms Krone blütenförmig und massiv, nicht fedrig.

### 3.4 Standardmaße und Kollision

- Modellhöhe `H = 1,2` (Toleranz 1,08–1,32). Die Blume darf die Obergrenze überschreiten, solange sie nicht kollidiert (Anhängsel-Regel).
- **Körperdurchmesser:** `D_Körper ≤ 1,0` Einheiten (visuell, nicht kollidierend über die Standard-Trefferbox hinaus).
- Trefferbox identisch zum Standard: Zylinder oder Kapsel, Radius 0,6, Höhe 1,2. Beim **Rollen** bleibt die Trefferbox unverändert (die Rollbewegung ist rein animatorisch, keine Physik-Rotation).

### 3.5 Animationsvertrag (12 Animationen)

Blooms Bewegungssprache ist "Kugel mit Blume": Er wippt sanft, rollt mit fester Achse und drückt Emotionen fast ausschließlich über die Blume und die Augen aus — der Körper selbst bleibt stoisch.

| # | Animation | Schleife | Dauer-Ziel | Posen- und Bewegungsbeschreibung |
|---|-----------|----------|------------|-----------------------------------|
| 1 | `idle` | ja | 2,8 s | Bloom wippt sanft auf der Stelle; die **Blume öffnet und schließt** sich langsam (ein Öffnungs-/Schließ-Zyklus pro Animationszyklus). Die Augen blinzeln gelegentlich, der Mund bleibt ruhig. |
| 2 | `walk` | ja | 1,4 s pro Zyklus | **Bloom rollt** wie eine Kugel: Der Körper dreht sich um die seitliche Achse vorwärts (ein Rollen pro Zyklus), die Blume bleibt durch eine gegenläufige Kopfbewegung "oben" (Pendel-Optik). Die Arme werden beim Rollen eingezogen. |
| 3 | `run` | ja | 1,0 s pro Zyklus | Schnelleres Rollen: Der Körper dreht sich schneller, die Blume neigt sich in Rollrichtung leicht zurück, kleine Blätter/Staub wirbeln hinterher. |
| 4 | `punch` | nein | 0,7 s | Ein kurzer **Arm-Stups** nach vorn: Der rechte Arm stößt schnell aus und zieht sich zurück. Wirkt wie ein lässiges "Weg da" ohne jede Aggression. |
| 5 | `kick` | nein | 0,7 s | Ein **Hüpfer-Tritt**: Bloom hüpft kurz hoch und stößt in der Luft mit dem Körper nach vorn (kein Bein — er hat keins). Ein runder, komischer "Ramm"-Tritt. |
| 6 | `jump` | nein | 0,8 s | Bloom hüpft **wie ein Ball**: Der Kugelkörper hebt ab, federt weich, die Blume wackelt. Die Landung ist ein rundes Aufsetzen mit einem kleinen Nachfedern. |
| 7 | `happy` | nein | 2,2 s | Die **Blume blüht komplett auf** (maximale Öffnung, Strahlen), und es regnet **Konfetti** (Partikel) um Bloom. Die Augen werden zu fröhlichen Bögen, Bloom macht einen kleinen Hüpfer. |
| 8 | `sad` | nein | 2,6 s | Die **Blume welkt**: Die Blütenblätter hängen schlaff herab, die Blume wird **grau** (`#8a8a8a`). Bloom senkt sich leicht, die Augen werden klein und traurig. |
| 9 | `stun` | ja | 2,0 s | Bloom schwankt seitlich, kleine Blütenblätter rieseln von der Blume, die Augen werden zu Spiralen/Stirnrunzeln. Er wirkt benommen, aber stabil (er kann nicht umfallen — er ist eine Kugel). |
| 10 | `carry` | ja | 1,0 s | Bloom **rollt mit dem Gegenstand auf dem Kopf**: Der Gegenstand balanciert auf der Blume (die ihn wie eine Schale trägt), Bloom rollt besonders vorsichtig. |
| 11 | `run-carry` | ja | 1,1 s | Schnelles Rollen mit balancierendem Gegenstand: Bloom rollt schneller, der Gegenstand wackelt gefährlich, die Blume "greift" leicht mit den Blütenblättern, um ihn zu halten. |
| 12 | `victory` | nein | 2,8 s | Die **Blume verwandelt sich in einen Stern** (Blütenblätter formen sich zu einer Sternform um, gelbe Mitte leuchtet), Bloom dreht sich langsam um die eigene Achse, kleine Funken fallen. Er strahlt mit geschlossenen, glücklichen Augen. |

**Audio je Animation (SFX):** `walk`/`run`: weiches, rundes "Tock-tock"-Rollen (wie ein Ball), bei `run` schneller. `punch`: weicher "Plopp". `jump`: rundes, federndes Aufsetzen. `happy`: Konfetti-Rascheln + aufblühendes "Plopp". `sad`: welkes, leises "Seufz". `victory`: funkelndes Glissando mit weichem Glockenklang.

### 3.6 Porträt

- **`icon.png` (256×256):** Bloom als Kugel mit Blume und Augen, zentriert. Blume und Augen müssen im Downscale erkennbar sein. Hintergrund: transparent oder helles Lila.
- **`splash.png` (1024×1024):** Bloom in ruhiger, humorvoller Pose (Kugel mit leicht schräger Blume, als würde er augenzwinkern), vor weichem lila-grünem Hintergrund mit dezenten Oasen-/Kaktus-Elementen. Hohe Sättigung.
- **Identität:** Porträt und 3D-Modell zeigen dieselbe Figur — Lila `#7b2ff7`, Blumenkrone, Augen auf dem Körper, Plüsch-Stacheln.

### 3.7 Siegerpose

`victory` (3.5, Zeile 12): Die Blume verwandelt sich in einen leuchtenden Stern, Bloom dreht sich. Die Kamera zeigt ihn frontal, die Stern-Blume als krönendes Detail. Die Pose dauert 2,8 s und endet in der gehaltenen End-Pose (Stern-Blume leuchtet).

### 3.8 Voice & Audio (optional, budget-abhängig)

| Sample | Inhalt/Tonfall | Beschreibung |
|--------|----------------|--------------|
| `cheer` | Sanftes Summen | Ruhiges, warmes "Mh-hm-hm!" mit zufriedenem Summ-Ton. |
| `laugh` | Trockenes, leises Summen | Ein leises, humorvolles "Hm. Hm. Hm." — sehr trocken, sehr Bloom. |
| `ohno` | Ruhig überraschtes Summen | "Oh." in sanftem, fast gelangweiltem Ton — er regt sich nie stark auf. |
| `victory` | Langes, warmes Summen | "Mh-hmm-hmm!" mit aufsteigender, warmer Melodie. |
| `sad` | Leises, tiefes Summen | Enttäuschtes, tiefes "Mh..." mit hängendem Ende. |
| `item` | Neugierig-ruhiges Summen | "Interessant." in sanftem, nachdenklichem Ton. |

Tonfall-Konvention: ruhig, warm, trocken-humorvoll; niemals laut oder hektisch. Bloom klingt, als hätte er schon alles gesehen.

### 3.9 Heimat-Insel und Weltbezug

Blooms Heimat ist der Oasen-Rand des Dschungeltempels (`world-dschungeltempel.md`) — dieselbe Insel wie Tiko. In Flavor-Texten wird er als stiller Beobachter am Wasserloch gezeigt, der Tikos Lärm mit stoischer Ruhe erträgt. Rein narrativer Bezug — auf dem Dschungeltempel hat er keinen Vor- oder Nachteil.

### 3.10 Strategie-Tipp (Ladebildschirm)

> "Bloom rollt gelassen durchs Spiel: Wer nicht hetzt, sieht die wandernde Sternen-Statue — und kauft im richtigen Moment."

Hinweis: Der Tipp ist ein ruhiger, spielmechanisch neutraler Ratschlag (Sternen-Statue gilt für alle gleich) und passt zu Blooms gelassener Art.

## 4. Formulas

### 4.1 Größen-Toleranz

`1,08 ≤ H ≤ 1,32` mit Ziel `H = 1,2`. Körperdurchmesser `D_Körper ≤ 1,0` Einheiten (visuell, nicht kollidierend). Blumen-Überhöhe: Blütenspitze bis `H + 0,3` erlaubt (Anhängsel-Regel).

### 4.2 Farbwerte

Primärfarbe `#7b2ff7` → normalisiert `(r,g,b) = (0,482; 0,184; 0,969)`.

Sekundärfarben: Blütenblätter `#ff4d6d`→`#7b2ff7` (Verlauf), Blütenmitte `#ffd34e`, Stacheln `#5a1fd0`, welker Zustand `#8a8a8a`.

Farbabstand zu allen anderen Primärfarben gemäß `characters-overview.md` 4.6: alle Abstände `d ≥ 0,20` erfüllt (engster Abstand zu Tiko `#2bffb9` mit `d ≈ 0,57`).

### 4.3 Animations-Zeitbudget

Summe der einmaligen Animationsdauern (punch + kick + jump + happy + sad + victory): `0,7 + 0,7 + 0,8 + 2,2 + 2,6 + 2,8 = 9,8 s`. Alle Werte innerhalb der Bereiche aus 3.5.

### 4.4 Roll-Konsistenz

Die Vorwärtsbewegung der `walk`-Animation muss konstant sein (`|Δv| ≤ 5 %` über den Zyklus, gemessen an der Root-Motion-Kurve), damit das Rollen nicht "stottert". Der Körper muss pro Zyklus genau **eine volle Umdrehung** um die seitliche Achse ausführen (`θ = 360° ± 10°`), damit Rollen und Fortbewegung synchron bleiben.

### 4.5 Blumen-Zustandsmachine

Die Blume besitzt genau vier Zustände: `offen`, `geschlossen`, `geblüht` (happy), `welk` (sad/grau). Übergangsdauer zwischen den Zuständen `≤ 0,3 s`. In `stun` bleibt die Blume im zuletzt aktiven Zustand (Blätter-Rieseln optional).

## 5. Edge Cases

1. **Bloom rollt in enge Passagen:** Das Rollen ist eine Animation, keine Physik; die Trefferbox bleibt ein stehender Zylinder. Bloom passt überall hindurch wie jeder andere.
2. **Blume bleibt beim `freeze_animation()` offen:** Einfrieren hält den Blütenzustand exakt; `resume_animation()` setzt den Öffnungs-/Schließ-Zyklus fort. Kein Zustandssprung der Blume.
3. **`sad`-Welken und danach `happy`:** Die Blume muss sauber von `welk` über `geschlossen` zu `geblüht` wechseln (Zustandsmachine 4.5); sie darf nie "halb welk, halb geblüht" bleiben.
4. **Bloom auf dem Dschungeltempel (Heimat):** Kein spielmechanischer Effekt; nur narrative Flavor-Texte. Tiko und Bloom teilen die Insel ohne gegenseitige Beeinflussung.
5. **Plüsch-Stacheln als "Waffe"-Missverständnis:** Die Stacheln sind rein dekorativ (Plüsch, keine Kollision). Minigames dürfen Blooms Stacheln nie als Gameplay-Element nutzen (kein versteckter Vorteil).
6. **Rollen im Menü/Character-Select:** In der Auswahl-Vorschau läuft `idle` (nicht `walk`); die Rollbewegung ist nur auf dem Board und in Minispielen sichtbar.
7. **Blume grau in `sad` und Farbcodierung:** Der Wechsel auf Grau (`#8a8a8a`) darf die Signaturfarbe Lila im HUD/Icon nicht beeinflussen — das Icon bleibt immer lila.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `character-bloom.md` | Art | Verwendung |
|------------------------------------|-----|------------|
| `design/gdd/characters-overview.md` | Peer | Liefert den verbindlichen Vertrag: 12 Animationen, Maße, Trefferbox, Porträt, API. |
| `design/gdd/world-dschungeltempel.md` | Peer | Liefert die Heimat-Insel, Themen und Flavor-Kontext. |
| `design/gdd/game-concept.md` | Quelle | Liefert Kern-Daten (Name, Typ, Farbe, Persönlichkeit). |
| `design/gdd/ui-character-select.md`, `design/gdd/ui-hud.md` | Peer | Verwendung von Porträt, Name und Animationen. |
| `design/gdd/audio-voice.md` | Peer | Steuerung der optionalen Voice-Lines. |
| `common/scripts/character.gd` | Code | Basisklasse, die alle Animationen ansteuert. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `plugins/characters/bloom/` (Plugin) | Die konkreten Assets müssen exakt dieser Spezifikation entsprechen. |
| `design/gdd/characters-overview.md` | Referenziert Bloom im Roster (Sektion 1) und in den Formeln (4.6). |
| Ladebildschirm | Zeigt `splash.png` und den Strategie-Tipp (3.10). |
| Siegerehrung (`victory-conditions.md`) | Löst die `victory`-Animation aus. |

### 6.3 Bidirektionalität

`characters-overview.md` verweist auf dieses Kapitel (Roster), dieses Kapitel verweist auf `characters-overview.md` (Vertrag). `world-dschungeltempel.md` muss Bloom als Bewohner erwähnen (ebenso Tiko); dieses Kapitel verweist auf die Insel. Wird Blooms Design geändert, müssen Plugin, Overview-Roster und Insel-Kapitel synchron aktualisiert werden.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Blüten-Öffnungszyklus (`idle`) | Feel | 1,5–4,0 s pro Zyklus | 2,8 s | Wie oft sich die Blume öffnet/schließt; schneller = lebendiger, langsamer = stoischer. |
| Roll-Umdrehung `θ` (`walk`) | Kurve | 340–380 °/Zyklus | 360 ° | Synchronität von Optik und Fortbewegung (4.4); Abweichung > 10° ist ein sichtbarer Schlupf. |
| Roll-Konstanz | Feel | ±1 % – ±10 % | ±5 % | Gleichmäßigkeit des Rollens (4.4). |
| Körperdurchmesser `D_Körper` | Feel | 0,8–1,1 Einheiten | 1,0 | Rundlichkeit der Kugel. Rein visuell; darf nie kollidieren. |
| Konfetti-Dichte (`happy`) | Feel | 0–12 Partikel | 8 Partikel | Menge des Konfetti-Regens. Bei Low-End automatisch reduziert. |
| Welk-Grauwert (`sad`) | Feel | 40–60 % Helligkeit von Lila | `#8a8a8a` | Wie stark die Blume vergraut; weniger grau = subtiler, mehr = dramatischer. |
| `victory`-Stern-Leuchtstärke | Feel | 0,5–1,0 (Emission) | 0,9 | Glanz der Stern-Blume. |

Kein Knob verändert Spielwerte; alle wirken nur auf Optik, Sound und Timing.

## 8. Acceptance Criteria

1. **Modell:** Das Plugin `plugins/characters/bloom/character.tscn` lädt in Godot 4.2 ohne Fehler; Root-Node hat `character.gd`. PASS/FAIL.
2. **Silhouette:** Bloom ist als Schattenriss von allen anderen 7 Arenians unterscheidbar (Kugel + Blumenkrone + zwei kurze Arme). PASS/FAIL.
3. **Farben:** Primärfarbe entspricht `#7b2ff7`; Blume, Augen und Plüsch-Stacheln sind vorhanden und farblich korrekt. PASS/FAIL.
4. **Animationen:** Alle 12 Pflichtanimationen existieren mit den Namen aus 3.5; `play_animation("victory")` spielt die Stern-Blumen-Pose. PASS/FAIL.
5. **Animations-Qualität:** `walk` erfüllt Roll-Konsistenz und `θ = 360° ± 10°` (4.4); `happy` zeigt voll aufgeblühte Blume + Konfetti; `sad` zeigt welkende, graue Blume; `kick` ist der Hüpfer-Tritt ohne Bein. PASS/FAIL.
6. **API:** `freeze_animation()` hält Bloom exakt (auch mitten im Rollen/Blühen); `resume_animation()` setzt an gleicher Stelle fort. PASS/FAIL.
7. **Maße:** `1,08 ≤ H ≤ 1,32`; Trefferbox identisch zum Standard (`r = 0,6`, `h = 1,2`), bleibt beim Rollen unverändert; Blume/Stacheln kollidieren nicht. PASS/FAIL.
8. **Balance:** Blooms exportierte Gameplay-Parameter sind identisch zu allen anderen Arenians; Plüsch-Stacheln haben keine Kollision/Gameplay-Funktion. PASS/FAIL.
9. **Porträt:** `icon.png` (256×256) zeigt Kugel + Blume + Augen, bei 32 px erkennbar; `splash.png` (1024×1024) zeigt Bloom in ruhiger Pose; beide farbidentisch zum 3D-Modell (Blume im Icon immer lila, nie grau). PASS/FAIL.
10. **Siegerpose:** Simulierter Spielgewinn löst `victory` aus (2,8 s, Stern-Blume + Drehung); End-Pose wird ≥ 1,0 s gehalten. PASS/FAIL.
11. **Strategie-Tipp:** Der Ladebildschirm zeigt den Satz aus 3.10. PASS/FAIL.
12. **Voice (falls aktiv):** Alle 6 Samples aus 3.8 existieren, ≤ 1,5 s, Tonfall ruhig/warm/trocken-humorvoll. PASS/FAIL.
13. **Fehlerresistenz:** Aufruf einer nicht existierenden Animation crasht nicht, fällt auf `idle` zurück, loggt Fehler. PASS/FAIL.
