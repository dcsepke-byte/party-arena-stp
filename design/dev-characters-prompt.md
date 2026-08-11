# CCGS Party Arena — DEV: Charaktere (Milestone 5)

Du bist das Claude Code Game Studios Team. Milestone 1-4 (Feldtypen, Stern-Mechanik,
Items, Minigames) sind fertig und verifiziert. Jetzt kommt Milestone 5: die 8 Arenians.

## Kontext
- **Projekt:** /opt/data/SuperTuxParty (Godot 4.2, harter Fork von Super Tux Party)
- **Game Bible:** design/gdd/characters-overview.md (AUTORITÄT), character-brix.md bis
  character-momo.md
- **Bestehender Charakter-Code:** common/scripts/character.gd (Basisklasse),
  common/scripts/loader/character_loader.gd, plugins/characters/ (Tux, Godette, Beastie,
  Green Tux — das sind Tux-IP, müssen durch die 8 Arenians ersetzt werden)
- **Engine:** Godot 4.2, Import: `/opt/data/godot/Godot_v4.7.1-stable_linux.x86_64 --headless --import`

## DEIN MILESTONE: Die 8 Arenians (aus design/gdd/characters-overview.md)

Die 8 Eigen-IP-Arenians als Charakter-Plugins anlegen. Jeder Charakter lebt in einem
eigenen Ordner unter `plugins/characters/`, wird vom CharacterLoader entdeckt und
nutzt die Basisklasse `character.gd`.

| # | Name | Typ | Heimat | Persönlichkeit | Farbe |
|---|---|---|---|---|---|
| 1 | Brix | Stein-Golem | Mechanik-Stadt | mutig, tollpatschig | Orange #ff6a00 |
| 2 | Nixie | Axolotl | Sonnenstrand | neugierig, wasseraffin | Türkis #00f0ff |
| 3 | Pip | Flieg. Eichhörnchen | Wolkenwerk | schnell, frech | Gelb #ffd34e |
| 4 | Koko | Panda | Zuckerwald | freundlich, stark | Rosa #ff4d6d |
| 5 | Tiko | Vogel (Tukan) | Dschungeltempel | chaotisch, lustig | Grün #2bffb9 |
| 6 | Bolt | Roboter | Mechanik-Stadt | logisch, präzise | Blau #3a86ff |
| 7 | Bloom | Kaktus | Dschungeltempel | ruhig, humorvoll | Lila #7b2ff7 |
| 8 | Momo | Waschbär | Frostgipfel | clever, trickreich | Pink #ff3cac |

## WICHTIG: 3D-Modelle (GLB) kann der Agent NICHT zeichnen

Die visuellen 3D-Modelle (GLB/Blend) zeichnet Danny später in Blender. Deine Aufgabe
ist die **Struktur, Logik und Metadaten** — nicht die Kunst. Für jedes Minispiel:

1. **Plugin-Ordner** `plugins/characters/<Name>/` mit:
   - `character.tscn` — Root-Szene (Node3D mit character.gd), mit Platzhalter-Mesh
     (z.B. einfache Kapsel/Box in der Charakter-Farbe) als visueller Platzhalter
   - `character.gd` (falls nötig) — erbt von Character, definiert Farbe/Name
   - `character.json` — Metadaten: name, typ, heimat, persönlichkeit, farbe (hex)
   - `icon.png`-Platzhalter (kann ein einfarbiges PNG in der Charakter-Farbe sein)
2. **CharacterLoader-Integration:** Die 8 Arenians werden vom Loader entdeckt.
3. **Tux-IP entfernen:** Die alten Tux/Godette/Beastie/Green Tux-Charaktere werden
   aus dem Auswahl-Screen entfernt (nicht unbedingt gelöscht, aber nicht mehr geladen).

## Aufgaben (Reihenfolge, verifizieren nach jedem)

1. **Analysiere** den bestehenden Charakter-Code (character.gd, character_loader.gd,
   ein bestehendes Charakter-Plugin als Vorlage). Verstehe die Plugin-Struktur.
2. **Erstelle die 8 Arenian-Plugins** (Struktur + Logik + Metadaten + Platzhalter-Mesh
   in Charakter-Farbe).
3. **Integriere in den CharacterLoader** und entferne Tux-IP aus dem Auswahl-Screen.
4. **Verifiziere:**
   - Godot importiert ohne neue Fehler: `/opt/data/godot/Godot_v4.7.1-stable_linux.x86_64 --headless --import`
   - Schreibe einen Test (Python, wie in Milestone 1-4) der prüft:
     - Alle 8 Arenians existieren mit korrekten Namen/Farben
     - Jeder hat character.tscn + character.json
     - character.json ist valide (name, typ, heimat, farbe)
     - Tux-IP nicht mehr im Auswahl-Screen
5. **Commit** mit beschreibender Nachricht.

## WICHTIG
- Arbeite NUR an diesem Milestone. Kein Scope-Creep.
- **Definition of Done:**
  - [ ] 8 Arenian-Plugins erstellt (Struktur + Logik + Metadaten + Platzhalter-Mesh)
  - [ ] CharacterLoader integriert die 8 Arenians
  - [ ] Tux-IP aus dem Auswahl-Screen entfernt
  - [ ] Godot importiert ohne neue Fehler
  - [ ] Charakter-Test existiert und ist grün
  - [ ] Commit gemacht
- Wenn nicht ALLE Punkte zutreffen → NICHT fertig melden, weiterarbeiten.
- **Verifizieren aus FRISCHER SHELL.**
- Nutze design/gdd/characters-overview.md als Design-Autorität. Bei Unklarheit lesen, nicht raten.
- Am Ende: `[BUILD_COMPLETE]` mit genauer Zusammenfassung (was geändert, Test-Ergebnis, Commit-Hash).

## WICHTIG FÜR DIESEN LAUF
- Schreibe JETZT direkt den Code. Kein Plan erstellen und auf Freigabe warten.
- Arbeite durch bis alle 5 Aufgaben fertig sind. Kein Stoppen nach Aufgabe 1.
- Alle Datei-Schreibrechte sind erteilt (Write/Edit in settings.json + --dangerously-skip-permissions).
- **GDScript-Pitfall (aus Milestone 1):** Nutze IMMER explizite Typen (`var x: int = ...`),
  NIE `:=` bei Dictionary-Zugriffen (Variant-Inferenz wird als Fehler behandelt und
  blockiert den Godot-Import). Verifiziere am Ende, dass deine geänderten .gd-Dateien
  ohne Parse-Fehler importieren.
- **Realistisch bleiben:** Die 3D-Modelle sind Platzhalter (Danny zeichnet später).
  Fokus auf saubere Plugin-Struktur + korrekte Metadaten + Loader-Integration.
