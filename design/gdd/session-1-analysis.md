# Session 1 — Projekt-Detektion & GDD-Plan (CCGS)

## Projektphase: Systems Design

**Stage Confidence: PASS** — Game Concept final, Engine (Godot 4.2) konfiguriert.
Kein Systems Index, keine GDDs über das Concept hinaus. Fork-Code ist Basis,
nicht Party-Arena-Code — muss entschieden werden, was bleibt und was neu kommt.

## Geplante GDD-Kapitel (10 Teile, ~50 Kapitel)

**Teil 0 — Meta & Vision:** Game Bible Index, Vision & Pillars, Glossary, Systems Index

**Teil I — Core Game:** Core Loop, Star Economy, Dice & Movement, Victory Conditions, Catch-Up Mechanics, Coin Economy

**Teil II — Board & Fields:** Board Architecture (40 Felder), Start, Sternen-Shop, Item-Shop, Ereignis-Felder, Glück/Pech, Münz-Bonus, Mini-Spiel-Felder

**Teil III — Items:** Item System, Glücks-Würfel, Stern-Teleporter, Schutzschild, Münz-Magnet, Dieb-Handschuh

**Teil IV — Minigames:** Minigame Architecture, 5 Kategorien, Reward System, Design Template

**Teil V — Characters:** 8 Arenians

**Teil VI — World:** 7+1 Insel-Boards

**Teil VII–X — UI/UX, Audio, Narrative, Technical Design**

Jedes Kapitel: Overview, Player Fantasy, Detailed Rules, Formulas, Edge Cases, Dependencies, Tuning Knobs, Acceptance Criteria.

## Kritische Lücken

### 🔴 Kritisch
- **8-Spieler-Support** — STP hart auf 4 limitiert (`LOBBY_SIZE=4`). Alles muss skaliert werden.
- **Feldtypen-Redesign** — STP (BLUE/RED/GREEN/YELLOW/SHOP) → PA (Start/Stern-Shop/Item-Shop/Ereignis/Glück-Pech/Münz-Bonus/Mini-Spiel). NodeBoard-Klasse redesignen.
- **7+1 neue Boards** — STP hat nur 2. Jede Insel eigener 40-Felder-Pfad.
- **8 neue Charaktere** — STP: 4 (Tux-IP) → PA: 8 Arenians (Eigen-IP). 3D-Modelle, Texturen, Animationen.
- **12 neue Minigames** — im Cartoon/Toy-Look.

### 🟡 Bedeutend
- **Stern-Mechanik** — STP: Cakes (30). PA: Sterne kaufen (20), wandert.
- **Bonus-Sterne** — neue Endgame-Phase.
- **5 neue Items** — neue Item-Klassen.
- **Rebranding** — Cookies→Münzen, Cakes→Sterne, Sara→ArenaStar, Nolok/GNU entfernen.
- **Art Style Migration** — CC0/KDE → Cartoon, Toy-like, High Saturation.
- **Systems Index fehlt**, **kein Technical Design**.

## Nächste Schritte
1. `/map-systems` — Systemzerlegung
2. Fork-Strategie entscheiden
3. Core-GDDs (Core Loop + Star Economy) zuerst
4. Board/Field → Items → Minigames → Characters → World → Technical
