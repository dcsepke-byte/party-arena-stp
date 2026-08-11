# UI-Shop — Party Arena Game Bible

> **Teil:** VII — UI/UX
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/ui-overview.md, design/gdd/star-economy.md (geplant), design/gdd/item-system.md (geplant)

---

## 1. Overview

Dieses Kapitel spezifiziert die Shop-Overlays von Party Arena: den **Sternen-Shop** (Kauf der wandernden Sternen-Statue für 20 Münzen) und den **Item-Shop** (Kauf von bis zu 3 Items). Beide erscheinen als modales Overlay über dem BoardHUD, sobald der aktive Spieler das jeweilige Feld betritt ([field-star-shop.md](field-star-shop.md), [field-item-shop.md](field-item-shop.md)). Das Kapitel definiert das semi-transparente Overlay, das zentrierte Shop-Fenster, den Aufbau beider Shops, die Kauf-, Ablehn- und Abbruch-Interaktionen, die Zustände bei zu wenig Münzen und vollem Inventar, die ArenaStar-Kommentare zu Preis, Mangel und Items sowie die Einstiegs- und Schließ-Animation. Kaufentscheidungen und Preislogik liegen in der Ökonomie ([star-economy.md](star-economy.md), [item-system.md](item-system.md), [coin-economy.md](coin-economy.md)); dieses Kapitel beschreibt ausschließlich die Darstellung und Interaktion. Alle Regeln aus [ui-overview.md](ui-overview.md) gelten verbindlich.

## 2. Player Fantasy

Der Shop soll sich anfühlen wie der **Höhepunkt eines Einkaufsbummels auf der Party-Insel**: ein leuchtendes, leicht schwungvoll eingeflogenes Fenster, in dessen Mitte im Sternen-Shop ein großer, rotierender Stern funkelt, während ArenaStar wie ein flinker Ladenbesitzer jeden Preis und jedes Item kommentiert. Der Spieler soll sofort erkennen, ob er kaufen kann oder nicht, und der Kauf selbst muss sich **belohnend** anfühlen (Stern-Explosion, Münz-Sound, ArenaStar-Jubel). Die Fantasy ist: **"Hier wird mein Tag gemacht"** — ein klarer, freundlicher Kaufmoment ohne Kleingedrucktes. Gleichzeitig ist der Shop nie frustrierend: Fehlt das Geld, erklärt ArenaStar freundlich den Unterschied ("Du brauchst 20 Münzen! Du hast nur X."), und der graue Button mit rotem Preis zeigt den Mangel unmissverständlich an, ohne den Spieler zu beschämen.

## 3. Detailed Rules

### 3.1 Overlay und Fenster

- **Auslöser:** Der aktive Spieler landet auf einem Sternen-Shop- oder Item-Shop-Feld; nach der Lande-Animation öffnet der jeweilige Shop.
- **Overlay:** Ein semi-transparentes, dunkles Overlay (60 % Schwarz) über dem gesamten BoardHUD (Ebene 10, [ui-overview](ui-overview.md) 3.2). Es blockiert alle Eingaben an das Board; die Kamera steht still.
- **Fenster:** Das Shop-Fenster ist zentriert (horizontale + vertikale Mitte), Breite 720 px (Sternen-Shop) bzw. 960 px (Item-Shop), Höhe nach Inhalt (max. 540 px).
- **Einstiegs-Animation:** Das Fenster fliegt von unten ins Bild: Startposition 60 px unterhalb des Endpunkts, Übergang 300 ms mit **Ease-Out-Back** (Überschwinger ~10 %, Formel 4.1). Schließen: 150 ms Ease-In nach unten (gemäß [ui-overview](ui-overview.md) 3.8).
- **First-Focus:** Beim Öffnen des Sternen-Shops ist der KAUFEN-Button fokussiert (sofern aktiv), sonst ABLEHNEN. Beim Item-Shop ist Item-Slot 1 fokussiert (sofern aktiv), sonst NICHTS KAUFEN.
- **Fokus-Isolation:** Während der Shop offen ist, sind Würfel-Button, Item-Slots und Kamera-Steuerung des HUDs gesperrt ([ui-hud](ui-hud.md) 3.5). Nach dem Schließen kehrt der Fokus an den Würfel-Button zurück (bzw. das nächste Aktionsziel, [ui-overview](ui-overview.md) 3.2).

### 3.2 Sternen-Shop — Aufbau

Das Fenster des Sternen-Shops enthält, von oben nach unten:

1. **Titel:** "⭐ Sternen-Shop ⭐" (`font_title`), zentriert.
2. **Stern-Darstellung:** Ein großer Stern in der Mitte (128 × 128 px), der sich langsam um die eigene Achse dreht (eine volle Drehung in 8 s; Formel 4.2). Der Stern ist **golden** (normal) oder **grau** (wenn der Spieler < 20 Münzen hat oder der Stern bereits gekauft wurde).
3. **Preis:** "20 Münzen" (groß, `font_subtitle`), mit Münz-Icon vor der Zahl.
4. **KAUFEN-Button:** "KAUFEN (A)" — grün (`success`), wenn der Kauf möglich ist; grau (deaktiviert), wenn nicht.
5. **ABLEHNEN-Button:** "ABLEHNEN (B)" — rot (`danger`), immer aktiv, schließt den Shop ohne Kauf.

**Zustände des Sternen-Shops:**

| Zustand | Bedingung | Stern | KAUFEN | ABLEHNEN |
|---------|-----------|-------|--------|----------|
| Kaufbar | `münzen ≥ 20` UND Stern nicht gekauft | golden, dreht | grün, aktiv | rot, aktiv |
| Zu wenig Münzen | `münzen < 20` UND Stern nicht gekauft | grau, dreht | grau, deaktiviert | rot, aktiv |
| Stern gekauft | Stern bereits gekauft (unabhängig von Münzen) | grau, dreht | grau, deaktiviert | rot, aktiv |

### 3.3 Sternen-Shop — Interaktion und ArenaStar

- **Kauf:** `ui_accept` (A / X / A je Layout) auf KAUFEN bestätigt den Kauf: 20 Münzen werden abgezogen, der Stern-Zähler des Spielers erhöht sich (Stern-Explosion aus [ui-hud](ui-hud.md) 3.7), der Stern im Shop erlischt, und der Shop schließt nach 300 ms automatisch (der Stern "reist" zur Statuen-Position, [star-economy.md](star-economy.md)).
- **Ablehnen:** `ui_cancel` (B / Kreis / B) oder ABLEHNEN-Button schließt den Shop ohne Kauf.
- **ArenaStar-Kommentare:**
  - Beim Öffnen: "Ein funkelnder Stern für 20 Münzen!"
  - Zu wenig Münzen: "Du brauchst 20 Münzen! Du hast nur [X]." (X = aktueller Münzbestand, dynamisch)
  - Stern bereits gekauft: "Der Stern wurde bereits gekauft. Versuche es am nächsten Shop!"
  - Kauf bestätigt: "Glückwunsch! Ein Stern für dich!"
- **Hinweistext:** Bei "Zu wenig Münzen" und "Stern gekauft" wird zusätzlich ein dezenter Hinweistext unter dem Preis eingeblendet (nicht nur ArenaStar-Sprache), damit die Ursache auch bei deaktiviertem Voice lesbar ist.
- **Sound:** Öffnen `ui_open`, Kaufen `ui_click` + Stern-Sound ([audio-sfx.md](audio-sfx.md)), Ablehnen `ui_back`, deaktivierter Versuch `ui_error`.

### 3.4 Item-Shop — Aufbau

Das Fenster des Item-Shops enthält, von oben nach unten:

1. **Titel:** "🎒 Item-Shop 🎒" (`font_title`), zentriert.
2. **Item-Auswahl:** 3 Items nebeneinander (horizontal). Jedes Item-Panel zeigt:
   - **Item-Icon** (groß, 128 × 128 px)
   - **Item-Name** (z. B. "Glücks-Würfel", "Stern-Teleporter", "Schutzschild", "Münz-Magnet", "Dieb-Handschuh"; Sortiment je Insel/Shop, [field-item-shop.md](field-item-shop.md))
   - **Item-Beschreibung** (genau 1 Zeile, z. B. "Würfle bis 10")
   - **Preis** (Münz-Icon + Zahl)
   - **Kaufen-Button** (Tastenlabel je Slot, siehe 3.5)
3. **NICHTS-KAUFEN-Button:** "NICHTS KAUFEN (X)" — unten, zentriert, `secondary`-Farbe, immer aktiv.

### 3.5 Item-Shop — Tasten-Zuordnung

Die 3 Items werden über die **vier Gesichtstasten** direkt angewählt und gekauft — ohne Cursor-Fokus-Reihenfolge. Die Zuordnung ist über alle Controller-Layouts konsistent über die **Tastenposition** definiert ([ui-overview](ui-overview.md) 3.5):

| Slot | Position | Xbox | PlayStation | Nintendo Switch |
|------|----------|------|-------------|------------------|
| Item 1 | Süd | A | X (Cross) | A |
| Item 2 | Ost | B | Kreis | B |
| Item 3 | West | X | Quadrat | Y |
| NICHTS KAUFEN | Nord | Y | Dreieck | X |

Hinweis zur Auflösung: Die im Kapitel-Auftrag verwendeten Bezeichnungen "A/B/C je nach Slot" und "NICHTS KAUFEN (X)" sind über diese Tabelle vereinheitlicht: "C" ist die West-Taste, "(X)" ist die Nord-Taste — die scheinbare Doppelbelegung löst sich auf, weil im Nintendo-Layout die Nord-Taste die Beschriftung "X" trägt. Die UI-Beschriftungen zeigen immer das korrekte Layout-Label ([ui-overview](ui-overview.md) 3.5).

**Regeln:**

1. Ein Druck auf die Item-Taste kauft das Item sofort, wenn der Kauf möglich ist (ausreichend Münzen, Inventarplatz frei). Keine Zwischenbestätigung — der Einkauf im Item-Shop ist bewusst ein "Schnellkauf".
2. Ein Druck auf eine **nicht kaufbare** Item-Taste spielt `ui_error`; es wird nichts gekauft, der Shop bleibt offen.
3. **NICHTS KAUFEN** (Nord-Taste) schließt den Shop ohne Kauf. Es gibt im Item-Shop **keine** `ui_cancel`-Funktion im klassischen Sinn: Die Ost-Taste ist hier "Item 2 kaufen", nicht "Abbrechen" (dokumentierte Ausnahme, siehe Edge Case 5).
4. **Zusätzlich zur Tasten-Zuordnung** ist die Item-Auswahl per Fokus-Navigation erreichbar (D-Pad links/rechts zwischen den 3 Items, `ui_accept` zum Kaufen), damit Maus-/Tastaturspieler ohne Gesichtstasten-Eindeutigkeit kaufen können. Beide Wege führen zum selben Kaufvorgang.

### 3.6 Item-Shop — Zustände und ArenaStar

**Zustand "Inventar voll" (3 Items belegt, [item-system.md](item-system.md)):**

- Alle 3 Kaufen-Buttons sind grau (deaktiviert).
- Ein Hinweistext erscheint: "Inventar voll! (Max 3 Items)".
- ArenaStar: "Dein Inventar ist voll! Benutze erst ein Item."
- NICHTS KAUFEN bleibt aktiv.

**Zustand "Zu wenig Münzen" (einzelnes Item):**

- Der Kaufen-Button **dieses Items** ist grau; der Preis dieses Items ist in **Rot** dargestellt (nicht nur der Button — die rote Preis-Zahl ist das primäre Signal).
- Items, die der Spieler sich leisten kann, bleiben normal (grüne Buttons, weiße Preise).
- ArenaStar kommentiert beim Hover/Fokus auf ein zu teures Item: "Dafür reichen deine Münzen noch nicht."

**ArenaStar-Kommentare je Item beim Hover/Fokus:**

| Item | Kommentar |
|------|-----------|
| Glücks-Würfel | "Riskiere alles mit einem Würfel bis 10!" |
| Stern-Teleporter | "Schnurstracks zum Stern!" |
| Schutzschild | "Sicher ist sicher!" |
| Münz-Magnet | "Münzen, wohin du auch schaust!" |
| Dieb-Handschuh | "Psst … niemand wird es merken." |

- Der Kommentar erscheint nur für das aktuell fokussierte/gehoverte Item; bei Maus-Hover gilt die 300-ms-Verzögerung aus [ui-board](ui-board.md) 3.9 (Tooltip-Konvention), bei Fokuswechsel sofort.

### 3.7 Kauf-Ablauf und Rückkopplung

- **Item-Kauf:** Beim erfolgreichen Kauf spielt `ui_click` + Kauf-Sound, das Item-Icon springt kurz (Squash-Stretch, 200 ms), die Münzen des Spielers werden abgezogen (Zähler-Roll-Animation im HUD, [ui-hud](ui-hud.md) 3.6), und das Item erscheint im Inventar des Spielers (Item-Slots im HUD füllen sich). Der Shop bleibt offen, damit der Spieler weitere Items kaufen kann, solange Münzen und Inventarplatz reichen.
- **Stern-Kauf:** Wie in 3.3; der Shop schließt nach dem Kauf.
- **Kein Kauf (Ablehnen/Nichts kaufen):** Der Shop schließt; keine Änderung an Münzen oder Inventar.
- **Nach dem Schließen:** Die Kamera bleibt auf dem aktuellen Feld; die nächste Aktion des aktiven Spielers (würfeln, wenn Zug fortgesetzt wird, sonst nächster Spieler) wird wie in [core-loop.md](core-loop.md) fortgesetzt.

## 4. Formulas

### 4.1 Einstiegs-Animation (Ease-Out-Back)

`y(t) = y_end − 60 × (1 − f(t))`, mit `f(t)` = Ease-Out-Back-Interpolation über 300 ms, Überschwinger ~10 %

- `y_end` = Endposition des Fensters (zentriert), `y(t)` = vertikale Position zum Zeitpunkt `t`.
- Konkrete Prüfgröße: Das Fenster überschreitet seine Endposition um höchstens 10 % der Slide-Strecke (60 px → max. +6 px) und landet ohne Nachschwingen innerhalb 300 ms ± 30 ms.
- Akzeptanz: Kein sichtbarer Sprung am Animationsanfang; die Endposition ist nach 300 ms stabil.

### 4.2 Stern-Rotation

`θ(t) = 2π × (t / 8 s)`

- `θ(t)` = Drehwinkel des Shop-Sterns (Radiant), eine volle Umdrehung pro 8 s.
- Akzeptanz: Der Stern dreht gleichmäßig (konstante Winkelgeschwindigkeit); bei Zustand "grau" bleibt die Rotation erhalten (Zustand ändert nur Farbe, nicht Bewegung).

### 4.3 Kaufbarkeit

`K_stern = (M ≥ 20) AND (S_gekauft = falsch)`

`K_item_j = (M ≥ Preis_j) AND (Inventar_belegt < 3)`

- `M` = aktueller Münzbestand des aktiven Spielers, `Preis_j` = Preis des Items `j`, `Inventar_belegt` = Anzahl belegter Item-Slots (0–3).
- Erwartungswerte: Sternpreis `= 20`; Item-Preise aus [item-system.md](item-system.md) (z. B. Glücks-Würfel 5, Teleporter 8, Schild 6, Magnet 4, Handschuh 10).
- Akzeptanz: Der KAUFEN-Button bzw. Item-Button ist genau dann aktiv, wenn `K = wahr`; in allen anderen Fällen ist er deaktiviert (grau) und löst `ui_error` aus.

### 4.4 Preis-Rot-Signal

`Preis_farbe = rot, wenn (M < Preis_j) AND (Inventar_belegt < 3)`

- Akzeptanz: Bei zu wenig Münzen ist die Preis-Zahl des betroffenen Items rot und der Button grau; ist nur das Inventar voll, ist der Preis weiß, aber der Button grau (die Ursachen sind also unterscheidbar dargestellt).

### 4.5 Shop-Dauer

`T_shop ≤ 3 s` (Blockierzeit eines Shop-Besuchs ohne Kauf)

- `T_shop` = Zeit, die der Shop nach dem Öffnen mindestens sichtbar bleibt, bevor der Spieler durch NICHTS KAUFEN/ABLEHNEN schließen kann — es gibt **kein** künstliches Zeitlimit; `T_shop` ist eine Untergrenze für die Schließ-Interaktion (Verhindern von "verschluckten" Tasten, [ui-overview](ui-overview.md) 3.5).
- Akzeptanz: Der Spieler kann den Shop erst nach 3 s nach dem Öffnen schließen; jede Aktion davor wird gepuffert und nach Ablauf ausgeführt.

## 5. Edge Cases

1. **Münzen exakt 20:** `K_stern = wahr` (≥ 20); der Kauf ist erlaubt und lässt den Spieler auf 0 Münzen zurück. Der Zähler zeigt nach dem Kauf "0", nie negativ.
2. **Münzen exakt 0:** Alle Kaufen-Buttons sind grau, Preise rot; NICHTS KAUFEN/ABLEHNEN bleiben aktiv. ArenaStar zeigt den Differenz-Hinweis.
3. **Inventar voll UND zu wenig Münzen:** Beide Mangel-Zustände gelten gleichzeitig; die Hinweistexte werden kombiniert ("Inventar voll!" + roter Preis). Es erscheint kein widersprüchlicher Zustand (kein aktiver Button).
4. **Item-Shop mit weniger als 3 angebotenen Items:** Das Sortiment kann je Insel/Shop weniger als 3 Items umfassen ([field-item-shop.md](field-item-shop.md)). Leere Slots werden als ausgegraute Platzhalter angezeigt (kein Button, keine Taste). Die Tasten-Zuordnung aus 3.5 gilt nur für tatsächlich vorhandene Items (Item 1 immer Süd, Item 2 immer Ost, Item 3 immer West; es gibt keine "Lücken-Verschiebung").
5. **`ui_cancel`-Ausnahme im Item-Shop:** Die Ost-Taste ist im Item-Shop "Item 2 kaufen", nicht "Abbrechen". Dies ist eine dokumentierte Ausnahme zur globalen `ui_cancel`-Semantik ([ui-overview](ui-overview.md) 3.5). Verlassen geht ausschließlich über NICHTS KAUFEN. Der Sternen-Shop behält die normale `ui_cancel`-Semantik (ABLEHNEN).
6. **Doppel-Öffnung durch schnelles Landen:** Landet der Spieler nacheinander auf Item-Shop- und Sternen-Shop-Feld, kann der zweite Shop erst nach dem Schließen des ersten geöffnet werden; eine automatische Öffnung während eines offenen Shops ist unmöglich (Overlay-Ebene 10 sperrt).
7. **Spieler schließt den Shop und die Runde endet gleichzeitig:** Da nur der aktive Spieler im Shop interagiert und der Zug erst nach dem Schließen fortgesetzt wird, kann die Runde nicht während des Shops enden. Der Fokus kehrt nach dem Schließen immer an das HUD zurück.
8. **Kauf bei unterbrochener Verbindung (Online):** Bei Verbindungsabbruch während des Shops erscheint der Verbindungs-Dialog ([technical-multiplayer.md](technical-multiplayer.md)); der Shop wird geschlossen und nach Wiederverbindung (falls die Partie fortgesetzt wird) erneut in seinem letzten Zustand geöffnet (Kauf/kein Kauf ist serverseitig entschieden).
9. **Stern bereits gekauft, aber Münzen ausreichend:** Es gilt Zustand "Stern gekauft"; der KAUFEN-Button bleibt grau, auch wenn der Spieler 20+ Münzen hat. Der Stern ist pro Statuen-Position nur einmal kaufbar ([star-economy.md](star-economy.md)).
10. **Maus-Fokus auf deaktiviertem Item:** Ein Klick auf einen grauen Item-Button spielt `ui_error` und wählt nichts aus; der Mauszeiger ändert sich nicht in den "Klick"-Cursor über deaktivierten Buttons (visuelle Signale: grauer Button, roter Preis, Hinweistext).

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `ui-shop.md` | Art | Verwendung |
|----------------------------|-----|------------|
| `design/gdd/ui-overview.md` | Dach | Liefert Tokens, Overlay-Ebenen, Fokus-Regeln, ControlHelper, UI-Sound und Transitions. |
| `design/gdd/ui-hud.md` | Peer | Zeigt Münz-/Stern-Zähler und Item-Slots, die beim Kauf animiert werden; Fokus-Rückkehr an den Würfel-Button. |
| `design/gdd/ui-board.md` | Peer | Die Kamera steht während des Shops; die Feld-UI zeigt den Shop-Auslöser. |
| `design/gdd/star-economy.md` | Quelle | Definiert Sternpreis (20), Kauf-Regeln und Statuen-Positionierung. |
| `design/gdd/item-system.md` | Quelle | Definiert Items, Preise, Inventar-Limit (3) und Nutzungs-Zeitpunkt. |
| `design/gdd/coin-economy.md` | Quelle | Definiert den Münzbestand, der die Kaufbarkeit (4.3) bestimmt. |
| `design/gdd/field-star-shop.md`, `field-item-shop.md` | Quelle | Lösen den Shop-Auslöser aus und definieren das Sortiment. |
| `design/gdd/narrative-arena-star.md` | Nachgeordnet | Muss die ArenaStar-Kommentare und den Voice-Vertrag für den Shop konkretisieren. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `design/gdd/ui-hud.md` | Verwendet den Shop-Ablauf, um Zähler und Inventar nach dem Kauf zu aktualisieren. |
| `design/gdd/audio-ui.md` / `audio-sfx.md` | Muss ui_open/ui_click/ui_error/ui_back sowie Kauf- und Stern-Sounds liefern. |
| `design/gdd/item-system.md` | Muss die Kaufbestätigung (Inventar befüllen) auf den Kauf-Button-Trigger anbinden. |
| `design/gdd/technical-multiplayer.md` | Muss die serverseitige Kauf-Entscheidung und Verbindungsunterbrechung absichern. |

### 6.3 Bidirektionalität

Der Shop ist ein Overlay über dem BoardHUD: [ui-hud.md](ui-hud.md) spezifiziert die Zähler, die der Shop anspricht, und [ui-shop.md](ui-shop.md) definiert, wie diese Zähler während des Shops gesperrt sind. Die Ökonomie-Kapitel liefern die Preise und Regeln; dieses Kapitel liefert der Ökonomie die Darstellung. Eine Änderung des Sternpreises in `star-economy.md` muss in den Zuständen dieses Kapitels (3.2, 4.3) ohne UI-Änderung wirksam bleiben (Preise kommen aus der Datenquelle, nicht aus hartkodierten UI-Werten).

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Slide-Strecke | Feel | 30–120 px | 60 px | Distanz des Einflugs; größer = schwungvoller |
| Einstiegs-Dauer | Feel | 200–500 ms | 300 ms | Tempo des Einflugs |
| Überschwinger (Back) | Feel | 0–20 % | 10 % | Stärke des Ease-Out-Back-Schwungs |
| Schließ-Dauer | Feel | 100–300 ms | 150 ms | Tempo des Schließens |
| Stern-Rotationsdauer | Feel | 4–16 s | 8 s | Rotationsgeschwindigkeit des Shop-Sterns |
| Overlay-Schwärze | Feel | 40–80 % | 60 % | Abdunklung des Boards hinter dem Shop |
| Fenster-Breite Sternen-Shop | Feel | 560–960 px | 720 px | Größe des Shop-Fensters |
| Fenster-Breite Item-Shop | Feel | 800–1200 px | 960 px | Größe des Shop-Fensters |
| Item-Icon-Größe | Feel | 96–160 px | 128 px | Größe der Item-Icons und des Shop-Sterns |
| Minimale Schließ-Sperre `T_shop` | Gate | 0,5–5 s | 3 s | Zeit, bevor der Shop geschlossen werden kann |

## 8. Acceptance Criteria

Ein QA-Tester kann folgende Prüfungen ausführen:

1. **Overlay-Verhalten:** Das Overlay ist 60 % Schwarz, das Fenster ist zentriert; Eingaben erreichen das Board nicht, solange der Shop offen ist; die Kamera steht still. PASS/FAIL.
2. **Einstiegs-Animation:** Das Fenster fliegt in 300 ms (Ease-Out-Back, Überschwinger ≤ 10 % der Slide-Strecke) von unten ein und ist danach stabil. PASS/FAIL.
3. **Sternen-Shop — Kaufbar:** Bei `M ≥ 20` und nicht gekauftem Stern ist der Stern golden, KAUFEN grün; `ui_accept` bestätigt den Kauf, zieht 20 Münzen ab, erhöht den Stern-Zähler und schließt den Shop. PASS/FAIL.
4. **Sternen-Shop — Zu wenig Münzen:** Bei `M < 20` ist der Stern grau, KAUFEN grau (deaktiviert), der Hinweistext und ArenaStar ("Du brauchst 20 Münzen! Du hast nur X.") erscheinen; ein Aktivierungsversuch spielt `ui_error`. PASS/FAIL.
5. **Sternen-Shop — Bereits gekauft:** Bei bereits gekauftem Stern ist KAUFEN grau, unabhängig vom Münzbestand; der Hinweistext "Der Stern wurde bereits gekauft. Versuche es am nächsten Shop!" erscheint. PASS/FAIL.
6. **Sternen-Shop — Ablehnen:** `ui_cancel` bzw. ABLEHNEN schließt den Shop ohne Änderungen an Münzen oder Sternen. PASS/FAIL.
7. **Item-Shop — Aufbau:** 3 Items nebeneinander mit Icon (128 × 128), Name, 1-Zeilen-Beschreibung, Preis und Kaufen-Button; NICHTS KAUFEN unten zentriert. PASS/FAIL.
8. **Item-Shop — Tasten-Zuordnung:** Item 1 = Süd, Item 2 = Ost, Item 3 = West, NICHTS KAUFEN = Nord (Layout-korrigierte Labels); ein Druck auf eine kaufbare Item-Taste kauft sofort, ohne Zwischenbestätigung. PASS/FAIL.
9. **Item-Shop — Inventar voll:** Bei 3 belegten Slots sind alle Kaufen-Buttons grau, der Hinweis "Inventar voll! (Max 3 Items)" erscheint; NICHTS KAUFEN bleibt aktiv. PASS/FAIL.
10. **Item-Shop — Zu wenig Münzen:** Bei `M < Preis_j` ist der Button des Items grau und der Preis rot; andere Items bleiben kaufbar; ArenaStar kommentiert das Item beim Hover/Fokus. PASS/FAIL.
11. **Kauf-Rückkopplung:** Nach einem Item-Kauf spielt der Sound, das Icon springt (Squash-Stretch 200 ms), die Münzen rollen im HUD, das Inventar füllt sich, der Shop bleibt offen. PASS/FAIL.
12. **Erlebbar (Experiential):** Eine Testperson erkennt in unter 5 Sekunden, ob sie sich ein Item/einen Stern leisten kann und welche Taste kauft bzw. den Shop verlässt. PASS/FAIL.
