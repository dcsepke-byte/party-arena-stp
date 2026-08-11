# Brix — Party Arena Game Bible

> **Teil:** V — Characters (5.2)
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** `design/gdd/game-concept.md`, `design/gdd/characters-overview.md`

---

## 1. Overview

Brix ist der **Stein-Golem** aus der Mechanik-Stadt — der kräftigste, schwerste und gutmütigste Tollpatsch der Arena. Er ist breit, massiv und quadratisch gebaut, mit runden Kanten, übergroßen Händen, kleinen leuchtenden Augen und Moos-Flecken auf den Schultern. Seine Persönlichkeit ist mutig und gutherzig, aber tollpatschig: Er will immer helfen und stößt dabei gern etwas um. Seine Signaturfarbe ist Orange (`#ff6a00`). Wie alle Arenians besitzt Brix keinerlei spielmechanische Vorteile — er ist genauso schnell, genauso stark und genauso verwundbar wie jeder andere Charakter. Sein "Gewicht" ist eine reine Inszenierung aus Animation, Sound und Pose.

Dieses Kapitel spezifiziert Brix vollständig: Identität, visuelles Design, alle 12 Pflichtanimationen, Porträt, Siegerpose, optionale Voice-Lines, Heimat-Bezug und Strategie-Tipp. Es ist an den Vertrag aus `characters-overview.md` gebunden.

| Kernfakt | Wert |
|----------|------|
| ID / Ordnername | `brix` |
| Anzeigename | Brix |
| Typ | Stein-Golem |
| Heimat-Insel | Mechanik-Stadt |
| Persönlichkeit | mutig, tollpatschig, gutherzig |
| Primärfarbe | Orange `#ff6a00` |
| Silhouetten-Archetyp | breit, massiv, quadratisch/rechteckig |
| Modellhöhe | 1,2 Einheiten (1,08–1,32) |
| Trefferbox | Zylinder oder Kapsel, Radius 0,6, Höhe 1,2 |

## 2. Player Fantasy

Brix spielt sich wie der **freundliche Riese der Gruppe**: Wenn man Brix wählt, fühlt man sich stark, unverwüstlich und ein bisschen ungelenk. Jede seiner Bewegungen vermittelt Masse — die Schritte lassen den Boden beben, die Fäuste sind riesig, und selbst sein Jubel wirkt, als könnte er gleich etwas umwerfen. Die Fantasie dahinter lautet: **"Ich bin der Fels in der Brandung — aber bitte stellt nichts Zerbrechliches in meine Nähe."** Brix-Spieler genießen die komische Diskrepanz zwischen gutem Willen und tollpatschiger Wirkung.

Design-Pillar-Bezug: **Überzeichnet** — Brix' Schwere ist extrem übertrieben (Bodenbeben, Staubwolken, knirschende Steine). **Wiedererkennbar** — seine rechteckige Silhouette ist die unverwechselbarste der Arena; selbst als winziges Icon oder aus der Kamera-Distanz ist er sofort als Brix lesbar. Seine Identität wird nie über Stärke-Spielwerte, sondern immer über Bewegung, Sound und Form erzählt — ein klares Beispiel für die Balance-Philosophie aus `characters-overview.md`.

## 3. Detailed Rules

### 3.1 Identität und Kernaussage

Brix stammt aus der Mechanik-Stadt, der Insel aus Zahnrädern, Dampf und Spielzeug-Technik. Er ist dort als steinerner "Kraftkern" geboren — ein Golem, der aus den Felsen der Insel geformt wurde und seitdem versucht, sich in der präzisen Welt der Maschinen zurechtzufinden. Er versteht Mechanik instinktiv schlecht, aber Menschen (und Arenians) instinktiv gut. Seine Kernaussage: **"Ich bin groß, ich bin freundlich, und ich breche dauernd versehentlich etwas."**

### 3.2 Visuelles Design

1. **Modell:** Robuster Stein-Golem im Cartoon/Toy-Stil, hohe Sättigung. Der Körper besteht aus großen, rundkantigen Felsbrocken (Kopf, Brust, zwei Arme, zwei kurze Beine). Die Gelenke sind sichtbare Fugen mit kleinen Moos- oder Grasbüscheln.
2. **Hände:** Übergroß, etwa so groß wie sein Kopf — das Markenzeichen. Bei `punch` und `happy` sind sie besonders präsent.
3. **Gesicht:** Kleine, leuchtende Augen (helles Gelb/Weiß, `#fff3b0`), die im Dunkeln leicht glimmen. Kein sichtbarer Mund; Emotionen werden über Augenform (Zusammenkneifen, Weiten), Körperhaltung und Steinknirschen ausgedrückt.
4. **Moos-Flecken:** Grüne (`#5a8f3c`) Moos-Patches auf beiden Schultern und am oberen Rücken — der einzige Farbkontrast zum Orange.
5. **Textur:** Hohe Sättigung, weiche Cartoon-Schattierung, keine realistischen Stein-Detailtexturen. Kanten sind abgerundet (Toy-Look). Kleine Risse als Flavor, aber niemals gruselig.
6. **Sekundärfarbe:** Dunkler Steinton `#6b4a2f` für Fugen und die Rückseite; Akzentfarbe Orange `#ff6a00` für die Hauptflächen.

### 3.3 Silhouette

- **Archetyp:** Breit, massiv, **quadratisch/rechteckig**. Brix ist deutlich breiter als jeder andere Arenian (Schulterbreite bis ca. 1,6 Einheiten), aber nicht höher (1,2 Einheiten). Das Breiten-Höhen-Verhältnis ist das markanteste der Arena.
- **Erkennung:** Auch ohne Farbe ist Brix an der rechteckigen Blockform, den übergroßen Händen und der gedrungenen Haltung erkennbar. Er steht immer leicht nach vorne gelehnt, als würde er gleich loslaufen.
- **Abgrenzung:** Anders als der kantige, technische Bolt hat Brix **runde** Ecken und organische, unregelmäßige Felsflächen. Bolt ist geometrisch-präzise, Brix ist massig-organisch.

### 3.4 Standardmaße und Kollision

- Modellhöhe `H = 1,2` (Toleranz 1,08–1,32). Brix darf mit den Schultern horizontal über die Trefferbox hinausragen, aber diese Teile erzeugen keine Kollision.
- Trefferbox identisch zum Standard: Zylinder oder Kapsel, Radius 0,6, Höhe 1,2. Brix' visuelle Breite darf größer sein als die Trefferbox; Minigame-Trefferchecks verwenden ausschließlich die Standard-Trefferbox (Fairness).

### 3.5 Animationsvertrag (12 Animationen)

Alle Animationen sind im Stil "schwerer Stein": langsame Anlaufzeiten, kräftige Abschlüsse, viel Staub/Erschütterung. Bewegungen wirken massig, aber nie träge-lahm — sie sind übertrieben und komisch.

| # | Animation | Schleife | Dauer-Ziel | Posen- und Bewegungsbeschreibung |
|---|-----------|----------|------------|-----------------------------------|
| 1 | `idle` | ja | 2,4 s | Brix wippt leicht von einem Bein aufs andere, die Schultern heben und senken sich. Alle ~1,2 s knirschen die Steine (leises Fugen-Knarren). Augen glimmen sanft. |
| 2 | `walk` | ja | 1,6 s pro Zyklus | Schwere, weite Schritte mit deutlicher Vorlage. Bei jedem Schritt hebt kurz eine Staubwolke auf; der Oberkörper wippt vertikal stark. Die großen Hände pendeln als Fäuste. |
| 3 | `run` | ja | 1,1 s pro Zyklus | Stampfender Dauerlauf; der Boden "bebt" (Kamera-/Effekt-Feedback). Arme pumpen, Kopf ist gesenkt, als würde er durch eine Wand wollen. |
| 4 | `punch` | nein | 0,8 s | Mächtiger, weiter Haken mit der rechten Faust; der Oberkörper dreht mit, danach federt er in den Stand zurück. Kleine Steinsplitter-Partikel am Abschluss. |
| 5 | `kick` | nein | 0,9 s | Kräftiger Tritt mit Schwung; der Körper dreht leicht mit, das Standbein wackelt kurz. Am Ende eine kleine Erschütterung. |
| 6 | `jump` | nein | 1,0 s | Ein Satz mit Anlauf-Staubwolke; in der Luft zieht Brix die Beine an, fällt dann schwer und federnd auf (kurzer Boden-Dip beim Landen). |
| 7 | `happy` | nein | 2,0 s | Beide riesigen Fäuste in die Höhe, die Augen leuchten hell auf. Die Steinoberfläche "glüht" kurz in der Signaturfarbe (Emissive-Puls). Kleiner Freudenhüpfer, der den Boden erzittern lässt. |
| 8 | `sad` | nein | 2,8 s | Brix zerfällt theatralisch in einen Haufen Steine (die Einzelteile senken sich, der Kopf bleibt oben auf dem Haufen liegen), dann setzt er sich wieder zusammen — erst Kopf, dann Rumpf, dann Arme. Die Augen glimmen schwach. |
| 9 | `stun` | ja | 2,0 s | Brix schwankt vor und zurück, kleine Steinchen rieseln von den Schultern. Die Augen blinken im Kreis (Sterne-Drehung optional). Er wirkt benommen, aber niemals verletzlich-besorgniserregend. |
| 10 | `carry` | ja | 0,9 s | Brix hält einen Gegenstand mit beiden großen Händen vor der Brust, als wäre es ein kostbares Ei. Er geht in Zeitlupe, um nichts fallen zu lassen. |
| 11 | `run-carry` | ja | 1,2 s | Gleiche Tragehaltung, aber im Stampf-Tempo; der Gegenstand wackelt gefährlich, Brix' Gesicht zeigt konzentriertes Bemühen. |
| 12 | `victory` | nein | 3,0 s | Brix stemmt einen riesigen, goldenen Stern über den Kopf (der Stern ist ein Effekt-/Requisit-Node), dreht sich dabei langsam um die eigene Achse und lacht tief und echoend. Kleine Funken fallen vom Stern. |

**Audio je Animation (SFX):** `idle`: leises Steinknirschen. `walk`/`run`: schwere, tiefe Trittsounds mit Hall, bei `run` zusätzlich ein tiefes Beben. `punch`/`kick`: dumpfer Stein-auf-Stein-Schlag. `jump`/Landung: kräftiger, federnder Aufprall. `sad`: rumpelndes Stein-auf-Stein-Geräusch beim Zerfallen. `victory`: triumphaler, hallender Bass-Ton.

### 3.6 Porträt

- **`icon.png` (256×256):** Brix' Kopf und Schultern, zentriert. Die leuchtenden Augen und die Moos-Schultern müssen auch im Downscale erkennbar sein. Hintergrund: transparent oder warmes Orange.
- **`splash.png` (1024×1024):** Brix in Sieger-Haltung (Fäuste in die Hüften gestemmt, leichte Vorlage), vor weichem orange-braunem Hintergrund mit dezenten Steinpartikeln. Hohe Sättigung, Cartoon-Schattierung.
- **Identität:** Porträt und 3D-Modell zeigen dieselbe Figur — gleiche Proportionen (übergroße Hände), gleiche Farbe (`#ff6a00`), gleiche Moos-Flecken.

### 3.7 Siegerpose

`victory` (3.5, Zeile 12): Brix stemmt den goldenen Stern über den Kopf und dreht sich. Die Kamera zeigt ihn leicht von unten (Hero-Shot), um die Masse zu betonen. Die Pose dauert 3,0 s und endet in einer gehaltenen End-Pose (beide Arme hoch, Stern über dem Kopf), bis die Siegerehrung weitergeht.

### 3.8 Voice & Audio (optional, budget-abhängig)

| Sample | Inhalt/Tonfall | Beschreibung |
|--------|----------------|--------------|
| `cheer` | Tiefes, echoendes Jubeln | "Höhö! Wir haben's geschafft!" in dumpfer, hallender Golem-Stimme. |
| `laugh` | Tiefes, echoendes Lachen | Polterndes "Hohohohoh!", als würde man in ein Fass lachen. |
| `ohno` | Bestürztes Grollen | "Oh-oh." tief, mit leichtem Steinknirschen am Ende. |
| `victory` | Triumphruf | Kurzer, mächtiger Siegesschrei mit Hall. |
| `sad` | Leises Grollen | Enttäuschtes "Hmpf..." mit knirschendem Unterton. |
| `item` | Neugieriges Brummen | "Was macht das wohl?" in naiv-freundlichem Ton. |

Tonfall-Konvention: tief, langsam, echoend; niemals bedrohlich. Brix ist gutherzig, sein Brummen ist warm, nicht angsteinflößend.

### 3.9 Heimat-Insel und Weltbezug

Brix' Heimat ist die Mechanik-Stadt (`world-mechanik-stadt.md`). Im Einleitungstext der Insel und in Flavor-Texten wird er als der steinerne "Kraftkern" der Stadt gezeigt, der zwischen den Zahnrädern wohnt und regelmäßig Maschinen versehentlich stilllegt. Dieser Bezug ist rein narrativ — auf der Mechanik-Stadt hat Brix keinerlei Vor- oder Nachteil.

### 3.10 Strategie-Tipp (Ladebildschirm)

> "Brix mag den Item-Shop — mit Schutzschild ist er unaufhaltsam!"

Der Tipp ist spielmechanisch neutral (er nennt ein Item und einen Shop, die für alle gleich sind), passt aber zur tollpatschigen Persönlichkeit: Brix "verzeiht" dank Schutzschild seine eigenen Patzer.

## 4. Formulas

### 4.1 Größen-Toleranz

`1,08 ≤ H ≤ 1,32` mit Ziel `H = 1,2` (siehe `characters-overview.md` 4.4). Für Brix gilt zusätzlich das Breiten-Kriterium:

`W_Schulter ≥ 1,2 × H` — die Schulterbreite muss mindestens 120 % der Höhe betragen, um den massigen Archetyp zu garantieren. Maximalwert: `W_Schulter ≤ 1,6` (nicht-kollidierend, visuell).

### 4.2 Farbwerte

Primärfarbe `#ff6a00` → normalisiert `(r,g,b) = (1,000; 0,416; 0,000)`.

Sekundärfarben: Steinfuge `#6b4a2f`, Moos `#5a8f3c`, Augen `#fff3b0`.

Farbabstand zu allen anderen Primärfarben gemäß `characters-overview.md` 4.6: Der engste Abstand besteht zu Koko (`#ff4d6d`) mit `d ≈ 0,26`; Ziel `d ≥ 0,20` ist erfüllt.

### 4.3 Animations-Zeitbudget

Summe der einmaligen Animationsdauern (punch + kick + jump + happy + sad + victory): `0,8 + 0,9 + 1,0 + 2,0 + 2,8 + 3,0 = 10,5 s`. Alle Werte müssen innerhalb der in 3.5 angegebenen Bereiche liegen.

### 4.4 Siegerpose-Endhaltung

Die `victory`-End-Pose muss mindestens `1,0 s` gehalten werden können, ohne in den `idle`-Zustand zurückzufallen (für Kamera und Screenshot).

## 5. Edge Cases

1. **Brix' breite Schultern ragen über die Trefferbox:** Erlaubt. Sie erzeugen keine Kollision; Minigame-Checks nutzen nur die Standard-Trefferbox. Bei sichtbarer Kollision mit Wänden ist der Fehler zu beheben (Mesh darf nicht in Collider umgewandelt werden).
2. **`sad`-Zerfall mitten in Bewegung:** Wird `sad` ausgelöst, während Brix zwischen Feldern läuft, bricht die Bewegung ab, die Animation läuft vollständig, danach steht Brix am Ziel-Feld. Kein Zwischenzustand mit halb zerfallenem Golem im Board.
3. **Brix in engen Minispiel-Korridoren:** Da die Trefferbox Standard ist, passt Brix überall hindurch, wo jeder andere auch hindurchpasst. Die breite Optik ist rein visuell; wird sie als unfair empfunden, ist das ein Art-Feedback (nicht gameplay-relevant) und über `W_Schulter` (Tuning, Sektion 7) justierbar.
4. **`victory` mit Stern-Requisit bei eingefrorener Animation:** Frieren während der Pose friert auch das Stern-Requisit ein; beim Fortsetzen endet die Pose normal.
5. **Emission der Augen im hellen Licht:** Die Augen sollen auch bei Tageslicht-Inseln sichtbar sein; die Emissive-Stärke muss ≥ `0,8` im Standard-Material betragen, sonst verlieren sie ihre Erkennbarkeit.
6. **Brix auf seiner Heimat-Insel Mechanik-Stadt:** Kein spielmechanischer Effekt; nur narrative Flavor-Texte und mögliche Spezial-Dialoge des ArenaStar.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `character-brix.md` | Art | Verwendung |
|-----------------------------------|-----|------------|
| `design/gdd/characters-overview.md` | Peer | Liefert den verbindlichen Vertrag: 12 Animationen, Maße, Trefferbox, Porträt, API. |
| `design/gdd/world-mechanik-stadt.md` | Peer | Liefert die Heimat-Insel, Themen und Flavor-Kontext. |
| `design/gdd/game-concept.md` | Quelle | Liefert Kern-Daten (Name, Typ, Farbe, Persönlichkeit). |
| `design/gdd/ui-character-select.md`, `design/gdd/ui-hud.md` | Peer | Verwendung von Porträt, Name und Animationen. |
| `design/gdd/audio-voice.md` | Peer | Steuerung der optionalen Voice-Lines. |
| `common/scripts/character.gd` | Code | Basisklasse, die alle Animationen ansteuert. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `plugins/characters/brix/` (Plugin) | Die konkreten Assets (Modell, Texturen, Animationen, Porträts, Voice) müssen exakt dieser Spezifikation entsprechen. |
| `design/gdd/characters-overview.md` | Referenziert Brix im Roster (Sektion 1) und in den Formeln (4.6). |
| Ladebildschirm | Zeigt `splash.png` und den Strategie-Tipp (3.10). |
| Siegerehrung (`victory-conditions.md`) | Löst die `victory`-Animation aus. |

### 6.3 Bidirektionalität

`characters-overview.md` verweist auf dieses Kapitel (Roster), dieses Kapitel verweist auf `characters-overview.md` (Vertrag). `world-mechanik-stadt.md` muss Brix als Bewohner erwähnen; dieses Kapitel verweist auf die Insel. Wird Brix' Design geändert, müssen Plugin, Overview-Roster und Insel-Kapitel synchron aktualisiert werden.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Schulterbreite `W_Schulter` | Feel | 1,2 × H bis 1,6 Einheiten | 1,2 × H = 1,44 | Steuert die "Massigkeit" der Silhouette. Rein visuell; größer = comic-hafter, darf nie kollidieren. |
| `idle`-Wipp-Geschwindigkeit | Feel | 1,5–3,5 s pro Wipp-Zyklus | 2,4 s | Lebendigkeit in der Wartepose; schneller = unruhiger, langsamer = schwerer. |
| Schritterschütterung bei `walk`/`run` | Feel | 0 (aus) bis 0,3 (stark) | 0,2 | Stärke des Bodenbebens (Kamera-Mikro-Shake). Nur bei Brix sichtbar; darf keine Spieler-Steuerung beeinflussen. |
| `happy`-Glühen (Emissive-Puls) | Feel | 0,5–1,5 s Pulsdauer | 1,0 s | Dauer des Aufleuchtens der Steine. Länger = majestätischer. |
| `victory`-Dauer | Feel | 2,0–4,0 s | 3,0 s | Länge der Siegerpose; kürzer = zügiger, länger = theatralischer. |
| Voice-Echo-Stärke | Feel | 0,2–0,8 (Dry/Wet) | 0,5 | Hall-Intensität der Stimme; Brix' Markenzeichen "echoend". |

Kein Knob verändert Spielwerte; alle wirken nur auf Optik, Sound und Timing.

## 8. Acceptance Criteria

1. **Modell:** Das Plugin `plugins/characters/brix/character.tscn` lädt in Godot 4.2 ohne Fehler; Root-Node hat `character.gd`. PASS/FAIL.
2. **Silhouette:** Brix ist als Schattenriss (ohne Farbe, ohne Details) von allen anderen 7 Arenians unterscheidbar; die Schulterbreite erfüllt `1,2 × H ≤ W ≤ 1,6`. PASS/FAIL.
3. **Farben:** Primärfarbe entspricht `#ff6a00` (± Toleranz gemäß Farbformel 4.2); Moos-Flecken und Augen sind vorhanden und farblich korrekt. PASS/FAIL.
4. **Animationen:** Alle 12 Pflichtanimationen existieren mit den Namen aus 3.5; `play_animation("victory")` spielt die Siegerpose. PASS/FAIL.
5. **Animations-Qualität:** `idle` loopt nahtlos ohne sichtbaren Sprung; `walk`/`run` erzeugen Trittsounds und (bei `run`) Beben; `sad` zeigt den Zerfall-und-Wiederaufbau; `happy` zeigt das Aufglühen. PASS/FAIL.
6. **API:** `freeze_animation()` hält Brix exakt in der aktuellen Pose (kein Zurückfallen); `resume_animation()` setzt an gleicher Stelle fort. PASS/FAIL.
7. **Maße:** `1,08 ≤ H ≤ 1,32`; Trefferbox Zylinder/Kapsel `r = 0,6`, `h = 1,2`, identisch zum Standard. PASS/FAIL.
8. **Balance:** Brix' exportierte Gameplay-Parameter (Bewegungsgeschwindigkeit, Sprunghöhe, Kollisionsmaske) sind identisch zu allen anderen Arenians. PASS/FAIL.
9. **Porträt:** `icon.png` (256×256) zeigt Kopf+Schultern mit leuchtenden Augen, bei 32 px erkennbar; `splash.png` (1024×1024) zeigt Brix in Sieger-Haltung; beide farbidentisch zum 3D-Modell. PASS/FAIL.
10. **Siegerpose:** Simulierter Spielgewinn löst `victory` aus (3,0 s, Stern-Requisit, Kamera-Hero-Shot); End-Pose wird ≥ 1,0 s gehalten. PASS/FAIL.
11. **Strategie-Tipp:** Der Ladebildschirm zeigt exakt den Satz aus 3.10. PASS/FAIL.
12. **Voice (falls aktiv):** Alle 6 Samples aus 3.8 existieren, ≤ 1,5 s, Tonfall tief/echoend/warm. PASS/FAIL.
13. **Fehlerresistenz:** Aufruf einer nicht existierenden Animation crasht nicht, fällt auf `idle` zurück, loggt Fehler. PASS/FAIL.
