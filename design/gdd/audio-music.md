# Musik — Party Arena Game Bible

> **Teil:** 8 — Audio (8.2)
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/audio-overview.md, design/gdd/world-overview.md, design/gdd/narrative-arena-star.md, design/gdd/core-loop.md

---

## 1. Overview

Dieses Kapitel spezifiziert die gesamte Musik von Party Arena: das Hauptmenü-Thema, alle acht Insel-/Board-Themen (sieben Inseln plus Sternenzitadelle), die Minispiel-Musik (Countdown, Action-Loop, Ergebnis-Fanfare), das Sieg-Thema sowie das optionale System dynamischer Intensitäts-Layer. Jedes Musikstück wird mit Titel, BPM, Taktart, Tonart, Besetzung, Stimmung, Form (Taktplan) und Loop-Verhalten definiert. Die Musik folgt der Insel-Identität aus `world-overview.md`: Jede Insel hat einen eigenen Musikstil, der sie auf einen Blick — oder besser: auf ein Hören — wiedererkennbar macht (Design-Pfeiler „Wiedererkennbar"). Die Musik wird über den Musik-Bus abgespielt (`audio-overview.md` Abschnitt 3.1), über die Crossfade-Zeiten aus `audio-overview.md` Abschnitt 3.8 übergeblendet und durch das Ducking aus `audio-overview.md` Abschnitt 3.4 zugunsten von Stimme und Popups abgesenkt.

Alle Musik-Dateien sind Ogg-Vorbis q=4 (~128 kbps), Stereo, 48 kHz (`audio-overview.md` Abschnitt 3.2). Dieses Kapitel ist die einzige maßgebliche Quelle für die musikalischen Inhalte; Abweichungen in anderen Kapiteln sind zu korrigieren oder als Design-Entscheidung zu dokumentieren.

## 2. Player Fantasy

Die Musik macht die Party Arena zu einer **musikalischen Reise durch ein Spielzeug-Paradies**: Jede Insel klingt so, wie sie aussieht. Am Sonnenstrand wiegen sich Steel Drums im Hawaii-Chill, im Zuckerwald dreht sich ein Bonbon-Walzer, über Wolkenwerk schweben Harfen-Arpeggien, auf dem Frostgipfel glitzern kristalline Celesta-Töne, im Dschungeltempel pulsieren Bongos, in der Mechanik-Stadt tickt ein präzises Zahnrad-Ballett, und auf der Sternenzitadelle braust ein volles Orchester mit Chor. Der Spieler erlebt die Inselauswahl als **Schaufensterbummel durch Klangwelten**: Schon im Menü kündigt die Musik an, was einen erwartet.

Die zentrale emotionale Verheißung: **„Die Musik feiert mit dir."** Sie beginnt ruhig und einladend (Menü), trägt die Partie mit einem lebendigen Board-Thema, beschleunigt beim Minispiel-Start (Countdown → Action-Loop) und gipfelt in einer dramatischen Siegerehrung. Auch Niederlagen klingen nie bedrohlich — die Musik bleibt durchgehend verspielt und warm, ganz im Sinne des positiven Tons von ArenaStar (`narrative-arena-star.md`). Das Hauptmenü-Thema „ArenaStars Einladung" ist die akustische Visitenkarte des Spiels: Wer es hört, soll sofort wissen, dass hier eine fröhliche, überzeichnete Spielshow beginnt.

## 3. Detailed Rules

### 3.1 Musik-System-Überblick

1. **Ein Musik-Stream pro Spielzustand.** Es erklingt immer genau ein Musikstück: Menü-Thema im Menü, Insel-Thema auf dem Board, Countdown + Action-Loop im Minispiel, Sieg-Thema in der Siegerehrung. Während eines Crossfades (Maximaldauer 1,5 s, `audio-overview.md` Abschnitt 3.8) erklingen zwei Streams gleichzeitig; danach ist wieder genau einer aktiv.
2. **Loop-Verhalten:** Board-Themen und das Menü-Thema sind nahtlose Loops. Ein Loop ist dann nahtlos, wenn der Übergang vom letzten zum ersten Takt weder einen Sprung in Lautstärke noch einen hörbaren Phasenbruch erzeugt (Abschnitt 3.8).
3. **Dynamische Musik:** Das Ducking (Kommentar/Popup/Stimme) senkt die Musik zeitweise ab (`audio-overview.md` Abschnitt 3.4). Die Musik selbst ändert ihre Struktur dadurch nicht.
4. **Insel-Intro:** Während des 5-Sekunden-Insel-Intros (`world-overview.md` Abschnitt 3.6) erklingt das Insel-Thema ab dem ersten Takt; der Insel-Titel-Einblender ist mit dem musikalischen Intro-Segment synchronisiert (Abschnitt 3.4 dieses Kapitels).
5. **ArenaStar-Leuchten:** Das Leuchten des ArenaStar-Modells pulsiert mit dem Musiktakt (100 BPM Default ohne Musik, `narrative-arena-star.md` Abschnitt 3.6.3). Die Musik-Systeme liefern dafür einen BPM-Wert (Abschnitt 4.1).

### 3.2 Hauptmenü-Thema: „ArenaStars Einladung"

| Eigenschaft | Wert |
|-------------|------|
| Einsatz | Hauptmenü (`ui-mainmenu.md`) |
| Dauer (Loop) | 90 s |
| BPM | 120 |
| Taktart | 2/2 (alla breve) |
| Tonart | C-Dur |
| Besetzung | Kleine Marching Band: Trompete, Klarinette, Snare, Tuba |
| Stimmung | Einladend, verspielt, feierlich |

Form (Taktplan, 90 Takte):

| Abschnitt | Takte | Beschreibung |
|-----------|-------|--------------|
| Intro | 8 | Snare-Wirbel mit Tuba-Fundament; Trompete spielt Fanfare-Motiv; lädt ein. |
| A | 16 | Hauptmelodie (Trompete), Klarinette Gegenstimme, Tuba Bass, Snare marschiert. |
| B | 16 | Kontrastteil; Klarinette übernimmt die Melodie, Trompete antwortet (Call & Response). |
| A' | 16 | Wiederholung von A mit leicht erweiterter Instrumentierung (Tutti). |
| Bridge | 8 | Reduzierter Satz (Tuba + Snare), Spannungsaufbau auf die Schluss-A-Wiederholung. |
| A | 16 | Finale A-Wiederholung, voller Satz, feierlich. |
| Outro | 10 | Fanfare-Schluss (Trompete, Tuba-Kadenz C–F–G–C), Snare-Ritardando, nahtloser Loop-Rücksprung ins Intro. |

Hinweis zur Form: Bei 120 BPM im 2/2-Takt dauert 1 Takt exakt 1 Sekunde; die 90-Takte-Form ergibt damit exakt 90 s Loop-Dauer. Der Outro-Endpunkt ist so komponiert, dass Takt 90 nahtlos in Takt 1 (Intro) übergeht.

### 3.3 Insel-/Board-Themen (8 Themen)

Jede Insel hat genau ein Board-Thema. Die Themen sind nahtlose Loops mit einer Zieldauer von 120 s (± 10 %), Ausnahme Sternenzitadelle (durchkomponiert, Abschnitt 3.3.8).

| Insel | Titel | BPM | Taktart | Tonart | Stil / Stimmung |
|-------|-------|-----|---------|--------|-----------------|
| Sonnenstrand | Wellen-Tanz | 110 | 4/4 | D-Dur | Steel Drums, Ukulele, Marimba; Chill/Hawaii |
| Zuckerwald | Bonbon-Walzer | 120 | 3/4 | F-Dur | Glockenspiel, Fagott, Celesta; Süß/Walzer |
| Wolkenwerk | Wolken-Schweben | 100 | 4/4 | F-Lydisch | Harfe, Flöte, Streicher-Pads; Schwebend/Ambient |
| Frostgipfel | Eis-Kristall | 90 | 4/4 | d-Moll | Celesta, Tremolo-Strings, Glasharmonika; Kristallin/Kalt |
| Dschungeltempel | Tempel-Geheimnis | 130 | 4/4 | e-Phrygisch | Marimba, Bongos, Didgeridoo; Geheimnisvoll/Pulsierend |
| Mechanik-Stadt | Zahnrad-Ballett | 140 | 4/4 | G-Mixolydisch | Xylophon, Marimba, Tuba, Metronom-Spur; Präzise/Mechanisch |
| Sternenzitadelle | Sternen-Thron | 80→160 | 4/4 | C-Dur→E-Dur | Volle Orchester + 8-stimmiger Chor; Heroisch/Feierlich |

#### 3.3.1 Sonnenstrand — „Wellen-Tanz" (110 BPM, D-Dur)

| Eigenschaft | Wert |
|-------------|------|
| Besetzung | Steel Drums (Lead), Ukulele (Begleitung), Marimba (Zweitstimme), leichte Percussion (Shaker) |
| Stimmung | Entspannt, sonnig, Hawaii-Urlaub |
| Zieldauer | 122 s (56 Takte × 2,1818 s) |

Form (56 Takte): Intro(4) → A(16) → B(16) → A'(16) → Outro(4).

- Intro: Ukulele-Schlagmuster (Viertel), Shaker, Steel Drum setzt das Hauptmotiv an.
- A: Steel-Drum-Melodie (D-Dur-Pentatonik), Marimba antwortet im Wechsel.
- B: Kontrastteil mit ruhigerer Ukulele-Begleitung, Steel Drum spielt lange Töne.
- A': Wiederholung von A mit Marimba-Konterpunkt.
- Outro: kurze Schlussphrase, die nahtlos in das Intro-Motiv zurückführt.

#### 3.3.2 Zuckerwald — „Bonbon-Walzer" (120 BPM, F-Dur, 3/4)

| Eigenschaft | Wert |
|-------------|------|
| Besetzung | Glockenspiel (Melodie), Fagott (Bass), Celesta (Zweittstimme/Füllung) |
| Stimmung | Süß, tänzerisch, Walzer |
| Zieldauer | 120 s (80 Takte × 1,5 s) |

Form (80 Takte, 3/4): Intro(8) → A(24) → B(16) → A'(24) → Outro(8).

- Intro: Celesta-Arpeggien (F-Dur), Fagott setzt den Walzer-Bass (Grundton auf 1, Quinten auf 2–3) ein.
- A: Glockenspiel-Melodie im Walzer-Dreiertakt, Celesta begleitet mit gebrochenen Akkorden.
- B: Fagott führt eine tiefere, rundere Melodie; Glockenspiel antwortet („Bonbon-Dialog").
- A': A-Wiederholung mit Celesta-Verzierung.
- Outro: Walzer-Schlusskadenz, nahtlos zurück ins Intro.

#### 3.3.3 Wolkenwerk — „Wolken-Schweben" (100 BPM, F-Lydisch)

| Eigenschaft | Wert |
|-------------|------|
| Besetzung | Harfe (Arpeggien), Flöte (Melodie), Streicher-Pads |
| Stimmung | Schwebend, leicht, ambient |
| Zieldauer | 120 s (50 Takte × 2,4 s) |

Form (50 Takte): Intro(4) → A(16) → B(16) → A'(8) → Outro(6).

- Intro: Streicher-Pad (F-Lydisch, schwebend), Harfe setzt mit leisen Arpeggien ein.
- A: Flöten-Melodie über Harfen-Arpeggien; keine Perkussion.
- B: Streicher übernehmen die Melodie, Flöte schwebt als Gegenstimme; ruhiger Höhepunkt.
- A': verkürzte A-Wiederholung (8 Takte).
- Outro: Harfe arpeggiert aus, Pad klingt nach; nahtloser Rücksprung ins Intro.

Hinweis: Die lydische Quart (H statt B über F) ist das wiedererkennbare Intervall des Themas.

#### 3.3.4 Frostgipfel — „Eis-Kristall" (90 BPM, d-Moll)

| Eigenschaft | Wert |
|-------------|------|
| Besetzung | Celesta (Melodie), Tremolo-Strings, Glasharmonika (Glissandi) |
| Stimmung | Kristallin, kalt, klar |
| Zieldauer | 120 s (45 Takte × 2,6667 s) |

Form (45 Takte): Intro(8) → A(8) → B(16) → A'(8) → Outro(5).

- Intro: Celesta-Einzeltöne wie Eiskristalle, Tremolo-Strings als kalter Teppich.
- A: Celesta-Melodie (d-Moll, leicht melancholisch), Glasharmonika-Glissandi als Eis-Funken.
- B: Tremolo-Strings führen die Melodie, Celesta begleitet; dynamisch etwas dichter.
- A': A-Wiederholung, leiser.
- Outro: 5-taktiger Ausklang (kürzere Wiederholung des Intro-Motivs), nahtloser Loop.

#### 3.3.5 Dschungeltempel — „Tempel-Geheimnis" (130 BPM, e-Phrygisch)

| Eigenschaft | Wert |
|-------------|------|
| Besetzung | Marimba (Melodie), Bongos (Rhythmus), Didgeridoo (Bass-Drohne) |
| Stimmung | Geheimnisvoll, pulsierend, archaisch |
| Zieldauer | 120 s (65 Takte × 1,846 s) |

Form (65 Takte): Intro(4) → A(16) → B(16) → A'(16) → B'(8) → Outro(5).

- Intro: Bongo-Puls (tiefe Konga-Töne), Didgeridoo-Drohne auf E, Marimba setzt ein Motiv ein.
- A: Marimba-Melodie (e-Phrygisch: F natürliches → geheimnisvoller Halbton), Bongos treiben.
- B: Ruhigerer Mittelteil, Marimba und Didgeridoo im Dialog, Bongos reduzieren auf Grundschlag.
- A': A-Wiederholung, dichter.
- B': verkürzte B-Wiederholung (8 Takte), Spannungsaufbau.
- Outro: 5-taktiger Abschluss, Didgeridoo-Drohne klingt nach, Loop-Rücksprung.

#### 3.3.6 Mechanik-Stadt — „Zahnrad-Ballett" (140 BPM, G-Mixolydisch)

| Eigenschaft | Wert |
|-------------|------|
| Besetzung | Xylophon (Melodie), Marimba (Begleitung), Tuba (Bass), Metronom-Spur (Maschinen-Puls) |
| Stimmung | Präzise, mechanisch, spieluhr-artig |
| Zieldauer | 120 s (70 Takte × 1,714 s) |

Form (70 Takte): Intro(8) → A(16) → B(16) → C(16) → B'(8) → Outro(6).

- Intro: Metronom-Spur (durchgehender 8tel-Puls wie ein Zahnrad), Tuba setzt ein Maschinen-Ostinato ein.
- A: Xylophon-Melodie (G-Mixolydisch: F# → heller, mechanischer Klang), Marimba begleitet.
- B: Tuba führt eine schwere, „schwerfällige" Phrase; Xylophon antwortet mit kurzen Staccato-Figuren.
- C: Dichter Satz, alle Instrumente im 8tel-Puls; „Ballett der Zahnräder".
- B': verkürzte B-Wiederholung (8 Takte).
- Outro: Maschinen-Puls läuft aus, Tuba-Schluss, nahtloser Rücksprung ins Intro.

Hinweis: Die Metronom-Spur ist ein eigener Klang (trockener Holzblock-Klick), der bewusst als „Maschine" erkennbar bleibt.

#### 3.3.7 Sternenzitadelle — „Sternen-Thron" (80→160 BPM, C-Dur→E-Dur)

| Eigenschaft | Wert |
|-------------|------|
| Besetzung | Volle Orchesterbesetzung (Streicher, Blech, Holz, Pauken, Becken) + 8-stimmiger Chor (SATB × 2, „Ahhh"-Vokale) |
| Stimmung | Heroisch, feierlich, triumphierend |
| Dauer | 180 s, durchkomponiert (kein nahtloser Loop) |

**Struktur (durchkomponiert in drei Sätzen):**

| Satz | Zeitfenster | Ziel-BPM | Beschreibung |
|------|-------------|----------|--------------|
| Satz A | 0–60 s | 80 | Ruhig-erhaben; Streicher + Chor („Ahhh"), Pauken nur dezent. |
| Satz B | 60–120 s | 120 | Erhoben; Blech setzt ein, Chor voller, marcato. |
| Satz C | 120–180 s | 160 | Triumphal; volles Orchester + 8-stimmiger Chor, Becken, große Schlusssteigerung. |

Regeln:

1. **Tempo-Kopplung an die Runde:** Das tatsächlich erklingende Tempo wird der aktuellen Runde zugeordnet (Tuning-Knob, Abschnitt 7). In Runde 1–3 steht Satz A im Vordergrund, Runde 4–7 Satz B, Runde 8–10 Satz C. Da die Partie auf der Sternenzitadelle 8–10 Runden dauert, steigt das wahrgenommene Tempo mit der Runde („BPM steigt mit Runde"). Die Sätze sind an Phrasengrenzen (8 Takte) sauber aneinanderfügbar; ein Satzwechsel erfolgt ausschließlich an einer Phrasengrenze mit einer Überleitung von 2 s.
2. **Modulation C-Dur → E-Dur bei Feld 20:** Sobald der führende Spieler Feld 20 erreicht oder passiert (erstmals in der Partie), moduliert die Musik von C-Dur nach E-Dur (große Terz nach oben, dramatischer Pivot). Die Modulation ist in jedem Satz als komponierter Pivot-Takt eingebaut; nach der Aktivierung bleibt E-Dur für den Rest der Partie bestehen (kein Zurückmodulieren). Wird Feld 20 nie erreicht (praktisch ausgeschlossen, da Feld 20 auf dem Hauptpfad liegt), entfällt die Modulation.
3. **Kein nahtloser Loop:** Endet das Stück (nach 180 s bzw. nach Satz C), folgt eine **Atempause von 1,0 s**, danach startet das Stück neu. Wird das Board vorzeitig beendet (letzte Runde), endet die Musik mit dem letzten Satz und geht in den Victory-Crossfade über (1,5 s, `audio-overview.md` Abschnitt 3.8).
4. **Chor:** Der 8-stimmige Chor singt ausschließlich „Ahhh"-Vokale (kein Text). Ab Satz B ist der Chor durchgehend präsent; in Satz C in voller Stärke.

### 3.4 Minispiel-Musik

#### 3.4.1 Countdown — „3-2-1-LOS"

| Eigenschaft | Wert |
|-------------|------|
| Einsatz | Minispiel-Start (`minigame-architecture.md`) |
| Dauer | 4,0 s (exakt) |
| Inhalt | 3 taktgenaue Töne (C4, E4, G4 aufsteigend) + Fanfare (C-Dur-Kadenz) |

Regeln:

1. **Zeitplan:** Ton 1 (C4) bei t = 0 s, Ton 2 (E4) bei t = 1 s, Ton 3 (G4) bei t = 2 s, LOS-Fanfare bei t = 3 s; Ende bei t = 4 s. Jeder Ton ist ein kurzer, heller Blip (0,3 s, Synthesizer-Fanfare, `audio-sfx.md` Abschnitt 3.6).
2. **Taktgenau:** Die Töne sind auf die Schläge eines 120-BPM-Pulses gelegt (1 Schlag = 0,5 s; jeder Ton fällt auf einen geraden Schlag), sodass sie als zählend empfunden werden.
3. **LOS-Fanfare:** C-Dur-Kadenz (C–F–G–C) als kurzer Tusch (1,0 s), Blech/Streicher-Unisono.
4. **Wiederholung:** Der Countdown wird pro Minispiel genau einmal abgespielt. Kann das Minispiel nicht starten (Abbruch), wird der Countdown abgebrochen und die Musik kehrt ins Board-Thema zurück (Crossfade 0,3 s).

#### 3.4.2 Action-Loop (30 s, 150 BPM)

| Eigenschaft | Wert |
|-------------|------|
| Einsatz | Während des Minispiels (`minigame-architecture.md`) |
| Dauer (Loop) | 30 s (± 1 s) |
| BPM | 150 |
| Fundament | Perkussiv: Kick auf 1 und 3, Snare/Clap auf 2 und 4, Hi-Hats in Achteln |

Der Basis-Loop ist ein perkussives Fundament, das **pro Minispiel-Kategorie** angepasst wird (`minigame-categories.md`). Die Kategorie-Varianten modulieren die oberen Schichten, nicht das Grundtempo:

| Kategorie | Anpassung des Basis-Loops |
|-----------|---------------------------|
| Geschicklichkeit | Leicht und beschwingt; helle Synth-Arpeggios, verspielte Melodie-Fragmente. |
| Reaktion | Schnelle Hi-Hats (16tel), hohe Energie, weniger Melodie, mehr Treiber. |
| Puzzle/Logik | Leise und sanft (−4 dB relativ zum Basis-Loop); reduzierte Perkussion, warme Pads, keine Ablenkung. |
| Rechnen/Wort | Neutral; deutlicher Metronom-Klick (Holzblock) auf jedem Schlag, unterstützt Zähl-Arbeit. |
| Kooperation | Warm und hymnisch; breite Akkorde, Bläser/Streicher-Fläche, gemeinschaftsstiftend. |

Regeln:

1. **Loop-Dauer 30 s (± 1 s):** Die Phrasierung wird als 18 Takte plus Auftakt (2 Schläge) realisiert; der Loop-Endpunkt geht nahtlos in den Anfang über.
2. **Ein Action-Loop pro Minispiel.** Das Minispiel wählt die Kategorie-Variante; es gibt keinen Mid-Minigame-Wechsel.
3. **Verhältnis zum Countdown:** Der Action-Loop beginnt exakt bei t = 0 s des Minispiels; der Countdown (4 s) läuft davor. Übergang Countdown → Action-Loop: Die LOS-Fanfare endet bei t = 4 s, der Action-Loop setzt unmittelbar danach ein (kein Crossfade, harter Schnitt als Start-Knalleffekt).

#### 3.4.3 Ergebnis-Fanfare (10 s, 3 Stufen)

| Eigenschaft | Wert |
|-------------|------|
| Einsatz | Nach Minispiel-Ende, während der Ergebnis-Präsentation |
| Dauer | 10,0 s |
| Stufen | 3, abhängig von der Platzierung des Spielers |

| Platzierung | Stufe | Klang | Charakter |
|-------------|-------|-------|-----------|
| Platz 1 | Heroisch | Trompeten-Fanfare (Es-Dur), voller Blechsatz | Triumph, Sieg |
| Platz 2–3 | Fröhlich | Flöten-Melodie (C-Dur), leichtes Blech | Zufrieden, aufmunternd |
| Platz 4 und schlechter | Neutral | Sanfte, kurze Phrase (Streicher, keine Fanfare) | Trost, Neutral |

Regeln:

1. **Je Platzierung genau eine Stufe.** Bei Team-Minigames (`field-minigame.md`) gilt die Stufe für das Team: Das Siegerteam hört die heroische Stufe, das Verliererteam die neutrale Stufe (2v2: es gibt keinen „Platz 2–3"-Fall für Teams).
2. **Keine Wertung im Klang:** Die neutrale Stufe klingt nicht negativ, sondern schlicht und tröstlich — sie enthält keine absteigenden oder dissonanten Elemente.
3. **Übergang:** Die Ergebnis-Fanfare folgt auf das Spielende-Signal (`audio-sfx.md` Abschnitt 3.6, tiefer Gong). Nach der Ergebnis-Präsentation kehrt die Musik ins Board-Thema zurück (Crossfade 0,3 s).

### 3.5 Sieg-Thema: „Sternen-Krönung"

| Eigenschaft | Wert |
|-------------|------|
| Einsatz | Siegerehrung (`victory-conditions.md`) |
| Dauer | 30 s |
| BPM | 90 |
| Taktart | 3/4 |
| Tonart | Es-Dur |
| Besetzung | Chor („Ahhh") + Orchester |
| Stimmung | Feierlich, krönend |

Form (15 Takte × 2 s = 30 s):

| Abschnitt | Takte | Dauer | Beschreibung |
|-----------|-------|-------|--------------|
| Fanfare | 2 | 4 s | Blech-Fanfare (Es-Dur), Chor setzt mit „Ahhh" ein. |
| Thema | 8 | 16 s | Volles Thema: Chor + Streicher + Blech; die Melodie krönt den Sieger. |
| Krönungs-Fanfare | 5 | 10 s | Steigerung mit Pauken und Becken; Schlussakkord mit Chor. |

Regeln:

1. **Einmalig und endgültig:** Das Sieg-Thema wird genau einmal pro Partie abgespielt, beginnend mit dem Victory-Crossfade (1,5 s, `audio-overview.md` Abschnitt 3.8). Es wird nicht geloopt.
2. **Chor ohne Text:** Der Chor singt ausschließlich „Ahhh"-Vokale; der Name des Siegers wird von ArenaStar gesprochen (`audio-voice.md` Abschnitt 3.2, Kategorie Sieges-Zeremonie), nicht gesungen.
3. **Platzierungs-Anzeige:** Die Reihenfolge der Platzierungen wird während des Themas eingeblendet; das Thema dauert lang genug (30 s), um alle Platzierungen zu präsentieren (Referenz: 2–8 Spieler, `victory-conditions.md`).
4. **Nach dem Sieg-Thema** kehrt die Musik ins Menü zurück (Crossfade 1,0 s).

### 3.6 Dynamische Intensitäts-Layer (optional, Post-Launch)

Zusätzlich zu den statischen Board-Themen ist ein System dynamischer Intensitäts-Layer spezifiziert (optional, Post-Launch):

1. **Drei Layer je Insel-Thema:** `ruhig`, `normal`, `intensiv`. Alle drei Layer teilen sich Tonart, BPM, Form und Loop-Punkte; sie unterscheiden sich in der Instrumentierungsdichte und Dynamik:
   - `ruhig`: reduzierte Besetzung (z. B. nur Ukulele + Shaker), leiser.
   - `normal`: die volle Besetzung aus Abschnitt 3.3.
   - `intensiv`: volle Besetzung plus zusätzliche Rhythmus- und Füllstimmen, höhere Dynamik.
2. **Layer-Zuordnung über die Runde:** Runde 1–3 → `ruhig`, Runde 4–7 → `normal`, Runde 8–10 → `intensiv`. Die Zuordnung gilt für die Sternenzitadelle nur eingeschränkt (dort regelt die Satz-Kopplung aus 3.3.7 das Tempo; die Layer entfallen).
3. **Wechselzeitpunkt:** Der Layer-Wechsel erfolgt ausschließlich in der Rundenende-Wartung (`board-architecture.md` Abschnitt 3.12), nie mitten in einem Spielerzug.
4. **Wechselübergang:** Der Wechsel zwischen Layern nutzt einen Crossfade von 1,0 s (gleiche Kurven wie `audio-overview.md` Abschnitt 3.8).
5. **Post-Launch-Status:** Dieses System ist optional und nicht Teil des Alpha-Umfangs. Die Board-Themen werden so komponiert, dass die Layer-Bearbeitung nachträglich möglich ist (getrennte Stems, gleiche Loop-Punkte).

### 3.7 Loop-Spezifikation und Qualität

1. **Nahtloser Loop:** Für alle Loops (Menü-Thema, Board-Themen, Action-Loop) gilt: Der Übergang vom letzten zum ersten Takt ist frei von hörbaren Lautstärkesprüngen, Phasenbrüchen oder Hall-Abrissen. Die Loop-Punkte werden im Ogg-Export als exakte Sample-Positionen gesetzt (keine Interpolation).
2. **Loop-Punkt-Kontrolle:** Der Loop-Punkt wird beim Export automatisiert geprüft (Abschnitt 8).
3. **Lautheit:** Alle Musik-Dateien werden auf −18 LUFS integriert normalisiert (True Peak ≤ −1 dBTP, `audio-overview.md` Abschnitt 3.12).
4. **Stems (Post-Launch):** Für die dynamischen Layer und potenzielle Ducking-Optionen werden die Board-Themen als Stems (Melodie, Begleitung, Bass, Rhythmus, Atmo) geliefert. Die Stems teilen Loop-Punkte mit dem Vollmix.

### 3.8 Übergänge und BPM-Lieferung

1. **Crossfade-Tabelle:** Die Musikübergänge folgen exakt `audio-overview.md` Abschnitt 3.8 (Menü→Board 1,0 s, Board→Minispiel 0,5 s, Minispiel→Board 0,3 s, Board→Victory 1,5 s, Victory→Menü 1,0 s).
2. **BPM-Wert für ArenaStar-Leuchten:** Das Audio-System liefert den aktuellen BPM-Wert (Abschnitt 4.1) an das ArenaStar-Modell (`narrative-arena-star.md` Abschnitt 3.6.3). Liegt keine Musik an (Menü-Pause), wird 100 BPM geliefert.
3. **Tempo-Wechsel (Sternenzitadelle):** Der Satz-/Tempo-Wechsel (3.3.7) wird dem Leucht-System gemeldet, damit das Pulsieren synchron bleibt.

## 4. Formulas

Variablendefinitionen:
- `T` = Dauer eines Taktes in Sekunden.
- `BPM` = Schläge pro Minute.
- `B` = Schläge pro Takt (aus der Taktart: 2/2 → 2, 4/4 → 4, 3/4 → 3).
- `N_Takte` = Anzahl der Takte der Form.
- `D` = Loop-Dauer in Sekunden.

### 4.1 Takt-Dauer und Loop-Dauer

`T = (B × 60) / BPM`, `D = N_Takte × T`.

- Beispiel Hauptmenü (2/2, 120 BPM): `T = (2 × 60) / 120 = 1,0 s`, `D = 90 × 1,0 = 90 s`.
- Beispiel Sonnenstrand (4/4, 110 BPM): `T = (4 × 60) / 110 ≈ 2,1818 s`, `D = 56 × 2,1818 ≈ 122,2 s`.
- Beispiel Zuckerwald (3/4, 120 BPM): `T = (3 × 60) / 120 = 1,5 s`, `D = 80 × 1,5 = 120 s`.
- Erwartungswerte: Alle Board-Themen (außer Sternenzitadelle) haben `D ∈ [108, 132] s` (120 s ± 10 %).

### 4.2 Form-Summenkontrolle

Für jedes Loop-Stück gilt: `Σ N_Abschnitt = N_Takte`.

- Hauptmenü: `8 + 16 + 16 + 16 + 8 + 16 + 10 = 90`.
- Sonnenstrand: `4 + 16 + 16 + 16 + 4 = 56`.
- Zuckerwald: `8 + 24 + 16 + 24 + 8 = 80`.
- Wolkenwerk: `4 + 16 + 16 + 8 + 6 = 50`.
- Frostgipfel: `8 + 8 + 16 + 8 + 5 = 45`.
- Dschungeltempel: `4 + 16 + 16 + 16 + 8 + 5 = 65`.
- Mechanik-Stadt: `8 + 16 + 16 + 16 + 8 + 6 = 70`.
- Sieg-Thema: `2 + 8 + 5 = 15` (bei 3/4, 90 BPM: `T = 2 s`, `D = 30 s`).
- Erwartungswert: Jede Form-Summe ist ganzzahlig und entspricht `N_Takte`.

### 4.3 Sternenzitadelle: Tempo-Map

`BPM(Satz) = {A: 80, B: 120, C: 160}`. Runden-Zuordnung: `Satz(Runde r) = A` für `r ∈ {1,2,3}`, `B` für `r ∈ {4,5,6,7}`, `C` für `r ∈ {8,9,10}`.

- Beispiel: In Runde 5 erklingt Satz B (120 BPM); in Runde 9 Satz C (160 BPM).
- Erwartungswert: Das Tempo ist über die Runden monoton nicht-fallend (80 → 160).

### 4.4 Countdown-Zeitplan

`t_i = i` Sekunden für Ton `i ∈ {1,2,3}` (C4, E4, G4); `t_LOS = 3 s`; Gesamtdauer `D = 4 s`.

- Beispiel: Ton 3 (G4) erklingt bei `t = 2 s`; die LOS-Fanfare beginnt bei `t = 3 s` und endet bei `t = 4 s`.

### 4.5 Action-Loop-Dauer

`D_Loop = 30 s ± 1 s`. Bei 150 BPM und 4/4 gilt `T = 1,6 s`; die 30-s-Ziel wird als 18 Takte (28,8 s) plus 2-Schlag-Auftakt (1,6 s) realisiert.

- Erwartungswert: Der Loop-Endpunkt fällt auf einen geraden Schlag und geht nahtlos in den Anfang über.

## 5. Edge Cases

1. **Loop nicht nahtlos:** Weist ein Loop einen hörbaren Sprung oder Phasenbruch am Loop-Punkt auf, gilt die Datei als fehlerhaft (Blocker, Abschnitt 8). Der Fehler wird an den Musik-Produzenten zurückgemeldet; das Spiel startet nicht mit einer fehlerhaften Loop-Datei.
2. **Insel-Thema länger/kürzer als 120 s:** Alle Themen außer der Sternenzitadelle müssen `D ∈ [108, 132] s` erfüllen (Formel 4.1). Ein Thema außerhalb dieses Bereichs wird angepasst (Taktzahl oder BPM); eine Abweichung über 10 % ist ein Blocker.
3. **Sternenzitadelle vor Feld 20:** Wird Feld 20 in der Partie nie erreicht, entfällt die Modulation C-Dur→E-Dur (3.3.7 Regel 2). Die Musik bleibt in C-Dur; das ist kein Fehler.
4. **Sternenzitadelle, Runde endet mitten in einem Satz:** Der Satzwechsel erfolgt nur an Phrasengrenzen (8 Takte). Endet die Runde mitten in einer Phrase, wartet der Wechsel auf die nächste Phrasengrenze; bis dahin erklingt der aktuelle Satz weiter (kein harter Schnitt).
5. **Minispiel-Abbruch während des Countdowns:** Der Countdown wird abgebrochen; die Musik kehrt ins Board-Thema zurück (Crossfade 0,3 s). Der Action-Loop startet nicht.
6. **Team-Minigame mit Platzierung:** Bei 2v2/1v3 gibt es keinen „Platz 2–3"-Fall; das Siegerteam hört die heroische Stufe, das Verliererteam die neutrale Stufe (3.4.3 Regel 2).
7. **Menü-Pause (keine Musik):** Liegt keine Musik an (z. B. während eines Ladebildschirms oder bei deaktiviertem Musik-Bus), liefert das System den BPM-Defaultwert 100 an das ArenaStar-Leuchten. Das ist kein Fehler.
8. **Deaktivierter Musik-Bus:** Ist der Musik-Bus stummgeschaltet, spielen die Musik-Streams weiter (stumm), damit die BPM-Lieferung und die Crossfade-Logik konsistent bleiben. Ein Wiedereinschalten stellt die Musik sofort hörbar her.
9. **Wiederholtes Minispiel in derselben Runde:** Nur das erste Minispiel pro Runde ist das reguläre Minispiel (`field-minigame.md`). Sollte ein weiteres Minispiel folgen (Sonderfall), werden Countdown und Action-Loop erneut abgespielt; die Ergebnis-Fanfare wird pro Minispiel-Ende ausgelöst.
10. **Victory-Crossfade bei sehr kurzer Siegerehrung:** Die Siegerehrung kann kürzer sein als das 30-s-Sieg-Thema (z. B. bei Abbruch). Wird die Siegerehrung abgebrochen, endet das Sieg-Thema sofort und die Musik wechselt ins Menü (Crossfade 1,0 s).
11. **Zuckerwald-Walzer und Loop:** Der 3/4-Takt mit 80 Takten ergibt exakt 120 s. Der Loop-Punkt fällt auf die „1" eines Walzer-Takts; eine Verschiebung um einen Schlag würde den Walzer-Charakter brechen (Validierung Abschnitt 8).

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `audio-music.md` | Art | Verwendung |
|-------------------------------|-----|------------|
| `design/gdd/audio-overview.md` | Quelle | Bus-Struktur (Musik-Bus), Crossfade-Zeiten (3.8), Ducking (3.4), Format-Tiers (3.2), LUFS-Ziele (3.12). |
| `design/gdd/world-overview.md` | Quelle | Insel-Liste, Insel-Identitäten, Musik-Stil-Angaben (Tabelle 3.2), Insel-Intro (3.6). |
| `design/gdd/narrative-arena-star.md` | Peer | ArenaStar-Leuchten-BPM (3.6.3), Siegerehrungs-Ablauf; die Musik begleitet die Moderation. |
| `design/gdd/core-loop.md` | Peer | Rundenstruktur (Runde 1–10) für die Tempo-Map der Sternenzitadelle und die Layer-Zuordnung. |
| `design/gdd/minigame-architecture.md` | Peer | Minispiel-Start/Ende (Countdown, Action-Loop, Ergebnis-Fanfare). |
| `design/gdd/minigame-categories.md` | Peer | Die 5 Kategorien für die Action-Loop-Varianten. |
| `design/gdd/victory-conditions.md` | Peer | Siegerehrung (Sieg-Thema, Platzierungs-Anzeige). |

### 6.2 Systeme, die von diesem Dokument abhängen

| System/Kapitel | Art der Abhängigkeit |
|----------------|----------------------|
| `ui-mainmenu.md` | Spielt das Hauptmenü-Thema; Menü-Motiv-Angaben. |
| `ui-board.md` | Zeigt den Insel-Titel-Einblender synchron zum Insel-Intro (Musik-Intro). |
| `audio-sfx.md` | Teilt den Countdown-Zeitplan (t = 0/1/2/3 s); die SFX-Countdown-Pieps und die Musik-LOS-Fanfare greifen ineinander. |
| `audio-voice.md` | Ducking der Musik bei Stimme (Sidechain); das Sieg-Thema läuft parallel zur Sieg-Moderation von ArenaStar. |
| `narrative-arena-star.md` | Leucht-Animation pulsiert mit dem BPM-Wert, den dieses Kapitel liefert. |
| `technical-architecture.md` | Muss das Musik-System (Stream-Verwaltung, Crossfade, BPM-Lieferung) als Systembaustein führen. |
| Board-Plugins (`plugins/boards/INSELNAME/audio/`) | Liefern die Insel-Musik; `board.json` referenziert den Musikstil (`world-overview.md` Abschnitt 3.12). |

### 6.3 Bidirektionalität

`audio-overview.md` verweist auf dieses Kapitel (Musik-Inhalte), dieses Kapitel verweist zurück (Systemrahmen). `world-overview.md` nennt die Musik-Stile je Insel; dieses Kapitel setzt sie in konkrete Stücke um und verweist auf die Inseln. `audio-sfx.md` und `audio-voice.md` teilen die Übergangs- und Ducking-Parameter. Änderungen an der Insel-Liste (`world-overview.md`) erfordern eine Prüfung der Board-Themen; Änderungen an BPM/Tonart eines Themas erfordern eine Rückmeldung an `world-overview.md` und `narrative-arena-star.md` (Leucht-BPM).

### 6.4 Design-Entscheidungen (dokumentierte Klärungen)

1. **Hauptmenü-Form (90 Takte, 2/2):** Die Form-Angaben summieren sich auf 90 Takte; bei 120 BPM im 2/2-Takt ergibt 1 Takt = 1 s, also exakt 90 s Loop-Dauer. Das Konzept nennt „90s Loop, BPM 120" — die 2/2-Interpretation erfüllt beides widerspruchsfrei.
2. **Sieg-Thema-Form (Fanfare 4, Thema 16, Krönung 10):** Diese Zahlen werden als **Sekunden** interpretiert (4 + 16 + 10 = 30 s). Im 3/4-Takt bei 90 BPM (1 Takt = 2 s) ergibt sich die Taktverteilung 2/8/5 (Formel 4.2). Die Sekundenangaben bleiben in Abschnitt 3.5 explizit erhalten.
3. **Sternenzitadelle (durchkomponiert + Runden-Tempo):** „BPM steigt mit Runde" wird als Satz-Kopplung interpretiert (Satz A/B/C mit Ziel-BPM 80/120/160, zugeordnet zu Runde 1–3/4–7/8–10). Das Stück bleibt durchkomponiert (180 s), die Sätze sind an Phrasengrenzen wechselbar. Die Modulation C-Dur→E-Dur wird als einmaliger, komponierter Pivot bei erstmaligem Erreichen von Feld 20 spezifiziert.
4. **Countdown-Tonabstand (500 ms vs. 1000 ms):** Das SFX-Kapitel nennt 500 ms Abstand, das Musik-Kapitel einen 4-s-Zeitplan. Klärung: Die drei Pieps erklingen bei t = 0/1/2 s (Abstand 1000 ms), die LOS-Fanfare bei t = 3 s; Gesamtdauer 4 s. Die 500-ms-Angabe im SFX-Konzept wird verworfen (siehe `audio-sfx.md` Abschnitt 6.4).

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| BPM je Insel-Thema | Kurve | je ± 15 BPM | siehe 3.3 | Gefühltes Tempo der Insel; ändert die Loop-Dauer (Formel 4.1). |
| Loop-Zieldauer | Kurve | 100–140 s | 120 s | Länge der Board-Themen; kürzere Loops wiederholen sich häufiger. |
| BPM-Default für Leuchten | Kurve | 80–140 BPM | 100 | Puls des ArenaStar-Leuchtens ohne Musik. |
| Layer-Schwellen (Runde) | Kurve | 1–10 | 1–3 / 4–7 / 8–10 | Ab welcher Runde ruhig/normal/intensiv erklingt. |
| Satz-Tempo-Map (Zitadelle) | Kurve | 60–180 BPM je Satz | 80/120/160 | Steilheit der Tempo-Steigerung über die Runden. |
| Modulations-Feld (Zitadelle) | Kurve | Feld 15–25 | 20 | Ab welchem Feld die C-Dur→E-Dur-Modulation ausgelöst wird. |
| Action-Loop-Dauer | Kurve | 20–45 s | 30 s | Wie oft sich der Minispiel-Loop wiederholt. |
| Action-Loop-Lautstärke (Puzzle) | Kurve | −8 bis 0 dB | −4 dB | Relative Absenkung der Puzzle-Variante. |
| Countdown-Zeitplan | Gate | fest | t = 0/1/2/3 s | Änderung nur mit Musik + SFX synchron (sonst Taktbruch). |
| Dynamische Layer | Gate | an/aus | aus (Post-Launch) | Aktiviert die Intensitäts-Layer. |
| Sieg-Thema-Dauer | Kurve | 20–45 s | 30 s | Länge der Siegerehrung; muss die Platzierungs-Anzeige abdecken. |

Alle Knobs liegen in der Audio-Konfiguration (zentrale Musik-Konfigurationsdatei), nicht im Code. Änderungen an BPM/Tonart eines Themas erfordern eine Hörprüfung des Loops und eine Rückmeldung an `world-overview.md` (Insel-Identität) und `narrative-arena-star.md` (Leucht-BPM).

## 8. Acceptance Criteria

Ein QA-Tester (oder CI-Hook) kann die folgenden Prüfungen ausführen (PASS/FAIL):

1. **Datei-Vollständigkeit:** Unter `assets/audio/music/` existieren: 1 Hauptmenü-Thema, 8 Insel-Themen, 1 Countdown, 1 Action-Loop pro Kategorie (5), 3 Ergebnis-Fanfaren (Stufen), 1 Sieg-Thema. PASS/FAIL.
2. **Loop-Dauer:** Jedes Loop-Stück (Menü, Boards, Action-Loop) erfüllt seine Ziel-Dauer aus Formel 4.1 (Boards: 120 s ± 10 %; Menü: 90 s; Action-Loop: 30 s ± 1 s). PASS/FAIL (Timer-Messung).
3. **Nahtlosigkeit:** Der Übergang vom letzten zum ersten Takt jedes Loops ist frei von hörbaren Sprüngen oder Phasenbrüchen (Hörprüfung mit 3 Testern; kein Tester meldet einen Bruch). PASS/FAIL.
4. **Form-Summe:** Für jedes Stück stimmt die Form-Summe mit `N_Takte` überein (Formel 4.2). PASS/FAIL (Manuell am Taktplan geprüft).
5. **Tempo/Tonart:** Jedes Thema erklingt in der spezifizierten BPM und Tonart (Tabelle 3.3; Messung mit Stimmgerät/DAW-Analyse: ± 1 BPM, Tonart korrekt). PASS/FAIL.
6. **Sternenzitadelle Tempo-Map:** In einer Testpartie auf der Sternenzitadelle mit 10 Runden ist das Tempo monoton nicht-fallend (Runde 1–3 ≈ 80 BPM, 4–7 ≈ 120 BPM, 8–10 ≈ 160 BPM) und wechselt nur an Phrasengrenzen. PASS/FAIL.
7. **Modulation:** Beim erstmaligen Erreichen von Feld 20 moduliert die Musik von C-Dur nach E-Dur; danach bleibt E-Dur (kein Zurückmodulieren). PASS/FAIL (Hörprüfung in einer Testpartie).
8. **Countdown-Zeitplan:** Die drei Pieps erklingen bei t = 0/1/2 s (C4/E4/G4), die LOS-Fanfare bei t = 3 s; Gesamtdauer 4,0 s. PASS/FAIL (Timer-Messung).
9. **Action-Loop-Kategorien:** Jede Kategorie-Variante erfüllt ihre Spezifikation (Geschicklichkeit: Synth; Reaktion: 16tel-Hi-Hats; Puzzle: −4 dB, sanft; Rechnen: Metronom-Klick; Kooperation: warm/hymnisch). PASS/FAIL (Hörprüfung).
10. **Ergebnis-Fanfare:** Platz 1 → heroische Trompeten-Stufe, Platz 2–3 → fröhliche Flöten-Stufe, Platz 4+ → neutrale, sanfte Stufe. Keine Stufe enthält absteigende oder dissonante Elemente in der neutralen Variante. PASS/FAIL.
11. **Sieg-Thema:** Das Sieg-Thema erklingt genau einmal pro Partie (30 s), startet mit dem Victory-Crossfade (1,5 s) und wird nicht geloopt. PASS/FAIL.
12. **Crossfade-Einhaltung:** Alle Musikübergänge folgen der Tabelle aus `audio-overview.md` Abschnitt 3.8 (Equal-Power, exakte Dauer). PASS/FAIL.
13. **BPM-Lieferung:** Das ArenaStar-Leuchten erhält den korrekten BPM-Wert (aktuelle Musik bzw. 100 BPM ohne Musik). PASS/FAIL (Schnittstellentest).
14. **Lautheit:** Jede Musik-Datei ist auf −18 LUFS integriert normalisiert, True Peak ≤ −1 dBTP. PASS/FAIL (Messung).
15. **Erlebbar (Experiential):** Eine Testperson kann bei laufendem Sound (ohne Bild) jede der 7 Inseln anhand der Musik eindeutig der richtigen Insel zuordnen (mindestens 6 von 7 korrekt). PASS/FAIL.
