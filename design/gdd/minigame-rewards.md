# Minispiel-Belohnungen — Party Arena Game Bible

> **Teil:** IV — Minigames
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md (Abschnitt "Minispiele"), design/gdd/minigame-architecture.md (Abschnitt 3.9), STP-Auszahlungslogik (`server/lobby.gd` `_goto_board`)

---

## 1. Overview

Dieses Kapitel definiert, wie Minispiele Münzen auszahlen: die Platzierungs-Belohnung für 1.–8. Platz, die Skalierung für 2–8 Spieler, den Verlierer-Bonus für Teilnahme, die Gleichstands-Mittelung, die Koop-Auszahlung, die Interaktion mit dem Item Münz-Magnet, die Minispiel-Statistik für den Bonus-Stern "Schnellster" und den Belohnungs-Screen. Grundprinzip: **Jedes Minispiel zahlt an jeden teilnehmenden Spieler Münzen aus; niemand geht leer aus.** Die Belohnung ist der primäre Münz-Faucet der Minispiel-Phase und wird gegen die Stern-Kosten (20 Münzen) und die Item-Preise bilanziert. Das System ersetzt die STP-Auszahlungslogik (`get_ffa_reward`, Duel-Transfer, 1v3-Fixbeträge) durch ein einheitliches, platzierungsbasiertes Modell für alle 2–8 Spieler.

## 2. Player Fantasy

Der Belohnungs-Screen ist der emotionale Höhepunkt nach jedem Minispiel — der Moment, in dem sich Anstrengung in sichtbarem Fortschritt niederschlägt. Die Fantasie lautet: **"Egal wie ich abgeschnitten habe — ich habe etwas bekommen, und mein Konto ist gewachsen."** Für die Siegerin oder den Sieger ist es ein Triumph (10 Münzen + ArenaStar-Lob); für die Letztplatzierten ein Trost, der die Niederlage abfedert (Teilnahme-Bonus, freundliche Kommentare, überzeichnete Trotz-Animation). Die Staffelung 10/7/5/3/2/2/2/2 belohnt Spitzenleistung deutlich, bestraft aber nicht: Der Abstand zwischen Platz 1 und den hinteren Plätzen ist spürbar, aber nicht demütigend — das hält die Partie für Gelegenheitsspieler und Kinder offen (Flow und Fairness). Gleichstände werden großzügig gemittelt ("beide bekommen den Durchschnitt"), was Konflikte am Tisch verhindert: Es gibt keine "fast gewonnen"-Enttäuschung, sondern geteilte Freude. Der animierte Belohnungs-Screen (Münzen fliegen zum Konto, Charaktere hüpfen) macht den Moment physisch fühlbar (Pfeiler 3, Interaktiv wirkend), und ArenaStar kommentiert die Top 3 persönlich (Relatedness). Für den Gesamtspielverlauf erzeugt die regelmäßige Auszahlung ein verlässliches **Fortschritts-Gefühl**: Nach jedem Minispiel nähert man sich dem nächsten Stern, und der Bonus-Stern "Schnellster" gibt den Minispiel-Helden am Spielende eine zusätzliche Chance auf die Siegerehrung.

## 3. Detailed Rules

### 3.1 Grundprinzip

1. Jedes Minispiel zahlt Münzen an **alle** teilnehmenden Spieler (2–8).
2. Die Auszahlung basiert auf der **Platzierung** (1.–n.), die das Framework nach `minigame-architecture.md` Abschnitt 3.9 berechnet (tie-gruppiertes Array).
3. Es gibt **keine Münz-Abzüge** in Minispielen: Niemand verliert Münzen an ein Minispiel. Dies ist eine bewusste Design-Entscheidung gegenüber STP (dort: Duel überträgt Münzen, 1v3/Coop-Abzüge). Begründung: familienfreundlich, kein "Bestrafungs-Moment", konsistent mit dem Anti-Pfeiler "kein Skill-basiertes Wettkampf-Spiel" aus `vision-pillars.md`.
4. Die Auszahlung erfolgt einmalig pro Minispiel und wird sofort dem Münz-Kontostand gutgeschrieben (spätestens beim Belohnungs-Screen).
5. Der Versuchs-Modus (Try) zahlt **keine** Münzen und zählt **nicht** in die Statistik (Architektur Abschnitt 3.12).

### 3.2 Platzierungs-Belohnung (8 Spieler)

Die Basis-Belohnung `B` für 8 Spieler (ohne Verlierer-Bonus, ohne Magnet):

| Platz | Basis `B` |
|-------|-----------|
| 1 | 10 |
| 2 | 7 |
| 3 | 5 |
| 4 | 3 |
| 5 | 2 |
| 6 | 2 |
| 7 | 2 |
| 8 | 2 |

Eigenschaften: monoton fallend, großzügiger Boden von 2 Münzen für alle hinteren Plätze, klare Sprünge an der Spitze (10→7→5→3).

### 3.3 Skalierung für 2–8 Spieler

Die Belohnung für Platz `p` bei `n` Spielern ergibt sich aus der 8-Spieler-Basistabelle:

- **n ≥ 3:** `R(p, n) = B[p]` für p = 1…n — es werden die ersten n Einträge der 8er-Tabelle verwendet.
- **n = 2 (Sonderfall):** `R(1, 2) = 10`, `R(2, 2) = 5`. Begründung (Design-Entscheidung): Bei einem 1-gegen-1 wäre die Übernahme von `B[2] = 7` zu flach — der Abstand 10:7 lässt die Niederlage vernachlässigbar wirken und nimmt dem Duell die Spannung. Der Wert 5 erzeugt ein klares, aber nicht demütigendes Gefälle.

| n | Basis-Belohnungen (ohne Bonus) |
|---|--------------------------------|
| 2 | 10, 5 |
| 3 | 10, 7, 5 |
| 4 | 10, 7, 5, 3 |
| 5 | 10, 7, 5, 3, 2 |
| 6 | 10, 7, 5, 3, 2, 2 |
| 7 | 10, 7, 5, 3, 2, 2, 2 |
| 8 | 10, 7, 5, 3, 2, 2, 2, 2 |

### 3.4 Verlierer-Bonus

- Jeder Spieler auf **Platz 5–8** (absolute Platzierung, unabhängig von n) erhält einen zusätzlichen Teilnahme-Bonus von **+1 Münze**.
- Konsequenz: Bei n ≤ 4 erhält **niemand** den Verlierer-Bonus, weil die Plätze 5–8 nicht existieren. Begründung: In kleinen Spielen sind auch die hinteren Plätze bereits relativ großzügig bedacht (3 bzw. 5 Münzen); der Bonus zielt auf die Frustrations-Dämpfung in großen Runden, wo der letzte Platz sonst besonders hart wirkt.
- Der Bonus wird **nach** der Gleichstands-Mittelung und **vor** dem Magnet-Multiplikator behandelt (siehe 3.5, 3.7): Der Magnet verdoppelt den Basisbetrag, **nicht** den Verlierer-Bonus.

Effektive Auszahlung (8 Spieler, ohne Magnet):

| Platz | Basis | Verlierer-Bonus | Effektiv |
|-------|-------|-----------------|----------|
| 1 | 10 | — | 10 |
| 2 | 7 | — | 7 |
| 3 | 5 | — | 5 |
| 4 | 3 | — | 3 |
| 5 | 2 | +1 | 3 |
| 6 | 2 | +1 | 3 |
| 7 | 2 | +1 | 3 |
| 8 | 2 | +1 | 3 |

### 3.5 Gleichstand (Ties)

- Gleichständige Spieler bilden eine Gruppe (Architektur Abschnitt 3.9). Die Gruppe belegt die Plätze `p … p+k−1` gemeinsam (k = Gruppengröße).
- Jedes Mitglied erhält den **arithmetischen Mittelwert** der Basis-Belohnungen der belegten Plätze, kaufmännisch gerundet (halbe Werte werden aufgerundet).
- Es gibt **keinen** "nächsten Platz" unterhalb der Gruppe: Die Gruppe verbraucht alle belegten Plätze.
- Verlierer-Bonus: Eine Gruppe erhält den Bonus, wenn ihr **Startplatz p ≥ 5** ist.
- Formel in Abschnitt 4.2.

Beispiel (aus der Aufgabenstellung): Zwei Spieler teilen sich Platz 2 (in einem Spiel mit n ≥ 3). Belegt werden Plätze 2 und 3 → Basis-Mittelwert `(7 + 5)/2 = 6`. Beide erhalten 6 Münzen; es gibt keinen 3. Platz.

### 3.6 Koop-Minispiele

Für Minispiele mit `team_mode = "coop_all"` (Sternen-Brücke) und `team_mode = "coop_teams"` (Schatz-Trage):

- **Basis für alle Spieler: 5 Münzen**, unabhängig vom Team-Erfolg. Diese Basis ersetzt den Verlierer-Bonus (Teilnahme ist in Koop die Norm, keine Bestrafung).
- **Leistungs-Bonus:**
  - `coop_all` (Sternen-Brücke): `Bonus = floor(3 × Fortschritt / 100)`, wobei `Fortschritt` der Brücken-Anteil in Prozent ist (Kategorien Abschnitt 3.6.2). Bei 100 % → 3 Münzen, 67 % → 2, 33 % → 1, 0 % → 0.
  - `coop_teams` (Schatz-Trage): Siegerteam-Mitglieder erhalten **+3**, Verliererteam-Mitglieder **+1**.
- Der Verlierer-Bonus (3.4) gilt in Koop **nicht** (durch die 5-Münzen-Basis abgedeckt).
- Die Auszahlung an Einzelspieler ist bei `coop_all` für alle identisch; bei `coop_teams` unterscheidet sie sich nur zwischen den Teams, nicht innerhalb eines Teams.

### 3.7 Münz-Magnet

- Das Item Münz-Magnet (`item-coinmagnet.md`) verdoppelt die **Basis-Belohnung** eines Minispiels. Konkret:
  - Wettbewerbs-Minispiele: `Auszahlung = 2 × Basis` (nach Gleichstands-Mittelung) `+ Verlierer-Bonus`.
  - Koop-Minispiele: `Auszahlung = 2 × 5 = 10` plus unveränderter Leistungs-Bonus.
- Der Verlierer-Bonus wird **nicht** verdoppelt. Der Koop-Leistungs-Bonus wird **nicht** verdoppelt.
- **Kein Stacking:** Mehrfach aktive Magnet-Quellen (falls das Item-System mehrere gleichzeitig erlaubt) bleiben bei Faktor 2; der Multiplikator ist binär (1 oder 2).
- Bezug zum Item: `item-coinmagnet.md` definiert, für wie viele Erträge bzw. Runden der Magnet aktiv ist; dieses Kapitel definiert nur die Anwendung auf Minispiel-Belohnungen. Ist der Magnet zum Zeitpunkt der Auszahlung aktiv (Spielerzustand `magnet_active = true`), greift der Faktor 2.
- Beispiel: Spieler auf Platz 3 (Basis 5) mit aktivem Magnet → 2 × 5 = 10. Spieler auf Platz 7 (Basis 2 + Bonus 1) mit aktivem Magnet → 2 × 2 + 1 = 5.

### 3.8 Minispiel-Statistik und Bonus-Stern "Schnellster"

- Das Framework zählt pro Spieler die **Minispiel-Siege**:
  - Wettbewerbs-Minispiele (`by_points`/`by_position`, `team_mode = "ffa"`): ein Sieg = Platz 1 (einschließlich geteilter Platz 1 bei Gleichstand).
  - Koop-Minispiele: `coop_teams` → ein Sieg für jedes Mitglied des Siegerteams; `coop_all` → ein Sieg für alle, wenn der Fortschritt 100 % erreicht wurde.
- Die Zählung läuft über die gesamte Partie (alle Runden, nie zurückgesetzt) und wird in der Spieler-Statistik geführt.
- Am Spielende vergibt `victory-conditions.md` den Bonus-Stern **"Schnellster"** an den Spieler mit den meisten Minispiel-Siegen. Gleichstand bei der Sieg-Zahl wird dort über den dort definierten Tiebreaker aufgelöst; dieses Kapitel liefert nur die Statistik.
- Der Versuchs-Modus zählt nicht (3.1).

### 3.9 Belohnungs-Screen

- Nach der RESULTS-Phase (Architektur Abschnitt 3.3) zeigt das Framework den Belohnungs-Screen (Weiterentwicklung der STP-Rewardscreens `client/rewardscreens/*`):
  - **Alle n Platzierungen** werden als Spalten/Reihen animiert eingeblendet, Platz 1 zuerst und hervorgehoben (größer, goldener Rahmen).
  - Jede Platzierung zeigt den Charakter mit Emotion: Top 3 "happy", Rest "sad/trotzig" (überzeichnet, Pfeiler 2).
  - Die Münz-Belohnung wird als Zahl mit Münz-Icon angezeigt und **zum Kontostand animiert** (Münzen fliegen zum Porträt; Zähler dreht hoch). Bei aktivem Magnet wird der verdoppelte Betrag mit einem Magneten-Symbol markiert.
  - Der neue Kontostand wird nach der Animation angezeigt.
- **ArenaStar-Kommentare:** ArenaStar kommentiert die Top 3 (kurze, personalisierte Sprüche, ≤ 3 s, überspringbar — siehe `narrative-arena-star.md`). Sie blockiert die Eingabe nie länger als 3 s (Pfeiler 3, Tuning-Knob in `vision-pillars.md`).
- Fortsetzen: Jeder Spieler bestätigt mit `action1` (STP-ContinueCheck-Mechanik); wenn alle bestätigt haben (oder ein Timer abläuft), kehrt das Spiel zum Board zurück.
- Bei Koop-Minispielen zeigt der Screen das Team-Ergebnis (Team-Grenze) statt der Einzelplatzierung; der Leistungs-Bonus wird separat ausgewiesen (Basis + Bonus).

### 3.10 Ökonomischer Kontext

- **Faucet-Größe:** Ein 8-Spieler-Minispiel pumpt `10+7+5+3+2+2+2+2 = 33` Münzen (Basis) plus bis zu 4 Münzen Verlierer-Bonus (4 Spieler auf 5.–8.) = **maximal 37 Münzen** in die Ökonomie. Bei n = 4: `25` Münzen; bei n = 2: `15` Münzen.
- **Pro-Spieler-Schnitt:** Bei 8 Spielern ~4,6 Münzen pro Minispiel (37/8). Über eine Partie mit ~9 Minispielen (8–10 Runden) ≈ **41 Münzen aus Minispielen pro Spieler** — genug für ca. 2 Sterne (à 20), ergänzt durch Board-Münzen (Felder, Ereignisse, Bonus-Felder). Details und Bilanz in `coin-economy.md`.
- **Gini-/Spreizungs-Hinweis:** Der Faktor zwischen Platz 1 (10) und letztem Platz (3 effektiv) beträgt ~3,3. Das ist bewusst moderat: Minispiel-Skill soll die Partie beeinflussen, aber nicht determinieren (Anti-Pfeiler 1). Die Belohnung wirkt als leichter Catch-up (die hinteren Spieler holen relativ auf), nicht als Schneeball.
- **Interaktion mit Stern-Kauf:** Da die Stern-Statue wandert und jeder Spieler Münzen ansammelt, hält die Minispiel-Auszahlung alle Spieler in Reichweite des Stern-Preises (20). Ein Spieler, der bei Board-Münzen Pech hat, kann über Minispiele konkurrenzfähig bleiben.

## 4. Formulas

### 4.1 Platzierungs-Belohnung `R(p, n)`

Basistabelle `B = [10, 7, 5, 3, 2, 2, 2, 2]` (Index 0 = Platz 1).

`R(p, n) =` 
- für `n ≥ 3`: `B[p−1]`, für `p = 1…n`
- für `n = 2`: `10` falls `p = 1`, sonst `5`

Gültigkeitsbereich: `n ∈ [2,8]`, `p ∈ [1,n]`. Ausgabe: ganze Münzen.

### 4.2 Gleichstands-Mittelung

Gegeben eine Gleichstands-Gruppe der Größe `k` mit Startplatz `p`:

`Basis_gruppe = round( (1/k) · Σ_{i=p}^{p+k−1} B[i−1] )`

mit **kaufmännischem Runden** (halbe Werte aufgerundet: 8,5 → 9; 2,5 → 3).

`Auszahlung_Mitglied = Basis_gruppe + (1 falls p ≥ 5 sonst 0)`

Beispiele:
- Zwei Spieler teilen Platz 2: `(7+5)/2 = 6` → je 6, kein Bonus (p=2).
- Zwei Spieler teilen Platz 4/5 (k=2, p=4): `(3+2)/2 = 2,5` → 3, kein Bonus (p=4 < 5) → je 3.
- Zwei Spieler teilen Platz 5/6 (k=2, p=5): `(2+2)/2 = 2`, Bonus (p=5 ≥ 5) → je 3.
- Alle 8 gleichauf (k=8, p=1): `(10+7+5+3+2+2+2+2)/8 = 33/8 = 4,125` → je 4, kein Bonus.

### 4.3 Münz-Magnet

`Auszahlung = M · Basis + Bonus`

| Variable | Definition | Wert |
|----------|-----------|------|
| `M` | Magnet-Multiplikator | 1 (inaktiv) oder 2 (aktiv) |
| `Basis` | `Basis_gruppe` (4.2) bzw. Koop-Basis 5 | ganzzahlig |
| `Bonus` | Verlierer-Bonus (0 oder 1) bzw. Koop-Leistungs-Bonus | ganzzahlig |

Beispiele:
- Platz 3, kein Magnet: `1·5 + 0 = 5`.
- Platz 3, Magnet: `2·5 + 0 = 10`.
- Platz 7, Magnet: `2·2 + 1 = 5`.
- Koop (Sternen-Brücke, 100 %, Magnet): `2·5 + 3 = 13`.

### 4.4 Koop-Bonus

- `coop_all`: `Bonus = floor(3 · Fortschritt / 100)`, `Fortschritt ∈ [0,100]` %.
  - Beispiel: 67 % → `floor(201/100) = 2`.
- `coop_teams`: `Bonus = 3` (Siegerteam) bzw. `1` (Verliererteam).
- Gesamt Koop: `Auszahlung = M · 5 + Bonus`.

### 4.5 Gesamtauszahlung einer Runde

`S(n) = Σ_{p=1}^{n} R(p, n) + (Anzahl der Plätze ≥ 5 bei Einzelplatzierung) · 1`

- n=8: `33 + 4 = 37` (wenn 4 Spieler die Plätze 5–8 belegen; bei Gleichständen kann die Bonus-Zahl abweichen).
- n=4: `25 + 0 = 25`.
- n=2: `15 + 0 = 15`.

### 4.6 Ökonomie-Projektion

`E(s) = S(n) · s`, wobei `s` die Anzahl der Minispiele pro Partie ist (≈ Runden − 1; 8–10 Runden → 7–9 Minispiele, da die letzte Runde in die Siegerehrung mündet).

- n=8, s=9: `37 · 9 = 333` Münzen Gesamt-Faucet aus Minispielen pro Partie.
- Pro Spieler: `333/8 ≈ 41,6` Münzen. (Referenz für `coin-economy.md`.)

## 5. Edge Cases

1. **Alle 8 Spieler gleichauf:** Alle erhalten die Mittelung (4.2) = 4 Münzen; kein Verlierer-Bonus (p=1). Das ist ein seltener, aber gültiger Fall.
2. **Gleichstand mit Magnet:** Die Mittelung (4.2) wird zuerst berechnet, dann verdoppelt (4.3). Beispiel: zwei Spieler teilen Platz 2 (Basis 6), beide mit Magnet → je 12.
3. **Gleichstand in Koop:** `coop_all` hat keine Einzelplatzierung; die Mittelung ist nicht anwendbar. `coop_teams`: Der Team-Erfolg bestimmt die Auszahlung; innerhalb eines Teams ist sie identisch (kein Tie-Fall).
4. **Disconnect eines Spielers:** Der Spieler belegt den letzten Platz (Architektur 3.12) und erhält dessen Auszahlung (bei 8 Spielern: Basis 2 + Bonus 1 = 3; mit aktivem Magnet: 5). Sein Spielerzustand wird, falls vorhanden, dennoch ausbezahlt, damit das Board-Spiel konsistent bleibt.
5. **n=2, Verlierer-Bonus:** Platz 2 liegt nicht in 5–8; daher **kein** Bonus. Zweiter erhält 5 (bzw. 10 mit Magnet). Dies ist die bewusste Konsequenz aus 3.4.
6. **Ungerade n (3, 5, 7):** Es gibt die Plätze 5–7; der Verlierer-Bonus greift nur für Plätze ≥ 5 (bei n=3: niemand; bei n=5: Platz 5; bei n=7: Plätze 5–7). Beispiele: n=5, Platz 5 → Basis 2 + 1 = 3.
7. **Rundungsabweichung:** Durch die Mittelung kann die tatsächliche Gesamtauszahlung von `S(n)` um ±1 Münze je Gleichstands-Gruppe abweichen. Das ist akzeptiert und dokumentiert; es gibt keinen Rettungs-Mechanismus, weil die Abweichung klein und die Fairness höher gewichtet ist.
8. **Magnet-Aktivierung während des Minispiels:** Maßgeblich ist der Spielerzustand **zum Zeitpunkt der Auszahlung** (Beginn des Belohnungs-Screens). Erwirbt ein Spieler den Magnet erst auf dem Board nach dem Minispiel, gilt er für das nächste Minispiel, nicht für das gerade beendete.
9. **Try-Modus:** Keine Auszahlung, keine Statistik (3.1).
10. **Minispiel-Abbruch durch Framework-Fehler:** Alle nicht platzierten Spieler erhalten den letzten Platz (Architektur 3.12). Bei 8 Spielern: alle Platz 8 → Mittelung nicht nötig, jeder erhält Basis 2 + Bonus 1 = 3 (bzw. 5 mit Magnet).
11. **Minispiel-Sieg bei geteiltem Platz 1:** Beide Mitglieder einer geteilten Spitze erhalten einen Minispiel-Sieg für die Statistik (3.8). Es gibt keinen "halben" Sieg.
12. **Bonus-Stern-Gleichstand:** Die Statistik liefert die Sieg-Zahl; die Auflösung des Gleichstands liegt bei `victory-conditions.md` (Tiebreaker). Dieses Kapitel verdoppelt keine Sterne und vergibt nichts zusätzlich.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `minigame-rewards.md` | Art | Verwendung |
|--------------------------------------|-----|------------|
| `design/gdd/minigame-architecture.md` | Peer | Liefert die Platzierungs-Struktur (tie-gruppiert) und den Lebenszyklus (RESULTS → REWARDS). |
| `design/gdd/minigame-categories.md` | Peer | Liefert die Koop-Modi und Fortschritts-/Team-Definitionen (Sternen-Brücke, Schatz-Trage). |
| `design/gdd/coin-economy.md` | Peer | Die Münz-Ökonomie bilanziert diesen Faucet gegen Senken (Stern 20, Items). |
| `design/gdd/item-coinmagnet.md` | Peer | Definiert Aktivierung/Nutzen des Magneten; dieses Kapitel die Anwendung auf Minispiele. |
| `design/gdd/victory-conditions.md` | Nachgeordnet | Vergibt den Bonus-Stern "Schnellster" aus der Statistik (3.8). |
| `design/gdd/catch-up.md` | Peer | Der Verlierer-Bonus ist ein Mini-Catch-up; die Catch-up-Strategie muss ihn einordnen. |
| `design/gdd/narrative-arena-star.md` | Nachgeordnet | Kommentare im Belohnungs-Screen (3.9). |
| `design/gdd/ui-hud.md` | Nachgeordnet | Kontostand-Animation und Münz-Flug im Belohnungs-Screen. |
| `.claude/rules/design-docs.md` | Regelwerk | 8-Sektionen-Standard. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `minigame-architecture.md` | Muss die Auszahlung am Ende der REWARDS-Phase an den Spielerzustand übergeben (Framework-Aufruf). |
| `coin-economy.md` | Muss den Minispiel-Faucet (4.6) als Quelle führen. |
| `item-coinmagnet.md` | Muss den Magnet-Faktor 2 für Minispiel-Belohnungen referenzieren. |
| `ui-hud.md`, `ui-accessibility.md` | Muss die Bonus- und Magnet-Kennzeichnung im Belohnungs-Screen anzeigen. |
| `technical-architecture.md` | Muss die Auszahlungs-Berechnung im Server (autoritär) verorten (vgl. `server/lobby.gd`). |
| `systems-index.md` | Führt das Belohnungssystem als eigenes System. |

### 6.3 Bidirektionalität

Die Auszahlung ist der Übergabepunkt zwischen Minispiel-Framework und Ökonomie: Das Framework liefert die Platzierung, dieses Kapitel die Münzen, die Ökonomie die Bilanz. Die Abhängigkeit zu `item-coinmagnet.md` ist wechselseitig — der Magnet verdoppelt hier, und das Item-Kapitel muss diese Anwendung explizit aufführen. Die Abhängigkeit zu `victory-conditions.md` ist einseitig gerichtet (dieses Kapitel liefert die Statistik, die Siegbedingungen verbrauchen sie) und wird dort als Quelle referenziert.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Basistabelle `B` | Kurve | Einträge ganzzahlig ≥ 1, monoton fallend | `[10, 7, 5, 3, 2, 2, 2, 2]` | Bestimmt Spreizung und Gesamt-Faucet der Minispiel-Phase. |
| 2-Spieler-Wert Platz 2 | Kurve | 3–9 | 5 | Gefälle im Duell; zu niedrig = frustrierend, zu hoch = wirkungslos. |
| Verlierer-Bonus-Betrag | Kurve | 0–3 | 1 | Trost-Stärke für die hinteren Plätze. |
| Verlierer-Bonus-Schwelle | Gate | 4–7 | 5 | Ab welchem Platz der Bonus greift (bei n ≤ Schwelle zahlt niemand). |
| Koop-Basis | Kurve | 3–8 | 5 | Grundsicherung in Koop-Minispielen. |
| Koop-Bonus-Deckel (`coop_all`) | Kurve | 1–5 | 3 | Maximaler Fortschritts-Bonus. |
| Koop-Team-Boni | Kurve | Sieg 1–5, Niederlage 0–3 | 3 / 1 | Belohnungs-Gefälle zwischen den Teams. |
| Magnet-Multiplikator | Kurve | 1–3 | 2 | Stärke des Münz-Magneten in Minispielen. |
| Rundungsmodus | Kurve | kaufmännisch / abrunden | kaufmännisch | Rundung bei Gleichstands-Mittelung (aufrunden = spielerfreundlich, abrunden = inflationsärmer). |
| Sieg-Definition (geteilter Platz 1) | Gate | zählt / zählt nicht | zählt | Ob geteilte Siege in die "Schnellster"-Statistik eingehen. |

Änderungen an der Basistabelle verschieben den Gesamt-Faucet (4.5) und müssen in `coin-economy.md` gespiegelt werden.

## 8. Acceptance Criteria

Ein QA-Tester kann folgende Prüfungen ausführen:

1. **Auszahlungs-Matrix:** Für n = 2, 4, 6, 8 wird je ein Minispiel mit eindeutiger Platzierung gespielt; die Auszahlungen entsprechen exakt den Tabellen in 3.2/3.3 (2: 10/5; 4: 10/7/5/3; 6: 10/7/5/3/2/2; 8: 10/7/5/3/2/2/2/2). PASS/FAIL.
2. **Verlierer-Bonus:** Bei n = 8 erhalten die Plätze 5–8 jeweils +1 (effektiv 3); bei n = 4 erhält niemand einen Bonus. PASS/FAIL.
3. **Gleichstands-Mittelung:** Ein konstruiertes Gleichstands-Szenario (zwei Spieler teilen Platz 2) zahlt beiden 6 aus und erzeugt keinen 3. Platz. Weitere Fälle aus 4.2 (Platz 4/5 → 3; Platz 5/6 → 3; alle gleich → 4). PASS/FAIL.
4. **Magnet:** Mit aktivem Magnet erhält Platz 3 genau 10; Platz 7 genau 5 (2×2+1); ohne Magnet 5 bzw. 3. Kein Stacking bei mehrfach aktivem Magnet. PASS/FAIL.
5. **Koop-Auszahlung:** Sternen-Brücke bei 100 % zahlt jedem 5+3=8 (ohne Magnet); bei 0 % 5. Schatz-Trage zahlt Siegerteam 5+3=8, Verliererteam 5+1=6. PASS/FAIL.
6. **Statistik "Schnellster":** Nach einer konstruierten Partie mit bekannten Siegen entspricht die Sieg-Zählung (3.8) den erwarteten Werten inklusive geteilter Platz-1-Siege und Koop-Siege. PASS/FAIL.
7. **Belohnungs-Screen:** Der Screen zeigt alle n Platzierungen animiert, Top 3 mit happy-Animation, die Münz-Belohnung fliegt zum Konto, der neue Kontostand stimmt mit dem Vorher-Wert + Auszahlung überein. PASS/FAIL.
8. **ArenaStar-Kommentare:** ArenaStar kommentiert genau die Top 3; kein Kommentar blockiert die Eingabe länger als 3 s. PASS/FAIL.
9. **Disconnect-Auszahlung:** Ein während des Minispiels disconnected Spieler erhält die letzte-Platz-Auszahlung; die übrigen Auszahlungen sind unverändert. PASS/FAIL.
10. **Ökonomie-Bilanz:** Die Summe der Auszahlungen einer 8-Spieler-Runde (37) stimmt mit der Projektion in 4.5 überein; die Gesamtbilanz über eine Testpartie liegt innerhalb ±5 % der Projektion in 4.6. PASS/FAIL.
11. **Erlebbar (Experiential):** In einem Playtest mit 8 Spielern (gemischt, ab 6 Jahren) gibt kein Teilnehmer an, sich nach einem Minispiel "bestraft" gefühlt zu haben (Ja/Nein-Abfrage); ≥ 80 % geben an, die Belohnung sei "fair" gewesen (1–5-Skala, Ziel ≥ 4). PASS/FAIL.
