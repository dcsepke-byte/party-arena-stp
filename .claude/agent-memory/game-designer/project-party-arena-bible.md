---
name: project-party-arena-bible
description: Party Arena game bible project state — 6 Core-Game chapters (Teil I) written 2026-08-11, bible-index statuses updated, direct execution approved
metadata:
  type: project
---

Party Arena (STP-Fork, Godot 4): Game-Bible-Schreibauftrag am 2026-08-11. Die 6 Core-Game-Kapitel (Teil I) wurden unter `design/gdd/` geschrieben: `core-loop.md`, `star-economy.md`, `dice-movement.md`, `victory-conditions.md`, `catch-up.md`, `coin-economy.md`. Die Status in `design/gdd/bible-index.md` wurden von `[geplant]` auf `[geschrieben]` gesetzt.

**Warum:** `design/gdd/game-bible-prompt.md` gibt ausdrücklich Freigabe: "schreibe sofort, keine Rückfragen". Der User (Danny/Hermes-Team) will komplette Kapitel, keinen Skeleton-then-approve-Zyklus für diesen Batch.

**Korrektur 2026-08-11:** Der frühere Eintrag "11 World+Narrative GDD chapters written" stimmt nicht mit dem Plattenzustand überein — diese Dateien existieren NICHT in `design/gdd/`. Tatsächlich vorhanden sind nur: `game-concept.md`, `session-1-analysis.md`, `game-bible-prompt.md`, `bible-index.md` (vorher) plus die 6 neuen Core-Kapitel. Kapitel 0.2–0.4 (vision-pillars/glossary/systems-index) und alle Teile II–XI sind noch NICHT geschrieben, obwohl bible-index sie teils als `[geschrieben]` listet. Vor dem Schreiben weiterer Kapitel den tatsächlichen Dateibestand prüfen.

**How to apply:** Bei Folgeschreibaufträgen zur Game Bible direkt vollständige Dateien schreiben. Die 8 Sektionen (Overview, Player Fantasy, Detailed Rules, Formulas, Edge Cases, Dependencies, Tuning Knobs, Acceptance Criteria) sind Pflicht. Bei Konflikten im Konzept (z.B. Glücks-Würfel "5 fest vs. 1–10") explizit als Design-Entscheidung in Sektion 6 dokumentieren, nicht stillschweigend ändern. Design-Konsistenz entscheidungen: Sternpreis 20, Startguthaben 10, Minispiel-Auszahlung 10/7/5/3/2, eine aktive Sternen-Statue, Standard-Rangfolge (1,2,2,4), max. 1 Stern-Kauf/Spieler/Runde. Siehe [[feedback-direct-writing]].
