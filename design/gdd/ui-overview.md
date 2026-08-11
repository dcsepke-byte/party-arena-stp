# UI-Overview — Party Arena Game Bible

> **Teil:** VII — UI/UX
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/vision-pillars.md

---

## 1. Overview

Dieses Kapitel definiert das UI-Gesamtsystem von Party Arena: die Architektur auf Basis von Godot-Control-Nodes und Theme-System, den Katalog aller Screens und Overlays, das Overlay-Modell (kein Screen-Stack), die verbindlichen Design-Tokens (Farben, Typografie, Abstände, Radien, Outlines), die Skalierung relativ zu einer 1920×1080-Basisauflösung, das einheitliche Input-Handling über den ControlHelper (STP), das UI-Sound-System (UISound Autoload), die Fokus- und Navigationsregeln für Gamepad, Tastatur und Maus sowie die Transitionen zwischen Screens und Overlays. Es ist das Dach aller nachfolgenden `ui-*.md`-Kapitel: Jede UI-Entscheidung in [ui-mainmenu](ui-mainmenu.md), [ui-hud](ui-hud.md), [ui-board](ui-board.md), [ui-shop](ui-shop.md), [ui-character-select](ui-character-select.md) und [ui-accessibility](ui-accessibility.md) muss die hier definierten Tokens, Regeln und Formeln einhalten. Das Spiel rendert ausschließlich SDR; eine HDR-Pipeline ist nicht vorgesehen und wird nicht unterstützt.

## 2. Player Fantasy

Das UI von Party Arena soll sich anfühlen wie ein **lebendiges Spielzeug, das auf jede Berührung antwortet** und nie fragt, was als Nächstes kommt. Der Spieler soll jeden Bildschirm sofort lesen können: leuchtende, dicke, cartoonhafte Bedienelemente auf dunklem Grund, große abgerundete Panels, klare Symbole und eine Schrift, die nach Spielspaß aussieht, nicht nach Anleitung. Drei konkrete Versprechen:

1. **"Ich weiß sofort, wo ich bin und was ich tun kann."** Jeder Screen hat genau einen klaren Fokus (Hauptaktion), die aktive Auswahl ist immer sichtbar umrandet, und es gibt nie zwei gleichstarke Aktionen, die um die Aufmerksamkeit konkurrieren (Pfeiler: Sofort verständlich).
2. **"Alles fühlt sich lebendig an."** Jede Eingabe quittiert sich sichtbar und hörbar innerhalb von 0,2 Sekunden: Buttons federn, Klicks klingen cartoonhaft, Overlays gleiten mit Schwung ein, der Fokusrahmen pulsiert (Pfeiler: Interaktiv wirkend).
3. **"Das hier ist ein Party-Spielzeug, kein Office-Programm."** Abgerundete Ecken, dicke Outlines, hohe Sättigung und der Komika-Axis-Schriftzug machen jede UI zu einem Teil der Spielzeugwelt, nicht zu einem davon getrennten Systemmenü (Pfeiler: Überzeichnet, Wiedererkennbar).

Der 2-Minuten-Test aus [vision-pillars.md](vision-pillars.md) gilt für das UI verschärft: Ein neuer Spieler muss ohne Anleitung erkennen, welcher Screen aktiv ist, welches Element fokussiert ist und wie er die Hauptaktion auslöst.

## 3. Detailed Rules

### 3.1 Screens und Overlays (Gesamtkatalog)

Party Arena kennt genau **10 Screens** und **3 Overlay-Typen**. Ein Screen ist ein Vollbild-Control-Root; ein Overlay ist ein modales oder nicht-modales Fenster über dem aktiven Screen.

**Screens (Vollbild):**

| Screen | Zweck | Erreichbar von | Verlassen zu |
|--------|-------|----------------|--------------|
| `MainMenu` | Hauptmenü, Spielstart, Einstellungen, Statistik, Credits | Boot | Lobby, SettingsMenu, StatisticsScreen, CreditsScreen, Beenden |
| `Lobby` | Host/Join, Spieler-Setup, Insel- und Rundenwahl, Server-Browser | MainMenu | CharacterSelect, MainMenu |
| `CharacterSelect` | Charakter-Auswahl vor Spielstart | Lobby | Lobby (Host), BoardHUD |
| `BoardHUD` | Das aktive Brettspiel (Board + HUD) | CharacterSelect | PauseMenu, VictoryScreen |
| `MinigameHUD` | Ein laufendes Minispiel (eigener UI-Rahmen) | BoardHUD | BoardHUD |
| `VictoryScreen` | Siegerehrung nach der letzten Runde | BoardHUD | MainMenu, Lobby |
| `SettingsMenu` | Audio, Video, Sprache, Eingabe | MainMenu, PauseMenu (als Overlay) | MainMenu, PauseMenu |
| `StatisticsScreen` | Persönliche Statistik | MainMenu | MainMenu |
| `CreditsScreen` | Credits | MainMenu | MainMenu |
| `LoadingScreen` | Übergang mit Ladeanzeige | überall | Ziel-Screen |

**Overlays (über aktivem Screen):**

| Overlay | Modal? | Öffnet über | Schließen durch |
|---------|--------|-------------|-----------------|
| `PauseMenu` | Ja | BoardHUD, MinigameHUD | Fortsetzen, Zurück zum Menü, Einstellungen |
| `ShopOverlay` | Ja | BoardHUD (Sternen-Shop-Feld, Item-Shop-Feld) | Kaufen/Ablehnen/Abbruch |
| `ArenaStarPopup` (Sprechblase + Kommentar) | Nein | jedem Screen | automatisch nach Ablauf |
| `ConfirmDialog` (Bestätigungs-/Fehlerdialog) | Ja | jedem Screen | Bestätigen/Abbrechen |

### 3.2 Overlay-Modell — kein Screen-Stack

Es gibt **keinen Screen-Stack**. Zu jedem Zeitpunkt ist genau ein Screen aktiv; Overlays werden über dem aktiven Screen in festen Ebenen (Layern) dargestellt. Wird ein Overlay geschlossen, ist automatisch wieder der darunterliegende Screen aktiv — es wird nichts "zurückgepoppt". Diese Regel gilt ausnahmslos, auch bei Overlay-über-Overlay (z. B. ConfirmDialog über ShopOverlay).

**Ebenen-Reihenfolge (von unten nach oben):**

1. Ebene 0: Aktiver Screen (Vollbild)
2. Ebene 10: Modale Overlays (`ShopOverlay`, `PauseMenu`) — Öffnungs-Reihenfolge bei mehreren: das zuletzt geöffnete liegt oben
3. Ebene 20: `ConfirmDialog` (immer über allen modalen Overlays)
4. Ebene 30: Nicht-modale `ArenaStarPopup`s und Toasts (blockieren keine Eingabe, keine Fokusänderung)
5. Ebene 40: `LoadingScreen` (blockiert Eingabe vollständig, höchste Ebene)
6. Ebene 50: System-Fehlerdialog (nur bei schweren Fehlern, über allem)

**Regeln für modale Overlays:**

1. Ein modales Overlay blockiert jede Eingabe an den darunterliegenden Screen vollständig (Fokus-Isolation).
2. Beim Öffnen wandert der Fokus auf das erste logische Element des Overlays (Definition pro Overlay in den jeweiligen Kapiteln).
3. Beim Schließen kehrt der Fokus auf das Element des darunterliegenden Screens zurück, das vor dem Öffnen fokussiert war.
4. Es darf höchstens ein `ConfirmDialog` gleichzeitig existieren. Wird ein zweiter angefordert, ersetzt er den ersten (der erste gilt als abgebrochen).
5. Nicht-modale Overlays (`ArenaStarPopup`) verschieben den Fokus nie und blockieren keine Eingabe; sie kollidieren nicht mit dem aktiven Fokus.

### 3.3 Design-Tokens

Alle Tokens sind im Theme-System (`default_theme.tres`) als Theme-Konstanten, Theme-Farben und Theme-Fonts hinterlegt. Kein UI-Element definiert Farben, Radien oder Schriftgrößen hart im Node; alles entstammt dem Theme.

#### 3.3.1 Farben (SDR, dunkler Grund)

| Token | Wert (Hex) | Verwendung |
|-------|-----------|------------|
| `bg_e0` | `#1A1A24` | Hintergrund Vollbild-Screens |
| `bg_e1` | `#23233A` | Panels, Karten, Fenster |
| `bg_e2` | `#2E2E4A` | Innerhalb von Panels, Input-Felder |
| `outline` | `#0D0D14` | Outlines auf Panels und Buttons |
| `primary` | `#FFD93D` | Hauptaktion, Fokus, CTA-Buttons (Gelb) |
| `primary_text` | `#1A1A24` | Text auf `primary`-Flächen |
| `secondary` | `#4DD0E1` | Sekundäraktionen, Info (Türkis) |
| `success` | `#66BB6A` | Kaufen, Bestätigen, positiv (Grün) |
| `danger` | `#EF5350` | Ablehnen, Verlassen, negativ (Rot) |
| `text_primary` | `#FFFFFF` | Haupttext |
| `text_secondary` | `#B8B8C8` | Sekundärtext, Beschriftungen |
| `text_disabled` | `#6A6A7E` | Deaktivierte Elemente |
| `focus_ring` | `#FFFFFF` | Fokus-Rahmen (immer kontrastierend) |

**Spieler-Farben (8, kanonisch):** P1 `#E53935` (Rot), P2 `#F57C00` (Orange), P3 `#C0CA33` (Limette), P4 `#43A047` (Grün), P5 `#26A69A` (Mint), P6 `#1E88E5` (Blau), P7 `#8E24AA` (Violett), P8 `#EC407A` (Pink). Alle benachbarten Farbabstände im HSV-Hue ≥ 30° (Prüfung in [ui-accessibility](ui-accessibility.md)). Die 8 Farben gelten für Portraits, Spieler-Marker, Namensschilder und Spieler-spezifische UI-Akzente.

#### 3.3.2 Typografie

| Token | Wert |
|-------|------|
| `font_primary` | Komika Axis (Cartoon-Font). Fallback bei Lizenzfrage: Baloo 2 (Open Source, gleiche cartoon-Ästhetik). |
| `font_caption` | 16 px — **globale Mindestgröße**, kein UI-Text darf kleiner dargestellt werden |
| `font_body` | 20 px |
| `font_button` | 24 px |
| `font_subtitle` | 28 px |
| `font_title` | 36 px |
| `font_headline` | 48 px (Logo, Runden-Titel) |

Alle Größen sind Basisgrößen bei Text-Multiplikator 1,0 und beziehen sich auf die 1920×1080-Basisauflösung. Der Multiplikator `t_text` (1,0 / 1,25 / 1,5, siehe [ui-accessibility](ui-accessibility.md)) skaliert ausnahmslos alle UI-Texte; eine Ausnahme von dieser Regel ist nicht zulässig. Ziffern für Zähler (Münzen, Sterne, Runden) verwenden dieselbe Schrift, werden aber mit tabellarischer Ziffernbreite gesetzt, damit Zähler beim Ändern nicht springen.

#### 3.3.3 Abstände, Radien, Outlines

- **Abstands-Raster:** 4-px-Basis. Zulässige Abstände: 4, 8, 12, 16, 24, 32, 48. Keine Zwischenwerte.
- **Radius:** Panels, Fenster und Buttons: **12 px** (Standard, verbindlich). Vollrunde "Pill"-Form (Radius = halbe Höhe) ist nur für Chips, Badges und kleine Icon-Buttons erlaubt, nicht für primäre Aktions-Buttons.
- **Outlines:** Panels und Buttons haben eine **3 px** dicke Outline in `outline` (`#0D0D14`). Der Fokus-Rahmen ist davon getrennt (siehe 3.7) und hat 2 px.

### 3.4 Skalierung und Auflösungen

- **Basisauflösung:** 1920×1080. Alle Layouts und Tokens sind relativ zu dieser Auflösung definiert.
- **Stretch-Modus:** Das Projekt verwendet Godot-Stretch mit Basis 1920×1080 und proportionalem Seitenverhältnis (keep aspect). Das gesamte UI liegt unter einem `CanvasLayer`-Root, der über das Stretch-System skaliert; es wird keine manuelle Einzelskala auf Controls gelegt.
- **Formel** für den Skalierungsfaktor: siehe Sektion 4.1.
- **Safe-Areas:** UI-Ränder halten einen Mindestabstand von 24 px zu allen Bildschirmrändern ein; auf Geräten mit Notch/Display-Ausschnitt (Touch) wird der Rand auf 48 px erhöht. Kritische Elemente (Buttons, Zähler) liegen nie näher als 24 px am Rand.
- **Unterstützte Formate:** 16:9 (Ziel), 16:10 und 4:3 werden durch Letterboxing (schwarze Balken) abgedeckt; kein UI-Element wird beschnitten. Formate außerhalb von 4:3 bis 16:9 sind nicht unterstützt (z. B. 21:9 wird auf 16:9 zentriert dargestellt).
- **Minimal-Auflösung:** 1280×720. Darunter wird das Spiel nicht unterstützt; die effektive Mindestschriftgröße (Sektion 4.2) muss auch bei 1280×720 noch ≥ 16 px betragen.

### 3.5 Input-Handling (ControlHelper)

Der **ControlHelper (STP)** ist die einzige Instanz, die physische Eingaben (Gamepad, Tastatur, Maus) in logische UI-Aktionen übersetzt. Kein Screen wertet physische Tasten direkt aus; alle Screens reagieren nur auf logische Aktionen. Damit sind Layout-Unterschiede (Xbox/PlayStation/Nintendo), Remapping ([ui-accessibility](ui-accessibility.md)) und spätere Touch-Unterstützung zentral gelöst.

**Logische UI-Aktionen und Standard-Belegung:**

| Logische Aktion | Xbox | PlayStation | Nintendo Switch | Tastatur | Maus |
|------------------|------|-------------|------------------|----------|------|
| `ui_accept` (Bestätigen) | A | X (Cross) | A | Enter, Leertaste | Linksklick |
| `ui_cancel` (Abbrechen/Zurück) | B | Kreis | B | Escape, Rücktaste | Rechtsklick |
| `ui_up/down/left/right` (Navigation) | D-Pad + linker Stick | D-Pad + linker Stick | D-Pad + linker Stick | Pfeiltasten, WASD | — (Hover) |
| `ui_pause` (Pause/Menü) | Start | Options | + | Escape, P | — |
| `ui_tab_left/right` (Item-Slots, Reiter) | LB/RB | L1/R1 | L/ZL, R/ZR | 1/2/3, Q/E | — |
| `ui_toggle` (Kamera/Minimap) | Select/Back, Y | Share/Touchpad, Dreieck | −, Y | Tab | — |

Regeln:

1. **Eindeutige Quellen:** Maus-Hover setzt den Hover-State; der Tastatur/Gamepad-Fokus ist davon unabhängig. Ein Klick aktiviert das Element unter dem Mauszeiger.
2. **Layout-Auflösung:** Der ControlHelper erkennt den Controllertyp und zeigt in allen UI-Beschriftungen (z. B. "A / Enter") die korrekte Taste des erkannten Layouts an. Wird kein Gamepad erkannt, gelten Tastatur-Beschriftungen.
3. **Gemischte Eingabe:** Wechselt ein Spieler zwischen Maus und Gamepad, übernimmt die zuletzt genutzte Eingabequelle die Führung; der Fokus folgt der aktiven Quelle.
4. **Input-Pufferung:** Wird eine Aktion 100 ms vor dem Ende einer Transition oder Overlay-Animation abgeschickt, wird sie gepuffert und nach Abschluss ausgeführt. Ältere Eingaben werden verworfen (verhindert "verschluckte" Bestätigungen beim Screen-Wechsel).
5. **Wiederholung:** Wiederholte Navigation (D-Pad gedrückt halten) folgt dem OS-Standard (Erstverzögerung 400 ms, danach 120 ms Intervall). Für die Maus gilt keine Wiederholung.

### 3.6 UI-Sound (UISound Autoload)

Der **UISound Autoload (STP)** ist die einzige Quelle für UI-Sounds. Jede UI-Interaktion hat einen zugeordneten Sound:

| Ereignis | Sound | Lautstärke |
|----------|-------|------------|
| Hover / Fokuswechsel | `ui_hover` (kurzer Tick, 40 ms) | −18 dB |
| Aktivierung (Klick/Bestätigen) | `ui_click` (Cartoon-Pop, 80 ms) | −12 dB |
| Overlay öffnen | `ui_open` (Slide-Pop, 150 ms) | −12 dB |
| Overlay schließen | `ui_close` (Slide-down, 120 ms) | −14 dB |
| Fehler (deaktiviertes Ziel) | `ui_error` (tiefer Buzz, 120 ms) | −10 dB |
| Zähler-Änderung (Münzen) | `ui_counter` (Klick pro Ziffernschritt) | −14 dB |
| Zurück (cancel) | `ui_back` (tieferes Pop, 100 ms) | −14 dB |

Regeln:

1. **Jeder Button-Klick spielt `ui_click`.** Ausnahme: ein deaktivierter Button spielt beim Aktivierungsversuch `ui_error` und führt die Aktion nicht aus.
2. Sounds laufen auf dem UI-Bus und respektieren die Einstellung "UI" aus [ui-mainmenu](ui-mainmenu.md). Die Hover-Sounds können gemeinsam mit dem UI-Tab "Hinweise" deaktiviert werden (siehe 3.6-Regel 3).
3. Hover-Sounds werden nicht abgespielt, wenn der Fokus über Maus-Hover und nicht über Tastatur/Gamepad gewechselt hat — vermeidet Dauergeplätscher bei Mausnutzung.
4. UI-Sounds dürfen den Spiel- und Musikbus nicht beeinflussen und werden bei aktiviertem Mono-Audio ([ui-accessibility](ui-accessibility.md)) korrekt gemischt.

### 3.7 Navigation und Fokus

1. **Explizite Fokus-Nachbarn:** Jedes fokussierbare Element setzt die Fokus-Nachbarn (oben/unten/links/rechts) explizit. Automatische Fokusberechnung ist nicht zulässig, da sie bei Gamepad-Navigation zu Sprüngen führt.
2. **Fokus-Rahmen immer sichtbar:** Das fokussierte Element hat einen **2 px** breiten `focus_ring`-Rahmen (`#FFFFFF`) mit einem Abstand von 2 px zur Elementkante. Der Rahmen ist in jedem Zustand sichtbar (auch bei aktivem Hover), damit Gamepad-Spieler die Position immer sehen.
3. **Fokus-Hierarchie:** Fokus reiht sich in Leserichtung (links→rechts, oben→unten) aneinandergereiht; die expliziten Nachbarn haben Vorrang vor der Lesereihenfolge.
4. **Erster Fokus:** Jeder Screen/Overlay definiert ein "First-Focus-Element" (in den Kapiteln spezifiziert). Beim Betreten wird dieses fokussiert.
5. **Keine toten Zonen:** Jedes fokussierbare Element führt über seine Nachbarn zu mindestens einem anderen Element; es gibt keine Elemente, die per Gamepad unerreichbar sind (Prüfung in Sektion 8).
6. **Deaktivierte Elemente:** Deaktivierte Elemente (z. B. grauer Kaufen-Button) sind nicht fokussierbar und werden in der Fokus-Navigation übersprungen. Die Ursache der Deaktivierung wird separat als Text/Badge angezeigt (nie nur durch Farbe).
7. **Scrollen:** Übersteigt ein Panel seinen Inhalt, wird beim Fokussieren automatisch zum fokussierten Element gescrollt (Scroll-Offset so, dass das Element vollständig sichtbar ist).

### 3.8 Transitionen

| Übergang | Dauer | Kurve | Beschreibung |
|----------|-------|-------|--------------|
| Vollbild-Screen-Wechsel | 300 ms | Ease-In-Out | Crossfade: neuer Screen blendet über den alten ein; alter Screen blockiert währenddessen keine Eingabe |
| Modal-Overlay öffnen | 200 ms | Ease-Out | Slidet von unten ins Bild (Startposition: 40 px unterhalb des Endpunkts) |
| Modal-Overlay schließen | 150 ms | Ease-In | Slidet nach unten aus dem Bild (Zielposition: 40 px unterhalb) |
| ArenaStarPopup ein/aus | 250 ms | Ease-Out / Ease-In | Fade + leichter Zoom (95 % → 100 %) |
| LoadingScreen | 300 ms | Ease-In-Out | Fade; Mindestanzeigedauer 500 ms (siehe 4.4) |

Regeln:

1. Während einer Transition wird der Fokus nicht neu gesetzt; er wandert erst nach Abschluss der Transition auf das First-Focus-Element des neuen Screens.
2. Transitions können durch die Einstellung "Reduzierte Bewegung" ([ui-accessibility](ui-accessibility.md)) auf einen 100-ms-Fade ohne Slide- oder Zoom-Komponente reduziert werden.
3. Keine Transition dauert länger als 300 ms; der Pfeiler "Interaktiv wirkend" (Feedback-Latenz ≤ 0,5 s) bleibt damit gewahrt.

### 3.9 Konsistenz-Regeln (verbindlich für alle ui-Kapitel)

1. **Eine Hauptaktion pro Screen/Overlay.** Sie ist visuell dominant (größter Button, `primary`-Farbe, unten rechts positioniert). Sekundäraktionen sind kleiner und in `secondary`.
2. **Buttons links unten / rechts unten:** Abbruch-Aktionen (`ui_cancel`) stehen immer links von Bestätigungs-Aktionen. Auf Gamepad: Ost-Button (`ui_cancel`) = links, Süd-Button (`ui_accept`) = rechts — damit die physische Tastenlogik (rechts = bestätigen) mit der räumlichen Anordnung übereinstimmt.
3. **Symbole über Text:** Kritische Zustände (Münzen, Sterne, Runden, aktiver Spieler) werden primär durch Icons + Zahlen dargestellt; Text ist Ergänzung.
4. **Einheitliche Icons:** Icons entstammen dem Icon-Vokabular des Themes; kein Screen definiert eigene Icon-Symbole für bereits vokabularisierte Konzepte.
5. **Deaktivierung sichtbar machen:** Deaktivierte Elemente werden nie nur durch Farbe als deaktiviert markiert; zusätzlich wird die Ursache als Text oder Icon angezeigt.
6. **Keine Text-Duplikation:** Eine Zahl (z. B. Münzen) existiert zu jedem Zeitpunkt höchstens einmal sichtbar pro Kontext; keine doppelten Zähler.

### 3.10 HDR-Unterstützung

Party Arena unterstützt **kein HDR**. Konkret: Die Rendering-Pipeline ist SDR-only; 2D-HDR-Buffer sind deaktiviert; alle UI-Farben sind im sRGB-Farbraum definiert und dürfen nicht auf HDR-Werte (> 1,0) skaliert werden. Die Einstellung für HDR wird weder angeboten noch getestet. Farb-Tokens (3.3.1) gelten damit unverändert auf allen unterstützten Ausgabegeräten.

## 4. Formulas

### 4.1 UI-Skalierungsfaktor

`s = min(W_viewport / 1920, H_viewport / 1080)`

- `W_viewport` = Breite des Viewports in Pixeln, `H_viewport` = Höhe des Viewports in Pixeln.
- Das UI wird als Ganzes um den Faktor `s` skaliert (Stretch keep aspect); `s` ist für Breite und Höhe identisch.
- Erwartungswerte: Bei 1920×1080 gilt `s = 1,0`; bei 1280×720 gilt `s = 720/1080 = 0,667`; bei 2560×1440 gilt `s = 1440/1080 = 1,333`.
- Akzeptanz: Für jede unterstützte Auflösung (16:9, 16:10, 4:3, siehe 3.4) gilt `s ∈ [0,667; 1,333]` ohne Verlust von UI-Inhalten.

### 4.2 Effektive Mindestschriftgröße

`F_eff = F_caption × s × t_text`

- `F_caption` = 16 px (Basis-Mindestgröße), `s` = Skalierungsfaktor (4.1), `t_text` = Text-Multiplikator (1,0 / 1,25 / 1,5).
- Akzeptanz: Für alle unterstützten Auflösungen und alle Text-Multiplikatoren gilt `F_eff ≥ 16 px`. Kritischer Fall: 1280×720 bei `t_text = 1,0`: `F_eff = 16 × 0,667 × 1,0 ≈ 10,7 px` — dies ist **nicht** zulässig; deshalb gilt die Zusatzregel, dass der Stretch-Modus bei Auflösungen unter 1920×1080 die Schriftgrößen um den Faktor `1/t_min` anhebt, wobei `t_min = max(s, 1,0)` gilt (Schrift wird nie kleiner skaliert als auf Basisauflösung). Damit gilt bei 1280×720: `F_eff = 16 × max(0,667;1,0) × 1,0 = 16 px`. Diese Regel ist verbindlich; eine Unterschreitung von 16 px ist ein Blocker.

### 4.3 Fokus-Reichbarkeit

`R_fokus = e_fokussierbar / E_gesamt`

- `e_fokussierbar` = Anzahl der fokussierbaren Elemente, die per Gamepad-Navigation (ausgehend vom First-Focus) erreichbar sind,
- `E_gesamt` = Gesamtzahl der fokussierbaren Elemente auf dem Screen.
- Akzeptanz: `R_fokus = 1,0` für jeden Screen und jedes Overlay. Jedes `e` mit `R_fokus < 1,0` ist ein Defekt (Fokus-Falle).

### 4.4 Loading-Mindestanzeige

`T_loading = max(D_lade, 0,5 s)`

- `D_lade` = tatsächliche Ladedauer des Zielinhalts.
- Akzeptanz: Der LoadingScreen ist nie kürzer als 0,5 s sichtbar (verhindert Flackern), aber bei `D_lade > 5 s` wird zusätzlich eine Fortschrittsanzeige und ein ArenaStar-Hinweis eingeblendet.

### 4.5 UI-Feedback-Latenz

`F = t_eingabe − t_anzeige`

- `t_eingabe` = Zeitpunkt der Spieler-Eingabe, `t_anzeige` = Zeitpunkt der ersten sicht- oder hörbaren Bestätigung.
- Zielwert: `F ≤ 0,2 s` für alle UI-Interaktionen (strenger als der globale 0,5-s-Wert aus [vision-pillars.md](vision-pillars.md), weil UI-Latenz als besonders kritisch gilt).
- Akzeptanz: Stichprobe von 20 UI-Interaktionen (Menü-Auswahl, Kaufen, Pfadwahl, Item-Nutzung) ergibt in 100 % der Fälle `F ≤ 0,2 s`.

### 4.6 Fokus-Kontrast

`C = (L_fokus + 0,05) / (L_hintergrund + 0,05)`

- `L_fokus` = relative Leuchtdichte des Fokus-Rahmens (`focus_ring`, Weiß), `L_hintergrund` = relative Leuchtdichte der Fläche, auf der der Rahmen liegt.
- Akzeptanz: `C ≥ 3:1` für den Fokus-Rahmen gegen jede mögliche Hintergrundfläche (dunkle Panels, helle Buttons, Spielfläche). Für Text gilt zusätzlich `C ≥ 4,5:1` gegen den jeweiligen Hintergrund (WCAG-AA).

## 5. Edge Cases

1. **Auflösungswechsel während des Spiels:** Wird die Auflösung während einer laufenden Partie geändert (SettingsMenu aus dem PauseMenu), skaliert das UI live über `s` neu; laufende Animationen werden nicht unterbrochen, Fokus und Fokusposition bleiben erhalten. PASS/FAIL-Prüfung: Der Fokus liegt nach dem Wechsel auf demselben Element wie vorher.
2. **Controller-Trennung mitten in der Navigation:** Wird der aktive Controller getrennt, übernimmt automatisch die nächste verfügbare Eingabequelle (anderes Gamepad oder Tastatur); der Fokus bleibt erhalten. Ist keine Quelle mehr vorhanden, öffnet der `ConfirmDialog` "Controller nicht gefunden — Tastatur verwenden?" mit Tastatur-Fokus.
3. **Overlay über Overlay:** Wird aus dem `PauseMenu` das `SettingsMenu` als Overlay geöffnet und daraus ein `ConfirmDialog`, liegt dieser auf Ebene 20. Schließt der Dialog, kehrt der Fokus in das SettingsMenu-Overlay zurück, nicht in den Screen darunter (Regel 3.2.3).
4. **Lokalisierung mit langen Strings:** Sprachen wie DE/FR können um > 40 % längere Strings erzeugen. Jedes Text-Label hat einen definierten Maximalraum; Überschreitungen werden durch automatisches Layout (Zeilenumbruch, kleineres `font_body` ist NICHT erlaubt) oder durch ein Icon + Kurztext gelöst. Grundsätzlich werden Symbole bevorzugt (3.9.3). Siehe Sprachliste in [ui-mainmenu](ui-mainmenu.md).
5. **Deaktivierter Button mit Fokus-Anspruch:** Da deaktivierte Buttons nicht fokussierbar sind (3.7.6), muss der Grund der Deaktivierung immer als Text/Badge daneben stehen; sonst ist der Zustand für Tastatur-/Gamepad-Spieler unsichtbar.
6. **Maus + Gamepad gleichzeitig:** Hover-State und Fokus-State können unterschiedliche Elemente meinen. Klick aktiviert das Maus-Ziel; Gamepad-Navigation bewegt nur den Fokus. Nach einer Gamepad-Eingabe wird der Maus-Hover ausgeblendet (bis die Maus wieder bewegt wird), um Doppel-Hervorhebung zu vermeiden.
7. **Transitionen bei deaktivierter Reduzierte-Bewegung-Einstellung:** Alle Slide-/Zoom-Transitionen (3.8) werden bei "Reduzierte Bewegung" auf 100-ms-Fades reduziert; dies gilt auch für Shop-, Item- und ArenaStar-Animationen der Unterkapitel.
8. **Eingabe während LoadingScreen:** Während der LoadingScreen aktiv ist (Ebene 40), werden alle Eingaben verworfen (keine Pufferung über 500 ms hinaus). Eine gehaltene Bestätigungstaste darf nach dem Laden nicht unbeabsichtigt eine Aktion auslösen (Key-Repeat-Sperre: Die erste Eingabe nach dem Laden wird ignoriert, wenn sie innerhalb von 150 ms nach Transitions-Ende kommt).
9. **Kapitel-übergreifende Token-Änderung:** Ändert sich ein Design-Token (3.3), betrifft die Änderung alle Screens. Es gibt keine Ausnahme-Tokens; jede Token-Änderung erfordert einen Review-Eintrag (Regeln aus [bible-index.md](bible-index.md)).
10. **Spielerzahl-Änderung in der Lobby:** Von 2 auf 8 Spieler oder zurück ändert sich die Anzahl der HUD-Slots ([ui-hud](ui-hud.md)) und der Auswahl-Panels ([ui-character-select](ui-character-select.md)) live; das Layout ist für jede Spielerzahl von 2–8 definiert und wird nie zwischen den Runden umgebaut.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `ui-overview.md` | Art | Verwendung |
|--------------------------------|-----|------------|
| `design/gdd/game-concept.md` | Quelle | Liefert die Screens, den Spielablauf und die Stilvorgaben, die hier zu UI-Regeln ausgearbeitet werden. |
| `design/gdd/vision-pillars.md` | Quelle | Definiert die Pfeiler (Sofort verständlich, Interaktiv, Überzeichnet, Wiedererkennbar) und die Feedback-Latenz, die das UI erfüllen muss. |
| `design/gdd/glossary.md` | Peer | Liefert die Fachbegriffe (ControlHelper, UISound, Overlay, Fokus), die hier konsistent verwendet werden. |
| `design/gdd/technical-architecture.md` | Nachgeordnet | Muss die UI-Node-Struktur (Control-Root, CanvasLayer-Ebenen, Theme-Instanziierung) technisch abbilden. |
| `.claude/rules/design-docs.md` | Regelwerk | Definiert den 8-Sektionen-Standard. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| Alle `ui-*.md`-Kapitel (mainmenu, hud, board, shop, character-select, accessibility) | Müssen die Tokens (3.3), Fokus-Regeln (3.7), Transitionen (3.8) und Konsistenz-Regeln (3.9) einhalten. |
| `design/gdd/audio-ui.md` (Teil VIII) | Muss die UISound-Soundspezifikation (3.6) als konkrete Assets und Bus-Zuordnung ausführen. |
| `design/gdd/technical-architecture.md` | Muss ControlHelper und UISound als Systeme verzeichnen (systems-index). |
| `design/gdd/ui-accessibility.md` | Setzt den Text-Multiplikator und die Reduzierte-Bewegung-Einstellung um, die in 3.3.2 und 3.8 referenziert werden. |

### 6.3 Bidirektionalität

Jedes UI-Unterkapitel verweist auf `ui-overview.md` als Dach und muss dessen Regeln spiegeln. Umgekehrt referenziert `ui-overview.md` die Unterkapitel für konkrete First-Focus-Elemente und Overlay-Details. Wird in einem Unterkapitel eine Abweichung von einem Token oder einer Regel nötig, wird sie in diesem Kapitel in Sektion 5 (Edge Cases) ergänzt und im Review-Log vermerkt.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Panel-Radius | Feel | 8–20 px | 12 px | Weichheit der Cartoon-Optik; größere Werte wirken spielzeugartiger |
| Outline-Dicke | Feel | 2–5 px | 3 px | Kontur-Stärke; dicker = cartoonhafter, aber dünner bei kleinen Elementen |
| Fokus-Rahmen-Dicke | Feel | 1–4 px | 2 px | Sichtbarkeit des Fokus; größer = besser sichtbar, aber invasiver |
| Vollbild-Transition | Feel | 100–400 ms | 300 ms | Tempo der Screen-Wechsel |
| Overlay-Transition | Feel | 100–300 ms | 200 ms | Tempo der Modal-Animationen |
| Slide-Versatz | Feel | 16–80 px | 40 px | Strecke des Slide-in/Slide-out |
| Input-Pufferzeit | Gate | 50–200 ms | 100 ms | Fenster, in dem vorzeitig abgeschickte Eingaben übernommen werden |
| Key-Repeat-Sperre nach Transition | Gate | 0–300 ms | 150 ms | Verhindert unbeabsichtigte Aktionen nach dem Laden |
| Hover-Sound | Feel | an/aus | an | Beeinflusst die Geräuschkulisse bei Mausnutzung; per Option abschaltbar |
| Stretch-Mindestfaktor `1/t_min` | Kurve | 0,8–1,0 | 1,0 | Hebt die Schriftgröße unterhalb der Basisauflösung an (4.2) |

Alle Knobs sind im Theme bzw. in den Projekt-Einstellungen zentral hinterlegt und nicht pro Screen überschreibbar. Änderungen sind mit Review-Eintrag zu dokumentieren.

## 8. Acceptance Criteria

Ein QA-Tester kann folgende Prüfungen automatisiert oder manuell ausführen:

1. **Screen-Vollständigkeit:** Alle 10 Screens und 4 Overlay-Typen aus 3.1 existieren und sind über die in 3.1 angegebenen Wege erreichbar. PASS/FAIL.
2. **Overlay-Ebenen:** Bei geöffnetem `ShopOverlay` über `BoardHUD` und zusätzlich geöffnetem `ConfirmDialog` liegt der Dialog sichtbar über dem Shop; Eingaben erreichen den Screen darunter nicht. PASS/FAIL.
3. **Fokus-Rückkehr:** Nach Schließen eines modalen Overlays liegt der Fokus auf dem Element, das vor dem Öffnen fokussiert war. PASS/FAIL.
4. **Fokus-Reichbarkeit:** Für jeden Screen und jedes Overlay gilt `R_fokus = 1,0` (Formel 4.3), geprüft per automatisiertem Fokus-Durchlauf mit Gamepad. PASS/FAIL.
5. **Fokus-Rahmen:** Der Fokus-Rahmen ist auf jedem Screen bei ausschließlicher Gamepad-Navigation in jedem Zustand sichtbar; er hebt sich mit `C ≥ 3:1` von der Fläche ab (4.6). PASS/FAIL.
6. **Mindestschriftgröße:** Bei 1280×720 und allen Text-Multiplikatoren gilt auf jedem Screen `F_eff ≥ 16 px` (Formel 4.2). PASS/FAIL.
7. **UI-Feedback-Latenz:** Stichprobe von 20 UI-Interaktionen erreicht in 100 % der Fälle `F ≤ 0,2 s` (4.5). PASS/FAIL.
8. **Transitions-Dauer:** Kein Screen-Wechsel dauert länger als 300 ms, keine Overlay-Animation länger als 200 ms (bzw. 150 ms beim Schließen); bei "Reduzierte Bewegung" werden alle auf ≤ 100 ms Fade reduziert. PASS/FAIL.
9. **UI-Sound:** Jeder Button-Klick spielt `ui_click`; jeder Versuch auf einem deaktivierten Button spielt `ui_error` und führt keine Aktion aus. PASS/FAIL.
10. **Eingabe-Nach-Laden-Sperre:** Nach dem LoadingScreen löst eine innerhalb von 150 ms gehaltene Bestätigungstaste keine Aktion aus. PASS/FAIL.
11. **Erlebbar (Experiential):** Eine Testperson ohne Vorkenntnisse identifiziert auf drei zufälligen Screens innerhalb von 2 Sekunden den Fokus und die Hauptaktion. PASS/FAIL.
