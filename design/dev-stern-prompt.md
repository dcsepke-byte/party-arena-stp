# CCGS Party Arena — DEV: Stern-Mechanik (Milestone 2)

Du bist das Claude Code Game Studios Team. Milestone 1 (Feldtypen-Migration)
ist fertig und verifiziert. Jetzt kommt Milestone 2: die Stern-Mechanik.

## Kontext
- **Projekt:** /opt/data/SuperTuxParty (Godot 4.2, harter Fork von Super Tux Party)
- **Game Bible:** design/gdd/star-economy.md (AUTORITÄT für dieses Milestone)
- **Feldtypen:** bereits migriert (node.gd hat FELD_TYP: START, STERN_SHOP, ITEM_SHOP,
  EREIGNIS, GLUECK_PECH, MUENZ_BONUS, MINISPIEL)
- **Bestehender Shop-Code:** common/scenes/board_logic/controller/shop.gd, shop_item.gd
- **Bestehendes Board:** common/scenes/board_logic/node/node.gd (hat noch `cake`-Logik
  von STP — "Cake" war STPs Stern-Äquivalent, muss zu "Stern"/Star migriert werden)
- **Engine:** Godot 4.2, Import: `/opt/data/godot/Godot_v4.7.1-stable_linux.x86_64 --headless --import`

## DEIN MILESTONE: Stern-Mechanik (aus design/gdd/star-economy.md)

Die Stern-Mechanik aus der Game Bible umsetzen:

1. **Sternen-Statue (aktiv/inaktiv):** Zu jedem Zeitpunkt ist genau EIN Sternen-Shop-Feld
   das aktive (Statue steht dort). Die übrigen sind inaktiv (kein Kauf möglich).
   - Startposition: per Gleichverteilung auf eines der Sternen-Shop-Felder gewürfelt.
   - Position ist für alle Spieler sichtbar.

2. **Stern-Kauf:** Ein Stern kostet exakt 20 Münzen.
   - Nur wer auf dem AKTIVEN Sternen-Shop-Feld steht, darf kaufen.
   - Höchstens 1 Stern-Kauf pro Spieler und Runde.
   - Nach dem Kauf WANDERT die Statue auf ein anderes Sternen-Shop-Feld.

3. **Statue wandert nach Kauf:** Nach einem Kauf zieht die Statue auf ein anderes
   Sternen-Shop-Feld (nicht das aktuelle). Sonderfall: wenn alle anderen Sternen-Shop-Felder
   besetzt sind, bleibt sie (oder zieht auf das nächste freie).

4. **Anti-Regel:** Sterne können NICHT gestohlen oder durch Items manipuliert werden.

5. **Migriere die STP-"Cake"-Logik** in node.gd zu "Stern"/"Star" (Rebranding).

## Aufgaben (Reihenfolge, verifizieren nach jedem)

1. **Analysiere** den bestehenden Shop-Code (shop.gd, shop_item.gd) und die Cake-Logik
   in node.gd. Verstehe, wie STP den Stern-Kauf abwickelt.
2. **Implementiere die Sternen-Statue** (aktiv/inaktiv) gemäß star-economy.md.
3. **Implementiere den Stern-Kauf** (20 Münzen, nur auf aktivem Feld, 1 pro Runde).
4. **Implementiere die Statuen-Wanderung** nach Kauf.
5. **Migriere Cake → Stern** (Rebranding, keine "Cake"-Strings mehr).
6. **Verifiziere:**
   - Godot importiert ohne neue Fehler: `/opt/data/godot/Godot_v4.7.1-stable_linux.x86_64 --headless --import`
   - Schreibe einen Test (Python, wie in Milestone 1) der die Stern-Logik prüft:
     - Statue startet auf einem Sternen-Shop-Feld
     - Kauf nur mit 20 Münzen möglich
     - Statue wandert nach Kauf auf anderes Feld
7. **Commit** mit beschreibender Nachricht.

## WICHTIG
- Arbeite NUR an diesem Milestone. Kein Scope-Creep.
- **Definition of Done:**
  - [ ] Sternen-Statue aktiv/inaktiv implementiert
  - [ ] Stern-Kauf (20 Münzen, 1 pro Runde) implementiert
  - [ ] Statuen-Wanderung nach Kauf implementiert
  - [ ] Anti-Regel (kein Diebstahl) respektiert
  - [ ] Cake → Stern migriert (keine "Cake"-Strings in geänderten Dateien)
  - [ ] Godot importiert ohne neue Fehler
  - [ ] Stern-Logik-Test existiert und ist grün
  - [ ] Commit gemacht
- Wenn nicht ALLE Punkte zutreffen → NICHT fertig melden, weiterarbeiten.
- **Verifizieren aus FRISCHER SHELL.**
- Nutze design/gdd/star-economy.md als Design-Autorität. Bei Unklarheit lesen, nicht raten.
- Am Ende: `[BUILD_COMPLETE]` mit genauer Zusammenfassung (was geändert, Test-Ergebnis, Commit-Hash).

## WICHTIG FÜR DIESEN LAUF
- Schreibe JETZT direkt den Code. Kein Plan erstellen und auf Freigabe warten.
- Arbeite durch bis alle 7 Aufgaben fertig sind. Kein Stoppen nach Aufgabe 1.
- Alle Datei-Schreibrechte sind erteilt (Write/Edit in settings.json + --dangerously-skip-permissions).
- **GDScript-Pitfall (aus Milestone 1):** Nutze IMMER explizite Typen (`var x: int = ...`),
  NIE `:=` bei Dictionary-Zugriffen (Variant-Inferenz wird als Fehler behandelt und
  blockiert den Godot-Import). Verifiziere am Ende, dass deine geänderten .gd-Dateien
  ohne Parse-Fehler importieren.
