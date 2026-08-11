# Pip — Party Arena Game Bible

> **Teil:** V — Characters (5.4)
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** `design/gdd/game-concept.md`, `design/gdd/characters-overview.md`

---

## 1. Overview

Pip ist das **fliegende Eichhörnchen** aus dem Wolkenwerk — schnell, frech und nie stillzustehen. Er ist die kleinste Figur der Arena: ein winziges Eichhörnchen mit Flughäuten (Patagien) zwischen Vorder- und Hinterbeinen, großen Kulleraugen und einem flauschigen, buschigen Schwanz. Seine Signaturfarbe ist Gelb (`#ffd34e`). Pip hüpft statt zu laufen und macht bei jeder Gelegenheit kurze Gleitflüge; seine Energie ist ansteckend. Wie alle Arenians hat er keinerlei spielmechanische Vorteile — seine Schnelligkeit ist eine reine Animations- und Persönlichkeitsinszenierung, die exakt auf dieselbe Feld-zu-Feld-Geschwindigkeit gemappt ist wie bei allen anderen Charakteren.

Dieses Kapitel spezifiziert Pip vollständig: Identität, visuelles Design, alle 12 Pflichtanimationen, Porträt, Siegerpose, optionale Voice-Lines, Heimat-Bezug und Strategie-Tipp. Es ist an den Vertrag aus `characters-overview.md` gebunden.

| Kernfakt | Wert |
|----------|------|
| ID / Ordnername | `pip` |
| Anzeigename | Pip |
| Typ | Fliegendes Eichhörnchen |
| Heimat-Insel | Wolkenwerk |
| Persönlichkeit | schnell, frech, immer in Bewegung |
| Primärfarbe | Gelb `#ffd34e` |
| Silhouetten-Archetyp | kleinste Figur, Flughaut bei Sprüngen, buschiger Schwanz |
| Modellhöhe | 1,2 Einheiten (1,08–1,32) |
| Trefferbox | Zylinder oder Kapsel, Radius 0,6, Höhe 1,2 |

## 2. Player Fantasy

Pip spielt sich wie der **Flummi der Gruppe**: Wer Pip wählt, fühlt sich schnell, gewitzt und einen Tick unverschämt. Er zappelt, wenn er stillstehen soll, er lacht, wenn andere stolpern, und er ist mit einer Gleitflug-Nummer zur Stelle, sobald etwas passiert. Die Fantasie dahinter lautet: **"Ich bin überall gleichzeitig — und meistens einen Schritt voraus."** Pips Frechheit ist dabei nie bösartig, sondern die pure Freude am Tempo und an der Bewegung.

Design-Pillar-Bezug: **Sofort verständlich** — Pips geringe Größe und der riesige, buschige Schwanz sind unverwechselbar. **Überzeichnet** — er hüpft fast ohne Bodenkontakt und wirkt in der Luft so natürlich wie auf dem Boden. **Interaktiv wirkend** — seine Flughäute spannen sich bei Sprüngen sichtbar, sein Schwanz ist ein zweites Ausdrucksorgan (gestellt bei Freude, hängend bei Trauer). **Wiedererkennbar** — Gelb + klein + buschiger Schwanz: Pip ist auf jedem Bildschirm, in jedem Mini-Map-Icon und in jedem Chaos erkennbar. Er ist der Beweis, dass ein Charakter ohne Spielwert-Vorteil trotzdem "der Schnelle" sein kann — durch reine Bewegungschoreografie.

## 3. Detailed Rules

### 3.1 Identität und Kernaussage

Pip lebt im Wolkenwerk (`world-wolkenwerk.md`), der schwebenden Himmelsinsel. Er wurde zwischen Wolkenschichten und Regenbögen geboren und hat gelernt, den Wind als Verbündeten zu nutzen. Seine Kernaussage: **"Stillstehen ist für Leute, die keine Flughäute haben."** Er nimmt nichts zu ernst — außer dem nächsten Sprung.

### 3.2 Visuelles Design

1. **Modell:** Kleines, rundliches Eichhörnchen im Cartoon/Toy-Stil, hohe Sättigung. Der Körper ist kompakt, der Kopf im Verhältnis groß (Baby-Schema → niedlich, frech).
2. **Flughäute (Patagien):** Hautfalten zwischen Vorder- und Hinterbeinen, die an den Hand- und Fußgelenken ansetzen. Im Ruhezustand eng am Körper anliegend; bei Sprüngen/Gleitflügen gespannt als rautenförmige Segel sichtbar. Farbe: warmes Gelb mit hellerer Unterseite (`#ffe89b`).
3. **Schwanz:** Sehr groß, buschig, etwa so voluminös wie der restliche Körper. Wird wie ein Segel und ein Ausdrucksorgan eingesetzt (siehe 3.5).
4. **Gesicht:** Große, runde Kulleraugen (`#3a2a10` mit weißen Glanzpunkten), die bei Aufregung noch größer werden. Kleine, spitze Ohren mit hellen Innenflächen. Ein schelmisches Grinsen mit kleinem Zähnchen.
5. **Textur:** Flauschiges, weiches Fell (Toy-Look, keine realistischen Fell-Streifen), hohe Sättigung, klare Formen.

### 3.3 Silhouette

- **Archetyp:** Kleinste Figur der Arena. Im Stand ist Pip rundlich-kompakt mit übergroßem Schwanz; **in der Luft** (Sprung/Gleitflug) entfaltet er eine rautenförmige Flughaut-Silhouette, die sein Erkennungszeichen ist.
- **Erkennung:** Die Kombination aus geringer Körperbreite, buschigem Schwanz (ca. 0,8 Einheiten lang, gewölbt) und der Flughaut-Raute bei Sprüngen ist ohne Farbe eindeutig.
- **Abgrenzung:** Im Vergleich zu Koko (rund, kugelig, groß) ist Pip deutlich kleiner und energischer; im Vergleich zu Nixie (stromlinienförmig, Kiemen) ist Pip kompakt mit buschigem Schwanz, nicht gestreckt.

### 3.4 Standardmaße und Kollision

- Modellhöhe `H = 1,2` (Toleranz 1,08–1,32). Obwohl Pip "die kleinste Figur" ist, gilt dieselbe Standardhöhe wie für alle — der "Kleinheits"-Eindruck entsteht über die **schmale Körperbreite** und die Proportionen (großer Kopf, kompakte Gliedmaßen), nicht über eine kleinere Modellhöhe.
- **Körperbreite:** `W_Körper ≤ 0,5` Einheiten (schmalster Arenian), Schwanz und Flughäute ragen darüber hinaus, ohne zu kollidieren.
- Trefferbox identisch zum Standard: Zylinder oder Kapsel, Radius 0,6, Höhe 1,2.

### 3.5 Animationsvertrag (12 Animationen)

Pips Bewegungssprache ist "Federn, Flattern, Kullern": Er ist fast nie vollständig am Boden, jeder Schritt ist ein Mini-Hüpfer, und Sprünge gehen nahtlos in kurze Gleitflüge über.

| # | Animation | Schleife | Dauer-Ziel | Posen- und Bewegungsbeschreibung |
|---|-----------|----------|------------|-----------------------------------|
| 1 | `idle` | ja | 2,0 s | Pip zappelt: Er dreht den Kopf ruckartig nach links und rechts (Ausschau halten), der Schwanz zuckt, die Füße tippen. Er kann maximal 1,0 s wirklich ruhig sein, dann bewegt sich wieder etwas. |
| 2 | `walk` | ja | 1,2 s pro Zyklus | Schnelle, federnde Hüpfer — fast ein Flattern. Die Flughäute zucken bei jedem Hüpfer kurz auf, der Schwanz pumpt als Balancier- und Antriebshilfe. |
| 3 | `run` | ja | 0,9 s pro Zyklus | Kurze Gleitflüge zwischen schnellen Hüpfern: Pip springt ab, spannt die Flughäute, gleitet eine halbe Körperlänge und hüpft weiter. Der Schwanz wellt hinterher. |
| 4 | `punch` | nein | 0,5 s | Blitzschneller Pieks mit der kleinen Pfote nach vorn; die Bewegung ist so schnell, dass sie fast als Zuckung wirkt. Ein "Puff"-Sound begleitet den Abschluss. |
| 5 | `kick` | nein | 0,6 s | Ein Dreh-Tritt: Pip dreht sich in der Luft um 90° und tritt mit beiden Hinterbeinen. Wirkt wie ein akrobatischer Kuller-Trick. |
| 6 | `jump` | nein | 1,0 s | Pip springt hoch und **gleitet**: Er spreizt die Flughäute zu einer Raute, gleitet einen weiten, flachen Bogen und landet federn. Das ist Pips Signatur-Bewegung. |
| 7 | `happy` | nein | 2,0 s | Pip fliegt eine **Runde im Kreis** (ein voller Looping-artiger Kreis in der Luft, Flughäute gespannt), landet und kichert. Der Schwanz sträubt sich vor Freude. |
| 8 | `sad` | nein | 2,2 s | Pip zieht die Flughaut wie eine Kapuze **über den Kopf**, der Schwanz hängt schlaff herab, die Ohren sinken. Er wirkt geknickt, aber niedlich. |
| 9 | `stun` | ja | 1,8 s | Pip wackelt benommen, kleine Sterne kreisen über seinem Kopf, der Schwanz zuckt unkontrolliert. Er taumelt leicht seitlich. |
| 10 | `carry` | ja | 0,8 s | Pip trägt einen Gegenstand **über dem Kopf** (beide Pfötchen hochgestreckt), flattert leicht mit den Flughäuten, um das Gewicht zu halten. Der Schwanz balanciert. |
| 11 | `run-carry` | ja | 1,0 s | Pip flattert mit dem Gegenstand über dem Kopf in schnellen, kurzen Gleitflügen; das Objekt wackelt, Pip klemmt es mit einem Daumen fest. |
| 12 | `victory` | nein | 2,6 s | Pip **schwebt mit ausgebreiteten Flughäuten** in der Luft, auf seinem Kopf sitzt ein kleiner leuchtender Stern. Er dreht sich langsam, zwinkert und grinst. Kleine Glitzer-Partikel. |

**Audio je Animation (SFX):** `walk`/`run`: leichte, helle "Hopf"-Geräusche (kein schwerer Tritt). `jump`: kurzes "Wusch" beim Spreizen der Flughäute. `punch`: helles "Puff". `happy`: aufsteigendes Kicher-Glissando. `sad`: einzelner, leiser "Plopp"-Ton. `victory`: funkelndes Glitzer-Glissando.

### 3.6 Porträt

- **`icon.png` (256×256):** Pips Kopf mit großen Augen und buschigem Schwanz über der Schulter, zentriert. Auch im Downscale müssen die Kulleraugen und die Gelb-Farbe lesbar bleiben. Hintergrund: transparent oder hellgelb.
- **`splash.png` (1024×1024):** Pip in Gleitflug-Haltung (Flughäute gespannt, Schwanz gewölbt, Grinsen) vor weichem gelb-weißem Hintergrund mit dezenten Wölkchen. Hohe Sättigung, dynamische Pose.
- **Identität:** Porträt und 3D-Modell zeigen dieselbe Figur — Gelb `#ffd34e`, große Augen, buschiger Schwanz, Flughäute.

### 3.7 Siegerpose

`victory` (3.5, Zeile 12): Pip schwebt mit gespannten Flughäuten, der Stern auf dem Kopf. Die Kamera zeigt ihn leicht von unten vor einem hellen Hintergrund, Glitzer fällt. Die Pose dauert 2,6 s und endet in der gehaltenen Schwebe-End-Pose (bis die Siegerehrung weitergeht).

### 3.8 Voice & Audio (optional, budget-abhängig)

| Sample | Inhalt/Tonfall | Beschreibung |
|--------|----------------|--------------|
| `cheer` | Schnelles Piepsen | Helles, schnelles "Jii-piii!" mit aufgeregtem Kichern. |
| `laugh` | Gekicher | Schnelles, hohes Kichern in Triolen, wie ein rasches "hi-hi-hi-hi!". |
| `ohno` | Erschrockenes Piepsen | Hohes, überraschtes "Piep!?" — kurz, schrill, aber komisch. |
| `victory` | Triumph-Gezwitscher | Langes, triumphales "Juhuu-piep!" mit Kicher-Ende. |
| `sad` | Leises Piepsen | Tief betrübtes, leises "Pip..." mit hängendem Ende. |
| `item` | Neugieriges Piepsen | "Ooh, was ist das?" in schnellem, frechem Ton. |

Tonfall-Konvention: hoch, schnell, piepsig; niemals schrill-schmerzhaft. Pips Stimme ist Energie pur.

### 3.9 Heimat-Insel und Weltbezug

Pips Heimat ist das Wolkenwerk (`world-wolkenwerk.md`). In Flavor-Texten wird er als Windreiter gezeigt, der zwischen den schwebenden Inselchen von Wolke zu Wolke springt. Rein narrativer Bezug — auf dem Wolkenwerk hat er keinen Vor- oder Nachteil.

### 3.10 Strategie-Tipp (Ladebildschirm)

> "Pip ist schnell — aber er hasst es, auf dem Glück/Pech-Feld zu landen. Erst würfeln, dann frech sein!"

Hinweis: Der Tipp ist ein humorvoller, spielmechanisch neutraler Ratschlag (Glück/Pech-Feld gilt für alle gleich) und passt zu Pips frecher, ungeduldiger Art.

## 4. Formulas

### 4.1 Größen-Toleranz

`1,08 ≤ H ≤ 1,32` mit Ziel `H = 1,2`. Schmale Körperbreite: `W_Körper ≤ 0,5` Einheiten (rein visuell). Schwanz-Länge `L_Schwanz ≤ 0,9` Einheiten, nicht kollidierend.

### 4.2 Farbwerte

Primärfarbe `#ffd34e` → normalisiert `(r,g,b) = (1,000; 0,827; 0,306)`.

Sekundärfarben: Flughaut-Unterseite `#ffe89b`, Augen `#3a2a10`, Glitzer-Stern (Victory) `#fff3b0`.

Farbabstand zu allen anderen Primärfarben gemäß `characters-overview.md` 4.6: engster Abstand zu Brix (`#ff6a00`) mit `d ≈ 0,30`; Ziel `d ≥ 0,20` erfüllt.

### 4.3 Animations-Zeitbudget

Summe der einmaligen Animationsdauern (punch + kick + jump + happy + sad + victory): `0,5 + 0,6 + 1,0 + 2,0 + 2,2 + 2,6 = 8,9 s` — das niedrigste einmalige Budget aller Arenians, passend zu Pips Tempo. Alle Werte innerhalb der Bereiche aus 3.5.

### 4.4 Flugzeit-Anteil

Anteil der `walk`- und `run`-Zyklen, in denen Pip keinen Bodenkontakt hat: `F_Kontaktfrei ≥ 60 %` für `run` (gemessen über die Root-Motion-Kurve). Das macht das "flatternde" Laufen prüfbar.

## 5. Edge Cases

1. **Pip "klein" trotz Standardhöhe:** Pips Kompaktheit entsteht über die schmale Körperbreite (`W_Körper ≤ 0,5`) und die Proportionen, nicht über eine reduzierte Höhe. Eine kleinere Modellhöhe wäre ein Vertragsbruch (Standard-Trefferbox würde nicht mehr passen).
2. **Flughäute bei `freeze_animation()`:** Frieren Pip mitten im Gleitflug ein, bleibt er in der Luft stehen; `resume_animation()` setzt den Flug fort. Das Board-System stellt nach Animationsende sicher, dass Pip auf dem Ziel-Feld steht.
3. **`victory`-Stern-Requisit bei Partikel-Deaktivierung:** Der Stern ist ein Node/Anhängsel, kein Partikel; er bleibt auch bei deaktivierten Partikeln sichtbar. Nur der Glitzer-Schweif entfällt.
4. **Pip auf dem Wolkenwerk (Heimat):** Kein spielmechanischer Effekt; nur narrative Flavor-Texte.
5. **Schnelle `punch`-Animation wirkt unfair:** Die 0,5-s-Animation ist rein kosmetisch; Minispiel-Timing basiert auf Spieler-Input, nicht auf Animationslänge. Kein Balance-Problem, da keine Trefferbox aus der Animation abgeleitet wird.
6. **Buschiger Schwanz verdeckt Icon-Details:** Im `icon.png` muss der Schwanz hinter dem Körper gezeichnet sein, sodass Kopf + Augen frei bleiben (Z-Priority im Porträt, nicht im 3D-Modell relevant).

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `character-pip.md` | Art | Verwendung |
|---------------------------------|-----|------------|
| `design/gdd/characters-overview.md` | Peer | Liefert den verbindlichen Vertrag: 12 Animationen, Maße, Trefferbox, Porträt, API. |
| `design/gdd/world-wolkenwerk.md` | Peer | Liefert die Heimat-Insel, Themen und Flavor-Kontext. |
| `design/gdd/game-concept.md` | Quelle | Liefert Kern-Daten (Name, Typ, Farbe, Persönlichkeit). |
| `design/gdd/ui-character-select.md`, `design/gdd/ui-hud.md` | Peer | Verwendung von Porträt, Name und Animationen. |
| `design/gdd/audio-voice.md` | Peer | Steuerung der optionalen Voice-Lines. |
| `common/scripts/character.gd` | Code | Basisklasse, die alle Animationen ansteuert. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `plugins/characters/pip/` (Plugin) | Die konkreten Assets müssen exakt dieser Spezifikation entsprechen. |
| `design/gdd/characters-overview.md` | Referenziert Pip im Roster (Sektion 1) und in den Formeln (4.6). |
| Ladebildschirm | Zeigt `splash.png` und den Strategie-Tipp (3.10). |
| Siegerehrung (`victory-conditions.md`) | Löst die `victory`-Animation aus. |

### 6.3 Bidirektionalität

`characters-overview.md` verweist auf dieses Kapitel (Roster), dieses Kapitel verweist auf `characters-overview.md` (Vertrag). `world-wolkenwerk.md` muss Pip als Bewohner erwähnen; dieses Kapitel verweist auf die Insel. Wird Pips Design geändert, müssen Plugin, Overview-Roster und Insel-Kapitel synchron aktualisiert werden.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| `idle`-Zappel-Intervall | Feel | 0,5–2,0 s | 1,0 s | Maximale Ruhephase in der Wartepose; kürzer = unruhiger. |
| Körperbreite `W_Körper` | Feel | 0,4–0,6 Einheiten | 0,5 | Kompaktheit der Silhouette. Rein visuell; darf nie kollidieren. |
| Flugzeit-Anteil `F_Kontaktfrei` (run) | Feel | 50–80 % | 60 % | Wie stark das Laufen als Flattern wirkt (4.4). |
| Gleit-Bogenhöhe bei `jump` | Feel | 0,3–0,7 Einheiten | 0,5 | Höhe des Gleitbogens; höher = dramatischer, flacher = schneller wirkend. |
| Schwanz-Volumen | Feel | 0,7–1,1 Einheiten Länge | 0,9 | Größe des buschigen Schwanzes. Rein visuell. |
| `victory`-Dauer | Feel | 2,0–4,0 s | 2,6 s | Länge der Siegerpose. |

Kein Knob verändert Spielwerte; alle wirken nur auf Optik, Sound und Timing.

## 8. Acceptance Criteria

1. **Modell:** Das Plugin `plugins/characters/pip/character.tscn` lädt in Godot 4.2 ohne Fehler; Root-Node hat `character.gd`. PASS/FAIL.
2. **Silhouette:** Pip ist als Schattenriss von allen anderen 7 Arenians unterscheidbar (Kleinheit + buschiger Schwanz + Flughaut-Raute im Sprung). PASS/FAIL.
3. **Farben:** Primärfarbe entspricht `#ffd34e`; Flughäute, Augen und Schwanz sind vorhanden und farblich korrekt. PASS/FAIL.
4. **Animationen:** Alle 12 Pflichtanimationen existieren mit den Namen aus 3.5; `play_animation("victory")` spielt die Schwebe-Pose. PASS/FAIL.
5. **Animations-Qualität:** `run` erfüllt `F_Kontaktfrei ≥ 60 %`; `jump` zeigt die Flughaut-Raute; `happy` enthält die Flugrunde im Kreis; `sad` zeigt die Flughaut-Kapuze. PASS/FAIL.
6. **API:** `freeze_animation()` hält Pip exakt (auch im Gleitflug); `resume_animation()` setzt an gleicher Stelle fort. PASS/FAIL.
7. **Maße:** `1,08 ≤ H ≤ 1,32`; Körperbreite `≤ 0,5`; Trefferbox identisch zum Standard (`r = 0,6`, `h = 1,2`); Schwanz/Flughäute kollidieren nicht. PASS/FAIL.
8. **Balance:** Pips exportierte Gameplay-Parameter sind identisch zu allen anderen Arenians. PASS/FAIL.
9. **Porträt:** `icon.png` (256×256) zeigt Kulleraugen + Schwanz, bei 32 px erkennbar; `splash.png` (1024×1024) zeigt Pip im Gleitflug; beide farbidentisch zum 3D-Modell. PASS/FAIL.
10. **Siegerpose:** Simulierter Spielgewinn löst `victory` aus (2,6 s, Schwebe + Stern auf dem Kopf); End-Pose wird ≥ 1,0 s gehalten. PASS/FAIL.
11. **Strategie-Tipp:** Der Ladebildschirm zeigt den Satz aus 3.10. PASS/FAIL.
12. **Voice (falls aktiv):** Alle 6 Samples aus 3.8 existieren, ≤ 1,5 s, Tonfall hoch/schnell/piepsig. PASS/FAIL.
13. **Fehlerresistenz:** Aufruf einer nicht existierenden Animation crasht nicht, fällt auf `idle` zurück, loggt Fehler. PASS/FAIL.
