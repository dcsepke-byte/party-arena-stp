---
name: feedback-direct-writing
description: User approved direct file writing without per-section approval for the Game Bible batch
metadata:
  type: feedback
---

Bei der Game-Bible-Generierung (Party Arena) sollen Dateien direkt komplett geschrieben werden — kein Skeleton-then-approve pro Sektion.

**Why:** `design/gdd/game-bible-prompt.md` erteilt explizite Freigabe ("FANG JETZT AN. Kein Plan, keine Rückfrage"). Der User hat alle kreativen Entscheidungen bereits im Prompt getroffen und detailliert vorgegeben.

**How to apply:** Wenn der User einen vollständigen, detaillierten Schreibauftrag mit fertigen Design-Vorgaben liefert, direkt schreiben statt Rückfragen. Die inkrementelle Skeleton-Approval-Regel (design-docs.md) gilt für Design-Sessions mit offenen Entscheidungen, nicht für freigegebene Massen-Generierung.
