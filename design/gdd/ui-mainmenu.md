# UI-MainMenu — Party Arena Game Bible

> **Teil:** VII — UI/UX
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/ui-overview.md

---

## 1. Overview

Dieses Kapitel spezifiziert das Hauptmenü (Screen `MainMenu`) von Party Arena: den animierten Hintergrund (3D-Szene mit ArenaStar und rotierenden Inseln, optional statisches Key Art), das pulsierende "PARTY ARENA"-Logo, die fünf Menüpunkte (SPIELEN, EINSTELLUNGEN, STATISTIK, CREDITS, BEENDEN) mit ihren Untermenüs, die ArenaStar-Präsenz als kommentierender Begleiter, den Server-Browser für Online-Spiele sowie das Konami-Code-Easter-Egg zur Freischaltung aller Inseln für Tests. Das Hauptmenü ist der erste Eindruck des Spiels und muss die Pfeiler "Sofort verständlich" und "Überzeichnet" unmittelbar erlebbar machen: Innerhalb von 3 Sekunden nach dem Boot sieht der Spieler das Logo, den Menüpunkt SPIELEN und den Fokus darauf. Alle Regeln aus [ui-overview.md](ui-overview.md) gelten verbindlich (Tokens, Fokus, Transitionen, UI-Sound).

## 2. Player Fantasy

Der erste Moment im Spiel soll sich anfühlen wie das Betreten einer großen Spielzeug-Bühne: Eine bunte, schwebende Welt aus Inseln dreht sich im Hintergrund, das Maskottchen ArenaStar winkt und kommentiert jede Menü-Auswahl, und das Logo "PARTY ARENA" pulsiert einladend. Der Spieler soll sofort zwei Dinge wissen: **"Hier kann ich Party spielen"** und **"Was ich als Nächstes tun soll, steht direkt vor mir."** Die emotionale Note ist Vorfreude: Das Menü ist kein Verwaltungsbildschirm, sondern das Foyer der Party — hell, laut, freundlich und mit einem Gastgeber (ArenaStar), der einen begrüßt. Ein erfahrener Spieler erreicht SPIELEN → Lobby in unter 5 Sekunden; ein Neuling versteht die Menüstruktur ohne Anleitung (2-Minuten-Test).

## 3. Detailed Rules

### 3.1 Screen-Aufbau

Der `MainMenu`-Screen besteht aus genau diesen Ebenen (von unten nach oben):

1. **Hintergrund (Ebene 0):** Entweder die animierte 3D-Szene (Standard) oder statisches Key Art (Perfomance-Option, siehe Tuning-Knob 7.4).
2. **Logo (Ebene 1):** "PARTY ARENA" in 3D-Cartoon-Schrift, pulsierend.
3. **Menü-Navigation (Ebene 2):** Vertikale Liste der 5 Menüpunkte.
4. **ArenaStar (Ebene 3):** Kleine 2D/3D-Animation links oder rechts, winkt und kommentiert.
5. **Online-Anzeige (Ebene 4):** Verbindungsstatus + Server-Browser-Zugang in der oberen rechten Ecke.
6. **Version/Footer (Ebene 4):** Build-Version und Godot-Logo klein unten rechts.

### 3.2 Hintergrund

- **Standard:** Eine 3D-Szene mit ArenaStar in der Mitte und den 7 Inseln (Sonnenstrand, Zuckerwald, Wolkenwerk, Frostgipfel, Dschungeltempel, Mechanik-Stadt, Sternenzitadelle), die langsam um ein Zentrum rotieren. Rotationsgeschwindigkeit: eine volle Umdrehung in 120 s (0,5 U/min). Die Inseln leuchten in ihren Signaturfarben.
- **Performance-Option:** Statisches Key Art (gerendertes Standbild der Szene) ersetzt die 3D-Szene. Diese Option wird über den Tuning-Knob in Sektion 7 gesetzt; auf Geräten unterhalb des Performance-Budgets (siehe [technical-performance.md](technical-performance.md)) wird sie automatisch aktiviert.
- Der Hintergrund ist dekorativ und darf den Fokus nie auf sich ziehen: Helligkeit und Bewegung liegen unterhalb des Logo-/Menü-Niveaus (Regel "Vordergrund darf Vorder- sein" aus [vision-pillars.md](vision-pillars.md)).

### 3.3 Logo

- Text: "PARTY ARENA", 3D-Cartoon-Schrift (Komika Axis, aufgewertet mit Tiefe/Glanz).
- Puls-Animation: Skalierung oszilliert mit `A(t) = 1 + 0,04 × sin(2π × 0,5 × t)` (siehe 4.1), Frequenz 0,5 Hz, Amplitude 4 %.
- Farbe: `primary`-Gelb mit dunkler Outline; der Glanz ist dezent animiert (kein Flackern).
- Position: oben mittig, oberhalb der Menüliste; Größe `font_headline` (48 px) oder größer (Logo-Ausnahme).

### 3.4 Menüpunkte und Navigation

Die 5 Menüpunkte erscheinen als vertikale Liste, zentriert, mit `font_button`-Größe. Die Reihenfolge ist fest:

| # | Menüpunkt | Aktion bei Bestätigen | Primär/Sekundär |
|---|-----------|------------------------|-----------------|
| 1 | SPIELEN | Öffnet Lobby (Host/Join + Server-Browser) | Primär |
| 2 | EINSTELLUNGEN | Öffnet SettingsMenu | Sekundär |
| 3 | STATISTIK | Öffnet StatisticsScreen | Sekundär |
| 4 | CREDITS | Öffnet CreditsScreen | Sekundär |
| 5 | BEENDEN | Öffnet ConfirmDialog "Spiel wirklich beenden?" | Sekundär |

Regeln:

1. **First-Focus:** Beim Betreten des MainMenu ist SPIELEN fokussiert.
2. **Fokus-Navigation:** vertikal über die Liste; horizontale Navigation ist nicht definiert (die Menüpunkte sind die einzigen fokussierbaren Elemente der zentralen Ebene).
3. **SPIELEN ist visuell dominant:** größerer Button (125 % Breite/Höhe), `primary`-Farbe, während EINSTELLUNGEN/STATISTIK/CREDITS/BEENDEN als `secondary`-Buttons dargestellt sind.
4. **BEENDEN bestätigt:** Ein Bestätigen auf BEENDEN öffnet sofort einen `ConfirmDialog` (Ebene 20); erst dessen Bestätigung beendet das Spiel. `ui_cancel` schließt den Dialog zurück zum Menü.
5. **Tastatur-Kürzel:** Die Menüpunkte sind zusätzlich über Zifferntasten 1–5 direkt anwählbar (SPIELEN=1 … BEENDEN=5). Bei Gamepad entfällt das Kürzel.

### 3.5 Untermenü EINSTELLUNGEN (SettingsMenu)

Das SettingsMenu ist ein Vollbild-Screen (aus dem Hauptmenü) bzw. ein Overlay (aus dem PauseMenu, siehe [ui-overview.md](ui-overview.md)). Es hat vier Reiter (Tabs), die mit `ui_tab_left/right` oder Klick gewechselt werden:

**Audio:**
- Master-Lautstärke (Schieberegler 0–100 %, Default 100 %)
- Musik (0–100 %, Default 80 %)
- SFX (0–100 %, Default 100 %)
- Stimme (ArenaStar, 0–100 %, Default 100 %)
- Mono-Audio-Umschalter (verweist auf [ui-accessibility](ui-accessibility.md))

**Video:**
- Auflösung (Liste der unterstützten Auflösungen, siehe [ui-overview](ui-overview.md) 3.4)
- Fullscreen (Ein/Aus)
- VSync (Ein/Aus)
- HDR wird nicht angeboten (SDR only, [ui-overview](ui-overview.md) 3.10)

**Sprache:**
- Auswahlliste: Deutsch, English, Français, Español, Português, 日本語, 中文 (DE/EN/FR/ES/PT/JP/ZH)
- Die Sprachauswahl ist sofort wirksam; ein Hinweis "Sprache geändert" erscheint als Toast, die ausgewählte Sprache wird gespeichert.

**Eingabe:**
- Controller-Mapping: alle Aktionen aus [ui-overview](ui-overview.md) 3.5 umbelegbar (siehe [ui-accessibility](ui-accessibility.md) "Controller-Remapping")
- Anzeige des erkannten Controllertyps (Xbox/PlayStation/Nintendo/Tastatur)

Regeln:
1. First-Focus im SettingsMenu ist der Reiter "Audio".
2. Änderungen werden sofort übernommen und beim Verlassen gespeichert; es gibt keinen "Speichern"-Button (kein Bestätigungs-Dialog für Audio/Video/Sprache). Ausnahme: Das Controller-Mapping hat einen eigenen "Auf Standard zurücksetzen"-Button.
3. `ui_cancel` im SettingsMenu führt zurück zum Hauptmenü (bzw. PauseMenu).

### 3.6 Untermenü STATISTIK (StatisticsScreen)

Zeigt die lokal gespeicherte Spielerstatistik an:

| Statistik | Quelle |
|-----------|--------|
| Gesamt-Spiele | Anzahl abgeschlossener Partien |
| Siege | Anzahl Partien, die der lokale Spieler gewonnen hat |
| Lieblingscharakter | Charakter mit den meisten absolvierten Partien (bei Gleichstand: alphabetisch erster) |
| Meistgespielte Insel | Insel mit den meisten absolvierten Partien |
| Münzen gesammelt | Summe aller im Spiel verdienten Münzen (kumuliert) |
| Minispiel-Rekorde | Pro Minispiel: bester erreichter Rang + beste Punktzahl |

Regeln:
1. Die Statistik ist rein informativ; keine Lösch- oder Reset-Funktion im UI (Reset nur über internes Debug-Menü).
2. Liegen noch keine Daten vor, zeigt jeder Eintrag "—" statt 0.
3. First-Focus ist der "Zurück"-Button; `ui_cancel` führt zurück zum Hauptmenü.
4. Speicherung der Statistik: lokal im Savegame; Detailformat in [technical-data-structures.md](technical-data-structures.md).

### 3.7 Untermenü CREDITS (CreditsScreen)

Zeigt eine scrollbare Liste:

- **CCGS Team** (Entwicklungsteam)
- **Danny** (Art)
- **Engine:** Godot 4.2
- **STP-Team** (Fork-Basis: Super Tux Party als Ausgangspunkt)

Regeln:
1. Autoscroll von unten nach oben mit 40 px/s; `ui_accept`/`ui_cancel` beendet den Autoscroll und schließt zum Hauptmenü.
2. First-Focus ist der "Zurück"-Button.
3. Zusätzliche nicht-teambezogene Lizenzen (Fonts, Plugins) erscheinen über einen Unterpunkt "Lizenzen" am Ende der Liste.

### 3.8 SPIELEN → Lobby (Host/Join)

Das Bestätigen von SPIELEN öffnet die `Lobby` mit zwei Wegen:

- **Host:** Neues lokales Spiel erstellen (Spielerzahl 2–8 wählen, Insel und Rundenanzahl wählen).
- **Join:** Server-Browser öffnen.

Der **Server-Browser** zeigt:

- **Lokales Netzwerk:** automatisch erkannte Server (Name, Spielerzahl, Ping) — automatischer Scan alle 5 s.
- **Direkt-IP:** manuelle Eingabe einer IP-Adresse + Port zum Beitreten.

Regeln:
1. First-Focus in der Lobby ist "Host".
2. Der Server-Browser sortiert nach Ping aufsteigend; nicht erreichbare Server werden nach 3 erfolglosen Verbindungsversuchen als "Nicht erreichbar" markiert.
3. Die Lobby-Details (Insel, Runden) spezifiziert [core-loop.md](core-loop.md) und die Board-Kapitel; UI-relevante Punkte der Lobby werden dort bzw. in [ui-character-select](ui-character-select.md) behandelt.

### 3.9 ArenaStar im Hauptmenü

- ArenaStar steht links (bei 16:9) bzw. wahlweise rechts (TUNING), in der unteren Hälfte, und führt Idle-Animationen aus (Winken, Schauen zur Menüauswahl, Hüpfen).
- **Kommentare:** Bei Menü-Auswahl bzw. Fokuswechsel spricht ArenaStar kurze Kommentare (als Sprechblase, siehe "Untertitel" in [ui-accessibility](ui-accessibility.md)). Beispiele:
  - Fokus auf SPIELEN: "Spielen! Gute Wahl!"
  - Fokus auf EINSTELLUNGEN: "Ganz nach deinem Geschmack!"
  - Fokus auf STATISTIK: "Deine Rekorde warten!"
  - Fokus auf CREDITS: "Danke an alle, die Party Arena möglich machen!"
  - Fokus auf BEENDEN: "Schon weg? Bis zum nächsten Mal!"
  - Spiel wird beendet (Dialog bestätigt): "Tschüssi!"
- **Nicht aufdringlich:** Ein Kommentar pro Fokuswechsel; der gleiche Kommentar wird nicht zweimal hintereinander gespielt; die Sprechblase verschwindet nach 3 s oder sobald der Fokus wechselt.
- **Voice:** Kommentare werden gesprochen (Voice-Bus) und als Untertitel eingeblendet, wenn Untertitel aktiv sind ([ui-accessibility](ui-accessibility.md)).
- **Begrüßung:** Beim ersten Start nach dem Boot: "Willkommen in der Party Arena!" (einmalig, danach nur noch beim Betreten des Menüs nach einem beendeten Spiel kürzer: "Schön, dich zu sehen!").

### 3.10 Easter Egg — Konami-Code

Der Konami-Code (oben, oben, unten, unten, links, rechts, links, rechts, B, A) schaltet **alle Inseln für Testing frei** (auch jene, die noch gesperrt sind):

1. **Eingabe:** Die Sequenz wird im MainMenu über Gamepad/Tastatur eingegeben, ohne dass ein Menüpunkt fokussiert sein muss; die Eingabe wird über ein Eingabefenster von 5 s zwischen zwei Tasten gepuffert.
2. **Bestätigung:** Nach dem letzten Zeichen spielt `ui_click` und ein kurzer ArenaStar-Kommentar erscheint: "Alle Inseln freigeschaltet! Viel Spaß beim Testen!"
3. **Wirkung:** Der Freischalt-Status aller Inseln wird für die aktuelle Sitzung auf "freigeschaltet" gesetzt und im Savegame als Debug-Flag gespeichert.
4. **Nur Testzwecke:** Der Code ist in der finalen Auslieferung dokumentiert, aber nicht im UI sichtbar (kein Hinweis).
5. **Keine Fokus-Störung:** Die Code-Eingabe bewegt den Fokus nicht; die Menüpunkte bleiben bedienbar.

### 3.11 Online-Anzeige

- In der oberen rechten Ecke zeigt ein kleines Badge den Netzwerkstatus: "Offline" (grau), "Lokales Netzwerk" (türkis), "Online" (grün).
- Das Badge ist nicht fokussierbar; ein Klick darauf öffnet den Server-Browser.

## 4. Formulas

### 4.1 Logo-Puls

`A(t) = 1 + 0,04 × sin(2π × 0,5 × t)`

- `A(t)` = Skalierungsfaktor des Logos zum Zeitpunkt `t` (Sekunden), `sin` in Radiant.
- Erwartungswert: Amplitude 0,04 (± 4 % Skalierung), Frequenz 0,5 Hz (eine volle Puls-Bewegung pro 2 s).
- Akzeptanz: Die Skalierung bewegt sich dauerhaft innerhalb `A ∈ [0,96; 1,04]`; kein Hüpfen (Sprung in `A`).

### 4.2 Menü-Reaktionszeit

`T_reich = t_spielen → lobby ≤ 5 s`

- `t_spielen → lobby` = Zeit vom Boot-Bildschirm bis zum sichtbaren Lobby-Screen bei sofortigem SPIELEN-Druck.
- Akzeptanz: `T_reich ≤ 5 s` auf Referenzhardware; Überschreitung gilt als Blocker (verletzt "Sofort verständlich").

### 4.3 Server-Browser-Refresh

`T_scan = 5 s` (Refresh-Intervall des LAN-Scans)

- Akzeptanz: Ein im lokalen Netzwerk gestarteter Server erscheint spätestens 2 × `T_scan` = 10 s nach dem ersten Scan im Browser.

### 4.4 Konami-Eingabefenster

`T_konami = 5 s` (maximale Zeit zwischen zwei aufeinanderfolgenden Tasten der Sequenz)

- Akzeptanz: Überschreitet eine Pause zwischen zwei Tasten `T_konami`, wird die bisher eingegebene Sequenz verworfen und die Zählung beginnt von vorn; ein Fehlton (`ui_error`) signalisiert den Abbruch.

### 4.5 Spielerzahl-Skalierung der Lobby-Liste

`B = max(2, min(P, 8))`

- `P` = Anzahl der beigetretenen Spieler in der Lobby.
- Akzeptanz: Die Lobby zeigt für `P ∈ [2,8]` genau `B` aktive Spieler-Plätze; die UI erlaubt nicht weniger als 2 oder mehr als 8 aktive Plätze.

## 5. Edge Cases

1. **Beenden im letzten Moment:** Wird BEENDEN bestätigt und schließt sich der ConfirmDialog, während eine Transition (Lobby-Öffnen) bereits angestoßen wurde, gewinnt der zuletzt bestätigte Befehl; das Spiel beendet sich. Die Transitions-Sperre aus [ui-overview](ui-overview.md) (3.8) verhindert, dass eine gehaltene Taste versehentlich beide Aktionen auslöst.
2. **Kein Speicherstand / erste Partie:** Bei leerem Savegame zeigt STATISTIK überall "—", und die Lobby wählt die Standardwerte (Insel: Sonnenstrand, Runden: 10). Es erscheint kein Fehlerdialog.
3. **Sprachwechsel mit langen Strings:** Deutsche Menüpunkte (z. B. "EINSTELLUNGEN") müssen bei FR/PT ohne Layout-Bruch darstellbar sein; die Buttons haben ausreichende Mindestbreite (siehe [ui-overview](ui-overview.md) Edge Case 4).
4. **Nicht erreichbarer Server:** Wählt der Spieler im Server-Browser einen Server, der beim Verbinden wegfällt, erscheint ein `ConfirmDialog` "Server nicht erreichbar" und der Fokus kehrt in den Server-Browser zurück. Kein Absturz, keine eingefrorene Verbindungsanzeige.
5. **Konami-Code während einer laufenden Partie:** Der Code wirkt nur im MainMenu. In der Lobby und im Spiel wird die Eingabe als normale Navigation behandelt (keine Freischaltung).
6. **ArenaStar-Kommentare bei schnellem Fokus-Scrollen:** Scrollt der Spieler schnell durch alle 5 Menüpunkte, wird nur der Kommentar des zuletzt fokussierten Punktes gespielt (maximal 1 Kommentar pro 800 ms); vorherige werden abgebrochen. Verhindert Kommentar-Spam.
7. **First-Launch:** Beim allerersten Start wird zusätzlich zur Begrüßung ein kurzer Hinweis eingeblendet ("Drücke A / Enter zum Spielen"), der nach dem ersten SPIELEN-Druck nie wieder erscheint.
8. **Auflösungsänderung im SettingsMenu:** Wird die Auflösung geändert, bleibt das SettingsMenu geöffnet; das UI skaliert live über `s` ([ui-overview](ui-overview.md) 4.1). Die Änderung wird erst beim Verlassen gespeichert, ist aber sofort wirksam.
9. **Controller fehlt beim Boot:** Wird kein Gamepad erkannt, zeigt das Eingabe-Untermenü "Tastatur" als aktiven Typ; die Button-Beschriftungen wechseln auf Tastatur-Labels (siehe [ui-overview](ui-overview.md) 3.5).
10. **Zurück-Navigation aus der Lobby:** `ui_cancel` in der Lobby (ohne laufendes Spiel) führt zurück zum MainMenu und setzt den Fokus auf SPIELEN.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `ui-mainmenu.md` | Art | Verwendung |
|--------------------------------|-----|------------|
| `design/gdd/ui-overview.md` | Dach | Liefert Tokens, Fokus-Regeln, Transitionen, Overlay-Ebenen, ControlHelper und UI-Sound, die der MainMenu nutzt. |
| `design/gdd/game-concept.md` | Quelle | Liefert die Inseln (für den Hintergrund), die Charaktere (für Statistik) und das Spielkonzept. |
| `design/gdd/vision-pillars.md` | Quelle | Definiert die Pfeiler, die das Menü (Begrüßung, Lebendigkeit) erfüllen muss. |
| `design/gdd/world-overview.md` | Nachgeordnet | Muss die Inseln für den rotierenden Hintergrund als 3D-Assets spezifizieren. |
| `design/gdd/narrative-arena-star.md` | Nachgeordnet | Muss die ArenaStar-Kommentare und den Voice-Vertrag für das Menü konkretisieren. |
| `design/gdd/ui-accessibility.md` | Nachgeordnet | Setzt Untertitel, Textgröße, Remapping und Kontrast um, die das Menü erfüllen muss. |
| `design/gdd/technical-multiplayer.md` | Nachgeordnet | Muss Lobby-Host/Join und Server-Browser technisch abbilden. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `design/gdd/ui-hud.md` | Übernimmt die in der Lobby gewählte Spielerzahl und die Spielerfarben. |
| `design/gdd/ui-character-select.md` | Wird nach der Lobby aufgerufen; übernimmt die Anzahl der Spieler. |
| `design/gdd/audio-ui.md` | Muss die im Menü verwendeten Sounds (ui_click, ui_open, ArenaStar-Voice) liefern. |
| `design/gdd/audio-music.md` | Liefert die Titel-/Menümusik, die auf dem MainMenu-Screen läuft. |
| `design/gdd/technical-data-structures.md` | Speichert die Statistik- und Freischaltdaten (Savegame), die STATISTIK und Konami-Egg nutzen. |

### 6.3 Bidirektionalität

Das Hauptmenü ist der Einstieg in Lobby und Charakter-Auswahl; die Kapitel [ui-character-select](ui-character-select.md) und die Lobby-Dokumentation müssen den Rücksprung zum Hauptmenü (via `ui_cancel`) als Eingang von `ui-mainmenu.md` behandeln. Die ArenaStar-Kommentare des Menüs und die des HUD ([ui-hud](ui-hud.md)) folgen demselben Voice-Vertrag aus `narrative-arena-star.md`.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Hintergrund-Modus | Performance | `3D-Szene`, `Key Art` | `3D-Szene` | Bestimmt, ob die animierte Insel-Szene oder das Standbild läuft; Performance-Vs-Lebendigkeit |
| Insel-Rotation | Feel | 60–240 s pro Umdrehung | 120 s | Tempo der Hintergrundbewegung; schneller = lebendiger, langsamer = ruhiger |
| Logo-Puls-Amplitude | Feel | 0,02–0,08 | 0,04 | Stärke des Pulsierens; größer = auffälliger |
| Logo-Puls-Frequenz | Feel | 0,25–1,0 Hz | 0,5 Hz | Tempo des Pulsierens |
| Kommentar-Sperrzeit | Feel | 400–1500 ms | 800 ms | Mindestabstand zwischen zwei ArenaStar-Kommentaren; verhindert Spam |
| Sprechblasen-Dauer | Feel | 1,5–5 s | 3 s | Anzeigedauer einer ArenaStar-Sprechblase |
| Server-Scan-Intervall | Gate | 2–10 s | 5 s | Häufigkeit der LAN-Scans; kleiner = aktueller, größer = weniger Netzlast |
| Konami-Eingabefenster `T_konami` | Gate | 2–10 s | 5 s | Toleranz der Code-Eingabe |
| Menü-Reaktionsziel `T_reich` | Gate | 3–8 s | 5 s | Zeitbudget Boot→Lobby; harte Obergrenze für "Sofort verständlich" |

## 8. Acceptance Criteria

Ein QA-Tester kann folgende Prüfungen ausführen:

1. **Boot→Lobby:** Von einem kalten Start erreicht der Spieler bei sofortigem SPIELEN-Druck die Lobby in `T_reich ≤ 5 s`. PASS/FAIL.
2. **Menüpunkte:** Alle 5 Menüpunkte sind vorhanden, in der festen Reihenfolge (SPIELEN, EINSTELLUNGEN, STATISTIK, CREDITS, BEENDEN) und per Gamepad-D-Pad/Stick und Tastatur erreichbar; SPIELEN ist beim Betreten fokussiert. PASS/FAIL.
3. **Beenden-Dialog:** BEENDEN öffnet einen ConfirmDialog; erst dessen Bestätigung beendet das Spiel; `ui_cancel` kehrt ins Menü zurück. PASS/FAIL.
4. **SettingsMenu-Vollständigkeit:** Die Reiter Audio (Master/Musik/SFX/Stimme), Video (Auflösung/Fullscreen/VSync, kein HDR), Sprache (DE/EN/FR/ES/PT/JP/ZH) und Eingabe (Controller-Mapping) existieren und sind wirksam. PASS/FAIL.
5. **Statistik:** Alle 6 Statistikfelder (Gesamt-Spiele, Siege, Lieblingscharakter, meistgespielte Insel, Münzen gesammelt, Minispiel-Rekorde) werden nach mindestens einer abgeschlossenen Partie mit Daten gefüllt und bei leerem Savegame als "—" angezeigt. PASS/FAIL.
6. **ArenaStar-Kommentare:** Bei Fokuswechsel auf jeden der 5 Menüpunkte erscheint ein passender Kommentar (Sprechblase + Voice bei aktiver Stimme); kein Kommentar wird zweimal hintereinander wiederholt; Schnell-Scrollen erzeugt maximal 1 Kommentar pro 800 ms. PASS/FAIL.
7. **Konami-Code:** Die Eingabe oben, oben, unten, unten, links, rechts, links, rechts, B, A im MainMenu schaltet alle Inseln frei (Bestätigungskommentar erscheint); eine falsche/unterbrochene Eingabe (Pause > 5 s) verwirft die Sequenz. PASS/FAIL.
8. **Server-Browser:** Ein im lokalen Netzwerk gestarteter Server erscheint im Browser; Direkt-IP-Verbindung funktioniert; nicht erreichbare Server erzeugen einen Fehlerdialog ohne Absturz. PASS/FAIL.
9. **Online-Badge:** Der Status (Offline / Lokales Netzwerk / Online) wird korrekt angezeigt und aktualisiert sich nach Netzwerkwechseln innerhalb von 5 s. PASS/FAIL.
10. **Erlebbar (Experiential):** Eine Testperson ohne Vorkenntnisse findet ohne Anleitung SPIELEN und erreicht die Lobby in unter 5 Sekunden; der 2-Minuten-Test aus [vision-pillars](vision-pillars.md) Szenario A ist im Menü bestanden. PASS/FAIL.
