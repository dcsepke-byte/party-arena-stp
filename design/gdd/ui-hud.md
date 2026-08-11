# UI-HUD — Party Arena Game Bible

> **Teil:** VII — UI/UX
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/ui-overview.md, design/gdd/core-loop.md (geplant)

---

## 1. Overview

Dieses Kapitel spezifiziert das Board-HUD (Screen `BoardHUD`), das während des gesamten Brettspiels sichtbar ist. Es umfasst die horizontale Spieler-Leiste am oberen Bildschirmrand (Portraits, Namen, Münzen, Sterne, aktiver Item-Slot, Schutzschild-Indikator), die Runden-Anzeige, den Würfel-Button für den aktiven Spieler, die Item-Slots des aktiven Spielers, die Münz- und Stern-Zähler-Animationen, den ArenaStar-Kommentator in der Ecke, den Pause-Button und die optionale Minimap. Das HUD muss zu jedem Zeitpunkt vier Fragen beantworten: **Wer ist dran? Was soll er tun? Wie steht es um die Spieler? Was ist gerade passiert?** Es gilt der Grundsatz: Das HUD ist so sparsam wie möglich und so informativ wie nötig — es überlagert das 3D-Board nur minimal (Transparenz, kompakte Bauweise). Alle Regeln aus [ui-overview.md](ui-overview.md) gelten verbindlich.

## 2. Player Fantasy

Das HUD soll sich anfühlen wie ein **übersichtliches Armaturenbrett einer Partyshow**: Man erkennt auf einen Blick den Stand aller Mitspieler, sieht sofort, wessen Zug es ist, und bekommt durch die animierten Zähler (Münzen fliegen, Sterne explodieren) ein Gefühl von Feiern bei jedem Gewinn. Der aktive Spieler fühlt sich eingeladen: Sein Portrait leuchtet, sein Würfel-Button pulsiert als klare Aufforderung, und ArenaStar kommentiert die Ereignisse wie ein Showmaster. Für die nicht aktiven Spieler ist das HUD eine **Live-Ergebnisliste**, die Spannung erzeugt ("Wer führt? Wer kann noch aufholen?"), ohne jemals zu überfordern. Der 2-Minuten-Test (Szenario C: Split-Screen-Identifikation) ist die Messlatte: In einer 8-Spieler-Partie muss jeder Spieler jederzeit seinen eigenen und den aktiven Spieler eindeutig identifizieren können.

## 3. Detailed Rules

### 3.1 HUD-Layout (oberer Bildschirmrand)

Das HUD liegt als horizontale Leiste am oberen Rand und besteht aus drei Zonen:

1. **Spieler-Leiste (links bis mittig):** bis zu 8 Portrait-Slots nebeneinander.
2. **Runden-Anzeige (zentriert oben):** "Runde 5 / 10".
3. **Rechte Zone:** Pause-Button, Minimap-Toggle, ArenaStar (Ecke).

Der Würfel-Button und die Item-Slots des aktiven Spielers liegen **außerhalb** der oberen Leiste: Würfel-Button in der unteren Bildschirmmitte, Item-Slots unterhalb des Portraits des aktiven Spielers (bzw. unten links neben dem Würfel-Button, siehe 3.5).

### 3.2 Spieler-Leiste

- **Portrait-Slots:** Das HUD zeigt immer exakt 8 Slots. Bei weniger als 8 Spielern werden die Slots zentriert ausgerichtet; leere Slots bleiben sichtbar und werden ausgegraut (`text_disabled`-Färbung, 40 % Deckkraft), damit die Leiste nicht springt.
- **Pro Spieler sichtbar (in jedem Slot):**
  - **Portrait** (Charakter-Portrait in der Spielerfarbe gerahmt)
  - **Name** (kurz; bei langen Namen automatisch abgekürzt/gekürzt mit "…")
  - **Münzen:** Gold-Münz-Icon + Zahl
  - **Sterne:** Stern-Icon + Zahl
  - **Aktiver Item-Slot:** Wenn der Spieler ein aktiviertes/ausgerüstetes Item trägt, wird dessen Icon im Slot angezeigt (siehe 3.5). Pro Spieler ist genau **ein** Item-Slot im HUD sichtbar (das zuletzt aktivierte bzw. das nächste nutzbare Item); die vollständige 3-Slot-Inventarliste gibt es nur für den aktiven Spieler.
  - **Schutzschild-Indikator:** Besitzt der Spieler einen Schutzschild ([item-shield.md](item-shield.md)), erscheint ein kleines Schild-Icon über dem Portrait.
- **Slot-Größe:** Basis 64 × 64 px Portrait + darunter Name/Zähler. Bei 8 Spielern beträgt der Slot-Abstand (Pitch) höchstens 234 px (siehe Formel 4.1); die Slots sind kompakt, damit die gesamte Leiste bei 1920 px Breite mit Rand passt.
- **Anordnung:** Slots sind in Spieler-Reihenfolge (P1…P8) von links nach rechts angeordnet; bei weniger Spielern werden die Slots zentriert (siehe Formel 4.2).

### 3.3 Aktiver Spieler (Hervorhebung)

- Das Portrait des aktiven Spielers wird **vergrößert auf 110 %** dargestellt (bezogen auf die Basis-Slot-Größe).
- Es erhält einen **golden leuchtenden Rahmen** (`primary`-Gelb) mit einer **Puls-Animation**: Rahmen-Opazität oszilliert zwischen 0,6 und 1,0 mit 1 Hz (Formel 4.3).
- Zusätzlich erscheint ein kleiner **Pfeil** über dem Portrait des aktiven Spielers (in dessen Spielerfarbe), der auch aus dem Augenwinkel erkennbar ist (Split-Screen-Test, [vision-pillars](vision-pillars.md) 3.4).
- **Regel:** Es gibt genau eine aktive Hervorhebung zu jedem Zeitpunkt. In Warte-/Minispiel-Phasen ([core-loop](core-loop.md)) kann die Hervorhebung ruhen, aber nie mehr als eine sein.

### 3.4 Runden-Anzeige

- Text: "Runde 5 / 10", zentriert über der Spieler-Leiste, `font_subtitle`-Größe.
- Das aktuelle Rundennummern-Label (der Zähler vor dem Schrägstrich) ist in `primary`-Gelb, die Gesamtrundenzahl in `text_secondary`.
- **Rundenwechsel-Animation:** Beim Start einer neuen Runde hüpft der Zähler einmal (Squash-and-Stretch, 300 ms) und ArenaStar kommentiert "Runde X!".
- Die Gesamtrundenzahl stammt aus der Lobby-Einstellung (8, 10 oder 15 Runden; Standard 10). Siehe [core-loop](core-loop.md).

### 3.5 Würfel-Button und Item-Slots (nur aktiver Spieler)

**Würfel-Button:**
- Großer runder Würfel-Button (Durchmesser 96 px) in der unteren Bildschirmmitte, leicht erhöht über dem unteren Rand (48 px Abstand).
- Beschriftung darunter: "ZUM WÜRFELN: A DRÜCKEN" (Tastenlabel gemäß erkanntem Layout, [ui-overview](ui-overview.md) 3.5).
- **Puls-Animation** als Aufforderung (Skalierung 1,00–1,06, 1 Hz), solange der aktive Spieler würfeln kann.
- **Sichtbarkeit:** Der Button ist nur sichtbar, wenn der aktive Spieler an der Reihe ist und würfeln kann (kein Item-Auswahl-Modus aktiv, keine Pfadwahl offen). In allen anderen Phasen ist er ausgeblendet.
- **Würfeln:** `ui_accept` löst den Würfelwurf aus. Nach dem Wurf wechselt der Button in einen "Bestätigen"-Zustand (siehe [ui-board](ui-board.md), Bewegungsschritte).

**Item-Slots (aktiver Spieler):**
- 3 kleine Slots (56 × 56 px) unterhalb des Portraits des aktiven Spielers, nebeneinander.
- Jeder Slot zeigt das Item-Icon. **Belegte Slots** sind farbig (Hintergrund `bg_e2`, Icon vollfarbig); **leere Slots** sind grau (Icon ausgeblendet, Slot bei 40 % Deckkraft).
- **Aktivierung (Gamepad):** `ui_tab_left`/`ui_tab_right` (LB/RB bzw. L1/R1) wählen einen Slot aus; `ui_accept` bestätigt die Nutzung des Items.
- **Aktivierung (Tastatur):** Tasten 1/2/3 wählen den Slot direkt; Enter bestätigt.
- **Fokus-Kopplung:** Die Item-Slots sind nur fokussierbar, wenn mindestens ein Item belegt ist und der aktive Spieler an der Reihe ist. Der Fokus wandert in dieser Phase vom Würfel-Button auf die Item-Slots (Reihenfolge: Würfel → Item 1 → Item 2 → Item 3), wobei die Item-Nutzung **vor** dem Würfeln möglich ist ([item-system](item-system.md)).
- **Ausgewählter Slot:** Der ausgewählte Slot erhält den Fokus-Rahmen ([ui-overview](ui-overview.md) 3.7); die Auswahl ist vor dem Bestätigen änderbar.

### 3.6 Münz-Zähler-Animation

- **Auslöser:** Jede Änderung des Münzbestands eines Spielers (Feld-Effekt, Minispiel-Auszahlung, Kauf, Diebstahl).
- **Animation:** Die Zahl fliegt kurz nach oben (Gewinn) oder nach unten (Verlust) — eine Roll-Animation: Die Ziffern drehen über 400 ms vom alten zum neuen Wert; bei großen Sprüngen (> 10 Münzen) werden Zwischenwerte durchlaufen (200 ms pro Ziffernschritt).
- **Farbfeedback:** Bei Gewinn färbt sich die Zahl 300 ms lang in `success`-Grün, bei Verlust in `danger`-Rot; danach zurück zu `text_primary`.
- **Sound:** `ui_counter` (Klick pro Ziffernschritt), bei Gewinn zusätzlich ein kurzer Münz-Sound aus [audio-sfx.md](audio-sfx.md).
- **Gleichzeitige Änderungen:** Ändern sich mehrere Spieler in derselben Aktion (z. B. Minispiel-Auszahlung), animieren alle betroffenen Zähler parallel; keine Serialisierung.

### 3.7 Stern-Zähler-Animation

- **Auslöser:** Stern-Kauf (oder Bonus-Stern-Vergabe, siehe [victory-conditions](victory-conditions.md)).
- **Animation:** Beim Stern-Kauf "explodiert" ein Stern auf dem Zähler: Das Stern-Icon des Spielers wird 600 ms lang auf 150 % skaliert, mit einem kurzen Strahlen-/Funken-Effekt und einer Squash-Stretch-Bewegung; danach kehrt es zur Normalgröße zurück und der Zähler erhöht sich.
- **Sound:** Jubel-/Stern-Sound aus [audio-sfx.md](audio-sfx.md); ArenaStar kommentiert ("Ein Stern für [Name]!").
- **Blockierung:** Während der Explosion (600 ms) ist der Zähler desselben Spielers nicht erneut animierbar (Schutz vor Überlagerung); andere Spieler-Zähler sind davon nicht betroffen.

### 3.8 ArenaStar im HUD

- **Position:** Kleine 2D-Illustration von ArenaStar in der unteren linken Ecke (Gegenstück zum Hauptmenü, dort untere Mitte).
- **Funktion:** Kommentiert aktuelle Ereignisse per Sprechblase (Text + optional Voice), z. B.:
  - Stern-Kauf: "Ein Stern für [Name]!"
  - Minispiel-Start: "Jetzt wird's spannend!"
  - Münzverlust: "Ups, Pech gehabt!"
  - Letzte Runde: "Die letzte Runde!"
- **Regeln:** Identisch zum Hauptmenü (maximal 1 Kommentar pro 800 ms, Sprechblase 3 s, keine Kommentar-Wiederholung direkt nacheinander). ArenaStar blockiert nie die Eingabe; seine Sprechblase liegt auf Ebene 30 ([ui-overview](ui-overview.md) 3.2) und verschiebt den Fokus nicht.
- **Untertitel:** Sind Untertitel aktiv ([ui-accessibility](ui-accessibility.md)), erscheint der Text der Sprechblase zusätzlich als fester Untertitel am unteren Rand.

### 3.9 Pause-Button

- **Auslöser:** `ui_pause` (Start/Options/+ bzw. Escape/P).
- **Wirkung:** Öffnet das `PauseMenu` als modales Overlay (Ebene 10) über dem BoardHUD.
- **PauseMenu-Inhalt:**
  - Fortsetzen (`ui_accept`)
  - Einstellungen (öffnet SettingsMenu als Overlay)
  - Zurück zum Hauptmenü (mit ConfirmDialog "Aktuelles Spiel wird nicht gespeichert. Wirklich beenden?")
  - Spieler-Farben/Controller-Status (nur Anzeige)
- **Pause-Zeit:** Siehe [ui-accessibility](ui-accessibility.md) (Singleplayer unbegrenzt, Multiplayer 60 s).
- Der Pause-Button ist nicht als UI-Element klickbar, sondern ausschließlich über `ui_pause` erreichbar (kein sichtbarer Button in der Leiste; der Hinweis ist nur in der Eingabe-Hilfe sichtbar).

### 3.10 Minimap (optional)

- **Toggle:** `ui_toggle` (Select/Back bzw. −/Tab) schaltet die Minimap ein/aus; Standard: **aus**.
- **Darstellung:** Kleine, vereinfachte Vorschau des Boards in der oberen rechten Ecke unter der Leiste (ca. 20 % der Bildschirmbreite, maximal 384 × 216 px). Sie zeigt: Feld-Pfad als stilisierte Punkte, die Sternen-Statue als Stern-Symbol, alle Spieler als farbige Punkte in ihren Spielerfarben, den aktiven Spieler mit Puls-Ring.
- **Skalierung:** Die Minimap skaliert das Board-Layout proportional auf ihre Größe; sie ist rein informativ, nicht interaktiv (kein Klick auf Felder).
- **Performance:** Die Minimap wird bei aktiver 3D-Szene als 2D-Overlay gezeichnet (kein zweiter 3D-Viewport), um das Performance-Budget ([technical-performance.md](technical-performance.md)) zu schonen.
- **Fokus:** Die Minimap ist nicht fokussierbar.

### 3.11 HUD bei Minispiel- und Zwischenphasen

- Während eines Minispiels ([core-loop](core-loop.md)) wechselt die UI auf den `MinigameHUD`; die Spieler-Leiste mit Münz-/Stern-Stand bleibt in kompakter Form sichtbar (kein Würfel-Button, keine Item-Slots).
- Während der Siegerehrung wird die Spieler-Leiste ausgeblendet und durch den `VictoryScreen` ersetzt.
- Während Lade-/Wartezeiten (Ebene 40) bleibt das HUD unsichtbar; nach dem Laden erscheint es mit einem 200-ms-Fade.

## 4. Formulas

### 4.1 Slot-Pitch bei 8 Spielern

`p = (W_hud − 2 × m) / 8`

- `W_hud` = verfügbare HUD-Breite (1920 px bei Basisauflösung), `m` = Randabstand (24 px).
- Erwartungswert: `p = (1920 − 48) / 8 = 234 px`.
- Akzeptanz: Bei 8 Spielern dürfen sich die Portraits (inkl. 110 %-Vergrößerung des aktiven) nicht überlappen; `p ≥ 234 px` bei Basisauflösung.

### 4.2 Zentrierung bei weniger Spielern

`offset = (8 − P) / 2 × p`

- `P` = aktive Spielerzahl (2–8), `p` = Slot-Pitch (4.1).
- Der erste Slot beginnt bei `x = offset` (links), damit die Gruppe zentriert ist.
- Beispiel: `P = 2` → `offset = 3 × p`; die zwei Slots stehen mittig.
- Akzeptanz: Für jedes `P ∈ [2,8]` ist die Gruppe der aktiven Slots horizontal zentriert (± 4 px).

### 4.3 Puls-Animation des aktiven Rahmens

`O(t) = 0,6 + 0,4 × (0,5 + 0,5 × sin(2π × 1,0 × t))`

- `O(t)` = Rahmen-Opazität (0–1), Frequenz 1 Hz.
- Erwartungswert: `O` oszilliert zwischen 0,6 und 1,0; keine Sprünge.
- Akzeptanz: Der Rahmen ist zu jedem Zeitpunkt sichtbar (`O ≥ 0,6`).

### 4.4 Würfel-Aufforderung

`A_w(t) = 1 + 0,06 × (0,5 + 0,5 × sin(2π × 1,0 × t))`

- `A_w(t)` = Skalierung des Würfel-Buttons (1,00–1,06), 1 Hz.
- Akzeptanz: Der Würfel-Button pulsiert nur, wenn der aktive Spieler tatsächlich würfeln kann; außerhalb ist er ausgeblendet (Regel 3.5).

### 4.5 Münz-Roll-Animation

`T_roll = 0,2 s × |W_neu − W_alt|` mit `T_roll ≤ 1,2 s`

- `W_neu`/`W_alt` = neuer/alter Münzbestand, `T_roll` = Animationsdauer.
- Beispiel: Änderung von 23 auf 31 → `|31−23| = 8` → `T_roll = 1,6 s`, gedeckelt auf 1,2 s.
- Akzeptanz: Die Roll-Animation endet spätestens nach 1,2 s; der Endwert wird nie vor Animationsende angezeigt (kein Sprung von alt auf neu ohne Zwischenwerte bei `|Δ| ≤ 10`).

### 4.6 Stern-Explosion

`T_stern = 0,6 s` (fest)

- Akzeptanz: Die Explosions-Animation dauert exakt 600 ms; währenddessen ist der betroffene Zähler nicht erneut animierbar.

## 5. Edge Cases

1. **Spielerzahl 2:** Bei `P = 2` sind 6 Slots ausgegraut und zentriert; die Leiste ist deutlich schmaler als der Bildschirm. Der aktive Spieler ist trotzdem eindeutig hervorgehoben (Rahmen + Pfeil).
2. **Spieler mit 0 Münzen:** Der Münz-Zähler zeigt "0", nie negativ; Verlust-Effekte werden bei 0 auf den tatsächlich vorhandenen Betrag gedeckelt (siehe [field-luck.md](field-luck.md)). Die Roll-Animation nach unten endet bei 0.
3. **Item-Nutzung ohne nutzbares Item:** Der Spieler bestätigt `ui_accept` am Würfel-Button, hat aber ein Item, das nicht nutzbar ist (falsche Phase). Der Würfelwurf wird ausgeführt (Item-Nutzung ist optional); ein Versuch, ein nicht nutzbares Item zu aktivieren, spielt `ui_error` ([ui-overview](ui-overview.md) 3.6).
4. **Mehrere gleichzeitige Münzänderungen:** Bei einer Minispiel-Auszahlung mit 8 Spielern animieren alle Zähler parallel; die 800-ms-Kommentarsperre ([ui-overview](ui-overview.md) 3.8) begrenzt ArenaStar-Kommentare auf 1 pro 800 ms.
5. **Name länger als Slot:** Der Name wird auf die Slot-Breite gekürzt (abgeschnitten mit "…"); das vollständige Profil erscheint als Tooltip beim Hover/Fokus (nur wenn Fokus auf dem Slot liegt; Slots sind sonst nicht fokussierbar, um die Navigation nicht zu verlangsamen).
6. **Runden-Anzeige bei variabler Rundenanzahl:** Bei 8 Runden zeigt die Anzeige "Runde X / 8"; die Gesamtrundenzahl wird nach Spielstart nie geändert (Fixierung in der Lobby).
7. **Minimap bei nicht geladener Board-Geometrie:** Während der Board-Generierung ([board-architecture.md](board-architecture.md)) bleibt die Minimap leer (graues Rechteck), bis die Feldpositionen geladen sind; sie blendet nie falsche Positionen ein.
8. **Pause mitten in einer Animation:** Wird `ui_pause` während der Münz-Roll- oder Stern-Explosion gedrückt, friert die Animation ein und läuft nach dem Fortsetzen weiter (keine Animationszeit läuft während der Pause).
9. **HUD bei 8 Spielern und kleiner Auflösung (1280×720):** Die Slots skalieren über `s = 0,667` ([ui-overview](ui-overview.md) 4.1); der Pitch bei 8 Spielern wird auf `p = (1280 − 48) / 8 = 154 px` skaliert. Die Portraits bleiben erkennbar (Silhouetten-Test, [vision-pillars](vision-pillars.md) 4.2). Die 110 %-Vergrößerung bleibt proportional.
10. **Aktiver Spieler scheidet aus / wird gesperrt:** In den Standard-Regeln scheidet kein Spieler aus; falls ein Modus dies vorsieht, geht die Hervorhebung an den nächsten aktiven Spieler über und der betroffene Slot wird 40 %-gedimmt (kein Fehlerdialog).

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `ui-hud.md` | Art | Verwendung |
|---------------------------|-----|------------|
| `design/gdd/ui-overview.md` | Dach | Liefert Tokens, Fokus-Regeln, Overlay-Ebenen, ControlHelper, UI-Sound und Transitions. |
| `design/gdd/core-loop.md` | Quelle | Definiert die Phasen (Würfeln, Bewegung, Kauf, Minispiel), in denen das HUD umschaltet. |
| `design/gdd/item-system.md` | Quelle | Definiert Items und Inventar, die das HUD als Slots anzeigt. |
| `design/gdd/star-economy.md` | Quelle | Definiert Stern-Kauf und Zähler, die das HUD animiert. |
| `design/gdd/coin-economy.md` | Quelle | Definiert Münzquellen/-senken, die das HUD animiert. |
| `design/gdd/board-architecture.md` | Nachgeordnet | Liefert die Board-Geometrie für die Minimap. |
| `design/gdd/ui-board.md` | Peer | Teilt sich den BoardHUD-Screen; Kamera/Feld-UI und HUD müssen zusammenpassen. |
| `design/gdd/ui-accessibility.md` | Nachgeordnet | Setzt Untertitel, Textgröße, Spielerfarben-Ersatz (Symbole) und Pause-Zeit um. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `design/gdd/ui-board.md` | Verwendet das HUD (Würfel-Button, Runden-Anzeige) als Gegenstück zur 3D-Board-Interaktion. |
| `design/gdd/ui-shop.md` | Öffnet als Overlay über dem HUD; beim Schließen muss der Fokus an das HUD (Würfel-Button) zurückkehren. |
| `design/gdd/ui-character-select.md` | Muss die Spielerfarben und Charakter-Portraits liefern, die das HUD anzeigt. |
| `design/gdd/audio-ui.md` / `audio-sfx.md` | Muss ui_counter-, Münz- und Stern-Sounds sowie ArenaStar-Voice liefern. |
| `design/gdd/technical-performance.md` | Muss das HUD-Budget (Minimap als 2D-Overlay, keine 3D-Doppel-Viewports) absichern. |

### 6.3 Bidirektionalität

Das HUD ist der ständige Begleiter des BoardHUD-Screens; [ui-board.md](ui-board.md) behandelt die 3D-Interaktion, [ui-hud.md](ui-hud.md) die 2D-Information. Beide referenzieren sich wechselseitig und müssen gemeinsam getestet werden (Split-Screen-Szenario C). Der Fokus-Rückkehr-Pfad über Overlays (Shop schließen → Würfel-Button) verbindet sich mit [ui-shop.md](ui-shop.md).

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Slot-Pitch `p` | Feel | 180–280 px | 234 px | Dichte der Spieler-Leiste; kleiner = kompakter, größer = luftiger |
| Portrait-Basisgröße | Feel | 48–80 px | 64 px | Erkennbarkeit der Portraits im Split-Screen |
| Aktive-Vergrößerung | Feel | 105–125 % | 110 % | Stärke der Hervorhebung des aktiven Spielers |
| Rahmen-Puls-Frequenz | Feel | 0,5–2,0 Hz | 1,0 Hz | Tempo des Pulsierens des aktiven Rahmens |
| Rahmen-Puls-Opazität | Feel | 0,5–0,8 (Minimum) | 0,6 | Sichtbarkeits-Untergrenze des Rahmens |
| Würfel-Button-Größe | Feel | 72–128 px | 96 px | Aufforderungs-Stärke; größer = präsenter |
| Würfel-Puls-Amplitude | Feel | 0,03–0,10 | 0,06 | Stärke des Würfel-Pulsierens |
| Münz-Roll-Cap `T_roll` | Feel | 0,6–2,0 s | 1,2 s | Maximale Dauer der Münz-Roll-Animation |
| Stern-Explosionsdauer | Feel | 0,3–1,0 s | 0,6 s | Inszenierungsstärke des Stern-Kaufs |
| Kommentar-Sperrzeit (HUD) | Feel | 400–1500 ms | 800 ms | Abstand zwischen ArenaStar-Kommentaren im HUD |
| Minimap-Größe | Feel | 10–30 % der Breite | 20 % | Sichtbarkeit vs. Verdeckung des Boards |

## 8. Acceptance Criteria

Ein QA-Tester kann folgende Prüfungen ausführen:

1. **Spieler-Leiste:** Bei jeder Spielerzahl `P ∈ [2,8]` zeigt das HUD exakt 8 Slots (bei `P < 8` zentriert, leere Slots ausgegraut), jeder mit Portrait, Name, Münzen, Sternen, aktivem Item-Slot und ggf. Schutzschild-Indikator. PASS/FAIL.
2. **Aktiver Spieler:** Genau ein Portrait ist zu jedem Zeitpunkt auf 110 % vergrößert, golden umrahmt (Puls-Opazität 0,6–1,0) und mit Pfeil markiert. PASS/FAIL.
3. **Runden-Anzeige:** "Runde X / Y" wird korrekt angezeigt; die Rundenanzahl stammt aus der Lobby-Wahl; beim Rundenwechsel hüpft der Zähler einmal. PASS/FAIL.
4. **Würfel-Button:** Der Würfel-Button erscheint nur beim aktiven Spieler in Würfel-Phase, pulsiert (1,00–1,06) und zeigt "ZUM WÜRFELN: [Tastenlabel]"; `ui_accept` löst den Wurf aus. PASS/FAIL.
5. **Item-Slots:** Die 3 Slots des aktiven Spielers zeigen belegte (farbig) und leere (grau) Zustände; Auswahl per LB/RB bzw. 1/2/3, Bestätigung per `ui_accept`; bei leerem Inventar sind die Slots nicht fokussierbar. PASS/FAIL.
6. **Münz-Roll-Animation:** Bei einer Münzänderung um `|Δ| ≤ 10` läuft die Ziffern-Roll-Animation mit Zwischenwerten und endet spätestens nach 1,2 s; der Endwert erscheint nicht vor Animationsende; Gewinn = grün, Verlust = rot. PASS/FAIL.
7. **Stern-Explosion:** Beim Stern-Kauf explodiert das Stern-Icon 600 ms lang (150 % Skalierung); der Zähler erhöht sich erst nach der Explosion; keine Doppel-Animation innerhalb 600 ms. PASS/FAIL.
8. **ArenaStar:** Kommentare erscheinen als Sprechblase (max. 1 pro 800 ms, keine direkte Wiederholung), blockieren nie die Eingabe; bei aktiven Untertiteln erscheint der Text zusätzlich unten. PASS/FAIL.
9. **Pause:** `ui_pause` öffnet das PauseMenu; die Pause-Zeit folgt [ui-accessibility](ui-accessibility.md) (SP unbegrenzt, MP 60 s mit Auto-Resume). PASS/FAIL.
10. **Minimap:** `ui_toggle` schaltet die Minimap ein/aus (Standard aus); sie zeigt Pfad, Sternen-Statue und Spieler als farbige Punkte, ist nicht interaktiv und nicht fokussierbar. PASS/FAIL.
11. **Split-Screen-Identifikation:** In einer 8-Spieler-Partie (Split-Screen-Szenario C aus [vision-pillars](vision-pillars.md)) identifiziert eine Testperson alle Spieler, den aktiven Spieler und den Sternen-Statue-Stand korrekt. PASS/FAIL.
12. **Erlebbar (Experiential):** Eine Testperson beantwortet nach 2 Minuten Beobachtung korrekt, wer dran ist, was zu tun ist und wie der Münz-/Sternstand der Spieler ist. PASS/FAIL.
