# Technische Datenstrukturen und Speicherformate — Party Arena

> **Status:** Proposed
> **Version:** 2.0.0
> **Letzte Anderung:** 2026-08-11
> **Abhangigkeiten:** technical-architecture.md, technical-multiplayer.md

---

## 1. Overview

Dieses Dokument definiert samtliche Datenstrukturen, Speicherformate und Netzwerk-Nachrichtenformate, die in Party Arena verwendet werden. Es dient als zentrale Referenz fur alle Entwickler — jede neue Komponente, die Daten speichert oder ubertragt, MUSS ihre Strukturen hier dokumentieren.

### Datenfluss-Ubersicht

```
┌──────────────────────────────────────────────────────────────┐
│                     SERVER (Autoritativ)                      │
│                                                               │
│  ┌─────────────────┐  ┌──────────────┐  ┌─────────────────┐ │
│  │  Spieler-Daten   │  │  Board-Daten  │  │  Minispiel-Daten │ │
│  │  (PlayerData)    │  │  (BoardData)  │  │  (MinigameMeta)  │ │
│  └────────┬────────┘  └──────┬───────┘  └────────┬────────┘ │
│           │                  │                    │           │
│  ┌────────▼──────────────────▼────────────────────▼────────┐ │
│  │              Server Game State (Dictionary)             │ │
│  │  - players: Array von PlayerData (1–8 Eintrage)        │ │
│  │  - board: BoardData                                     │ │
│  │  - current_turn: int                                    │ │
│  │  - current_player_index: int                            │ │
│  │  - phase: String                                        │ │
│  └────────┬───────────────────────────────────────────────┘ │
│           │ RPC: _rpc_sync_game_state (ServerUpdate)        │
│           │ (als JSON-kompatibles Dictionary)               │
└───────────┼──────────────────────────────────────────────────┘
            │  ENet UDP (Port 10567)
    ┌───────┼───────────┬───────────┬───────────┐
    │       │           │           │           │
┌───▼───┐ ┌─▼───┐ ┌─────▼─┐ ┌─────▼─┐ ┌─────▼─┐
│Client 1│ │Cli.2│ │Cli. 3 │ │  ...  │ │Cli. 8 │
│Lokaler │ │     │ │       │ │       │ │       │
│State   │ │     │ │       │ │       │ │       │
│(Read-  │ │     │ │       │ │       │ │       │
│Only)   │ │     │ │       │ │       │ │       │
└────────┘ └─────┘ └───────┘ └───────┘ └───────┘
```

### Kernprinzipien

1. **Server = Autoritativ:** Alle Datenstrukturen werden auf dem Server erstellt, validiert und gespeichert. Clients erhalten nur Read-Only-Kopien.
2. **Dictionary-basiert:** Alle Daten werden als Godot-Dictionaries gespeichert und ubertragen (RPC-kompatibel). Keine benutzerdefinierten Godot-Objekte im Netzwerk.
3. **Flache Strukturen:** Keine tief verschachtelten Dictionaries (maximal 3 Ebenen). Bei Bedarf in separate Dictionaries aufteilen.
4. **Typisiert:** Jedes Feld hat einen definierten Typ (int, float, String, bool, Array, Dictionary). Keine untypisierten Felder in der Spezifikation.
5. **Validierbar:** Jede Struktur hat definierte Wertebereiche und Validierungsregeln — einfach in Unit-Tests zu prufen.
6. **Extensibel:** Neue Felder konnen hinzugefugt werden, ohne alte zu brechen (vorwarts-kompatibel). Client ignoriert unbekannte Felder.

---

## 2. Player Fantasy

Der Spieler interagiert nie direkt mit diesen Datenstrukturen — aber er spurt ihre Qualitat.

### Was der Spieler merkt

- **Konsistente Darstellung:** Das HUD zeigt immer korrekte Werte (Munzen, Sterne, Position). Keine Desyncs zwischen dem, was der Spieler sieht, und dem tatsachlichen Server-Zustand.
- **Keine verlorenen Daten:** Wenn ein Spieler das Spiel speichert und spater ladt, sind alle Werte exakt so, wie sie waren. Keine veranderten Munzstande, keine verschwundenen Items.
- **Schnelle Ladezeiten:** Speicher-Dateien sind kompakt (unter 10 KB), Spiele laden in unter 1 Sekunde.
- **Faire Validierung:** Wenn der Client versucht zu schummeln (Munzen manipulieren, Items duplizieren), wird die Aktion vom Server abgelehnt. Der Spieler merkt nichts davon — seine illegale Aktion schlagt einfach still fehl.

### Was der Entwickler merkt

- **Klare Schemas:** Jede Datenstruktur ist hier dokumentiert. Kein Raten, welche Felder ein Dictionary hat.
- **RPC-Kompatibilitat:** Alle Strukturen sind sofort netzwerk-tauglich (nur primitive Typen: int, float, String, bool, Array, Dictionary, Vector2, Vector3).
- **Validierbarkeit:** Jede Struktur hat definierte Wertebereiche — einfach in Unit-Tests zu validieren.
- **Serialisierbarkeit:** Alle Strukturen konnen mit Godot-Bordmitteln serialisiert werden (`var_to_bytes`, ConfigFile, JSON).

---

## 3. Detailed Rules

### 3.1 Spieler-Daten (PlayerData)

Die zentrale Datenstruktur fur einen einzelnen Spieler. Wird vom Server verwaltet und als Teil des Game-State an Clients gesendet. Pro Spiel existieren 8 PlayerData-Instanzen (eine pro Spieler, auch fur nicht verbundene Slots).

#### Vollstandiges Schema

```
Dictionary PlayerData {
    "id": int
        Spieler-ID (1–8). Eindeutig innerhalb einer Spiel-Session.
        Wird beim Lobby-Join zugewiesen. Andert sich wahrend des
        Spiels NICHT. ID 1 ist typischerweise der Host.

    "name": String
        Spieler-Name. Maximale Lange: 16 Zeichen.
        Erlaubte Zeichen: Buchstaben (Unicode), Ziffern, Leerzeichen,
        Bindestrich, Unterstrich. Keine HTML/BBcode-Tags.
        Default: "Spieler N" (N = id).
        Wird vor der Anzeige sanitized (Tags entfernt, getrimmt).

    "character_id": String
        Charakter-ID (Plugin-Name des Arenian).
        Mogliche Werte: "brix", "nixie", "koko", "pip", "zara",
        "flint", "luna", "momo".
        Default: Leerstring "" (bis zur Auswahl in der Lobby).
        Server pruft: Charakter existiert als Plugin und ist nicht
        bereits von anderem Spieler gewahlt (First-Come-First-Served).

    "coins": int
        Aktuelle Munz-Anzahl. Wertebereich: 0–99 (Hard-Cap).
        Startwert: START_COINS = 10.
        Minimum: 0 (niemals negativ — Transaktionen werden
        abgelehnt, wenn sie coins < 0 ergeben wurden).
        Maximum: 99 (alle weiteren Einnahmen verfallen).
        UI-Display: Zeigt Werte bis 999 an (Visuelles Cap,
        Hard-Cap bleibt 99).

    "stars": int
        Aktuelle Stern-Anzahl. Wertebereich: 0–99 (Hard-Cap).
        Startwert: 0.
        Erhoht durch: Stern-Kauf (20 Munzen), Bonus-Sterne
        (am Spielende, +1 pro gewonnener Kategorie).
        Kein anderer Weg, Sterne zu erhalten.
        Sterne konnen NICHT verloren oder gestohlen werden
        (Anti-Regel: "Stern-Diebstahl existiert nicht").
        Ausnahme: Keine. Sterne sind unantastbar.

    "field_index": int
        Aktuelle Position auf dem Board. Wertebereich: 0–39.
        0 = Startfeld. 39 = letztes Feld.
        Wird bei Bewegung aktualisiert (field_index + dice_value,
        modulo BOARD_FIELDS bei Umlauf-Uberschreitung).
        Bei Teleporter-Nutzung: Direktes Setzen durch Server.

    "items": Array[String]
        Item-IDs im Inventar. Maximale Lange: 3 (MAX_ITEMS).
        Mogliche Werte: "glueckswuerfel", "schutzschild",
        "muenzmagnet", "teleporter", "diebhandschuh".
        Leeres Array = keine Items.
        Reihenfolge: Chronologisch nach Kauf-Zeitpunkt.
        Wenn Array voll (size == 3) und Spieler will Item kaufen:
        Kauf wird abgelehnt. Spieler muss zuerst Item verwenden.

    "shield_active": bool
        Schutzschild-Status.
        true = Schutzschild aktiv. Blockt den nachsten negativen
        Event-Effekt oder Item-Diebstahl.
        false = Kein Schutz.
        Wird automatisch auf false gesetzt, sobald ein negativer
        Effekt geblockt wurde (einmaliger Schutz).
        Wird durch Item "schutzschild" auf true gesetzt.
        Wird bei Runden-Beginn NICHT zuruckgesetzt (bleibt uber
        Runden hinweg aktiv, bis verbraucht).

    "coin_magnet_turns": int
        Verbleibende Zuge des Munz-Magneten. Wertebereich: 0–3.
        0 = Kein Magnet aktiv.
        1–3 = Verbleibende Zuge (COIN_MAGNET_DURATION = 3).
        Wird zu Beginn jedes eigenen Zuges um 1 dekrementiert.
        Wahrend aktiv: Jedes betretene Feld gibt +2 zusatzliche
        Munzen (auf COIN_BONUS-Felder additiv, also z.B.
        5 + 2 = 7 Munzen).
        Wird bei Runden-Beginn NICHT zuruckgesetzt.

    "laps_completed": int
        Anzahl vollstandiger Umlaufe (Startfeld-Uberquerungen).
        Wertebereich: 0–99.
        Startwert: 0.
        Wird erhoht, wenn der Spieler das Startfeld (Index 0)
        uberquert (nicht: darauf landet). Uberquerung = Bewegung
        von Feld 39 zu Feld 0+.
        Relevanz: Viellaufer-Bonus-Stern-Kategorie, Statistik.

    "minigames_won": int
        Anzahl gewonnener Minispiele (1. Platz).
        Wertebereich: 0–MAX_TURNS (maximal 10).
        Wird nach jedem Minispiel aktualisiert.
        Relevanz: Minispiel-Meister-Bonus-Stern-Kategorie,
        Tiebreaker (3. Kriterium nach Sternen → Munzen →
        Minispiel-Siegen).

    "items_used": int
        Anzahl verwendeter Items uber das gesamte Spiel.
        Wertebereich: 0–99.
        Relevanz: Statistik, eventuell Bonus-Kategorie.

    "events_triggered": int
        Anzahl ausgeloster Ereignis-Felder uber das gesamte Spiel.
        Wertebereich: 0–99.
        Relevanz: Ereignis-Held-Bonus-Stern-Kategorie.

    "total_fields_traveled": int
        Summe aller gereisten Felder uber das gesamte Spiel.
        Wertebereich: 0–999.
        Wird nach jeder Bewegung um dice_value erhoht.
        Relevanz: Viellaufer-Bonus-Stern-Kategorie.

    "is_connected": bool
        Verbindungsstatus.
        true = Spieler ist verbunden und spielt aktiv.
        false = Spieler ist disconnected. KI ubernehmen.
        Wird NUR vom Server auf false gesetzt (bei Disconnect).
        Bei Reconnect (optional, Post-Launch): Wieder auf true.

    "is_ai": bool
        KI-Status.
        true = Dieser Slot wird von der KI gesteuert (entweder
        weil Spieler disconnected ist oder weil es ein reiner
        KI-Slot ist, z.B. zum Auffullen bei < 8 menschlichen
        Spielern im Online-Modus).
        false = Menschlicher Spieler.

    "color": String
        Spieler-Farbe als Hex-String (z.B. "#ff3333").
        P1: "#ff3333" (Rot)
        P2: "#3366ff" (Blau)
        P3: "#33ff66" (Grun)
        P4: "#ffe633" (Gelb)
        P5: "#ff8c33" (Orange)
        P6: "#b333ff" (Lila)
        P7: "#33ffee" (Cyan)
        P8: "#ff33a8" (Pink)
        Wird im HUD, auf Namensschildern und in der Siegerehrung
        verwendet. Ubertragen als String (nicht als Godot-Color-
        Objekt — RPC-kompatibel).

    "controller_id": int
        Gamepad-ID. Wertebereich: -1 bis 7.
        -1 = Tastatur (nur P1 und P2).
        0–7 = Gamepad-Index.
        Verwendet fur Splitscreen-Zuordnung und Input-Isolation.
}
```

#### Validierungsregeln (Server-seitig, vor jeder State-Anderung)

Jedes PlayerData-Dictionary wird vor der Annahme durch den Server validiert. Die Validierung pruft:

- `id` muss im Bereich 1–8 liegen.
- `name` darf nicht leer sein und maximal 16 Zeichen lang sein (nach Trimming).
- `name` darf keine HTML/BBcode-Tags enthalten (Regex: `<[^>]*>` muss leer sein).
- `character_id` muss in der Liste der 8 Arenian-Plugin-IDs sein ODER leer sein (vor Lobby-Auswahl).
- `coins` muss im Bereich 0–99 liegen.
- `stars` muss im Bereich 0–99 liegen.
- `field_index` muss im Bereich 0–39 liegen.
- `items` darf maximal 3 Eintrage haben.
- `items` Eintrage mussen in der Liste der 5 Item-IDs sein.
- `coin_magnet_turns` muss im Bereich 0–3 liegen.
- `laps_completed` darf nicht negativ sein.
- `color` muss ein gultiger Hex-Color-String sein (Regex: `#[0-9a-fA-F]{6}`).
- `controller_id` muss im Bereich -1 bis 7 liegen.

**Fehlerbehandlung:** Schlagt eine Validierung fehl, wird der State-Update verworfen, eine Warnung geloggt (`push_warning`) und der Server sendet ein Full-State-Update an den betroffenen Client, um mogliche Desyncs zu beheben.

### 3.2 Board-Daten (BoardData)

Die zentrale Datenstruktur fur das aktuelle Spiel-Board. Wird einmalig bei Spielstart vom Server aus dem Board-Plugin geladen und bei State-Anderungen aktualisiert. Ein BoardData-Dictionary existiert genau 1× pro Spiel.

#### Vollstandiges Schema

```
Dictionary BoardData {
    "board_id": String
        Board-Plugin-ID (Ordnername in plugins/boards/).
        Mogliche Werte: "sonnenstrand", "korallenriff",
        "vulkaninsel", "nebelwald", "kristallhoehle",
        "wolkenreich", "zeitgarten", "schattenarchipel".

    "board_name": String
        Anzeigename des Boards (lokalisiert).
        Beispiele: "Sonnenstrand", "Korallenriff".

    "fields": Array[FieldData]
        Array von exakt 40 FieldData-Dictionaries (Index 0–39).
        Index im Array = Feld-Index auf dem Board.
        Jedes Element ist ein FieldData Dictionary (siehe 3.3).

    "star_shop_positions": Array[int]
        Indizes der Sternen-Shop-Felder. Lange: 1–3.
        Dies sind die Felder, zwischen denen die Sternen-Statue
        wandern kann. Standard: [12, 24, 36] (gleichmassig
        verteilt auf dem 40-Felder-Board).
        Die aktive Position ist NICHT hier, sondern in
        active_star_shop_index.

    "item_shop_positions": Array[int]
        Indizes der Item-Shop-Felder. Lange: 1–4.
        Fixe Positionen — Item-Shops wandern nicht.
        Standard: [8, 28] (2 Shops pro Board, gleichmassig
        verteilt).

    "active_star_shop_index": int
        Index des aktuell aktiven Sternen-Shop-Feldes.
        Einer der Werte aus star_shop_positions.
        Initial: star_shop_positions[0] (oder zufallig gewahlt
        aus dem Array bei Spielbeginn).
        Andert sich bei Stern-Wanderung (nach jedem Kauf).

    "star_available": bool
        Ist der Stern im aktuellen Shop verfugbar?
        true = Stern kann gekauft werden (Statue leuchtet).
        false = Stern wurde bereits gekauft (Statue grau).
        Wird NUR true, wenn der Stern zu einer neuen Position
        wandert (nach erfolgreichem Kauf).
        Wird false, sobald der Stern an der aktuellen Position
        gekauft wurde.

    "current_turn": int
        Aktuelle Runde. Wertebereich: 1–MAX_TURNS (10).
        1 = Erste Runde.
        10 = Letzte Runde.
        Wird nach dem Zug des letzten Spielers (vor der
        Minispiel-Phase) erhoht.
        Wenn current_turn > MAX_TURNS → Spielende (Bonus-Sterne).

    "current_round": int
        Alias fur current_turn (identischer Wert).
        Existiert fur semantische Klarheit ("Runde" = mehrere
        Zuge + Minispiel + Stern-Phase).
        Wird synchron mit current_turn aktualisiert.

    "current_player_index": int
        Spieler-ID des aktuell aktiven Spielers. Wertebereich: 1–8.
        Rotiert nach jedem Zug: 1→2→...→8→1→...
        Die Zug-Reihenfolge wird in der Vorrunde einmalig
        festgelegt und bleibt fur die gesamte Partie bestehen.

    "phase": String
        Aktuelle Spiel-Phase.
        Mogliche Werte:
        "ROLL"        — Spieler wurfelt
        "MOVE"        — Figur bewegt sich
        "EVENT"       — Feld-Ereignis wird ausgefuhrt
        "SHOP"        — Spieler kann kaufen (Stern/Item)
        "MINIGAME"    — Minispiel wird gespielt
        "STAR"        — Stern-Kaue, Stern-Wanderung
        "BONUS_STARS" — Bonus-Sterne werden berechnet
        "VICTORY"     — Sieger-Zeremonie
        Initial: "ROLL".

    "item_shop_offers": Array[Array[String]]
        Item-Angebote pro Shop. Ausseres Array: ein Eintrag
        pro Item-Shop (typisch 2). Inneres Array: 3 Item-IDs
        (die im Shop angebotenen Items).
        Wird zu Spielbeginn zufallig generiert (pro Shop
        3 aus den 5 verfugbaren Items ziehen).
        Wird wahrend des Spiels NICHT verandert (fixes Angebot).

    "bonus_star_categories": Array[String]
        Die 3 fur dieses Spiel gezogenen Bonus-Stern-Kategorien.
        Wird zu Spielbeginn zufallig aus dem 10er-Pool gezogen.
        Wird den Spielern erst am Spielende offenbart
        (Uberraschungs-Moment).
        Leeres Array vor Spielende (wird bei BONUS_STARS-Phase
        gefullt und an Clients gesendet).

    "event_history": Array[String]
        Chronologische Liste aller bereits ausgelosten Events
        (Event-IDs). Maximal 100 Eintrage (bei 8 Spielern ×
        10 Runden × ~2 Events pro Runde < 160; altere Eintrage
        werden verworfen).
        Verwendet fur die "kein 2× hintereinander"-Regel:
        Letztes Element wird mit nachstem Kandidaten verglichen.
}
```

#### Board-spezifische Konstanten (aus global.gd)

- `BOARD_FIELDS = 40` — Standard-Felderanzahl. Boards konnen abweichen (30–60 Felder), aber 40 ist der empfohlene Standard.
- `MUENZEN_FUER_STERN = 20` — Kosten fur einen Stern.
- `MAX_TURNS = 10` — Maximale Rundenanzahl (Standard fur 2–3 Spieler; 9 fur 4–5; 8 fur 6–8).

### 3.3 Feld-Daten (FieldData)

Datenstruktur fur ein einzelnes Feld auf dem Board. 40 FieldData-Instanzen pro Board, gespeichert in `BoardData.fields` als Array.

#### Vollstandiges Schema

```
Dictionary FieldData {
    "index": int
        Feld-Index. Wertebereich: 0–39.
        Eindeutig innerhalb des Boards.
        Entspricht dem Index im BoardData.fields Array.
        Wird beim Board-Laden gesetzt und nie geandert.

    "type": String
        Feld-Typ (Enum als String).
        Mogliche Werte:
        "START"       — Startfeld. Kein aktiver Effekt.
                        Nur 1× pro Board (Index 0).
        "STAR_SHOP"   — Sternen-Shop. Stern kaufen (20 Munzen).
                        2–3× pro Board.
        "ITEM_SHOP"   — Item-Shop. Items kaufen (3–8 Munzen).
                        2× pro Board.
        "EVENT"       — Zufalls-Event aus event_pool.
                        5–8× pro Board.
        "LUCK"        — Glucks-Feld (Munz-Gewinn oder -Verlust).
                        3–4× pro Board.
        "COIN_BONUS"  — Munz-Bonus (fixer Betrag).
                        4× pro Board.
        "MINIGAME"    — Minispiel-Trigger (kein sofortiges
                        Minispiel; Minispiel ist feste Runden-Phase).
                        4–6× pro Board.

    "next_indices": Array[int]
        Indizes der nachsten Felder (ausgehende Verbindungen).
        Lange: 1–3.
        1 Eintrag = Linearer Pfad, keine Abzweigung.
        2 Eintrage = Abzweigung (Spieler wahlt).
        3 Eintrage = Komplexe Kreuzung (selten).
        Jeder Eintrag MUSS ein gultiger Feld-Index sein (0–39,
        nicht self). Darf nicht auf sich selbst zeigen.

    "prev_indices": Array[int]
        Indizes der vorherigen Felder (eingehende Verbindungen).
        Lange: 1–3.
        Ruckwarts-Verbindungen. Fur Ruckwarts-Bewegung
        (Teleporter-Item, negative Events).
        next/prev-Konsistenz MUSS gelten: Wenn A.next enthalt B,
        dann B.prev enthalt A.

    "is_branch_decision": bool
        true = Dieses Feld ist ein Abzweigungs-Entscheidungspunkt
        (next_indices.size() > 1).
        false = Keine Entscheidung notig.
        Abgeleitet aus next_indices, nicht manuell gesetzt.

    "coin_bonus_value": int
        Munz-Bonus fur COIN_BONUS Felder. Wertebereich: 0–20.
        0 = Kein Bonus (Standard fur alle Nicht-COIN_BONUS-Felder).
        Typische Werte: 3 (kleiner Bonus), 5 (mittlerer Bonus),
        8 (grosser Bonus).
        Wird bei Betreten sofort gutgeschrieben (additiv mit
        Munz-Magnet: +2 extra).

    "event_pool": Array[String]
        Event-Pool fur EVENT Felder. Leeres Array fur andere
        Feld-Typen.
        Enthalt Event-IDs (z.B. "coin_shower", "coin_loss",
        "item_gift", "star_steal", "teleport_random",
        "shield_grant", "skip_turn", "extra_roll").
        Ein Event wird beim Betreten per Gleichverteilung aus
        dem Pool gezogen.
        Regel "kein 2× hintereinander": Wenn das letzte Event
        in der event_history mit dem gezogenen ubereinstimmt,
        wird neu gezogen (maximal 3 Versuche; danach wird das
        Event trotzdem verwendet).

    "minigame_tier": String
        Schwierigkeits-Tier fur MINIGAME Felder.
        "LEICHT" / "MITTEL" / "SCHWER".
        Beeinflusst, welches Minispiel aus der Queue gezogen
        wird. Leere Minispiele bevorzugt bei LEICHT,
        komplexere bei SCHWER.
        Leerer String fur andere Feld-Typen.

    "visual_position": Array[float]
        3D-Position des Feldes. Exakt 3 Werte: [x, y, z].
        y = Hohe (meist 0.0 fur flache Felder; >0 fur
        erhohte Plattformen, Brucken, etc.).
        Wird fur Figuren-Positionierung und Kamera-Bewegung
        verwendet.
        Koordinatensystem: Godot 3D (Y-up).

    "visual_rotation": float
        Rotation des Feldes in Grad (Drehung um Y-Achse).
        Wertebereich: 0.0–360.0.
        0.0 = Standard-Ausrichtung.
        Wird fur die visuelle Ausrichtung des Feld-Modells
        verwendet (z.B. Kurven im Pfad).

    "branch_labels": Array[String]
        UI-Labels fur Abzweigungen. Lange: 0–3.
        Leeres Array = Keine Abzweigung (nur 1 next-Eintrag).
        Bei Abzweigung: Ein Label pro next-Eintrag, in gleicher
        Reihenfolge (branch_labels[0] gehort zu next_indices[0]).
        Beispiele: ["Sonnenpfad", "Schattenweg"],
        ["Sicherer Weg", "Riskante Abkurzung"].
        Maximale Lange pro Label: 20 Zeichen.
}
```

#### Feldtyp-Verteilung (Standard-40-Felder-Board)

| Feldtyp | Anzahl | Typische Indizes | Beschreibung |
|---|---|---|---|
| `START` | 1 | 0 | Startfeld. Alle Spieler starten hier. Kein Effekt bei Landung.|
| `STAR_SHOP` | 3 | 12, 24, 36 | Sternen-Shop. Gleichmassig uber das Board verteilt. Stern wandert zwischen diesen Feldern. |
| `ITEM_SHOP` | 2 | 8, 28 | Item-Shop. Fixe Positionen. Je 3 Items im Angebot. |
| `EVENT` | 6 | 5, 10, 15, 20, 25, 35 | Ereignis-Felder. Ziehen zufalliges Event aus Pool. |
| `LUCK` | 4 | 3, 13, 23, 33 | Glucks-/Pech-Felder. Munz-Anderung per 50/50-Chance. |
| `COIN_BONUS` | 4 | 7, 17, 27, 37 | Munz-Bonus-Felder. Fixe Munz-Gutschrift (3/5/8). |
| `MINIGAME` | 4 | 9, 19, 29, 39 | Minispiel-Marker. Kein sofortiger Effekt; Minispiel ist feste Runden-Phase. |
| Normale Felder (kein Effekt) | 16 | Restliche | Reine Durchgangsfelder. Kein Effekt bei Landung oder Uberquerung. |

### 3.4 Item-Definition (ItemDefinition — statisch, pro Item-Plugin)

Jedes Item-Plugin in `plugins/items/<name>/` enthalt eine `item_definition.json`. Diese Daten werden vom Item-Loader geparst und als statische Referenz im Speicher gehalten. Sie andern sich wahrend des Spiels nicht.

#### Vollstandiges JSON-Schema

```json
{
    "item_id": "glueckswuerfel",
    "display_name": "Glucks-Wurfel",
    "price": 5,
    "description_short": "Garantiert eine 5 beim nachsten Wurfeln. Einmalig verwendbar.",
    "effect_type": "fixed_dice",
    "effect_value": 5,
    "duration_turns": 1,
    "use_phase": "ROLL",
    "icon_path": "icon.webp",
    "model_path": "glueckswuerfel.glb",
    "sfx_use": "glueckswuerfel_use.ogg"
}
```

#### Feld-Definitionen

| Feld | Typ | Beschreibung | Wertebereich / Validierung |
|---|---|---|---|
| `item_id` | String | Eindeutige Item-ID. Plugin-Name. | `^[a-z_]+$`, max 30 Zeichen. Muss dem Plugin-Ordnernamen entsprechen. |
| `display_name` | String | Anzeigename im Shop und Inventar (lokalisiert via `.po`). | Nicht leer, max 30 Zeichen. |
| `price` | int | Kaufpreis in Munzen. | 1–15. Standardwerte: Glucks-Wurfel 5, Schutzschild 6, Munz-Magnet 7, Teleporter 4, Diebhandschuh 8. |
| `description_short` | String | Kurzbeschreibung im Shop-Tooltip. | Max 150 Zeichen. Erklart Effekt und Dauer in einem Satz. |
| `effect_type` | String | Effekt-Typ. Bestimmt die Server-Logik. | Einer von: "fixed_dice" (fester Wurfelwert), "teleport_star" (Teleport zum Stern), "passive_shield" (Schutzschild), "coin_multiplier" (Munz-Magnet), "steal" (Diebstahl). |
| `effect_value` | Variant | Effekt-spezifischer Wert. | Typ abhangig von effect_type: fixed_dice → int (1–6), teleport_star → String ("nearest_star"), passive_shield → null, coin_multiplier → int (Bonus-Munzen), steal → String ("random"). |
| `duration_turns` | int | Wirkungsdauer in Zugen. 1 = einmalig (wird sofort nach Anwendung entfernt). | 1–5. Standard: 1 fur alle Items ausser Munz-Magnet (3). |
| `use_phase` | String | In welcher Phase kann das Item verwendet werden? | "ROLL" (vor dem Wurfeln), "MOVE" (wahrend der Bewegung), "ANY" (jederzeit, auch passiv). |
| `icon_path` | String | Pfad zum Icon (relativ zum Plugin-Ordner). | `.webp` oder `.png`, empfohlen 128×128 px. |
| `model_path` | String | Pfad zum 3D-Modell (relativ). | `.glb` oder `.gltf`. Max 500 Tris. |
| `sfx_use` | String | Pfad zum Sound bei Benutzung (relativ). | `.ogg`, 64–96 kbps Mono, < 300 KB. |

#### Die 5 Items in der Ubersicht

| Item-ID | Anzeigename | Preis | Effekt-Typ | Dauer | Phase |
|---|---|---|---|---|---|
| `glueckswuerfel` | Glucks-Wurfel | 5 | fixed_dice (Wert: 5) | 1 Zug | ROLL |
| `schutzschild` | Schutzschild | 6 | passive_shield | Bis Auslosung | ANY |
| `muenzmagnet` | Munz-Magnet | 7 | coin_multiplier (+2) | 3 Zuge | ANY |
| `teleporter` | Teleporter | 4 | teleport_star ("nearest_star") | 1 Zug | ROLL |
| `diebhandschuh` | Dieb-Handschuh | 8 | steal ("random") | 1 Zug | ROLL |

### 3.5 Minispiel-Metadaten (minigame.json — pro Minispiel-Plugin)

Jedes Minispiel-Plugin in `plugins/minigames/<name>/` MUSS eine `minigame.json` mit Metadaten enthalten. Diese Datei wird vom Minispiel-Loader geparst und an die Minispiel-Queue ubergeben.

#### Vollstandiges JSON-Schema

```json
{
    "minigame_id": "muenzregen",
    "display_name": "Munzregen",
    "category": "geschicklichkeit",
    "min_players": 2,
    "max_players": 8,
    "duration_seconds": 30,
    "description": "Sammle die meisten fallenden Munzen! Bewegt euch geschickt und schnappt euch die goldenen Munzen, bevor sie im Sand versinken.",
    "instructions": "Bewege deinen Arenian mit dem linken Stick und sammle die goldenen Munzen ein. Halte Ausschau nach der seltenen roten Super-Munze!",
    "tags": ["sammeln", "bewegung", "wettlauf", "geschicklichkeit"],
    "sort_order": "descending",
    "controls": {
        "primary": "left_stick",
        "secondary": null
    },
    "arena_variant": false,
    "thumbnail": "thumbnail.webp"
}
```

#### Feld-Definitionen

| Feld | Typ | Beschreibung | Validierung |
|---|---|---|---|
| `minigame_id` | String | Plugin-ID. Kleinbuchstaben, Unterstriche. Entspricht Ordnername. | `^[a-z_]+$`, max 30 Zeichen. |
| `display_name` | String | Anzeigename (lokalisiert). | Nicht leer, max 30 Zeichen. |
| `category` | String | Minispiel-Kategorie. Bestimmt UI-Gruppierung und Gewichtung in der Queue. | Einer von: "geschicklichkeit", "reaktion", "puzzle_logik", "rechnen_wort", "kooperation". |
| `min_players` | int | Minimale Spielerzahl. Minispiele mit min_players > aktuelle Spielerzahl werden nicht ausgewahlt. | 1–8, muss <= max_players sein. |
| `max_players` | int | Maximale Spielerzahl. Minispiele mit max_players < aktuelle Spielerzahl werden nicht ausgewahlt. | 2–8, muss >= min_players sein. |
| `duration_seconds` | int | Dauer in Sekunden (Standard: 30). | 15–120. Abweichungen mussen begrundet werden. |
| `description` | String | Kurzbeschreibung fur Ladebildschirm und Minispiel-Vorstellung. | Max 200 Zeichen. |
| `instructions` | String | Spielanleitung, eingeblendet vor Minispiel-Start. | Max 300 Zeichen. |
| `tags` | Array[String] | Tags fur Filterung, Statistik und Queue-Gewichtung. | Beliebig viele, je max 20 Zeichen. Empfohlen: 3–5 Tags. |
| `sort_order` | String | Score-Sortierung: "descending" (hoherer Score = besser) oder "ascending" (niedrigerer Score = besser, z.B. Zeit). | "ascending" oder "descending". |
| `controls.primary` | String\|null | Primare Steuerung des Minispiels. | "left_stick", "right_stick", "motion", "button", "touch" oder null. |
| `controls.secondary` | String\|null | Sekundare Steuerung. | Wie primary. |
| `arena_variant` | bool | Hat das Minispiel eine ArenaStar-Variante (optional, Post-Launch)? | true/false. Default: false. |
| `thumbnail` | String | Pfad zum Thumbnail-Bild (relativ zum Plugin-Ordner). | `.webp` oder `.png`, 512×288 px empfohlen. |

#### Die 12 Minispiele in der Ubersicht

| Minispiel-ID | Kategorie | Min/Max Spieler | Dauer | Sortierung |
|---|---|---|---|---|
| `muenzregen` | geschicklichkeit | 2/8 | 30s | descending |
| `schildkroetenrennen` | reaktion | 2/8 | 30s | ascending (Zeit) |
| `kokosnuss_werfen` | geschicklichkeit | 2/8 | 30s | descending |
| `krabben_jagd` | reaktion | 2/8 | 30s | descending |
| `muschel_memory` | puzzle_logik | 2/6 | 45s | descending |
| `wellen_reiten` | geschicklichkeit | 2/8 | 30s | descending |
| `perlen_tauchen` | reaktion | 2/8 | 30s | descending |
| `vulkan_ausbruch` | geschicklichkeit | 2/8 | 25s | ascending (Zeit) |
| `laternen_flug` | geschicklichkeit | 2/8 | 30s | descending |
| `bruecken_bau` | puzzle_logik | 2/6 | 45s | ascending (Zeit) |
| `nebel_irrgarten` | puzzle_logik | 2/8 | 40s | ascending (Zeit) |
| `schatz_trage` | kooperation | 4/8 | 35s | descending |

### 3.6 Charakter-Daten (character.json — pro Charakter-Plugin)

Jedes Charakter-Plugin in `plugins/characters/<name>/` MUSS eine `character.json` enthalten.

#### Vollstandiges JSON-Schema

```json
{
    "id": "brix",
    "display_name": "Brix",
    "description": "Ein frohlicher Baumeister von der Mechanik-Stadt. Immer optimistisch, immer hungrig auf Abenteuer. Tollpatschig aber gutherzig.",
    "catchphrase": "Stein auf Stein — das wird fein!",
    "home_island": "mechanik_stadt",
    "model_path": "brix.glb",
    "portrait_path": "portrait.webp",
    "icon_path": "icon.webp",
    "voice_pack": "brix_voice",
    "stats": {
        "speed": 3,
        "luck": 4,
        "strength": 3,
        "agility": 2
    },
    "animations": {
        "idle": "brix_idle",
        "walk": "brix_walk",
        "jump": "brix_jump",
        "celebrate": "brix_celebrate",
        "sad": "brix_sad",
        "taunt": "brix_taunt"
    },
    "unlock_condition": null
}
```

#### Feld-Definitionen

| Feld | Typ | Beschreibung |
|---|---|---|
| `id` | String | Charakter-ID (Plugin-Name). Kleinbuchstaben, Unterstriche. |
| `display_name` | String | Anzeigename im Auswahl-Screen (lokalisiert). |
| `description` | String | Kurzbeschreibung im Charakter-Auswahl-Screen. Max 200 Zeichen. |
| `catchphrase` | String | Charakter-Spruch, wird bei Auswahl abgespielt/eingeblendet. Max 80 Zeichen. |
| `home_island` | String | Heimat-Insel-Plugin-ID. Referenz auf `plugins/boards/<id>/`. |
| `model_path` | String | Pfad zum 3D-Modell (relativ zum Plugin-Ordner). |
| `portrait_path` | String | Pfad zum Portrat-Bild (Charakter-Auswahl). Empfohlen 512×512 px. |
| `icon_path` | String | Pfad zum Mini-Icon (HUD). Empfohlen 128×128 px. |
| `voice_pack` | String | Name des Voice-Packs. Ordner in `assets/sounds/voices/<voice_pack>/`. |
| `stats` | Dictionary | Charakter-Statistiken. **Rein kosmetisch** — haben KEINEN Gameplay-Effekt. Dienen nur der UI-Darstellung und Charakter-Fantasie. Werte 1–5. |
| `animations` | Dictionary | Animations-Namen fur den AnimationTree. 6 Pflicht-Animationen: idle, walk, jump, celebrate, sad, taunt. |
| `unlock_condition` | String\|null | Freischaltbedingung. null = sofort verfugbar. String = Beschreibung der Bedingung (z.B. "Win 5 games on Sonnenstrand"). |

**Wichtig:** Die `stats` haben KEINEN spielmechanischen Effekt. Alle 8 Arenians sind gameplay-technisch vollstandig identisch. Stats sind rein kosmetische Charakter-Fantasie.

### 3.7 Speicherformate (Persistenz)

#### 3.7.1 Einstellungen und Statistiken (data.cfg)

- **Format:** Godot ConfigFile (`.cfg`)
- **Speicherort:** `user://data.cfg`
- **Lese-/Schreibzugriff:** Hauptmenu (lesen), nach jedem Spiel (Statistiken schreiben), bei Einstellungsanderung (sofort schreiben)
- **Maximale Grosse:** ~10 KB

**Sektionen und Schlossel:**

```
[settings]
audio_master = 100          # 0–100, Master-Lautstarke in Prozent
audio_music = 80            # 0–100, Musik-Lautstarke
audio_sfx = 100             # 0–100, SFX-Lautstarke
audio_voice = 90            # 0–100, Stimmen-Lautstarke
video_fullscreen = true     # true/false
video_resolution = "1920x1080"  # String, eine der unterstutzten Auflosungen
video_vsync = true          # true/false
video_aa = "TAA"            # "AUS", "MSAA_2X", "MSAA_4X", "TAA"
video_scale_3d = 1.0        # 0.5–1.0 in 0.1 Schritten
video_shadows = "NIEDRIG"   # "AUS", "NIEDRIG", "MITTEL"
video_texture_quality = "HOCH"  # "NIEDRIG", "MITTEL", "HOCH"
video_particles = "NORMAL"  # "AUS", "WENIG", "NORMAL"
language = "de"             # "de", "en", "fr", "es", "ja", "zh"
accessibility_subtitles = true       # true/false
accessibility_colorblind_mode = "AUS"  # "AUS", "PROTANOPIE", "DEUTERANOPIE", "TRITANOPIE"
accessibility_reduce_motion = false  # true/false
accessibility_high_contrast = false  # true/false
accessibility_mono_audio = false     # true/false
accessibility_text_size = "NORMAL"   # "NORMAL", "GROSS", "SEHR_GROSS"
accessibility_screen_shake = true    # true/false

[statistics]
total_games_played = 0          # int, Gesamtanzahl gespielter Partien
total_wins = 0                  # int, Gesamtanzahl gewonnener Partien (1. Platz)
total_coins_collected = 0       # int, Summe aller gesammelten Munzen
total_stars_bought = 0          # int, Summe aller gekauften Sterne
total_minigames_played = 0      # int, Summe aller gespielten Minispiele
total_minigames_won = 0         # int, Summe gewonnener Minispiele (1. Platz)
total_items_used = 0            # int, Summe verwendeter Items
total_events_triggered = 0      # int, Summe ausgeloster Ereignis-Felder
total_fields_traveled = 0       # int, Summe gereister Felder
total_playtime_seconds = 0      # int, Gesamtspielzeit in Sekunden
favorite_character = "brix"     # String, meistgenutzter Charakter
favorite_island = "sonnenstrand"  # String, meistgespielte Insel
highest_coins_in_game = 0       # int, Hochstwert Munzen in einer Partie
highest_stars_in_game = 0       # int, Hochstwert Sterne in einer Partie
longest_game_turns = 0          # int, Langste Partie in Runden

[unlocks]
unlocked_characters = ["brix","nixie","koko","pip","zara","flint","luna","momo"]
unlocked_islands = ["sonnenstrand","korallenriff","vulkaninsel","nebelwald","kristallhoehle","wolkenreich","zeitgarten","schattenarchipel"]

[controls_p1]
move_left = 65          # Keycode A
move_right = 68         # Keycode D
move_up = 87            # Keycode W
move_down = 83          # Keycode S
confirm = 4194309       # Keycode Enter
cancel = 4194310        # Keycode Escape
use_item = 70           # Keycode F
taunt = 84              # Keycode T
accelerate = 4194325    # Keycode Shift
skip = 4194305          # Keycode Tab

[controls_p2]
move_left = 73          # Keycode I
move_right = 76         # Keycode L
move_up = 74            # Keycode J
move_down = 75          # Keycode K
confirm = 4194374       # Keycode Right Shift
cancel = 4194310        # Keycode Escape
use_item = 85           # Keycode U
taunt = 79              # Keycode O
accelerate = 4194325    # Keycode Shift
skip = 4194305          # Keycode Tab
```

#### 3.7.2 Spielstand-Dateien (SaveGame)

- **Format:** Godot ConfigFile (`.cfg`) oder binar via `var_to_bytes()`
- **Speicherort:** `user://savegames/save_<timestamp>.sav`
- **Lese-/Schreibzugriff:** Nur im Pause-Menu (Spieler speichert manuell)
- **Maximale Grosse:** ~20 KB pro Spielstand

```
Dictionary SaveGame {
    "version": String
        Spiel-Version zum Zeitpunkt des Speicherns.
        "2.0.0" — verhindert Laden in inkompatiblen alteren Versionen.
        Bei Abweichung: Migrationsfunktion prufen, ggf. Warnung anzeigen.

    "timestamp": int
        Unix-Timestamp des Speicher-Zeitpunkts.
        Verwendet fur Sortierung im Lade-Menu (neueste zuerst).

    "board_id": String
        Board-Plugin-ID der laufenden Partie.

    "current_turn": int
        Aktuelle Runde (1–10).

    "current_round": int
        Alias fur current_turn.

    "current_player_index": int
        Spieler-ID des aktiven Spielers (1–8).

    "phase": String
        Aktuelle Phase ("ROLL", "MOVE", etc.).

    "players": Array[PlayerData]
        Vollstandige Spieler-Daten (1–8 Eintrage).
        Siehe Abschnitt 3.1.

    "board": BoardData
        Vollstandige Board-Daten.
        Siehe Abschnitt 3.2.

    "minigame_history": Array[String]
        IDs der bereits gespielten Minispiele.
        Verhindert Wiederholung im selben Spiel bei Fortsetzung.

    "event_history": Array[String]
        IDs der bereits ausgelosten Events.
        Fur "kein 2× hintereinander"-Regel bei Fortsetzung.

    "game_seed": int
        Zufalls-Seed des Spiels.
        Ermoglicht deterministisches Wiederherstellen.
}
```

### 3.8 Netzwerk-Nachrichten (RPC-Dictionaries)

Alle RPCs verwenden Dictionaries als Payload. Godot RPCs unterstutzen nur primitive Typen — Dictionaries sind der flexibelste Weg.

#### 3.8.1 player_action (Client → Server)

Client sendet eine Spieler-Aktion. Server validiert und fuhrt aus.

```
Dictionary PlayerAction {
    "type": String
        Aktions-Typ.
        Mogliche Werte:
        "roll"          — Wurfeln
        "buy_star"      — Stern kaufen
        "buy_item"      — Item kaufen
        "use_item"      — Item benutzen (aus Inventar)
        "choose_path"   — Pfad an Abzweigung wahlen
        "skip"          — Aktion uberspringen (Pass)

    "player_id": int
        Spieler-ID (1–8). Wird vom Server verifiziert
        (muss mit multiplayer.get_remote_sender_id()
        ubereinstimmen).

    "data": Dictionary
        Aktions-spezifische Daten.
        Bei "roll": {} (leer, keine zusatzlichen Daten)
        Bei "buy_star": {} (leer, Stern-Preis ist fest)
        Bei "buy_item": {"item_id": "glueckswuerfel"}
        Bei "use_item": {"item_id": "teleporter"}
        Bei "choose_path": {"branch_index": 0}
        Bei "skip": {} (leer)
}

Beispiel 1 — Wurfeln:
{
    "type": "roll",
    "player_id": 3,
    "data": {}
}

Beispiel 2 — Item kaufen:
{
    "type": "buy_item",
    "player_id": 5,
    "data": {"item_id": "schutzschild"}
}

Beispiel 3 — Pfad wahlen:
{
    "type": "choose_path",
    "player_id": 2,
    "data": {"branch_index": 1}
}
```

#### 3.8.2 server_update (Server → Alle Clients)

Server sendet periodische State-Updates. Frequenz: Board-Modus nur bei Anderungen, Minispiel-Modus alle 50ms.

```
Dictionary ServerUpdate {
    "type": String
        Update-Typ.
        "full_state"    — Kompletter Game-State (nach Initial Load,
                          Reconnect, oder bei Client-seitigem
                          State-Mismatch).
        "partial_state" — Nur geanderte Felder (Board-Modus).
        "event"         — Einzelnes Ereignis (Feld-Effekt,
                          Item-Effekt).
        "animation"     — Animations-Trigger (rein visuell, keine
                          State-Anderung).
        "minigame_sync" — Minispiel-Sync (Positionen, Scores).

    "phase": String
        Aktuelle Phase ("ROLL", "MOVE", "EVENT", "SHOP",
        "MINIGAME", "STAR", "BONUS_STARS", "VICTORY").

    "current_player": int
        Spieler-ID des aktiven Spielers.

    "players": Array[PlayerData]
        Alle Spieler-Daten (1–8 Eintrage).
        Bei partial_state: Nur geanderte Spieler.

    "board": Dictionary
        Board-Anderungen.
        Bei full_state: Komplettes BoardData.
        Bei partial_state: Nur geanderte Felder
        (z.B. {"active_star_shop_index": 24, "star_available": true}).
        Bei event/animation: Leeres Dictionary {}.

    "event": Dictionary
        Ereignis-Daten (nur bei type="event").
        Enthalt: event_id, description (lokalisiert),
        results (Dictionary mit player_id → effect).

    "turn": int
        Aktuelle Runde.

    "timestamp_ms": int
        Server-Zeitstempel in Millisekunden.
        Fur Client-seitige Latenzmessung.
}

Beispiel — Full-State-Update nach Spielstart:
{
    "type": "full_state",
    "phase": "ROLL",
    "current_player": 1,
    "players": [ /* PlayerData fur 8 Spieler */ ],
    "board": { /* BoardData */ },
    "event": {},
    "turn": 1,
    "timestamp_ms": 1234567890123
}

Beispiel — Partial-State-Update nach Wurfelwurf:
{
    "type": "partial_state",
    "phase": "MOVE",
    "current_player": 1,
    "players": [
        {"id": 1, "dice_value": 5, "field_index": 5}
    ],
    "board": {},
    "event": {},
    "turn": 1,
    "timestamp_ms": 1234567895000
}
```

#### 3.8.3 minigame_start (Server → Alle Clients)

Wird zu Beginn eines Minispiels gesendet.

```
Dictionary MinigameStart {
    "type": "minigame_start"
        Fixer Typ.

    "minigame_id": String
        ID des zu startenden Minispiels ("muenzregen").

    "players": Array[int]
        Spieler-IDs der Teilnehmer (2–8 Eintrage).

    "seed": int
        Zufalls-Seed fur deterministisches Minispiel.

    "countdown_seconds": int
        Countdown-Dauer vor Start (Standard: 5).

    "duration_seconds": int
        Minispiel-Dauer in Sekunden (aus minigame.json).
}

Beispiel:
{
    "type": "minigame_start",
    "minigame_id": "muenzregen",
    "players": [1, 2, 3, 4, 5, 6, 7, 8],
    "seed": 987654321,
    "countdown_seconds": 5,
    "duration_seconds": 30
}
```

#### 3.8.4 minigame_input (Client → Server, wahrend Minispiel)

Client sendet Input-Stream wahrend des Minispiels. Unreliable Ubertragung (Toleranz fur Paketverlust).

```
Dictionary MinigameInput {
    "type": "minigame_input"
        Fixer Typ.

    "player_id": int
        Spieler-ID (vom Server verifiziert).

    "input_data": Dictionary
        Input-spezifische Daten.
        Bei left_stick: {"x": 0.5, "y": -0.3}
        Bei button: {"action": "jump", "pressed": true}
        Bei motion: {"accelerometer": {"x": 0.1, "y": 0.2, "z": 0.9}}
}

Beispiel:
{
    "type": "minigame_input",
    "player_id": 3,
    "input_data": {
        "x": 0.7,
        "y": -0.1,
        "action": null
    }
}
```

#### 3.8.5 minigame_result (Server → Alle Clients)

Wird am Ende eines Minispiels gesendet.

```
Dictionary MinigameResult {
    "type": "minigame_result"
        Fixer Typ.

    "minigame_id": String
        ID des gespielten Minispiels.

    "rankings": Array[Dictionary]
        Sortierte Platzierungen (1. Platz zuerst).
        Jeder Eintrag:
        {
            "player_id": int,
            "score": float,
            "placement": int  # 1–8
        }

    "coin_rewards": Dictionary
        Munz-Belohnungen pro Spieler.
        Key = player_id (int), Value = Munzen (int).
        Beispiel: {1: 10, 2: 5, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    "catch_up_bonus": Dictionary
        Catch-Up Bonus-Munzen.
        Key = player_id (int), Value = Bonus-Munzen (int).
        Leer {}, wenn kein Catch-Up aktiv.

    "duration_actual": float
        Tatsachliche Dauer in Sekunden.
}

Beispiel:
{
    "type": "minigame_result",
    "minigame_id": "muenzregen",
    "rankings": [
        {"player_id": 3, "score": 42.0, "placement": 1},
        {"player_id": 1, "score": 35.0, "placement": 2},
        {"player_id": 5, "score": 28.0, "placement": 3},
        {"player_id": 2, "score": 22.0, "placement": 4},
        {"player_id": 7, "score": 18.0, "placement": 5},
        {"player_id": 4, "score": 15.0, "placement": 6},
        {"player_id": 6, "score": 10.0, "placement": 7},
        {"player_id": 8, "score": 5.0, "placement": 8}
    ],
    "coin_rewards": {1: 5, 3: 10, 5: 3, 2: 0, 4: 0, 6: 0, 7: 0, 8: 0},
    "catch_up_bonus": {8: 3, 6: 1},
    "duration_actual": 30.5
}
```

#### 3.8.6 game_over (Server → Alle Clients)

Wird am Ende des Spiels nach der Bonus-Stern-Vergabe gesendet.

```
Dictionary GameOver {
    "type": "game_over"
        Fixer Typ.

    "rankings": Array[Dictionary]
        Finale Rangliste (1. Platz zuerst).
        Jeder Eintrag:
        {
            "player_id": int,
            "stars": int,           # Sterne vor Bonus-Sternen
            "coins": int,           # Munzen bei Spielende
            "bonus_stars": int,     # Durch Bonus-Sterne erhalten
            "bonus_categories": [String],  # Welche Kategorien gewonnen?
            "total_stars": int,     # Sterne nach Bonus-Sternen (stars + bonus_stars)
            "placement": int        # Finale Platzierung (1–8)
        }

    "bonus_star_categories": Array[String]
        Die 3 gezogenen Bonus-Stern-Kategorien dieses Spiels.

    "stats": Dictionary
        Spiel-Statistiken (fur Statistik-Bildschirm).
        Key = player_id, Value = Dictionary mit Statistiken:
        {
            "minigames_won": int,
            "items_used": int,
            "events_triggered": int,
            "fields_traveled": int,
            "laps_completed": int,
            "avg_dice_roll": float
        }

    "duration_seconds": float
        Gesamtdauer des Spiels in Sekunden.
}

Beispiel:
{
    "type": "game_over",
    "rankings": [
        {
            "player_id": 3, "stars": 3, "coins": 45,
            "bonus_stars": 1, "bonus_categories": ["Minispiel-Meister"],
            "total_stars": 4, "placement": 1
        },
        {
            "player_id": 1, "stars": 2, "coins": 62,
            "bonus_stars": 1, "bonus_categories": ["Munz-Konig"],
            "total_stars": 3, "placement": 2
        }
        // ... (Spieler 2–8)
    ],
    "bonus_star_categories": ["Munz-Konig", "Minispiel-Meister", "Viellaufer"],
    "stats": {
        1: {"minigames_won": 2, "items_used": 4, "events_triggered": 5,
            "fields_traveled": 87, "laps_completed": 2, "avg_dice_roll": 3.8}
        // ...
    },
    "duration_seconds": 1380.0
}
```

---

## 4. Formulas

### 4.1 Datenvalidierung (Server-seitig, vor jedem State-Update)

Jedes eingehende Dictionary wird gegen sein Schema validiert. Die Validierung folgt diesem Muster:

- **Typ-Prufung:** Jedes Feld hat den erwarteten Typ (int, float, String, bool, Array, Dictionary). Falscher Typ → Validierung fehlgeschlagen.
- **Wertebereich-Prufung:** Jedes Feld hat einen definierten Wertebereich (z.B. `coins` 0–99). Wert ausserhalb → Validierung fehlgeschlagen.
- **Existenz-Prufung:** Pflichtfelder mussen vorhanden sein. Fehlendes Pflichtfeld → Validierung fehlgeschlagen.
- **Referenz-Prufung:** Felder, die auf andere Daten verweisen (z.B. `character_id`), mussen auf existierende Entitaten zeigen.

**Fehlerbehandlung bei gescheiterter Validierung:**
1. `push_warning("[WARN] State-Update-Validierung fehlgeschlagen fur Spieler %d: %s" % [player_id, reason])`
2. Update wird verworfen (keine State-Anderung).
3. Server sendet `server_update` vom Typ `"full_state"` an den betroffenen Client, um mogliche Desyncs zu beheben.

### 4.2 Clamp-Formel fur Munzen und Sterne

Um Integer-Overflow zu verhindern und das UI sauber zu halten:

```
new_coins = clamp(old_coins + amount, 0, 99)
new_stars = clamp(old_stars + amount, 0, 99)
```

- `amount` kann positiv (Einnahme) oder negativ (Ausgabe) sein.
- `clamp(value, min, max)` = wenn `value < min`, dann `min`; wenn `value > max`, dann `max`; sonst `value`.
- Hard-Cap 99 schutzt vor UI-Overflow und macht das Balancing uberschaubar.
- UI-Display-Cap 999 ist rein visuell; der tatsachliche Wert uberschreitet nie 99.

### 4.3 Pfad-Konsistenzprufung (Board-Validierung)

Bei jedem Board-Ladevorgang wird die next/prev-Konsistenz gepruft:

```
Fur jedes Feld i im Board:
    Fur jeden next_idx in fields[i].next_indices:
        Prufe: 0 <= next_idx < BOARD_FIELDS
        Prufe: next_idx != i (kein Feld zeigt auf sich selbst)
        Prufe: i in fields[next_idx].prev_indices (next/prev-Konsistenz)

    Fur jeden prev_idx in fields[i].prev_indices:
        Prufe: 0 <= prev_idx < BOARD_FIELDS
        Prufe: prev_idx != i
        Prufe: i in fields[prev_idx].next_indices
```

**Fehlerbehandlung:** Schlagt die Konsistenzprufung fehl, wird das Board nicht geladen. `push_error("[ERROR] Board-Konsistenzprufung fehlgeschlagen: Feld %d" % i)`. Das Board wird im Menu ausgegraut und ist nicht spielbar.

### 4.4 Feldtyp-Validierung (Board-Validierung)

```
Pflicht-Felder pro Board:
    START:       genau 1
    STAR_SHOP:   2–3
    ITEM_SHOP:   1–4
    EVENT:       3–8
    LUCK:        2–6
    COIN_BONUS:  2–6
    MINIGAME:    2–8
    (Rest: neutrale Felder ohne Effekt)

Prufung:
    count(START) == 1
    count(STAR_SHOP) >= 2 AND count(STAR_SHOP) <= 3
    count(ITEM_SHOP) >= 1 AND count(ITEM_SHOP) <= 4
    count(EVENT) >= 3 AND count(EVENT) <= 8
    count(LUCK) >= 2 AND count(LUCK) <= 6
    count(COIN_BONUS) >= 2 AND count(COIN_BONUS) <= 6
    count(MINIGAME) >= 2 AND count(MINIGAME) <= 8
    Summe aller count() == BOARD_FIELDS (40)
```

### 4.5 Statistiken-Aktualisierung nach Spielende

Nach jedem Spiel werden die lokalen Statistiken (`data.cfg`) des Spielers aktualisiert. Betroffen sind nur die Statistiken des lokalen Spielers (der Client, auf dem das Spiel lauft). Im Online-Modus speichert nur der Host-Client.

```
total_games_played += 1
total_coins_collected += (Summe aller Munz-Einnahmen des Spielers)
total_stars_bought += (Spieler.stars am Spielende, vor Bonus-Sternen)
total_minigames_played += (Anzahl Minispiele im Spiel = current_turn)
total_minigames_won += (Spieler.minigames_won)
total_items_used += (Spieler.items_used)
total_events_triggered += (Spieler.events_triggered)
total_fields_traveled += (Spieler.total_fields_traveled)
total_playtime_seconds += (Spiel.duration_seconds)

if player.placement == 1:
    total_wins += 1

if player.stars > highest_stars_in_game:
    highest_stars_in_game = player.stars

if player.coins > highest_coins_in_game:
    highest_coins_in_game = player.coins

if game_turns > longest_game_turns:
    longest_game_turns = game_turns

# Favorite-Updates (einfache Mehrheit)
if times_used_character[player.character_id] > times_used_character[favorite_character]:
    favorite_character = player.character_id

if times_played_island[board_id] > times_played_island[favorite_island]:
    favorite_island = board_id
```

---

## 5. Edge Cases

1. **Item-Inventar voll (3/3), Spieler betritt Item-Shop:** Kauf wird abgelehnt. Shop-UI zeigt alle Items ausgegraut mit Hinweis "Inventar voll (max. 3)". Spieler kann Shop schliessen (Pass) oder vorhandenes Item verwenden (falls use_phase erlaubt), dann neu kaufen.

2. **PlayerData-Hash stimmt nicht zwischen Server und Client:** Server sendet nach jedem State-Update einen Hash des kompletten Player-State. Client vergleicht mit lokalem State. Bei Abweichung: Client fordert Full-State-Update an (`_rpc_request_full_state`). Server sendet `server_update` vom Typ `"full_state"`. Client uberschreibt lokalen State komplett.

3. **Feld-Typ MINIGAME wird betreten, aber kein Minispiel verfugbar:** Alle 12 Minispiele wurden bereits gespielt. Server: Minigame-Queue gibt null zuruck. Phase wechselt direkt zu STERN (Minispiel wird ubersprungen). Client zeigt kurze Nachricht "Keine Minispiele mehr verfugbar — Stern-Phase beginnt."

4. **SaveGame aus alterer Version laden:** Version im SaveGame weicht von `VERSION` ab. Lade-Funktion pruft Versions-Kompatibilitat. Migrations-Pfad: Alte Keys in neue Keys ubersetzen. Wenn Migration nicht moglich: Warnung "Spielstand inkompatibel. Neues Spiel starten."

5. **8 Spieler gleichzeitig auf demselben Feld:** `visual_position` jedes Spielers wird leicht versetzt (Kreis-Pattern, Radius 0,5, Winkel = player_id * 45°). Alle erhalten den Feld-Effekt (Reihenfolge nach player_id). UI zeigt Stapel-Indikator ("8 Spieler hier").

6. **Item-Preis wird serverseitig durch Event modifiziert:** Server fuhrt `price_modifier`-Dictionary: `{"global": 0, "item_shop_0": -2, "item_shop_1": 0}`. Tatsachlicher Preis = `max(1, item.price + price_modifier[shop_id])`. Minimum 1 Munze (Item kostet nie 0). Client erhalt `actual_price` im Shop-Update.

7. **Spieler hat 0 Munzen und betritt LUCK-Feld mit negativem Ergebnis:** Clamping greift: `new_coins = clamp(0 - loss_amount, 0, 99) = 0`. Spieler verliert keine Munzen (kann nicht unter 0 fallen). Event-Kommentar: "Du hast Gluck — du hast keine Munzen zum Verlieren!"

8. **MinigameResult enthalt weniger Platzierungen als Spieler:** Ein Spieler hat im Minispiel 0 Score und wurde disconnected. Regel: Disconnectete Spieler werden auf den letzten Platz gesetzt (Platz = aktuelle Spielerzahl). Ihr Score = 0.

9. **BoardData.fields enthalt ungultige next/prev-Verweise:** Board-Ladung schlagt fehl. Board wird im Menu ausgegraut. Fehler wird geloggt mit Feld-Index und Grund.

10. **Zwei Spieler wahlen simultan denselben Charakter in der Lobby:** Server verarbeitet RPCs sequenziell. Erster RPC gewinnt. Zweiter RPC wird abgelehnt mit `_rpc_character_rejected`. Client zeigt "Charakter bereits gewahlt" und offnet erneut Auswahl.

---

## 6. Dependencies

### 6.1 Interne Abhangigkeiten

| Datenstruktur | Verwendet von | Verwendung |
|---|---|---|
| `PlayerData` | `server/game.gd`, `client/game.gd`, `controller.gd`, `player_info.gd`, Lobby, Victory, SaveGame | Zentrale Spieler-Daten fur alle Systeme |
| `BoardData` | `server/game.gd`, `client/game.gd`, `controller.gd`, `node.gd`, Board Loader | Board-Zustand und -Konfiguration |
| `FieldData` | `BoardData.fields`, `controller.gd` (Feld-Effekte), `node.gd`, Board Loader | Feld-Logik, Pfad-Verkettung |
| `ItemDefinition` | `item_loader.gd`, `shop.gd`, `controller.gd` | Item-Shop und Effekte |
| `MinigameMetadata` | `minigame_loader.gd`, `minigame_queue.gd`, `controller.gd` | Minispiel-Auswahl und -Konfiguration |
| `CharacterData` (character.json) | `character_loader.gd`, `character_select.gd`, `player_board.gd` | Charakter-Plugins |
| `PlayerAction` | Alle Client-Systeme → Server via RPC | Spieler-Input |
| `ServerUpdate` | Server → Alle Clients via RPC | State-Synchronisation |
| `MinigameStart`, `MinigameInput`, `MinigameResult` | Server ↔ Clients via RPC | Minispiel-Lebenszyklus |
| `GameOver` | Server → Alle Clients via RPC | Spielende, Siegerehrung |
| `SaveGame` | `savegames.gd`, `pause_menu.gd` | Spielstand speichern/laden |
| `data.cfg` | `global.gd`, `options_menu.gd`, `savegames.gd` | Einstellungen + Statistiken |

### 6.2 Externe Abhangigkeiten

| Abhangigkeit | Zweck |
|---|---|
| Godot ConfigFile | Speicherformat fur `.cfg` Dateien |
| Godot JSON | Parsen der `.json` Plugin-Manifeste |
| Godot `var_to_bytes` / `bytes_to_var` | Binare Serialisierung fur SaveGames |
| Godot `multiplayer` (RPC) | Netzwerk-Ubertragung der Dictionaries |

---

## 7. Tuning Knobs

### 7.1 Wertebereich-Tuning

| Parameter | Ort | Standard | Bereich | Beschreibung |
|---|---|---|---|---|
| `START_COINS` | `global.gd` | `10` | 0–30 | Start-Munzen pro Spieler. Hoher = schnellerer Stern-Kauf. |
| `MUENZEN_FUER_STERN` | `global.gd` | `20` | 10–40 | Stern-Preis. Hoher = seltener Sterne. |
| `MAX_ITEMS` | `global.gd` | `3` | 1–5 | Max Items im Inventar. Hoher = mehr strategische Optionen. |
| `MAX_COINS` (Hard-Cap) | `global.gd` | `99` | 50–999 | Maximaler Munzwert. Hoher = weniger Verfall. |
| `MAX_STARS` (Hard-Cap) | `global.gd` | `99` | 50–999 | Maximaler Sternwert. |
| `MINIGAME_WINNER_COINS` | `global.gd` | `10` | 5–20 | Munz-Belohnung 1. Platz. |
| `MINIGAME_2ND_COINS` | `global.gd` | `5` | 2–10 | Munz-Belohnung 2. Platz. |
| `MINIGAME_3RD_COINS` | `global.gd` | `3` | 1–5 | Munz-Belohnung 3. Platz. |
| `BOARD_FIELDS` | Board-Plugin | `40` | 30–60 | Felder pro Board. Mehr Felder = langere Bewegungen. |
| `MAX_TURNS` | `global.gd` / Lobby | `10` (varies) | 5–20 | Rundenanzahl. Bestimmt Spieldauer. |

### 7.2 Item-Preis-Tuning

| Item-ID | Standard-Preis | Preis-Bereich | Begrundung |
|---|---|---|---|
| `glueckswuerfel` | 5 | 3–8 | Gunstig, da nur ein einmaliger garantierter Wert. |
| `schutzschild` | 6 | 4–10 | Mittlerer Preis, sehr nutzlich fur defensive Spieler. |
| `muenzmagnet` | 7 | 5–12 | Teurer, da Effekt uber 3 Zuge wirkt und kumulativ Munzen bringt. |
| `teleporter` | 4 | 2–8 | Gunstig, da die zufallige Position auch ein Nachteil sein kann. |
| `diebhandschuh` | 8 | 5–15 | Teuer, da aggressiv und spielentscheidend (kann Item des Gegners klauen). |

### 7.3 Board-Daten-Tuning

| Parameter | Ort | Standard | Bereich | Beschreibung |
|---|---|---|---|---|
| `star_shop_count` | Board-Plugin | 3 | 2–4 | Anzahl Sternen-Shops. Mehr = mehr Kaufgelegenheiten. |
| `event_field_count` | Board-Plugin | 6 | 3–8 | Anzahl Event-Felder. Mehr = mehr Zufall. |
| `coin_bonus_base` | Board-Plugin | 5 | 3–8 | Basis-Munz-Bonus auf COIN_BONUS-Feldern. |
| `event_pool_size` | Board-Plugin | 4 | 3–6 | Event-Vielfalt pro Feld. |

### 7.4 Speicher-Platz-Budget

| Datei | Typische Grosse | Maximum | Beschreibung |
|---|---|---|---|
| `data.cfg` | ~2 KB | ~10 KB | Einstellungen + Statistiken |
| `savegame_*.sav` | ~5 KB | ~20 KB | Ein Spielstand |
| `*.json` (Plugin-Manifeste) | ~1 KB pro Datei | ~3 KB | Wird beim Laden geparst |

---

## 8. Acceptance Criteria

### 8.1 PlayerData

- [ ] **AC-DS-001:** `PlayerData.id` ist einzigartig innerhalb einer Spiel-Session (1–8). Keine zwei Spieler haben dieselbe ID.
- [ ] **AC-DS-002:** `PlayerData.name` ist maximal 16 Zeichen lang. HTML/BBcode-Tags werden entfernt.
- [ ] **AC-DS-003:** `PlayerData.character_id` ist einer der 8 Arenians und innerhalb einer Session einzigartig (First-Come-First-Served).
- [ ] **AC-DS-004:** `PlayerData.coins` ist niemals negativ und niemals grosser als 99.
- [ ] **AC-DS-005:** `PlayerData.stars` ist niemals negativ und niemals grosser als 99.
- [ ] **AC-DS-006:** `PlayerData.field_index` ist immer im Bereich 0–39.
- [ ] **AC-DS-007:** `PlayerData.items` enthalt maximal 3 Eintrage. Alle Eintrage sind gultige Item-IDs.
- [ ] **AC-DS-008:** `PlayerData.color` ist ein gultiger Hex-Color-String (#RRGGBB) und fur jeden Spieler unterscheidbar.
- [ ] **AC-DS-009:** `PlayerData.shield_active` schutzt genau einmal vor einem negativen Effekt und wird danach false.
- [ ] **AC-DS-010:** `PlayerData.coin_magnet_turns` dekrementiert sich korrekt bei jedem eigenen Zug.

### 8.2 BoardData und FieldData

- [ ] **AC-DS-011:** `BoardData.fields` enthalt exakt BOARD_FIELDS Felder (Standard: 40).
- [ ] **AC-DS-012:** Jedes `FieldData.next_indices` Array enthalt 1–3 gultige Feld-Indizes (0–39, nicht self).
- [ ] **AC-DS-013:** next/prev-Konsistenz ist gewahrleistet: A.next enthalt B → B.prev enthalt A.
- [ ] **AC-DS-014:** `FieldData.type` ist einer der 7 definierten Typen (START, STAR_SHOP, ITEM_SHOP, EVENT, LUCK, COIN_BONUS, MINIGAME).
- [ ] **AC-DS-015:** `FieldData.event_pool` ist nur fur Typ EVENT mit Eintragen gefullt. Andere Typen haben leeres Array.
- [ ] **AC-DS-016:** `FieldData.coin_bonus_value` ist nur fur Typ COIN_BONUS grosser als 0. Andere Typen haben 0.
- [ ] **AC-DS-017:** `FieldData.branch_labels` hat dieselbe Lange wie `next_indices` (bei Abzweigungen) oder ist leer (bei linearem Pfad).
- [ ] **AC-DS-018:** `BoardData.active_star_shop_index` ist immer einer der Werte aus `star_shop_positions`.

### 8.3 Plugin-Manifeste

- [ ] **AC-DS-019:** Jedes Minispiel-Plugin enthalt eine gultige `minigame.json` mit allen Pflichtfeldern.
- [ ] **AC-DS-020:** Jedes Item-Plugin enthalt gultige `item_definition.json` mit `item_id`, `price`, `effect_type`.
- [ ] **AC-DS-021:** Jedes Charakter-Plugin enthalt eine gultige `character.json` mit allen Pflichtfeldern (inkl. 6 Animationen).
- [ ] **AC-DS-022:** Plugin-Manifest-ID (`item_id`, `minigame_id`, `character.json:id`) entspricht dem Plugin-Ordnernamen.

### 8.4 Netzwerk-Nachrichten

- [ ] **AC-DS-023:** `PlayerAction.type` ist einer der 6 definierten Typen. Server validiert dies.
- [ ] **AC-DS-024:** `PlayerAction.data` ist immer ein Dictionary (niemals null).
- [ ] **AC-DS-025:** `ServerUpdate` enthalt keine Godot-Objekte — nur primitive Typen und Dictionaries.
- [ ] **AC-DS-026:** `MinigameResult.rankings` ist nach `placement` sortiert (1 zuerst).
- [ ] **AC-DS-027:** `MinigameResult.coin_rewards` summiert sich nicht uber die definierten Maxima (max 10 pro Spieler aus Minispiel).
- [ ] **AC-DS-028:** `GameOver.rankings` enthalt alle 8 Spieler, sortiert nach `total_stars` absteigend.

### 8.5 Speicherung

- [ ] **AC-DS-029:** `data.cfg` enthalt alle Sektionen: `[settings]`, `[statistics]`, `[unlocks]`, `[controls_p1]`, `[controls_p2]`.
- [ ] **AC-DS-030:** Statistiken werden nach jedem Spiel automatisch aktualisiert (nicht nur bei manuellem Speichern).
- [ ] **AC-DS-031:** SaveGame-Dateien sind nicht grosser als 20 KB (gemessen mit 8 Spielern, Board mit 40 Feldern).
- [ ] **AC-DS-032:** Laden eines SaveGames aus einer inkompatiblen Version zeigt eine verstandliche Fehlermeldung und bricht nicht ab.

### 8.6 Validierung (Server-seitig)

- [ ] **AC-DS-033:** Server validiert alle eingehenden `PlayerAction` Dictionaries vor der Ausfuhrung.
- [ ] **AC-DS-034:** PlayerData-Validierung blockt ungultige Werte (negative Munzen, ungultige Position, falsche Item-IDs).
- [ ] **AC-DS-035:** BoardData-Validierung blockt inkonsistente next/prev-Verweise.
- [ ] **AC-DS-036:** Feldtyp-Verteilung wird bei jedem Board-Ladevorgang validiert (Pflicht-Felder vorhanden).

---

> **Nachste Datei:** `technical-performance.md` — Performance-Ziele und Optimierung
> **Referenz:** `technical-architecture.md` — Gesamtarchitektur
> **Referenz:** `technical-multiplayer.md` — Multiplayer-Architektur
> **Referenz:** `technical-fork-strategy.md` — Fork-Strategie
> **Referenz:** `systems-index.md` — Systemzerlegung
