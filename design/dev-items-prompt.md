# CCGS Party Arena — DEV: Item-System (Milestone 3)

Du bist das Claude Code Game Studios Team. Milestone 1 (Feldtypen) und Milestone 2
(Stern-Mechanik) sind fertig und verifiziert. Jetzt kommt Milestone 3: das Item-System.

## Kontext
- **Projekt:** /opt/data/SuperTuxParty (Godot 4.2, harter Fork von Super Tux Party)
- **Game Bible:** design/gdd/item-system.md (AUTORITÄT), item-luckydice.md, item-teleporter.md,
  item-shield.md, item-coinmagnet.md, item-thiefglove.md
- **Bestehender Item-Code:** common/scenes/board_logic/controller/itemselection.gd,
  shop_item.gd, common/scripts/loader/item_loader.gd, plugins/items/ (cookie_steal_trap,
  dice, lucky_seven, item.gd)
- **Engine:** Godot 4.2, Import: `/opt/data/godot/Godot_v4.7.1-stable_linux.x86_64 --headless --import`

## DEIN MILESTONE: Item-System (aus design/gdd/item-system.md)

Die 5 Party-Arena-Items aus der Game Bible umsetzen:

| Item | Preis | Effekt | Typ |
|---|---|---|---|
| **Glücks-Würfel** | 5 | Würfelt 1-10 statt 1-6 | immediate |
| **Stern-Teleporter** | 8 | Bewegt sich zum Sternen-Shop | immediate |
| **Schutzschild** | 6 | Blockt 1 negativen Effekt | passive |
| **Münz-Magnet** | 4 | +3 Münzen bei nächstem Münz-Feld | delayed |
| **Dieb-Handschuh** | 10 | Stiehlt Gegner 5 Münzen | immediate |

## Aufgaben (Reihenfolge, verifizieren nach jedem)

1. **Analysiere** den bestehenden Item-Code (item_loader.gd, itemselection.gd, shop_item.gd,
   plugins/items/). Verstehe, wie STP Items lädt und abwickelt.
2. **Implementiere das Item-Framework** gemäß item-system.md: `item_price`, Effekt-Typen
   (immediate/delayed/passive), Aktivierung, Verbrauch.
3. **Implementiere die 5 Items** als Plugins (Glücks-Würfel, Stern-Teleporter, Schutzschild,
   Münz-Magnet, Dieb-Handschuh) mit korrekten Preisen und Effekten.
4. **Integriere Items in den Shop** (Item-Shop-Feld, Kauf mit Münzen).
5. **Verifiziere:**
   - Godot importiert ohne neue Fehler: `/opt/data/godot/Godot_v4.7.1-stable_linux.x86_64 --headless --import`
   - Schreibe einen Test (Python, wie in Milestone 1/2) der die Item-Logik prüft:
     - Alle 5 Items existieren mit korrekten Preisen (5/8/6/4/10)
     - Effekt-Typen korrekt (immediate/delayed/passive)
     - Kauf reduziert Münzen korrekt
6. **Commit** mit beschreibender Nachricht.

## WICHTIG
- Arbeite NUR an diesem Milestone. Kein Scope-Creep.
- **Definition of Done:**
  - [ ] Item-Framework implementiert (Preis, Effekt-Typen, Aktivierung, Verbrauch)
  - [ ] Alle 5 Items als Plugins mit korrekten Preisen/Effekten
  - [ ] Items im Shop kaufbar (Münz-Abzug korrekt)
  - [ ] Godot importiert ohne neue Fehler
  - [ ] Item-Test existiert und ist grün
  - [ ] Commit gemacht
- Wenn nicht ALLE Punkte zutreffen → NICHT fertig melden, weiterarbeiten.
- **Verifizieren aus FRISCHER SHELL.**
- Nutze design/gdd/item-system.md als Design-Autorität. Bei Unklarheit lesen, nicht raten.
- Am Ende: `[BUILD_COMPLETE]` mit genauer Zusammenfassung (was geändert, Test-Ergebnis, Commit-Hash).

## WICHTIG FÜR DIESEN LAUF
- Schreibe JETZT direkt den Code. Kein Plan erstellen und auf Freigabe warten.
- Arbeite durch bis alle 6 Aufgaben fertig sind. Kein Stoppen nach Aufgabe 1.
- Alle Datei-Schreibrechte sind erteilt (Write/Edit in settings.json + --dangerously-skip-permissions).
- **GDScript-Pitfall (aus Milestone 1):** Nutze IMMER explizite Typen (`var x: int = ...`),
  NIE `:=` bei Dictionary-Zugriffen (Variant-Inferenz wird als Fehler behandelt und
  blockiert den Godot-Import). Verifiziere am Ende, dass deine geänderten .gd-Dateien
  ohne Parse-Fehler importieren.
