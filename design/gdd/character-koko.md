# Koko — Party Arena Game Bible

> **Teil:** V — Characters (5.5)
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** `design/gdd/game-concept.md`, `design/gdd/characters-overview.md`

---

## 1. Overview

Koko ist der **Panda** aus dem Zuckerwald — freundlich, stark und gemütlich. Statt des klassischen Schwarz-Weiß trägt sie rosa Akzente: ein rundlicher Körper mit rosa Ohren, Pfoten und Augenpartie, dazu ein Zuckerstangen-Muster auf dem Bauch. Ihre Signaturfarbe ist Rosa (`#ff4d6d`). Koko watschelt bedächtig, reibt sich beim Warten den Bauch und umarmt zum Sieg einen riesigen Lutscher. Sie verkörpert Wärme und Gemütlichkeit, aber auch eine ruhige, unterschwellige Stärke. Wie alle Arenians hat sie keinerlei spielmechanische Vorteile — ihr "starker" Eindruck ist reine Inszenierung, und ihre Watschel-Bewegung ist exakt auf dieselbe Feld-zu-Feld-Geschwindigkeit gemappt wie bei allen anderen.

Dieses Kapitel spezifiziert Koko vollständig: Identität, visuelles Design, alle 12 Pflichtanimationen, Porträt, Siegerpose, optionale Voice-Lines, Heimat-Bezug und Strategie-Tipp. Es ist an den Vertrag aus `characters-overview.md` gebunden.

| Kernfakt | Wert |
|----------|------|
| ID / Ordnername | `koko` |
| Anzeigename | Koko |
| Typ | Panda |
| Heimat-Insel | Zuckerwald |
| Persönlichkeit | freundlich, stark, gemütlich |
| Primärfarbe | Rosa `#ff4d6d` |
| Silhouetten-Archetyp | rund, kugelig, große Ohren |
| Modellhöhe | 1,2 Einheiten (1,08–1,32) |
| Trefferbox | Zylinder oder Kapsel, Radius 0,6, Höhe 1,2 |

## 2. Player Fantasy

Koko spielt sich wie die **kuschelige Ruhe in der Party**: Wer Koko wählt, fühlt sich warm, zufrieden und ein bisschen unverwüstlich. Sie wirkt nie hektisch — selbst wenn sie rennt, ist es ein gemütliches, tapsendes Rollen. Gleichzeitig strahlt sie eine sanfte Stärke aus: Sie ist diejenige, die am Ende des Tages alle umarmt, egal ob Sieg oder Niederlage. Die Fantasie dahinter lautet: **"Ich bin hier, um Spaß zu haben — und ich habe die Geduld, das durchzustehen."**

Design-Pillar-Bezug: **Sofort verständlich** — der kugelige Körper und die runden Ohren machen Koko auf einen Blick lesbar. **Überzeichnet** — ihr Watscheln und das gähnende, bauchreibende Idle sind komisch übertrieben. **Interaktiv wirkend** — ihre Emotionen sind körperlich (Bauch reiben, Pfoten klatschen, Gesicht verstecken). **Wiedererkennbar** — Rosa + rund + Zuckerstangen-Bauch: Koko ist im HUD, im Icon und auf dem Board unverwechselbar. Sie zeigt, wie "Gemütlichkeit" als spielerisches Gefühl transportiert wird, ohne einen einzigen Spielwert zu verändern.

## 3. Detailed Rules

### 3.1 Identität und Kernaussage

Koko lebt im Zuckerwald (`world-zuckerwald.md`), wo die Bäume aus Bonbons wachsen und die Wege aus Schokolade sind. Sie ist dort aufgewachsen und hat eine tiefe, unerschütterliche Ruhe entwickelt. Ihre Kernaussage: **"Alles wird gut — und wenn nicht, gibt es Lutscher."** Ihre Stärke ist nicht aggressiv, sondern beschützend und herzlich.

### 3.2 Visuelles Design

1. **Modell:** Rundlicher Panda im Cartoon/Toy-Stil, hohe Sättigung. Der Körper ist eine weiche, fast kugelige Masse; Arme und Beine sind kurz und plüschig. Keine scharfen Kanten.
2. **Farbgebung (statt Schwarz-Weiß):** Der Körper ist warmes Creme/Weiß (`#fff5e6`) mit kräftigen **rosa Akzenten** (`#ff4d6d`) an Ohren-Innenflächen, Pfoten, Augenpartie und Füßen. Der Bauch trägt das Zuckerstangen-Muster.
3. **Zuckerstangen-Muster:** Auf dem Bauch verläuft ein diagonales Rot-Weiß-Rosa-Streifenmuster, das an eine Zuckerstange erinnert. Es ist das wichtigste Detail für die Wiedererkennung aus der Nähe.
4. **Gesicht:** Freundliche, große Augen (`#2a1a2a` mit Glanzpunkten) in rosa Augenpartie; eine kleine runde Nase; ein sanftes, breites Lächeln. Immer ein leicht geröteter "Kuschel"-Wangenfleck.
5. **Ohren:** Groß, rund, plüschig — von hinten deutlich sichtbar und ein zentrales Silhouetten-Element.
6. **Textur:** Weiches, plüschiges Fell (Toy-Look, hohe Sättigung, weiche Schattierung).

### 3.3 Silhouette

- **Archetyp:** Rund, kugelig, große Ohren. Koko ist die rundeste Silhouette der Arena — eine Kugel auf kurzen Beinen mit zwei runden Ohren oben.
- **Erkennung:** Auch ohne Farbe ist die Kugelform mit den seitlich abstehenden runden Ohren eindeutig. Der Bauch wölbt sich vor; die Arme sind kurz und hängen seitlich.
- **Abgrenzung:** Anders als Bloom (rund mit Blumenkrone und zwei Armen) hat Koko **Ohren statt Blume** und einen kompakteren, stabileren Stand. Anders als Brix (breit-quadratisch) ist Koko rein rund ohne jede Kante.

### 3.4 Standardmaße und Kollision

- Modellhöhe `H = 1,2` (Toleranz 1,08–1,32). Die Ohren dürfen die Obergrenze überschreiten, solange sie nicht kollidieren.
- **Körperdurchmesser:** `D_Körper ≤ 1,0` Einheiten (visuell rundlich, nicht kollidierend über die Standard-Trefferbox hinaus).
- Trefferbox identisch zum Standard: Zylinder oder Kapsel, Radius 0,6, Höhe 1,2.

### 3.5 Animationsvertrag (12 Animationen)

Kokos Bewegungssprache ist "Gemütlich mit Gewicht": Alles ist weich, rund und ein kleines bisschen langsam — aber niemals träge. Übergänge sind sanft; es gibt keine abrupten Bewegungen.

| # | Animation | Schleife | Dauer-Ziel | Posen- und Bewegungsbeschreibung |
|---|-----------|----------|------------|-----------------------------------|
| 1 | `idle` | ja | 3,0 s | Koko reibt sich zufrieden den Bauch und gähnt dann herzhaft (einmal pro Zyklus). Die Ohren wackeln beim Gähnen leicht. Sie steht locker, das Gewicht auf beiden Beinen. |
| 2 | `walk` | ja | 1,6 s pro Zyklus | Gemächliches Watscheln: Koko schaukelt von einer Seite zur anderen, die Arme halten leicht ab, der Bauch wippt mit. Jeder Schritt ist ein weiches, rundes Aufsetzen. |
| 3 | `run` | ja | 1,1 s pro Zyklus | Tapsendes Rollen-Watscheln: Koko bewegt sich schneller, der Körper neigt sich leicht vor, die Arme pumpen kurz und rundlich. Es wirkt wie ein eiliges Watscheln, nie wie ein Sprint. |
| 4 | `punch` | nein | 0,8 s | Runder, freundlicher Hieb mit der plüschigen Pfote; die Bewegung ist ein weicher Bogen, kein harter Schlag. Am Ende federt der Arm zurück. |
| 5 | `kick` | nein | 0,8 s | Gemütlicher, runder Tritt mit dem kurzen Bein; der Körper dreht sich leicht mit. Wirkt wie ein "Weg-da" mit Samtpfote. |
| 6 | `jump` | nein | 0,9 s | Koko hüpft: Der runde Körper hebt sich als Ganzes, in der Luft wackeln Ohren und Bauch nach, die Landung ist weich und federt einmal nach. |
| 7 | `happy` | nein | 2,2 s | Koko **klatscht in die Pfoten** und hüpft auf der Stelle; dabei regnen kleine Bonbons um sie herum (Partikel). Sie strahlt mit geschlossenen, glücklichen Augen. |
| 8 | `sad` | nein | 2,8 s | Koko **setzt sich hin** (ihre kurzen Beine verschwinden unter dem Bauch) und versteckt ihr Gesicht hinter beiden Pfoten. Die Ohren sinken seitlich herab. |
| 9 | `stun` | ja | 2,0 s | Koko taumelt weich vor und zurück, der Bauch wackelt, kleine Sternchen kreisen über dem Kopf. Sie wirkt benommen, aber niemals panisch. |
| 10 | `carry` | ja | 1,0 s | Koko hält einen Gegenstand mit beiden Pfoten **vor dem Bauch**, direkt auf dem Zuckerstangen-Muster. Sie watschelt besonders vorsichtig. |
| 11 | `run-carry` | ja | 1,2 s | Watschel-Tempo mit Gegenstand: Koko klemmt das Objekt an den Bauch, eine Pfote oben, und eilt so schnell sie kann — was immer noch gemütlich wirkt. |
| 12 | `victory` | nein | 3,0 s | Koko **umarmt einen riesigen Lutscher** (Requisit-Node, etwa 1,8 Einheiten groß): Sie drückt ihn an sich, schaukelt glücklich hin und her, die Augen sind geschlossen vor Freude. Kleine Zuckerstaub-Partikel. |

**Audio je Animation (SFX):** `idle`: weiches, zufriedenes Brummen beim Bauchreiben; Gähnen mit rundem, warmem Ton. `walk`/`run`: leise, weiche "Tapp"-Geräusche (dumpf, plüschig). `punch`/`kick`: weicher "Puff"-Ton. `happy`: Bonbon-Regen-Klingeln + Händeklatschen. `victory`: warmes, rundes Glissando mit Zuckerstaub-Rauschen.

### 3.6 Porträt

- **`icon.png` (256×256):** Kokos Gesicht mit Ohren und Zuckerstangen-Bauch-Ausschnitt, zentriert. Rosa Augenpartie und Ohren müssen im Downscale erkennbar sein. Hintergrund: transparent oder helles Rosa.
- **`splash.png` (1024×1024):** Koko in freundlicher Sitz-Haltung (oder mit Lutscher), vor weichem rosa-cremefarbenem Hintergrund mit dezenten Bonbon-Elementen. Hohe Sättigung, warmes Lächeln.
- **Identität:** Porträt und 3D-Modell zeigen dieselbe Figur — Rosa `#ff4d6d`, runde Ohren, Zuckerstangen-Muster, Creme-Körper.

### 3.7 Siegerpose

`victory` (3.5, Zeile 12): Koko umarmt den riesigen Lutscher. Die Kamera zeigt sie in leichter Untersicht (Hero-Shot), der Lutscher ragt über den Bildrand. Die Pose dauert 3,0 s und endet in der gehaltenen Umarmungs-End-Pose.

### 3.8 Voice & Audio (optional, budget-abhängig)

| Sample | Inhalt/Tonfall | Beschreibung |
|--------|----------------|--------------|
| `cheer` | Zufriedenes Jubeln | Warmes, rundes "Juhu!" mit zufriedenem Brummen am Ende. |
| `laugh` | Tiefes, zufriedenes Brummen | Ruhiges, warmherziges "Hm-hm-hm", wie ein glückliches Brummbär-Lachen. |
| `ohno` | Sanft erschrockenes Brummen | Überraschtes "Oh!" in warmem, tiefem Ton — nie schrill. |
| `victory` | Glückliches Jubeln | Langes, warmes "Juhuu!" mit Kuschel-Unterton. |
| `sad` | Leises, verlegenes Brummen | Enttäuschtes "Oh... " mit hängendem, weichem Ende. |
| `item` | Neugierig-zufriedenes Brummen | "Mmm, was haben wir denn da?" in freundlichem, neugierigem Ton. |

Tonfall-Konvention: tief, warm, rund, langsam; niemals schrill oder hektisch. Koko klingt wie eine Umarmung.

### 3.9 Heimat-Insel und Weltbezug

Kokos Heimat ist der Zuckerwald (`world-zuckerwald.md`). In Flavor-Texten wird sie als Hüterin der Zuckerstangen-Bäume gezeigt, die jeden Besucher mit einem Lutscher begrüßt. Rein narrativer Bezug — auf dem Zuckerwald hat sie keinen Vor- oder Nachteil.

### 3.10 Strategie-Tipp (Ladebildschirm)

> "Koko nimmt sich Zeit: Wer auf dem Ereignis-Feld ruhig bleibt, behält den Überblick über alle anderen."

Hinweis: Der Tipp ist ein ruhiger, spielmechanisch neutraler Ratschlag (Ereignis-Feld gilt für alle gleich) und passt zu Kokos gelassener Persönlichkeit.

## 4. Formulas

### 4.1 Größen-Toleranz

`1,08 ≤ H ≤ 1,32` mit Ziel `H = 1,2`. Körperdurchmesser `D_Körper ≤ 1,0` Einheiten (visuell, nicht kollidierend). Ohren dürfen `H + 0,2` überschreiten (Anhängsel-Regel).

### 4.2 Farbwerte

Primärfarbe `#ff4d6d` → normalisiert `(r,g,b) = (1,000; 0,302; 0,427)`.

Sekundärfarben: Körper-Creme `#fff5e6`, Augen `#2a1a2a`, Lutscher-Requisit Rot-Weiß `#ff4d6d`/`#ffffff`.

Farbabstand zu allen anderen Primärfarben gemäß `characters-overview.md` 4.6: engster Abstand zu Brix (`#ff6a00`) mit `d ≈ 0,26` (das engste Paar des Roster); Ziel `d ≥ 0,20` erfüllt.

### 4.3 Animations-Zeitbudget

Summe der einmaligen Animationsdauern (punch + kick + jump + happy + sad + victory): `0,8 + 0,8 + 0,9 + 2,2 + 2,8 + 3,0 = 10,5 s`. Alle Werte innerhalb der Bereiche aus 3.5.

### 4.4 Watschel-Rundheit

Der horizontale Versatz des Oberkörpers in `walk` muss eine glatte Sinus-ähnliche Kurve beschreiben (`R² ≥ 0,9` bei Kurvenanpassung), damit das Watscheln weich und nicht eckig wirkt. Gemessen über die Root-/Hüft-Bewegung der Animation.

## 5. Edge Cases

1. **Koko wirkt "langsamer" als andere:** Die Watschel-Animation ist auf dieselbe Fortbewegungszeit (2,4 s/Feld) gemappt wie bei allen Charakteren. Es ist ein dokumentierter optischer Effekt, dass Koko trotz identischer Geschwindigkeit gemütlicher wirkt — kein Gameplay-Unterschied.
2. **`sad` im Sitzen (kurze Beine verschwinden):** Beim Setzen muss die Trefferbox unverändert bleiben (Standard), auch wenn das Modell niedriger wirkt. Die Trefferbox wird nie an die Sitz-Pose angepasst.
3. **Lutscher-Requisit in `victory` bei deaktivierten Partikeln:** Der Lutscher ist ein Node, kein Partikel; der Zuckerstaub entfällt, der Lutscher bleibt.
4. **Zuckerstangen-Muster im Icon:** Das Muster muss auch im 32-px-Icon als diagonale Streifung erkennbar sein (kein Weichzeichnen). Ist es nicht erkennbar, wird es durch Ohren + Rosa-Farbe kompensiert.
5. **Koko auf dem Zuckerwald (Heimat):** Kein spielmechanischer Effekt; nur narrative Flavor-Texte und mögliche ArenaStar-Dialoge.
6. **`happy`-Bonbon-Regen bei Low-End-Geräten:** Der Bonbon-Regen ist optional; ohne Partikel bleibt das Pfotenklatschen als Jubel eindeutig erkennbar.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `character-koko.md` | Art | Verwendung |
|----------------------------------|-----|------------|
| `design/gdd/characters-overview.md` | Peer | Liefert den verbindlichen Vertrag: 12 Animationen, Maße, Trefferbox, Porträt, API. |
| `design/gdd/world-zuckerwald.md` | Peer | Liefert die Heimat-Insel, Themen und Flavor-Kontext. |
| `design/gdd/game-concept.md` | Quelle | Liefert Kern-Daten (Name, Typ, Farbe, Persönlichkeit). |
| `design/gdd/ui-character-select.md`, `design/gdd/ui-hud.md` | Peer | Verwendung von Porträt, Name und Animationen. |
| `design/gdd/audio-voice.md` | Peer | Steuerung der optionalen Voice-Lines. |
| `common/scripts/character.gd` | Code | Basisklasse, die alle Animationen ansteuert. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `plugins/characters/koko/` (Plugin) | Die konkreten Assets müssen exakt dieser Spezifikation entsprechen. |
| `design/gdd/characters-overview.md` | Referenziert Koko im Roster (Sektion 1) und in den Formeln (4.6). |
| Ladebildschirm | Zeigt `splash.png` und den Strategie-Tipp (3.10). |
| Siegerehrung (`victory-conditions.md`) | Löst die `victory`-Animation aus. |

### 6.3 Bidirektionalität

`characters-overview.md` verweist auf dieses Kapitel (Roster), dieses Kapitel verweist auf `characters-overview.md` (Vertrag). `world-zuckerwald.md` muss Koko als Bewohnerin erwähnen; dieses Kapitel verweist auf die Insel. Wird Kokos Design geändert, müssen Plugin, Overview-Roster und Insel-Kapitel synchron aktualisiert werden.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| `idle`-Gähn-Intervall | Feel | 2,0–5,0 s pro Zyklus | 3,0 s | Wie oft Koko gähnt; häufiger = verschlafener, seltener = wacher. |
| Körperdurchmesser `D_Körper` | Feel | 0,8–1,1 Einheiten | 1,0 | Rundlichkeit der Silhouette. Rein visuell; darf nie kollidieren. |
| Watschel-Amplitude | Feel | 0,1–0,3 Einheiten | 0,2 | Seitlicher Schaukel-Versatz in `walk`. Größer = watscheliger, kleiner = kontrollierter. |
| Watschel-Rundheit `R²` | Feel | 0,85–1,0 | 0,9 | Weichheit der Schaukelkurve (4.4). |
| Bonbon-Regen-Dichte (`happy`) | Feel | 0–10 Partikel | 6 Partikel | Menge der Bonbons. Nur Optik. |
| `victory`-Lutscher-Größe | Feel | 1,4–2,2 Einheiten | 1,8 | Größe des Lutscher-Requisits; größer = comic-hafter. |

Kein Knob verändert Spielwerte; alle wirken nur auf Optik, Sound und Timing.

## 8. Acceptance Criteria

1. **Modell:** Das Plugin `plugins/characters/koko/character.tscn` lädt in Godot 4.2 ohne Fehler; Root-Node hat `character.gd`. PASS/FAIL.
2. **Silhouette:** Koko ist als Schattenriss von allen anderen 7 Arenians unterscheidbar (Kugel + runde Ohren). PASS/FAIL.
3. **Farben:** Primärfarbe entspricht `#ff4d6d`; Creme-Körper, rosa Akzente und Zuckerstangen-Muster sind vorhanden und farblich korrekt. PASS/FAIL.
4. **Animationen:** Alle 12 Pflichtanimationen existieren mit den Namen aus 3.5; `play_animation("victory")` spielt die Lutscher-Umarmung. PASS/FAIL.
5. **Animations-Qualität:** `walk` erfüllt die Watschel-Rundheit (4.4); `happy` enthält Pfotenklatschen + Bonbon-Regen; `sad` zeigt das Hinsetzen mit verstecktem Gesicht. PASS/FAIL.
6. **API:** `freeze_animation()` hält Koko exakt; `resume_animation()` setzt an gleicher Stelle fort. PASS/FAIL.
7. **Maße:** `1,08 ≤ H ≤ 1,32`; Trefferbox identisch zum Standard (`r = 0,6`, `h = 1,2`), bleibt auch in der Sitz-Pose unverändert. PASS/FAIL.
8. **Balance:** Kokos exportierte Gameplay-Parameter sind identisch zu allen anderen Arenians. PASS/FAIL.
9. **Porträt:** `icon.png` (256×256) zeigt Ohren + Zuckerstangen-Bauch, bei 32 px erkennbar; `splash.png` (1024×1024) zeigt Koko freundlich sitzend; beide farbidentisch zum 3D-Modell. PASS/FAIL.
10. **Siegerpose:** Simulierter Spielgewinn löst `victory` aus (3,0 s, Lutscher-Umarmung); End-Pose wird ≥ 1,0 s gehalten. PASS/FAIL.
11. **Strategie-Tipp:** Der Ladebildschirm zeigt den Satz aus 3.10. PASS/FAIL.
12. **Voice (falls aktiv):** Alle 6 Samples aus 3.8 existieren, ≤ 1,5 s, Tonfall tief/warm/rund. PASS/FAIL.
13. **Fehlerresistenz:** Aufruf einer nicht existierenden Animation crasht nicht, fällt auf `idle` zurück, loggt Fehler. PASS/FAIL.
