# Stern-Teleporter

**Status:** Final (v1.0)
**Gültig für:** Party Arena (PA), Godot 4.2, 2–8 Spieler
**Teil der Game Bible:** Teil III — Items
**Rahmenkapitel:** `item-system.md` (verbindliche Grundregeln für Inventar, Kauf, Phasen, HUD)

---

## 1. Overview

Der **Stern-Teleporter** ist ein sofort wirksames (`immediate`) Item zum Preis von **8 Münzen**. Er teleportiert den Spieler direkt zu einem **Sternen-Shop-Feld seiner Wahl** — vorausgesetzt, dieser Shop hat einen **verfügbaren Stern** (nicht bereits gekauft).

**TUNING-ENTSCHEIDUNG (diese Version):** Der Teleporter ersetzt den gesamten Zuganteil Würfeln + Bewegen. Der Spieler würfelt in diesem Zug **nicht** und bewegt sich **nicht** — er wird sofort und direkt zum Ziel-Shop teleportiert. Es gibt in dieser Version **keine** Variante, bei der zusätzlich gewürfelt wird.

Der Teleporter ist das stärkste Werkzeug zur **Stern-Sicherung**: Er umgeht Bewegung und Feldrisiken und garantiert den Zugang zu einem Stern-Kauf (sofern der Spieler 20 Münzen besitzt und der Shop einen Stern führt).

---

## 2. Player Fantasy

**"Ich erscheine, wo man mich nicht erwartet."** Der Stern-Teleporter bedient die Fantasie des überlegenen Schachzugs:

- **Zeitersparnis und Risikovermeidung:** Andere Spieler müssen Felder ablaufen und Ereignisse riskieren; der Teleporter-Spieler überspringt das Brett und steht sofort am Ziel.
- **Der gesicherte Kauf:** Das Gefühl, einen Stern praktisch "in der Tasche" zu haben, sobald das Item aktiviert wird — vorausgesetzt, man hat die 20 Münzen.
- **Macht über den Spielplan:** Die Wahl des Ziel-Shops (bei mehreren Shops) ist eine echte taktische Entscheidung: Welcher Shop ist am wenigsten umkämpft? Wo wandert der Stern nach dem Kauf hin?
- **Vorbereitungs-Belohnung:** Wer früh Münzen hortet und den Teleporter kauft, belohnt sich mit einem garantierten Stern.

---

## 3. Detailed Rules

### 3.1 Preis und Erwerb

- **Preis:** 8 Münzen im Item-Shop (Sortiment und Kauf siehe `item-system.md` §3.2).
- **Erwerb zusätzlich möglich:** durch Events (Event-Grants, siehe `item-system.md` §3.6).

### 3.2 Aktivierung

- **Aktivierungsphase:** Phase 0 (Item-Aktivierung **vor dem Würfeln**).
- **Voraussetzung:** Mindestens ein Sternen-Shop auf dem Board hat einen **verfügbaren Stern** (`star_available = true`). Ist kein Stern verfügbar, ist das Item **nicht aktivierbar** und wird **nicht verbraucht**.
- **Ablauf:**
  1. Spieler aktiviert den Teleporter in Phase 0.
  2. Das System ermittelt alle Sternen-Shops mit verfügbarem Stern (Formel F1).
  3. Bei mehreren Shops mit Stern öffnet sich eine **Ziel-Auswahl-UI**; der Spieler wählt einen Ziel-Shop.
  4. Der Spieler wird **sofort** zum Ziel-Shop-Feld teleportiert.
  5. Der **Sternen-Shop-Besuch** läuft normal ab: Der Spieler kann einen Stern für 20 Münzen kaufen; nach dem Kauf wandert der Stern zu einem neuen Feld (Regeln siehe `field-star-shop.md` / `star-economy.md`).
- **Kein Würfeln, keine Bewegung:** In diesem Zug gibt es keine Würfelphase und keine Bewegungsphase. Der Teleport ersetzt beides.
- **Verbrauch:** Das Item wird bei **erfolgreicher** Teleportation verbraucht. Bei einer blockierten Aktivierung (kein Stern verfügbar) bleibt es im Inventar.

### 3.3 "Kein Stern verfügbar"-Fall

- Wählt der Spieler (in der UI) einen Shop aus, der inzwischen keinen Stern mehr hat, zeigt die UI die Meldung **"Kein Stern verfügbar"** an. Das Item wird **nicht verbraucht**, und der Spieler **würfelt normal** (der Zug läuft als normaler Würfelzug weiter).
- **Design-Hinweis:** Dieser Fall kann in der Praxis nur durch einen UI- oder Zustandsfehler eintreten, da die Ziel-Auswahl nur Shops **mit** verfügbarem Stern anbietet. Die Regel existiert als Sicherheitsnetz (Defense in Depth).

### 3.4 Animation

1. Der Charakter hält den Teleporter (Stern-Szepter/Anhänger) hoch; **Sternenstaub** umhüllt den Körper.
2. Der Charakter **verschwindet** (Auflösung in funkelnden Partikeln).
3. Kurze Reise-Sequenz (Sternenpfad), dann **erscheint** der Charakter mit einem Aufblitzen am gewählten Sternen-Shop-Feld.
4. Die Sternen-Shop-Interaktion öffnet sich direkt.

**Zeitbudget:** Gesamte Effektphase ≤ 3 Sekunden (längstes Item, da Teleport).

### 3.5 Kombinationsregeln

| Kombination | Erlaubt? | Verhalten |
|---|---|---|
| Teleporter + Glücks-Würfel | **Nein** | Beide ersetzen den Wurf; schließen sich in Phase 0 gegenseitig aus. |
| Teleporter + Münz-Magnet | **Ja** | Münz-Magnet kann in Phase 0 mitaktiviert werden. Der Teleporter-Zug zählt als eigener Zug des Magneten (Zähler dekrementiert), erzeugt aber selbst keine Münz-Gewinne. Der Stern-Kauf wird **nicht** verdoppelt. |
| Teleporter + Dieb-Handschuh | **Nein** | Der Handschuh erfordert Phase 2 (nach dem Würfeln, vor der Bewegung). Ein Teleporter-Zug hat weder Wurf noch Bewegung → Handschuh nicht aktivierbar. |
| Teleporter + Schutzschild | **Ja** | Unabhängig; Schild bleibt passiv aktiv. |

### 3.6 Spielende

- Ein Teleporter kann auch im letzten Zug des Spiels verwendet werden (sofern ein Stern verfügbar ist). Der nachfolgende Stern-Kauf ist ein normaler Shop-Besuch; das Spiel endet danach nach den normalen Regeln (`victory-conditions.md`).

---

## 4. Formulas

### F1 — Verfügbarkeit eines Ziels

**Benannter Ausdruck:**

```
S = { s ∈ Shops | star_available(s) = true }
can_activate = |S| >= 1
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| Shops | Menge | 2–3 | Alle Sternen-Shop-Felder des aktuellen Boards |
| star_available(s) | bool | {0, 1} | Ob Shop `s` aktuell einen nicht gekauften Stern anbietet |
| S | Menge | ∅ oder 1–3 | Menge der Shops mit verfügbarem Stern |
| can_activate | bool | {0, 1} | Teleporter aktivierbar |

**Ausgabebereich:** `can_activate` ist 1 genau dann, wenn mindestens ein Shop einen Stern führt. Das Item ist blockiert, sobald alle Sterne gekauft wurden (S = ∅).

**Arbeitsbeispiel:** Board hat 3 Sternen-Shops. Zwei Sterne wurden bereits gekauft, einer ist verfügbar → S = {Shop_3}, |S| = 1 → `can_activate = 1`. Der Spieler wird nur Shop_3 angeboten (keine Auswahl nötig).

### F2 — Ziel-Auswahl bei mehreren Shops

**Benannter Ausdruck:**

```
target = player_choice(S)   // S wie in F1
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| S | Menge | 1–3 | Shops mit verfügbarem Stern |
| player_choice | Funktion | S → S | Spieler wählt genau ein Element aus S |
| target | Shop | ∈ S | Der gewählte Ziel-Shop |

**Ausgabebereich:** `target` ist immer ein Element von S (niemals ein Shop ohne Stern). Bei |S| = 1 entfällt die UI, `target` ist der einzige Shop.

**Arbeitsbeispiel:** S = {Shop_1, Shop_2}. Der Spieler wählt Shop_2 → `target = Shop_2`. Er wird zu Shop_2 teleportiert.

### F3 — Gesamtkosten eines teleportierten Stern-Kaufs (strategische Formel)

**Benannter Ausdruck:**

```
total_cost = star_price + teleporter_price
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| star_price | int | 20 (fix) | Stern-Preis am Sternen-Shop |
| teleporter_price | int | 8 (fix) | Kaufpreis des Teleporters |
| total_cost | int | 28 (fix) | Münzaufwand für "Stern via Teleporter" |

**Ausgabebereich:** Exakt 28 Münzen in der Standard-Konfiguration. Der Münz-Magnet hat hierauf **keinen** Einfluss (Stern-Preis wird nicht verdoppelt).

**Arbeitsbeispiel:** Ein Spieler mit 25 Münzen kann sich den Teleporter (8) **nicht** leisten und den Stern gleichzeitig kaufen (28 > 25). Mit 30 Münzen ist der kombinierte Kauf möglich; nach dem Kauf bleiben 2 Münzen.

---

## 5. Edge Cases

| # | Fall | Konkretes Verhalten |
|---|---|---|
| E1 | Kein Sternen-Shop hat einen verfügbaren Stern | Aktivierung blockiert; Teleporter bleibt im Inventar; Meldung "Kein Stern verfügbar". |
| E2 | Mehrere Shops mit Stern | Ziel-Auswahl-UI wird gezeigt; Spieler wählt Ziel. |
| E3 | Genau ein Shop mit Stern | Keine UI; Teleport geht automatisch zu diesem Shop. |
| E4 | Ziel-Shop verliert Stern zwischen Auswahl und Ankunft | Unmöglich innerhalb eines Zuges (keine fremden Aktionen zwischen Aktivierung und Ankunft). Als Sicherheitsnetz: "Kein Stern verfügbar"-Fall greift (siehe 3.3). |
| E5 | Teleporter im letzten Zug aktiviert | Zulässig; Stern-Kauf findet normal statt; Spielende danach nach `victory-conditions.md`. |
| E6 | Teleporter + Münz-Magnet | Erlaubt; Teleporter-Zug zählt als Magnet-Zug (Zähler dekrementiert am Zugende); Stern-Kauf wird nicht verdoppelt. |
| E7 | Teleporter + Dieb-Handschuh | Handschuh nicht aktivierbar in diesem Zug (kein Würfeln/Bewegen). |
| E8 | Spieler hat < 20 Münzen am Ziel-Shop | Teleport findet trotzdem statt (Item verbraucht); der Stern-Kauf ist mangels Münzen nicht möglich. Kein Rücktritt vom Teleport. |
| E9 | Aktivierung außerhalb von Phase 0 | Blockiert; Item bleibt im Inventar. |
| E10 | Spielende vor Aktivierung | Ungenutzter Teleporter verfällt ersatzlos. |
| E11 | Der einzige Shop mit Stern ist 0 Felder entfernt | Teleport ist trotzdem gültig und verbraucht das Item; die Bewegung wäre sonst 0 Felder. Strategisch meist unnötig, aber erlaubt. |

---

## 6. Dependencies

**Der Stern-Teleporter ist abhängig von:**

| System | Art der Abhängigkeit |
|---|---|
| `item-system.md` | Kauf, Inventar, Phasen (Phase 0), HUD, Verbrauch, Blockade-Regeln. |
| `field-star-shop.md` | Ziel-Feld, Stern-Kauf-Interaktion, Stern wandert nach Kauf. |
| `star-economy.md` | Stern-Preis (20), Stern-Verfügbarkeit (`star_available`), Stern-Wanderung. |
| `dice-movement.md` | Überspringt Würfel- und Bewegungsphase; Zugphasen-Konsistenz. |
| `board-architecture.md` | Anzahl und Position der Sternen-Shops (2–3) pro Board. |
| `coin-economy.md` | Kaufpreis (8); Münz-Magnet-Interaktion (Stern-Preis nicht verdoppelt). |
| `ui-hud.md` / `ui-board.md` | Ziel-Auswahl-UI, Teleport-Visualisierung auf dem Brett. |
| `technical-data-structures.md` | Item-Datenstruktur (`item_id = teleporter`, `item_effect_type = immediate`). |
| `audio-overview.md` / `audio-sfx.md` | Teleport-Sound, Ankunft-Sound. |

**Gegenrichtung (müssen in ihren Kapiteln auf den Teleporter verweisen):**

- `field-star-shop.md` → Spieler können per Teleporter ankommen, ohne gewürfelt zu haben.
- `star-economy.md` → Der Teleporter erzeugt zusätzliche, planbare Stern-Kauf-Gelegenheiten.
- `dice-movement.md` → Ein Item kann Würfeln und Bewegung vollständig ersetzen.
- `item-system.md` → listet den Teleporter als eines der 5 aktiven Items.
- `field-item-shop.md` → verkauft den Teleporter für 8 Münzen.

---

## 7. Tuning Knobs

| Knopf | Standard | Sicherer Bereich | Beeinflusste Gameplay-Größe |
|---|---|---|---|
| K1 Preis | 8 | 7–10 | Häufigkeit des Stern-Sicherungswerkzeugs; zu günstig (≤6) entwertet normale Stern-Erreichbarkeit. |
| K2 Aktivierungsmodus | **statt Würfeln** (fix) | statt Würfeln / vor Würfeln + zusätzlich bewegen | "Statt Würfeln" macht das Item stark und klar; "zusätzlich bewegen" macht es übermächtig (2 Aktionen). Alternative nur als Experiment. |
| K3 Stern-Verfügbarkeitspflicht | an | an / aus | "An" verhindert wertlose Teleports auf leere Shops; "aus" erlaubt Positions-Teleports (deutlich schwächer). |
| K4 Ziel-Bereich | jeder Shop mit Stern | jeder Shop / nur nächster / nur entferntester | Eingrenzung erhöht die Planungsanforderung; "jeder Shop" ist am flexibelsten und stärksten. |
| K5 Stern-Preis-Aufschlag nach Teleport | 0 (normal: 20) | 0–5 Aufschlag | Ein Aufschlag (z. B. 25) würde den Teleporter abschwächen, da der Vorteil des garantierten Zugangs teurer wird. |
| K6 Zusammenwirken mit Münz-Magnet | Stern nicht verdoppelt | — | Fixe Regel: Ausgaben werden nie verdoppelt. |

---

## 8. Acceptance Criteria

| ID | Kriterium | Pass-Bedingung |
|---|---|---|
| AC1 | Teleport statt Würfeln | Nach Aktivierung würfelt der Spieler nicht und bewegt sich nicht; er erscheint auf dem gewählten Sternen-Shop-Feld. |
| AC2 | Ziel-Auswahl | Bei mehreren Shops mit Stern öffnet sich eine Auswahl; nur Shops mit Stern sind wählbar. |
| AC3 | Einzel-Shop-Fall | Bei genau einem Shop mit Stern entfällt die Auswahl; Teleport erfolgt automatisch. |
| AC4 | Kein Stern verfügbar | Aktivierung ist blockiert; das Item bleibt im Inventar; keine Bewegung/kein Wurf wird ersetzt. |
| AC5 | Sicherheitsnetz | Wird (durch Fehler) ein Shop ohne Stern gewählt, wird das Item nicht verbraucht und der Spieler würfelt normal. |
| AC6 | Stern-Kauf am Ziel | Am Ziel-Shop ist ein Stern-Kauf für 20 Münzen möglich; nach dem Kauf wandert der Stern. |
| AC7 | Zu wenig Münzen | Hat der Spieler < 20 Münzen, erfolgt der Teleport trotzdem; der Stern-Kauf ist nicht möglich. |
| AC8 | Verbrauch | Bei erfolgreicher Teleportation ist das Item aus dem Inventar entfernt. |
| AC9 | Kombination mit Glücks-Würfel | Beide können nicht im selben Zug aktiviert werden. |
| AC10 | Kombination mit Dieb-Handschuh | Der Handschuh ist in einem Teleporter-Zug nicht aktivierbar. |
| AC11 | Animation | Sternenstaub-Auflösung und Erscheinen am Ziel sind für alle Spieler sichtbar; Dauer ≤ 3 s. |
| AC12 | Preis | Der Kaufpreis im Item-Shop beträgt exakt 8 Münzen. |
