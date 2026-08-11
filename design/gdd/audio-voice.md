# Audio Voice — Sprachausgabe

## 1. Overview
Die Sprachausgabe von Party Arena wird dominiert von **ArenaStar**, dem charismatischen Showmaster-Maskottchen. Mit ~210 voll vertonten Zeilen führt er durch Menüs, kommentiert Ereignisse, moderiert Minispiele und krönt den Gewinner. Die 8 Arenians haben je ~8 kurze emotionale Vokalisationen (Lachen, Seufzer, Jubel) — keine Sprachausgabe. Das System nutzt den dedizierten Godot AudioServer Bus "Stimme" (−3 dB) mit Sidechain-Ducking auf Musik (−8 dB).

## 2. Player Fantasy
Der Spieler fühlt sich **persönlich begleitet**. ArenaStar ist kein kaltes UI-Element — er spricht den Spieler an, feuert an, tröstet bei Pech und feiert Erfolge. Seine Stimme ist freundlich, energiegeladen, nie herablassend. Auch ohne Lesen zu müssen versteht jeder (auch Kinder ab 6), was zu tun ist. Die Charakter-Vokalisationen geben den Arenians Persönlichkeit: Brix' tiefes Grollen beim Sieg, Tiko's chaotisches "Kraa!", Momos kesses Kichern.

## 3. Detailed Rules

### 3.1 ArenaStar — Das Maskottchen (~210 Zeilen, 10 Kategorien)

**Aufnahme-Spezifikation:**
- Format: 48 kHz, 24-bit, Mono .wav (Recording)
- Delivery: .ogg Vorbis, 96 kbps, Mono (96 kHz Sample-Rate ausreichend)
- Pegel: −6 dBFS Peak, −18 dBFS RMS (Sprach-standard)

**Stimm-Charakter:**
- Geschlecht: Männlich-weich (Tenor-Lage, nicht Bariton)
- Pitch: Mittel-hoch (200–300 Hz Grundfrequenz)
- Tempo: Zügig aber deutlich (~4 Silben pro Sekunde)
- Charakter: Begeisterter Showmaster — denk an einen freundlichen Spielshow-Moderator, nicht an einen Zirkusdirektor
- Vorbilder: "Quizmaster mit Herz", nicht "aggressiver Verkäufer"

**Kategorie 1: Menü (15 Zeilen)**
- "Willkommen in der PARTY ARENA!" (Startmenü)
- "Wähle deine Insel, Arenianer!" (Board-Auswahl)
- "Wer wird heute der hellste Stern?" (Charakter-Auswahl)
- "Bereit? Dann los!" (Spielstart)
- "Einstellungen — hier machst du das Spiel zu DEINEM Spiel!" (Settings)
- "Statistik — schau wie weit du gekommen bist!" (Statistik)
- "Die tapferen Entwickler von Claude Code Game Studios!" (Credits)
- "Bis zum nächsten Mal, Arenianer!" (Spiel beenden)
- "Server suchen... ich funkle schon!" (Server-Browser)
- "Zu zweit, zu acht — jeder ist willkommen!" (Lobby)

**Kategorie 2: Spiel-Anweisungen (30 Zeilen)**
- "[SPIELERNAME]! Du bist dran! Würfle!" (Zug-Beginn)
- "Wähle deinen Pfad mit Bedacht!" (Abzweigung)
- "Ein Item? Gute Idee! Wähle weise!" (Item aktivieren)
- "Minispiel-Zeit! Zeigt was ihr könnt!" (Minispiel-Start)
- "Stern oder nicht Stern — das ist hier die Frage!" (Stern-Shop)
- "Weiter so, [SPIELERNAME]!" (nach Zug-Ende)
- "Nur noch [N] Runden! Gebt alles!" (letzte Runden)

**Kategorie 3: Countdown (5 Zeilen)**
- "3..." (tief, ruhig)
- "2..." (mittel, Spannung steigt)
- "1..." (hoch, erwartungsvoll)
- "LOS!" (laut, explosiv, energiegeladen)
- "LOS LOS LOS!" (Variante für Koop-Minispiele)

**Kategorie 4: Ereignisse (50 Zeilen — je Event 2–3 Varianten)**
Beispiele:
- "Sternschnuppen-Regen! Wünsch dir was!" / "Sternschnuppen für alle!" / "Münz-Regen vom Himmel!"
- "Piraten-Überfall! Haltet eure Münzen fest!" / "Aaarrr! Piraten!"
- "Großzügiger ArenaStar! Ein Geschenk für den Letzten!" (lacht)
- "Tausch-Basar! Alles auf den Kopf gestellt!" / "Wer steht jetzt wo? Ich blick's selbst nicht mehr!"
- "Würfel-Verdoppler! Doppelt hält besser!"
- "Stern-Rabatt! Jetzt zuschlagen!"
- "Item-Regen! Fangt sie alle!"
- "Münzsturm! Schnell, sammelt ein!"
- "Rückruf! Zurück zum Start, alle miteinander!"
- "Schneesturm! Zwei von euch machen Pause... brrr!"
- "Fluch des Tempels! Oooh, das tut weh!"
- "Nordlicht! Wunderschön... und nützlich!"

**Kategorie 5: Minispiel-Moderation (40 Zeilen)**
- "Gut gemacht, [SPIELERNAME]!" (Top-Platzierung)
- "Knapp daneben! Beim nächsten Mal!" (knapp verloren)
- "Und der Gewinner ist... [SPIELERNAME]!" (1. Platz)
- "Platz [N]: [SPIELERNAME]!" (Ansage aller Platzierungen)
- "Was für ein spannendes Minispiel!" (neutral)
- "Unglaublich! So knapp war's noch nie!" (enger Ausgang)
- "Keine Sorge [SPIELERNAME], du holst wieder auf!" (Verlierer trösten)
- "Teamwork makes the dream work!" (Koop-Minispiel)
- "[SPIELERNAME] mit dem perfekten Move!" (besonders gute Leistung)

**Kategorie 6: Shop-Kommentare (20 Zeilen)**
- "Schnäppchen gefällig? Drei zur Auswahl!" (Item-Shop)
- "Der Glücks-Würfel! Immer eine gute Wahl!" (Hover Glücks-Würfel)
- "Der Stern-Teleporter! Zack, schon bist du da!" (Hover Teleporter)
- "Das Schutzschild! Sicher ist sicher!" (Hover Schutzschild)
- "Der Münz-Magnet! Geld zieht Geld an!" (Hover Münz-Magnet)
- "Der Dieb-Handschuh! Äh, ich mein... sehr strategisch!" (Hover Dieb-Handschuh, verschwörerisch)
- "Ein funkelnder Stern für 20 Münzen!" (Stern-Shop)
- "Gute Wahl, [SPIELERNAME]!" (nach Kauf)
- "Du brauchst 20 Münzen! Komm wieder, wenn du genug hast!" (zu wenig Münzen)
- "Inventar voll! Erstmal was verbrauchen!" (Inventar-Limit)

**Kategorie 7: Sieges-Zeremonie (15 Zeilen)**
- "Die Party Arena ist vorbei! Lasst uns die Sterne zählen!"
- "Bonus-Sterne! Wer hat sie verdient?"
- "Der Reichste: [SPIELERNAME]! [N] Bonus-Sterne!"
- "Der Schnellste: [SPIELERNAME]! [N] Bonus-Sterne!"
- "Und der Gewinner... mit [S] Sternen... IST... [SPIELERNAME]!!!"
- "Ein würdiger Champion! Die Sternen-Zitadelle ist stolz auf dich!"
- "Platz [N]: [SPIELERNAME] mit [S] Sternen." (für Plätze 2–8)
- "Danke fürs Spielen, Arenianer! Bis zum nächsten Mal!"

**Kategorie 8: Tutorial (15 Zeilen)**
- "Dein erstes Mal in der Party Arena? Ich erklär's dir!"
- "Du würfelst, ziehst, und landest auf einem Feld. Jedes Feld macht was anderes!"
- "Am Ende jeder Runde gibt's ein Minispiel! Da kannst du Münzen gewinnen!"
- "Mit 20 Münzen kaufst du einen Stern. Wer am Ende die meisten Sterne hat, gewinnt!"
- "Bonus-Sterne gibt's am Ende obendrauf! Für besondere Leistungen!"
- "Probier's einfach aus — du wirst sehen, es ist kinderleicht!"
- "Das war's! Viel Spaß in der Arena!"

**Kategorie 9: Idle-Kommentare (10 Zeilen)**
- "Keine Eile... aber die Sterne warten!" (nach 10s Inaktivität)
- "Die Spannung steigt!" (nach 15s)
- "Triff eine Wahl! Oder lass den Zufall entscheiden!" (nach 20s)
- "Ich zähle bis drei... nur ein Scherz! Nimm dir Zeit!" (nach 30s)
- "Bereit wenn du es bist!" (nach 40s)

**Kategorie 10: Besondere Momente (10 Zeilen)**
- "[SPIELERNAME] hat den ERSTEN Stern gekauft!" (erster Stern-Kauf)
- "Letzte Runde! Alles oder nichts!" (Runde 10/10)
- "Gleichstand! Sudden-Death-Minispiel!" (Tie-Breaker)
- "Was für eine Aufholjagd von [SPIELERNAME]!" (großer Positionswechsel)
- "Alle Items weg! [SPIELERNAME] wurde bestohlen!" (Dieb-Handschuh-Erfolg)
- "Schutzschild aktiviert! [SPIELERNAME] ist immun!" (Schild-Block)

### 3.2 Charakter-Vokalisationen (64 Sounds, 8 Charaktere × 8)

Jeder Arenian hat 8 emotionale Vokalisationen. KEINE Sprachausgabe — nur Laute, die Persönlichkeit transportieren.

| Kategorie | Typ | Beispiel |
|---|---|---|
| Freude (2×) | Positiv, kurz | Lachen, Juchzen |
| Trauer/Enttäuschung (2×) | Negativ, kurz | Seufzen, "Och nö..." |
| Überraschung (1×) | Neutral, kurz | "Oh!", "Huch!" |
| Sieg (1×) | Positiv, lang (2s) | Jubel, charakteristischer Sieges-Laut |
| Anstrengung (1×) | Neutral, mittel | angestrengtes "Hmpf!" |
| Spezial (1×) | Charakterspezifisch | Siehe unten |

**Aufnahme-Spezifikation:**
- Format: 48 kHz, 16-bit, Mono .wav
- Delivery: .ogg Vorbis, 64 kbps, Mono
- Pegel: −6 dBFS Peak (Lautheit variiert nach Emotion)

**Charakterspezifische Sounds:**

| Charakter | Stimm-Charakter | Spezial-Sound |
|---|---|---|
| Brix | Tiefes, echoendes Grollen (Stein) | Steine knirschen beim Lachen |
| Nixie | Helles Kichern, Blubber-Geräusche | Unterwasser-Bubbl-Geräusch |
| Pip | Schnelles, hohes Piepsen | Flügel-Flatter-Geräusch |
| Koko | Tiefes, zufriedenes Brummen | Gemütliches Gähnen |
| Tiko | Lautes "Kraa!", melodisches Trillern | Federn-Raschel-Explosion |
| Bolt | Elektronisches "Boop-Boop!" | Zahnrad-Klackern beim Jubeln |
| Bloom | Sanftes Summen | Blumen-Aufblüh-Geräusch (soft Pop) |
| Momo | Verschwörerisches Kichern "Hehe!" | Tasche-Raschel-Geräusch |

### 3.3 Stimmen-Priorität und Ducking-System

- **Stimme-Bus**: −3 dB relativ zu Master, eigener Bus für Ducking-Kontrolle
- **Sidechain-Ducking**: ArenaStar-Stimme duckt Musik-Bus um −8 dB
  - Attack: 50ms (schnelles Ducking)
  - Release: 200ms (sanftes Zurückkommen)
  - Ratio: 4:1 (moderat)
  - Threshold: −20 dBFS (greift früh)
- **Queue-System**: ArenaStar spricht nie über sich selbst
  - Wenn neue Zeile während aktiver Zeile: Alte Zeile fade-out (150ms), neue Zeile startet nach 100ms Pause
  - Kein Interrupt außer bei Countdown (Countdown bricht jede laufende Zeile sofort ab)
- **Charakter-Vokalisationen**: Spielen parallel zu ArenaStar (anderer Bus-Zweig), aber ArenaStar duckt sie NICHT. Bei exakt gleichzeitigem Start: Charakter 50ms Verzögerung.

### 3.4 Untertitel-System

- **Anzeige**: Weißer Text (#FFFFFF), 2px schwarze Outline (#000000), Schrift Komika Axis 18px
- **Position**: Unterer Bildschirmrand, zentriert, max 2 Zeilen à 40 Zeichen
- **Timing**: Erscheint 100ms vor Audio-Beginn, verschwindet 300ms nach Audio-Ende
- **Toggle**: In Audio-Einstellungen: "Untertitel: AN/AUS"
- **Was wird untertitelt**: Alle ArenaStar-Zeilen (210). Charakter-Vokalisationen: NEIN (sie sind emotional, nicht kommunikativ).
- **Mehrsprachigkeit**: Untertitel folgen eingestellter Spielsprache (DE/EN/FR/ES/PT/JP/ZH). Audio bleibt Deutsch (keine Mehrsprach-Aufnahme geplant).

### 3.5 Voice-Fallback (Voice-aus-Modus)

Wenn Stimme-Bus deaktiviert (Mute oder Volume = 0%):
- Alle ArenaStar-Zeilen werden als **Text-Sprechblase** über ArenaStars 3D-Modell angezeigt
- Sprechblasen-Stil: Cartoon-Bubble, weiß mit 3px Outline, spitze Ecke zu ArenaStar
- Dauer: Textlänge (in Zeichen) × 80ms, Minimum 2 Sekunden, Maximum 8 Sekunden
- Sprechblasen queue-en nicht — neue ersetzt alte (wie Audio)
- Im Voice-aus-Modus werden auch die Untertitel deaktiviert (sie wären redundant)

## 4. Formulas

### F1: Sprechblasen-Dauer im Voice-Fallback
```
Dauer = clamp(text.length() × 80ms, 2000ms, 8000ms)
Wobei: text.length() = Zeichenanzahl (inkl. Leerzeichen)
```

### F2: Ducking-Gain-Reduction
```
GR = (Input_Level - Threshold) × (1 - 1/Ratio)
Für Input = −6 dBFS (typische Stimme):
GR = (−6 - (−20)) × (1 - 1/4) = 14 × 0.75 = 10.5 dB
→ Begrenzt auf max 8 dB (Hard-Limit im Godot Compressor)
```

### F3: Audio-Queue-Interrupt-Regel
```
Wenn neue_zeile.queued ∧ aktive_zeile.spielend:
  Wenn neue_zeile.typ == "countdown":
    aktive_zeile.stop()  // sofort
  Sonst:
    aktive_zeile.fade_out(150ms)
    warte(100ms)
  neue_zeile.play()
```

### F4: Charakter-Stimmen-Pegel relativ zu ArenaStar
```
ArenaStar_Spitzenpegel = −6 dBFS
Charakter_Spitzenpegel = −9 dBFS (leiser als ArenaStar)
→ Charakter-Vokalisationen sind immer leiser als ArenaStar
```

## 5. Edge Cases

- **ArenaStar zweimal kurz hintereinander**: Queue-System verarbeitet beide nacheinander. Wenn erste Zeile noch in Fade-Out (150ms), wartet zweite Zeile bis Fade-Out + 100ms Pause abgeschlossen.
- **Countdown unterbricht Shop-Dialog**: Spieler kauft Item in letzter Sekunde vor Minispiel → ArenaStar: "Gute Wahl! — 3... 2... 1... LOS!" → Countdown bricht Shop-Kommentar ab. Shop-Kommentar wird NICHT nachgeholt.
- **Charakter-Vokalisation bei Stummschaltung**: Wenn SFX+Stimme-Bus gemutet (Fokus-Verlust), keine Vokalisationen. Bei Rückkehr: Keine Nachholung (nicht rekonstruierbar).
- **Gleichzeitiger Sieg-Jubel (Team-Minispiel)**: Beide Gewinner-Charaktere spielen Sieg-Vokalisation. Zweiter startet mit 100ms Versatz (automatische Staffelung).
- **Untertitel zu lang**: Wenn Untertitel >80 Zeichen → Auf 2 Zeilen à max 40 Zeichen umbrechen. Wenn immer noch zu lang → Kürzen auf 80 Zeichen (mit "..."). Dies sollte bei den geschriebenen Zeilen nicht vorkommen — Design-Regel: Max 70 Zeichen pro ArenaStar-Zeile.
- **Fehlende Audio-Datei**: Wenn .ogg nicht geladen werden kann → Text-Fallback (Sprechblase) automatisch, auch wenn Stimme-Bus aktiv. Error-Log: "Voice line missing: [dateiname].ogg"
- **Sprachwechsel zur Laufzeit**: Untertitel wechseln sofort (String-Resource-Reload). Audio wechselt NICHT (bleibt Deutsch) — dafür müssten separate Audio-Spuren existieren (nicht in Scope v1).

## 6. Dependencies

- **audio-overview.md**: Bus-Struktur, Ducking-System, Crossfade (Stimme hat eigenes Ducking)
- **audio-music.md**: Musik-Lautstärke (Stimme duckt Musik)
- **narrative-arena-star.md**: ArenaStar-Persönlichkeit, Catchphrases, Sprechweise (hier vertont)
- **narrative-flavor.md**: Event-Texte, Item-Beschreibungen (hier vertonte Varianten)
- **characters-overview.md**: Charakter-Namen, Persönlichkeiten (hier Vokalisationen)
- **ui-accessibility.md**: Untertitel-Toggle, Text-Skalierung (Untertitel-Größe folgt Text-Größen-Stufen)
- **ui-overview.md**: UI-Theme-Schriftart (Untertitel nutzt Komika Axis)
- **field-event.md**: Event-IDs (Audio-Kategorie 4 referenziert diese)
- **item-system.md**: Item-IDs (Shop-Kommentare referenzieren Items)

## 7. Tuning Knobs

| Knob | Default | Safe Range | Beeinflusst |
|---|---|---|---|
| VOICE_BUS_VOLUME | −3 dB | −12 bis 0 dB | Alle Stimmen-Lautstärke |
| VOICE_DUCKING_AMOUNT | −8 dB | −12 bis −3 dB | Musik-Reduktion bei Stimme |
| VOICE_DUCKING_ATTACK | 50ms | 20–100ms | Ducking-Geschwindigkeit |
| VOICE_DUCKING_RELEASE | 200ms | 100–500ms | Musik-Rückkehr-Geschwindigkeit |
| SPEECH_RATE | 1.0 | 0.8–1.3 | ArenaStar-Sprech-Tempo |
| SPEECH_PITCH | 1.0 | 0.9–1.2 | ArenaStar-Stimmhöhe |
| SUBTITLE_FONT_SIZE | 18px | 14–24px | Untertitel-Größe (Basis) |
| SUBTITLE_MAX_CHARS_PER_LINE | 40 | 30–50 | Max Zeichen/Zeile |
| SPEECH_BUBBLE_DURATION_PER_CHAR | 80ms | 50–120ms | Sprechblasen-Dauer |
| SPEECH_BUBBLE_MIN_DURATION | 2000ms | 1000–3000ms | Min Sprechblasen-Dauer |
| CHARACTER_VOCAL_LEVEL | −9 dBFS | −12 bis −6 dBFS | Charakter-Vokalisationen-Lautstärke |
| QUEUE_FADE_OUT_MS | 150ms | 100–300ms | Fade-Out bei Interrupt |

## 8. Acceptance Criteria

1. ✅ ArenaStar hat ≥200 aufgenommene Zeilen, verteilt auf 10 Kategorien (Recording-Asset-Check)
2. ✅ Jeder Arenian hat ≥8 Vokalisationen, verteilt auf 6 Kategorien (Recording-Asset-Check)
3. ✅ ArenaStar-Stimme duckt Musik um −8 dB (Audio-Messung: Musik-Pegel vor/während Stimme)
4. ✅ Queue-System: Zwei aufeinanderfolgende Zeilen überlappen nicht (Audio-Prüfung)
5. ✅ Countdown unterbricht laufende Zeile sofort (Funktionstest: Shop-Kommentar + Countdown)
6. ✅ Untertitel erscheinen 100ms vor Audio, verschwinden 300ms nach Audio (Timing-Prüfung)
7. ✅ Untertitel folgen eingestellter Sprache (DE/EN/FR/ES/PT/JP/ZH) (Lokalisierungstest)
8. ✅ Voice-Fallback: Sprechblase erscheint wenn Stimme-Bus gemutet (Funktionstest)
9. ✅ Sprechblasen-Dauer = clamp(text.length×80ms, 2s, 8s) (Timing-Prüfung mit verschiedenen Texten)
10. ✅ Charakter-Vokalisationen werden NIE untertitelt (Untertitel-Log prüft auf Abwesenheit)
11. ✅ Keine Sprachausgabe für Charaktere — nur Vokalisationen (Recording-Asset-Check: keine Wörter)
12. ✅ Audio-Fehler: Fehlende .ogg zeigt Sprechblase statt Stille (Error-Injection-Test)
13. ✅ ArenaStar spricht nie über sich selbst — keine doppelten Stimm-Overlays (Stress-Test mit schnellen Events)
14. ✅ Untertitel-Format: Weiß + 2px schwarze Outline, max 2 Zeilen (UI-Pixel-Prüfung)
15. ✅ Sieg-Vokalisationen bei Team-Minispiel: 100ms Staffelung (Audio-Prüfung)
16. ✅ Voice-Regler (0–100%) in Einstellungen steuert Stimme-Bus korrekt (Audio-Messung)
