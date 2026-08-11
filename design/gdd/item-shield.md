# Schutzschild

**Status:** Final (v1.0)
**Gültig für:** Party Arena (PA), Godot 4.2, 2–8 Spieler
**Teil der Game Bible:** Teil III — Items
**Rahmenkapitel:** `item-system.md` (verbindliche Grundregeln für Inventar, Kauf, Phasen, HUD)

---

## 1. Overview

Der **Schutzschild** ist ein passiv wirkendes (`passive`) Item zum Preis von **6 Münzen**. Er blockt **einen einzigen negativen Effekt** vollständig und wird dabei selbst verbraucht. Er wird **niemals manuell aktiviert** — seine Auslösung ist vollautomatisch, sobald ein blockbarer negativer Effekt eintritt.

Der Schutzschild ist das einzige **defensive** Item des Item-Sets. Er schützt vor:

- **Dieb-Handschuh** (Item-Diebstahl und Münz-Diebstahl),
- **Pech-Feld** (Münz-Verlust),
- **negativen Events** (Münz-Verlust, Item-Verlust).

Er schützt **nicht** vor: Event-Teleportation (Rückruf), Positions-Tausch und normalen Spielmechaniken.

Der Schutzschild bleibt **über mehrere Runden aktiv**, bis er ausgelöst wird. Er belegt währenddessen einen Inventar-Slot — die Opportunitätskosten seiner Sicherheit.

---

## 2. Player Fantasy

**"Ich bin abgesichert."** Der Schutzschild bedient die Fantasie des Unverwundbaren:

- **Ruhe und Souveränität:** Während andere Spieler Pech-Felder und Diebe fürchten, fühlt sich der Schild-Träger sicher. Das Gefühl: "Mir kann nichts passieren."
- **Provokation mit Folgen:** Ein sichtbarer Schild (im HUD für alle sichtbar) schreckt Dieb-Handschuh-Besitzer ab oder lockt sie in eine Falle (ihr Handschuh wird verbraucht, ohne Beute).
- **Belohnung für Weitsicht:** Wer den Schild kauft, bevor er ein Pech-Feld oder einen Dieb erwartet, erlebt den befriedigenden Moment des "Schutzschild hat DICH geschützt!" — ein sichtbarer Beweis, dass sich die Investition gelohnt hat.
- **Schutz des Fortschritts:** Der Schild bewahrt erspielte Münzen und Items, also indirekt auch die eigene Stern-Strategie.

Die Fantasie ist bewusst **reaktiv statt aktiv**: Der Schild gibt kein Gefühl von Angriff, sondern von unangreifbarer Sicherheit.

---

## 3. Detailed Rules

### 3.1 Aktivierungs- und Block-Logik

- **Passiv:** Der Schild wird nie manuell aktiviert (kein HUD-Slot-Button; in Phasen 0 und 2 nicht auswählbar).
- **Wirkbeginn:** Der Schutz beginnt mit dem Eintritt des Items ins Inventar (Kauf oder Event-Grant).
- **Auslösung:** Wird ein **blockbarer negativer Effekt** gegen den Spieler aufgelöst, blockt der Schild diesen Effekt vollständig und wird **verbraucht** (zerbricht).
- **Benachrichtigung:** Bei Auslösung erscheint für alle Spieler sichtbar die Meldung **"Schutzschild hat DICH geschützt!"** (lokalisiert für den betroffenen Spieler).
- **Dauer:** Unbegrenzt (über Runden), bis zur Auslösung.

### 3.2 Blockbare vs. nicht blockbare Effekte (Interaktionsmatrix)

| # | Effekt | Quelle | Blockbar? |
|---|---|---|---|
| 1 | Item-Diebstahl | Dieb-Handschuh | **Ja** |
| 2 | Münz-Diebstahl (5–15) | Dieb-Handschuh | **Ja** |
| 3 | Münz-Verlust | Pech-Feld | **Ja** |
| 4 | Münz-Verlust | negatives Event | **Ja** |
| 5 | Item-Verlust | negatives Event | **Ja** |
| 6 | Event-Teleportation (Rückruf) | Event | **Nein** |
| 7 | Positions-Tausch | Event | **Nein** |
| 8 | Stern-Verlust (falls ein solches Event existiert) | Event | **Nein** (nur Münz-/Item-Verlust ist blockbar; Stern-Verlust fällt unter "normale Spielmechaniken", sofern eingeführt) |
| 9 | Münz-Verlust durch normale Spielmechanik (z. B. Minispiel-Niederlage mit Münzabzug) | normal | **Nein** |
| 10 | Item-Preis / Stern-Preis (Ausgaben) | Shop | **Nein** (keine negativen Effekte, sondern Kaufentscheidungen) |
| 11 | Münz-Verlust durch Pech bei aktivem Münz-Magnet | Pech-Feld + Magnet | **Ja** (Pech-Verlust bleibt auch mit Magnet unverdoppelt und ist blockbar) |

**Klarstellung zur Diebstahl-Blockade:** Der Schild blockt **beide** Formen des Dieb-Handschuhs (Item- und Münz-Diebstahl). Dies ist eine bewusste Vereinheitlichung (siehe `item-system.md` §3.7 und `item-thiefglove.md` §3.2).

### 3.3 Stacking- und Duplikatregeln

- **Nur 1 aktiver Schild:** Ein Spieler kann nie mehr als einen aktiven Schutzschild haben.
- **Zweiter Kauf (Shop):** Der Kauf eines zweiten Schutzschilds ist möglich (Münzen werden abgezogen), aber der zweite Schild **verfällt sofort wirkungslos** ("Verschwendung"). Er belegt keinen zusätzlichen Slot und verlängert nichts. Meldung: "Du hast bereits einen Schutzschild!".
- **Zweiter Schild per Event:** Gewährt ein Event einen Schild, obwohl bereits einer aktiv ist, erhält der Spieler stattdessen eine Kompensation von `floor(6 × 0.5) = 3` Münzen (siehe `item-system.md` F4). Es wird kein zweiter aktiver Schild erzeugt.
- **Begründung der Asymmetrie:** Shop-Käufe sind bewusste Entscheidungen (der Käufer hätte es wissen können); Event-Grants sind Zufall (Spieler soll nicht durch Zufall bestraft werden).

### 3.4 Mehrere negative Effekte gleichzeitig

- Treffen mehrere negative Effekte im selben Auflösungsmoment auf den Spieler (z. B. ein Event, das sowohl Münzen als auch Items abnimmt), blockt der Schild **nur den ersten** blockbaren Effekt in der **Reihenfolge der Effekt-Auflösung**.
- Die Auflösungsreihenfolge ist durch die Daten-Definition des jeweiligen Events/Effekts festgelegt (erste definierte Wirkung zuerst).
- Alle weiteren Effekte greifen ungehindert; der Schild ist nach dem ersten Block verbraucht.

### 3.5 Animation

1. Solange der Schild aktiv ist, umgibt ein **blauer Energie-Schild** den Charakter (dezenter, dauerhaft sichtbarer Effekt im HUD und am Charakter-Modell).
2. Bei Auslösung: Der Schild **leuchtet kurz auf** und **zerspringt** in blauen Splittern (zerbrechender Effekt).
3. Parallel erscheint die Meldung "Schutzschild hat DICH geschützt!" und die betroffene Wirkung (z. B. Münz-Verlust, Diebstahl) wird visuell neutralisiert (z. B. Münzen prallen ab, diebe Hand wird zurückgestoßen).
4. Das Schild-Icon erlischt (Verbrauch).

**Zeitbudget:** Auslösung ≤ 2 Sekunden.

### 3.6 Kombinationsregeln

| Kombination | Erlaubt? | Verhalten |
|---|---|---|
| Schild + Dieb-Handschuh (gleicher Spieler) | **Ja** | Der Schild schützt den Besitzer; der Handschuh greift andere an. Beide können im selben Zug verwendet werden (Handschuh in Phase 2). |
| Schild + Münz-Magnet | **Ja** | Unabhängig; der Schild blockt Pech-Verluste, der Magnet verdoppelt Gewinne. |
| Schild + Glücks-Würfel / Teleporter | **Ja** | Unabhängig. |
| Zwei Schilde (aktiv + Kauf) | **Nein** (Stacking verboten) | Zweiter Kauf verfällt wirkungslos (siehe 3.3). |

---

## 4. Formulas

### F1 — Block-Prädikat

**Benannter Ausdruck:**

```
block(e) = e ∈ {diebstahl_item, diebstahl_muenzen, pech_muenzverlust, event_muenzverlust, event_itemverlust}
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| e | enum | siehe Matrix §3.2 | Der eintretende Effekt |
| block(e) | bool | {0, 1} | 1, wenn der Schild den Effekt blockt |
| diebstahl_item, diebstahl_muenzen, pech_muenzverlust, event_muenzverlust, event_itemverlust | enum | — | Die fünf blockbaren Effekt-Kategorien |

**Ausgabebereich:** Bool. Nicht blockbare Effekte (Event-Teleportation, Positions-Tausch, normale Spielmechaniken, Kauf-Ausgaben) ergeben 0.

**Arbeitsbeispiel:** Ein Pech-Feld zieht dem Spieler 5 Münzen ab. `e = pech_muenzverlust` → `block(e) = 1`. Der Verlust entfällt; der Schild zerbricht. Ein Event-Teleport (Rückruf) mit `e = event_teleportation` → `block(e) = 0`; der Spieler wird teleportiert, der Schild bleibt erhalten.

### F2 — Schild-Zustand (Zustandsübergang)

**Benannter Ausdruck:**

```
state_next = "spent"   falls state = "active" UND block(e) = 1
             "active"  sonst (bei nicht blockbaren Effekten oder vor Auslösung)
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| state | enum | {"none", "active", "spent"} | Zustand des Schilds |
| block(e) | bool | {0, 1} | Block-Prädikat aus F1 |
| state_next | enum | {"active", "spent"} | Folgezustand |

**Ausgabebereich:** Der Schild wechselt genau einmal von "active" nach "spent" (beim ersten blockbaren Effekt). Es gibt keinen erneuten Aktivierungszyklus.

**Arbeitsbeispiel:** Schild gekauft → state = "active". Pech-Feld betreten → block = 1 → state_next = "spent". Ein weiteres Pech-Feld im selben Zug greift jetzt ungehindert.

### F3 — Verbleibende Block-Kapazität

**Benannter Ausdruck:**

```
capacity = 1  falls state = "active"
           0  falls state = "spent" oder "none"
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| capacity | int | {0, 1} | Anzahl noch blockbarer Effekte |
| state | enum | {"none", "active", "spent"} | Schild-Zustand |

**Ausgabebereich:** 0 oder 1 (kein Mehrfach-Block).

**Arbeitsbeispiel:** Nach der Auslösung ist `capacity = 0`; das System kann den Spieler nicht erneut schützen.

---

## 5. Edge Cases

| # | Fall | Konkretes Verhalten |
|---|---|---|
| E1 | Dieb-Handschuh gegen Schild-Ziel | Handschuh **und** Schild werden verbraucht; kein Item- und kein Münz-Transfer. |
| E2 | Pech-Feld mit aktivem Schild | Münz-Verlust entfällt; Schild zerbricht; Meldung wird angezeigt. |
| E3 | Negatives Event mit Münz- **und** Item-Verlust | Nur der erste blockbare Effekt (Daten-Reihenfolge) wird geblockt; der zweite greift. Schild danach verbraucht. |
| E4 | Event-Teleportation (Rückruf) | **Nicht** blockt; Spieler wird teleportiert; Schild bleibt aktiv. |
| E5 | Positions-Tausch | **Nicht** blockt; Tausch findet statt; Schild bleibt aktiv. |
| E6 | Zweiter Schild im Shop gekauft | Münzabzug, Schild verfällt wirkungslos; kein zweiter aktiver Schild, kein Slot belegt. |
| E7 | Event gewährt zweiten Schild | Kompensation 3 Münzen; kein zweiter aktiver Schild. |
| E8 | Schild am Spielende ungenutzt | Verfällt ersatzlos (kein Rückkauf, keine Bonuspunkte). |
| E9 | Schild + Pech bei aktivem Münz-Magnet | Der Pech-Verlust ist ohnehin nie verdoppelt; der Schild blockt ihn vollständig. |
| E10 | Mehrere Diebe greifen im selben Zug an | Nur der erste Angriff wird geblockt (Schild verbraucht); der zweite Angriff greift ungehindert (setzt voraus, dass zwei Handschuhe im selben Zug gegen denselben Spieler eingesetzt werden — nach Turn-Reihenfolge möglich, da andere Spieler ihre Handschuhe in ihren eigenen Zügen einsetzen). |
| E11 | Schild beim Aktivierungsversuch in Phase 0 | Nicht auswählbar (passiv); keine manuelle Aktivierung möglich. |

---

## 6. Dependencies

**Der Schutzschild ist abhängig von:**

| System | Art der Abhängigkeit |
|---|---|
| `item-system.md` | Kauf, Inventar, HUD-Anzeige (Passiv-Icon), Verbrauch, Kompensation F4. |
| `item-thiefglove.md` | Blockt Item- und Münz-Diebstahl; beide Items verbraucht. |
| `field-luck.md` | Blockt Münz-Verlust des Pech-Felds. |
| `field-event.md` | Blockt Münz-Verlust und Item-Verlust aus negativen Events; blockt NICHT Event-Teleportation und Positions-Tausch. |
| `coin-economy.md` | Münz-Verlust-Systeme, auf die der Schild wirkt; Kaufpreis (6). |
| `technical-data-structures.md` | Item-Datenstruktur (`item_id = shield`, `item_effect_type = passive`); Effekt-Auflösungsreihenfolge. |
| `ui-hud.md` | Dauerhaftes Schild-Icon, Auslöse-Benachrichtigung. |
| `audio-overview.md` / `audio-sfx.md` | Schild-Aufleuchten/-Zerspringen-Sound. |

**Gegenrichtung (müssen in ihren Kapiteln auf den Schutzschild verweisen):**

- `item-thiefglove.md` → Ein Schild beim Ziel blockt den Diebstahl und verbraucht den Handschuh.
- `field-luck.md` → Pech-Verluste können durch ein Item vollständig entfallen.
- `field-event.md` → Negative Event-Wirkungen können durch ein Item neutralisiert werden; nicht blockbare Wirkungen (Teleportation, Positions-Tausch) müssen explizit als "nicht blockbar" geführt werden.
- `item-system.md` → listet den Schild als eines der 5 aktiven Items (passiv).
- `field-item-shop.md` → verkauft den Schild für 6 Münzen; Duplikat-Kauf verfällt.

---

## 7. Tuning Knobs

| Knopf | Standard | Sicherer Bereich | Beeinflusste Gameplay-Größe |
|---|---|---|---|
| K1 Preis | 6 | 4–8 | Verfügbarkeit von Defensive; zu günstig (≤4) macht Dieb-Handschuh unattraktiv; zu teuer (≥8) macht Schutz selten. |
| K2 Block-Kapazität | 1 (Einmal-Block) | 1–2 Ladungen | Mehr Ladungen (2) erhöhen die Schutzdauer und schwächen Aggressions-Items; 1 hält das Gleichgewicht. |
| K3 Block-Umfang | 5 Kategorien (siehe F1) | Matrix anpassbar | Welche Effekte blockt; z. B. "Event-Teleportation blockbar" würde den Schild deutlich stärken. |
| K4 Duplikat-Politik (Shop-Kauf) | verfällt (Verschwendung) | verfällt / Kauf blockiert | "Kauf blockiert" ist anti-frustrierender, entfernt aber die Skill-Komponente; "verfällt" belohnt aufmerksame Spieler. |
| K5 Kompensation (Event-Duplikat) | 50 % (3 Münzen) | 25–100 % | Fairness bei Zufalls-Grants (siehe `item-system.md` K5). |
| K6 Reihenfolge bei Mehrfach-Effekten | Daten-Reihenfolge | Daten-Reihenfolge / zufällig / Spieler wählt | Die Reihenfolge bestimmt, welcher Effekt bei Mehrfach-Treffern geblockt wird. "Spieler wählt" ist eine stärkere, seltenere Option. |
| K7 Sichtbarkeit des Schilds | für alle sichtbar | sichtbar / verdeckt | Sichtbarkeit beeinflusst Dieb-Entscheidungen; verdeckt macht den Schild zu einem Bluff-Werkzeug. |

---

## 8. Acceptance Criteria

| ID | Kriterium | Pass-Bedingung |
|---|---|---|
| AC1 | Rein passiv | Der Schild ist in keiner Phase manuell aktivierbar (kein HUD-Button, keine Tastenwirkung). |
| AC2 | Pech-Feld-Block | Betritt der Spieler mit aktivem Schild ein Pech-Feld, entfällt der Münz-Verlust; der Schild zerbricht; die Meldung erscheint. |
| AC3 | Diebstahl-Block | Ein Dieb-Handschuh gegen ein Schild-Ziel erzeugt keinen Transfer; Handschuh und Schild sind danach verbraucht. |
| AC4 | Beide Diebstahl-Formen | Der Schild blockt sowohl Item- als auch Münz-Diebstahl (2 getrennte Tests). |
| AC5 | Nicht blockbare Effekte | Bei Event-Teleportation und Positions-Tausch bleibt der Schild aktiv (2 getrennte Tests). |
| AC6 | Mehrfach-Effekt-Reihenfolge | Ein Event mit Münz- und Item-Verlust: genau der erste (daten-definierte) Effekt entfällt; der zweite greift; Schild danach verbraucht. |
| AC7 | Hält über Runden | Ein unausgelöster Schild bleibt über mindestens 2 volle Runden aktiv (kein zeitlicher Verfall). |
| AC8 | Nur 1 aktiv | Der Kauf eines zweiten Schilds erzeugt keinen zweiten aktiven Schild und belegt keinen Slot; Münzen werden abgezogen. |
| AC9 | Event-Duplikat | Ein Event-Schild bei bereits aktivem Schild zahlt exakt 3 Münzen Kompensation. |
| AC10 | Animation | Der blaue Energieschild ist dauerhaft sichtbar und zerspringt bei Auslösung für alle sichtbar. |
| AC11 | Preis | Der Kaufpreis im Item-Shop beträgt exakt 6 Münzen. |
| AC12 | Meldung | Bei jeder Auslösung erscheint "Schutzschild hat DICH geschützt!". |
