# CCGS Game Bible — SOFORT SCHREIBEN (Freigabe erteilt)

Du bist das Claude Code Game Studios Team. Das Projekt ist FREIGEGEBEN —
schreibe jetzt SOFORT die komplette Game Bible, ohne weitere Rückfragen.

## Kontext
- Konzept: `design/gdd/game-concept.md`
- Lücken-Analyse: `design/gdd/session-1-analysis.md`
- Engine: Godot 4.2 (Super Tux Party Fork in /opt/data/SuperTuxParty)

## DEINE AUFGABE: SCHREIBE JETZT DIE KOMPLETTE GAME BIBLE

Erstelle ALLE ~65 Kapitel als Markdown-Dateien unter `design/gdd/`. KEIN Code.
Nur dokumentieren. Arbeite durch bis ALLE Kapitel geschrieben sind — stoppe
nicht nach dem Plan, schreibe die tatsächlichen Inhalte.

## Zu erstellende Dateien (ALLE)

**Meta (4):** `bible-index.md`, `vision-pillars.md`, `glossary.md`, `systems-index.md`

**Core Game (6):** `core-loop.md`, `star-economy.md`, `dice-movement.md`, `victory-conditions.md`, `catch-up.md`, `coin-economy.md`

**Board & Fields (8):** `board-architecture.md`, `field-start.md`, `field-star-shop.md`, `field-item-shop.md`, `field-event.md`, `field-luck.md`, `field-coin-bonus.md`, `field-minigame.md`

**Items (6):** `item-system.md`, `item-luckydice.md`, `item-teleporter.md`, `item-shield.md`, `item-coinmagnet.md`, `item-thiefglove.md`

**Minigames (4):** `minigame-architecture.md`, `minigame-categories.md`, `minigame-rewards.md`, `minigame-template.md`

**Characters (9):** `characters-overview.md`, `character-brix.md`, `character-nixie.md`, `character-pip.md`, `character-koko.md`, `character-tiko.md`, `character-bolt.md`, `character-bloom.md`, `character-momo.md`

**World (8):** `world-overview.md`, `world-sonnenstrand.md`, `world-zuckerwald.md`, `world-wolkenwerk.md`, `world-frostgipfel.md`, `world-dschungeltempel.md`, `world-mechanik-stadt.md`, `world-sternenzitadelle.md`

**UI/UX (7):** `ui-overview.md`, `ui-mainmenu.md`, `ui-hud.md`, `ui-board.md`, `ui-shop.md`, `ui-character-select.md`, `ui-accessibility.md`

**Audio (4):** `audio-overview.md`, `audio-music.md`, `audio-sfx.md`, `audio-voice.md`

**Narrative (3):** `narrative-overview.md`, `narrative-arena-star.md`, `narrative-flavor.md`

**Technical (5):** `technical-architecture.md`, `technical-multiplayer.md`, `technical-fork-strategy.md`, `technical-data-structures.md`, `technical-performance.md`

**README (1):** `README.md` (Master-Index mit Links)

## Jedes Kapitel: 8 Sektionen
1. Overview 2. Player Fantasy 3. Detailed Rules 4. Formulas 5. Edge Cases 6. Dependencies 7. Tuning Knobs 8. Acceptance Criteria

## WICHTIG
- Schreibe ALLE Kapitel. Kein Stoppen bis alle ~65 geschrieben sind.
- Entscheide die Fork-Strategie (technical-fork-strategy.md): was bleibt aus STP, was ist neu.
- Behandle die kritischen Lücken: 8-Spieler, Feldtypen-Redesign, 7+1 Boards, 8 Charaktere, 12 Minigames.
- Alles auf Deutsch, extrem detailliert.
- NACH ALLEN Kapiteln: erstelle `design/gdd/README.md` als Master-Index.
- Am Ende: melde "GAME BIBLE COMPLETE: X Dateien, Y Kapitel geschrieben".

FANG JETZT AN. Kein Plan, keine Rückfrage — schreibe die Dateien.
