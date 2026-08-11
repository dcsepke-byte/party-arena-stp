---
name: party-arena-gdd-bible
description: Stand der Party-Arena Game Bible unter design/gdd/ — 65 Kapitel, 8-Sektionen-Standard, Teil V (Characters) fertiggestellt
metadata:
  type: project
---

Die Party-Arena Game Bible lebt unter `design/gdd/` mit `bible-index.md` als Master-Index. Ziel: 65 Kapitel in 11 Teilen, jedes mit den 8 Pflichtsektionen. Stand 2026-08-11: `bible-index.md` und **Teil V (Characters, 9 Kapitel)** sind geschrieben: `characters-overview.md`, `character-brix.md`, `character-nixie.md`, `character-pip.md`, `character-koko.md`, `character-tiko.md`, `character-bolt.md`, `character-bloom.md`, `character-momo.md`. Alle anderen Teile (Core Game, Board & Fields, Items, Minigames, World, UI/UX, Audio, Narrative, Technical) sind noch [geplant].

**Kern-Designentscheidungen der Charaktere:**
- 8 Arenians, spielmechanisch **identisch** (keine Stats-Unterschiede, keine Asymmetrie); Unterschiede nur visuell/animatorisch/akustisch/narrativ.
- Alle 1,2 Einheiten hoch, identische Trefferbox (Zylinder/Kapsel r=0,6, h=1,2).
- Animationsvertrag: 12 Pflichtanimationen (idle, walk, run, punch, kick, jump, happy, sad, stun, carry, run-carry, victory).
- Plugin-Loader-Vertrag aus `common/scripts/loader/character_loader.gd` (Pflichtdateien character.tscn, icon.png, splash.png).

**Why:** Charaktere sind Persönlichkeits-Hüllen ohne Spielwert-Vorteil (kein Pay-to-Win, kein Balance-Albtraum).

**How to apply:** Bei neuen Charakter- oder World-Kapiteln die Overview als Vertrag nutzen; Statuswechsel im `bible-index.md` nachziehen. Verwandt: [[user-profile]], [[feedback-direct-execution]]
