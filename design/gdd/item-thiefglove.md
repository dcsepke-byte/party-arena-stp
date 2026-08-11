# Dieb-Handschuh

**Status:** Final (v1.0)
**Gültig für:** Party Arena (PA), Godot 4.2, 2–8 Spieler
**Teil der Game Bible:** Teil III — Items
**Rahmenkapitel:** `item-system.md` (verbindliche Grundregeln für Inventar, Kauf, Phasen, HUD)

---

## 1. Overview

Der **Dieb-Handschuh** ist ein sofort wirksames (`immediate`) Item zum Preis von **10 Münzen** — das teuerste Item des Sets. Er stiehlt von einem anderen Spieler entweder **1 zufälliges Item** aus dessen Inventar oder **5–15 Münzen** (Zufallswert). Der Spieler wählt vor der Ausführung, welche Diebstahl-Form er anwendet.

Der Handschuh ist das einzige **direkt aggressive** Item und kann spielentscheidend sein: Er kann dem Führenden die Münzen für einen Stern-Kauf wegnehmen oder ein wertvolles Item (z. B. einen Schutzschild oder Teleporter) entwenden.

**Aktivierungszeitpunkt (verbindlich):** Der Dieb-Handschuh wird **NACH dem Würfeln und VOR der Bewegung** aktiviert (Zug-Phase 2). Er ist die definierte Ausnahme von der Regel "Items werden vor dem Würfeln eingesetzt". Siehe §3.2 für die Begründung.

---

## 2. Player Fantasy

**"Ich nehme mir, was mir zusteht."** Der Dieb-Handschuh bedient die Fantasie des Schurken und Spielverderbers:

- **Der spielentscheidende Schlag:** Dem Führenden die Münzen zu stehlen und damit seinen Stern-Kauf zu verhindern, ist ein machtvoller, unvergesslicher Moment. Das Gefühl: "Ich habe das Spiel gerade gedreht."
- **Beute-Freude:** Das sichtbare Zufliegen des gestohlenen Items oder der Münzen zum eigenen Charakter erzeugt Schadenfreude und Triumph.
- **Kalkulierter Angriff:** Weil der Handschuh teuer ist (10 Münzen), fühlt sich jeder Einsatz wie eine bewusste, riskante Investition an — mit hohem Potenzial und hohem Verlustrisiko (Fehlschlag oder Schutzschild).
- **Risiko- und Timing-Fantasie:** Wer nach dem Würfeln erkennt, dass er auf einen Sternen-Shop zusteuert und noch Münzen braucht, kann mit dem Handschuh die fehlenden Münzen "organisieren" — ein planvoller Raubüberfall statt Zufallsglück.

---

## 3. Detailed Rules

### 3.1 Preis und Erwerb

- **Preis:** 10 Münzen im Item-Shop (Sortiment und Kauf siehe `item-system.md` §3.2).
- **Erwerb zusätzlich möglich:** durch Events (Event-Grants, siehe `item-system.md` §3.6).

### 3.2 Aktivierung (Zeitpunkt)

- **Aktivierungsphase:** Phase 2 (Item-Aktivierung **nach dem Würfeln, vor der Bewegung**). Dies ist die bewusste Ausnahme von der Standardregel "Aktivierung vor dem Würfeln" (siehe `item-system.md` §3.4).
- **Begründung der Ausnahme:** Der Dieb würfelt zuerst und kennt sein Bewegungsergebnis, bevor er zuschlägt. Dadurch kann er taktisch entscheiden: "Wenn ich auf einen Sternen-Shop zusteuere und mir Münzen fehlen, stehle ich sie jetzt." Das schafft eine einzigartige Timing-Entscheidung, die kein anderes Item bietet.
- **Nicht in Teleporter-Zügen:** Da ein Teleporter-Zug weder Würfeln noch Bewegung enthält, fehlt das Aktivierungsfenster (Phase 2 existiert nicht). Der Handschuh ist in solchen Zügen **nicht** aktivierbar.
- **Verbrauch:** Der Handschuh wird bei **jeder** Aktivierung verbraucht — bei Erfolg, bei Fehlschlag und bei Blockade durch einen Schutzschild. Die einzige Ausnahme: Es existiert kein gültiges Ziel → Aktivierung blockiert, Item bleibt erhalten.

### 3.3 Ablauf der Aktivierung

1. **Phase 2 erreichen:** Der Spieler hat gewürfelt, sich aber noch nicht bewegt.
2. **Ziel wählen:** Der Spieler wählt einen gültigen Ziel-Spieler aus der Spielerliste (Gültigkeit siehe 3.4).
3. **Modus wählen:** Der Spieler wählt zwischen **Item-Diebstahl** und **Münz-Diebstahl**. Ist das eigene Inventar voll (3 Items), ist Item-Diebstahl nicht wählbar (nur Münzen).
4. **Auflösung:** Je nach Modus, Ziel-Inventar, Ziel-Münzen und Ziel-Schutzschild wird der Diebstahl aufgelöst (Formeln F1–F3).
5. **Verbrauch:** Der Handschuh wird aus dem Inventar entfernt.

### 3.4 Gültige Ziele (Immunität)

Ein Ziel-Spieler ist genau dann gültig, wenn alle Bedingungen erfüllt sind:

| Bedingung | Regel |
|---|---|
| Nicht man selbst | Der Dieb kann sich nicht selbst bestehlen. |
| Nicht auf dem Startfeld | Ein Spieler auf dem **Startfeld** hat **Immunität** und kann nicht als Ziel gewählt werden. |
| Noch im Spiel | Ausgeschiedene/nicht aktive Spieler (falls das Spiel solche kennt) sind keine gültigen Ziele. |

- Sind **alle** anderen Spieler auf dem Startfeld (oder ausgeschieden), existiert kein gültiges Ziel → der Handschuh kann **nicht** aktiviert werden und bleibt im Inventar.
- **Hinweis:** Ein Ziel mit aktivem Schutzschild ist **gültig** (wählbar). Die Blockade wird erst bei der Auflösung wirksam. Das HUD zeigt den Schild des Ziels sichtbar; die UI warnt: "Ziel hat einen Schutzschild!". Der Spieler kann die Aktivierung bestätigen oder abbrechen.

### 3.5 Modus: Item-Diebstahl

- **Wirkung:** Es wird **1 zufälliges Item** aus dem Ziel-Inventar ausgewählt (gleichverteilt über alle Items des Ziels) und in das Inventar des Diebes übertragen.
- **Inventar-Kapazität des Diebes:** Ist das Inventar des Diebes voll, ist Item-Diebstahl in Schritt 3.3 nicht wählbar (die UI deaktiviert den Modus). Ein "übertragen trotz vollem Inventar" kann nicht eintreten.
- **Ziel ohne Items:** Hat das Ziel **kein Item** im Inventar, wird **automatisch auf Münz-Diebstahl zurückgefallen** (der Münz-Diebstahl wird wie in 3.6 aufgelöst).
- **Ziel mit Schutzschild:** Der Schild blockt den Item-Diebstahl; es findet **kein** Transfer statt, **kein** automatischer Rückfall auf Münzen. Handschuh und Schild werden verbraucht (siehe §3.7).

### 3.6 Modus: Münz-Diebstahl

- **Wirkung:** Der Dieb stiehlt **5–15 Münzen** (gleichverteilte Zufallszahl) vom Ziel, **begrenzt auf den tatsächlichen Münzkontostand** des Ziels.
- **Mindestbedingung:** Der Diebstahl ist nur möglich, wenn das Ziel **mindestens 5 Münzen** besitzt. Hat das Ziel **weniger als 5 Münzen**, schlägt der Diebstahl **fehl**; der Handschuh wird trotzdem verbraucht (siehe Formel F2).
- **Ziel mit Schutzschild:** Der Schild blockt den Münz-Diebstahl; kein Transfer; Handschuh und Schild werden verbraucht.
- **Keine Verdopplung:** Gestohlene Münzen werden durch einen aktiven Münz-Magnet **nicht** verdoppelt.

### 3.7 Interaktion mit dem Schutzschild

- Ein aktiver Schutzschild beim Ziel blockt **beide** Diebstahl-Formen (Item und Münzen) vollständig.
- Es werden **beide** Items verbraucht: der Handschuh des Diebes und der Schild des Ziels.
- Es findet **kein** Transfer statt (kein Item, keine Münzen).
- **Kein Rückfall:** Ist der Item-Diebstahl durch einen Schild blockt, erfolgt **kein** automatischer Wechsel auf Münz-Diebstahl.

### 3.8 Animation

1. Der Charakter zieht einen **schwarzen Handschuh** an; die Hand leuchtet violett auf.
2. Eine **schwarze, geisterhafte Hand** greift zum Ziel-Charakter (projiziert über das Board).
3. **Item-Diebstahl:** Das gestohlene Item-Icon löst sich vom Ziel und fliegt zum Dieb.
   **Münz-Diebstahl:** Münzen fliegen vom Ziel zum Dieb.
4. **Blockade:** Bei aktivem Schild prallt die Hand am blauen Schild ab; beide Effekte zerbersten.
5. **Fehlschlag (zu wenige Münzen):** Die Hand kommt leer zurück; eine "Fehlgeschlagen"-Meldung erscheint.

**Zeitbudget:** Effektphase ≤ 2,5 Sekunden.

### 3.9 Kombinationsregeln

| Kombination | Erlaubt? | Verhalten |
|---|---|---|
| Handschuh + Glücks-Würfel (gleicher Zug) | **Ja** | Glücks-Würfel in Phase 0, Handschuh in Phase 2. |
| Handschuh + Stern-Teleporter | **Nein** | Teleporter-Zug hat keine Phase 2 (kein Würfeln/Bewegen). |
| Handschuh + Münz-Magnet | **Ja** | Gestohlene Münzen werden nicht verdoppelt. |
| Handschuh + eigener Schutzschild | **Ja** | Der eigene Schild schützt den Dieb; unabhängig vom Angriff. |
| Zwei Handschuhe gegen dasselbe Ziel im selben Zug | **Ja** (verschiedene Diebe) | Jeder Handschuh löst separat auf; der erste blockbare Angriff verbraucht ein Ziel-Schild, der zweite greift dann ungehindert. |

---

## 4. Formulas

### F1 — Item-Diebstahl (zufällige Auswahl und Übertragung)

**Benannter Ausdruck:**

```
stolen_item = Uniform(target_inventory)      // falls |target_inventory| >= 1
fallback:    wechsle zu Münz-Diebstahl (F2)  // falls |target_inventory| = 0
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| target_inventory | Menge | ∅–3 | Items im Inventar des Ziels |
| stolen_item | Item | 1 Element | Gleichverteilt gezogenes Item |
| Uniform(M) | Funktion | M → Element | Zufällige, gleichverteilte Auswahl aus Menge M |

**Ausgabebereich:** Genau 1 Item wird übertragen, wenn das Ziel Items besitzt. Bei leerem Inventar erfolgt der automatische Rückfall auf Münz-Diebstahl.

**Arbeitsbeispiel:** Ziel-Inventar = {Schutzschild, Glücks-Würfel}. Jedes Item wird mit Wahrscheinlichkeit 1/2 gestohlen. Beispielausgang: Schutzschild → wandert in das Diebes-Inventar.

### F2 — Münz-Diebstahl (Zufallswert mit Deckelung und Fehlschlag)

**Benannter Ausdruck:**

```
fehlschlag = (balance_target < 5)
steal      = min(U{5, ..., 15}, balance_target)   // nur falls fehlschlag = 0
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| balance_target | int | 0–∞ | Münzkontostand des Ziels vor dem Diebstahl |
| U{5,...,15} | int | 5–15 | Gleichverteilte ganzzahlige Zufallszahl |
| steal | int | 0–15 | Effektiv transferierte Münzen |
| fehlschlag | bool | {0, 1} | 1, wenn Ziel < 5 Münzen hat |

**Ausgabebereich:** steal ∈ {0} ∪ [1, 15]. Bei `fehlschlag = 1` ist steal = 0 und der Handschuh wird trotzdem verbraucht. Bei Erfolg ist steal = min(Wurf, Kontostand); das Ziel kann dadurch auf 0 Münzen fallen, nie ins Minus.

**Arbeitsbeispiel 1 (Erfolg mit Deckelung):** Ziel hat 8 Münzen, Wurf = 12 → steal = min(12, 8) = **8**. Ziel hat danach 0 Münzen, Dieb +8.
**Arbeitsbeispiel 2 (Fehlschlag):** Ziel hat 3 Münzen → fehlschlag = 1 → steal = 0, Handschuh verbraucht, Meldung "Fehlgeschlagen".

### F3 — Blockade durch Schutzschild

**Benannter Ausdruck:**

```
blocked = shield_active(target)
Ergebnis = blocked ? "geblockt" : (Modus-spezifische Auflösung)
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| shield_active(target) | bool | {0, 1} | Ziel hat einen aktiven Schutzschild |
| Ergebnis | enum | {"item_gestohlen", "muenzen_gestohlen", "fehlgeschlagen", "geblockt"} | Endergebnis des Einsatzes |

**Ausgabebereich:** Bei "geblockt": kein Transfer, Handschuh verbraucht, Schild verbraucht. Bei "fehlgeschlagen": kein Transfer, Handschuh verbraucht, Schild unberührt.

**Arbeitsbeispiel:** Ziel hat einen aktiven Schild → Ergebnis = "geblockt". Der Dieb verliert seinen Handschuh, das Ziel verliert seinen Schild; niemand gewinnt oder verliert Münzen/Items.

### F4 — Gültige Zielmenge

**Benannter Ausdruck:**

```
ValidTargets = { p ∈ Players \ {self} | position(p) != start_field }
can_activate = |ValidTargets| >= 1
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| Players | Menge | 2–8 | Alle Spieler |
| self | Spieler | — | Der Dieb |
| position(p) | Feld | 1 Feld | Aktuelles Feld von Spieler p |
| start_field | Feld | 1 Feld | Das Startfeld des Boards |
| ValidTargets | Menge | ∅–7 | Wählbare Ziele |
| can_activate | bool | {0, 1} | Handschuh aktivierbar |

**Ausgabebereich:** can_activate = 1, wenn mindestens ein Gegner nicht auf dem Startfeld steht.

**Arbeitsbeispiel:** 4 Spieler; 2 Gegner stehen auf dem Startfeld, 1 Gegner auf Feld 12 → ValidTargets = {Gegner_Feld12}, can_activate = 1. Der Dieb kann nur diesen einen Gegner angreifen.

---

## 5. Edge Cases

| # | Fall | Konkretes Verhalten |
|---|---|---|
| E1 | Aktivierung gegen sich selbst | Nicht möglich; das eigene Profil ist in der Zielauswahl nicht wählbar. |
| E2 | Ziel auf dem Startfeld | Nicht wählbar (Immunität). |
| E3 | Alle Gegner auf dem Startfeld | Aktivierung blockiert; Handschuh bleibt im Inventar; Meldung "Kein gültiges Ziel". |
| E4 | Ziel ohne Items, Modus Item-Diebstahl | Automatischer Rückfall auf Münz-Diebstahl (F2). |
| E5 | Ziel mit < 5 Münzen, Modus Münz-Diebstahl | Fehlschlag; kein Transfer; Handschuh verbraucht. |
| E6 | Ziel mit < 5 Münzen, Modus Item, Ziel ohne Items | Rückfall auf Münz-Diebstahl → Fehlschlag (Ziel < 5) → kein Transfer, Handschuh verbraucht. |
| E7 | Ziel mit aktivem Schutzschild | Ergebnis "geblockt"; Handschuh und Schild verbraucht; kein Transfer; **kein** Rückfall auf Münzen. |
| E8 | Dieb-Inventar voll (3 Items) | Item-Diebstahl nicht wählbar; nur Münz-Diebstahl möglich. |
| E9 | Ziel-Münzen nach Diebstahl | Ziel fällt auf max. 0 Münzen; nie ins Minus. |
| E10 | Gestohlene Münzen + aktiver Münz-Magnet | Werden nicht verdoppelt. |
| E11 | Handschuh im Teleporter-Zug | Nicht aktivierbar (keine Phase 2). |
| E12 | Aktivierung in Phase 0 oder 3 | Blockiert; Handschuh bleibt im Inventar. |
| E13 | Zwei Diebe greifen dasselbe Ziel mit Schild an | Erster Angriff verbraucht den Schild; zweiter Angriff greift ungehindert (Handschuh verbraucht, Transfer erfolgt). |
| E14 | Spielende mit ungenutztem Handschuh | Verfällt ersatzlos. |
| E15 | Ziel besitzt genau das letzte Item, das der Dieb braucht | Normale Zufallsauswahl; kein gezieltes Stehlen eines bestimmten Items (die Auswahl ist zufällig, nicht wählbar). |

---

## 6. Dependencies

**Der Dieb-Handschuh ist abhängig von:**

| System | Art der Abhängigkeit |
|---|---|
| `item-system.md` | Kauf, Inventar (beide Seiten), Phasen (Phase 2), HUD, Verbrauch, Ziel-Auswahl-UI. |
| `item-shield.md` | Ziel-Schild blockt beide Diebstahl-Formen; beide Items verbraucht. |
| `coin-economy.md` | Münz-Transfer, Kontostände, Deckelung auf Ziel-Kontostand; Kaufpreis (10). |
| `board-architecture.md` | Startfeld-Position für die Immunitätsregel. |
| `victory-conditions.md` | Stern-Kauf des Führenden kann durch Münz-Diebstahl verhindert werden. |
| `item-coinmagnet.md` | Gestohlene Münzen werden nicht verdoppelt. |
| `technical-data-structures.md` | Item-Datenstruktur (`item_id = thiefglove`, `item_effect_type = immediate`); Ziel-Zustände. |
| `ui-hud.md` / `ui-board.md` | Ziel-Auswahl-UI, Diebstahl-Visualisierung, Schutzschild-Warnung. |
| `audio-overview.md` / `audio-sfx.md` | Diebstahl-/Abprall-Sounds. |

**Gegenrichtung (müssen in ihren Kapiteln auf den Dieb-Handschuh verweisen):**

- `item-shield.md` → Der Schild blockt den Handschuh (beide verbraucht).
- `coin-economy.md` → Ein Item kann Münzen von Spieler zu Spieler transferieren.
- `board-architecture.md` → Das Startfeld verleiht Immunität gegen Diebstahl.
- `item-system.md` → listet den Handschuh als eines der 5 aktiven Items.
- `field-item-shop.md` → verkauft den Handschuh für 10 Münzen (höchster Preis).

---

## 7. Tuning Knobs

| Knopf | Standard | Sicherer Bereich | Beeinflusste Gameplay-Größe |
|---|---|---|---|
| K1 Preis | 10 | 8–12 | Aggressions-Frequenz; der höchste Preis (10) hält das spielentscheidende Werkzeug selten und teuer. |
| K2 Münz-Diebstahl-Spanne | 5–15 | 3–20 | Erwarteter Beute-Wert (10 im Mittel) und Fehlschlags-Schwelle. |
| K3 Fehlschlags-Schwelle | < 5 Münzen | 0–10 | Höhere Schwelle macht den Münz-Diebstahl riskanter; 0 entfernt den Fehlschlag (steal = min(Wurf, Kontostand), auch bei 1 Münze). |
| K4 Auswahl bei Item-Diebstahl | zufällig | zufällig / Ziel wählt | "Zufällig" ist Standard; "Ziel wählt" (das Opfer bestimmt, welches Item es verliert) schwächt den Item-Diebstahl und erhöht die Interaktion. |
| K5 Startfeld-Immunität | an | an / aus | "An" schützt Rückständige; "aus" macht den Handschuh zu einem reinen Aggressions-Tool gegen Schwache. |
| K6 Schild-Interaktion | blockt beide Formen | blockt beide / blockt nur Items | "Nur Items" würde den Münz-Diebstahl gegen Schild-Ziele erlauben und den Schild abschwächen. |
| K7 Deckelung auf Ziel-Kontostand | an | an / aus | "Aus" erlaubte negatives Konto (verboten); "An" verhindert Minus. |
| K8 Timing (Phase) | nach Würfeln, vor Bewegung | Phase 0 / Phase 2 | Phase 2 (Standard) erlaubt die taktische Münz-Beschaffung nach dem Wurf; Phase 0 entfernt diese Timing-Entscheidung. |

---

## 8. Acceptance Criteria

| ID | Kriterium | Pass-Bedingung |
|---|---|---|
| AC1 | Aktivierungszeitpunkt | Der Handschuh wird **nach** dem Würfeln und **vor** der Bewegung eingesetzt (Phase 2). |
| AC2 | Ziel-Auswahl | Nur gültige Ziele sind wählbar: nicht man selbst, nicht Spieler auf dem Startfeld. |
| AC3 | Kein gültiges Ziel | Stehen alle Gegner auf dem Startfeld, ist die Aktivierung blockiert; der Handschuh bleibt im Inventar. |
| AC4 | Item-Diebstahl | Ein zufälliges Item wandert vom Ziel-Inventar in das Diebes-Inventar; Quelle verliert das Item. |
| AC5 | Zufallsverteilung | Bei Ziel-Inventar mit 2 Items ist jedes Item in 50 Testläufen in ca. 40–60 % der Fälle das gestohlene. |
| AC6 | Rückfall bei leerem Inventar | Ziel ohne Items + Modus Item → automatischer Münz-Diebstahl (F2). |
| AC7 | Münz-Diebstahl mit Deckelung | Ziel mit 8 Münzen, Wurf 12 → Transfer exakt 8; Ziel auf 0, Dieb +8. |
| AC8 | Fehlschlag | Ziel mit < 5 Münzen → kein Transfer; Handschuh verbraucht; Meldung "Fehlgeschlagen". |
| AC9 | Schild-Blockade | Ziel mit Schild → kein Transfer; Handschuh und Schild verbraucht; keine Rückfall auf Münzen. |
| AC10 | Volles Dieb-Inventar | Item-Diebstahl ist nicht wählbar; nur Münz-Diebstahl möglich. |
| AC11 | Verbrauch | Der Handschuh wird bei jeder Aktivierung verbraucht (Erfolg, Fehlschlag, Blockade). |
| AC12 | Keine Verdopplung | Gestohlene Münzen werden bei aktivem Münz-Magnet nicht verdoppelt. |
| AC13 | Nicht im Teleporter-Zug | In einem Zug mit aktiviertem Stern-Teleporter ist der Handschuh nicht aktivierbar. |
| AC14 | Animation | Die schwarze Hand greift zum Ziel; Item/Münzen fliegen zum Dieb; Blockade/Fehlschlag visuell unterscheidbar. |
| AC15 | Preis | Der Kaufpreis im Item-Shop beträgt exakt 10 Münzen (höchster Item-Preis). |
