# Ereignis-Feld — Party Arena Game Bible

> **Teil:** 2 — Board & Fields
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/game-bible-prompt.md

---

## 1. Overview

Das Ereignis-Feld (Feldtyp EREIGNIS) löst beim Landen ein zufälliges Ereignis aus der Ereignis-Kartei aus. Jedes Board besitzt 5–6 Ereignis-Felder an festen Positionen. Die Ereignis-Kartei umfasst mindestens 20 verschiedene Ereignisse, die kontext-sensitiv gefiltert und gewichtet gezogen werden (40 % kleine, 35 % mittlere, 20 % große, 5 % spielverändernde Ereignisse). Ereignisse wirken global auf alle Spieler oder gezielt auf einzelne; sie können Münzen, Items, Positionen und Würfel beeinflussen. ArenaStar kommentiert jedes Ereignis in einem Popup mit Name, Beschreibung und Kommentar. Die Kartei ist das wichtigste Instrument für Abwechslung, Catch-Up und „Chaos-Momente" einer Partie und übernimmt die erzählerischen Funktionen der entfernten STP-Figuren Nolok und GNU.

## 2. Player Fantasy

Das Ereignis-Feld ist die „Wundertüte" des Boards: Man weiß nie, was passiert, aber es ist immer eine kleine Geschichte — ein Sternschnuppen-Regen, ein Piraten-Überfall, ein Tausch-Basar. Die Ereignisse sollen das Gefühl einer lebendigen, reaktiven Arena erzeugen, in der das Glück umschlägt und niemand sicher führen kann. Spieler in Rücklage erleben Aufhol-Momente („Großzügiger ArenaStar"), Führende erleben das Risiko von Führung („Münz-Coup"). Die Player Fantasy ist die eines Zuschauers und Beteiligten zugleich: Man erlebt eine kurze, kommentierte Szene, die das Kräfteverhältnis verschieben kann.

## 3. Detailed Rules

### 3.1 Anzahl und Position

- Pro Board existieren `N_EREIGNIS ∈ {5, 6}` Ereignis-Felder.
- Referenz-Layout: Indizes 2, 6, 14, 18, 25 (5 Felder).
- Platzierungsregeln: nicht vor Index 2; Abstand entlang des Pfades zueinander ≥ 3 Felder.
- Ereignis-Felder können auf dem Hauptpfad und auf Abzweigungen liegen.

### 3.2 Auslösung

- Ein Ereignis wird beim LANDEN (letztes Feld eines Würfelzugs) ausgelöst — nicht beim Überqueren und nicht bei Effekt-Platzierung (board-architecture.md 3.11).
- Jede Landung auf einem Ereignis-Feld zieht genau ein Ereignis.

### 3.3 Ereignis-Kartei

Die Kartei umfasst aktuell 21 Ereignisse in 4 Gewichtsklassen. Gewichtsklasse, Name, Effekt und Kontext-Bedingung:

**Klein (Gewicht 40) — harmlose, überwiegend positive Effekte:**

| ID | Name | Effekt |
|---|---|---|
| K1 | Sternschnuppen-Regen | Alle Spieler erhalten +3 Münzen. |
| K2 | Glücksmoment | Auslösender Spieler erhält +5 Münzen. |
| K3 | Kleines Geschenk | Spieler auf dem letzten Platz (Rang N) erhält +4 Münzen. |
| K4 | Münzsturm | 10 Münz-Pickups (je 2 Münzen) erscheinen auf 10 zufälligen Feldern (nicht Start) für 1 Runde; Landung sammelt +2; Rundenende entfernt Rest. |
| K5 | Gruß aus der Ferne | Alle Spieler erhalten +2 Münzen. |
| K6 | Schatzkarte | Auslösender Spieler erhält +6 Münzen. |
| K7 | Netter Nieser | Auslösender Spieler +3 Münzen; alle anderen +1 Münze. |
| K8 | Glücksmünzen | Auslösender Spieler erhält +2 Münzen pro Item im Inventar. |

**Mittel (Gewicht 35) — spürbare Umverteilung, Items, Bewegung:**

| ID | Name | Effekt |
|---|---|---|
| M1 | Piraten-Überfall | Ein zufälliger Spieler (ungleich Auslöser) verliert 5 Münzen. |
| M2 | Großzügiger ArenaStar | Spieler auf dem letzten Platz (Rang N) erhält +10 Münzen. |
| M3 | Item-Regen | Alle Spieler erhalten 1 zufälliges Item; bei vollem Inventar (3) geht der Spieler leer aus. |
| M4 | Tausch-Basar | Alle Spieler tauschen paarweise die Board-Position mit ihrem Ranglisten-Nachbarn (Rang 0↔1, 2↔3, …); bei ungerader Spielerzahl bleibt der letzte Rang stehen. |
| M5 | Würfel-Verdoppler | Der nächste Würfelwurf eines beliebigen Spielers zählt doppelt (Schrittweite ×2); stapelt nicht. |
| M6 | Münz-Tausch | Der Führende (Rang 1) gibt 5 Münzen an den Letzten (Rang N); Geber fällt nie unter 0. |
| M7 | Schildkröten-Tempo | Auslösender Spieler bewegt sich 2 Felder rückwärts (nicht unter Feld 0; keine Feld-Effekte am Ziel). |

**Groß (Gewicht 20) — starke, spielentscheidende Effekte:**

| ID | Name | Effekt |
|---|---|---|
| G1 | Stern-Rabatt | `EVENT_MOD = −5` für Sternen-Shops (Preis 15); überschreibt vorhandenen Mod; Reset in Rundenende-Wartung. |
| G2 | Meteorit | 3 zufällige Spieler mit ≥ 1 Item verlieren je 1 zufälliges Item. Kontext-Bedingung: mindestens 3 Spieler mit ≥ 1 Item. |
| G3 | Münz-Coup | Der Führende (Rang 1) verliert 10 Münzen (nie unter 0). |
| G4 | Dieb-Komplott | Auslösender Spieler stiehlt 5 Münzen vom Führenden (Führender nie unter 0). |

**Spielverändernd (Gewicht 5) — verändern das Spielgefüge:**

| ID | Name | Effekt |
|---|---|---|
| S1 | Rückruf | Alle Spieler werden zum Startfeld teleportiert (kein Lap-Bonus, keine Feld-Effekte, Versatz-Schema). |
| S2 | Münz-Karussell | Alle Spieler geben ihre Münzen an den nächsten Spieler in Sitzreihenfolge weiter (Rotation: s → (s+1) mod N). |

Die Kartei ist erweiterbar (Ziel: mindestens 20; aktuell 21). Jede Erweiterung muss einer Gewichtsklasse zugeordnet werden und einen testbaren Effekt besitzen.

### 3.4 Gewichtete Auswahl

1. Kontext-Filter: Alle Ereignisse, deren Kontext-Bedingung (3.5) erfüllt ist, bilden die Auswahlmenge E_elig.
2. Gewichte: `W = {Klein: 40, Mittel: 35, Groß: 20, Spielverändernd: 5}` (Summe 100).
3. Kategorie-Ziehung: Gewichtete Zufallswahl unter den Gewichtsklassen, die mindestens 1 Ereignis in E_elig enthalten. Normierung: `p(Kategorie c) = W_c / Σ W_c'` über alle vertretenen Klassen.
4. Ereignis-Ziehung: Innerhalb der gewählten Klasse gleichverteilt über die enthaltenen Ereignisse.
5. Ausführung: Das Ereignis wird sofort ausgeführt; anschließend Popup (Name, Beschreibung, ArenaStar-Kommentar), das von allen Spielern gesehen wird (Blockierung kurz, Auto-Dismiss nach 2,5 s oder auf Eingabe).

### 3.5 Kontext-Bedingungen (Kontext-Sensitivität)

| Ereignis | Bedingung |
|---|---|
| M1 Piraten-Überfall | `N ≥ 2` (Ziel „ungleich Auslöser" existiert). |
| M4, S2 | `N ≥ 2`. |
| G2 Meteorit | Mindestens 3 Spieler besitzen ≥ 1 Item. |
| G4 Dieb-Komplott | Führender besitzt ≥ 1 Münze. |
| G3 Münz-Coup | Immer gültig (Clamp fängt 0 ab). |
| K3, M2 („Letzter") | Immer gültig (`N ≥ 2` ist durch Spielregel gegeben). |
| K4 Münzsturm | Immer gültig; bei aktivem Münzsturm werden alte Pickups entfernt und 10 neue gesetzt (Refresh, kein Stack). |
| M5 Würfel-Verdoppler | Immer gültig; bei aktivem Verdoppler Refresh auf ×2 (kein Stack auf ×4). |
| Alle übrigen | Immer gültig. |

### 3.6 Rangliste (für „Führender"/„Letzter")

Rangdefinition: primär Sterne absteigend, sekundär Münzen absteigend, tertiär Sitzplatzindex aufsteigend. Rang 1 = Führender, Rang N = Letzter.

### 3.7 Persistente Effekte und Resets

- `EVENT_MOD` (Stern-Rabatt/G1): einzelner Slot, Reset in Rundenende-Wartung.
- Würfel-Verdoppler (M5): persistiert bis zum nächsten Würfelwurf eines beliebigen Spielers (auch über Rundengrenzen); kein automatischer Verfall.
- Münzsturm (K4): Pickups verfallen in der Rundenende-Wartung; aktive Effekte stapeln nicht, sondern refreshen.

### 3.8 Popup-Darstellung

- Anzeige: Event-Name (Titel), Beschreibung (1–2 Sätze), ArenaStar-Kommentar (1 Satz, charakteristisch).
- Das Popup erscheint für alle Spieler gleichzeitig; die Partie pausiert kurz (max. 2,5 s oder Eingabe).
- Der ArenaStar-Kommentar ist pro Ereignis aus einem kleinen Pool von Sätzen gewählt (narrative-arena-star.md, geplant).

### 3.9 Visuelle und auditive Darstellung

- Ereignis-Felder tragen ein neutrales, „geheimnisvolles" Icon (z. B. Pergament/Kristall).
- Ereignisse haben kurze VFX (Sternschnuppen, Blitze, Konfetti), passend zum Effekt.
- Audio-Cue: „Whoosh"/Tusch beim Auslösen (audio-sfx.md, geplant).

## 4. Formulas

Variablendefinitionen:
- `W = {Klein: 40, Mittel: 35, Groß: 20, Spielverändernd: 5}` — Gewichte (Summe 100).
- `E_elig` — kontext-gefilterte Auswahlmenge.
- `C_elig` — Menge der Gewichtsklassen mit mindestens 1 Ereignis in `E_elig`.
- `|E_c|` — Anzahl der Ereignisse der Klasse c in `E_elig`.

Auswahl-Formeln:
- `p(Klasse c) = W_c / Σ_{c' ∈ C_elig} W_{c'}` (normierte Gewichte).
- `p(Ereignis e | Klasse c) = 1 / |E_c|` (gleichverteilt in der Klasse).
- `p(Ereignis e) = p(Klasse(e)) · 1 / |E_{Klasse(e)}|`.

Erwartungswerte:
- Vollständige Kartei (alle Klassen vertreten): p(Klein) = 0,40; p(Mittel) = 0,35; p(Groß) = 0,20; p(Spielverändernd) = 0,05.
- Fehlt z. B. „Spielverändernd" (kein S-Ereignis zulässig), normieren sich die übrigen Gewichte auf `Σ = 95` → p(Klein) = 40/95 ≈ 0,421.
- Beispiel (Referenz, vollständig): p(M5) = 0,35 · (1/7) = 0,05; p(S1) = 0,05 · (1/2) = 0,025.

Weitere Formeln:
- Münz-Clamp für alle negativen Effekte: `coins' = max(0, coins + Δ)`.
- Münzsturm: `N_Pickups = 10`, Wert je Pickup 2, Dauer 1 Runde.
- Würfel-Verdoppler: `Schrittweite' = 2 · Schrittweite` für genau den nächsten Wurf.

## 5. Edge Cases

1. **Ereignis-Klasse ohne zulässige Ereignisse:** Gewicht wird proportional auf die übrigen Klassen umverteilt (Formel 4).
2. **G2 Meteorit nicht zulässig:** Wenn weniger als 3 Spieler Items besitzen, wird G2 ausgeschlossen; die große Klasse zieht dann aus G1/G3/G4.
3. **Münz-Clamp:** Ein Spieler mit 2 Münzen verliert 5 → Endstand 0 (kein negativer Kontostand).
4. **M4 Tausch-Basar bei N = 2:** Rang 0 und 1 tauschen → beide tauschen ihre Position.
5. **M4 bei ungerader Spielerzahl:** Letzter Rang bleibt stehen.
6. **S1 Rückruf, alle bereits auf Feld 0:** No-Op; keine Münzbewegung, kein Lap-Bonus.
7. **M5 Verdoppler und Item-Würfel (Glücks-Würfel):** Der Verdoppler verdoppelt den tatsächlich geworfenen Würfelwert (auch 1–10 des Glücks-Würfels); stapelt nicht.
8. **K4 Münzsturm bei aktivem Münzsturm:** Refresh (alte Pickups entfernen, 10 neue setzen); keine 20 Pickups gleichzeitig.
9. **Ereignis-Ziel „zufälliger Spieler" (M1):** Gleichverteilt über alle Spieler außer dem Auslöser.
10. **Effekt-Platzierung durch Ereignisse (S1, M4, M7):** Löst an den Zielfeldern KEINE Feld-Effekte aus (board-architecture.md 3.11); einzige Ausnahme: MUENZ_BONUS gewährt halben Bonus (field-coin-bonus.md).
11. **Mehrere Ereignis-Feld-Landungen in einer Runde:** Jede Landung zieht unabhängig; persistente Effekte refreshen statt zu stapeln.
12. **AI-Spieler:** Dieselben Regeln; keine Sonderbehandlung bei Ereignissen.

## 6. Dependencies

### 6.1 Benötigt von `field-event.md`

| Kapitel/System | Art | Verwendung |
|---|---|---|
| `board-architecture.md` | Voraussetzung | EREIGNIS-Typ, Lande-Regel, Rundenende-Wartung (Resets, Pickup-Entfernung). |
| `field-star-shop.md` | Abhängig | G1 setzt `EVENT_MOD` (muss die Preis-Formel kennen). |
| `item-system.md` (geplant) | Quelle | M3/M2G2-Item-Vergabe und Item-Verlust. |
| `coin-economy.md` (geplant) | Quelle | Münz-Clamp, Umverteilungs-Bilanz (Catch-Up). |
| `catch-up.md` (geplant) | Quelle | Zielsetzung der Aufhol-Effekte (K3, M2, M6). |
| `narrative-arena-star.md` (geplant) | Quelle | Kommentar-Pools je Ereignis. |
| `dice-movement.md` (geplant) | Quelle | M5-Verdoppler, M7-Rückwärtsbewegung. |

### 6.2 Systeme, die von diesem Dokument abhängen

| Kapitel/System | Art der Abhängigkeit |
|---|---|
| `field-start.md` | Ereignis „Rückruf" (S1) zielt auf das Startfeld und muss die Bonus-Ausnahme beachten. |
| `field-coin-bonus.md` | Effekt-Platzierungen (M4, S1) können Spieler auf MUENZ_BONUS-Felder setzen (halber Bonus). |
| `catch-up.md` (geplant) | Nutzt die Kartei als Catch-Up-Instrument. |
| `ui-hud.md` (geplant) | Zeigt Ereignis-Popups und ArenaStar-Kommentare. |
| `coin-economy.md` (geplant) | Bilanziert die Umverteilungs-Ereignisse. |

### 6.3 Bidirektionalität

`board-architecture.md`, `field-star-shop.md`, `field-start.md` und `field-coin-bonus.md` verweisen auf dieses Kapitel; dieses Kapitel verweist zurück. Wechselseitigkeit ist damit hergestellt.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|---|---|---|---|---|
| Gewichte `W` | Kurve | Summe 100; je Klasse 0–60 | 40/35/20/5 | Chaos-Level und Spielveränderungs-Häufigkeit. |
| Münzbeträge der Ereignisse | Kurve | 1–15 | siehe Kartei | Stärke der Umverteilung. |
| `N_EREIGNIS` | Kurve | 5–6 | 5 | Ereignis-Dichte pro Runde. |
| Münzsturm-Pickups | Kurve | 5–15 | 10 | Umfang des Münzsturms. |
| Pickup-Wert | Kurve | 1–3 | 2 | Wert je Pickup. |
| Verdoppler-Faktor | Kurve | 2–3 | 2 | Stärke des Würfel-Verdopplers. |
| Popup-Dauer | Feel | 1–5 s | 2,5 s | Spieltempo. |
| Ereignis bei Überquerung | Gate | an/aus | aus | aus = nur Landungen lösen Ereignisse aus. |

## 8. Acceptance Criteria

Ein QA-Tester kann die folgenden Prüfungen ausführen:

1. **Kartei-Umfang:** Die Kartei enthält mindestens 20 Ereignisse (aktuell 21), jede Gewichtsklasse mindestens 1 Ereignis. PASS/FAIL.
2. **Gewichtung (statistisch):** Über 1000 Ziehungen mit vollständiger Kartei liegen die Klassenanteile innerhalb ±3 %-Punkten von 40/35/20/5. PASS/FAIL.
3. **Kontext-Filter:** G2 „Meteorit" erscheint nie, wenn weniger als 3 Spieler Items besitzen. PASS/FAIL.
4. **Münz-Clamp:** Kein Ereignis führt zu einem negativen Münzstand. PASS/FAIL.
5. **Tausch-Basar (N=4):** Nach M4 haben Rang 0↔1 und 2↔3 die Positionen getauscht; Münzen/Sterne bleiben bei den Spielern. PASS/FAIL.
6. **Rückruf:** Alle Spieler stehen nach S1 auf Feld 0; keine Münzbewegung; kein Lap-Bonus. PASS/FAIL.
7. **Verdoppler:** Nach M5 zählt der nächste Würfelwurf doppelt (z. B. Wurf 3 → 6 Schritte); der übernächste Wurf zählt wieder einfach. PASS/FAIL.
8. **Münzsturm:** 10 Pickups (je 2) erscheinen; Landung sammelt +2; nach der Rundenende-Wartung sind alle Pickups entfernt. PASS/FAIL.
9. **Popups:** Jedes ausgelöste Ereignis zeigt Name, Beschreibung und ArenaStar-Kommentar. PASS/FAIL.
10. **Keine Feld-Effekte bei Platzierung:** Spieler, die durch S1/M4/M7 auf ein Feld gesetzt werden, lösen dort keine Feld-Effekte aus (Ausnahme Münz-Bonus halb). PASS/FAIL.
