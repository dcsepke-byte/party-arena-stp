# CCGS Party Arena — DEV: Minigame-System (Milestone 4)

Du bist das Claude Code Game Studios Team. Milestone 1-3 (Feldtypen, Stern-Mechanik,
Items) sind fertig und verifiziert. Jetzt kommt Milestone 4: das Minigame-System.

## Kontext
- **Projekt:** /opt/data/SuperTuxParty (Godot 4.2, harter Fork von Super Tux Party)
- **Game Bible:** design/gdd/minigame-architecture.md (AUTORITÄT), minigame-categories.md,
  minigame-rewards.md, minigame-template.md
- **Bestehender Minigame-Code:** common/scripts/loader/minigame_loader.gd,
  plugins/minigames/ (boat_rally, bowling, dungeon_parkour, escape_from_lava, forest_run,
  harvest_food, haunted_dreams, hurdle, kernel_compiling, knock_off, memory, ...)
- **Engine:** Godot 4.2, Import: `/opt/data/godot/Godot_v4.7.1-stable_linux.x86_64 --headless --import`

## DEIN MILESTONE: Minigame-System (aus design/gdd/minigame-architecture.md)

### Teil A — Minigame-Framework (Architektur)
1. **Plugin-System:** Jedes Minispiel ist ein Ordner unter `plugins/minigames/` mit genau
   3 Pflichtdateien: `minigame.gd` (erbt von MinigameBase), `minigame.tscn` (Root Node3D),
   `minigame.json` (Metadaten: name, category, Spielerzahl-Bereich, Dauer, Beschreibung).
2. **Lebenszyklus:** COUNTDOWN (3,2,1,LOS) → PLAY (30s hartes Limit) → RESULTS (5s) → REWARDS.
3. **Kamera:** Bis 4 Spieler Split-Screen, ab 5 Vogelperspektive.
4. **Input-Mapping:** 2-8 Spieler gleichzeitig.
5. **Platzierung:** get_results() → Platzierung 1-n, Gleichstände gemittelt.
6. **Sonderfälle:** Disconnects, Zeitüberschreitung, Fehler.

### Teil B — 12 Minispiele (aus minigame-categories.md)
Die 12 geplanten Minispiele in 5 Kategorien bauen (3+3+2+2+2):

**Geschicklichkeit (3):** Münzregen, Balance-Akt, Zielwurf
**Reaktion (3):** ArenaStar sagt, Blitz-Fangen, Knöpfchen-Drücker
**Puzzle/Logik (2):** Gedächtnis-Paar, Orientierungs-Puzzle
**Rechnen/Wort (2):** Münz-Zählen, Wort-Bildung
**Kooperation (2):** Team-Schatzsuche, Gemeinsamer Turm

Jedes Minispiel: Ziel, Siegbedingung, Kernmechanik, Steuerung, Früh-Ende-Regel,
Skalierung 2-8 Spieler, ~30s Dauer.

## Aufgaben (Reihenfolge, verifizieren nach jedem)

1. **Analysiere** den bestehenden Minigame-Code (minigame_loader.gd, ein bestehendes
   Minispiel als Vorlage). Verstehe die STP-Minigame-Schnittstelle.
2. **Implementiere das Minigame-Framework** gemäß minigame-architecture.md (Lebenszyklus,
   Kamera, Input, Platzierung, Sonderfälle).
3. **Implementiere die 12 Minispiele** als Plugins (minigame.gd + minigame.tscn + minigame.json
   je Minispiel) in den 5 Kategorien.
4. **Verifiziere:**
   - Godot importiert ohne neue Fehler: `/opt/data/godot/Godot_v4.7.1-stable_linux.x86_64 --headless --import`
   - Schreibe einen Test (Python, wie in Milestone 1-3) der prüft:
     - Alle 12 Minispiele existieren mit korrekten Kategorien
     - Jedes hat die 3 Pflichtdateien (minigame.gd, minigame.tscn, minigame.json)
     - minigame.json ist valide (name == Ordnername, category korrekt)
5. **Commit** mit beschreibender Nachricht.

## WICHTIG
- Arbeite NUR an diesem Milestone. Kein Scope-Creep.
- **Definition of Done:**
  - [ ] Minigame-Framework implementiert (Lebenszyklus, Kamera, Input, Platzierung)
  - [ ] Alle 12 Minispiele als Plugins mit 3 Pflichtdateien
  - [ ] Kategorien korrekt (3+3+2+2+2)
  - [ ] Godot importiert ohne neue Fehler
  - [ ] Minigame-Test existiert und ist grün
  - [ ] Commit gemacht
- Wenn nicht ALLE Punkte zutreffen → NICHT fertig melden, weiterarbeiten.
- **Verifizieren aus FRISCHER SHELL.**
- Nutze design/gdd/minigame-architecture.md + minigame-categories.md als Design-Autorität.
  Bei Unklarheit lesen, nicht raten.
- Am Ende: `[BUILD_COMPLETE]` mit genauer Zusammenfassung (was geändert, Test-Ergebnis, Commit-Hash).

## WICHTIG FÜR DIESEN LAUF
- Schreibe JETZT direkt den Code. Kein Plan erstellen und auf Freigabe warten.
- Arbeite durch bis alle 5 Aufgaben fertig sind. Kein Stoppen nach Aufgabe 1.
- Alle Datei-Schreibrechte sind erteilt (Write/Edit in settings.json + --dangerously-skip-permissions).
- **GDScript-Pitfall (aus Milestone 1):** Nutze IMMER explizite Typen (`var x: int = ...`),
  NIE `:=` bei Dictionary-Zugriffen (Variant-Inferenz wird als Fehler behandelt und
  blockiert den Godot-Import). Verifiziere am Ende, dass deine geänderten .gd-Dateien
  ohne Parse-Fehler importieren.
- **Realistisch bleiben:** 12 komplette Minispiele sind viel. Priorisiere: Framework zuerst,
  dann so viele Minispiele wie sauber machbar. Lieber 8 saubere als 12 halbfertige.
  Jedes Minispiel muss die 3 Pflichtdateien haben und importieren.
