# Audio SFX — Sound-Effekte

## 1. Overview
Die Sound-Effekte (SFX) von Party Arena bilden die akustische Rückmeldung für jede Spieleraktion. Mit ~120 individuellen Sounds in 7 Kategorien (UI, Würfel, Bewegung, Felder, Items, Minispiele, Events, Ambient) wird jede Interaktion hörbar gemacht. Das SFX-System nutzt den Godot AudioServer Bus "SFX" (−3 dB relativ zu Master) mit Prioritäts-Steuerung und Audio-Pool für häufige Sounds.

## 2. Player Fantasy
Der Spieler **fühlt** jede Aktion: Jeder Knopf klickt zufriedenstellend, jeder Würfel klackert spannend, jeder Schritt klingt nach dem gewählten Charakter. Die Sound-Palette ist cartoonhaft überzeichnet — Münzen klimpern hell, Items haben charakteristische "Magic"-Sounds, und ArenaStars Countdown baut Spannung auf. Nichts klingt realistisch oder bedrohlich — alles klingt nach Spielzeug und Spaß.

## 3. Detailed Rules

### 3.1 UI-Sounds (Critical-Priorität, max 2 gleichzeitig)
Diese Sounds werden NIE von anderen Sounds geduckt oder verdrängt:

| Sound | Dauer | Frequenz | Charakter |
|---|---|---|---|
| Button-Hover | 50ms | Sinus 800→1200 Hz Sweep | Kurzes "Tick", −12 dB |
| Button-Click | 100ms | Sinus-Mix C5+E5+G5 | Positives "Pop", −6 dB |
| Button-Back | 100ms | Sinus 400 Hz | Dumpferes "Pop", −9 dB |
| Fehler-Buzz | 150ms | Square 200 Hz | "Bzz", −6 dB |
| Kauf-Bestätigung | 200ms | 5× Random Pitch 800–1200 Hz | Münz-Klimpern |
| Stern-Kauf | 500ms | Gliss C4→C6 (Harfe) | Magischer "Shing!", 30% Hall |
| Runden-Wechsel | 300ms | C-E-G aufsteigend (Orgel) | Neue Runde |

### 3.2 Würfel-Sounds (High-Priorität)
- **Würfel-Wurf**: 300ms, 4× Holz-Klackern, Random Pitch ±100 Hz um 1 kHz. Simuliert das Rollen eines Würfels auf Holz.
- **Würfel-Landung**: 200ms pro Zahl. Tonhöhe = Zahl auf C-Dur-Skala (1=C4, 2=D4, 3=E4, 4=F4, 5=G4, 6=A4). Spieler hören ihre Zahl.
- **Glücks-Würfel**: Extra "Sparkle"-Sound (200ms Glissando aufwärts) VOR dem Zahl-Ton. Signalisiert: "Besonderer Würfel!"

### 3.3 Bewegung (Low-Priorität, 4 Varianten pro Gewichtsklasse)
Jeder Charakter gehört einer von drei Gewichtsklassen an. Der Schritt-Sound wird pro Feld ausgelöst (beim Übergang von Feld zu Feld):

| Klasse | Charaktere | Dauer | Frequenz | Charakter |
|---|---|---|---|---|
| Leicht | Pip, Nixie, Tiko | 50ms | 2 kHz | Soft "tap" |
| Mittel | Koko, Momo, Bloom | 80ms | 800 Hz | Medium "thud" |
| Schwer | Brix, Bolt | 120ms | 200 Hz | Heavy "stomp" mit Bass-Boost |

### 3.4 Feld-Sounds (Low-Priorität)
Ausgelöst bei Betreten eines Feldes (nur beim exakten Landen, nicht beim Überqueren):

| Feldtyp | Sound | Dauer | Beschreibung |
|---|---|---|---|
| START | Glocke C5 | 500ms | Klarer Glockenklang mit Hall, "Willkommen zurück!" |
| STAR_SHOP | Harfen-Glissando | 300ms | Magischer aufsteigender Ton, "Hier gibt's Sterne!" |
| ITEM_SHOP | Registrierkasse | 100ms | Metallisches "Ding!" bei 2 kHz |
| EVENT | Trommel-Wirbel | 200ms | Spannung: "Was passiert jetzt?" |
| LUCK (positiv) | Münz-Regen | 300ms | Heller Münz-Prassel-Sound |
| LUCK (negativ) | Donnerschlag | 400ms | Tiefer, dumpfer Schlag |
| COIN_BONUS | 3× Münz-Klimpern | 400ms | Schnelles "bling-bling-bling" |
| MINIGAME | Fanfare | 500ms | Kurze C-Dur-Fanfare, "Minispiel-Zeit!" |

### 3.5 Item-Sounds (High-Priorität)
| Item | Aktivierung | Block/Effekt |
|---|---|---|
| Glücks-Würfel | Gold-Würfel-Roll 400ms | — |
| Teleporter | "Whoosh" 500ms, Weißes Rauschen mit Low→High Filter-Sweep | "Kein Stern verfügbar": Fehler-Buzz |
| Schutzschild | Energie-Schild "Bzzzzt" 300ms, Sägezahn-Wave | Block-Auslösung: Glas-Zerbrech 200ms + Energie-Fadeout 300ms |
| Münz-Magnet | Metallisches "Klack" + Summen 400ms, 60 Hz Brummen | — |
| Dieb-Handschuh | "Swish" 150ms + böses Lachen 300ms (kurz, cartoonhaft) | Geblockt von Schild: Schild-Block-Sound |

### 3.6 Minispiel-Sounds (High-Priorität)
- **Countdown**: 3× Piep-Ton (500ms Abstand). Tonhöhe C4→E4→G4 (aufsteigend, Spannungsaufbau)
- **Go-Signal**: Fanfare 800ms, C-Dur Arpeggio aufsteigend. Laut, energiegeladen.
- **Timer-Warnung** (letzte 5s): Tick alle 500ms, 1 kHz, leiser startend → laut endend. Volumen-Ramp von −12 dB auf −3 dB.
- **Spielende**: Tiefer Gong 1.5s, langer Ausklang. Reverb 60% Mix, 2s Decay-Time.
- **Punkte-Zählen**: Ein "Ding" (200ms, 1 kHz) pro Spieler. Abstand zwischen Dings: 300ms. Tempo steigt NICHT — alle Platzierungen gleicher Rhythmus, aber verschiedene Tonhöhe (höherer Platz = höherer Ton).
- **Ergebnis-Fanfare**: 3 Stufen à 3s: Platz 1 = heroisch (Trompeten-Fanfare C-Dur), Plätze 2–3 = fröhlich (Flöten-Melodie), Plätze 4–8 = neutral (sanfter Durakkord).

### 3.7 Event-Sounds (Low/High je nach Event-Typ)
- **Positives Event**: Aufsteigendes 3-Noten-Arpeggio in Dur, 300ms. Helle Instrumentation (Glockenspiel).
- **Negatives Event**: Absteigendes 3-Noten-Arpeggio in Moll + Donnerschlag, 500ms. Dunkle Instrumentation (Cello).
- **Neutrales Event**: Kurze neutrale Fanfare 200ms, einzelner Durakkord.

### 3.8 Ambient-Sounds (Low-Priorität, −18 dB unter Musik)
Jede Insel hat eigene Ambient-Loops und Random-Trigger:

| Insel | Loop (10–15s) | Random-Trigger | Intervall |
|---|---|---|---|
| Sonnenstrand | Wellen (sanft) | Möwen-Schrei | 5–15s |
| Zuckerwald | Wald-Atmo (Insekten, Blätter) | Bonbon-Pop | 3–8s |
| Wolkenwerk | Wind (leise, hoch) | Ballon-Quietschen | 8–20s |
| Frostgipfel | Wind-Heulen (tief) | Eis-Knacken | 5–12s |
| Dschungeltempel | Dschungel (Vögel, Insekten) | Trommel (leise, fern) | 10–20s |
| Mechanik-Stadt | Zahnräder-Summen (Loop) | Dampf-Zischen | 3–10s |
| Sternenzitadelle | Kosmisches Summen (tief) | Stern-Glitzer (hell, kurz) | 2–5s |

## 4. Formulas

### F1: Prioritäts-basierte Stimmen-Verteilung
```
Verfügbare Stimmen = 16 (Godot AudioServer Limit)
Critical: max 2 Stimmen (nie verdrängt)
High:    max 8 Stimmen (verdrängt Low bei Bedarf)
Low:     max 6 Stimmen (wird verdrängt wenn High+Low > 14)
```

### F2: Audio-Pool LRU-Auswahl
```
Pool-Größe = 16 AudioStreamPlayer3D
Bei Anforderung: 
  1. Suche inaktiven Player im Pool
  2. Wenn keiner: Verwende Least-Recently-Used Player (stoppe dessen Sound)
  3. Setze neuen Sound, spiele ab
```

### F3: Schritt-Sound-Lautstärke pro Gewichtsklasse
```
Leicht: −15 dB (relativ zu SFX-Bus)
Mittel: −12 dB
Schwer:  −9 dB (inkl. +3 dB Bass-Boost unter 150 Hz)
```

### F4: Timer-Warnung Volumen-Ramp
```
V(t) = V_start + (V_end - V_start) × (t / T)
Wobei: V_start = −12 dB, V_end = −3 dB, T = 5s, t = vergangene Zeit
```

## 5. Edge Cases

- **SFX-Stimmen-Limit erreicht**: Wenn 16 Stimmen aktiv sind, wird der älteste Low-Priorität-Sound gestoppt. Critical- und High-Sounds werden nie für Low-Sounds gestoppt.
- **Gleichzeitige Feld-Betretung**: Wenn mehrere Spieler gleichzeitig ein Feld betreten (Event-Teleport), werden Feld-Sounds nacheinander mit 100ms Abstand abgespielt (Queue).
- **SFX bei pausiertem Spiel**: Alle SFX pausieren mit dem Spiel (Godot Pause-Mode). Ausnahme: UI-Sounds im Pause-Menü (Critical-Priorität, Pause-Mode = Process).
- **Fenster-Verlust**: SFX stoppen sofort (mute_window_unfocus = true). Bei Rückkehr: SFX setzen fort, Ambient-Loops starten neu.
- **0 Münzen bei Münz-Klimpern**: Kein Sound (keine Münzen zum Klimpern). Stattdessen: Fehler-Buzz.
- **Audio-Device-Wechsel während SFX**: Alle aktiven SFX stoppen, Pool leeren, neue Sounds normal abspielen. Keine Wiederherstellung unterbrochener Sounds (nicht kritisch für Spielerlebnis).

## 6. Dependencies

- **audio-overview.md**: Bus-Struktur, Prioritäts-System, Audio-Pool, Spatial Audio (hier verwendet)
- **audio-music.md**: Musik-Lautstärke, Ducking (Musik duckt bei High-Priorität SFX nicht — umgekehrte Abhängigkeit)
- **audio-voice.md**: ArenaStar-Stimme hat eigene SFX (Mund-Bewegungs-Sound optional)
- **item-system.md**: Item-Namen und Aktivierungs-Zeitpunkte (hier: Item-Sounds)
- **field-event.md**: Event-Namen und Typen (hier: Event-Sounds)
- **minigame-architecture.md**: Minispiel-Phasen (hier: Minispiel-Sounds)
- **board-architecture.md**: Feldtypen (hier: Feld-Sounds)
- **world-overview.md**: Insel-Namen (hier: Ambient-Sounds pro Insel)
- **characters-overview.md**: Charakter-Namen und Gewichtsklassen (hier: Schritt-Sounds)

## 7. Tuning Knobs

| Knob | Default | Safe Range | Beeinflusst |
|---|---|---|---|
| SFX_BUS_VOLUME | −3 dB | −12 bis 0 dB | Alle SFX-Lautstärke |
| MAX_CRITICAL_VOICES | 2 | 1–4 | Max gleichzeitige UI-Sounds |
| MAX_HIGH_VOICES | 8 | 4–12 | Max Minispiel/Item-Sounds |
| MAX_LOW_VOICES | 6 | 2–10 | Max Ambient/Schritt-Sounds |
| TOTAL_VOICES | 16 | 8–32 | Godot AudioServer Limit |
| AMBIENT_VOLUME_OFFSET | −18 dB | −24 bis −12 dB | Ambient relativ zu Musik |
| TIMER_WARNING_VOLUME_START | −12 dB | −18 bis −6 dB | Timer-Tick Startlautstärke |
| TIMER_WARNING_VOLUME_END | −3 dB | −6 bis 0 dB | Timer-Tick Endlautstärke |
| STEP_LIGHT_VOLUME | −15 dB | −20 bis −10 dB | Schritt-Lautstärke leichte Charaktere |
| STEP_MEDIUM_VOLUME | −12 dB | −18 bis −8 dB | Schritt-Lautstärke mittlere Charaktere |
| STEP_HEAVY_VOLUME | −9 dB | −15 bis −6 dB | Schritt-Lautstärke schwere Charaktere |
| FIELD_SOUND_COOLDOWN | 200ms | 100–500ms | Min-Abstand zwischen Feld-Sounds |

## 8. Acceptance Criteria

1. ✅ Jeder Button-Hover/Click/Back erzeugt hörbaren Sound (UI-Interaktion)
2. ✅ Würfel-Wurf und Landung sind klar unterscheidbar (Würfel-Mechanik)
3. ✅ Schritte variieren hörbar nach Charakter-Gewichtsklasse (3 Klassen unterscheidbar)
4. ✅ Jeder Feldtyp hat eigenen Betretungs-Sound (8 Sounds, alle hörbar)
5. ✅ Jedes Item hat eigenen Aktivierungs-Sound (5 Sounds, eindeutig)
6. ✅ Minispiel-Countdown: 3 Piepser + Go-Fanfare, Timing exakt (3.0s + 0.8s)
7. ✅ Timer-Warnung: Tick alle 500ms in letzten 5s, Lautstärke nimmt zu
8. ✅ Minispiel-Ergebnis: 3 Fanfaren-Stufen korrekt nach Platzierung (Platz 1, 2–3, 4–8)
9. ✅ Events: Positiv/Negativ/Neutral haben unterscheidbare Sounds
10. ✅ Jede Insel hat Ambient-Loop + Random-Trigger (7 Inseln getestet)
11. ✅ 16-Stimmen-Limit wird eingehalten (Stress-Test: alle Sounds gleichzeitig triggern)
12. ✅ Critical-Sounds werden nie von Low-Priorität verdrängt (UI bleibt immer hörbar)
13. ✅ Pausierte SFX setzen bei Unpause korrekt fort
14. ✅ Fenster-Verlust stoppt alle SFX sofort (mute_window_unfocus = true)
15. ✅ Audio-Device-Wechsel: SFX funktionieren nach Hotplug ohne Neustart
16. ✅ Kein Sound clipping (−0.1 dBFS Headroom auf Master)
