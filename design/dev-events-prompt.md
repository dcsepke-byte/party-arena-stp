# CCGS Party Arena — DEV: Ereignis-Logik + Abzweigungs-Sonderregeln (Milestone 6c)

Du bist das Claude Code Game Studios Team. Alle Kern-Systeme (Feldtypen, Stern-Mechanik,
Items, Minigames, Charaktere, Boards, Abzweigungs-Logik) sind fertig und verifiziert.
Jetzt kommt die letzte Umsetzung: die Ereignis-Logik und die Abzweigungs-Sonderregeln.

## Kontext
- **Projekt:** /opt/data/SuperTuxParty (Godot 4.2, harter Fork von Super Tux Party)
- **Game Bible:** design/gdd/field-event.md (Ereignis-System AUTORITÄT), die world-*.md
  Kapitel (jede Insel hat ihre Ereignis-Kartei + Abzweigungs-Sonderregeln),
  design/gdd/board-architecture.md
- **Bestehende Boards:** plugins/boards/sonnenstrand/ bis sternenzitadelle/
  (board.gd hat handle_event()-Stub + BRANCHES-Daten + board.json mit event_pool,
  special_rules, branches)
- **Feld-Logik:** common/scenes/board_logic/node/node.gd, controller.gd
- **Engine:** Godot 4.2, Import: `/opt/data/godot/Godot_v4.7.1-stable_linux.x86_64 --headless --import`

## DEIN MILESTONE: Ereignis-Logik + Abzweigungs-Sonderregeln

### Teil A — Ereignis-System (aus field-event.md + den Insel-Kapiteln)

Die EREIGNIS-Felder müssen echte Effekte auslösen. Jede Insel hat eine eigene
Ereignis-Kartei (in world-*.md + board.json event_pool):

1. **Implementiere das Ereignis-System:** Wenn ein Spieler auf einem EREIGNIS-Feld
   landet, wird ein Ereignis aus dem Pool der Insel gezogen und sein Effekt ausgelöst.
2. **Ereignis-Effekte:** Münzen +/-, Items, Bewegung (vor/zurück), Stern-Rabatt, etc.
   gemäß field-event.md.
3. **Fülle handle_event()** in jeder board.gd mit der Insel-spezifischen Ereignis-Kartei
   aus world-*.md (z.B. Sonnenstrand: Quallen-Schwarm, Springflut, Muschel-Suche;
   Zuckerwald: Bonbon-Regen; Mechanik-Stadt: Förderband, Erfindermesse; etc.).

### Teil B — Abzweigungs-Sonderregeln (aus den Insel-Kapiteln)

Jede Insel hat spezielle Abzweigungs-Regeln (in world-*.md + board.json special_rules).
Implementiere die, die es gibt:
- **Sonnenstrand:** gleichwertige Abzweigungen (keine Sonderregel)
- **Zuckerwald / Wolkenwerk / Frostgipfel / Dschungeltempel / Mechanik-Stadt /
  Sternenzitadelle:** ihre jeweiligen Sonderregeln (Floß-Fahrt, Windkanal-Express,
  Eishöhlen-Dunkelheit, Lianen-Express, Rohrpost-Teleport, Kosmische Drift, Geister-Felder...)

Lies die genauen Regeln aus dem jeweiligen world-*.md und implementiere sie in board.gd.

## Aufgaben (Reihenfolge, verifizieren nach jedem)

1. **Analysiere** den handle_event()-Stub + die Ereignis-Kartei + Sonderregeln der Inseln.
2. **Implementiere das Ereignis-System** (Zieh-Mechanik + Effekte aus field-event.md).
3. **Fülle handle_event()** für alle 7 Inseln mit ihren Ereignis-Karteien.
4. **Implementiere die Abzweigungs-Sonderregeln** je Insel.
5. **Verifiziere:**
   - Godot importiert ohne neue Fehler: `/opt/data/godot/Godot_v4.7.1-stable_linux.x86_64 --headless --import`
   - Schreibe einen Test (Python) der prüft:
     - Jede Insel hat eine Ereignis-Kartei (nicht leer)
     - Jedes Ereignis hat einen Effekt (nicht nur Name)
     - Abzweigungs-Sonderregeln sind je Insel definiert
6. **Commit** mit beschreibender Nachricht.

## WICHTIG
- Arbeite NUR an diesen Milestones (Ereignis + Sonderregeln). Kein Scope-Creep.
- **Definition of Done:**
  - [ ] Ereignis-System implementiert (Zieh-Mechanik + Effekte)
  - [ ] handle_event() für alle 7 Inseln gefüllt (Ereignis-Karteien)
  - [ ] Abzweigungs-Sonderregeln je Insel implementiert
  - [ ] Godot importiert ohne neue Fehler
  - [ ] Ereignis-Test existiert und ist grün
  - [ ] Commit gemacht
- Wenn nicht ALLE Punkte zutreffen → NICHT fertig melden, weiterarbeiten.
- **Verifizieren aus FRISCHER SHELL.**
- Nutze design/gdd/field-event.md + die world-*.md als Autorität. Bei Unklarheit lesen, nicht raten.
- Am Ende: `[BUILD_COMPLETE]` mit genauer Zusammenfassung (was geändert, Test-Ergebnis, Commit-Hash).

## WICHTIG FÜR DIESEN LAUF
- Schreibe JETZT direkt den Code. Kein Plan erstellen und auf Freigabe warten.
- Arbeite durch bis alle 6 Aufgaben fertig sind. Kein Stoppen nach Aufgabe 1.
- Alle Datei-Schreibrechte sind erteilt (Write/Edit in settings.json + --dangerously-skip-permissions).
- **GDScript-Pitfall (aus Milestone 1):** Nutze IMMER explizite Typen (`var x: int = ...`),
  NIE `:=` bei Dictionary-Zugriffen. Verifiziere am Ende, dass deine geänderten .gd-Dateien
  ohne Parse-Fehler importieren. Prüfe auch auf doppelte Variablen-Deklarationen (war ein Bug in Milestone 6b).
