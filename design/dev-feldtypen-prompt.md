# CCGS Party Arena — DEV: Feldtypen-Migration (erster Milestone)

Du bist das Claude Code Game Studios Team. Die Game Bible ist fertig und von
Danny freigegeben (design/gdd/, 64 Kapitel). Jetzt beginnt die Umsetzung.

## Kontext
- **Projekt:** /opt/data/SuperTuxParty (Godot 4.2, harter Fork von Super Tux Party)
- **Game Bible:** design/gdd/ (besonders wichtig: board-architecture.md, field-start.md,
  field-star-shop.md, field-item-shop.md, field-event.md, field-luck.md,
  field-coin-bonus.md, field-minigame.md)
- **Fork-Strategie:** design/gdd/technical-fork-strategy.md (4 Kategorien: A=übernehmen,
  B=modifizieren, C=neu schreiben, D=komplett neu)
- **Engine:** Godot 4.2, Start: `godot --headless --import` zum Importieren
- **Bestehendes Board-System:** `common/scenes/board_logic/node/node.gd` (Feldtypen),
  `common/scenes/board_logic/player_board/player_board.gd`, `common/scripts/loader/board_loader.gd`

## DEIN ERSTER MILESTONE: Feldtypen-Migration (kritischste Lücke aus Session 1)

STP hat aktuell die Feldtypen BLUE/RED/GREEN/YELLOW/SHOP/NOLOK/GNU (GNU ist
Tux-IP und muss weg). Party Arena braucht laut Game Bible diese 7 neuen
Feldtypen auf dem 40-Felder-Board:

1. **Start** (1 Feld) — alle Spieler beginnen hier
2. **Sternen-Shop** (2-3 Felder) — Stern kaufen (20 Münzen), wandert danach
3. **Item-Shop** (2 Felder) — Item kaufen
4. **Ereignis** (5-6 Felder) — Zufalls-Effekt (gut oder schlecht)
5. **Glück/Pech** (3 Felder) — Münzen gewinnen/verlieren
6. **Münz-Bonus** (4 Felder) — Bonus-Münzen
7. **Mini-Spiel** (Rest) — normales Feld, löst das nächste Minispiel aus

## Aufgaben (genau diese Reihenfolge, verifizieren nach jedem)

1. **Analysiere** den bestehenden Feldtypen-Code in `node.gd` und der Board-Erweiterung.
   Identifiziere, wo die Enum/DEFS für BLUE/RED/GREEN/YELLOW/SHOP/NOLOK/GNU definiert
   sind und wo sie benutzt werden.
2. **Erstelle ein neues Feldtypen-System** gemäß design/gdd/board-architecture.md.
   Ersetze die STP-Feldtypen durch die 7 Party-Arena-Feldtypen. GNU und NOLOK
   entfernen (Tux-IP). Behalte STP-Logik wo sinnvoll (Kategorie B).
3. **Aktualisiere das bestehende Test-Board** (`plugins/boards/test/board.gd`) auf den
   neuen 40-Felder-Pfad mit der korrekten Feld-Verteilung aus der Game Bible.
4. **Verifiziere:** Godot importiert ohne Fehler.
   ```bash
   cd /opt/data/SuperTuxParty
   /opt/data/godot/Godot_v4.7.1-stable_linux.x86_64 --headless --import 2>&1 | tail -20
   ```
   Es darf KEINE Fehler geben. Schreibe einen Test, der die Feld-Verteilung prüft
   (Anzahl Start/Sternen-Shop/Item-Shop/Ereignis/Glück/Münz-Bonus/Mini-Spiel stimmt).
5. **Commit** mit beschreibender Nachricht.

## WICHTIG
- Arbeite NUR an diesem Milestone. Kein Scope-Creep auf Charaktere/Minispiele/Boards.
- **Definition of Done für diesen Milestone:**
  - [ ] Feldtypen-Migration komplett (7 neue Typen, GNU/NOLOK entfernt)
  - [ ] Test-Board hat korrekte Feld-Verteilung (40 Felder)
  - [ ] Godot importiert ohne Fehler (`--headless --import` = 0 Fehler)
  - [ ] Feld-Verteilungs-Test existiert und ist grün
  - [ ] Commit gemacht
- Wenn nicht ALLE Punkte zutreffen → NICHT fertig melden, weiterarbeiten.
- **Verifizieren aus FRISCHER SHELL**, nicht aus deiner Session.
- Nutze NUR die Game Bible als Design-Autorität. Bei Unklarheit: design/gdd/board-architecture.md
  lesen. Nicht raten.
- Am Ende: melde `[BUILD_COMPLETE]` mit genauer Zusammenfassung (was geändert,
  Test-Ergebnis, Commit-Hash).

## WICHTIG FÜR DIESEN LAUF
- Schreibe JETZT direkt den Code. Kein Plan erstellen und auf Freigabe warten.
- Arbeite durch bis alle 5 Aufgaben fertig sind. Kein Stoppen nach Aufgabe 1.
- Alle Datei-Schreibrechte sind erteilt (Write/Edit in settings.json + --dangerously-skip-permissions).
