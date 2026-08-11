# Board-Architektur — Party Arena Game Bible

> **Teil:** 2 — Board & Fields
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/session-1-analysis.md, design/gdd/game-bible-prompt.md

---

## 1. Overview

Das Kapitel Board-Architektur definiert die grundlegende, spielbare Struktur eines jeden Boards (Insel) in Party Arena. Ein Board besteht aus exakt 40 Feldern, die als Knoten einer neu designten `NodeBoard`-Klasse organisiert sind. Jedes Feld besitzt genau einen Typ aus dem neuen Feldtypen-System, das das Legacy-Enum `NODE_TYPES` (BLUE, RED, GREEN, YELLOW, SHOP, NOLOK, GNU) aus Super Tux Party vollständig ersetzt. Die 40 Felder bilden einen geschlossenen Hauptpfad aus 32 Feldern plus zwei Abzweigungen zu je 4 Feldern (Entscheidungspunkt → Alternativroute → Zusammenführung). Das Kapitel spezifiziert das verbindliche Referenz-Layout, die Feldtypen-Verteilung, die `NodeBoard`-Eigenschaften, das Plugin-Format (`plugin/boards/INSELNAME/`), die 3D-Positionierung (Feldabstand ~3 Einheiten), die Spieler-Stapelung (bis zu 8 Spieler pro Feld), die Kamera-Führung für 16:9 und 21:9 sowie die verbindliche Ablaufreihenfolge von Lande-Effekten und Rundenereignissen. Die Feld-Kapitel 2.2–2.8 bauen direkt auf diesem Kapitel auf.

Geschätzte Spielzeit (Referenz-Board): 8–10 Runden à ca. 5–8 Minuten → 40–80 Minuten pro Partie.

## 2. Player Fantasy

Das Board soll sich anfühlen wie eine lebendige Spielzeug-Diorama-Welt, in der man eine Reise unternimmt. Der Hauptpfad ist eine klar erkennbare Rennstrecke, die sich als geschlossene Schleife um die Insel zieht; Abzweigungen wirken wie einladende Alternativwege mit eigener Persönlichkeit (Belohnung, Risiko, Ereignis). Jedes Feld ist auf einen Blick lesbar — durch Form, Farbe, Icon und Animation (Pfeiler „Sofort verständlich" und „Wiedererkennbar"). Der Spieler soll jederzeit wissen: Wo bin ich, wohin führt der Weg, was passiert, wenn ich hier lande? Die wiederkehrende Struktur (identische Feldtypen-Abstände, identische Abzweigungs-Logik) macht jede neue Insel sofort vertraut, obwohl das Thema wechselt.

## 3. Detailed Rules

### 3.1 Feldtypen-Enum (neues System)

Jedes Feld besitzt genau einen Typ aus dem neuen Enum `FeldTyp`:

| Enum-Wert | Anzeigename | Kurzfunktion | Effekt bei Landung |
|---|---|---|---|
| START | Start | Herkunft und Ziel der Schleife | Lap-Bonus (field-start.md) |
| STERN_SHOP | Sternen-Shop | Stern-Kauf | Stern-Angebot (field-star-shop.md) |
| ITEM_SHOP | Item-Shop | Item-Kauf | Item-Angebot (field-item-shop.md) |
| EREIGNIS | Ereignis | zufälliges Ereignis | Ereignis-Ziehung (field-event.md) |
| GLUECK_PECH | Glück/Pech | Münz-Zufall | Münz-Effekt (field-luck.md) |
| MUENZ_BONUS | Münz-Bonus | garantierter Münz-Gewinn | Münz-Bonus (field-coin-bonus.md) |
| MINISPIEL | Mini-Spiel | setzt Minispiel-Kategorie | Kategorie-Markierung (field-minigame.md) |

Es gibt keine weiteren Feldtypen. Eine Erweiterung des Enums ist eine dokumentierte Design-Entscheidung und erfordert ein eigenes Feld-Kapitel.

### 3.2 Verteilung der Feldtypen (Mengengerüst)

Pro Board (40 Felder) gilt verbindlich:

| Feldtyp | Anzahl | Toleranz |
|---|---|---|
| START | 1 | exakt (Feld 0) |
| STERN_SHOP | 2–3 | pro Board festgelegt |
| ITEM_SHOP | 2 | exakt |
| EREIGNIS | 5–6 | pro Board festgelegt |
| GLUECK_PECH | 3 | exakt |
| MUENZ_BONUS | 4 | exakt |
| MINISPIEL | Rest | 40 − Summe der übrigen |

Die Summe aller Felder ist exakt 40. Formel siehe Sektion 4.

### 3.3 Referenz-Layout (verbindliche Muster-Vorlage)

Jedes Board muss die Struktur des Referenz-Layouts erfüllen: ein Hauptpfad aus 32 Feldern (Indizes 0–31 in Pfadreihenfolge) plus zwei Abzweigungen (A: Indizes 32–35, B: Indizes 36–39). Feld 0 ist immer das Startfeld. Das letzte Hauptpfad-Feld (31) verbindet zurück auf Feld 0 (Schleife).

Topologie (Schema):

```
[0]─[1]─[2]─[3]─[4]─[5]─[6]─[7]─[8]─[9D]──▶[10]─[11]─[12★]─[13M]─[14]─[15]─[16]─[17]─[18]─[19]─[20+]─[21]─[22D]──▶[23]─[24]─[25]─[26M★]─[27]─[28]─[29]─[30]─[31]──▶(zu [0])
                                      │                                                                      │
                                      ▼                                                                      ▼
                                 [32]─[33+]─[34]─[35]                                                      [36]─[37+]─[38]─[39]
                                 Abzweigung A (LD 10–13)                                                    Abzweigung B (LD 23–26)
```

Legende: D = Entscheidungspunkt, M = Zusammenführung, ★ = Sternen-Shop, + = Münz-Bonus. Nicht gekennzeichnete Typen (Ereignis, Glück/Pech, Item-Shop, Mini-Spiel) sind in der Tabelle unten.

Vollständige Referenztabelle (Index, Loop-Distanz LD, Typ, Route, Anmerkung):

| Index | LD | Typ | Route | Anmerkung |
|---|---|---|---|---|
| 0 | 0 | START | Haupt | Startfeld; ArenaStar-Begrüßung |
| 1 | 1 | MINISPIEL | Haupt | LEICHT |
| 2 | 2 | EREIGNIS | Haupt | — |
| 3 | 3 | MUENZ_BONUS | Haupt | Wert 5 |
| 4 | 4 | MINISPIEL | Haupt | LEICHT |
| 5 | 5 | GLUECK_PECH | Haupt | — |
| 6 | 6 | EREIGNIS | Haupt | — |
| 7 | 7 | MINISPIEL | Haupt | LEICHT |
| 8 | 8 | ITEM_SHOP | Haupt | — |
| 9 | 9 | MINISPIEL | Haupt | LEICHT; Entscheidungspunkt A |
| 10 | 10 | MINISPIEL | Haupt (Direktroute A) | LEICHT |
| 11 | 11 | MINISPIEL | Haupt (Direktroute A) | LEICHT |
| 12 | 12 | STERN_SHOP | Haupt (Direktroute A) | Statue #1 |
| 13 | 13 | MINISPIEL | Haupt | LEICHT; Zusammenführung A |
| 14 | 14 | EREIGNIS | Haupt | — |
| 15 | 15 | GLUECK_PECH | Haupt | — |
| 16 | 16 | MINISPIEL | Haupt | MITTEL |
| 17 | 17 | MINISPIEL | Haupt | MITTEL |
| 18 | 18 | EREIGNIS | Haupt | — |
| 19 | 19 | MINISPIEL | Haupt | MITTEL |
| 20 | 20 | MUENZ_BONUS | Haupt | Wert 8 |
| 21 | 21 | MINISPIEL | Haupt | MITTEL |
| 22 | 22 | MINISPIEL | Haupt | MITTEL; Entscheidungspunkt B |
| 23 | 23 | MINISPIEL | Haupt (Direktroute B) | MITTEL |
| 24 | 24 | MINISPIEL | Haupt (Direktroute B) | MITTEL |
| 25 | 25 | EREIGNIS | Haupt | — |
| 26 | 26 | STERN_SHOP | Haupt | Statue #2; Zusammenführung B |
| 27 | 27 | GLUECK_PECH | Haupt | — |
| 28 | 28 | ITEM_SHOP | Haupt | — |
| 29 | 29 | MINISPIEL | Haupt | SCHWER |
| 30 | 30 | MINISPIEL | Haupt | SCHWER |
| 31 | 31 | MINISPIEL | Haupt | SCHWER; letztes Feld vor Start |
| 32 | 10 | MINISPIEL | Abzweigung A1 | LEICHT |
| 33 | 11 | MUENZ_BONUS | Abzweigung A2 | Wert 5 |
| 34 | 12 | MINISPIEL | Abzweigung A3 | LEICHT |
| 35 | 13 | MINISPIEL | Abzweigung A4 | LEICHT |
| 36 | 23 | MINISPIEL | Abzweigung B1 | MITTEL |
| 37 | 24 | MUENZ_BONUS | Abzweigung B2 | Wert 3 |
| 38 | 25 | MINISPIEL | Abzweigung B3 | MITTEL |
| 39 | 26 | MINISPIEL | Abzweigung B4 | MITTEL |

Kontrollsummen: START 1, STERN_SHOP 2, ITEM_SHOP 2, EREIGNIS 5, GLUECK_PECH 3, MUENZ_BONUS 4, MINISPIEL 23 → Summe 40. MINISPIEL-Schwierigkeit: LEICHT 10, MITTEL 10, SCHWER 3.

Abweichungen vom Referenz-Layout sind erlaubt, solange alle Platzierungsregeln (unten) und das Mengengerüst (3.2) erfüllt sind. Alternative, im Konzept genannte Beispielpositionen: 3 Sternen-Shops bei 10, 20, 35; Item-Shops bei 8, 28 (wie im Referenz-Layout).

Platzierungsregeln:
1. Feld 0 ist IMMER START.
2. STERN_SHOP- und ITEM_SHOP-Felder liegen IMMER auf dem Hauptpfad, nie auf Abzweigungen.
3. GLUECK_PECH-Felder: nicht in den ersten 3 Feldern (Indizes 1–3); Abstand entlang des Pfades zueinander ≥ 3 Felder.
4. MUENZ_BONUS-Felder: auf geraden Streckenabschnitten (Hauptpfad-Segmente ohne Abzweigung oder Abzweigungs-Spuren); Abstand zu Entscheidungs-/Zusammenführungspunkten ≥ 2 Felder; nicht benachbart zueinander.
5. EREIGNIS-Felder: nicht vor Index 2; Abstand zueinander entlang des Pfades ≥ 3 Felder.
6. MINISPIEL-Felder füllen alle verbleibenden Positionen, auf Hauptpfad und Abzweigungen.

### 3.4 Abzweigungen

- Jede Abzweigung besteht aus genau einem Entscheidungspunkt (Feld mit 2 Ausgängen), genau 4 Alternativ-Feldern und genau einem Zusammenführungspunkt (Feld, an dem beide Routen wieder zusammenlaufen).
- Der Entscheidungspunkt ist ein normales Feld mit eigenem Feldtyp (Referenz: MINISPIEL). Seine `next`-Verbindungen zeigen auf das erste Direkt-Feld (Hauptpfad) und das erste Abzweig-Feld.
- Der Zusammenführungspunkt ist ein normales Feld mit eigenem Feldtyp (Referenz: MINISPIEL bzw. STERN_SHOP). Seine `prev`-Verbindungen zeigen auf das letzte Direkt-Feld und das letzte Abzweig-Feld.
- Direktroute und Abzweigung dürfen unterschiedlich lang sein. Referenz: Direktroute 4 Schritte, Abzweigung 5 Schritte (die Abzweigung ist ein 1-Schritt-längerer Alternativweg).
- Pfadwahl: Erreicht ein Spieler den Entscheidungspunkt, wählt er beim ersten Schritt frei zwischen den beiden Ausgängen. Es gibt keine Zugweiten-Beschränkung; die Wahl ist immer zulässig, auch wenn die verbleibenden Schritte nicht bis zur Zusammenführung reichen (der Spieler landet dann mitten auf der gewählten Route).
- Abzweigungen dürfen sich nicht überlappen: Kein Feld gehört zu mehr als einer Abzweigung; die Entscheidungs- und Zusammenführungspunkte der beiden Abzweigungen sind paarweise verschieden.

### 3.5 NodeBoard-Klasse

Jedes Feld ist eine Instanz der neu designten Klasse `NodeBoard` (Godot-Node3D; aus STP übernommen und vollständig neu spezifiziert):

| Eigenschaft | Typ | Bedeutung |
|---|---|---|
| index | Ganzzahl (0–39) | Eindeutige Feld-ID; während einer Partie unveränderlich. |
| type | FeldTyp | Der Feldtyp (3.1). |
| next | Liste von Feld-Referenzen (1–2) | Ausgehende Verbindungen in Bewegungsrichtung. |
| prev | Liste von Feld-Referenzen (1–2) | Eingehende Verbindungen. |
| event_handler | Referenz (optional) | Handler für STERN_SHOP, ITEM_SHOP, EREIGNIS; leer bei START, GLUECK_PECH, MUENZ_BONUS, MINISPIEL. |
| visual | Referenz auf 3D-Knoten | Icon/Modell/Partikel des Feldtyps. |
| fixed_value | Ganzzahl | MUENZ_BONUS: Bonus-Wert (3/5/8); STERN_SHOP: optionaler Preis-Override (0 = Standardpreis); sonst 0. |
| position_3d | 3D-Position (x, z; y = 0) | Platzierung auf der Spielebene. |
| ist_sichtbar | Bool | Legacy-Flag `_visible` aus STP; in Party Arena sind alle 40 Felder sichtbar, das Flag bleibt für Kompatibilität. |
| star_spawn | Bool | Legacy `potential_cake` → umbenannt; markiert STERN_SHOP-Felder als Statuen-Position. |

Konsistenzregeln:
- `next` und `prev` sind spiegelbildlich: Zeigt Feld A in `next` von Feld B, so zeigt B in `prev` von A.
- Jedes Feld hat genau einen Hauptpfad-Nachfolger; nur Entscheidungspunkte haben zwei `next`-Einträge.
- Die Verbindungen werden beim Laden aus dem Board-Manifest aufgebaut und beim Laden validiert (3.7).

### 3.6 Migration STP → Party Arena

Das Legacy-Enum `NODE_TYPES` (in `common/scenes/board_logic/node/node.gd`) wird vollständig durch das Feldtypen-System ersetzt. Bestehende Boards und Board-Editoren, die `NODE_TYPES` verwenden, müssen migriert werden.

| STP-Wert | Alte Bedeutung (STP) | Technische Nachfolge | Thematische Nachfolge |
|---|---|---|---|
| BLUE | farbcodiertes Minispiel-Feld (Kategorie 1) | MINISPIEL | entfällt; Kategorie folgt aus Loop-Distanz (field-minigame.md) |
| RED | farbcodiertes Minispiel-Feld (Kategorie 2) | MINISPIEL | Risiko-Aspekte → GLUECK_PECH (field-luck.md) |
| GREEN | farbcodiertes Minispiel-Feld (Kategorie 3) | MINISPIEL | erzählerische Effekte → EREIGNIS (field-event.md) |
| YELLOW | farbcodiertes Minispiel-Feld (Kategorie 4) | MINISPIEL | Glück/Pech-Aspekte → GLUECK_PECH (field-luck.md) |
| SHOP | Item-/Charakter-Shop | ITEM_SHOP (umbenannt) + neuer STERN_SHOP | Kaufhaus-Funktion bleibt; Stern-Kauf wird eigener Typ |
| NOLOK | Stör-/Ereignis-Feld | EREIGNIS | Figur entfernt; Effekte wandern in die Ereignis-Kartei (field-event.md) |
| GNU | Helfer-/Belohnungs-Feld | EREIGNIS / MINISPIEL | Figur entfernt; Belohnungs-Minispiele werden reguläre Minispiele |

Hinweis zur Glossar-Konsistenz: Das Glossar (glossary.md, Legacy-Tabelle) bildet die thematische Nachfolge ab (GREEN → Ereignis-Feld, YELLOW → Glück/Pech-Feld, SHOP → Item-Shop-Feld). Diese Tabelle ergänzt die technische Ebene: Die vier Farbfelder werden zu dem einen Typ MINISPIEL zusammengeführt; die thematischen Funktionen von Rot/Gelb (Risiko) und Grün (Erzählung) leben in GLUECK_PECH bzw. EREIGNIS weiter.

### 3.7 Board als Plugin

Jedes Board ist ein Plugin im STP-Format unter `plugin/boards/INSELNAME/`. Der STP-Plugin-Loader wird wiederverwendet; der Board-Loader wird auf die neuen Feldtypen erweitert.

| Pfad (relativ zu `plugin/boards/INSELNAME/`) | Inhalt |
|---|---|
| `board.tscn` | Szene: 40 NodeBoard-Knoten, Visuals, Kamera-Anker. |
| `board.gd` | Board-Logik: Felder registrieren, next/prev aufbauen, Validierung, Rundenende-Wartung. |
| `manifest.json` | Maschinenlesbare Board-Definition (Schema unten). |
| `visuals/` | Feld-Modelle, Icons, Materialien, Partikel, Feldtyp-Sprites. |
| `handlers/` | optionale, inselspezifische Event-Handler (z. B. eigene EREIGNIS-Inhalte). |
| `audio/` | optionale Insel-Musik und Ambience. |

Manifest-Schema (Pflichtfelder):
- `board_id` (eindeutig, kebab-case), `display_name`, `theme`, `description`.
- `player_min = 2`, `player_max = 8`.
- `fields`: exakt 40 Einträge mit `{ index, type, x, z, next (Indizes), prev (Indizes), fixed_value }`.
- `star_shop_order`: Liste der STERN_SHOP-Indizes in Pfadreihenfolge (für die Statuen-Wanderung, field-star-shop.md).
- `coin_bonus_values`: Zuordnung MUENZ_BONUS-Index → Wert (3/5/8).
- `minigame_tiers`: optionale Abweichung der Bandgrenzen (Standard: 1–13 / 14–26 / 27–39).

Lade-/Validierungsfehler (Board wird abgelehnt, Partie startet nicht): Indizes nicht 0–39, fehlende/doppelte Indizes, Startfeld ≠ 0, Mengengerüst verletzt (3.2), Verbindungen nicht spiegelbildlich, Feld nicht vom Start erreichbar, Abzweigungs-Struktur verletzt.

### 3.8 3D-Positionierung

- Alle Felder liegen auf einer Ebene (XZ-Ebene, y = 0).
- Benachbarte Felder werden entlang des Pfades mit einem Abstand d = 3,0 Einheiten positioniert (Toleranz 2,5–3,5 Einheiten, euklidisch).
- Abzweigungen verlaufen parallel zur Direktroute mit einem lateralen Versatz von 3,0 Einheiten; die Verbindung vom letzten Abzweig-Feld zur Zusammenführung ist eine kurze Kurve (3,0 ± 0,5 Einheiten).
- Empfohlene Gesamtausdehnung des Referenz-Layouts: ca. 30 × 22 Einheiten (Bounding-Box).

### 3.9 Spieler-Positionierung auf einem Feld

Bis zu 8 Spieler können sich gleichzeitig auf demselben Feld befinden. Sie werden deterministisch nach Sitzplatzindex s (0-basiert) versetzt. Es gibt keine Kollision, keine Blockierung und keine Interaktion zwischen Spielern auf demselben Feld.

| Anzahl n | Positionen (relativ zur Feldmitte, Einheiten) |
|---|---|
| 1 | (0, 0) |
| 2 | (0, −0.45), (0, +0.45) |
| 3 | Radius 0.60, Winkel 90°, 210°, 330° |
| 4 | Radius 0.60, Winkel 45°, 135°, 225°, 315° |
| 5–8 | Radius 0.60, Winkel θ_s = s·(360°/n) − 90°, Koordinaten (0.60·cos θ_s, 0.60·sin θ_s) |

Der Spieler mit Sitzplatz s belegt Slot s (mod n). Bei n = 1–4 gelten die festen Positionen, bei n = 5–8 die volle Kreisformel; beide Schemata sind deterministisch und kollisionsfrei innerhalb des Feldradius (Feldradius ≈ 1,2 Einheiten).

### 3.10 Kamera und Bildformate

- Die Kamera folgt dem aktuell ziehenden Spieler entlang des Hauptpfades (weiche Interpolation; keine harten Schnitte während einer Bewegung).
- Vertikale Halbausdehnung des Sichtfeldes: konstant V = 14 Einheiten. Horizontale Halbausdehnung: H = A · V mit Seitenverhältnis A.
  - 16:9 (A ≈ 1,78): H ≈ 24,9 Einheiten.
  - 21:9 (A ≈ 2,33): H ≈ 32,7 Einheiten.
- Framing-Anforderung: Zu jedem Zeitpunkt müssen das aktuelle Spielerfeld, die nächsten 3 Felder und die vorherigen 2 Felder im 16:9-Bild liegen. Mindestbedarf ≈ 5 Felder × 3 Einheiten = 15 Einheiten plus Abzweigungs-Versatz ≤ 6 Einheiten → gedeckt durch H ≈ 24,9. 21:9 zeigt horizontal eine Obermenge.
- Die gesamte Board-Ausdehnung muss in der vertikalen Richtung der Kamera innerhalb von ±V bleiben (Referenz-Bounding-Box 30 × 22 → Halbhöhe 11 < 14).
- HUD-Safe-Areas: Die Framing-Anforderung gilt für den sichtbaren Bereich ohne HUD-Überdeckung.

### 3.11 Landen vs. Überqueren

- Überqueren: Ein Feld, das ein Spieler als Zwischenschritt eines Würfelzugs durchschreitet, löst keinen Feld-Effekt aus. Ausnahme: Das Startfeld gewährt den Lap-Bonus auch beim Überqueren (field-start.md).
- Landen: Ein Feld, das ein Spieler als letztes Feld seines Würfelzugs erreicht, löst seinen Lande-Effekt aus (feldtyp-spezifisch).
- Platzierung durch Effekte (Teleporter, Ereignisse wie Tausch-Basar, Rückruf, Rückwärtsbewegung): löst grundsätzlich KEINE Feld-Effekte aus (kein Lap-Bonus, keine Läden, keine Ereignisse, kein Glück/Pech, keine Minispiel-Markierung). Einzige Ausnahme: MUENZ_BONUS gewährt bei Effekt-Platzierung den halben Bonus (field-coin-bonus.md).
- Auflösungsreihenfolge bei einer Landung: (1) Lande-Effekt des Feldtyps, (2) Münz-Pickup einsammeln (falls vorhanden), (3) Minispiel-Markierung (nur MINISPIEL-Felder; in der Game Bible ohne Wirkung, da alle Spieler teilnehmen).

### 3.12 Rundenablauf

1. Rundenbeginn: Rundenzähler erhöhen; ggf. Hinweis anzeigen.
2. Spielerzüge: Jeder Spieler in Sitzreihenfolge (0..N−1) macht genau einen Zug:
   a. Optionale Item-Nutzung vor dem Würfeln (item-system.md).
   b. Würfeln (Würfelwert w; Modifikatoren beachten, z. B. Würfel-Verdoppler).
   c. Bewegung: w Schritte; an Entscheidungspunkten freie Pfadwahl; beim Überqueren/Erreichen des Startfeldes Lap-Bonus.
   d. Landung: Lande-Effekt auflösen (3.11).
3. Nach dem letzten Spielerzug: Minispiel-Runde — alle Spieler nehmen teil; Kategorie gemäß field-minigame.md.
4. Rundenende-Wartung (in dieser Reihenfolge):
   a. Münz-Pickups (Münzsturm) entfernen.
   b. Sternen-Shops auffüllen (jeder leere Shop erhält 1 Stern).
   c. Item-Shops: neue Angebote generieren.
   d. Feld-Besuchszähler (MUENZ_BONUS) zurücksetzen.
   e. Ereignis-Modifikatoren zurücksetzen (Stern-Preis-Mod; Würfel-Verdoppler verfällt nicht automatisch, sondern wird durch den nächsten Würfelwurf konsumiert).
5. Falls die letzte Runde beendet ist: Siegerehrung (victory-conditions.md).

### 3.13 Spielzeit

Referenz-Board: 8–10 Runden à ca. 5–8 Minuten (abhängig von Spielerzahl und Minispiel-Länge) → 40–80 Minuten pro Partie.

## 4. Formulas

Variablendefinitionen:
- `N_total = 40` — Gesamtzahl der Felder (fix).
- `N_main = 32`, `N_branchA = 4`, `N_branchB = 4` — Hauptpfad und Abzweigungen.
- `N_STERN_SHOP ∈ {2, 3}`, `N_EREIGNIS ∈ {5, 6}`, `N_ITEM_SHOP = 2`, `N_GLUECK_PECH = 3`, `N_MUENZ_BONUS = 4`, `N_START = 1`.

Feldtyp-Summenformel:
- `N_fixed = N_START + N_STERN_SHOP + N_ITEM_SHOP + N_EREIGNIS + N_GLUECK_PECH + N_MUENZ_BONUS`
- `N_MINISPIEL = N_total − N_fixed = 30 − N_STERN_SHOP − N_EREIGNIS`

Erwartungswerte:
- `N_MINISPIEL ∈ {21, 22, 23}` für alle zulässigen Kombinationen (2/3 × 5/6).
- Referenz (N_STERN_SHOP = 2, N_EREIGNIS = 5): `N_MINISPIEL = 40 − (1+2+2+5+3+4) = 40 − 17 = 23`.

Beispielrechnung (Referenz):
- Kontrolle: `1 + 2 + 2 + 5 + 3 + 4 + 23 = 40`.

Weitere Formeln:
- Loop-Distanz `LD(f)`: Anzahl der Schritte vom Startfeld zum Feld f auf dem kürzesten Pfad. Hauptpfad-Feld Mi → `LD = i`. Abzweigungs-Feld Ak (k = 1..4) → `LD = LD(Entscheidungspunkt) + k`.
- Schwierigkeits-Band (MINISPIEL): LEICHT = LD 1–13, MITTEL = LD 14–26, SCHWER = LD 27–39.
- Feldabstand: `d = 3,0` Einheiten (Toleranz 2,5–3,5).
- Kamera: `V = 14`; `H = A · V`; `A ∈ {16/9, 21/9}`.
- Spieler-Offset: Tabelle in 3.9.

## 5. Edge Cases

1. **Verbindungs-Inkonsistenz:** `next`/`prev` nicht spiegelbildlich → Board-Validierung schlägt fehl, Partie startet nicht; Fehlermeldung nennt die betroffenen Feld-Indizes.
2. **Feld 0 nicht START:** Validierungsfehler (Blocker).
3. **Doppelte oder fehlende Indizes:** Validierungsfehler (Blocker).
4. **Zwei Entscheidungspunkte in einer Abzweigung:** Verboten; genau 1 Entscheidungs- und 1 Zusammenführungspunkt pro Abzweigung.
5. **Überlappende Abzweigungen:** Verboten; kein Feld gehört zu zwei Abzweigungen.
6. **Mehrere Spieler auf demselben Feld:** Versatz nach 3.9; bei 8 Spielern volle Kreisformel.
7. **Kamera bei Effekt-Platzierung (z. B. Rückruf):** Die Kamera springt weich zum neuen Spielerfeld, sobald alle Platzierungen aufgelöst sind; dieselbe Framing-Anforderung gilt.
8. **21:9-Bildschirm:** Horizontale Obermenge; V bleibt unverändert, sodass keine Board-Inhalte aus dem Bild fallen.
9. **Board mit 3 Sternen-Shops:** Mengengerüst bleibt gültig (N_STERN_SHOP = 3); N_MINISPIEL sinkt entsprechend (z. B. 22 bei N_EREIGNIS = 5).
10. **Schleife nicht geschlossen:** `M31.next` MUSS auf Feld 0 zeigen; sonst Validierungsfehler.

## 6. Dependencies

### 6.1 Benötigt von `board-architecture.md`

| Kapitel/System | Art | Verwendung |
|---|---|---|
| `field-start.md` | abhängig | Definiert Verhalten des START-Feldes (Index 0) und des Lap-Bonus. |
| `field-star-shop.md` | abhängig | Definiert Verhalten der STERN_SHOP-Felder und Statuen-Wanderung. |
| `field-item-shop.md` | abhängig | Definiert Verhalten der ITEM_SHOP-Felder. |
| `field-event.md` | abhängig | Definiert EREIGNIS-Felder und Ereignis-Kartei. |
| `field-luck.md` | abhängig | Definiert GLUECK_PECH-Felder. |
| `field-coin-bonus.md` | abhängig | Definiert MUENZ_BONUS-Felder (inkl. Effekt-Platzierungs-Ausnahme). |
| `field-minigame.md` | abhängig | Definiert MINISPIEL-Felder, Kategorie-Auflösung am Rundenende. |
| `core-loop.md` (geplant) | Quelle | Runden- und Zugstruktur, auf der 3.12 aufbaut. |
| `dice-movement.md` (geplant) | Quelle | Würfeln, Schrittzählung, Pfadwahl (3.12.2). |
| `technical-fork-strategy.md` (geplant) | Quelle | Migration der NodeBoard/NODE_TYPES aus dem STP-Fork. |
| Board-Loader / Plugin-Loader | System | Lädt und validiert `plugin/boards/INSELNAME/`. |
| Kamera-System | System | Framing gemäß 3.10. |
| Spieler-/Sitzplatz-System | System | Versatz-Schema gemäß 3.9. |

### 6.2 Systeme, die von diesem Dokument abhängen

| Kapitel/System | Art der Abhängigkeit |
|---|---|
| Alle Feld-Kapitel (2.2–2.8) | Setzen die `NodeBoard`-Eigenschaften, das Referenz-Layout und die Lande-Regeln (3.11) voraus. |
| `coin-economy.md` (geplant) | Nutzt die Feldtypen-Verteilung als Faucet/Sink-Quelle. |
| `star-economy.md` (geplant) | Nutzt `star_shop_order` und STERN_SHOP-Positionen. |
| `ui-board.md` (geplant) | Nutzt Feldtypen-Icons und Pfadwahl-Darstellung. |
| Board-Editoren / CI-Validierung | Prüfen das Manifest-Schema und das Mengengerüst (3.2). |

### 6.3 Bidirektionalität

Jedes Feld-Kapitel muss in seinen Dependencies auf `board-architecture.md` verweisen (Rückverweis). Die Verpflichtung ist wechselseitig (Regel des bible-index.md, Sektion 6.3).

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|---|---|---|---|---|
| Feldabstand `d` | Kurve | 2,5–3,5 Einheiten | 3,0 | Raumgefühl, Kameraframing, Board-Dichte. |
| Anzahl Sternen-Shops `N_STERN_SHOP` | Kurve | 2–3 | 2 | Stern-Verfügbarkeit pro Runde, Partietempo. |
| Anzahl Ereignis-Felder `N_EREIGNIS` | Kurve | 5–6 | 5 | Ereignis-Dichte, Chaos-Level. |
| Bandgrenzen Minispiel-Tier | Kurve | frei wählbar | 1–13 / 14–26 / 27–39 | Schwierigkeits-Progression der Minispiele. |
| Kamera-Vertikalhalbausdehnung `V` | Kurve | 10–18 Einheiten | 14 | Sichtweite, Framing-Sicherheit. |
| Spieler-Offset-Radius | Kurve | 0,4–0,9 Einheiten | 0,60 | Lesbarkeit bei 8 Spielern auf einem Feld. |
| Spielzeit pro Runde | Feel | 4–10 Minuten | 5–8 | Partielänge (40–80 Min.). |
| Abzweigungslänge | Kurve | 3–5 Felder | 4 | Risiko/Reward der Alternativroute. |

## 8. Acceptance Criteria

Ein QA-Tester (oder CI-Hook) kann die folgenden Prüfungen automatisiert ausführen:

1. **Ladetest:** Jedes Board-Plugin unter `plugin/boards/INSELNAME/` lädt; Validierung besteht (40 Felder, Indizes 0–39 eindeutig, Startfeld = 0). PASS/FAIL.
2. **Mengengerüst:** Die Summe der Feldtypen je Board ist exakt 40; STERN_SHOP ∈ {2,3}, ITEM_SHOP = 2, EREIGNIS ∈ {5,6}, GLUECK_PECH = 3, MUENZ_BONUS = 4, MINISPIEL = 40 − N_fixed. PASS/FAIL.
3. **Struktur:** Hauptpfad = 32 Felder, Abzweigungen A und B = je 4 Felder; jeder Entscheidungspunkt hat genau 2 `next`-Einträge; jede Zusammenführung genau 2 `prev`-Einträge (außer Start, der 1 prev hat). PASS/FAIL.
4. **Erreichbarkeit:** Jedes Feld ist vom Startfeld aus erreichbar; `M31.next` zeigt auf Feld 0; `next`/`prev` sind spiegelbildlich. PASS/FAIL.
5. **Abstand:** Alle benachbarten Feldpaare haben euklidische Distanz 3,0 ± 0,5 Einheiten. PASS/FAIL.
6. **Spieler-Stapelung:** 8 Spieler auf einem Feld → alle Positionen liegen innerhalb von 0,9 Einheiten um die Feldmitte und sind paarweise ≥ 0,3 Einheiten voneinander entfernt. PASS/FAIL.
7. **Kamera 16:9:** Während einer Testbewegung sind jederzeit das aktive Feld, 3 Felder voraus und 2 Felder rückwärts im Bild (ohne HUD-Überdeckung). PASS/FAIL.
8. **Kamera 21:9:** Derselbe Test bei 21:9 zeigt eine horizontale Obermenge des 16:9-Bildes; nichts fällt vertikal aus dem Bild. PASS/FAIL.
9. **Migration:** Kein neues Board verwendet `NODE_TYPES`; alle 40 Felder nutzen das neue `FeldTyp`-System. PASS/FAIL.
10. **Referenz-Layout:** Das Referenz-Board erfüllt die Tabelle in 3.3 inklusive Kontrollsummen (1/2/2/5/3/4/23). PASS/FAIL.
