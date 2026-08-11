# CCGS Party Arena — DEV: Abzweigungs-Logik (Milestone 6b)

Du bist das Claude Code Game Studios Team. Milestone 6 (7 Insel-Boards) ist fertig.
Jetzt kommt die ABZWEIGUNGS-LOGIK — die Karten sind aktuell nur lineare 40-Felder-
Schleifen, sollen aber echte zusammenhängende Karten mit Abzweigungen sein (Mario-Party-Stil).

## Kontext
- **Projekt:** /opt/data/SuperTuxParty (Godot 4.2, harter Fork von Super Tux Party)
- **Game Bible:** design/gdd/world-overview.md Sektion 3.8-3.9 (AUTORITÄT für Abzweigungen),
  world-sonnenstrand.md bis world-sternenzitadelle.md (jede Insel: Einstieg/Ausstieg/Δ)
- **Bestehende Boards:** plugins/boards/sonnenstrand/ bis sternenzitadelle/
  (jede hat board.gd mit REFERENCE_LAYOUT + board.json mit branches-Daten)
- **Feld-Logik:** common/scenes/board_logic/node/node.gd, player_board.gd, controller.gd
- **Engine:** Godot 4.2, Import: `/opt/data/godot/Godot_v4.7.1-stable_linux.x86_64 --headless --import`

## DEIN MILESTONE: Abzweigungs-Logik (aus world-overview.md 3.8-3.9)

Die Karten von linearen Schleifen zu echten Karten mit Abzweigungen machen.

### Struktur (aus world-overview.md 3.8)
- **Hauptpfad:** 32 Felder (1-32). Feld 1 = Start, Feld 32 → Loop zurück zu Feld 1.
- **2 Abzweigungen:** Je 4 Felder (A = 33-36, B = 37-40). Jede verbindet zwei Hauptpfad-
  Felder: Einstieg X, Ausstieg Y.
- **Feld-Verkettung:** Jedes Feld kennt genau einen Folge-Nachbarn (Loop) PLUS ggf.
  einen Abzweig-Nachbarn an den Junction-Feldern. Azyklisch mit genau einer Schleife.

### Wahlmechanik (aus world-overview.md 3.9)
1. **Junction-Wahl:** Wer auf einem Junction-Feld X landet, wählt zwischen Hauptpfad
   und Abzweigung. Pfadwahl-Pfeil in der UI.
2. **Passieren ohne Halt:** Passiert ein Spieler das Junction-Feld ohne anzuhalten,
   wird automatisch der Hauptpfad gewählt.
3. **Längenbilanz:** Summe aus Abzweigungs- + Hauptpfad-Feldern bleibt 40.

### Die 7 Inseln (Einstieg/Ausstieg/Δ aus den Insel-Kapiteln)
Lies die Einstieg/Ausstieg/Δ-Werte für jede Insel aus dem jeweiligen world-*.md
(und aus board.json branches: name, entry, exit, delta, fields).

## Aufgaben (Reihenfolge, verifizieren nach jedem)

1. **Analysiere** die bestehende Feld-Verkettung (node.gd, player_board.gd) — wie
   bestimmt aktuell ein Feld seinen Nachfolger? Wo muss Branch-Logik eingreifen?
2. **Implementiere die Abzweigungs-Logik:** Jedes Board kennt seine 2 Abzweigungen
   (Einstieg/Ausstieg/Δ). An Junction-Feldern wählt der Spieler Hauptpfad oder Abzweigung.
   - Füge die Junction-Entscheidung in den Bewegungs-Flow ein.
   - Beim Ausstieg aus einer Abzweigung geht es zurück zum Hauptpfad an Ausstieg Y.
3. **Integriere die board.json-branches** in board.gd (nicht nur dokumentieren, sondern
   die Felder 33-40 als echte Abzweigungs-Felder verdrahten).
4. **Verifiziere:**
   - Godot importiert ohne neue Fehler: `/opt/data/godot/Godot_v4.7.1-stable_linux.x86_64 --headless --import`
   - Schreibe einen Test (Python) der prüft:
     - Jede Insel hat 2 Abzweigungen mit gültigem Einstieg/Ausstieg (1-32)
     - Feld-Verkettung: Hauptpfad 1→32→1 (Schleife), Abzweigungen verbinden X→Y
     - Längenbilanz: 32 + 2×4 = 40 pro Insel
5. **Commit** mit beschreibender Nachricht.

## WICHTIG
- Arbeite NUR an diesem Milestone. Kein Scope-Creep.
- **Definition of Done:**
  - [ ] Abzweigungs-Logik implementiert (Junction-Wahl, Hauptpfad vs. Abzweigung)
  - [ ] Alle 7 Inseln: Einstieg/Ausstieg/Δ korrekt aus board.json verdrahtet
  - [ ] Feld-Verkettung korrekt (Hauptpfad 1-32-Schleife + 2×4 Abzweigungen)
  - [ ] Längenbilanz 40 pro Insel
  - [ ] Godot importiert ohne neue Fehler
  - [ ] Abzweigungs-Test existiert und ist grün
  - [ ] Commit gemacht
- Wenn nicht ALLE Punkte zutreffen → NICHT fertig melden, weiterarbeiten.
- **Verifizieren aus FRISCHER SHELL.**
- Nutze design/gdd/world-overview.md Sektion 3.8-3.9 als Autorität. Bei Unklarheit lesen, nicht raten.
- Am Ende: `[BUILD_COMPLETE]` mit genauer Zusammenfassung (was geändert, Test-Ergebnis, Commit-Hash).

## WICHTIG FÜR DIESEN LAUF
- Schreibe JETZT direkt den Code. Kein Plan erstellen und auf Freigabe warten.
- Arbeite durch bis alle 5 Aufgaben fertig sind. Kein Stoppen nach Aufgabe 1.
- Alle Datei-Schreibrechte sind erteilt (Write/Edit in settings.json + --dangerously-skip-permissions).
- **GDScript-Pitfall (aus Milestone 1):** Nutze IMMER explizite Typen (`var x: int = ...`),
  NIE `:=` bei Dictionary-Zugriffen. Verifiziere am Ende, dass deine geänderten .gd-Dateien
  ohne Parse-Fehler importieren.
