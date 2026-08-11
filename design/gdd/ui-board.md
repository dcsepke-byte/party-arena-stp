# UI-Board — Party Arena Game Bible

> **Teil:** VII — UI/UX
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/ui-overview.md, design/gdd/board-architecture.md (geplant)

---

## 1. Overview

Dieses Kapitel spezifiziert die 3D-Board-Ansicht und ihre Interaktionen während des Brettspiels: die Kameraführung (isometrisch als Standard, Third-Person als Alternative, Zoom-Stufen), die Feld-Hervorhebung und Pfad-Anzeige vor und nach dem Würfeln, die Abzweigungs-Auswahl, die Positionierung und Offset-Regeln der Spieler-Marker, die schwebenden Namensschilder, die Feld-Typ-Erkennung über 3D-Modelle und Boden-Icons, den Feld-Hover-Tooltip sowie die Kamera-Umschaltung und das Zoom-Handling. Das Board ist der zentrale Spielort; die UI muss die Regeln aus den Board-/Feld-Kapiteln so darstellen, dass der Spieler **ohne Textnachschlagen** erkennt, welche Felder welche Effekte haben, wohin er sich bewegen kann und was gerade passiert. Die 2D-HUD-Elemente sind in [ui-hud.md](ui-hud.md) spezifiziert; dieses Kapitel behandelt die Interaktion mit der 3D-Szene. Alle Regeln aus [ui-overview.md](ui-overview.md) gelten verbindlich.

## 2. Player Fantasy

Die Board-Ansicht soll sich anfühlen wie ein **lebendiges, dreidimensionales Spielbrett, das man erkunden und verstehen kann, ohne Regeln zu lesen**. Der Spieler sieht die Insel aus einem klaren, ruhigen Blickwinkel (Standard: isometrisch, alles Wichtige im Bild), kann heranzoomen, um ins Detail zu gehen, und bekommt bei jedem Zug eine visuelle Erzählung: Die möglichen Zielfelder leuchten auf, das gewürfelte Ziel glüht, und die eigene Spielfigur marschiert sichtbar über die Felder. Die Fantasy ist die eines **Tabletop-Spiels, das sich von selbst erklärt**: Man sieht den Sternen-Shop, man sieht die Münzfelder, man sieht die Abzweigungen — und man hat jederzeit das Gefühl, das ganze Brett im Griff zu haben. Für Zuschauer und wartende Spieler ist die Ansicht außerdem die Bühne der Partie: Man schaut zu, wie die Figuren reisen, und fiebert mit.

## 3. Detailed Rules

### 3.1 3D-Board-Ansicht und Kamera

- **Standard-Kamera:** Isometrisch. Die Kamera zeigt das Board aus einem festen, schrägen Winkel (Elevation ~35° über der Horizontalen), ohne freie Rotation. Der aktive Spieler bleibt im Bildmittelpunkt.
- **Alternative Kamera:** Third-Person hinter dem aktiven Spieler. Umschaltung über `ui_toggle_kamera` (Y / Dreieck / Tab, gemäß [ui-overview](ui-overview.md) 3.5). Die gewählte Kameraperspektive wird pro Partie gespeichert.
- **Kamera-Folgen:** Die Kamera folgt dem aktiven Spieler mit sanfter Bewegung (Lerp-Faktor 0,1 pro Frame bei 60 FPS; Formel 4.1). Bei "Reduzierte Bewegung" ([ui-accessibility](ui-accessibility.md)) entfällt das Smooth-Follow: Die Kamera springt hart auf die Zielposition (0 ms Übergang).
- **Kamera bei Wartezeit:** Während fremder Züge bleibt die Kamera auf dem zuletzt aktiven Spieler bzw. folgt optional der aktuell agierenden Figur (Einstellung "Kamera folgt aktivem Spieler" in den Optionen; Standard: an).

### 3.2 Zoom

- **Auslöser:** Rechter Stick (Gamepad) bzw. Mausrad (Maus).
- **Stufen:** Es gibt exakt 3 diskrete Zoom-Stufen (kein stufenloser Zoom):
  - **100 % (Standard):** Der aktive Spieler und ~8–12 Felder im Umfeld sind sichtbar.
  - **75 % (Übersicht):** Größerer Ausschnitt, ~15–20 Felder sichtbar.
  - **50 % (Ganzes Board):** Das gesamte Board passt in den Bildschirm (Formel 4.4).
- **Wechsel:** Ein Zoom-Wechsel dauert 250 ms (Ease-In-Out) und ist auch bei "Reduzierte Bewegung" erlaubt (Zoom gilt nicht als Bewegungs-Trigger).
- **Anzeige:** Beim Zoom-Wechsel erscheint kurz (600 ms) ein kleines Prozent-Label ("100 %") in der oberen rechten Ecke unter der Minimap ([ui-hud](ui-hud.md) 3.10).

### 3.3 Feld-Hervorhebung

- **Nach dem Würfeln:** Das Zielfeld (durch die gewürfelte Zahl bestimmt, [dice-movement.md](dice-movement.md)) leuchtet mit einem **goldenen Ring** auf, der pulsiert (1 Hz, Opazität 0,5–1,0; Formel 4.2). Zusätzlich schwebt ein Stern-/Pfeil-Icon über dem Zielfeld.
- **Während der Bewegung:** Das Zielfeld bleibt hervorgehoben; der Spieler-Marker wandert Feld für Feld zum Ziel (Bewegungslogik in [dice-movement.md](dice-movement.md)).
- **Mehrdeutigkeit:** Führen mehrere Pfade zum selben Feld (Schleifen), wird das Feld einmal hervorgehoben; die Wahl der Route erfolgt über die Abzweigungs-Auswahl (3.5).

### 3.4 Pfad-Anzeige (vor dem Würfeln)

- **Vor dem Wurf:** Die möglichen Zielfelder (1 bis 6 Schritte vom aktuellen Feld des aktiven Spielers, gemäß Standard-Würfel) werden **schwach markiert**: ein dezenter, semi-transparenter Kreis (40 % Deckkraft) auf jedem erreichbaren Feld.
- **Nach dem Wurf:** Nur das tatsächlich gewürfelte Zielfeld wird **stark markiert** (3.3); die schwachen Markierungen der nicht gewählten Felder erlöschen sofort.
- **Regel:** Die schwache Markierung erscheint nur, wenn der aktive Spieler würfeln kann und keine Pfadwahl offen ist. Bei Items, die den Würfel ersetzen (z. B. Glücks-Würfel 1–10, [item-luckydice.md](item-luckydice.md)), erweitert sich die Markierung entsprechend der maximalen Würfelaugen des aktiven Würfels.
- **Anzeige-Dauer:** Die Markierungen sind statisch (keine Animation), um visuelles Rauschen zu vermeiden; sie erscheinen mit einem 150-ms-Fade.

### 3.5 Abzweigungs-Auswahl

- **Auslöser:** Erreicht der aktive Spieler ein Feld, an dem sich der Pfad teilt ([board-architecture.md](board-architecture.md)), und sein Würfelwurf führt ihn über eine Abzweigung, wird eine Pfadwahl-UI eingeblendet.
- **Darstellung:** Ein zentriertes UI-Panel "Wähle deinen Pfad!" mit zwei Optionen (bei mehr als zwei Zweigen: maximal 3, Auswahl per Listenmarkierung). Jede Option zeigt ein **Icon** (Symbol des Zielbereichs, z. B. Stern, Münze, Item, Ereignis) und eine **Beschreibung** (ein kurzer Satz, z. B. "Zum Sternen-Shop").
- **Keine Zeitlimitierung:** Die Auswahl ist nicht zeitlimitiert; es steht aber eine Eingabe-Aufforderung im Panel: "Drücke A/B um zu wählen" (A = bestätigen, B = zur zweiten Option, je nach Fokus).
- **Fokus & Steuerung:** Die Optionen sind horizontal angeordnet; `ui_tab_left/right` (bzw. Pfeiltasten) bewegt den Fokus zwischen ihnen, `ui_accept` wählt die fokussierte Option. `ui_cancel` ist in dieser Phase **nicht** als "zurück" definiert (die Auswahl ist Pflicht); es bewegt ebenfalls den Fokus zur zweiten Option, um versehentliches Abbrechen zu verhindern.
- **Board-Visualisierung:** Das gewählte Teilstück des Pfads wird nach der Auswahl farblich hervorgehoben (Gold), während die Bewegung ausgeführt wird.

### 3.6 Spieler-Marker

- **Darstellung:** 3D-Modelle der Charaktere stehen auf den Feldern, zentriert auf dem Feldmittelpunkt.
- **Überlappung (mehrere Spieler auf einem Feld):** Stehen mehrere Spieler auf demselben Feld, werden sie versetzt positioniert (Offset in Einheiten; Formel 4.3):
  - 2 Spieler: seitlich versetzt um ±0,75 Einheiten.
  - 3–4 Spieler: Rauten-/Kreisformation auf dem Feld.
  - 5–8 Spieler: zweireihige Formation (vordere und hintere Reihe), Abstand 0,75 Einheiten.
- **Offset-Reihenfolge:** Die Versatz-Positionen werden nach Spieler-Reihenfolge (P1 zuerst) vergeben; sie sind deterministisch und ändern sich nicht innerhalb einer Partie.
- **Animation:** Betritt ein Spieler ein Feld mit mehreren Figuren, bewegt er sich direkt auf seinen freien Versatzpunkt (100 ms).
- **Aktiver Spieler:** Die Figur des aktiven Spielers wird zusätzlich durch einen Boden-Ring in der Spielerfarbe markiert (überlappungsfrei mit Feld-Markierungen).

### 3.7 Spieler-Namensschild

- **Darstellung:** Schwebender Text über dem Charakter, in der **Spielerfarbe** (Text + dezente dunkle Outline für Lesbarkeit).
- **Inhalt:** Name des Spielers. Bei 8 Spielern bleibt das Namensschild immer sichtbar (kein Abblenden bei Zoom 50 %).
- **Lesbarkeit:** Das Namensschild skaliert nicht mit dem Zoom (konstante Bildschirmgröße ~18 px `font_caption`), damit es bei 50 %-Zoom lesbar bleibt.
- **Kollision:** Bei dicht beieinanderstehenden Figuren (Überlappung 3.6) werden die Namensschilder vertikal gestaffelt (Offset 24 px pro Spieler), sodass sie sich nie überdecken.

### 3.8 Feld-Typ-Erkennung

- Jedes Feld zeigt ein eigenes **3D-Modell** (Themen-abhängig je Insel, [world-*.md](world-overview.md)) und zusätzlich ein **Boden-Icon** (flach auf dem Feld, aus dem Icon-Vokabular des Themes):
  - Sternen-Shop: Stern-Symbol
  - Item-Shop: Geschenk-/Einkaufswagen-Symbol
  - Ereignis: Blitz/Ausrufezeichen
  - Glück/Pech: Glücksrad-/Kleeblatt-Symbol
  - Münz-Bonus: Münz-Symbol
  - Minispiel: Würfel-/Party-Symbol
  - Start: Haus-/Flaggen-Symbol
- **Regel:** Das Boden-Icon ist das primäre Erkennungsmerkmal (Farbblindheit-sicher, [vision-pillars](vision-pillars.md) 3.4, [ui-accessibility](ui-accessibility.md)); das 3D-Modell verstärkt es thematisch. Kein Feldtyp wird ausschließlich über Farbe unterschieden.
- **Zusätzliche Marker:** Der Sternen-Shop zeigt zusätzlich die schwebende Sternen-Statue ([star-economy.md](star-economy.md)); der Item-Shop eine schwebende Geschenk-Markierung, wenn der Shop offen ist.

### 3.9 Feld-Hover-Tooltip

- **Auslöser:** Maus-Hover über einem Feld ODER Gamepad-Fokus, der über die `ui_toggle`-Feldauswahl (siehe unten) auf ein Feld gelegt wird.
- **Darstellung:** Tooltip (Panel nach [ui-overview](ui-overview.md)-Tokens) in der Nähe des Felds mit:
  - Feldtyp (Name + Icon)
  - Möglichen Effekten (1 Zeile, z. B. "Erhalte 5 Münzen", "Öffnet den Item-Shop")
  - Bei Ereignis-/Glück-Feldern: "? (zufällig)" statt konkreter Werte
- **Anzeige:** Der Tooltip erscheint nach 300 ms Hover-Verzögerung und verschwindet 200 ms nach Verlassen. Er liegt auf Ebene 30 ([ui-overview](ui-overview.md) 3.2), ist nicht fokussierbar und blockiert keine Eingabe.
- **Gamepad-Variante:** Da Gamepad-Hover nicht existiert, bietet das HUD eine optionale "Feld-Inspektion": Bei gedrücktem `ui_toggle_inspekt` (LB + D-Pad bzw. Taste gemäß Remapping) bewegt ein Markierungsring die Felder, und der Tooltip zeigt die Effekte des markierten Felds. Standard: an.

### 3.10 Kamera-Umschaltung und Persistenz

- **Toggle:** `ui_toggle_kamera` wechselt zwischen isometrisch (Standard) und Third-Person. Der Wechsel ist sofort (200 ms Blend).
- **Persistenz:** Die Wahl wird pro Partie gespeichert (nicht global); jede Partie startet standardmäßig isometrisch.
- **Third-Person-Sicht:** In Third-Person folgt die Kamera hinter dem aktiven Spieler (Lerp-Faktor 0,1); das Zielfeld bleibt durch den goldenen Ring sichtbar (3.3). Bei "Reduzierte Bewegung" ([ui-accessibility](ui-accessibility.md)) gilt dieselbe harte Sprung-Regel wie in 3.1.
- **Interaktion:** In beiden Modi sind alle Interaktionen (Würfeln, Item, Pfadwahl) identisch; es gibt keine Modi-abhängigen UI-Unterschiede außer der Kameraperspektive.

### 3.11 Board-UI und Split-Screen

- Bei lokalen 2–4-Spieler-Split-Screens ([technical-multiplayer.md](technical-multiplayer.md)) zeigt jedes Panel dieselbe Board-UI; der aktive Spieler jedes Panels ist dort der jeweilige lokale Spieler.
- Die Feld-Hervorhebung und Pfad-Anzeige beziehen sich im Split-Screen auf den Spieler des jeweiligen Panels. Die Kamera jedes Panels folgt unabhängig.
- **Wichtig:** Im Split-Screen mit 3–4 Spielern darf die Zoom-Stufe 50 % (ganzes Board) die Sichtbarkeit des aktiven Spielers nicht unter die Silhouetten-Grenze drücken (Prüfung mit [vision-pillars](vision-pillars.md) 4.2).

## 4. Formulas

### 4.1 Kamera-Folge (Lerp)

`pos_neu = pos_alt + (pos_ziel − pos_alt) × α`, mit `α = 0,1`

- `pos_alt` = aktuelle Kameraposition, `pos_ziel` = Zielposition (aktiver Spieler), `α` = Lerp-Faktor.
- Pro Frame (60 FPS) nähert sich die Kamera 10 % der Restdistanz an. Zeit bis 95 % Annäherung:
  `t_95 = ln(0,05) / ln(1 − 0,1) ≈ 28,4 Frames ≈ 0,47 s`.
- Akzeptanz: Bei einem Positionssprung des Spielers erreicht die Kamera innerhalb von `t_95 ≤ 0,5 s` 95 % der Zielposition; kein Überschwingen (Oszillieren um `pos_ziel`).

### 4.2 Zielfeld-Puls

`O_feld(t) = 0,5 + 0,5 × (0,5 + 0,5 × sin(2π × 1,0 × t))`

- `O_feld` = Opazität des goldenen Rings (0,5–1,0), Frequenz 1 Hz.
- Akzeptanz: Der Ring ist zu jedem Zeitpunkt sichtbar (`O ≥ 0,5`) und pulsiert gleichmäßig.

### 4.3 Spieler-Versatz bei Überlappung

Für 2 Spieler auf einem Feld:

`x_i = x_feld + offset_i`, mit `offset_1 = −0,75`, `offset_2 = +0,75` (Einheiten)

- `x_feld` = Feldmittelpunkt auf der x-Achse, `offset_i` = seitlicher Versatz des Spielers `i`.
- Für 3–8 Spieler wird die Formation aus 3.6 mit Grundabstand `d = 0,75` Einheiten deterministisch berechnet (Rautenformation 3–4, zweireihige Formation 5–8).
- Akzeptanz: Figuren auf demselben Feld überlappen sich nicht (Silhouetten bleiben vollständig sichtbar) und stehen innerhalb der Feldgrenzen (± 0,4 Einheiten um den Feldmittelpunkt bei einem angenommenen Feldradius von 1,0 Einheiten).

### 4.4 Zoom-Stufen und Sichtbarkeit

`Zoom ∈ {1,00; 0,75; 0,50}` (Skalierungsfaktor der Kameradistanz relativ zur Standard-Distanz)

`S_50 = e_erkennbar / E_gesamt` bei Zoom 50 %

- `e_erkennbar` = Anzahl der Spielerfiguren, die bei 50 %-Zoom in reiner Silhouette erkennbar sind (Silhouetten-Test, [vision-pillars](vision-pillars.md) 4.2), `E_gesamt` = Gesamtzahl der Spieler.
- Akzeptanz: `S_50 ≥ 0,90` — auch im weitesten Zoom bleiben mindestens 90 % der Figuren identifizierbar; sonst ist der Zoom-Bereich zu verkleinern.

### 4.5 Pfad-Markierungsbereich

`N_mark = max_augen(aktiver_Würfel)`

- `max_augen(aktiver_Würfel)` = maximale Augenzahl des aktuell aktiven Würfels (Standard 6, Glücks-Würfel 10, [item-luckydice.md](item-luckydice.md)).
- Akzeptanz: Vor dem Wurf sind exakt die Felder schwach markiert, die in `1…N_mark` Schritten erreichbar sind (inklusive Abzweigungen); Felder jenseits von `N_mark` sind nicht markiert.

## 5. Edge Cases

1. **Zielfeld außerhalb des sichtbaren Bereichs:** Liegt das gewürfelte Zielfeld außerhalb des aktuellen Kameraausschnitts, schwenkt die Kamera auf das Zielfeld (gleicher Lerp wie 4.1), während die Figur läuft. Der goldene Ring ist dann beim Ankommen sichtbar.
2. **Alle 8 Spieler auf demselben Feld:** Die zweireihige Formation (3.6) platziert alle 8 Figuren ohne Überlappung; die Namensschilder werden gestaffelt (3.7). Die Formation wird beim Betreten nicht neu berechnet, wenn die Reihenfolge unverändert bleibt.
3. **Abzweigung, aber nur ein erreichbarer Zweig:** Ergibt der Würfelwurf, dass nur einer der Abzweigungs-Pfade erreichbar ist, erscheint **keine** Pfadwahl-UI; die Figur bewegt sich automatisch auf diesem Pfad (keine sinnlose Auswahl).
4. **Abzweigung mit Item-Würfel (1–10):** Bei Glücks-Würfel können mehr als 2 Zweige erreichbar sein; die Pfadwahl zeigt maximal 3 Optionen, die nach Priorität des Zielinhalts (Stern > Item > Münze > Ereignis > Sonstiges) sortiert sind. Die nicht gezeigten Zweige sind bei der Auswahl nicht wählbar; der Spieler kann nicht "ins Leere" laufen.
5. **Feld-Hover auf unsichtbarem Feld:** Nicht sichtbare/gesperrte Felder ([board-architecture.md](board-architecture.md)) sind nicht hoverbar und zeigen keinen Tooltip; die Maus geht hindurch.
6. **Zoom 50 % mit langen Pfaden:** Bei sehr langen Boards ([world-*.md](world-overview.md)) zeigt Zoom 50 % das ganze Board; falls das Board das Seitenverhältnis des Bildschirms sprengt, wird der Zoom auf den minimalen Faktor begrenzt, der das Board vollständig zeigt (kann größer als 0,5 sein). Die 3 Stufen bleiben erhalten (die 50 %-Stufe wird dann als "Ganzes Board" bezeichnet).
7. **Kamera in Third-Person und Überlappung:** In Third-Person kann der aktive Spieler hinter anderen Figuren stehen; die Kamera positioniert sich so, dass die eigene Figur sichtbar bleibt (Kollisionsvermeidung: Kamera wandert nach oben/außen, wenn die Sicht blockiert ist; kein Durchsicht-Rendering).
8. **Pfadwahl ohne UI-Rückkehr:** Ist die Pfadwahl-UI offen, sind Würfel-Button und Item-Slots gesperrt ([ui-hud](ui-hud.md) 3.5); nach der Auswahl kehrt der Fokus an den Würfel-Button (bzw. das nächste Aktionsziel) zurück.
9. **Gamepad-Hover über Tooltip:** Der Tooltip bei Gamepad-Feld-Inspektion (3.9) wird nur angezeigt, solange die Inspektions-Taste gehalten wird; beim Loslassen verschwindet er sofort (kein hängender Tooltip).
10. **Reduzierte Bewegung und Zoom:** Zoom ist von "Reduzierte Bewegung" ausgenommen (3.2); nur Kamera-Folge-Bewegungen werden hart (Sprung). Ein Spieler mit Motion-Sickness sieht damit weiterhin ruhige, aber sprungfreie Zoom-Wechsel.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `ui-board.md` | Art | Verwendung |
|-----------------------------|-----|------------|
| `design/gdd/ui-overview.md` | Dach | Liefert Tokens, Fokus-Regeln, ControlHelper, Overlay-Ebenen und UI-Sound. |
| `design/gdd/ui-hud.md` | Peer | Teilt den BoardHUD-Screen; Würfel-Button, Runden-Anzeige und Item-Slots ergänzen die 3D-Ansicht. |
| `design/gdd/board-architecture.md` | Quelle | Definiert Feld-Verkettung, Pfade, Abzweigungen und Feldtypen, die hier dargestellt werden. |
| `design/gdd/dice-movement.md` | Quelle | Definiert Würfel und Bewegung, deren Zielfeld-Markierung hier visualisiert wird. |
| `design/gdd/field-star-shop.md`, `field-item-shop.md`, `field-event.md`, `field-luck.md`, `field-coin-bonus.md`, `field-minigame.md` | Quelle | Liefern die Feld-Effekte für Tooltips und Pfadwahl-Sortierung. |
| `design/gdd/technical-multiplayer.md` | Nachgeordnet | Muss Split-Screen-Panels und Kamera-Synchronisation abbilden. |
| `design/gdd/technical-performance.md` | Nachgeordnet | Muss das Kamerabudget (Lerp, 3D-Szenen je Panel) absichern. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `design/gdd/ui-hud.md` | Verwendet die Board-Interaktion (Würfel-Auslösung, Pfadwahl) als Gegenstück zur 2D-Leiste. |
| `design/gdd/ui-shop.md` | Öffnet als Overlay über der Board-Ansicht; die Kamera bleibt währenddessen stehen. |
| `design/gdd/board-architecture.md` | Muss Feldpositionen liefern, an denen die 3D-Marker platziert werden. |
| `design/gdd/world-*.md` | Muss die Feld-3D-Modelle und Boden-Icons je Insel bereitstellen. |
| `design/gdd/audio-sfx.md` | Muss Bewegungsschritt-, Würfel- und Markierungs-Sounds liefern. |

### 6.3 Bidirektionalität

Die Board-UI hängt von der Feld-/Pfad-Logik ab (Feldpositionen, erreichbare Felder) und liefert der Logik die Darstellung. Umgekehrt hängen die Feld-Kapitel davon ab, dass ihre Effekte im Tooltip korrekt dargestellt werden. Abweichungen zwischen Felddefinition und UI-Darstellung sind als Blocker zu behandeln (Tooltip muss den tatsächlichen Effekt zeigen).

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Lerp-Faktor `α` | Feel | 0,05–0,25 | 0,1 | Geschmeidigkeit der Kamerafolge; kleiner = träger, größer = direkter |
| Isometrie-Elevation | Feel | 25–45° | 35° | Blickwinkel der Standard-Kamera |
| Zielfeld-Puls-Frequenz | Feel | 0,5–2,0 Hz | 1,0 Hz | Tempo des goldenen Rings |
| Zielfeld-Puls-Minimum | Feel | 0,3–0,8 | 0,5 | Sichtbarkeits-Untergrenze des Rings |
| Versatz-Abstand `d` | Kurve | 0,5–1,2 Einheiten | 0,75 | Abstand der Figuren bei Überlappung; größer = luftiger, aber mehr Platzbedarf |
| Pfad-Markierungs-Deckkraft | Feel | 20–70 % | 40 % | Sichtbarkeit der schwachen Zielfeld-Markierung |
| Zoom-Stufen | Kurve | 2–4 Stufen | 3 (100/75/50 %) | Anzahl und Werte der Zoom-Stufen |
| Zoom-Wechsel-Dauer | Feel | 100–500 ms | 250 ms | Tempo des Zoom-Übergangs |
| Tooltip-Verzögerung | Feel | 100–800 ms | 300 ms | Verzögerung bis zum Erscheinen des Tooltips |
| Namensschild-Größe | Feel | 14–24 px | 18 px | Lesbarkeit der Namensschilder; Mindestgröße 16 px gemäß [ui-overview](ui-overview.md) |

## 8. Acceptance Criteria

Ein QA-Tester kann folgende Prüfungen ausführen:

1. **Kamera-Folge:** Bei einem Positionssprung des aktiven Spielers erreicht die Kamera 95 % der Zielposition in `t_95 ≤ 0,5 s` ohne Überschwingen. Bei "Reduzierte Bewegung" springt sie hart ohne Übergang. PASS/FAIL.
2. **Zoom-Stufen:** Die 3 Stufen 100 %/75 %/50 % sind per rechtem Stick und Mausrad erreichbar; der Wechsel dauert 250 ms und zeigt ein Prozent-Label; bei 50 % sind ≥ 90 % der Figuren per Silhouette erkennbar (`S_50 ≥ 0,90`). PASS/FAIL.
3. **Pfad-Anzeige:** Vor dem Wurf sind exakt die Felder in `1…6` Schritten schwach markiert; nach dem Wurf bleibt nur das Zielfeld stark markiert (goldener Ring, Puls 0,5–1,0). PASS/FAIL.
4. **Abzweigungs-Auswahl:** An einer Abzweigung erscheint "Wähle deinen Pfad!" mit 2–3 Optionen (Icon + Beschreibung), nicht zeitlimitiert; `ui_tab_left/right` bewegt den Fokus, `ui_accept` bestätigt; `ui_cancel` löst keine Abbrechen-Aktion aus. PASS/FAIL.
5. **Spieler-Marker:** Bei Überlappung werden Figuren deterministisch versetzt (2 Spieler ±0,75 Einheiten; 3–4 Raute; 5–8 zweireihig), ohne Silhouetten-Überlappung und innerhalb der Feldgrenzen. PASS/FAIL.
6. **Namensschilder:** Jede Figur hat ein schwebendes Namensschild in Spielerfarbe, das bei 50 %-Zoom und bei Überlappung lesbar und nicht überdeckt ist (Staffelung). PASS/FAIL.
7. **Feld-Typ-Erkennung:** Jeder Feldtyp ist über Boden-Icon eindeutig erkennbar (Silhouetten-Test); keine zwei Feldtypen unterscheiden sich nur durch Farbe. PASS/FAIL.
8. **Feld-Hover-Tooltip:** Bei Maus-Hover (300 ms) erscheint der Tooltip mit Feldtyp und Effekt; bei Gamepad-Inspektion nur bei gehaltener Taste; unsichtbare Felder zeigen keinen Tooltip. PASS/FAIL.
9. **Kamera-Toggle:** `ui_toggle_kamera` wechselt zwischen isometrisch und Third-Person; die Wahl ist pro Partie gespeichert; Partien starten isometrisch. PASS/FAIL.
10. **Split-Screen:** Bei 2–4 Spielern hat jedes Panel eine unabhängige Kamera und korrekte Feld-Hervorhebung für den jeweiligen aktiven Spieler. PASS/FAIL.
11. **Erlebbar (Experiential):** Eine Testperson ohne Vorkenntnisse erklärt nach 2 Minuten Beobachtung, welche Felder Münzen, Sterne, Items und Ereignisse bieten, und identifiziert das Zielfeld nach einem Wurf. PASS/FAIL.
