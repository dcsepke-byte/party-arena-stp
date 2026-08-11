# Session State — Systems Designer

## Aktuelle Aufgabe
Game Bible Teil III — Items: 6 Kapitel vollständig geschrieben (v1.0, Deutsch).

## Abgeschlossene Sektionen (alle 8 pro Datei)
- `design/gdd/item-system.md` — Framework (Pool, Inventar, Phasen, HUD, Datenstruktur)
- `design/gdd/item-luckydice.md` — Fest 5 (Tuning-Entscheidung dokumentiert)
- `design/gdd/item-teleporter.md` — Teleport STATT Würfeln (Tuning-Entscheidung dokumentiert)
- `design/gdd/item-shield.md` — Passiv, blockt 1 negativen Effekt
- `design/gdd/item-coinmagnet.md` — ×2 für 3 eigene Züge
- `design/gdd/item-thiefglove.md` — Item- oder Münz-Diebstahl

## Wichtige Entscheidungen
- Dieb-Handschuh: Aktivierung NACH Würfeln, VOR Bewegung (Phase 2) — gemäß Projekt-Kontext und item-system.md; widersprüchliche Vorgabezeile in item-thiefglove.md zugunsten der Mehrheits-Regel aufgelöst.
- Schutzschild blockt BEIDE Diebstahl-Formen (Item + Münzen).
- Schutzschild-Duplikat: Shop-Kauf verfällt wirkungslos ("Verschwendung"); Event-Duplikat → Kompensation 50 % (3 Münzen).
- Münz-Magnet: Wiederverwendung verfällt (kein Refresh/Stacking); Minispiele im realzeitlichen Fenster werden verdoppelt.
- Alle Aktivierungs-/Stacking-/Verbrauchs-Regeln sind itemspezifisch dokumentiert.

## Offene Punkte / Nächste Sektion
- Registry `design/registry/entities.yaml` existiert nicht → 5 Items als Cross-System-Fakten zum Eintragen vorgeschlagen.
- Restliche Game-Bible-Kapitel (Board/Field, Minigames, UI, etc.) folgen separat.

## Key decisions (Kurzreferenz)
| Item | Preis | Effekt-Typ | Aktivierung |
|---|---|---|---|
| Glücks-Würfel | 5 | immediate | Phase 0 (vor Würfeln) |
| Stern-Teleporter | 8 | immediate | Phase 0 (statt Würfeln) |
| Schutzschild | 6 | passive | automatisch |
| Münz-Magnet | 4 | delayed | Phase 0 (vor Würfeln) |
| Dieb-Handschuh | 10 | immediate | Phase 2 (nach Würfeln, vor Bewegung) |
