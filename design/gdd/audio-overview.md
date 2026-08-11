# Audio-Übersicht — Party Arena Game Bible

> **Teil:** 8 — Audio (8.1)
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/bible-index.md, design/gdd/technical-architecture.md, design/gdd/vision-pillars.md

---

## 1. Overview

Dieses Kapitel ist die Dach-Spezifikation des gesamten Audio-Systems von Party Arena. Es definiert die verbindliche Audio-Architektur: die 4-Bus-Struktur des Godot-AudioServers (Master, Musik, SFX, Stimme) mit ihren Zielpegeln, die Dateiformate und Qualitätsstufen je Audiokategorie, die Mono-/Stereo-Regeln, das dynamische Ducking (Sidechain), das SFX-Prioritäten- und Stimmen-Budget, den wiederverwendbaren 3D-Audio-Pool, die Spatial-Audio-Parameter, die Crossfade-Zeiten zwischen Spielzuständen, das Verhalten bei Fenster-Fokus-Verlust sowie die Behandlung von Audio-Device-Wechseln (Hotplug). Basis der Bus-Struktur ist die mitgelieferte `default_bus_layout.tres` aus dem Super-Tux-Party-Fork; sie wird auf die vier Ziel-Busse reduziert beziehungsweise erweitert. Die drei Kapitel `audio-music.md`, `audio-sfx.md` und `audio-voice.md` spezifizieren die konkreten Inhalte (Musikstücke, Sound-Effekte, Sprachausgabe); dieses Kapitel liefert den Rahmen, in dem alle Inhalte existieren.

Das Audio-System dient den vier Design-Pfeilern aus `vision-pillars.md`: Es muss **sofort verständlich** sein (jede Interaktion gibt akustisches Feedback), **überzeichnet** klingen (Cartoon/Toy-Ästhetik mit deutlichen, physisch unmöglichen Sound-Tropes), **interaktiv wirken** (das Audio reagiert sicht- und hörbar auf jeden Spielzustand) und **wiedererkennbar** sein (jede Insel, jeder Charakter und jede Spielphase hat ein eigenes, konsistentes Klangprofil).

## 2. Player Fantasy

Das Audio-System erzeugt das Gefühl, in einer **lebendigen Spielzeug-Arena** zu sein, die auf jede Aktion sofort und mit einem Lächeln antwortet. Jeder Klick, jedes Würfeln, jeder Schritt und jedes Ereignis hat einen eigenen, unverwechselbaren Klang — nichts passiert stumm. Die Musik ist der emotionale Taktgeber: Sie wechselt mit jeder Insel die Stimmung (von Hawaii-Chill bis Zahnrad-Mechanik) und begleitet die Partie von der entspannten Anmoderation bis zur triumphalen Siegerehrung. Wenn ArenaStar spricht, tritt die Musik respektvoll in den Hintergrund (Ducking), damit jedes Wort verstanden wird — der Spieler erlebt das wie einen Showmaster, der die Bühne für einen Moment übernimmt.

Die zentrale emotionale Verheißung: **"Jede Aktion klingt, als würde sie gefeiert."** Ein verlorenes Minispiel klingt nicht bestrafend, sondern tröstlich-verspielt; ein Stern-Kauf klingt wie ein kleines Feuerwerk; und selbst ein Fehler-UI klingt charmant-cartoonhaft statt technisch kalt. Gleichzeitig bleibt das System **unaufdringlich**: Ambient-Sounds liegen dezent unter der Musik, und die Gesamtlautstärke wird über einen einzigen Master-Regler gesteuert, während Detail-Regler (Musik, Effekte, Stimme) dem Spieler die Feinjustierung überlassen.

## 3. Detailed Rules

### 3.1 Bus-Struktur

Das Spiel nutzt exakt vier Audio-Busse. Basis ist die `default_bus_layout.tres` des STP-Forks; die Bus-Struktur wird auf die folgenden vier Busse reduziert beziehungsweise erweitert und bleibt während einer Partie unverändert.

| Bus | Zielpegel (relativ zu Master) | Inhalt | Route |
|-----|-------------------------------|--------|-------|
| Master | 0 dB | Gesamtmischung aller Busse | Ausgabe an das Audio-Device |
| Musik | −6 dB | Alle Musik-Streams (Menü, Boards, Minispiele, Victory) | Master |
| SFX | −3 dB | Alle Sound-Effekte inklusive UI, Würfel, Bewegung, Felder, Items, Minispiele, Events, Ambient | Master |
| Stimme | −3 dB | ArenaStar-Stimme, Charakter-Vokalisationen | Master |

Regeln:

1. **Master regelt die Gesamtlautstärke.** Der Master-Regler in den Audio-Einstellungen (`ui-overview.md`, `ui-accessibility.md`) verändert ausschließlich den Master-Bus-Pegel. Ein Spieler, der alle Geräusche abschalten will, nutzt den Master; wer nur die Stimme abschalten will, nutzt den Stimme-Bus.
2. **Bus-IDs sind stabil.** Die Reihenfolge und die Namen der Busse (`Master`, `Musik`, `SFX`, `Stimme`) sind über die gesamte Partie und alle Szenen hinweg identisch. Kein System darf einen Bus neu erzeugen oder umbenennen.
3. **Kein Bus speist einen anderen außer Master.** Es gibt keine Bus-Sendeketten wie SFX → Musik. Alle drei Inhalt-Busse routen direkt in den Master.
4. **Stummschaltung pro Bus.** Jeder Bus kann über seine `mute`-Eigenschaft einzeln stummgeschaltet werden. Die Stummschaltung des Stimme-Busses ist die Grundlage des Voice-Fallbacks (`audio-voice.md` Abschnitt 3.8).
5. **Pegel-Einstellungen werden gespeichert.** Die vom Spieler gewählten Bus-Pegel (Master, Musik, SFX, Stimme) werden in den Audio-Einstellungen persistiert (`technical-data-structures.md`) und beim Start wiederhergestellt. Die Zielpegel aus der Tabelle sind die **Werks-Sollwerte**, die nach einem Reset oder bei einer frischen Konfiguration gelten.

### 3.2 Dateiformate und Qualitäts-Tiers

Alle Audio-Dateien werden als Ogg-Vorbis ausgeliefert. Es gelten drei Qualitäts-Tiers, abhängig von der Kategorie:

| Kategorie | Format | Vorbis-Qualität | Ungefähre Bitrate | Quellrate | Kanäle |
|-----------|--------|-----------------|-------------------|-----------|--------|
| Musik | `.ogg` | q=4 | ~128 kbps | 48 kHz | Stereo |
| SFX | `.ogg` | q=2 | ~64 kbps | 48 kHz | Mono |
| Stimme | `.ogg` | q=3 | ~96 kbps | 48 kHz | Mono |
| UI (Teil von SFX) | `.ogg` | q=2 | ~64 kbps | 48 kHz | Mono |

Regeln:

1. **Die Projekt-Audio-Samplerate ist 48 kHz.** Alle Quellen werden mit 48 kHz produziert und exportiert, sodass Godot kein Resampling durchführen muss.
2. **SFX und UI teilen dasselbe Tier (q=2).** UI-Sounds sind eine Unterkategorie der SFX (Priorität Critical, siehe 3.5) und folgen dem SFX-Format.
3. **Ambience-Loops folgen dem SFX-Tier (q=2).** Sollte eine Hörprüfung bei Ambience-Loops einen hörbaren Qualitätsverlust zeigen, ist eine Ausnahme auf q=3 zulässig (Tuning-Knob, Abschnitt 7).
4. **Keine anderen Container.** Wave, FLAC oder MP3 werden nicht ausgeliefert. Quell-WAVs liegen nur im Asset-Produktionspfad, nicht im Spiel-Export.
5. **Loudness-Normalisierung:** Vor dem Export werden alle Dateien auf ein einheitliches integriertes Lautheitsziel normalisiert (Abschnitt 3.12).

### 3.3 Mono/Stereo-Regeln

| Kategorie | Kanalzahl | Begründung |
|-----------|-----------|------------|
| Musik | Stereo | Musik ist die atmosphärische Basis; Stereo-Breite unterstützt die Insel-Identität. |
| SFX (räumlich, 3D) | Mono | Mono-Quellen können im 3D-Raum eindeutig gepannt werden (Spatial Audio, 3.7). |
| Stimme | Mono | ArenaStar und Charaktere sprechen aus der Bildmitte; Mono verhindert Phasenprobleme. |
| UI | Mono | UI-Sounds sind nicht räumlich; Mono hält sie fokussiert und sparsam. |

Ausnahme Ambience: Ambient-Loops sind als Mono aufgenommen. Um ohne Verletzung der Mono-Regel eine räumliche Breite zu erzeugen, wird im Mix eine dezentrale Verbreiterung angewendet (gegengespannte Kopie mit 3 ms Delay, Pegel 50 %). Diese Verbreiterung ist ein Tuning-Knob (Abschnitt 7) und betrifft ausschließlich den SFX-Bus.

### 3.4 Dynamische Musik und Ducking (Sidechain)

Das Musik-Ducking wird über Sidechain-Verbindungen realisiert: Bestimmte Auslöser senken den Musik-Bus-Pegel zeitweise ab, damit darunterliegende Informationen (Sprache, Popup-Texte) klar verständlich bleiben.

| Ducking-Quelle | Auslöser | Betrag | Attack | Release |
|----------------|----------|--------|--------|---------|
| Kommentar-Ducking | Ein ArenaStar-Kommentar wird ausgelöst (Text oder Stimme) | −6 dB | 100 ms | 300 ms |
| Popup-Ducking | Ein Ereignis-/Event-Popup erscheint ohne Stimme | −3 dB | 100 ms | 300 ms |
| Stimmen-Sidechain | Der Stimme-Bus ist aktiv (ArenaStar-Stimme oder Charakter-Vokalisation) | −8 dB | 50 ms | 200 ms |

Regeln:

1. **Beträge addieren sich nicht.** Sind mehrere Ducking-Quellen gleichzeitig aktiv, gilt der **größte** aktive Betrag, nicht die Summe. Während eines vertonten ArenaStar-Kommentars gilt also `−8 dB` (Stimmen-Sidechain übersteuert das Kommentar-Ducking), niemals `−6 + (−8) = −14 dB`.
2. **Attack und Release** bezeichnen die Zeitkonstanten der Pegel-Hüllkurve: `Attack` = Zeit bis zum Erreichen des vollen Ducking-Betrags, `Release` = Zeit bis zur Rückkehr auf den Musik-Zielpegel. Die Hüllkurven sind linear in dB.
3. **Critical-Sounds werden nie geduckt** (Abschnitt 3.5): UI-Feedback bleibt bei vollem Pegel hörbar, auch während Musik duckt.
4. **Ducking gilt nur für den Musik-Bus.** Der SFX-Bus und der Stimme-Bus werden durch das Musik-Ducking nicht verändert. Der SFX-Bus wird seinerseits nie von Sprache geduckt (SFX bleiben bei ArenaStar-Kommentaren auf Normalpegel).
5. **Vorrang:** Gilt gleichzeitig ein Kommentar- und ein Popup-Ducking ohne Stimme, so gewinnt der Kommentar (−6 dB > −3 dB).

### 3.5 SFX-Prioritäten und Stimmen-Budget

Das Spiel hält eine **harte Obergrenze von 16 gleichzeitig klingenden SFX-Stimmen** ein. Diese Grenze wird vom Audio-System erzwungen (Stimmen-Manager); Musik (1–2 Streams während Crossfades) und Stimme (maximal 1 Stimme) sind davon getrennt.

| Priorität | Einsatz | Max. gleichzeitig | Verhalten |
|-----------|---------|-------------------|-----------|
| Critical | UI-Feedback (Button, Fehler, Kauf-Bestätigung) | 2 | Nie geduckt, nie verweigert, nie durch niedrigere Prioritäten unterbrochen. |
| High | Minispiel-Effekte, Item-Aktivierungen, Würfel | 8 | Standard-Priorität für spielrelevante Effekte. |
| Low | Ambient, Schritte, Feld-Sounds | 6 | Hintergrundgeräusche; werden zuerst unterbrochen. |

Allokationsregeln:

1. **Budget-Prüfung vor Wiedergabe.** Jede SFX-Wiedergabe-Anfrage wird klassifiziert (Critical/High/Low) und gegen das Budget geprüft.
2. **Kapazität frei:** Ist in der eigenen Prioritätsklasse Kapazität frei und die Gesamtzahl < 16, wird der Sound abgespielt.
3. **Budget voll:** Ist die Gesamtzahl = 16, wird ein Diebstahl-Versuch ausgeführt: Der aktivste Sound mit der niedrigsten Priorität wird ermittelt. Hat die neue Anfrage eine Priorität ≥ der Priorität des ermittelten Sounds, wird der alte Sound gestoppt und der neue gespielt. Andernfalls wird die Anfrage **verweigert** (kein Warteschlangen-Puffer für SFX).
4. **Gleichrangige Konkurrenz (LRU):** Unter Sounds derselben Priorität wird derjenige unterbrochen, der am längsten aktiv ist (least-recently-used).
5. **Critical-Sonderregel:** Critical-Sounds haben 2 exklusiv reservierte Stimmen. Sind beide belegt und trifft ein dritter Critical-Sound ein, wird der älteste aktive Critical-Sound gestoppt (UI-Feedback ist kurzlebig; ein neuer Klick ist wichtiger als ein ausklingender Hover). Critical-Sounds werden nie verweigert.
6. **Kein Pre-Emption von Musik/Stimme:** Das SFX-Budget kann keine Musik- oder Stimme-Stimme belegen. Umgekehrt kann eine laufende Musik-/Stimme-Wiedergabe nie durch ein SFX gestoppt werden.

### 3.6 Audio-Pool (3D-Wiederverwendung)

Für räumliche Board-Sounds (Schritte, Feld-Sounds, Ambient-One-Shots) wird ein **Pool aus 16 wiederverwendbaren `AudioStreamPlayer3D`-Knoten** vorgehalten. Der Pool ist die physische Implementierung der 3D-SFX-Stimmen; die Vergabe folgt den Budget-Regeln aus 3.5.

1. **Pool-Größe:** exakt 16 Instanzen, beim Start des Board-Spiels erzeugt, während der Partie nicht verändert.
2. **Wiederverwendung (LRU):** Wird eine neue 3D-SFX-Anfrage gestellt, wird der Pool-Slot mit dem ältesten letzten Einsatz belegt. Ist der Slot noch aktiv (Sound läuft noch), wird er gemäß den Prioritätsregeln aus 3.5 unterbrochen (niedrigste Priorität zuerst; bei Gleichstand LRU).
3. **Knoten-Konfiguration:** Jeder Pool-Slot hat die Spatial-Parameter aus 3.7 fest konfiguriert; beim Abspielen wird nur die Position (global transform), der Stream und die Lautstärke gesetzt.
4. **2D-Sounds nutzen den Pool nicht.** Nicht-räumliche Sounds (UI, Minispiel-Effekte ohne Position) verwenden kurzlebige, nicht-räumliche Player, die bei Spielende freigegeben werden. Sie zählen jedoch in dasselbe 16-Stimmen-Budget (Stimmen-Manager).
5. **Keine Stillzeit:** Idle Pool-Slots sind stumm geschaltet (Volume −∞), belegen aber keine zusätzliche CPU-Last außerhalb des normalen AudioServer-Betriebs.

### 3.7 Spatial Audio

Spatial Audio gilt für alle räumlichen Board-Sounds (Schritte, Feld-Sounds, platzierte Item-Effekte, Ambient-One-Shots an Positionen).

| Parameter | Wert |
|-----------|------|
| Modell | Inverse Distance (quadratisch) |
| Unit Size | 1,0 |
| Max Distance | 15 Einheiten |
| Doppler | Aus (nicht relevant für dieses Spiel) |
| Listener | An der aktiven Kamera befestigt (`ui-board.md` Kamera-Führung) |
| Panning | Mono-Quellen; Panner auf dem SFX-Bus |

Regeln:

1. **Entfernung = euklidische Distanz** zwischen der 3D-Position des Sounds und der Listener-Position in Einheiten.
2. **Jenseits von 15 Einheiten** fällt die Lautstärke auf 0 ab (kein hörbarer Sound außerhalb der Max Distance).
3. **Unit Size 1,0** bedeutet: Ein Sound in 1 Einheit Entfernung erklingt mit Referenzlautstärke; mit zunehmender Entfernung nimmt die Lautstärke nach dem inversen Quadrat ab.
4. **Doppler ist deaktiviert**, weil sich die Listener-Position im Board-Spiel nicht schnell genug bewegt, um einen glaubwürdigen Doppler-Effekt zu erzeugen; ein aktivierter Doppler würde als technischer Fehler wahrgenommen.
5. **Charaktere haben keine eigenen Listener.** In Split-Screen-Ansichten (8 Spieler) wird der Listener immer an der aktiven Hauptkamera geführt; die übrigen Ansichten teilen sich die Audio-Perspektive (Kamera-Regeln in `ui-board.md`).

### 3.8 Übergänge und Crossfade

Beim Wechsel zwischen Spielzuständen wird die Musik über eine Kreuzblende (Crossfade) übergeführt. Es gelten die folgenden Fade-Zeiten:

| Übergang | Crossfade-Dauer | Charakter |
|----------|-----------------|-----------|
| Menü → Board | 1,0 s | Gleichmäßig, einladend |
| Board → Minispiel | 0,5 s | Kurz, zügig (Flow erhalten) |
| Minispiel → Board | 0,3 s | Sehr kurz (schnelle Rückkehr) |
| Board → Victory | 1,5 s | Lang, dramatisch (Höhepunkt) |
| Victory → Menü | 1,0 s | Gleichmäßig, Abschluss |

Regeln:

1. **Equal-Power-Kreuzblende:** Die Pegel der ausgehenden und eingehenden Musik folgen über die Fade-Dauer einer sin²/cos²-Kurve, sodass die Summe beider Signale keinen Pegel-Einbruch erzeugt.
2. **Exakte Dauer:** Die Crossfade-Dauer wird vom Übergangssystem als Zeitwert vorgegeben (Tuning-Knob, Abschnitt 7). Die Fade-Kurven sind deterministisch und reproduzierbar.
3. **Ausnahme Minispiel:** Da Minispiel-Szenen eigene Musik verwenden (Countdown, Action-Loop), startet die Minispiel-Musik bei t = 0,0 s relativ zum Minispiel-Start, unabhängig von der Überblend-Dauer.
4. **Wiederholtes Board-Betreten:** Beim Wechsel von einem Board zu einem anderen (nicht vorgesehen im normalen Ablauf, aber beim Zurückkehren ins Menü möglich) gilt dieselbe Tabelle wie Menü ↔ Board.
5. **Pause:** Während einer Spielunterbrechung (z. B. Pause-Menü) wird die Musik nicht überblendet, sondern sofort pausiert und bei Fortsetzung nahtlos weitergeführt.

### 3.9 Stummschaltung bei Fokus-Verlust

Verliert das Spiel-Fenster den Fokus (Alt-Tab, Fensterwechsel), werden die Busse **SFX und Musik** stummgeschaltet. Diese Funktion ist optional und über die Einstellung `mute_window_unfocus` in `Global.gd` konfigurierbar (Erbe aus dem STP-Fork).

Regeln:

1. **Fokus-Verlust:** SFX-Bus und Musik-Bus werden auf stumm gesetzt (mute). Der Stimme-Bus und der Master-Bus bleiben unverändert. Eine laufende Stimme-Zeile läuft zu Ende (bewusst: ein begonnener Satz wird nicht abgeschnitten).
2. **Fokus-Rückkehr:** Die Busse werden sofort auf ihre vorherigen Pegel zurückgesetzt.
3. **Standard:** Die Funktion ist standardmäßig aktiviert (Tuning-Knob, Abschnitt 7).
4. **Ausnahme:** Im lokalen Mehrspieler-Modus mit 2–8 Spielern an einem Gerät gilt: Nur wenn alle lokalen Spieler das Spiel pausiert haben, darf der Fokus-Verlust die Busse stummschalten. Läuft eine Partie aktiv weiter, bleibt das Audio hörbar (sonst verlöre der wartende Spieler die akustische Orientierung).

### 3.10 Audio-Device-Wechsel (Hotplug)

Godot behandelt den Wechsel von Audio-Geräten (Kopfhörer abziehen, HDMI-Wechsel, Bluetooth) über den AudioServer. Das Spiel ergänzt ein definiertes Fehlerverhalten:

1. **Geräte-Verlust:** Stellt das Audio-System fest, dass das aktive Ausgabegerät nicht mehr verfügbar ist (Callback des AudioServer), werden **alle laufenden Sounds pausiert** (nicht gestoppt). Es wird kein neuer Sound gestartet.
2. **Reconnect-Versuch:** Das System versucht bis zu **3 Sekunden**, ein gültiges Ausgabegerät zu finden (Geräteliste neu einlesen).
3. **Reconnect erfolgreich:** Alle pausierten Sounds werden an der Pausenposition fortgesetzt. Bus-Pegel bleiben unverändert.
4. **Reconnect fehlgeschlagen:** Nach Ablauf der 3 Sekunden wechselt das System auf das **System-Standardgerät** (default device). Ist kein Gerät verfügbar, bleibt das Audio pausiert und das System wiederholt den Versuch alle 5 Sekunden, bis ein Gerät erscheint.
5. **Automatische Erkennung:** Wechselt der Spieler das Gerät selbst (z. B. Kopfhörer anschließen), übernimmt Godot den neuen Default-Output. Das Spiel unternimmt dabei keine weiteren Schritte; laufende Sounds werden vom AudioServer automatisch umgeroutet.
6. **Kein UI-Zwang:** Das Spiel zeigt bei Gerätewechseln kein modales Fenster. Ein dezenter Hinweis in den Audio-Einstellungen ist zulässig.

### 3.11 Asset-Struktur und Namenskonvention

Alle Audio-Assets liegen unter `assets/audio/`:

| Pfad | Inhalt |
|------|--------|
| `assets/audio/music/` | Musik-Streams (Menü, Boards, Minispiele, Victory) |
| `assets/audio/sfx/` | Sound-Effekte (inklusive UI) |
| `assets/audio/voice/` | ArenaStar-Stimme und Charakter-Vokalisationen |
| `assets/audio/ambient/` | Ambient-Loops und -One-Shots je Insel |

Es gilt die projektweite Namenskonvention `[kategorie]_[kontext]_[name]_[variante].[ext]`:

| Segment | Bedeutung | Beispiel |
|---------|-----------|----------|
| Kategorie | `mus`, `sfx`, `amb`, `voice` | `mus` |
| Kontext | `ui`, `board`, `menu`, `minigame`, `island`, `arena` | `board` |
| Name | eindeutiger Name des Sounds | `field_star_shop` |
| Variante | 01, 02, … bei mehreren Varianten | `01` |

Beispiele: `mus_board_sonnenstrand_01.ogg`, `sfx_ui_button_click_01.ogg`, `amb_island_frostgipfel_wind_loop.ogg`, `voice_arena_star_countdown_03.ogg`. Varianten werden durchnummeriert und per Round-Robin abgespielt (`audio-sfx.md` Abschnitt 3.9, `audio-voice.md` Abschnitt 3.2).

### 3.12 Lautheits-Ziele (LUFS)

Alle Audio-Inhalte werden auf einheitliche Lautheitsziele normalisiert, damit die Bus-Sollwerte (3.1) eine stabile Gesamtlautstärke ergeben.

| Kategorie | Ziel (integrierte Lautheit) | Peak-Limit |
|-----------|-----------------------------|------------|
| Musik | −18 LUFS | ≤ −1 dBTP |
| SFX | −18 LUFS (Einzeldateien) | ≤ −1 dBTP |
| Stimme | −16 LUFS | ≤ −1 dBTP |
| Master (Gesamtmix) | −16 LUFS (Zielbereich) | ≤ −1 dBTP |

Regeln:

1. **Normalisierung vor Export:** Jede Quelldatei wird vor dem Ogg-Export auf ihr Kategorie-Ziel normalisiert (integrierte Lautheit nach ITU-R BS.1770, gemessen über die volle Datei).
2. **True Peak:** Keine Datei überschreitet −1 dBTP, um Inter-Sample-Peaks im Master zu vermeiden.
3. **Die Werte sind Mischziele, keine harten Pegel:** Der tatsächliche Wiedergabepegel ergibt sich aus dem Datei-Pegel plus dem Bus-Sollwert aus 3.1. Die LUFS-Werte dienen der Reproduzierbarkeit und dem QA-Check (Abschnitt 8).
4. **Ambient liegt −18 dB unter der Musik:** Ambience wird zusätzlich zum SFX-Bus-Sollwert mit einer relativen Dämpfung von −18 dB gegenüber dem Musik-Sollwert abgemischt (Details in `audio-sfx.md` Abschnitt 3.8).

## 4. Formulas

Variablendefinitionen:
- `V_total` = Gesamtzahl gleichzeitig klingender SFX-Stimmen.
- `V_Critical = 2`, `V_High = 8`, `V_Low = 6` = Kapazität je Prioritätsklasse.
- `D` = angewandter Ducking-Betrag in dB (positiver Wert, wird subtrahiert).
- `L_musik` = aktueller Musik-Bus-Pegel in dB.

### 4.1 Stimmen-Budget

`V_total = V_Critical + V_High + V_Low ≤ 16`, mit `V_Critical ≤ 2`, `V_High ≤ 8`, `V_Low ≤ 6`.

- Erwartungswerte: `V_total ∈ [0, 16]`. Ein typisches Board-Spiel nutzt gleichzeitig 2–5 Stimmen (Schritte 1, Ambience 1–2, ein Feld-Sound 1, gelegentlich ein UI-Klick 1).
- Beispiel: 1 Schritt-Sound (Low) + 1 Feld-Sound (Low) + 1 Ambience-Loop (Low) + 1 UI-Click (Critical) + 1 Würfel-Landung (High) = `V_total = 5`, von denen `V_Low = 3`, `V_Critical = 1`, `V_High = 1` sind.
- Validierung: In keinem Moment während einer Partie überschreitet `V_total` den Wert 16; die Überschreitung ist ein Blocker (Abschnitt 8).

### 4.2 Ducking-Berechnung

`L_musik' = L_musik − D_effektiv`, wobei `D_effektiv = max({D_i})` über alle gleichzeitig aktiven Ducking-Quellen `i` ist.

- Quelle K = Kommentar-Ducking: `D_K = 6 dB`. Quelle P = Popup-Ducking: `D_P = 3 dB`. Quelle S = Stimmen-Sidechain: `D_S = 8 dB`.
- Beispiel 1 (nur Kommentar): `D_effektiv = 6 dB`, `L_musik' = −6 dB − 6 dB = −12 dB`.
- Beispiel 2 (Kommentar + Stimme gleichzeitig): `D_effektiv = max(6, 8) = 8 dB`, `L_musik' = −14 dB` — nicht `−20 dB`.
- Erwartungswerte: `D_effektiv ∈ [0, 8] dB`. Ein Wert unter 0 dB (Anhebung) ist nicht möglich; eine Summation der Beträge ist per Definition ausgeschlossen.

### 4.3 Crossfade-Zeiten

`T_Fade` ist die Dauer der Kreuzblende in Sekunden:

| Übergang | `T_Fade` |
|----------|----------|
| Menü → Board | 1,0 s |
| Board → Minispiel | 0,5 s |
| Minispiel → Board | 0,3 s |
| Board → Victory | 1,5 s |
| Victory → Menü | 1,0 s |

Die Pegelkurven: `g_aus(t) = cos²(π/2 · t/T_Fade)`, `g_ein(t) = sin²(π/2 · t/T_Fade)` für `t ∈ [0, T_Fade]`. An jedem Punkt gilt `g_aus(t) + g_ein(t) = 1` (Equal-Power).

### 4.4 Pool-Wiederverwendung (LRU)

`Slots = {Slot_1, …, Slot_16}`. Bei einer Anfrage wird `Slot* = argmin_{Slot ∈ Slots} t_letzterEinsatz(Slot)` gewählt.

- Ist `Slot*` stumm, wird er direkt belegt.
- Ist `Slot*` aktiv, wird nach 3.5 entschieden: Hat die Anfrage Priorität ≥ Priorität des aktiven Sounds, wird der Slot übernommen; sonst wird die Anfrage verweigert.
- Erwartungswert: Die Wiederverwendung ist deterministisch und reproduzierbar (gleiche Anfragesequenz → gleiche Slot-Belegung).

### 4.5 Geräte-Reconnect

`t_Reconnect = 3,0 s` (maximale Wartezeit auf ein Gerät), `t_Retry = 5,0 s` (Wiederholungsintervall ohne Gerät).

- Beispiel: Geräte-Verlust bei t = 0 s. Gelingt der Reconnect nicht innerhalb von 3 s, wechselt das System auf das Standardgerät. Ist auch das nicht verfügbar, bleibt das Audio pausiert; der nächste Versuch erfolgt bei t = 8 s (3 s + 5 s), dann t = 13 s, usw.
- Erwartungswert: In 95 % der Geräte-Verlust-Fälle ist der Reconnect innerhalb von 3 s erfolgreich (Zielgröße für QA).

## 5. Edge Cases

1. **Alle 16 SFX-Stimmen belegt, neue Anfrage ist Low:** Die Anfrage wird verweigert. Der Spieler hört den Sound nicht; kein Sound wird unterbrochen (Low kann von Low nicht stehlen, wenn alle Stimmen Low belegt sind und die Gesamtzahl 16 ist). Das System protokolliert die Verweigerung nicht als Fehler.
2. **Alle 16 Stimmen belegt, neue Anfrage ist Critical:** Die zwei exklusiv reservierten Critical-Stimmen sind immer frei (2 von 16 sind für Critical reserviert); trifft eine Critical-Anfrage ein, während beide Critical-Slots belegt sind, wird der älteste Critical-Sound gestoppt. Eine Critical-Verweigerung ist ausgeschlossen.
3. **Zwei Ducking-Quellen mit unterschiedlichen Attack-Zeiten gleichzeitig:** Die Hüllkurve folgt dem stärksten Betrag mit dessen eigener Attack-Zeit. Beispiel: Stimmen-Sidechain (Attack 50 ms) und Kommentar-Ducking (Attack 100 ms) gleichzeitig → es gilt `D = 8 dB` mit Attack 50 ms.
4. **Ducking-Auslöser endet vor Ablauf des Attack:** Ein extrem kurzer Kommentar (unter 50 ms) erreicht nie den vollen Ducking-Betrag; die Hüllkurve kehrt sofort um. Das ist korrekt und gewollt (kein hörbarer „Ducking-Wackler" bei Minimal-Texten).
5. **Mehrere Spieler landen gleichzeitig auf Feldern mit Sounds:** Die Feld-Sounds (Low, max 6) können gebündelt ankommen. Bei mehr als 6 gleichzeitigen Low-Anfragen werden die überzähligen verweigert (3.5). Das Spiel bevorzugt deterministisch die Sitzplatz-Reihenfolge (niedrigster Sitzplatzindex zuerst).
6. **Crossfade unterbrochen:** Wird ein Übergang begonnen und durch einen neuen Übergang abgelöst (z. B. Menü → Board, dann sofort Board → Minispiel), startet der neue Übergang ab dem aktuellen Mischzustand; die alte Fade-Kurve wird abgebrochen. Die neue Fade-Dauer gilt vollständig.
7. **Fokus-Verlust während eines Crossfades:** Die Busse werden stummgeschaltet; bei Fokus-Rückkehr wird der Crossfade ab dem Punkt fortgesetzt, an dem er unterbrochen wurde (kein Sprung).
8. **Geräte-Verlust während einer Stimme-Zeile:** Alle Sounds pausieren (3.10). Die Stimme-Zeile wird an der Pausenposition fortgesetzt, sobald ein Gerät verfügbar ist. Die Untertitel-Logik (`audio-voice.md` Abschnitt 3.7) pausiert die Text-Anzeige synchron.
9. **Stimme-Bus stummgeschaltet:** Der Voice-Fallback greift (`audio-voice.md` Abschnitt 3.8); die Stimmen-Sidechain wird inaktiv, da keine Stimme abgespielt wird. Das Kommentar-Ducking (−6 dB) bleibt aktiv, weil Kommentare auch als Text-Popups existieren.
10. **Ambience-Loop unterbrochen:** Ein Ambient-Loop (Low) kann von einem High-Sound unterbrochen werden (3.5.3). Nach dem Ende des High-Sounds wird der Loop **nicht automatisch neu gestartet**; er startet erst beim nächsten zyklischen Ambient-Tick oder beim nächsten Betreten der Insel neu. (Deterministisch: Kein versteckter Auto-Restart.)
11. **Sehr kurze SFX (unter 10 ms):** Hover-Sounds (50 ms) und Klicks (100 ms) sind kürzer als die kleinste Budget-Überprüfungsperiode; sie werden dennoch vollständig geprüft. Ein Sound kürzer als die Audio-Blockgröße wird trotzdem als „gespielt" gezählt (kein Sonderfall).
12. **Audio-Settings mit deaktiviertem SFX-Bus:** Ist der SFX-Bus stummgeschaltet, werden alle SFX-Anfragen weiterhin geprüft und belegt, aber unhörbar abgespielt (die Prioritätslogik bleibt konsistent; ein erneutes Einschalten stellt alle laufenden Sound-Wiedergaben sofort wieder her).
13. **Split-Screen-Listener:** Der einzige Listener sitzt an der aktiven Hauptkamera. In einem 8-Spieler-Split-Screen hören alle Spieler dieselbe räumliche Perspektive; das ist gewollt (kein eigenes Audio je Viewport).

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `audio-overview.md` | Art | Verwendung |
|-----------------------------------|-----|------------|
| `design/gdd/technical-architecture.md` | Peer | Definiert das Audio-System als Bestandteil der technischen Architektur; dieses Kapitel spezifiziert dessen Verhalten. |
| `design/gdd/technical-data-structures.md` | Peer | Persistiert die Audio-Einstellungen (Bus-Pegel, `mute_window_unfocus`, Untertitel-Toggle). |
| `design/gdd/ui-overview.md`, `design/gdd/ui-accessibility.md` | Peer | Audio-Einstellungs-UI; Regler für Master/Musik/SFX/Stimme, Untertitel-Toggle, Fokus-Stummschaltung. |
| `design/gdd/vision-pillars.md` | Quelle | Liefert die Pfeiler (Sofort verständlich, Überzeichnet, Interaktiv wirkend, Wiedererkennbar), denen das Audio dient. |
| `design/gdd/glossary.md` | Peer | Terminologie (Busse, Prioritäten, Ducking); Legacy-Begriffe werden nicht verwendet. |
| `design/gdd/board-architecture.md` | Konsument | Liefert die 3D-Positionen der Felder, die Spatial-Audio-Quellen referenzieren. |
| `design/gdd/ui-board.md` | Konsument | Kamera-Führung bestimmt die Listener-Position (3.7). |

### 6.2 Systeme, die von diesem Dokument abhängen

| System/Kapitel | Art der Abhängigkeit |
|----------------|----------------------|
| `audio-music.md` | Nutzt die Bus-Struktur (Musik-Bus), die Crossfade-Zeiten (3.8) und das Ducking (3.4) für alle Musikübergänge. |
| `audio-sfx.md` | Nutzt das SFX-Stimmen-Budget (3.5), den 3D-Pool (3.6), Spatial Audio (3.7) und die SFX-Format-Tiers (3.2). |
| `audio-voice.md` | Nutzt den Stimme-Bus (3.1), die Stimmen-Sidechain (3.4) und das Voice-Fallback (Stimme-Bus-Mute). |
| `technical-architecture.md` | Muss das Audio-System (Busse, Pool, Stimmen-Manager) als Systembaustein führen. |
| `Global.gd` | Implementiert `mute_window_unfocus` (3.9). |
| Minispiel-Szenen | Nutzen die Übergänge Board → Minispiel und Minispiel → Board (3.8). |

### 6.3 Bidirektionalität

Die drei Audio-Kapitel verweisen wechselseitig auf dieses Kapitel: `audio-music.md`, `audio-sfx.md` und `audio-voice.md` nennen die Bus-Struktur, das Ducking und die Budget-Regeln als Grundlage; dieses Kapitel verweist auf die drei Kapitel für die konkreten Inhalte. `ui-accessibility.md` und `ui-overview.md` verweisen auf die Audio-Einstellungen; dieses Kapitel verweist zurück. Änderungen an der Bus-Struktur, den Crossfade-Zeiten oder dem Ducking erfordern eine synchrone Prüfung aller vier Audio-/UI-Kapitel.

### 6.4 Design-Entscheidungen (dokumentierte Klärungen)

1. **Ducking-Konflikt (Kommentar vs. Stimme):** Das Konzept nennt für ArenaStar-Kommentare `−6 dB` (Überblick) und für die Stimmen-Sidechain `−8 dB` (Stimm-Kapitel). Klärung: Beide Werte sind gültig, bezeichnen aber **verschiedene Ducking-Quellen**. Das Kommentar-Ducking (`−6 dB`) gilt für jeden ausgelösten Kommentar (Text oder Stimme); die Stimmen-Sidechain (`−8 dB`) gilt, sobald der Stimme-Bus aktiv ist. Beide addieren sich nicht; der stärkste aktive Betrag gewinnt (Formel 4.2).
2. **Crossfade Victory → Menü:** Das Konzept spezifiziert nur vier Übergänge. Klärung: Für die Rückkehr von der Siegerehrung ins Menü wird symmetrisch `1,0 s` verwendet (Ergänzung in Tabelle 3.8).
3. **Fokus-Stummschaltung und Stimme:** Die Fokus-Stummschaltung betrifft nur SFX und Musik; eine laufende Stimme-Zeile wird nicht abgeschnitten (3.9). Begründung: Ein begonnener Satz soll nicht mitten im Wort abbrechen; die Stummschaltung dient der Diskretion, nicht der Sprachunterbrechung.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Master-Pegel | Kurve | Stumm bis 0 dB | 0 dB | Gesamtlautstärke; einziger Regler für die Gesamtlautheit. |
| Musik-Bus-Pegel | Kurve | −∞ bis 0 dB | −6 dB | Lautstärke der Musik relativ zur Gesamtmischung. |
| SFX-Bus-Pegel | Kurve | −∞ bis 0 dB | −3 dB | Lautstärke aller Effekte; höher = präsenteres Feedback. |
| Stimme-Bus-Pegel | Kurve | −∞ bis 0 dB | −3 dB | Lautstärke von ArenaStar und Charakteren. |
| `V_total` (SFX-Budget) | Kurve | 8–24 Stimmen | 16 | Polyphonie-Spielraum; höher = mehr gleichzeitige Sounds, riskiert Maskierung und CPU-Last. |
| Verteilung Critical/High/Low | Kurve | Summe = `V_total` | 2/8/6 | Prioritätsverhalten bei voller Auslastung. |
| Kommentar-Ducking `D_K` | Kurve | 3–9 dB | 6 dB | Wie stark Musik bei Kommentaren zurücktritt. |
| Popup-Ducking `D_P` | Kurve | 2–6 dB | 3 dB | Wie stark Musik bei reinen Popups zurücktritt. |
| Stimmen-Sidechain `D_S` | Kurve | 4–12 dB | 8 dB | Wie stark Musik bei aktiver Stimme zurücktritt. |
| Ducking-Attack/Release (Kommentar) | Feel | 50–250 ms / 150–600 ms | 100 / 300 ms | Wie schnell das Ducking ein- und ausklingt. |
| Ducking-Attack/Release (Stimme) | Feel | 20–150 ms / 100–500 ms | 50 / 200 ms | Sprachverständlichkeit vs. hörbares Pumpen. |
| Crossfade-Zeiten | Feel | 0,2–3,0 s je Übergang | siehe 3.8 | Übergangs-Charakter; Victory 1,5 s ist bewusst dramatisch. |
| `mute_window_unfocus` | Gate | an/aus | an | Ob Fokus-Verlust SFX+Musik stummschaltet. |
| `t_Reconnect` | Gate | 1–10 s | 3 s | Wartezeit vor Wechsel auf das Standardgerät. |
| `t_Retry` | Gate | 1–20 s | 5 s | Wiederholungsintervall bei fehlendem Gerät. |
| Ambience-Breite (Stereo-Verbreiterung) | Feel | 0–100 % | 50 % | Räumliche Breite der Ambience-Loops. |
| Ambience-Qualitätsausnahme | Gate | q=2 oder q=3 | q=2 | Erlaubt höhere Vorbis-Qualität für Ambience-Loops bei hörbarem Qualitätsverlust. |
| LUFS-Ziele | Kurve | je ± 2 LUFS | siehe 3.12 | Gesamtlautheit; ändert die gefühlte Mischbalance. |

Alle Knobs liegen in Konfigurationsdaten (Audio-Settings, zentrale Audio-Konfigurationsdatei), nicht im Code. Änderungen an `V_total`, der Prioritätsverteilung oder dem Ducking erfordern eine Neuvalidierung der Formeln 4.1 und 4.2 sowie eine Hörprüfung der kritischen Mischstellen (UI-Feedback unter Musik, Sprache unter Musik).

## 8. Acceptance Criteria

Ein QA-Tester (oder CI-Hook) kann die folgenden Prüfungen ausführen (PASS/FAIL):

1. **Bus-Struktur:** Beim Start des Spiels existieren exakt die Busse Master, Musik, SFX, Stimme mit den Sollpegeln 0 / −6 / −3 / −3 dB (relativ zu Master). PASS/FAIL.
2. **Dateiformate:** Alle ausgelieferten Audio-Dateien sind Ogg-Vorbis mit den Kategorie-Tiers (Musik q=4, SFX q=2, Stimme q=3) und den Kanalzahlen aus 3.2/3.3. Ein Validierungs-Skript prüft alle Dateien in `assets/audio/`. PASS/FAIL.
3. **Stimmen-Budget:** In einer aufgezeichneten 4-Spieler-Partie überschreitet die Anzahl gleichzeitiger SFX-Stimmen nie 16. PASS/FAIL (Log-Analyse).
4. **Prioritäts-Diebstahl:** Bei voller Auslastung (16 Stimmen, davon alle Low belegt) wird eine neue High-Anfrage durch Unterbrechung des ältesten Low-Sounds abgespielt; eine neue Low-Anfrage wird verweigert. PASS/FAIL (Autotest mit kontrollierter Sound-Sequenz).
5. **Critical-Reservierung:** Zwei gleichzeitige Critical-Sounds spielen immer; ein dritter unterbricht den ältesten Critical-Sound; keine Critical-Anfrage wird verweigert. PASS/FAIL.
6. **Ducking:** Während eines ArenaStar-Kommentars sinkt der Musik-Pegel um 6 dB (Text) bzw. 8 dB (Stimme) mit den spezifizierten Zeitkonstanten; gleichzeitige Quellen ergeben den maximalen Betrag, nie die Summe. PASS/FAIL (Pegel-Messung an den Bus-Outputs).
7. **Spatial Audio:** Ein Schritt-Sound in 1 Einheit Entfernung erklingt mit Referenzlautstärke; bei 15 Einheiten ist er unhörbar; die Lautstärke folgt der inversen Distanz. PASS/FAIL (Hörprüfung + Pegel-Messung bei 1, 5, 10, 15 Einheiten).
8. **Crossfade-Dauern:** Die Übergänge Menü→Board (1,0 s), Board→Minispiel (0,5 s), Minispiel→Board (0,3 s), Board→Victory (1,5 s), Victory→Menü (1,0 s) haben die exakten Dauen; die Pegelsumme bleibt während des Fades konstant (Equal-Power). PASS/FAIL (Timer-Messung).
9. **Fokus-Verlust:** Bei Fokus-Verlust werden SFX und Musik stummgeschaltet, Stimme nicht; bei Rückkehr werden die vorherigen Pegel sofort wiederhergestellt. PASS/FAIL.
10. **Geräte-Wechsel:** Simulierter Geräte-Verlust pausiert alle Sounds; ein innerhalb von 3 s verfügbares Gerät setzt die Wiedergabe fort; ohne Gerät wechselt das System nach 3 s auf das Standardgerät und wiederholt alle 5 s. PASS/FAIL (Simulation mit deaktiviertem Default-Device).
11. **Namenskonvention:** Jede Datei in `assets/audio/` erfüllt die Namenskonvention `[kategorie]_[kontext]_[name]_[variante].[ext]`. PASS/FAIL (CI-Hook).
12. **Lautheit:** Die integrierte Lautheit der ausgelieferten Musik-/SFX-/Stimmen-Dateien liegt innerhalb ±2 LUFS der Ziele aus 3.12; kein True Peak über −1 dBTP. PASS/FAIL (Messung mit Loudness-Analyzer).
13. **Erlebbar (Experiential):** Ein Testspieler kann bei laufendem Spiel mit geschlossenen Augen zwischen Menü, Board und Minispiel unterscheiden (Musikwechsel), einen Stern-Kauf hören (SFX) und ArenaStar verstehen, während Musik läuft (Ducking). Protokoll mit mindestens 5 Testspielern, Ziel: Median ≥ 4 von 5 für „Ich habe ArenaStar immer verstanden". PASS/FAIL.
