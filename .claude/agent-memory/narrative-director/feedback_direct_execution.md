---
name: feedback-direct-execution
description: Bei vollständig spezifizierten Schreibaufträgen sofort komplett ausführen, nicht sektionsweise rückfragen
metadata:
  type: feedback
---

Regel: Wenn der User einen **vollständig spezifizierten** Auftrag gibt (alle Inhalte/Parameter festgelegt, "schreibe alle X Dateien vollständig, keine Platzhalter"), dann sofort komplett ausführen. Nicht den inkrementellen Skeleton-pro-Sektion-Workflow aus `.claude/rules/design-docs.md` anwenden, nicht vor jeder Sektion um Freigabe fragen.

**Why:** Der User hat explizit "Schreibe alle 9 Dateien VOLLSTÄNDIG. Keine Platzhalter." verlangt; die Projekt-Prompt (`game-bible-prompt.md`) sagt "FANG JETZT AN. Kein Plan, keine Rückfrage." Der question-first-Protokoll-Teil gilt für offene Design-Entscheidungen, nicht für bereits vollständig entschiedene Schreibaufträge.

**How to apply:** Bei klar spezifizierten Content-Deliverables (Game-Bible-Kapitel, Charakter-Spezifikationen) direkt schreiben. Klärende Fragen nur stellen, wenn echte Mehrdeutigkeit besteht, die das Ergebnis verfälschen würde. Nach Abschluss Buchhaltung nachziehen (z. B. Status im `bible-index.md` aktualisieren), da die Bible-Prozessregeln das verlangen. Verwandt: [[user-profile]]
