# Charakter-System — Party Arena Game Bible

> **Teil:** V — Characters (5.1)
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** `design/gdd/game-concept.md`, `design/gdd/session-1-analysis.md`, `common/scripts/character.gd`, `common/scripts/loader/character_loader.gd`, `common/scripts/loader/plugin_system.gd`

---

## 1. Overview

Das Charakter-System spezifiziert die 8 spielbaren Arenians von Party Arena: ihre Rolle im Spiel, den Plugin-Ladevertrag, den Auswahlprozess, den verbindlichen Animationsvertrag, den Größen- und Kollisionsstandard, das Porträt-Format, die Siegerpose und die optionale Sprachausgabe. Die zentrale Designentscheidung lautet: **Alle 8 Charaktere sind spielmechanisch vollständig identisch.** Es gibt keine unterschiedlichen Stats, keine versteckten Eigenschaften, keine Pay-to-Win-Heibel und keinen Balance-Albtraum. Die Unterschiede zwischen den Charakteren sind ausschließlich visuell (Modell, Farbe, Silhouette), animationstechnisch (Bewegungs-Posen, Timing), akustisch (Voice-Lines, Bewegungs-Sounds) und narrativ (Persönlichkeit, Heimat-Insel, Sprüche). Ein Charakter ist damit eine **Persönlichkeits-Hülle ohne Spielwert-Vorteil** — die Wahl ist reine Selbstexpression, nie eine Metagame-Entscheidung.

Der technische Rahmen wird vom Fork-System von Super Tux Party geerbt und auf die 8 neuen Eigen-IP-Arenians übertragen: Jeder Charakter lebt in einem eigenen Plugin-Ordner unter `plugins/characters/`, wird beim Start automatisch vom `CharacterLoader` entdeckt und über eine gemeinsame Basisklasse (`character.gd`) angesteuert. Dieses Kapitel ist das Master-Dokument für alle acht Einzelkapitel (`character-brix.md` bis `character-momo.md`) und für alle Systeme, die Charaktere anzeigen, bewegen oder animieren.

| # | Charakter | Typ | Heimat-Insel | Persönlichkeit | Primärfarbe |
|---|-----------|-----|--------------|----------------|-------------|
| 1 | Brix | Stein-Golem | Mechanik-Stadt | mutig, tollpatschig, gutherzig | Orange `#ff6a00` |
| 2 | Nixie | Axolotl | Sonnenstrand | neugierig, wasseraffin, verspielt | Türkis `#00f0ff` |
| 3 | Pip | Fliegendes Eichhörnchen | Wolkenwerk | schnell, frech, immer in Bewegung | Gelb `#ffd34e` |
| 4 | Koko | Panda | Zuckerwald | freundlich, stark, gemütlich | Rosa `#ff4d6d` |
| 5 | Tiko | Vogel (Tukan) | Dschungeltempel | chaotisch, lustig, Feder-Wirbel | Grün `#2bffb9` |
| 6 | Bolt | Roboter | Mechanik-Stadt | logisch, präzise, liebenswert | Blau `#3a86ff` |
| 7 | Bloom | Kaktus | Dschungeltempel (Oasen-Rand) | ruhig, humorvoll, Stacheln nur Deko | Lila `#7b2ff7` |
| 8 | Momo | Waschbär | Frostgipfel | clever, trickreich, Schabernack | Pink `#ff3cac` |

## 2. Player Fantasy

Das Charakter-System verspricht dem Spieler: **"Wähle den, der du sein willst — nicht den, der am stärksten ist."** In einer Couch-Party-Runde mit 2–8 Spielern ist der Charakter das primäre Identifikations- und Unterscheidungsmerkmal. Jeder Spieler findet seinen Arenian anhand von Aussehen, Persönlichkeit und Animation: Wer laut und chaotisch feiern will, nimmt Tiko; wer ruhig und gemütlich mitfährt, nimmt Koko oder Bloom; wer sich clever und verschlagen fühlt, nimmt Momo. Da alle gleich stark sind, entsteht keine "Tier-List"-Diskussion am Auswahlbildschirm — die Auswahl ist eine reine Stimmungs- und Stilfrage und dauert deshalb nie länger als wenige Sekunden.

Die Design-Pillars werden direkt bedient:

1. **Sofort verständlich:** Jeder Charakter ist auf einen Blick als eigenständige Figur erkennbar — eine starke, unverwechselbare Silhouette (rechteckig, stromlinienförmig, rund, kantig) plus eine satte Signaturfarbe.
2. **Überzeichnet statt realistisch:** Die Animationen sind bewusst übertrieben (Brix' Bodenbeben, Blooms Rollen, Tikos Feder-Explosionen). Jeder Zustand ist sofort lesbar: Happy ist überschwänglich, Sad ist theatralisch.
3. **Interaktiv wirkend:** Charaktere reagieren sichtbar auf das Spielgeschehen — sie jubeln, trauern, werden gestunnt, tragen Items. Das Board wirkt lebendig, weil die Figuren ständig in Bewegung sind.
4. **Wiedererkennbar:** Über Spiel, Ladebildschirm, Porträt, HUD und Siegerpose hinweg ist dieselbe Figur wiederzuerkennen. Die Silhouette bleibt auch klein, aus der Distanz und für Farbfehlsichtige lesbar.

Emotional ist der Charakter der **Stellvertreter des Spielers im Spiel**: Er trägt den Sieg (Siegerpose), den Ärger (Sad-Animation) und die Schadenfreude (Happy-Animation) sichtbar zur Schau. Die Wahl des Charakters ist eine kleine Selbst-Inszenierung vor der Gruppe — eine der stärksten sozialen Bindungen des Party-Genres.

## 3. Detailed Rules

### 3.1 Balance-Philosophie: Identische Leistung

1. **Verbot jeder spielmechanischen Asymmetrie.** Kein Charakter besitzt andere Stats (Geschwindigkeit, Sprungkraft, Trefferbox-Größe, Würfelmodifikationen, Minispiel-Eigenschaften). Die einzige Ausnahme sind rein kosmetische Animationen und Sounds, die nachweislich keine Kollision oder Physik verändern.
2. **Identische Bewegungsparameter auf dem Board.** Alle Charaktere bewegen sich mit derselben Feld-zu-Feld-Geschwindigkeit (Laufgeschwindigkeit zwischen zwei Feldern: 2,4 Sekunden pro Feld, siehe `dice-movement.md`), unabhängig von Schrittlänge oder Gangart. Schritt-Animationen werden auf dieselbe Fortbewegungsdauer gemappt.
3. **Identische Physik in Minispielen.** Trefferboxen, Schwerkraft, Sprunghöhe und Kollisionsmasken sind charakterübergreifend identisch. Visuelle Unterschiede (z. B. Brix' breite Schultern) dürfen keine Kollision erzeugen, die über die Standard-Trefferbox hinausgeht.
4. **Keine versteckten Boni.** Weder Heimat-Inseln noch Persönlichkeit noch Seltenheit haben irgendeinen spielmechanischen Effekt. Ein Charakter auf seiner Heimat-Insel ist genauso stark wie überall sonst.
5. **Konsistenzprüfung:** Jeder neue Charakter durchläuft die Akzeptanzkriterien aus Sektion 8, die explizit die Spielwert-Gleichheit nachweisen.

### 3.2 Der Roster: 8 Arenians

Der Roster ist fest auf 8 Charaktere definiert (Tabelle in Sektion 1). Jeder Charakter hat genau ein Einzelkapitel in Teil V der Bible. Neue Charaktere sind nur über den Plugin-Mechanismus (3.3) möglich und erfordern einen Producer-Freigabeprozess; sie erhöhen die maximale Auswahl, aber nie die maximale Spielerzahl (die bleibt bei 8).

### 3.3 Plugin-Loader und Ordnervertrag

1. **Basisverzeichnis:** `plugins/characters/`. Jeder Charakter belegt genau **ein Unterverzeichnis**, dessen Name gleichzeitig die **kanonische Charakter-ID** ist. Konvention: Kleinbuchstaben, kebab-case, ohne Leerzeichen und Umlaute: `brix`, `nixie`, `pip`, `koko`, `tiko`, `bolt`, `bloom`, `momo`. Der Anzeigename (z. B. "Brix") ist die in Großschreibung gesetzte ID.
2. **Pflichtdateien je Charakter-Ordner:**
   - `character.tscn` — die instanziierbare Charakter-Szene (Root-Node vom Typ `Node3D`).
   - `icon.png` — kleines Porträt für HUD und Auswahl-Grid.
   - `splash.png` — großes Porträt für den Auswahlbildschirm und Ladebildschirme.
3. **Optionale Dateien:** 3D-Modell (`*.glb`/`*.blend`), Texturen (`*.png`, `*.tres`), `custom_animations.tres` (AnimationLibrary), Materialien.
4. **Entdeckung:** Der `CharacterLoader` scannt `plugins/characters/` beim Spielstart über `PluginSystem.load_files_from_path`. Ein Charakter gilt nur dann als geladen, wenn sein `character.tscn` existiert und am Root-Node das Skript `common/scripts/character.gd` hängt. Fehlt das Skript, wird eine Warnung ausgegeben und der Charakter übersprungen (genaue Fehlerbehandlung in Sektion 5).
5. **Lade-API:** Der Loader stellt bereit: Liste aller geladenen Charakter-IDs, Instanziierung einer Charakter-Szene per ID, Laden von `splash.png` und `icon.png` per ID. Jeder Aufruf mit unbekannter ID schlägt mit einem eindeutigen Fehler fehl und darf das Spiel nicht zum Absturz bringen.
6. **Erweiterbarkeit:** Ein neuer Charakter ist ein neuer Ordner. Keine Änderung an Kern-Code, Loader, UI oder Board-Logik ist nötig, solange der Vertrag eingehalten wird.

### 3.4 Charakter-Auswahl vor Spielstart

1. **Zeitpunkt:** Vor Spielbeginn, nach der Lobby- und vor der Insel-/Board-Auswahl (Reihenfolge siehe `ui-mainmenu.md` und `ui-character-select.md`).
2. **Spielerzahl:** 2–8 lokale Spieler (plus optional KI-Auffüllung gemäß Lobby-Einstellung). Die Auswahl ist beendet, wenn alle aktiven Spieler einen Charakter bestätigt haben.
3. **Duplikat-Regel:** **Kein Charakter darf doppelt gewählt werden.** Die Zuordnung Spieler → Charakter muss injektiv sein. Die UI erzwingt dies hart: Ist ein Charakter bereits gewählt, ist seine Kachel für andere Spieler gesperrt (deutlich visuell markiert, inkl. Namensschild des wählenden Spielers). Die Regel ist als Tuning-Knob modellierbar (siehe Sektion 7), Standard ist "verboten".
4. **Auswahl-Bestätigung:** Zuerst gewählt, dann bestätigt (Bestätigen-Knopf). Vor der Bestätigung ist Wechseln frei; nach der Bestätigung ist der Charakter fixiert, bis der Spieler die Bestätigung explizit zurücknimmt.
5. **Vorschau:** Auf dem Auswahlbildschirm wird der markierte Charakter als 3D-Modell in einer Vorschau-Drehbühne gezeigt (idle-Animation läuft) sowie `splash.png` als Großporträt. Das 3D-Modell wird live aus dem Plugin instanziiert.
6. **Namensvergabe:** Jeder Spieler kann optional einen Kurznamen vergeben; Standard ist der Charaktername. Die Anzeige im HUD nutzt den gewählten Namen, das Porträt immer den Charakter.
7. **Abbruch/Timeout:** Bricht ein Spieler vor der Bestätigung ab, wird seine Auswahl verworfen. Ein Spiel ohne mindestens 2 bestätigte Spieler startet nicht.

### 3.5 Der Animationsvertrag

Jeder Charakter muss **exakt 12 benannte Animationen** bereitstellen. Die Namen sind verbindlich (kleingeschrieben, Bindestrich für `run-carry`) und müssen als Zustandsnamen der AnimationTree-State-Machine beziehungsweise als Animationsnamen des AnimationPlayer existieren. Fehlende Animationen gelten als Vertragsverstoß (Blocker, siehe Sektion 8).

| # | Animationsname | Schleife | Typische Dauer | Verwendung |
|---|----------------|----------|----------------|------------|
| 1 | `idle` | ja | 2,0–3,0 s | Ruhepose auf dem Board, Auswahl-Vorschau, Wartezeiten |
| 2 | `walk` | ja | 1,2–1,8 s pro Zyklus | Feld-zu-Feld-Bewegung |
| 3 | `run` | ja | 0,8–1,3 s pro Zyklus | Beschleunigte Bewegung (z. B. Renn-Minispiele, schnelle Sequenzen) |
| 4 | `punch` | nein | 0,5–0,9 s | Faustschlag (Minispiel-Aktionen, Interaktionen) |
| 5 | `kick` | nein | 0,6–1,0 s | Tritt (Minispiel-Aktionen) |
| 6 | `jump` | nein | 0,6–1,0 s | Sprung (Minispiele, Bewegungshighlights) |
| 7 | `happy` | nein | 1,5–2,5 s | Jubel (Stern gekauft, Minispiel-Sieg, Event-Positiv) |
| 8 | `sad` | nein | 2,0–3,0 s | Trauer (Event-Negativ, Diebstahl, Minispiel-Niederlage) |
| 9 | `stun` | ja | 1,5–2,5 s | Betäubt (Item-Wirkung, Event) |
| 10 | `carry` | ja | 0,7–1,1 s | Tragen eines Gegenstands im Stand/Gehen |
| 11 | `run-carry` | ja | 0,9–1,3 s | Tragen eines Gegenstands in Eile |
| 12 | `victory` | nein | 2,0–4,0 s | Siegerpose beim Spielgewinn (Siegerehrung) |

Regeln:

1. **State-Machine-Konvention:** Alle 12 Namen müssen als Zustände existieren. Die State-Machine benötigt zusätzlich einen Start-/Idle-Zustand, der beim Laden aktiv ist.
2. **API-Vertrag (Basisklasse `character.gd`):** Das Spiel steuert Animationen ausschließlich über vier Methoden:
   - `play_animation(anim_name)` — weicher Übergang zur genannten Animation (AnimationPlayer: `play`; AnimationTree: State-Machine-`travel`).
   - `jump_to_animation(anim_name)` — sofortiger Sprung ohne Übergang (für harte Zustandswechsel); muss nach dem Szenen-Laden funktionieren, ohne dass der Default-Zustand die Animation überschreibt.
   - `freeze_animation()` — pausiert die laufende Animation an Ort und Stelle (für Pausen, Rundenwechsel, Screenshot-/Menü-Überlagerung).
   - `resume_animation()` — setzt die pausierte Animation fort.
   - Diese vier Methoden sind die **einzige** erlaubte Schnittstelle. Kein Spielcode darf direkt auf AnimationPlayer/AnimationTree zugreifen.
3. **Einfrieren-Verhalten:** `freeze_animation()` muss die Pose exakt halten (kein Zurückfallen in den Default-Zustand). `resume_animation()` muss exakt an der eingefrorenen Stelle fortsetzen.
4. **Loop-Sicherheit:** Schleifen-Animationen (idle, walk, run, stun, carry, run-carry) müssen nahtlos loopen (kein sichtbarer Sprung am Zyklusende).
5. **Zusatz-Animationen:** Weitere Zustände (z. B. `sit`, `stun-begin`, `stun-end`) sind erlaubt, ersetzen aber keine der 12 Pflichtanimationen.
6. **Gameplay-Bindung:** `happy`, `sad`, `stun`, `victory` werden vom Spielzustand ausgelöst (Stern-Kauf, Event-Ergebnis, Item-Treffer, Spielende). Die Zuordnung steht in `narrative-flavor.md` und `ui-hud.md`.

### 3.6 Größen- und Kollisionsstandard

1. **Zielhöhe:** Jeder Charakter ist im Godot-Koordinatensystem **1,2 Einheiten hoch** (±10 %, also 1,08–1,32). Gemessen wird vom Boden (Y = 0, Fußsohle) bis zum höchsten statischen Punkt des Modells (nicht bis zur Spitze einer optionalen, animierten Flughaut/Antenne im Bewegungszustand; dafür siehe 3.6.4).
2. **Trefferbox:** Ein `CollisionShape3D` als Kind des Root-Nodes, standardmäßig ein **Zylinder** (`CylinderShape3D`) mit Radius 0,6 und Höhe 1,2 Einheiten. Alternative: **Kapsel** (`CapsuleShape3D`) mit Radius 0,6 und Höhe 1,2 (Gesamthöhe inklusive Kappen). Die Trefferbox ist für alle 8 Charaktere **identisch**.
3. **Zentrierung:** Die Trefferbox ist horizontal auf die Modellmitte zentriert; ihre Unterkante liegt bei Y = 0.
4. **Silhouette vs. Hitbox:** Das sichtbare Modell darf die Trefferbox in horizontaler Ausdehnung überschreiten (z. B. Brix' Schultern, Koko's Bauch, Blooms Arme), solange diese Teile **keine Kollision** erzeugen. Vertikal darf das Modell die 1,32-Obergrenze nur mit animierten, nicht-kollidierenden Anhängseln (Kiemen, Antenne, Flughaut) überschreiten.
5. **Kollisions-Layer/Mask:** Alle Charaktere verwenden dieselben Kollisionslayer und -masken (Werte werden in `technical-architecture.md` definiert). Die Trefferbox ist als "Area/Collider" für Minispiel-Checks und Feld-Interaktionen nutzbar, blockiert aber nie die Bewegung anderer Spieler auf dem Board.
6. **Board-Repräsentation:** Im Board-Spiel ist der Charakter ein `Node3D` am aktuellen Feld (siehe `board-architecture.md`). Er läuft Feld zu Feld, wobei die Fortbewegungszeit charakterübergreifend identisch ist (3.1.2).

### 3.7 Porträt-Format

1. **`icon.png`:** 256×256 Pixel, quadratisch. Verwendung: HUD-Spielerleiste, Auswahl-Grid-Kacheln, Ergebnistafeln. Anforderungen: Charakter zentriert und vollständig sichtbar, Kopf mindestens 40 % der Bildbreite, hohe Sättigung, Silhouette auch bei 32-Pixel-Downscale lesbar.
2. **`splash.png`:** 1024×1024 Pixel, quadratisch. Verwendung: Auswahl-Heldenpanel, Ladebildschirm, Siegerehrung. Anforderungen: Charakter zentriert, weicher Hintergrund in Signaturfarbe oder Transparenz, Porträt-Haltung (Gesicht/Kopf zur Kamera), hohe Sättigung.
3. **Identität:** Porträt und 3D-Modell müssen dieselbe Figur in derselben Farbwelt zeigen (gleiche Primär-/Sekundärfarben). Das Porträt darf stilisiert sein (illustrativ), aber nicht derart abweichen, dass eine Verwechslung möglich ist.
4. **Dateiformat:** PNG, verlustfrei, sRGB. Kein Alpha-Zwang, aber Transparenz im Hintergrund ist empfohlen.

### 3.8 Siegerpose

1. Jeder Charakter besitzt eine **einzigartige** `victory`-Animation (2–4 s), die bei der Siegerehrung abgespielt wird (Sternenzitadelle/Finale, siehe `victory-conditions.md`).
2. Während der Pose schwenkt die Kamera auf den Sieger; alle anderen Spieler spielen ihre `happy`- oder `sad`-Animation je nach Platzierung.
3. Die Pose ist charakteristisch (siehe Einzelkapitel) und nutzt oft ein Requisit oder einen Effekt (Stern, Welle, Rakete, Lutscher, Münzstapel).
4. Wird die Siegerehrung übersprungen, darf die Pose entfallen, ohne dass ein Fehler auftritt.

### 3.9 Voice-Lines (optional, audio-budget-abhängig)

1. **Status:** Optional. Voice-Lines werden nur eingebaut, wenn das Audio-Budget (siehe `audio-voice.md`) es erlaubt. Fehlen sie, fällt der Charakter auf generische SFX und Text-Bubbles zurück.
2. **Pflicht-Set je Charakter** (falls Voice aktiviert): Jubel (`cheer`), Lachen (`laugh`), Missgeschick (`ohno`), Sieg (`victory`), Niederlage (`sad`), Item-Nutzung (`item`). Optional: Item-Kauf, Stern-Kauf, Begrüßung.
3. **Technische Vorgaben:** Mono, 44,1 kHz, Ogg Vorbis, maximale Länge 1,5 s pro Sample, Ziel-Lautstärke normalisiert auf −3 dBFS ± 3 dB. Dateinamen-Konvention `vo_[id].ogg` im Charakter-Ordner.
4. **Persönlichkeitsabgleich:** Der Tonfall muss zur Persönlichkeit passen (Brix: tief, echoend; Pip: schnell, piepsig; Bolt: Bleeper, usw. — Details in den Einzelkapiteln).
5. **Wiedergaberegeln:** Keine Voice-Line darf spielmechanische Informationen verbergen oder ersetzen (kein Pay-to-Win-Charakterflüstern). Voice-Lines werden nie über anderen Voice-Lines abgespielt (Prioritäts-Queue, siehe `audio-voice.md`).

### 3.10 Strategie-Tipp für Ladebildschirme

Jeder Charakter hat genau einen Ladebildschirm-Tipp (ein Satz), der die Persönlichkeit und eine spielmechanisch **neutrale**, aber nützliche Spielhilfe verbindet. Beispiele stehen in den Einzelkapiteln (z. B. Brix: "Brix mag den Item-Shop — mit Schutzschild ist er unaufhaltsam!"). Die Tipps sind rein informativ und dürfen keine falschen Vorteile suggerieren.

### 3.11 Namens- und Markenregeln

1. Die 8 Arenians sind Eigen-IP. Die Legacy-Charaktere aus Super Tux Party (Tux, Godette, Beastie, Green Tux) werden **nicht** als spielbare Arenians übernommen (siehe `technical-fork-strategy.md`). Ihre Plugin-Ordner dürfen für Entwicklungstests weiter existieren, gelten aber nicht als Roster.
2. Kein Charakter-Name darf mit ArenaStar, einer Insel oder einem Item kollidieren.

## 4. Formulas

### 4.1 Gültige Spielerzahl

`2 ≤ P ≤ 8`, wobei `P` die Anzahl der bestätigten Spieler ist. Ist `P < 2`, startet kein Spiel; ist `P > 8`, ist die Lobby voll und weitere Spieler werden abgewiesen.

### 4.2 Duplikat-Freiheit (Injektivität)

Die Zuordnung `S: Spieler → Charakter` muss injektiv sein: Für zwei verschiedene Spieler `i ≠ j` gilt `S(i) ≠ S(j)`. Da der Roster genau 8 Charaktere und `P ≤ 8` gilt, existiert immer mindestens eine injektive Zuordnung. Die UI erzwingt sie; die Anzahl der freien Zuordnungen beim Start der Auswahl beträgt `F = 8! / (8 − P)!`.

### 4.3 Animationsabdeckung

`C = (A_vorhanden / A_pflicht) × 100`, mit `A_pflicht = 12`.

- Akzeptanzregel: Für jeden ausgelieferten Charakter gilt `C = 100`. `C < 100` ist ein Blocker für die Aufnahme in den Roster.

### 4.4 Größen-Toleranz

`H` = Modellhöhe in Einheiten. Akzeptanz: `1,08 ≤ H ≤ 1,32`. Abweichung `ΔH = |H − 1,2| ≤ 0,12`.

### 4.5 Trefferbox-Toleranz

- Zylinder: `r = 0,6 ± 0,05`, `h = 1,2 ± 0,1`.
- Kapsel: `r = 0,6 ± 0,05`, Gesamthöhe `1,2 ± 0,1`.
- Alle 8 Charaktere müssen innerhalb der Toleranz denselben Satz erfüllen (identische Trefferbox).

### 4.6 Farbabstand zwischen Charakteren

Für zwei Charaktere `i`, `j` mit normalisierten RGB-Werten `(r,g,b) ∈ [0,1]`:

`d_ij = sqrt( ((r_i − r_j)² + (g_i − g_j)² + (b_i − b_j)²) / 3 )`

- Design-Ziel: `d_ij ≥ 0,20` für alle Paare der Primärfarben. Das engste Paar im aktuellen Roster ist Brix (`#ff6a00`) vs. Koko (`#ff4d6d`) mit `d ≈ 0,26` — der Zielwert ist damit erfüllt, aber knapp; neue Charakterfarben müssen den Zielwert gegen **alle** bestehenden Primärfarben nachweisen.
- Zweck: Verwechslungsfreiheit in HUD, Auswahl und auf dem Board. Farbfehlsichtigkeit wird zusätzlich über Silhouetten abgedeckt (nicht über Farben allein, siehe `ui-accessibility.md`).

### 4.7 Ladezeit-Budget

`t_Charakter ≤ 150 ms` pro Charakter-Szene (Instanziierung inklusive Modell und Texturen) auf der Referenz-Hardware aus `technical-performance.md`. Für alle 8 Charaktere: `Σ t ≤ 1,2 s`. Überschreitung verlängert den Ladebildschirm und ist ein Performance-Fund (Sektion 7).

### 4.8 Voice-Budget (nur bei aktivierter Sprachausgabe)

`V_gesamt = 6 Samples × 8 Charaktere = 48 Samples`; Speicherziel `≤ 8 MB` insgesamt (bei ~80–150 kB pro Sample). Dauer je Sample `≤ 1,5 s`.

## 5. Edge Cases

1. **Zwei Spieler wählen denselben Charakter:** Die UI blockiert die zweite Auswahl hart (Kachel gesperrt, Meldung "Bereits gewählt"). Es ist kein Fall definiert, in dem Duplikate erlaubt sind — der Tuning-Knob (Sektion 7) ist der einzige Weg, dies zu ändern, und muss dann die Injektivitätsformel (4.2) ersetzen.
2. **Weniger als 2 bestätigte Spieler bei Auswahlende:** Das Spiel startet nicht. Die UI zeigt eine Meldung und wartet auf weitere Bestätigungen beziehungsweise Rückkehr zur Lobby.
3. **Mehr als 8 Spieler versuchen beizutreten:** Die Lobby lehnt ab; der 9. Spieler sieht "Lobby voll". Keine automatische Erweiterung.
4. **Charakter-Plugin ohne `character.tscn`:** Der Ordner wird vom Loader übersprungen, eine Warnung wird geloggt. Der Charakter fehlt in der Auswahl.
5. **`character.tscn` ohne `character.gd`-Skript:** Der Loader überspringt den Charakter mit Warnung (Verhalten der Basisklasse). Kein Absturz, kein halbgeladener Zustand.
6. **Charakter-Ordner mit ungültigem Namen (z. B. Umlaute, Leerzeichen):** Der Ordner wird geladen, aber die ID muss auf den kanonischen Namensraum normalisiert werden; kann die ID nicht normalisiert werden, wird der Charakter übersprungen und gewarnt.
7. **Gleiche ID in zwei Ordnern:** Der zuerst entdeckte Ordner gewinnt, der zweite wird mit Warnung ignoriert. Die Auswahl enthält die ID genau einmal.
8. **Instanziierungsfehler beim Laden der Auswahl-Vorschau:** Die Vorschau fällt auf `splash.png` zurück; das 3D-Modell wird nicht angezeigt, die Auswahl bleibt funktional. Der Fehler wird geloggt.
9. **`freeze_animation()` während `victory`:** Die Pose friert ein und wird beim Fortsetzen beendet. Die Siegerehrung darf nicht an einer eingefrorenen Pose hängen bleiben; das System setzt nach `resume_animation()` auf den letzten Zustand des Spiels zurück.
10. **Animation fehlt zur Laufzeit:** Ruft ein System eine nicht existierende Animation auf, darf kein Crash entstehen. Die Basisklasse fällt auf `idle` zurück und loggt einen Fehler (Verhalten in `character.gd`).
11. **Charakter in Minispielen:** Minispiele instanziieren denselben Charakter-Nodes; die identische Trefferbox (3.6) garantiert faires Verhalten. Animationen wie `punch`/`kick`/`jump` werden nach Minispiel-Vertrag verwendet (siehe `minigame-architecture.md`).
12. **Alle 8 Charaktere im Spiel (P = 8):** Alle Charaktere sind vergeben; die Auswahl ist vollständig gesperrt. Kein freier Charakter existiert für Nachzügler — diese müssen in der Lobby warten oder einen anderen Slot belegen.
13. **Farbfehlsichtige Spieler:** Die Unterscheidung funktioniert über Silhouette und Form zusätzlich zur Farbe. Ein rein farbcodierter Zustand (z. B. "dein Charakter ist der Türkise") ist verboten (siehe `ui-accessibility.md`).
14. **Voice-Lines deaktiviert (Budget):** Alle Voice-Trigger spielen stattdessen generische UI-/SFX-Feedback-Sounds. Kein Charakter hat einen spielmechanischen Nachteil dadurch.
15. **Charakter auf fremder Heimat-Insel:** Kein Effekt. Der Heimat-Bezug ist rein narrativ (Einleitungstexte, Flavor).

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `characters-overview.md` | Art | Verwendung |
|----------------------------------------|-----|------------|
| `common/scripts/character.gd` | Code | Definiert die Basisklasse und den 4-Methoden-API-Vertrag (3.5.2). |
| `common/scripts/loader/character_loader.gd` | Code | Definiert den Plugin-Ladevertrag, Pflichtdateien und Entdeckung (3.3). |
| `common/scripts/loader/plugin_system.gd` | Code | Liefert den Verzeichnisscan, der die Charakter-Ordner findet (3.3.4). |
| `design/gdd/game-concept.md` | Quelle | Liefert den Roster (8 Arenians), Design-Pillars, Art-Style (High Saturation, Cartoon/Toy). |
| `design/gdd/technical-fork-strategy.md` | Peer | Legt fest, dass STP-Charaktere nicht als Arenians übernommen werden (3.11.1). |
| `design/gdd/ui-character-select.md` | Peer | Definiert den Auswahlbildschirm, der diesen Vertrag nutzt (3.4). |
| `design/gdd/ui-hud.md` | Peer | Verwendet `icon.png` und Charakternamen (3.7). |
| `design/gdd/audio-voice.md` | Peer | Steuert, ob Voice-Lines aktiv sind, und die Wiedergabe-Queue (3.9). |
| `design/gdd/dice-movement.md` | Peer | Definiert die Fortbewegungszeit pro Feld, die alle Charaktere teilen (3.1.2). |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `character-brix.md` … `character-momo.md` (8 Kapitel) | Jedes Einzelkapitel muss diesen Vertrag erfüllen (12 Animationen, Maße, Porträt, API). |
| Board-System (`board-architecture.md`) | Instanziiert Charakter-Nodes auf Feldern und bewegt sie Feld zu Feld. |
| Minigame-System (`minigame-architecture.md`) | Nutzt dieselben Charakter-Nodes und die Standard-Trefferbox. |
| Siegerehrung (`victory-conditions.md`) | Löst die `victory`-Animation aus (3.8). |
| UI-System (`ui-character-select.md`, `ui-hud.md`) | Zeigt Porträts, Namen und Animationen aus diesem Vertrag. |
| Audio-System (`audio-voice.md`) | Spielt die optionalen Voice-Lines nach diesem Vertrag ab. |
| Ladebildschirm | Zeigt `splash.png` und den Strategie-Tipp (3.10). |

### 6.3 Bidirektionalität

Jedes in 6.1 und 6.2 genannte Kapitel muss bei seiner Erstellung einen Rückverweis auf dieses Kapitel enthalten. Insbesondere: Die 8 Charakter-Einzelkapitel verweisen in Sektion 6 auf `characters-overview.md`, und dieses Kapitel verweist auf sie in 6.2. Wird der Animationsvertrag (3.5) geändert, müssen alle 8 Einzelkapitel und `character.gd` synchron aktualisiert werden.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Duplikat-Charaktere erlaubt | Regel | `verboten` / `erlaubt` | `verboten` | Bestimmt, ob zwei Spieler denselben Arenian wählen dürfen. `erlaubt` verletzt die Injektivitätsformel (4.2) und erfordert eine Farb-/Namensdisambiguierung im HUD (z. B. "Pip A", "Pip B"). |
| Modellhöhe `H` | Kurve | 1,08–1,32 Einheiten | 1,2 | Rein visuelle Skalierung. Bleibt innerhalb der Trefferbox-Toleranz; Änderung außerhalb 1,08–1,32 ist ein Vertragsbruch. |
| Trefferbox-Radius | Kurve | 0,55–0,65 | 0,6 | Wirkt auf Minispiel-Physik und Feld-Checks. Muss für alle 8 Charaktere identisch bleiben. |
| Fortbewegungszeit pro Feld | Kurve | 1,8–3,0 s | 2,4 s | Spielfluss-Gefühl; wirkt auf alle Charaktere gleich. Kein Per-Charakter-Knob. |
| Animationsdauern (je Typ) | Feel | Bereiche aus 3.5 | Mittelwert je Zeile | Je länger Happy/Sad, desto theatralischer; je länger Walk/Run, desto zäher die Bewegung. Muss die identische Fortbewegungszeit (3.1.2) einhalten. |
| Minimale Farbdistanz `d_ij` | Kurve | 0,15–0,35 | 0,20 | Schwelle für Verwechslungsfreiheit neuer Charakterfarben. Höher = strengere Farbtrennung. |
| Ladezeit-Budget je Charakter | Kurve | 100–250 ms | 150 ms | Performance-Gate; höher erlaubt aufwendigere Modelle, verlängert aber Ladebildschirme. |
| Voice aktiviert | Gate | `an` / `aus` | `aus` (Budget-abhängig) | Schaltet die 6 Samples je Charakter ein; `aus` nutzt generische SFX (3.9). |
| Voice-Lautstärke | Feel | −9 bis 0 dBFS Ziel | −3 dBFS | Einheitliche Wahrnehmbarkeit; keine Charakterstimme darf lauter als eine andere sein. |

Alle Knobs sind spielmechanisch neutral, solange sie **für alle 8 Charaktere identisch** angewendet werden. Ein Per-Charakter-Knob, der Leistung verändert, ist durch die Balance-Philosophie (3.1) verboten.

## 8. Acceptance Criteria

Ein QA-Tester (oder CI-Hook) kann die folgenden Prüfungen automatisiert oder manuell ausführen:

1. **Roster-Vollständigkeit:** Genau die 8 Arenians (Brix, Nixie, Pip, Koko, Tiko, Bolt, Bloom, Momo) erscheinen in der Auswahl, keine STP-Legacy-Charaktere. PASS/FAIL.
2. **Plugin-Laden:** Für jede der 8 Charakter-IDs existiert `plugins/characters/[id]/character.tscn` mit `character.gd` am Root-Node; `CharacterLoader.get_loaded_characters()` liefert genau diese 8 IDs. PASS/FAIL.
3. **Animationsvertrag:** Jede der 12 Pflichtanimationen (3.5) ist für alle 8 Charaktere vorhanden und per `play_animation` aufrufbar; `C = 100` für alle. PASS/FAIL.
4. **API-Funktionstest:** `play_animation`, `jump_to_animation`, `freeze_animation`, `resume_animation` verhalten sich wie spezifiziert (weicher Übergang, harter Sprung, Einfrieren ohne Zurückfallen, Fortsetzen an gleicher Stelle). PASS/FAIL.
5. **Größenprüfung:** Für alle 8 Charaktere gilt `1,08 ≤ H ≤ 1,32`; Messung im Editor an der Fuß-zu-Kopf-Bounding-Box des Modells. PASS/FAIL.
6. **Trefferbox-Gleichheit:** Alle 8 Charaktere besitzen eine Trefferbox innerhalb der Toleranz aus 4.5; die Parameter sind identisch. PASS/FAIL.
7. **Balance-Gleichheit:** Ein automatischer Vergleich der exportierten Gameplay-Parameter (Bewegungsgeschwindigkeit, Sprunghöhe, Kollisionsmaske) über alle 8 Charaktere zeigt keinerlei Unterschied. PASS/FAIL.
8. **Porträts:** `icon.png` (256×256) und `splash.png` (1024×1024) existieren für alle 8; Icon ist bei 32-Pixel-Downscale erkennbar; Porträt und 3D-Modell zeigen dieselbe Figur/Farbwelt. PASS/FAIL.
9. **Siegerpose:** Bei einem simulierten Spielgewinn spielt jeder Charakter seine `victory`-Animation (2–4 s); die Kamera schwenkt auf den Sieger. PASS/FAIL.
10. **Duplikat-Regel:** Bei 2–8 Spielern ist es unmöglich, einen bereits gewählten Charakter erneut zu bestätigen; die UI blockiert dies. PASS/FAIL.
11. **Farbdistanz:** Für alle Primärfarbenpaare gilt `d_ij ≥ 0,20` (4.6). PASS/FAIL.
12. **Ladezeit:** `t_Charakter ≤ 150 ms` je Charakter auf Referenz-Hardware; Gesamtladezeit der Auswahl inklusive aller 8 Modelle ≤ 2 s. PASS/FAIL.
13. **Fehlerresistenz:** Entfernt man während eines Tests ein `character.tscn`, startet das Spiel ohne Absturz, der betroffene Charakter fehlt in der Auswahl, eine Warnung wurde geloggt. PASS/FAIL.
14. **Voice-optional:** Bei deaktivierter Sprachausgabe spielen alle Voice-Trigger generische SFX; kein Funktionsverlust. Bei aktivierter Sprachausgabe existieren alle 6 Pflicht-Samples je Charakter. PASS/FAIL.
15. **Erlebbar (Experiential):** Ein neuer Spieler kann in unter 30 Sekunden in der Auswahl einen Charakter wählen und bestätigen, ohne die Regeln zu kennen. PASS/FAIL.
