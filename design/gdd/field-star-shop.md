# Sternen-Shop — Party Arena Game Bible

> **Teil:** 2 — Board & Fields
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/game-bible-prompt.md

---

## 1. Overview

Der Sternen-Shop (Feldtyp STERN_SHOP) ist der Ort, an dem Spieler Sterne kaufen — die Siegwährung von Party Arena. Jedes Board besitzt 2–3 Sternen-Shop-Felder an festen Positionen auf dem Hauptpfad. Ein Stern kostet im Standard 20 Münzen. Jeder Shop hält genau einen Stern; nach dem Kauf wandert die Sternen-Statue (das markierte „aktuelle" Stern-Angebot) zum nächsten Sternen-Shop-Feld in Pfadreihenfolge. Sind alle Sterne einer Runde verkauft, bleiben die Shops leer und werden am Rundenende wieder aufgefüllt. Ereignisse können den Sternpreis temporär um ±5 Münzen modifizieren. Pro Kauf wird maximal 1 Stern erworben; der Kauf ist optional — ein Spieler kann ablehnen. ArenaStar erscheint beim Betreten und bietet den Stern an.

## 2. Player Fantasy

Der Sternen-Shop ist das große Ziel jeder Partie: ein goldener Sockel mit schwebendem, glänzendem Stern, inszeniert als „der Preis" der Runde. Wer das Feld betritt, erlebt einen Moment der Spannung und Entscheidung: „Kann ich ihn mir leisten? Soll ich sparen oder zuschlagen?" Der wandernde Stern (die Statue zieht nach jedem Kauf zum nächsten Shop) erzeugt das Gefühl, dass der Stern einem davoneilt — man muss ihn an der richtigen Stelle erwischen. Der Kauf selbst ist ein triumphaler Moment: Der Stern verschwindet mit Partikeleffekt, die Münzen sinken, der eigene Sternvorrat wächst. Die Player Fantasy ist die eines Jägers, der das wertvollste Objekt der Insel erbeutet.

## 3. Detailed Rules

### 3.1 Anzahl und Position

- Pro Board existieren `N_STERN_SHOP ∈ {2, 3}` Sternen-Shop-Felder.
- Die Positionen sind fest, werden im Board-Manifest (`star_shop_order`) in Pfadreihenfolge hinterlegt und liegen IMMER auf dem Hauptpfad (nie auf Abzweigungen).
- Referenz-Layout: Statue #1 bei Index 12, Statue #2 bei Index 26. Alternative Beispielpositionen (Konzept): 10, 20, 35 für 3 Shops.
- Die Reihenfolge der Statuen-Wanderung ist die Pfadreihenfolge (aufsteigende Loop-Distanz), zyklisch über den Loop.

### 3.2 Stern-Bestand pro Shop

- Jeder Sternen-Shop hält genau 0 oder 1 Stern.
- Zu Rundenbeginn (nach der Rundenende-Wartung der Vorrunde) gilt: Jeder Shop hat genau 1 Stern.
- Wird der Stern eines Shops gekauft, sinkt dessen Bestand auf 0. Der Shop bleibt leer, bis die Rundenende-Wartung ihn auffüllt.
- „Alle Sterne gekauft" bedeutet: Alle `N_STERN_SHOP` Shops haben Bestand 0.

### 3.3 Statuen-Wanderung

- Wird ein Stern bei Shop j gekauft, wandert die Sternen-Statue zum nächsten Shop in Pfadreihenfolge: `(j + 1) mod N_STERN_SHOP`.
- Mechanische Bedeutung: Das Spiel markiert den nächsten Shop, der noch einen Stern besitzt, als „aktuelles Stern-Angebot" (Highlight, Pfeil, ArenaStar-Kommentar). Besitzt der nächste Shop bereits seinen eigenen Stern, ist er einfach der neue markierte Shop.
- Besitzt KEIN Shop mehr einen Stern (alle verkauft), gibt es kein markiertes Angebot; alle Shops zeigen den geschlossenen Zustand bis zur Rundenende-Wartung.
- Die Statue ist also eine visuelle/thematische Markierung des nächsten verfügbaren Sterns; der Sternbestand je Shop bleibt unabhängig davon korrekt (0 oder 1).

### 3.4 Preis und Kauf

- Standardpreis: `STAR_PRICE = 20` Münzen.
- Effektiver Preis: `P_eff = STAR_PRICE + EVENT_MOD`, wobei `EVENT_MOD ∈ {−5, 0, +5}` durch Ereignisse gesetzt wird (einzelner Modifikator-Slot, field-event.md). Reset auf 0 in der Rundenende-Wartung.
- Kaufbedingungen: Spieler landet per Würfelzug auf einem STERN_SHOP-Feld, UND der Shop hat Bestand 1, UND der Spieler besitzt mindestens `P_eff` Münzen.
- Kaufvorgang:
  1. ArenaStar erscheint und bietet den Stern an (Dialog mit Preisangabe).
  2. Spieler wählt „Kaufen" oder „Ablehnen".
  3. Bei Kauf: Münzen werden abgezogen (`coins' = coins − P_eff`), der Spieler erhält 1 Stern, der Shop-Bestand wird 0, die Statue wandert (3.3), der Stern verschwindet mit Partikeleffekt.
- Maximal 1 Stern pro Kauf und pro Shop-Besuch. Ein Spieler kann in derselben Runde an verschiedenen Shops weitere Sterne kaufen, sofern er sie erreicht und genug Münzen hat (kein Standard-Limit; optionaler Tuning-Knob, siehe Sektion 7).
- Der Kauf ist optional: Ablehnen ist jederzeit möglich, der Stern bleibt im Shop für den nächsten Besucher.

### 3.5 Unzureichende Münzen

- Besitzt der Spieler weniger Münzen als `P_eff`, zeigt ArenaStar die Meldung: „Du hast nicht genug Münzen! Du brauchst X." (X = `P_eff`, Standard 20).
- Die Kauf-Option ist deaktiviert; der Spieler verlässt den Shop ohne Kauf. Der Stern bleibt verfügbar.

### 3.6 Shop geschlossen

- Hat der Shop Bestand 0 (Stern wurde diese Runde bereits gekauft), wird beim Betreten die Shop-geschlossen-Animation abgespielt (dunkler/leerer Sockel, „GESCHLOSSEN"-Schild). Es gibt kein Angebot und keinen Kauf-Dialog.

### 3.7 Preis-Modifikation durch Ereignisse

- Ereignisse können `EVENT_MOD` auf −5 („Stern-Rabatt": Preis 15) oder +5 (Preis 25) setzen.
- Der Modifikator gilt global für alle Sternen-Shops, bis zur Rundenende-Wartung.
- Mehrfache Ereignisse stapeln nicht; ein neues Ereignis überschreibt den Wert.
- Der angezeigte Preis ist immer der aktuelle `P_eff`.

### 3.8 Auffüllen am Rundenende

- In der Rundenende-Wartung (board-architecture.md 3.12.4b) wird jeder Shop mit Bestand 0 auf Bestand 1 gesetzt. Shops mit Bestand 1 bleiben unverändert (kein Doppel-Stern).
- Die Statuen-Markierung wird neu auf den ersten Shop in Pfadreihenfolge gesetzt, der einen Stern besitzt.

### 3.9 Visuelle und auditive Darstellung

- Visual: goldener Sockel mit schwebendem, rotierendem Stern; leuchtender Strahlenkranz.
- Nach Kauf: Der Stern verschwindet mit Glitzer-/Schwupp-Effekt; der Sockel bleibt leer.
- Geschlossener Zustand: Sockel abgedunkelt, kein Stern, „GESCHLOSSEN"-Schild.
- Audio-Cue: glockenartiger „Kauf"-Sound, Fanfare beim Stern-Gewinn (audio-sfx.md, geplant).

## 4. Formulas

Variablendefinitionen:
- `N_STERN_SHOP ∈ {2, 3}` — Anzahl der Sternen-Shops.
- `STAR_PRICE = 20` — Standardpreis (Bereich 10–30).
- `EVENT_MOD ∈ {−5, 0, +5}` — globaler Preis-Modifikator (Standard 0).
- `P_eff = STAR_PRICE + EVENT_MOD` — effektiver Preis.
- `bestand(j) ∈ {0, 1}` — Sternbestand von Shop j.
- `coins(p)` — Münzstand des Spielers p.

Kauf-Formel:
- Kauf gültig ⇔ `bestand(j) = 1` UND `coins(p) ≥ P_eff`.
- Nach Kauf: `coins' = coins − P_eff`; `bestand(j) = 0`; Statue → Shop `(j + 1) mod N_STERN_SHOP` mit `bestand = 1`.

Erwartungswerte:
- Standardkauf: `P_eff = 20`. Mit Rabatt: `P_eff = 15`. Mit Teuerung: `P_eff = 25`.
- Pro Runde sind maximal `N_STERN_SHOP` Sterne kaufbar (= 2 im Referenz-Layout).

Beispielrechnung:
- Spieler hat 23 Münzen, `EVENT_MOD = 0` → Kauf möglich: `23 − 20 = 3` Münzen bleiben.
- Spieler hat 14 Münzen, `EVENT_MOD = −5` (Preis 15) → Kauf NICHT möglich: „Du brauchst 15."
- Spieler hat 20 Münzen, `EVENT_MOD = +5` (Preis 25) → Kauf NICHT möglich.

## 5. Edge Cases

1. **Exakt 20 Münzen:** Kauf gelingt; Münzstand wird 0 (Clamp verhindert negative Stände ohnehin).
2. **Zwei Spieler im selben Shop in derselben Runde:** Der Erste kauft; der Zweite sieht den geschlossenen Zustand (Bestand 0).
3. **Statue wandert auf einen Shop, der noch seinen eigenen Stern hat:** Kein Doppel-Stern; der Shop ist einfach der neue markierte Shop.
4. **Alle Sterne einer Runde verkauft:** Alle Shops zeigen geschlossen; in der Rundenende-Wartung werden alle auf Bestand 1 gesetzt.
5. **Ereignis-Preismodifikation während eines laufenden Kauf-Dialogs:** Kann nicht eintreten, da Ereignisse nur bei Landungen ausgelöst werden und kein Ereignis während eines Dialogs prozessiert wird. Der Dialog zeigt immer den aktuellen `P_eff`.
6. **Dritter Shop (N_STERN_SHOP = 3):** Statuen-Wanderung ist zyklisch: nach Shop 3 folgt Shop 1.
7. **Effekt-Platzierung auf ein STERN_SHOP-Feld (z. B. Tausch-Basar):** Kein Shop-Besuch, kein Angebot, kein Kauf (Regel: Effekt-Platzierung löst keine Feld-Effekte aus).
8. **Überqueren eines STERN_SHOP-Feldes:** Kein Effekt; nur Landungen öffnen den Shop.
9. **AI-Spieler:** Kaufen nach derselben Regel; die Kauf-Entscheidung folgt der AI-Logik (Schwierigkeitsgrad), nicht den Menschen-Regeln.
10. **Stern-Bestand und Statue am Rundenende:** Auch wenn nicht alle Sterne verkauft wurden, bleiben nicht verkaufte Sterne liegen; nur leere Shops werden aufgefüllt.

## 6. Dependencies

### 6.1 Benötigt von `field-star-shop.md`

| Kapitel/System | Art | Verwendung |
|---|---|---|
| `board-architecture.md` | Voraussetzung | STERN_SHOP-Typ, Hauptpfad-Platzierung, `star_shop_order`, Rundenende-Wartung. |
| `field-event.md` | Quelle | Setzt `EVENT_MOD` (Stern-Rabatt +5/−5). |
| `coin-economy.md` (geplant) | Quelle | Münz-Clamp, Faucet/Sink-Bilanz (Sterne als größte Sink). |
| `star-economy.md` (geplant) | Quelle | Stern als Siegwährung, Gesamtbilanz über 8–10 Runden. |
| `narrative-arena-star.md` (geplant) | Quelle | Angebots-Dialoge und Kommentare. |
| `ui-shop.md` (geplant) | System | Kauf-UI, Preis-Anzeige, Bestätigungsdialog. |

### 6.2 Systeme, die von diesem Dokument abhängen

| Kapitel/System | Art der Abhängigkeit |
|---|---|
| `star-economy.md` (geplant) | Nutzt `P_eff`, Statuen-Wanderung und Refill als Kernregeln. |
| `victory-conditions.md` (geplant) | Zählt gekaufte Sterne als Siegkriterium. |
| `item-teleporter.md` (geplant) | Ziel des Stern-Teleporters ist die aktuelle Statuen-Position (markierter Shop). |
| `field-event.md` | Ereignis „Stern-Rabatt" hängt von `EVENT_MOD` und `P_eff` ab. |
| `ui-board.md` (geplant) | Zeigt Statuen-Highlight und Shop-Zustände. |

### 6.3 Bidirektionalität

`board-architecture.md` und `field-event.md` verweisen auf dieses Kapitel; dieses Kapitel verweist zurück. Wechselseitigkeit ist damit hergestellt.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|---|---|---|---|---|
| `STAR_PRICE` | Kurve | 10–30 | 20 | Tempo der Stern-Ökonomie; höherer Preis = längere Partie. |
| `N_STERN_SHOP` | Kurve | 2–3 | 2 | Stern-Verfügbarkeit pro Runde. |
| `EVENT_MOD`-Betrag | Kurve | 0–10 | 5 | Wirkung von Rabatt/Teuerung. |
| Kauf-Limit je Spieler pro Runde | Gate | kein / 1 | kein | Verhindert Stern-Hortung durch einen Spieler. |
| Refill-Timing | Kurve | jede Runde / alle 2 Runden | jede Runde | Steuert Stern-Knappheit. |
| Preis-Override je Shop (`fixed_value`) | Kurve | 0 (= Standard) oder 15–25 | 0 | Erlaubt inselspezifische Shop-Preise. |

## 8. Acceptance Criteria

Ein QA-Tester kann die folgenden Prüfungen ausführen:

1. **Anzahl/Position:** Jedes Board hat 2–3 STERN_SHOP-Felder auf dem Hauptpfad; `star_shop_order` ist in Pfadreihenfolge. PASS/FAIL.
2. **Kauf erfolgreich:** Spieler mit ≥ 20 Münzen landet auf einem Shop mit Bestand 1 → Kauf klappt, 1 Stern addiert, 20 Münzen abgezogen, Statue wandert zum nächsten Shop. PASS/FAIL.
3. **Kauf abgelehnt:** Spieler wählt „Ablehnen" → kein Münzabzug, Stern bleibt im Shop. PASS/FAIL.
4. **Zu wenig Münzen:** Spieler mit < `P_eff` sieht die Meldung „Du hast nicht genug Münzen! Du brauchst X." und kann nicht kaufen. PASS/FAIL.
5. **Geschlossener Shop:** Nach dem letzten Stern-Kauf der Runde zeigt der Shop die geschlossene Animation; kein Kauf-Dialog. PASS/FAIL.
6. **Refill:** Nach der Rundenende-Wartung haben alle Shops Bestand 1; nicht verkaufte Sterne bleiben. PASS/FAIL.
7. **Rabatt:** Ereignis „Stern-Rabatt" → `P_eff = 15`; Kauf mit 15 Münzen möglich; nach Rundenende wieder 20. PASS/FAIL.
8. **Max 1 Stern pro Kauf:** Ein einzelner Kauf-Vorgang vergibt exakt 1 Stern (keine Mehrfach-Käufe in einem Dialog). PASS/FAIL.
9. **Effekt-Platzierung:** Tausch-Basar auf ein STERN_SHOP-Feld öffnet keinen Shop. PASS/FAIL.
10. **Statue bei 3 Shops:** Zyklische Wanderung 1→2→3→1; markierter Shop ist immer der nächste mit Bestand 1. PASS/FAIL.
