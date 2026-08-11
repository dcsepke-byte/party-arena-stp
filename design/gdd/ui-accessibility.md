# UI-Accessibility — Party Arena Game Bible

> **Teil:** VII — UI/UX
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/ui-overview.md, design/gdd/vision-pillars.md

---

## 1. Overview

Dieses Kapitel spezifiziert die Barrierefreiheit (Accessibility) von Party Arena. Es definiert verbindliche Standards für Untertitel, Textgrößen, Farbenblind-Modi (Protanopie, Deuteranopie, Tritanopie), Kontrast-Modus, Screen-Shake-Reduktion, Motion-Sickness-Einstellungen, kombinierte Eingabe-Hilfe (Gamepad + Tastatur gleichzeitig), Controller-Remapping, Mono-Audio, den Schwierigkeits-Assist für Kinder ab 6 Jahren, die Pause-Zeit-Regeln und das Prinzip "Spieler nie nur über Farbe unterscheiden" (Form/Symbol-Fallback). Ziel ist, dass Party Arena mit **einer Eingabequelle (Tastatur ODER Gamepad) vollständig spielbar** ist, dass alle Informationen mindestens zwei Kanäle haben (Text+Icon, Farbe+Form, Audio+Untertitel) und dass einseitig hörende, farbenblinde, bewegungsempfindliche oder ungeübte Spieler (Kinder, Großeltern) ohne Anpassung des Spielprinzips mitspielen können. Alle Regelungen greifen zusätzlich zu den Regeln aus [ui-overview.md](ui-overview.md); wo sie kollidieren, hat dieses Kapitel Vorrang (Accessibility schlägt Ästhetik).

## 2. Player Fantasy

Die Barrierefreiheit von Party Arena soll sich für den Spieler so anfühlen wie ein **Gastgeber, der jeden Gast bedenkt**: "Egal wie du spielst, ob mit Tastatur, Gamepad, mit oder ohne Rot-Grün-Sehen, mit empfindlichem Gleichgewicht oder als Sechsjährige — du bist willkommen und kannst sofort mitspielen." Es gibt keine abgetrennte "Behinderten-Ecke": Die Einstellungen sind Teil des normalen Menüs, und die Effekte (große Schrift, kräftige Konturen, Symbole neben Farben) machen das Spiel für **alle** klarer, nicht nur für Betroffene. Die emotionale Note ist **Selbstverständlichkeit**: Niemand muss erklären, dass er Hilfe braucht — die Unterstützung ist schlicht da. Dies ist kein Add-on, sondern ein Kernversprechen der Marke ("Party für alle") und ein direkter Ausdruck des Pfeilers "Sofort verständlich".

## 3. Detailed Rules

### 3.1 Untertitel

- **Geltungsbereich:** Alle ArenaStar-Kommentare (Voice) sowie alle wichtigen gesprochenen Ansagen erscheinen als Text. Dazu gehören: Menü-Kommentare ([ui-mainmenu](ui-mainmenu.md) 3.9), HUD-Kommentare ([ui-hud](ui-hud.md) 3.8), Shop-Kommentare ([ui-shop](ui-shop.md) 3.3/3.6), Moderation von Minispielen und Siegerehrung.
- **Toggle:** In den Einstellungen (Untermenü "Bedienung", Reiter "Barrierefreiheit") ein-/ausschaltbar. Standard: **an**.
- **Darstellung:** Untertitel erscheinen als zentrierte, schwarz umrandete weiße Schrift (`font_body`, Mindestkontrast 4,5:1) am unteren Bildschirmrand (Ebene 30, [ui-overview](ui-overview.md) 3.2), überlappen das HUD nicht und werden bei aktiver ArenaStar-Sprechblase nicht doppelt eingeblendet (die Sprechblase selbst gilt als Untertitel, wenn sie am selben Ort erscheint; siehe Edge Case 1).
- **Nicht-verbale Hinweise:** Wichtige Soundereignisse (z. B. "Item gekauft") haben kein Untertitel-Pendant, da sie durch Icon/Zähler visuell abgebildet sind.

### 3.2 Textgrößen (3 Stufen)

- **Stufen:** Normal (Multiplikator `t_text = 1,0`), Groß (`1,25`), Sehr Groß (`1,5`).
- **Wirkung:** Der Multiplikator skaliert **ausnahmslos alle UI-Texte** ([ui-overview](ui-overview.md) 3.3.2), inklusive HUD-Zähler, Tooltips, Untertitel und Minispiel-Anweisungen.
- **Layout:** Layouts müssen bei allen 3 Stufen funktionsfähig bleiben (kein Abschneiden, keine überlappenden Elemente). Elemente mit festen Mindestbreiten (z. B. Buttons) wachsen mit der Schrift.
- **Einstellung:** Im Untermenü "Bedienung" → "Barrierefreiheit". Standard: Normal.
- **Interaktion mit Auflösung:** Die Mindestgrößen-Regel (effektiv ≥ 16 px, [ui-overview](ui-overview.md) 4.2) gilt in allen Stufen.

### 3.3 Farbenblind-Modi

Es gibt drei Farbenblind-Modi plus den Normal-Modus. Der Modus wird in den Einstellungen gewählt; **alle UI-Elemente passen sich an** (Spielerfarben, Feld-Markierungen, HUD-Akzente, Minimap-Punkte, Charakter-Auswahl).

**Gemeinsame Grundregeln:**

1. In allen Modi bleibt das **Form-/Symbol-Fallback** (3.9) aktiv bzw. wird erzwungen.
2. Feld-Typen sind ohnehin über Form + Icon unterscheidbar ([ui-board](ui-board.md) 3.8, [vision-pillars](vision-pillars.md) 3.4); die Farbenblind-Modi ändern an der Feld-Erkennbarkeit nichts.
3. Jede Modus-Änderung ist sofort wirksam (kein Neustart nötig) und wird gespeichert.

**Protanopie (Rot-Grün, erster Typ):**
- Spieler-Farben werden **durch Symbole ergänzt**: Jeder Spieler erhält ein festes Symbol-Badge (3.9), das permanent neben Portrait, Name und Marker sichtbar ist. Dies ist die primäre Maßnahme.
- Zusätzlich wird der Rot-Anteil der Spielerfarbe P1 (Rot) abgeschwächt (Helligkeit um 15 % erhöht), damit sie sich vom Grün (P4) stärker über die Helligkeit unterscheidet — die Symbole tragen die Hauptlast.

**Deuteranopie (Rot-Grün, zweiter Typ):**
- Alternative Farbpalette mit **Blau/Gelb-Betonung** wird auf die 8 Spielerfarben angewendet (Remap-Tabelle 4.1).
- Symbole sind ebenfalls Pflicht.

**Tritanopie (Blau-Gelb):**
- Alternative Farbpalette mit **Rot/Grün-Betonung** (Remap-Tabelle 4.2).
- Symbole sind ebenfalls Pflicht.

### 3.4 Kontrast-Modus

- **Toggle:** "Hoher Kontrast" in den Einstellungen. Standard: **aus**.
- **Wirkung:**
  - Alle Panel-/Button-Outlines werden von 3 px auf **5 px schwarze Outlines** verstärkt (`#000000`).
  - Alle Texte werden auf **Weiß** (`#FFFFFF`) auf dunklem Grund (`#000000` oder `bg_e0`) gesetzt; `text_secondary` wird aufgehellt (Kontrast ≥ 7:1).
  - Der Fokus-Rahmen wird auf 3 px verstärkt und zusätzlich in `primary`-Gelb eingefärbt (bei weißem Grund wechselt er zu Schwarz).
  - Icons erhalten eine schwarze Outline (2 px).
- **Geltungsbereich:** Betrifft alle Screens, Overlays, Tooltips und Untertitel; keine Ausnahmen.

### 3.5 Screen-Shake-Reduktion

- **Einstellung:** 3 Stufen: 0 % (aus), 50 % (Standard), 100 % (voll).
- **Wirkung:** Der Screen-Shake des Spiels (z. B. bei Ereignissen, Minispiel-Effekten, Explosionen) wird mit dem gewählten Faktor skaliert. Bei 0 % ist jeglicher Screen-Shake deaktiviert (Kamera bleibt ruhig); bei 50 % ist die Amplitude halbiert.
- **Geltungsbereich:** Alle Quellen von Screen-Shake im gesamten Spiel (Board, Minispiele, Siegerehrung).
- **Umsetzung als Multiplikator:** Formel 4.3.

### 3.6 Motion-Sickness — Reduzierte Bewegung

- **Toggle:** "Reduzierte Bewegung" in den Einstellungen. Standard: **aus**.
- **Wirkung (kumulativ):**
  - **Kamera:** Das Smooth-Follow der Board-Kamera ([ui-board](ui-board.md) 3.1) entfällt; die Kamera springt hart auf die Zielposition (kein Lerp).
  - **Transitionen:** Alle Slide- und Zoom-Transitionen ([ui-overview](ui-overview.md) 3.8) werden auf 100-ms-Fades reduziert (keine Einflug- oder Vergrößerungsbewegungen). Die Shop-Einstiegs-Animation ([ui-shop](ui-shop.md) 3.1) wird zu einem Fade.
  - **UI-Animationen:** Puls-/Rotations-Animationen, die Bewegung erzeugen (Logo-Puls, Portrait-Rotation), werden auf statische Darstellung reduziert (Logo ohne Puls, Portrait als Standbild, aber weiterhin mit Zustandsfarben).
- **Nicht betroffen:** Spieler-Marker-Bewegungen auf dem Board und Minigame-Bewegungen bleiben unverändert (sie sind spielnotwendig); die Einstellung dämpft nur **nicht-notwendige** Kamerabewegung.
- **Ausnahme:** Der Zoom selbst (3 Stufen) bleibt erhalten ([ui-board](ui-board.md) 3.2) — er gilt als Nutzeraktion, nicht als automatische Bewegung.

### 3.7 Eingabe-Hilfe (kombinierte Button-Beschriftung)

- **Regel:** Jeder Button, der eine Aktion auslöst, zeigt **Gamepad- UND Tastatur-Binding gleichzeitig**, z. B. "A / Enter", "B / Esc", "START / P".
- **Reihenfolge:** "Gamepad / Tastatur"; bei erkanntem Controller wird das Gamepad-Label layout-korrekt angezeigt (Xbox/PlayStation/Nintendo, [ui-overview](ui-overview.md) 3.5).
- **Geltungsbereich:** Alle Screens und Overlays (Hauptmenü, Shop, Pfadwahl, Pause, Minispiel-Anweisungen).
- **Zusätzlich:** Eine Eingabe-Übersicht ("Steuerung ansehen") ist im Pause-Menü und in den Einstellungen abrufbar; sie listet alle Aktionen mit beiden Bindings.
- **Remapping-Wirkung:** Ändert der Spieler ein Binding ([ui-overview](ui-overview.md) 3.5), aktualisieren sich alle Beschriftungen live.

### 3.8 Controller-Remapping

- **Geltungsbereich:** Alle Aktionen aus [ui-overview](ui-overview.md) 3.5 sind umbelegbar (Bestätigen, Abbrechen, Navigation, Pause, Tab links/rechts, Toggle, Kamera-Toggle).
- **Einstellungsort:** Einstellungen → Eingabe → Controller-Mapping.
- **Regeln:**
  - Jede Aktion ist frei belegbar; eine Taste kann mehreren Aktionen zugeordnet werden (Konflikt wird als Warnung angezeigt, aber nicht blockiert).
  - "Auf Standard zurücksetzen" stellt die Default-Belegung wieder her.
  - Das Mapping wird pro Eingabetyp getrennt gespeichert (Gamepad-Layouts und Tastatur getrennt).
  - Konflikte mit `ui_pause` sind erlaubt, aber der Spieler wird gewarnt ("Diese Taste ist auch für Pause belegt").
- **Tastatur:** Auch Tastatur-Bindings sind umbelegbar (einschließlich der Zifferntasten 1/2/3 für Item-Slots).

### 3.9 Spieler-Farben — nie nur über Farbe

- **Grundprinzip:** Die 8 Spieler unterscheiden sich NIE ausschließlich durch Farbe. Jeder Spieler hat ein festes **Form-/Symbol-Fallback**:

| Spieler | Symbol |
|---------|--------|
| P1 | Kreis |
| P2 | Stern |
| P3 | Dreieck |
| P4 | Quadrat |
| P5 | Herz |
| P6 | Raute |
| P7 | Halbmond |
| P8 | Blitz |

- **Anzeige:**
  - **Immer sichtbar** an allen kritischen Orten: HUD-Portraits ([ui-hud](ui-hud.md) 3.2), Minimap-Punkte ([ui-hud](ui-hud.md) 3.10), Split-Screen-Panels, Siegerehrung.
  - **Optional im Normal-Modus:** In "Barrierefreiheit" kann "Symbole anzeigen" deaktiviert werden (Standard: **an**, Empfehlung: immer an).
  - **Pflicht in allen Farbenblind-Modi** und im Kontrast-Modus; dort nicht ausblendbar.
- **Zusätzlich:** Namensschilder ([ui-board](ui-board.md) 3.7) tragen den Spielernamen als zweiten Kanal.

### 3.10 Mono-Audio

- **Toggle:** "Mono-Audio" in den Einstellungen → Audio. Standard: **aus**.
- **Wirkung:** Alle Stereo-Sounds werden auf Mono heruntergemischt (Mischung beider Kanäle zu gleichen Teilen), sodass spielrelevante Informationen nicht nur auf einem Ohr ankommen. Betrifft alle Busse (Master, Musik, SFX, Stimme, UI).
- **Hinweis:** Mono-Audio betrifft nur die Wiedergabe; es wird keine separate Sound-Inszenierung für Mono erzeugt (das Mischen ist ausreichend, da Party Arena keine links/rechts-kritischen Sound-Puzzle hat).

### 3.11 Schwierigkeits-Assist (für Kinder ab 6)

- **Toggle:** "Schwierigkeits-Assist" in den Einstellungen → Barrierefreiheit. Standard: **aus**.
- **Wirkung bei aktiviertem Assist:**
  1. **Vereinfachte Minispiel-Regeln als Text-Popup:** Vor jedem Minispiel ([minigame-categories.md](minigame-categories.md)) erscheint ein kurzes Popup mit der Regel in einfacher Sprache (max. 2 Sätze) plus einem Symbol-Diagramm; der Spieler bestätigt mit `ui_accept` (kein Timer auf dem Popup).
  2. **Verlängerte Timelimits (+10 s):** Alle Minispiel- und Reaktions-Timer werden um 10 Sekunden verlängert (Formel 4.4).
  3. **Auto-Würfel nach 5 s Inaktivität:** Ist der aktive Spieler 5 s untätig (kein Tastendruck im Würfel-/Auswahl-Schritt), würfelt das Spiel automatisch für ihn. Bei der Abzweigungs-Auswahl wird bei 5 s Inaktivität der erste (priorisierte) Zweig gewählt ([ui-board](ui-board.md) 3.5). Die Auto-Würfel-Funktion wird mit einem Zähler angezeigt ("Würfelt automatisch in 5 … 4 …").
- **Geltungsbereich:** Assist wirkt nur auf Zeitsysteme und Regelerklärungen; er verändert keine Würfelwahrscheinlichkeiten, Preise oder Siegbedingungen (kein versteckter "Kindermodus" mit anderen Spielregeln).
- **Zielgruppe:** Ab 6 Jahren; die Einstellung ist bewusst einfach gehalten (ein Schalter).

### 3.12 Pause-Zeit

- **Singleplayer:** Pause ist **unbegrenzt** (kein Timer, keine Auto-Fortsetzung).
- **Multiplayer (lokal oder online):** Pause ist auf **60 s** begrenzt; danach erfolgt **Auto-Resume** (das Spiel wird automatisch fortgesetzt).
  - Anzeige: Ein Countdown im Pause-Menü (ab 10 s rot, letzte 5 s hörbare Ticks).
  - Grund: Eine einzelne Pause darf eine Multiplayer-Partie nicht unbegrenzt blockieren.
- **Verhalten:** Die Pause-Zeit läuft nur, während das Pause-Menü geöffnet ist; Öffnen/Schließen pausiert den Countdown nicht (er läuft kontinuierlich in der Pause).
- **Kombination mit Assist:** Der Schwierigkeits-Assist ändert die Pause-Zeit nicht.

### 3.13 Verbindliche Mindeststandards (Querschnitt)

1. **Tastatur-only spielbar:** Das komplette Spiel (Menü, Lobby, Charakter-Auswahl, Board, Minispiele, Shop) ist ohne Maus und ohne Gamepad spielbar.
2. **Gamepad-only spielbar:** Das komplette Spiel ist ohne Maus und ohne Tastatur spielbar.
3. **Kein Blitzen ohne Warnung:** Inhalte mit schnellem, hellem Blitzen (mehr als 3 Blitze pro Sekunde) sind verboten; gibt es dennoch eine Szene mit Blitz-Risiko, wird vor dem ersten Blitz eine Warnung eingeblendet und das Blitzen ist überspringbar.
4. **Keine reine Farb-Kodierung:** Keine Information (Spieler, Feld, Zustand, Warnung) wird ausschließlich über Farbe transportiert (3.9, [ui-overview](ui-overview.md) 3.9).
5. **UI-Skalierung:** Alle UI-Elemente skalieren bei allen unterstützten Auflösungen korrekt ([ui-overview](ui-overview.md) 3.4).

## 4. Formulas

### 4.1 Deuteranopie-Remap-Tabelle

`F_d(i) = ersatzfarbe_i` für Spieler `i` (1–8)

| Spieler | Standard | Deuteranopie-Ersatz |
|---------|----------|---------------------|
| P1 | `#E53935` (Rot) | `#1565C0` (kräftiges Blau) |
| P2 | `#F57C00` (Orange) | `#FDD835` (Gelb) |
| P3 | `#C0CA33` (Limette) | `#00ACC1` (Türkis) |
| P4 | `#43A047` (Grün) | `#FFB300` (Amber) |
| P5 | `#26A69A` (Mint) | `#64B5F6` (helles Blau) |
| P6 | `#1E88E5` (Blau) | `#7E57C2` (Violett) |
| P7 | `#8E24AA` (Violett) | `#EC407A` (Magenta) |
| P8 | `#EC407A` (Pink) | `#9E9D24` (Oliv) |

- Die Tabelle ist der Ausgangspunkt; die maßgebliche Prüfung ist die Unterscheidbarkeit unter Deuteranopie-Simulation (Akzeptanzkriterium 10). `F_d(i) ≠ F_d(j)` für alle `i ≠ j`.

### 4.2 Tritanopie-Remap-Tabelle

`F_t(i) = ersatzfarbe_i` für Spieler `i` (1–8)

| Spieler | Standard | Tritanopie-Ersatz |
|---------|----------|-------------------|
| P1 | `#E53935` (Rot) | `#D32F2F` (Rot, bleibt) |
| P2 | `#F57C00` (Orange) | `#E64A19` (Rot-Orange) |
| P3 | `#C0CA33` (Limette) | `#7CB342` (Grün) |
| P4 | `#43A047` (Grün) | `#2E7D32` (dunkles Grün) |
| P5 | `#26A69A` (Mint) | `#009688` (Blaugrün) |
| P6 | `#1E88E5` (Blau) | `#5E35B1` (Indigo) |
| P7 | `#8E24AA` (Violett) | `#C2185B` (Purpur-Rot) |
| P8 | `#EC407A` (Pink) | `#F06292` (helles Pink) |

- Gleiche Prüfpflicht wie 4.1.

### 4.3 Screen-Shake-Multiplikator

`A_eff = A_max × q`, mit `q ∈ {0,0; 0,5; 1,0}`

- `A_max` = unskalierte Shake-Amplitude, `A_eff` = tatsächlich angewandte Amplitude, `q` = gewählte Stufe (0 % / 50 % / 100 %).
- Beispiel: `A_max = 20 px` bei `q = 0,5` → `A_eff = 10 px`; bei `q = 0` → `A_eff = 0 px`.
- Akzeptanz: Bei `q = 0` ist in keiner Szene eine Kamera-Bewegung durch Screen-Shake messbar (± 0 px).

### 4.4 Assist-Timer

`T_assist = T_standard + 10 s`

- `T_standard` = Original-Timer eines Minispiels oder Reaktionsschritts, `T_assist` = verlängerter Timer bei aktivem Assist.
- Beispiel: Minispiel mit 30 s → `T_assist = 40 s`.
- Akzeptanz: Alle Timer (inkl. Anzeige und Ablauf-Logik) verwenden `T_assist`; es gibt keinen Timer, der bei aktivem Assist die Originalzeit verwendet.

### 4.5 Auto-Würfel-Verzögerung

`T_auto = 5 s` (Inaktivität bis zum automatischen Würfel / zur Auto-Wahl)

- `T_auto` = Zeitspanne ohne Eingabe, nach der automatisch gewürfelt bzw. der erste Zweig gewählt wird.
- Akzeptanz: Bei aktivem Assist würfelt das Spiel nach genau 5 s Inaktivität; ein Tastendruck innerhalb der 5 s bricht den Auto-Vorgang ab und übergibt die Kontrolle an den Spieler.

### 4.6 Pause-Countdown (Multiplayer)

`T_pause = max(60 s − (t − t_pause), 0)`

- `t_pause` = Zeitpunkt des Pause-Eintritts, `t` = aktuelle Zeit.
- Akzeptanz: Bei `T_pause = 0` wird das Spiel automatisch fortgesetzt; der Countdown läuft nur, solange das Pause-Menü geöffnet ist.

## 5. Edge Cases

1. **Untertitel + ArenaStar-Sprechblase gleichzeitig:** Zeigt ArenaStar bereits eine Sprechblase mit demselben Text, wird der Untertitel nicht doppelt eingeblendet; die Sprechblase gilt als Untertitel. Ändert sich der Text (nächster Kommentar), aktualisieren sich beide synchron.
2. **Textgröße "Sehr Groß" in der HUD-Leiste bei 8 Spielern:** Bei `t_text = 1,5` wachsen die Zähler; die Slots werden breiter (Slot-Pitch wird dynamisch erhöht, [ui-hud](ui-hud.md) 4.1), bis die Leiste die volle Breite nutzt. Überschreitet die Summe die Bildschirmbreite, werden die Zähler in zwei Zeilen (Münzen über Sterne) gesetzt — kein Abschneiden.
3. **Farbenblind-Modus wechselt während einer laufenden Partie:** Der Wechsel ist sofort wirksam; Spielerfarben, Minimap-Punkte und Marker remappen live. Bereits platzierte Marker ändern ihre Farbe ohne Neupositionierung (Position bleibt deterministisch).
4. **Kontrast-Modus + Spielerfarben:** Der Kontrast-Modus verstärkt Outlines, ersetzt aber nicht die Spielerfarben; die Unterscheidbarkeit bleibt über Farbe **und** Symbol (3.9) gegeben.
5. **Mono-Audio + Voice:** Bei Mono-Audio wird auch ArenaStars Stimme mono abgespielt; die Untertitel (3.1) bleiben als zweiter Kanal erhalten.
6. **Assist bei Kooperations-Minispielen:** Das Regel-Popup erscheint auch vor Kooperations-Minispielen ([minigame-categories.md](minigame-categories.md)) und erklärt das gemeinsame Ziel in 2 Sätzen; die +10-s-Verlängerung gilt für alle Spieler gleichzeitig.
7. **Auto-Würfel vs. Item-Nutzung:** Der Auto-Würfel nach 5 s zählt auch, wenn der Spieler ein Item auswählen könnte; er würfelt ohne Item (Item-Nutzung ist optional). Der Assist begünstigt damit keine unbeabsichtigte Item-Nutzung.
8. **Pause-Zeit bei Verbindungsabbruch (Online):** Läuft der Pause-Timer während einer Verbindungsunterbrechung weiter, wird die Partie nach Ablauf fortgesetzt (Auto-Resume); der Verbindungs-Dialog ([technical-multiplayer.md](technical-multiplayer.md)) überlagert den Resume-Vorgang nicht.
9. **Remapping-Konflikt mit dem Assist-Auto-Würfel:** Der Auto-Würfel löst unabhängig von der Belegung der Bestätigungstaste aus; er verwendet keine Taste, sondern Inaktivität als Auslöser — es gibt keinen Remapping-Konflikt.
10. **Screen-Shake 0 % bei Minispiel-Effekten:** Auch Minispiel-Explosionen erzeugen bei `q = 0` keinerlei Kamerabewegung; die Effekte bleiben rein visuell/partikelbasiert (kein physikalischer Shake).

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `ui-accessibility.md` | Art | Verwendung |
|--------------------------------------|-----|------------|
| `design/gdd/ui-overview.md` | Dach | Liefert Tokens, Skalierung (4.1/4.2), Fokus-Regeln, ControlHelper (Remapping), Transitionen und die Mindestschriftgröße. |
| `design/gdd/vision-pillars.md` | Quelle | Definiert Silhouetten-/Farbregeln und Farbblind-Tests (Edge Case 4), die hier konkretisiert werden. |
| `design/gdd/glossary.md` | Peer | Definiert Begriffe wie "Signaturfarbe", "Silhouette", "Mikro-Feedback". |
| `design/gdd/ui-hud.md` | Peer | Muss das Symbol-Badge (3.9) in der Spieler-Leiste darstellen. |
| `design/gdd/ui-board.md` | Peer | Muss die Reduzierte-Bewegung-Regel (3.6) in der Kamera umsetzen. |
| `design/gdd/ui-shop.md` | Peer | Muss die kombinierte Eingabe-Hilfe (3.7) und die Slide-Animation (3.6) anpassen. |
| `design/gdd/minigame-*.md` | Nachgeordnet | Müssen Regel-Popups und Timer-Verlängerung (3.11) unterstützen. |
| `design/gdd/audio-overview.md` | Nachgeordnet | Muss Mono-Audio (3.10) und den UI-Bus abbilden. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| Alle `ui-*.md`-Kapitel | Müssen Textgrößen, Kontrast, Farbenblind-Modi, Untertitel und Eingabe-Hilfe erfüllen. |
| Alle `minigame-*.md`-Kapitel | Müssen Assist-Regel-Popups, +10-s-Timer und Screen-Shake-Regeln unterstützen. |
| `design/gdd/audio-*.md` | Muss Untertitel-Kanäle und Mono-Mischung berücksichtigen. |
| `design/gdd/technical-architecture.md` | Muss Remapping, Farbpaletten-Switching und Untertitel-System technisch abbilden. |
| `design/gdd/technical-multiplayer.md` | Muss die 60-s-Pause und Auto-Resume abbilden. |

### 6.3 Bidirektionalität

Die Accessibility-Regeln greifen in jedes UI- und Minigame-Kapitel ein; umgekehrt liefern die Kapitel die konkreten Inhalte, die accessibility-konform aufbereitet werden (z. B. Minispiel-Regeln für das Popup). Wird in einem Kapitel eine Barriere entdeckt (z. B. ein Zustand, der nur über Farbe kodiert ist), wird sie hier als Edge Case ergänzt und im betroffenen Kapitel korrigiert.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Text-Multiplikator-Stufen | Feel | 1,0 / 1,15–1,4 / 1,5–2,0 | 1,0 / 1,25 / 1,5 | Skaliert alle UI-Texte; obere Stufe darf Layouts nicht brechen |
| Kontrast-Outline-Dicke | Feel | 3–7 px | 5 px | Stärke der schwarzen Outlines im Kontrast-Modus |
| Screen-Shake-Stufen `q` | Feel | 0 / 0,25–0,75 / 1,0 | 0 / 0,5 / 1,0 | Dämpfung der Kamerabewegung |
| Assist-Timer-Zuschlag | Gate | +5 bis +20 s | +10 s | Verlängerung aller Timer bei aktivem Assist |
| Auto-Würfel-Verzögerung `T_auto` | Gate | 3–15 s | 5 s | Inaktivitätsdauer bis zum automatischen Würfeln |
| Pause-Countdown (MP) | Gate | 30–120 s | 60 s | Maximale Pausendauer im Multiplayer |
| Untertitel-Mindestgröße | Feel | 16–28 px | 20 px | Basisgröße der Untertitel (skaliert mit Textgröße) |
| Symbol-Anzeige (Normal-Modus) | Gate | an/aus | an | Sichtbarkeit der Spieler-Symbole außerhalb der Farbenblind-Modi |

## 8. Acceptance Criteria

Ein QA-Tester kann folgende Prüfungen ausführen:

1. **Tastatur-only:** Das komplette Spiel (Hauptmenü → Lobby → Charakter-Auswahl → Board → Minispiel → Siegerehrung) ist ohne Maus und ohne Gamepad abschließbar. PASS/FAIL.
2. **Gamepad-only:** Dasselbe ist ohne Maus und ohne Tastatur abschließbar. PASS/FAIL.
3. **Untertitel:** Bei aktivierten Untertiteln erscheint jeder ArenaStar-Kommentar als Text; bei deaktivierten nicht; die Untertitel sind bei `t_text = 1,5` und im Kontrast-Modus lesbar (Kontrast ≥ 4,5:1). PASS/FAIL.
4. **Textgrößen:** In allen 3 Stufen ist jeder Screen ohne abgeschnittene oder überlappende Texte bedienbar; keine UI-Schrift fällt unter die effektive Mindestgröße (16 px). PASS/FAIL.
5. **Farbenblind-Modi:** In jedem der 3 Modi sind alle 8 Spieler über Farbe + Symbol unterscheidbar; die 5 Prüfszenen pro Insel ([vision-pillars](vision-pillars.md) Edge Case 4) bleiben unter der jeweiligen Simulation funktional. PASS/FAIL.
6. **Kontrast-Modus:** Panels/Buttons haben 5-px-schwarze Outlines, Texte sind weiß auf dunklem Grund (≥ 7:1), der Fokus-Rahmen ist gelb und 3 px. PASS/FAIL.
7. **Screen-Shake:** Bei `q = 0` ist keine Kamerabewegung durch Shake messbar; bei `q = 0,5` ist die Amplitude halbiert (Messung gegen `q = 1,0`). PASS/FAIL.
8. **Reduzierte Bewegung:** Bei aktiviertem Toggle springt die Kamera hart (kein Lerp), Transitionen sind ≤ 100-ms-Fades, Logo-Puls und Portrait-Rotation sind statisch; der Zoom bleibt funktional. PASS/FAIL.
9. **Eingabe-Hilfe:** Jeder Aktions-Button zeigt Gamepad- und Tastatur-Label gleichzeitig (z. B. "A / Enter"); nach Remapping aktualisieren sich alle Labels live. PASS/FAIL.
10. **Remapping:** Alle Aktionen sind umbelegbar; "Auf Standard zurücksetzen" stellt die Defaults wieder her; Konflikte erzeugen eine Warnung, aber keinen Abbruch. PASS/FAIL.
11. **Mono-Audio:** Bei aktiviertem Mono-Audio ist auf einem einzelnen Lautsprecher dieselbe Information hörbar wie im Stereo-Modus (Test mit abgeklemmtem Kanal). PASS/FAIL.
12. **Assist:** Bei aktivem Assist erscheint vor jedem Minispiel ein Regel-Popup (max. 2 Sätze), alle Timer sind +10 s verlängert, und nach 5 s Inaktivität würfelt das Spiel automatisch (mit sichtbarem Countdown). PASS/FAIL.
13. **Pause-Zeit:** Im Singleplayer ist die Pause unbegrenzt; im Multiplayer wird nach 60 s automatisch fortgesetzt (Countdown-Anzeige). PASS/FAIL.
14. **Form-/Symbol-Fallback:** In der HUD-Leiste, der Minimap und den Split-Screen-Panels trägt jeder Spieler sein festes Symbol; in den Farbenblind- und Kontrast-Modi ist es nicht ausblendbar. PASS/FAIL.
15. **Erlebbar (Experiential):** Mindestens eine Testperson aus einer unterrepräsentierten Gruppe (Kind ab 6, ältere Person, Farbenblinde/-r, einseitig hörende Person) absolviert eine volle Runde ohne Assistenz; die Partie ist für die Person nachvollziehbar und abschließbar. PASS/FAIL.
