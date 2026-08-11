# CCGS Party Arena — DEV: Boards (Milestone 6, letzter)

Du bist das Claude Code Game Studios Team. Milestone 1-5 (Feldtypen, Stern-Mechanik,
Items, Minigames, Charaktere) sind fertig und verifiziert. Jetzt kommt der letzte
Milestone: die 7 Insel-Boards.

## Kontext
- **Projekt:** /opt/data/SuperTuxParty (Godot 4.2, harter Fork von Super Tux Party)
- **Game Bible:** design/gdd/world-overview.md (AUTORITÄT, Dach-Spezifikation),
  world-sonnenstrand.md bis world-sternenzitadelle.md (jede Insel einzeln)
- **Bestehende Boards:** plugins/boards/KDEValley (STP-Legacy, wird abgelöst),
  plugins/boards/test (Test-Board aus Milestone 1)
- **Board-Loader:** common/scripts/loader/board_loader.gd (entdeckt board.tscn in
  jedem Unterordner von plugins/boards/)
- **Feldtypen:** bereits migriert (FELD_TYP: START, STERN_SHOP, ITEM_SHOP, EREIGNIS,
  GLUECK_PECH, MUENZ_BONUS, MINISPIEL)
- **Engine:** Godot 4.2, Import: `/opt/data/godot/Godot_v4.7.1-stable_linux.x86_64 --headless --import`

## DEIN MILESTONE: Die 7 Insel-Boards (aus design/gdd/world-overview.md)

Die 7 Inseln als Board-Plugins anlegen. Jede Insel ist ein Ordner unter
`plugins/boards/` mit `board.tscn` + `board.gd` + `board.json`:

| # | Insel | Schwierigkeit | Farben |
|---|---|---|---|
| 1 | Sonnenstrand | ★☆☆☆☆ | Türkis, Sandgelb, Korallenrot |
| 2 | Zuckerwald | ★★☆☆☆ | Rosa, Schokobraun, Mintgrün |
| 3 | Wolkenwerk | ★★★☆☆ | Hellblau, Weiß, Regenbogen |
| 4 | Frostgipfel | ★★★☆☆ | Eisblau, Weiß, Violett |
| 5 | Dschungeltempel | ★★★★☆ | Dschungelgrün, Gold, Braun |
| 6 | Mechanik-Stadt | ★★★★☆ | Silber, Orange, Gelb |
| 7 | Sternenzitadelle | ★★★★★ | Gold, Tiefblau, Magenta |

## Jede Insel (aus world-overview.md + dem jeweiligen world-*.md)

1. **40-Felder-Board** — Hauptpfad 32 Felder + 2 Abzweigungen je 4 Felder.
2. **Feld-Verteilung** gemäß Game Bible (START 1, STERN_SHOP 2-3, ITEM_SHOP 2,
   EREIGNIS 5-6, GLUECK_PECH 3, MUENZ_BONUS 4, MINISPIEL Rest).
3. **board.json** — Metadaten: name, thema, schwierigkeit, farben, musik.
4. **board.gd** — erbt von der Board-Basisklasse, definiert das 40-Felder-Layout
   (REFERENCE_LAYOUT wie im Test-Board aus Milestone 1), Feld-Effekte.
5. **board.tscn** — Root-Szene mit board.gd.
6. **Themen-Deko** — einfache 3D-Platzhalter (Kugeln/Boxen in Insel-Farben) als
   visuelle Identität (Danny zeichnet später echte Assets).

## Aufgaben (Reihenfolge, verifizieren nach jedem)

1. **Analysiere** das Test-Board aus Milestone 1 (plugins/boards/test/board.gd) als
   Vorlage — es hat bereits das korrekte 40-Felder-REFERENCE_LAYOUT.
2. **Erstelle die 7 Insel-Boards** (board.tscn + board.gd + board.json je Insel) mit
   korrekter Feld-Verteilung und Insel-Farben.
3. **Integriere in den BoardLoader** (automatisch, da er board.tscn entdeckt).
4. **Verifiziere:**
   - Godot importiert ohne neue Fehler: `/opt/data/godot/Godot_v4.7.1-stable_linux.x86_64 --headless --import`
   - Schreibe einen Test (Python, wie in Milestone 1-5) der prüft:
     - Alle 7 Insel-Boards existieren (board.tscn + board.gd + board.json)
     - Jedes hat die korrekte Feld-Verteilung (40 Felder)
     - board.json ist valide (name, thema, schwierigkeit, farben)
5. **Commit** mit beschreibender Nachricht.

## WICHTIG
- Arbeite NUR an diesem Milestone. Kein Scope-Creep.
- **Definition of Done:**
  - [ ] 7 Insel-Boards erstellt (board.tscn + board.gd + board.json)
  - [ ] Jedes hat korrekte 40-Felder-Verteilung
  - [ ] Insel-Farben/Themen korrekt
  - [ ] BoardLoader integriert die 7 Inseln
  - [ ] Godot importiert ohne neue Fehler
  - [ ] Board-Test existiert und ist grün
  - [ ] Commit gemacht
- Wenn nicht ALLE Punkte zutreffen → NICHT fertig melden, weiterarbeiten.
- **Verifizieren aus FRISCHER SHELL.**
- Nutze design/gdd/world-overview.md als Dach-Autorität + das jeweilige world-*.md.
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
- **Realistisch bleiben:** Die 3D-Deko ist Platzhalter (Danny zeichnet später).
  Fokus auf saubere Board-Struktur + korrekte Feld-Verteilung + Loader-Integration.
