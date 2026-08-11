# Item-System

**Status:** Final (v1.0)
**Gültig für:** Party Arena (PA), Godot 4.2, 2–8 Spieler
**Teil der Game Bible:** Teil III — Items (Rahmenkapitel)
**Detail-Kapitel:** `item-luckydice.md`, `item-teleporter.md`, `item-shield.md`, `item-coinmagnet.md`, `item-thiefglove.md`

---

## 1. Overview

Das Item-System ist das strategische Kauf-, Inventar- und Einsatzsystem für Einmal-Verbrauchsgüter in Party Arena. Spieler kaufen Items im **Item-Shop** (2 Felder pro Board, 40-Felder-Pfad) für Münzen, halten maximal **3 Items gleichzeitig** im Inventar und setzen sie im eigenen Zug ein, um Würfeln, Bewegung, Münz-Wirtschaft oder Gegner-Interaktion zu beeinflussen.

Das System umfasst genau **5 aktive Items**:

| Item | Preis (Münzen) | Effekt (Kurzform) | Effekt-Typ |
|---|---|---|---|
| Glücks-Würfel | 5 | Würfelt eine feste 5 statt 1–6 | immediate |
| Stern-Teleporter | 8 | Teleportiert zum Sternen-Shop statt Würfeln | immediate |
| Schutzschild | 6 | Blockt automatisch 1 negativen Effekt | passive |
| Münz-Magnet | 4 | Verdoppelt alle Münz-Gewinne für 3 eigene Züge | delayed |
| Dieb-Handschuh | 10 | Stiehlt 1 Item oder 5–15 Münzen von einem Gegner | immediate |

Alle Items sind **Einmal-Verbrauchsgüter**: Sie verschwinden nach ihrer Aktivierung (Schutzschild nach seiner Auslösung) aus dem Inventar. Es gibt **keine Item-Rarität** — im Shop sind alle 5 Items gleich häufig vertreten; pro Besuch werden 3 zufällige Items angeboten.

Das Item-System ist das Bindeglied zwischen der Münz-Wirtschaft (Kauf, Diebstahl, Verdopplung) und der Stern-Ökonomie (Teleporter, gezielte Erreichbarkeit von Sternen-Shops) und erweitert die Kern-Mechanik "Würfeln → Ziehen → Feld-Effekt" um eine strategische Entscheidungsebene.

---

## 2. Player Fantasy

Das Item-System erfüllt im Spielerlebnis mehrere Fantasien, die je Item unterschiedlich gewichtet sind:

- **Der berechnende Planer (Glücks-Würfel):** "Ich kontrolliere den Zufall." Statt zu hoffen, eine 1–6 zu würfeln, legt der Spieler exakt fest, wo er landet. Das Gefühl: kluges Positionieren, präzises Ansteuern des Sternen-Shops oder Item-Shops.
- **Der Teleport-Coup (Stern-Teleporter):** "Ich erscheine, wo man mich nicht erwartet." Der Spieler überspringt Bewegung und Risiko und taucht direkt am Sternen-Shop auf. Das Gefühl: überlegener Schachzug, gesicherter Stern-Kauf.
- **Der Unverwundbare (Schutzschild):** "Ich bin abgesichert." Das passive Sicherheitsgefühl, gegen Pech, negative Events und Diebstahl immun zu sein. Das Gefühl: Ruhe und Provokation ("versuch es ruhig").
- **Der Münz-Tycoon (Münz-Magnet):** "Münzen fliegen mir zu." Der sichtbare Reichtums-Effekt (Münzen strömen magnetisch zum Charakter), wenn Gewinne verdoppelt werden. Das Gefühl: wirtschaftlicher Rausch, Snowball, Kaufkraft.
- **Der Schurke (Dieb-Handschuh):** "Ich nehme mir, was mir zusteht." Der spielentscheidende, aggressive Moment: dem Führenden die Münzen oder ein Item wegnehmen und dadurch dessen Stern-Kauf verhindern. Das Gefühl: Schadenfreude, taktische Überlegenheit, Comeback-Potenzial.

Übergreifend erzeugt das System die Fantasie **"Vorbereitung schlägt Zufall"**: Wer Münzen klug in Items investiert, kann Würfelpech ausgleichen, Schlüsselpositionen erzwingen und die eigene Strategie absichern — ohne dass die Würfel ihren überraschenden Charakter verlieren.

---

## 3. Detailed Rules

### 3.1 Item-Typen und Datenstruktur

Es gibt genau 5 Item-Typen. Jedes Item wird durch eine einheitliche Datenstruktur beschrieben:

| Feld | Typ | Beschreibung |
|---|---|---|
| `item_id` | String (stabiler Schlüssel) | Eindeutiger, sprachunabhängiger Schlüssel (z. B. `luckydice`). Primärschlüssel für Code, Save-Daten und Balancing-Referenzen. |
| `item_name` | String (lokalisiert) | Anzeigename in der jeweiligen Sprache (z. B. "Glücks-Würfel"). |
| `item_price` | Integer | Kaufpreis in Münzen. |
| `item_description` | String (lokalisiert) | Kurzbeschreibung für Shop/HUD (max. 1 Satz). |
| `item_icon` | Asset-Referenz | Icon für Shop, HUD und Benachrichtigungen. |
| `item_effect_type` | Enum: `immediate` / `delayed` / `passive` | Steuert die Aktivierungslogik (siehe 3.1.1). |

**Konkrete Ausprägung aller 5 Items:**

| `item_id` | `item_name` | `item_price` | `item_description` | `item_effect_type` |
|---|---|---|---|---|
| `luckydice` | Glücks-Würfel | 5 | "Würfle eine feste 5 statt 1–6." | `immediate` |
| `teleporter` | Stern-Teleporter | 8 | "Teleportiere dich zu einem Sternen-Shop mit verfügbarem Stern." | `immediate` |
| `shield` | Schutzschild | 6 | "Blockt automatisch den nächsten negativen Effekt." | `passive` |
| `coinmagnet` | Münz-Magnet | 4 | "Verdoppelt alle Münz-Gewinne für 3 Züge." | `delayed` |
| `thiefglove` | Dieb-Handschuh | 10 | "Stiehl ein Item oder 5–15 Münzen von einem Gegner." | `immediate` |

**3.1.1 Bedeutung von `item_effect_type`:**

- **`immediate`:** Der Effekt tritt sofort und einmalig bei der Aktivierung ein. Beispiele: Glücks-Würfel (ersetzt den Wurf), Stern-Teleporter (Teleport), Dieb-Handschuh (Diebstahl). Das Item wird unmittelbar nach der Aktivierung verbraucht.
- **`delayed`:** Der Effekt wird bei Aktivierung gestartet und wirkt über einen definierten Zeitraum fort. Beispiel: Münz-Magnet (3 eigene Züge). Das Item wird bei Aktivierung verbraucht; der Nachwirkungs-Zustand wird separat geführt.
- **`passive`:** Der Effekt ist ab Erhalt dauerhaft aktiv und wird nie manuell ausgelöst. Beispiel: Schutzschild (wartet auf einen negativen Effekt). Das Item wird erst bei seiner Auslösung verbraucht.

### 3.2 Item-Pool und Item-Shop

- Jedes Board hat **2 Item-Shop-Felder** (siehe `field-item-shop.md`).
- Landet ein Spieler auf einem Item-Shop-Feld, öffnet sich der Shop. Der Shop zeigt **genau 3 verschiedene Items** aus dem Gesamt-Pool der 5 Items.
- **Pool-Auswahl pro Besuch:** Bei jedem neuen Besuch wird das 3er-Sortiment neu und gleichverteilt gezogen (siehe Formel F1). Zwei aufeinanderfolgende Besuche können also dasselbe oder ein anderes Sortiment zeigen.
- **Rarität:** Es gibt keine. Alle 5 Items sind gleich wahrscheinlich im Sortiment und immer zum festen Listenpreis erhältlich.
- **Kaufbedingungen:** Ein Kauf ist nur möglich, wenn (a) der Spieler genügend Münzen hat (Münzen ≥ Preis) und (b) das Inventar nicht voll ist (Inventar-Belegung < 3). Siehe Formel F3.
- **Mehrfachkäufe:** Der Spieler darf in einem Shop-Besuch mehrere Items kaufen, solange nach jedem Kauf die Inventar-Obergrenze von 3 eingehalten wird. Das Sortiment bleibt während eines Besuchs unverändert.
- **Kein Verkauf:** In dieser Version gibt es keinen Item-Verkauf zurück in Münzen (siehe Tuning-Knopf K6).

### 3.3 Inventar

- **Maximale Belegung:** 3 Items gleichzeitig. Ein vierter Kauf ist blockiert.
- **Reihenfolge:** Das Inventar ist eine geordnete Liste (Slot 1–3). Neue Items werden in den ersten freien Slot einsortiert.
- **Einmal-Verbrauch:** Nach der Aktivierung wird das Item aus dem Inventar entfernt. Der Schutzschild wird nicht bei Erhalt, sondern erst bei seiner Auslösung entfernt.
- **Öffentlichkeit:** Die Inventarinhalte aller Spieler sind im HUD für alle sichtbar (Transparenz; wichtig für Dieb-Handschuh- und Schutzschild-Entscheidungen).
- **Sichtbarkeit:** Das Inventar wird in 3 HUD-Slots angezeigt (siehe 3.8).

### 3.4 Aktivierung und Zugphasen

Jeder Spieler-Zug ist in folgende Phasen gegliedert. Items sind nur in ihrer definierten Phase aktivierbar:

| Phase | Name | Erlaubte Item-Aktivierung |
|---|---|---|
| Phase 0 | Item-Aktivierung **vor dem Würfeln** | Glücks-Würfel, Stern-Teleporter, Münz-Magnet |
| Phase 1 | Würfeln | — |
| Phase 2 | Item-Aktivierung **nach dem Würfeln, vor der Bewegung** | Dieb-Handschuh |
| Phase 3 | Bewegung | — |
| Phase 4 | Feld-Effekt | — (Käufe, Events, etc.) |

**Verbindliche Regeln:**

1. **Maximal 1 würfelersetzendes Item pro Zug:** Glücks-Würfel und Stern-Teleporter ersetzen beide den normalen Würfelwurf. Sie schließen sich gegenseitig aus; der Spieler kann nicht beide im selben Zug aktivieren.
2. **Münz-Magnet ist kombinierbar:** Der Münz-Magnet ist kein Würfel-Modifikator und kann in Phase 0 zusammen mit einem würfelersetzenden Item aktiviert werden.
3. **Dieb-Handschuh nur nach realem Wurf:** Der Dieb-Handschuh ist nur in Zügen aktivierbar, in denen tatsächlich gewürfelt und bewegt wird. In einem Teleporter-Zug (kein Würfeln, keine Bewegung) ist er nicht aktivierbar.
4. **Schutzschild ist rein passiv:** Er wird nie manuell aktiviert. Sein Schutz beginnt mit dem Eintritt ins Inventar (Kauf oder Event-Grant).
5. **Verbrauchszeitpunkt:** `immediate`- und `delayed`-Items werden bei Aktivierung verbraucht; `passive`-Items erst bei Auslösung.
6. **Aktivierungsvalidierung:** Vor jeder Aktivierung prüft das System, ob das Item in der aktuellen Phase und im aktuellen Spielzustand gültig ist (z. B. Teleporter nur bei verfügbarem Stern). Ist die Aktivierung ungültig, wird sie blockiert; das Item wird **nicht** verbraucht.
7. **Keine Aktivierung außerhalb des eigenen Zugs:** Items können nur in Phase 0 bzw. Phase 2 des eigenen Zugs verwendet werden. Schutzschild wirkt dagegen passiv auch außerhalb des eigenen Zugs (z. B. wenn ein anderer Spieler den Dieb-Handschuh einsetzt).

### 3.5 Item-Animationen

Jede Item-Nutzung wird durch eine animierte Sequenz begleitet, die den Effekt für alle Spieler sichtbar macht. Grundablauf (Rahmenregel):

1. **Aktivierungs-Moment:** Der Charakter führt eine Item-Geste aus (Item-Gegenstand erscheint in der Hand).
2. **Effekt-Phase:** Die itemspezifische Effekt-Animation läuft (Details in den jeweiligen Item-Kapiteln).
3. **Auflösung:** Der Effekt wird spielmechanisch angewendet und das Item aus dem Inventar entfernt (bzw. beim Schutzschild: zerbrochener Schild).

Die itemspezifischen Animationsspezifikationen:
- Glücks-Würfel: `item-luckydice.md` §3.4
- Stern-Teleporter: `item-teleporter.md` §3.4
- Schutzschild: `item-shield.md` §3.4
- Münz-Magnet: `item-coinmagnet.md` §3.4
- Dieb-Handschuh: `item-thiefglove.md` §3.4

Alle Animationen müssen in der festgelegten Zeitspanne abspielbar sein, ohne den Spielfluss zu blockieren (Ziel: ≤ 2,5 Sekunden Effektphase; Teleporter ≤ 3 Sekunden).

### 3.6 Items von Events

- Manche Ereignis-Felder können Items gewähren (siehe `field-event.md`). Die Ereignis-Definition legt fest, *welches* Item gewährt wird.
- **Inventar voll:** Kann ein gewährtes Item nicht ins Inventar gelegt werden (Belegung = 3), erhält der Spieler stattdessen eine **Kompensationszahlung** von `floor(item_price × 0.5)` Münzen. Siehe Formel F4.
- **Duplikat Schutzschild:** Ist ein Schutzschild bereits im Inventar und ein Event gewährt einen zweiten, erhält der Spieler ebenfalls die Kompensation (3 Münzen). Ein zweiter aktiver Schutzschild wird nie erzeugt (siehe 3.7 und `item-shield.md` §3.3).
- **Keine Kompensation für gekaufte Duplikate:** Die "Verschwendungs"-Regel gilt nur für Shop-Käufe (Schutzschild), nicht für Event-Grants (siehe `item-shield.md` §3.3).

### 3.7 Item-Übergabe (Diebstahl & Schutzschild)

- **Dieb-Handschuh stiehlt:** Der Dieb-Handschuh kann ein zufälliges Item aus dem Ziel-Inventar stehlen oder 5–15 Münzen (Details: `item-thiefglove.md`).
- **Schutzschild blockt:** Ein aktiver Schutzschild beim Ziel blockt den Diebstahl vollständig — sowohl Item-Diebstahl als auch Münz-Diebstahl. Dabei werden **beide** Items verbraucht (Handschuh und Schild). Es findet kein Transfer statt.
- **Reihenfolge-Klarstellung:** Der Schutzschild blockt *jede* Diebstahl-Form des Handschuhs, nicht nur den Item-Diebstahl. Dies ist eine bewusste Vereinheitlichung der Regel in `item-shield.md` §3.1 und `item-thiefglove.md` §3.2.

### 3.8 HUD & Eingabe

- **Anzeige:** Das Inventar wird als **3 Slots** im HUD dargestellt (unterhalb der Spieler-Informationen). Jeder Slot zeigt das Item-Icon; leere Slots sind ausgegraut.
- **Tastatur:** Die Tasten **1 / 2 / 3** aktivieren das Item im jeweiligen Slot (Slot 1 → Taste 1, usw.).
- **Gamepad:** **LB / RB** bewegen die Slot-Markierung (Auswahl) zyklisch durch die 3 Slots; **A** bestätigt die Aktivierung des markierten Slots.
- **Aktivierungsfenster:** Die Slots sind nur während der eigenen Phasen 0 und 2 interaktiv. In anderen Phasen oder außerhalb des eigenen Zugs sind die Tasten wirkungslos.
- **Ungültige Aktivierung:** Ist das markierte Item im aktuellen Zustand nicht aktivierbar (z. B. Teleporter ohne verfügbaren Stern), wird bei Bestätigung eine Begründung angezeigt ("Kein Stern verfügbar") und nichts verbraucht.
- **Schutzschild-Anzeige:** Ein aktiver Schutzschild wird als dauerhaftes Passiv-Icon (nicht als aktivierbarer Slot) im HUD angezeigt, z. B. mit einem Glanz-Rahmen.

---

## 4. Formulas

### F1 — Shop-Pool-Auswahl (3 aus 5 ohne Zurücklegen)

**Benannter Ausdruck:**

```
P = ChooseWithoutReplacement(A, 3)
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| A | Menge | |A| = 5 | Gesamtmenge aller Items (5 Stück) |
| 3 | int | fix | Anzahl der im Shop angebotenen Items |
| P | Menge | |P| = 3 | Konkretes Sortiment eines Besuchs |
| Ω | Menge | |Ω| = C(5,3) = 10 | Ergebnisraum aller möglichen Sortimente |

**Ausgabebereich:** Genau 10 mögliche Sortimente, alle gleich wahrscheinlich (1/10 = 10 %). Jedes Sortiment enthält 3 verschiedene Items.

**Arbeitsbeispiel:** Spieler besucht den Shop. Es werden 3 der 5 Items ohne Zurücklegen gezogen. Mögliches Ergebnis: {Glücks-Würfel, Schutzschild, Münz-Magnet}. Die Wahrscheinlichkeit für genau dieses Sortiment beträgt 1/10.

### F2 — Einzel-Item-Verfügbarkeit pro Shop-Besuch

**Benannter Ausdruck:**

```
p_item = C(N-1, k-1) / C(N, k)
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| N | int | 5 (fix) | Gesamtzahl der Items im Pool |
| k | int | 3 (fix) | Sortimentsgröße des Shops |
| p_item | float | 0–1 | Wahrscheinlichkeit, dass ein bestimmtes Item im Sortiment liegt |
| C(a,b) | int | — | Binomialkoeffizient "a über b" |

**Ausgabebereich:** 0 ≤ p_item ≤ 1. Für N=5, k=3 ergibt sich p_item = C(4,2)/C(5,3) = 6/10 = **0,60**.

**Arbeitsbeispiel:** Der Glücks-Würfel erscheint in 6 der 10 möglichen Sortimente. Über viele Besuche hinweg wird er in ca. 60 % der Besuche angeboten.

### F3 — Kauf-Validierung

**Benannter Ausdruck:**

```
can_buy = (inventory_count < 3) AND (player_coins >= item_price)
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| inventory_count | int | 0–3 | Anzahl der Items im Inventar des Spielers |
| 3 | int | fix | Inventar-Obergrenze |
| player_coins | int | ≥ 0 | Münzkontostand des Spielers |
| item_price | int | 4–10 | Preis des Items (definierte Preise) |
| can_buy | bool | {0,1} | Kauf erlaubt |

**Ausgabebereich:** Bool. Kauf nur bei gleichzeitig erfüllten Bedingungen.

**Arbeitsbeispiel:** Spieler hat 2 Items im Inventar und 12 Münzen. Glücks-Würfel (Preis 5): can_buy = (2 < 3) AND (12 ≥ 5) = wahr. Nach dem Kauf: inventar_count = 3, player_coins = 7. Ein weiterer Kauf ist bis zur nächsten Verwendung blockiert.

### F4 — Kompensationszahlung (Event-Grant bei vollem Inventar oder Duplikat)

**Benannter Ausdruck:**

```
compensation = floor(item_price * 0.5)
```

| Symbol | Typ | Bereich | Beschreibung |
|---|---|---|---|
| item_price | int | 4–10 | Listenpreis des nicht annehmbaren Items |
| compensation | int | 2–5 | Ausgezahlte Münzen (abgerundet) |
| floor(x) | float→int | — | Abrunden auf ganze Münzen |

**Ausgabebereich:** {2, 3, 4, 5} — abhängig vom Item.

**Arbeitsbeispiel:** Inventar ist voll und ein Event gewährt einen Stern-Teleporter (Preis 8): compensation = floor(8 × 0.5) = **4 Münzen**. Konkret: Glücks-Würfel 5→2, Teleporter 8→4, Schutzschild 6→3, Münz-Magnet 4→2, Dieb-Handschuh 10→5.

### Interaktionsmatrix: Items × Systeme

| System | Glücks-Würfel | Teleporter | Schutzschild | Münz-Magnet | Dieb-Handschuh |
|---|---|---|---|---|---|
| Würfeln & Bewegung (`dice-movement`) | Ersetzt Wurf (5) | Ersetzt Wurf + Bewegung | — | — | — |
| Sternen-Shop (`field-star-shop`) | Ziel-Erreichung | Ziel / Ankunft | — | Preis nicht verdoppelt | Münzen klauen (Kauf verhindern) |
| Item-Shop (`field-item-shop`) | Kauf | Kauf | Kauf (Duplikat verfällt) | Kauf | — |
| Ereignis-Feld (`field-event`) | Verdoppler → 10 | — | Blockt negative Events | Event-Münzen verdoppelt | — |
| Glück/Pech (`field-luck`) | — | — | Blockt Pech-Verlust | Positiv verdoppelt, Pech normal | — |
| Münz-Bonus (`field-coin-bonus`) | — | — | — | Verdoppelt | — |
| Minispiel (`field-minigame`) | — | — | — | Belohnung verdoppelt | — |
| Spieler-Interaktion | — | — | Blockt Diebstahl | — | Stiehlt Items/Münzen |

---

## 5. Edge Cases

| # | Fall | Konkretes Verhalten |
|---|---|---|
| E1 | Inventar voll (3 Items), Spieler will kaufen | Kauf blockiert; Shop-Button inaktiv; Meldung "Inventar voll". Kein Münzabzug. |
| E2 | Münzen < Item-Preis | Kauf blockiert; Button inaktiv; Meldung "Nicht genug Münzen". |
| E3 | Shop bietet ein Item an, das der Spieler bereits besitzt | Weiterhin kaufbar, sofern Platz und Münzen vorhanden. Stacking-Regeln pro Item greifen (z. B. Schutzschild-Duplikat verfällt, siehe `item-shield.md` §3.3). |
| E4 | Item von Event bei vollem Inventar | Item wird nicht angenommen; Spieler erhält Kompensation F4. |
| E5 | Event gewährt zweiten Schutzschild | Kompensation F4 (3 Münzen); kein zweiter aktiver Schild. |
| E6 | Aktivierungsversuch in falscher Phase (z. B. Dieb-Handschuh in Phase 0) | Aktivierung blockiert; Item bleibt im Inventar; Hinweis auf korrekte Phase. |
| E7 | Teleporter ohne verfügbaren Stern | Aktivierung blockiert; Item bleibt im Inventar (siehe `item-teleporter.md` §5). |
| E8 | Münz-Magnet erneut aktiviert, während er aktiv ist | Item wird verbraucht, Effekt wird **nicht** verlängert oder gestapelt (Meldung "Magnet ist bereits aktiv"). |
| E9 | Glücks-Würfel + Würfel-Verdoppler-Event | Wurfergebnis 10 statt 5 (siehe `item-luckydice.md` §4). |
| E10 | Dieb-Handschuh, aber kein gültiges Ziel (alle Gegner auf Startfeld) | Aktivierung blockiert; Item bleibt im Inventar. |
| E11 | Spielende mit aktivem Münz-Magnet oder ungenutztem Schutzschild | Restliche Wirkung verfällt; keine Erstattung. |
| E12 | Dieb-Handschuh in einem Teleporter-Zug | Nicht aktivierbar (kein Würfeln/Bewegen in diesem Zug). |
| E13 | Zwei würfelersetzende Items im selben Zug (Glücks-Würfel + Teleporter) | Nur eines aktivierbar; das zweite wird in Phase 0 blockiert. |
| E14 | Kauf eines zweiten Schutzschilds im Shop | Kauf ist möglich (Münzen werden abgezogen), das zweite Schild verfällt sofort wirkungslos; Meldung "Du hast bereits einen Schutzschild!". Kein zweiter Slot. |

---

## 6. Dependencies

**Das Item-System ist abhängig von:**

| System | Art der Abhängigkeit |
|---|---|
| `coin-economy.md` | Kauf (Münzabzug), Dieb-Handschuh (Münz-Transfer), Münz-Magnet (Verdopplung). |
| `star-economy.md` | Stern-Preis (20, nicht verdoppelt), Teleporter-Ziel, Stern wandert nach Kauf. |
| `dice-movement.md` | Zugphasen (Phase 0/1/2/3), Würfelersatz, Bewegung bis Wert 10 (Glücks-Würfel + Verdoppler). |
| `board-architecture.md` | 2 Item-Shop-Felder pro Board, Feld-Positionen. |
| `field-item-shop.md` | Shop-UI, Sortiment, Kaufablauf. |
| `field-event.md` | Events gewähren Items; negative Events werden vom Schutzschild geblockt. |
| `field-luck.md` | Pech-Verlust (Schild blockt), positiver Gewinn (Magnet verdoppelt). |
| `field-coin-bonus.md` | Bonus-Gewinne (Magnet verdoppelt). |
| `field-minigame.md` | Minispiel-Belohnungen (Magnet verdoppelt). |
| `ui-hud.md` | 3 Inventar-Slots, Tasten 1/2/3, Gamepad LB/RB + A, Schild-Icon. |
| `ui-shop.md` | Kauf-UI, Pool-Anzeige, Blockade-Meldungen. |
| `victory-conditions.md` | Spielende → verzögerte Effekte verfallen. |
| `technical-data-structures.md` | Item-Datenstruktur (6 Felder), Zustandsverwaltung. |
| `audio-overview.md` / `audio-sfx.md` | Item-Sounds und Aktivierungs-Feedback. |
| `accessibility` (`ui-accessibility.md`) | Alternative Eingabewege für Item-Aktivierung (Ein-Tasten-Modus). |

**Gegenrichtung (müssen in ihren Kapiteln auf das Item-System verweisen):**

- `coin-economy.md` → Item-Käufe, Münz-Diebstahl, Verdopplung.
- `star-economy.md` → Teleporter erzeugt zusätzliche Stern-Kauf-Gelegenheiten.
- `dice-movement.md` → Items können den Würfelwurf ersetzen oder den Wert auf 10 anheben.
- `board-architecture.md` / `field-item-shop.md` → Der Item-Shop verkauft die 5 definierten Items.
- `field-event.md` → Events können Items gewähren und werden teils vom Schild blockt.
- `ui-hud.md` → Inventar-Anzeige und Item-Aktivierungseingaben.
- `technical-data-structures.md` → Implementiert die Item-Datenstruktur.

---

## 7. Tuning Knobs

| Knopf | Standard | Sicherer Bereich | Beeinflusste Gameplay-Größe |
|---|---|---|---|
| K1 Item-Preise (pro Item) | 5 / 8 / 6 / 4 / 10 | 3–12 je Item | Kaufhäufigkeit, Münz-Druck, Wirtschaftstempo. Höhere Preise verzögern Item-Einsatz, niedrigere beschleunigen ihn. |
| K2 Inventar-Obergrenze | 3 | 2–4 | Strategische Tiefe und Bevorratung. Höher = mehr Flexibilität, geringeres Risiko; niedriger = härtere Entscheidungen. |
| K3 Sortimentsgröße des Shops | 3 | 2–4 | Verfügbarkeit einzelner Items (F2). Mehr = gezieltere Beschaffung. |
| K4 Pool-Refresh | pro Besuch | pro Besuch / pro Runde / fix pro Spiel | Vorhersehbarkeit und Shop-Strategie. "Fix pro Spiel" erhöht Planbarkeit, "pro Besuch" erhöht Zufall. |
| K5 Kompensationsrate (Event-Grant) | 50 % | 25–100 % | Fairness bei vollem Inventar; verhindert Frustration durch Event-Grants. |
| K6 Item-Verkauf | aus | optional (50 % Rückkauf) | Liquidität; verhindert "totes Inventar", senkt aber Risiko von Fehlkäufen. |
| K7 Item-Shops pro Board | 2 | 2–3 | Zugangshäufigkeit zu Items; beeinflusst die Item-Dichte einer Partie. |
| K8 Würfel-Verdoppler-Interaktion | an | an / aus | Macht Glücks-Würfel situationsabhängig stärker (10er-Wurf). |
| K9 Dieb-Handschuh: Startfeld-Immunität | an | an / aus | Schutz des Rückstands; schwächt den Dieb-Handschuh als reines Aggressions-Tool. |

---

## 8. Acceptance Criteria

Die folgenden Kriterien müssen von einem QA-Tester ohne Spezialwissen prüfbar sein (Pass/Fail):

| ID | Kriterium | Pass-Bedingung |
|---|---|---|
| AC1 | Sortimentsgröße | Jeder Item-Shop-Besuch zeigt genau **3 verschiedene** Items aus den 5. |
| AC2 | Preis-Korrektheit | Die angezeigten Preise sind exakt: Glücks-Würfel 5, Teleporter 8, Schutzschild 6, Münz-Magnet 4, Dieb-Handschuh 10. |
| AC3 | Häufigkeit im Sortiment | In 100 simulierten Shop-Besuchen erscheint jedes Item in 50–70 Besuchen (Erwartung 60). |
| AC4 | Kauf und Inventar | Ein Kauf zieht den Preis ab, legt das Item in den ersten freien Slot und ist bei Belegung = 3 blockiert. |
| AC5 | Kauf-Sperren | Bei zu wenig Münzen und bei vollem Inventar ist der Kauf-Button inaktiv; kein Münzabzug. |
| AC6 | Datenstruktur | Jedes der 5 Items hat vollständige Werte für `item_id`, `item_name`, `item_price`, `item_description`, `item_icon`, `item_effect_type`. |
| AC7 | HUD-Slots | Das HUD zeigt genau 3 Inventar-Slots; leere Slots sind ausgegraut. |
| AC8 | Tastatur-Aktivierung | Die Tasten 1/2/3 aktivieren das Item des jeweiligen Slots ausschließlich in der korrekten Phase. |
| AC9 | Gamepad-Aktivierung | LB/RB bewegen die Slot-Markierung; A aktiviert; außerhalb der Phase keine Wirkung. |
| AC10 | Einmal-Verbrauch | Nach Aktivierung ist das Item aus dem Inventar entfernt; der Schutzschild erst nach Auslösung. |
| AC11 | Event-Grant | Ein Event-Item bei vollem Inventar erzeugt eine Kompensation gemäß F4 und kein Inventar-Item. |
| AC12 | Duplikat-Schutzschild (Kauf) | Der Kauf eines zweiten Schutzschilds zieht Münzen ab, erzeugt aber keinen zweiten aktiven Schild und belegt keinen Slot. |
| AC13 | Items von Events | Mindestens ein Ereignis-Feld gewährt nachweislich ein Item. |
| AC14 | Schild blockt Diebstahl | Ein Dieb-Handschuh gegen ein Schild-Ziel erzeugt keinen Transfer; Handschuh und Schild sind danach verbraucht. |
| AC15 | Ungültige Aktivierung schont Item | Jede blockierte Aktivierung (falsche Phase, Teleporter ohne Stern, kein gültiges Ziel) lässt das Item unverbraucht im Inventar. |
