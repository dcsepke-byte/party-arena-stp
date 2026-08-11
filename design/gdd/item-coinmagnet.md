# Münz-Magnet

**Status:** Final (v1.0)
**Gültig für:** Party Arena (PA), Godot 4.2, 2–8 Spieler
**Teil der Game Bible:** Teil III — Items
**Rahmenkapitel:** `item-system.md` (verbindliche Grundregeln für Inventar, Kauf, Phasen, HUD)

---

## 1. Overview

Der **Münz-Magnet** ist ein verzögert wirkendes (`delayed`) Item zum Preis von **4 Münzen** — das günstigste Item des Sets. Er **verdoppelt alle eigenen Münz-Gewinne des Spielers für 3 eigene Züge** (den aktuellen Zug plus die nächsten 2).

Der Magnet wirkt auf **positive** Münz-Quellen:
- Münz-Bonus-Felder
- Glück-Felder (nur positive Ergebnisse)
- Minispiel-Belohnungen
- Event-Münzen

Er wirkt **nicht** auf:
- Pech-Verluste (bleiben normal, werden nicht halbiert),
- Stern-Kauf-Preis (20, bleibt unverändert),
- Item-Preise (Kaufausgaben),
- gestohlene Münzen (Dieb-Handschuh).

**Züge zählen pro Spieler, nicht pro Runde.** Bei 8 Spielern kann der Magnet daher bis zu **24 fremde Züge** (3 × 8) real abdecken, bevor der Spieler wieder an der Reihe ist. Die Wirkdauer ist ausschließlich über die **eigenen** Züge des Spielers definiert.

---

## 2. Player Fantasy

**"Münzen fliegen mir zu."** Der Münz-Magnet bedient die Fantasie des Münz-Tycoons:

- **Sichtbarer Reichtum:** Die magnetische Animation (Münzen strömen zum Charakter) macht die Verdopplung sinnlich erlebbar. Ein +10-Feld wird zu +20, ein Minispiel-Sieg zu einem dicken Batzen.
- **Wirtschaftlicher Snowball:** Der Magnet beschleunigt die Münz-Ansammlung und bringt den Spieler schneller in die Nähe des Stern-Preises (20 Münzen). Das Gefühl: "Ich bin auf dem Weg zum Reichtum."
- **Kalkulierte Investition:** Mit nur 4 Münzen Kaufpreis zahlt sich der Magnet bereits bei zwei mäßigen Gewinnen aus. Kluge Spieler aktivieren ihn vor Münz-reichen Feldern oder vor dem Minispiel.
- **Timing-Fantasie:** Da die Wirkung 3 eigene Züge hält, belohnt der Magnet Spieler, die den Spielverlauf vorausdenken ("Wo stehe ich in 2 Zügen? Wann ist das Minispiel?").

---

## 3. Detailed Rules

### 3.1 Preis und Erwerb

- **Preis:** 4 Münzen im Item-Shop (Sortiment und Kauf siehe `item-system.md` §3.2).
- **Erwerb zusätzlich möglich:** durch Events (Event-Grants, siehe `item-system.md` §3.6).

### 3.2 Aktivierung

- **Aktivierungsphase:** Phase 0 (Item-Aktivierung **vor dem Würfeln**).
- **Wirkbeginn:** Der Magnet ist ab dem Moment der Aktivierung aktiv. Der **aktuelle Zug** zählt als **Zug 1** von 3.
- **Verbrauch:** Das Item wird bei Aktivierung aus dem Inventar entfernt; die Wirkung wird als separater Zustand am Spieler geführt.
- **Nur eigene Gewinne:** Der Magnet verdoppelt ausschließlich die Münz-Gewinne des **aktivierenden Spielers**. Gewinne anderer Spieler bleiben unverändert.

### 3.3 Dauer und Zähler

- **Gesamtdauer:** 3 eigene Züge des Spielers (aktueller + 2 nächste).
- **Zählweise:** Der Zähler dekrementiert am **Ende jedes eigenen Zugs** des Spielers, während der Magnet aktiv ist.
- **Anzeige:** Unter dem Spieler-HUD erscheint das **Münz-Magnet-Icon mit einem Zähler**. Bei der Aktivierung lautet die Anzeige **"2 Züge verbleibend"** (die 2 Züge *nach* dem aktuellen).
- **Zählerschema:**

| Eigener Zug des Spielers | Anzeige zu Zugbeginn | Am Zugende |
|---|---|---|
| Aktivierung (Zug 1) | "2 Züge verbleibend" | Zähler wird 1 |
| Zug 2 | "1 Zug verbleibend" | Zähler wird 0 |
| Zug 3 | "Letzter Zug!" (0) | **Effekt endet** |

- **Wirkung im Zug 3:** Der Feld-Effekt des 3. Zugs wird noch verdoppelt; erst **nach** Abschluss des 3. Zugs endet die Wirkung.
- **Minispiel-Zeitfenster:** Minispiele finden nach den Zügen aller Spieler statt (siehe `core-loop.md`). Die Magnet-Wirkung ist ein **realzeitliches Fenster** von der Aktivierung bis zum Ende des 3. eigenen Zugs. Daraus folgt:
  - Das **Minispiel direkt nach der Runde der Aktivierung** liegt im Fenster (die nächsten 2 eigenen Züge stehen noch aus) → Belohnung wird verdoppelt.
  - Das **Minispiel nach dem 3. eigenen Zug** liegt außerhalb des Fensters (Wirkung endete mit dem 3. Zug) → Belohnung wird **nicht** verdoppelt.
- **8-Spieler-Fall:** Bei 8 Spielern können zwischen zwei eigenen Zügen bis zu 7 fremde Züge liegen. Der Magnet deckt daher real bis zu **24 fremde Züge** ab (3 eigene Züge × 8 Spieler, inkl. der eigenen), bevor er abläuft.

### 3.4 Verdopplungs-Matrix (Eligibility)

| Quelle | Verdoppelt? |
|---|---|
| Münz-Bonus-Feld (`field-coin-bonus`) | **Ja** |
| Glück-Feld, positives Ergebnis | **Ja** |
| Glück-Feld, negatives Ergebnis (Pech) | **Nein** (bleibt normal; wird nicht halbiert, nicht verdoppelt) |
| Minispiel-Belohnung | **Ja** |
| Event-Münzen (positive Grants) | **Ja** |
| Event, negative Münzwirkung | **Nein** (bleibt normal) |
| Gestohlene Münzen (Dieb-Handschuh) | **Nein** |
| Stern-Kauf (Ausgabe) | **Nein** (Preis bleibt 20) |
| Item-Kauf (Ausgabe) | **Nein** (Preise bleiben fix) |

**Regel:** Verdoppelt werden nur **Gewinne** (Zuflüsse) aus den vier positiven Quellen. **Ausgaben und Verluste** werden nie verändert.

### 3.5 Stacking- und Kombinationsregeln

| Kombination | Erlaubt? | Verhalten |
|---|---|---|
| Zweiter Münz-Magnet während aktiver Wirkung | **Nein** (kein Stacking) | Erneute Aktivierung verbraucht das Item, verlängert die Wirkung aber **nicht** und stapelt nicht (Meldung "Magnet ist bereits aktiv"). |
| Magnet + Glücks-Würfel | **Ja** | Beide in Phase 0; der Glücks-Würfel ersetzt den Wurf, der Magnet verdoppelt Gewinne des Zielfelds. |
| Magnet + Stern-Teleporter | **Ja** | Teleporter-Zug zählt als Magnet-Zug (Zähler dekrementiert); der Stern-Kauf wird **nicht** verdoppelt. |
| Magnet + Dieb-Handschuh | **Ja** | Gestohlene Münzen werden **nicht** verdoppelt. |
| Magnet + Schutzschild | **Ja** | Unabhängig; Schild blockt Pech-Verluste, die ohnehin nie verdoppelt werden. |

### 3.6 Animation

1. Der Charakter hält den Münz-Magnet (Metall-Magnet mit Münz-Symbol) hoch.
2. **Aktivierung:** Alle Münzen in der Nähe (visuell auch Münzen auf Feldern/Minispiel) schweben kurz auf und strömen **magnetisch zum Charakter**.
3. **Dauerhafte Anzeige:** Während der Wirkung schwebt das Magnet-Icon mit Zähler unter dem Spieler-HUD; der Charakter hat einen dezenten Magnet-Glanz.
4. **Gewinn-Momente:** Bei jedem verdoppelten Gewinn fliegen die Münzen sichtbar in doppelter Menge zum Charakter.
5. **Ende:** Das Icon erlischt, sobald der Zähler abläuft.

**Zeitbudget:** Aktivierungssequenz ≤ 2 Sekunden; die Daueranzeige ist persistent.

### 3.7 Spielende

- Wird der Magnet im letzten Zug des Spiels aktiviert oder ist er beim Spielende noch aktiv, **verfällt** die Restwirkung ersatzlos. Es gibt keine Auszahlung oder Bonuspunkte.

---

## 4. Formulas

### F1 — Verdopplung eines Gewinns

**Benannter Ausdruck:**

```
gain' = gain * 2   falls eligible(gain) = 1 UND magnet_active = 1
gain' = gain        sonst
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| gain | int | ≥ 0 | Basis-Münz-Gewinn vor Verdopplung |
| eligible(gain) | bool | {0, 1} | Quelle ist eine der vier verdoppelbaren Quellen (siehe §3.4) |
| magnet_active | bool | {0, 1} | Magnet-Wirkung im aktuellen Zeitfenster aktiv |
| gain' | int | ≥ 0 | Ausgezahlter Gewinn |

**Ausgabebereich:** gain' ∈ {gain, 2×gain}. Kein Wert dazwischen; Verluste/Ausgaben werden nie verändert.

**Arbeitsbeispiel:** Münz-Bonus-Feld gewährt 10 Münzen, Magnet aktiv → `gain' = 10 × 2 = 20`. Ein Pech-Verlust von 5 Münzen → `eligible = 0` → `gain' = 5` (der Spieler verliert 5, nicht 10 und nicht 2,5).

### F2 — Verbleibender Zähler

**Benannter Ausdruck:**

```
display = 2 - completed_own_turns_after_activation   // 0 wird als "Letzter Zug!" angezeigt
magnet_active = (completed_own_turns_after_activation < 3)
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| completed_own_turns_after_activation | int | 0–3 | Anzahl der eigenen Züge, die seit der Aktivierung abgeschlossen wurden |
| display | int | 0–2 | Anzeigewert "N Züge verbleibend" |
| magnet_active | bool | {0, 1} | Wirkung aktiv |

**Ausgabebereich:** display ∈ {2, 1, 0}; magnet_active wechselt nach dem 3. abgeschlossenen eigenen Zug auf 0.

**Arbeitsbeispiel:** Aktivierung in Zug 1: `completed = 0` → `display = 2` ("2 Züge verbleibend"). Nach Zug 1: `completed = 1` → `display = 1`. Nach Zug 2: `completed = 2` → `display = 0` ("Letzter Zug!"). Nach Zug 3: `completed = 3` → `magnet_active = 0`, Effekt endet.

### F3 — Realzeitliche Abdeckung bei N Spielern

**Benannter Ausdruck:**

```
max_wall_turns = 3 * N
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| N | int | 2–8 | Anzahl der Spieler |
| 3 | int | fix | Dauer in eigenen Zügen |
| max_wall_turns | int | 6–24 | Maximale Anzahl fremder+ eigener Züge, die real zwischen Aktivierung und Ablauf liegen |

**Ausgabebereich:** 6 (bei 2 Spielern) bis 24 (bei 8 Spielern).

**Arbeitsbeispiel:** N = 8 → `max_wall_turns = 3 × 8 = 24`. Der Magnet kann real bis zu 24 Züge abdecken, bevor der Spieler wieder dran ist.

### F4 — Strategischer Mindest-Return (Rentabilität)

**Benannter Ausdruck:**

```
break_even = magnet_price / 1   // jeder zusätzlich verdoppelte Gewinn von ≥ 1 Münze amortisiert
minimum_win_after_activation = ceil(magnet_price / 2)   // 2 Münzen, da 2× Gewinn = 1× Preis
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| magnet_price | int | 4 (fix) | Kaufpreis |
| minimum_win_after_activation | int | 2 (fix) | Nötiger Mindest-Gewinn in den 3 Zügen, damit sich der Kauf lohnt |

**Ausgabebereich:** Fixwerte für den Standardpreis.

**Arbeitsbeispiel:** Der Magnet kostet 4 Münzen. Ein einziger verdoppelter Gewinn von 2 Münzen (z. B. +2 → +4) erwirtschaftet die Extramünzen 2; der Magnet amortisiert sich bereits mit einem einzigen verdoppelten Gewinn von ≥ 2 Münzen und ist danach reiner Gewinn.

---

## 5. Edge Cases

| # | Fall | Konkretes Verhalten |
|---|---|---|
| E1 | Aktivierung im letzten Zug des Spiels | Wirkung startet, verfällt aber mit dem Spielende ersatzlos; keine Erstattung. |
| E2 | Erneute Aktivierung während aktiver Wirkung | Item wird verbraucht; Zähler wird **nicht** zurückgesetzt und **nicht** erhöht (Meldung "Magnet ist bereits aktiv"). |
| E3 | Pech-Feld während aktiver Wirkung | Verlust bleibt normal (z. B. −5, nicht −10, nicht −2,5). |
| E4 | Münz-Bonus im 3. Zug | Wird noch verdoppelt (der 3. Zug ist Teil der Wirkung). |
| E5 | Minispiel nach dem 3. Zug | Wird **nicht** verdoppelt (Fenster geschlossen). |
| E6 | Minispiel nach der Aktivierungsrunde | Wird verdoppelt (Fenster offen; die 2 nächsten eigenen Züge stehen noch aus). |
| E7 | Stern-Kauf während aktiver Wirkung | Preis bleibt 20; keine Verdopplung, kein Rabatt. |
| E8 | Item-Kauf während aktiver Wirkung | Preise bleiben fix; keine Verdopplung. |
| E9 | Dieb-Handschuh während aktiver Wirkung | Gestohlene Münzen werden nicht verdoppelt. |
| E10 | Aktivierung außerhalb von Phase 0 | Blockiert; Item bleibt im Inventar. |
| E11 | 8-Spieler-Partie, lange Pausen zwischen eigenen Zügen | Zähler dekrementiert nur bei eigenen Zügen; real können bis zu 24 Züge vergehen (F3). |
| E12 | Magnet + Teleporter im selben Zug | Erlaubt; der Teleporter-Zug zählt als eigener Zug (Zähler dekrementiert am Zugende); der Stern-Kauf wird nicht verdoppelt. |
| E13 | Gewinn durch Event außerhalb des eigenen Zugs | Nicht möglich: Events lösen nur im eigenen Feld-Effekt aus. Fremde Events betreffen andere Spieler und werden nicht verdoppelt. |
| E14 | Ungenutzter Magnet am Spielende | Verfällt ersatzlos. |

---

## 6. Dependencies

**Der Münz-Magnet ist abhängig von:**

| System | Art der Abhängigkeit |
|---|---|
| `item-system.md` | Kauf, Inventar, Phasen (Phase 0), HUD (Zähler), Verbrauch, Stacking-Regeln. |
| `coin-economy.md` | Alle Münz-Gewinne und -Verluste; Verdopplung von Zuflüssen; Kaufpreis (4). |
| `field-coin-bonus.md` | Bonus-Gewinne werden verdoppelt. |
| `field-luck.md` | Positive Ergebnisse verdoppelt; Pech-Verluste unverändert. |
| `field-minigame.md` | Minispiel-Belohnungen im Zeitfenster werden verdoppelt. |
| `field-event.md` | Event-Münzen (positiv) verdoppelt; negative Event-Münzen unverändert. |
| `star-economy.md` | Stern-Preis (20) wird nicht verdoppelt. |
| `item-thiefglove.md` | Gestohlene Münzen werden nicht verdoppelt. |
| `victory-conditions.md` | Spielende → Restwirkung verfällt. |
| `technical-data-structures.md` | Item-Datenstruktur (`item_id = coinmagnet`, `item_effect_type = delayed`); Zustandsführung des Zählers pro Spieler. |
| `ui-hud.md` | Magnet-Icon mit Zähler ("N Züge verbleibend"). |
| `audio-overview.md` / `audio-sfx.md` | Magnet-/Münz-Sounds. |

**Gegenrichtung (müssen in ihren Kapiteln auf den Münz-Magnet verweisen):**

- `coin-economy.md` → Ein Item kann Münz-Gewinne vorübergehend verdoppeln.
- `field-minigame.md` → Minispiel-Belohnungen können während eines aktiven Magneten verdoppelt ausgezahlt werden.
- `field-coin-bonus.md` / `field-luck.md` → Felder können durch ein Item verstärkte Auszahlungen erzeugen.
- `item-system.md` → listet den Magnet als eines der 5 aktiven Items (delayed).
- `field-item-shop.md` → verkauft den Magnet für 4 Münzen.

---

## 7. Tuning Knobs

| Knopf | Standard | Sicherer Bereich | Beeinflusste Gameplay-Größe |
|---|---|---|---|
| K1 Preis | 4 | 3–6 | Rentabilität und Kaufhäufigkeit; bei 3 wird der Magnet fast immer rentabel, bei 6 seltener. |
| K2 Dauer | 3 eigene Züge | 2–5 | Wie viele Gewinn-Momente abgedeckt werden; 5 Züge machen den Magnet dominant (deckt oft 2 Minispiele ab). |
| K3 Multiplikator | ×2 | ×1,5–×3 | Stärke pro Gewinn; ×3 kann die Wirtschaft stark verzerren, ×1,5 ist dezent. |
| K4 Verdoppelbares Set | 4 Quellen (siehe §3.4) | Set anpassbar | Hinzufügen/Entfernen von Quellen (z. B. "gestohlene Münzen verdoppeln" macht Dieb+ Magnet zu einem starken Combo). |
| K5 Stacking-Politik | keine Verlängerung | verfällt / verlängert auf max 3 | "Verlängert" (Refresh auf 3 Züge) belohnt Doppelkäufe; "verfällt" verhindert Dauerverdopplung. |
| K6 Zählbasis | eigene Züge | eigene Züge / Runden | "Runden" (3 Runden) wäre bei 8 Spielern deutlich mächtiger (bis zu 24 eigene Züge nicht möglich — daher nur eigene Züge als Standard). |
| K7 Minispiel-Einbeziehung | Minispiele im Zeitfenster verdoppelt | an / aus | "Aus" schwächt den Magnet spürbar (Minispiel-Belohnungen sind eine Hauptquelle). |

---

## 8. Acceptance Criteria

| ID | Kriterium | Pass-Bedingung |
|---|---|---|
| AC1 | Aktivierung | Der Magnet wird in Phase 0 aktiviert; danach zeigt das HUD-Icon "2 Züge verbleibend". |
| AC2 | Münz-Bonus-Verdopplung | Ein Münz-Bonus von +10 wird zu +20, solange der Magnet aktiv ist. |
| AC3 | Pech unverändert | Ein Pech-Verlust von −5 bleibt exakt −5. |
| AC4 | Minispiel-Verdopplung | Eine Minispiel-Belohnung von 8 wird zu 16, wenn das Minispiel im Zeitfenster liegt. |
| AC5 | Minispiel außerhalb | Eine Minispiel-Belohnung nach dem 3. eigenen Zug wird nicht verdoppelt. |
| AC6 | Stern-Preis unverändert | Ein Stern-Kauf kostet während der Wirkung exakt 20 Münzen. |
| AC7 | Item-Preis unverändert | Ein Item-Kauf kostet während der Wirkung den unveränderten Listenpreis. |
| AC8 | Zählerverlauf | Der Zähler zeigt 2 → 1 → 0 über die 3 eigenen Züge und erlischt danach. |
| AC9 | Nur eigene Gewinne | Gewinne anderer Spieler werden während der Wirkung nicht verdoppelt. |
| AC10 | Kein Stacking | Eine zweite Aktivierung während der Wirkung verlängert den Zähler nicht und stapelt nicht. |
| AC11 | 8-Spieler-Szenario | In einer 8-Spieler-Partie bleibt der Magnet über 3 eigene Züge aktiv, auch wenn dazwischen 7 fremde Züge liegen (real bis zu 24 Züge). |
| AC12 | Spielende | Ein beim Spielende aktiver Magnet verfällt ersatzlos. |
| AC13 | Animation | Münzen fliegen bei jedem verdoppelten Gewinn sichtbar magnetisch zum Charakter. |
| AC14 | Preis | Der Kaufpreis im Item-Shop beträgt exakt 4 Münzen. |
