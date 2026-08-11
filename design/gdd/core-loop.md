# Kern-Loop — Party Arena Game Bible

> **Teil:** I — Core Game
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/bible-index.md

---

## 1. Overview

Der Kern-Loop von Party Arena ist der verschachtelte Ablauf, der das gesamte Spiel antreibt. Er besteht aus drei Ebenen: dem **Mikro-Loop** (Würfeln → Ziehen → Feld-Effekt innerhalb eines einzelnen Spielerzugs), dem **Meso-Loop** (eine Spielrunde: alle Spieler ziehen nacheinander → Minispiel → Stern-Phase) und dem **Makro-Loop** (die Partie: 8–10 Runden, gefolgt von Bonus-Sternen, Endabrechnung, Siegerehrung und Statistik-Bildschirm). Eine Partie dauert 20–30 Minuten und wird von 2–8 Spielern bestritten, die als Arenians über ein 40-Felder-Brett (eine Insel von Aethonia) ziehen. Das Maskottchen ArenaStar moderiert jede Phase: Er wirft den Würfel, kündigt das Minispiel an, verteilt Münzen und krönt am Ende den Sieger. Dieses Kapitel definiert die verbindliche Phasen-Struktur einer Runde, die Zug-Reihenfolge, die Runden-Grenzen, die Bestimmung der Rundenanzahl und die Zeitbudgets aller Phasen. Alle anderen Core-Game-Kapitel ([dice-movement](dice-movement.md), [coin-economy](coin-economy.md), [star-economy](star-economy.md), [victory-conditions](victory-conditions.md), [catch-up](catch-up.md)) setzen auf dieser Struktur auf.

## 2. Player Fantasy

Die Spieler sollen sich wie Teilnehmer einer großen, übertriebenen Arena-Show fühlen — moderiert von einem charismatischen Stern. Der Mikro-Loop erzeugt das **Kribbeln des Würfels** (Sensation): Jeder Wurf ist ein kleines Glücksspiel mit hör- und sichtbarer Spannung. Die Bewegung übersetzt das Ergebnis in sichtbaren Fortschritt auf dem Brett und gibt an Abzweigungen ein Gefühl von **Kontrolle** (Autonomie: "Ich entscheide, welchen Weg ich nehme"). Der Feld-Effekt ist die **Überraschung** (Discovery): Mal gibt es Münzen, mal ein Ereignis, mal Glück oder Pech. Der Meso-Loop bündelt diese Einzelerfahrungen zu einem **Wettbewerbs-Höhepunkt**: Das Minispiel ist der Moment, in dem reine Geschicklichkeit zählt und die Gruppe gemeinsam lacht oder jubelt (Fellowship). Die Stern-Phase erzeugt die **Begehrlichkeit** (Fantasy): Wer hat genug Münzen, um sich den begehrten Stern zu sichern, bevor die Statue weiterwandert? Der Makro-Loop liefert die **Fortschritts-Erzählung** (Challenge): Über 8–10 Runden baut sich eine Rangfolge auf, die bis zur letzten Runde offen bleibt (Catch-Up hält sie spannend). Das wiederkehrende "Nur noch eine Runde"-Gefühl entsteht dadurch, dass jede Runde mit einem klaren Höhepunkt (Minispiel) endet und die Stern-Phase den Spielstand sichtbar verändert — der natürliche Drang, den eigenen Rückstand aufzuholen, trägt zur nächsten Runde.

Design-Ziele nach MDA: **Sensation** (Würfel- und Münz-Feedback), **Challenge** (Minispiele), **Fellowship** (geteilte Tischplatten-Atmosphäre), **Discovery** (Feld-Effekte), **Fantasy** (Arena-Show). Nach der Selbstbestimmungstheorie (SDT) bedient der Loop **Autonomie** (Pfadwahl, Kauf-Entscheidungen, Item-Timing), **Kompetenz** (Minispiel-Skill, Planung der Zugreihenfolge) und **Relatedness** (ArenaStar als Gastgeber, gemeinsame Erlebnisse).

## 3. Detailed Rules

### 3.1 Begriffe: Zug, Runde, Partie

1. **Zug (Turn):** Die Aktion eines einzelnen Spielers, bestehend aus Roll-Phase → Bewegungs-Phase → Feld-Effekt-Phase. Ein Zug wird vollständig abgeschlossen, bevor der nächste Spieler an der Reihe ist.
2. **Runde (Round):** Ein vollständiger Durchgang durch alle Spieler (jeder macht genau einen Zug), gefolgt von der Minispiel-Phase und der Stern-Phase. Die Runde ist die Basiseinheit des Makro-Loops.
3. **Partie (Game):** Das gesamte Spiel: Vorrunde (Reihenfolge-Würfeln) → 8–10 Runden → Bonus-Stern-Phase → Endabrechnung → Siegerehrung → Statistik-Bildschirm.
4. **Umlauf (Lap):** Das einmalige Überqueren des Startfelds im Uhrzeigersinn. Ein Umlauf ist **keine** Spielrunde; der Begriff wird in [dice-movement](dice-movement.md) präzisiert und für Statistiken (z. B. Vielläufer-Bonus) genutzt.

### 3.2 Die Phasen-Struktur einer Runde

Jede Runde läuft exakt in dieser Reihenfolge ab:

1. **Zug-Phase:** Alle Spieler machen in fester Zug-Reihenfolge genau einen Zug (Roll → Move → Feld-Effekt).
2. **Minispiel-Phase:** Nachdem der letzte Spieler seinen Zug beendet hat, wird immer genau ein Minispiel gespielt (unabhängig davon, auf welchen Feldern die Spieler gelandet sind). ArenaStar kündigt das Minispiel an, die Spieler konkurrieren, Münzen werden nach Platzierung vergeben (Tabelle in [coin-economy](coin-economy.md)).
3. **Stern-Phase:** Stern-Käufe werden abgewickelt (Spieler, die auf dem aktiven Sternen-Shop-Feld stehen), die Sternen-Statue wandert nach einem Kauf um, der Spielstand wird aktualisiert und als Runden-Zusammenfassung angezeigt.

Es gibt **keine** weitere Phase pro Runde. Insbesondere löst das Landen auf einem Mini-Spiel-Feld **kein** eigenes Minispiel aus — das Minispiel ist eine feste Runden-Phase (siehe 3.2.2). Mini-Spiel-Felder sind neutrale Landefelder ohne Effekt (Design-Entscheidung, dokumentiert in Sektion 6).

### 3.3 Der Zug (Turn) eines Spielers

Der aktive Spieler (der an der Reihe ist) durchläuft drei Unterphasen, die nicht unterbrochen werden können:

**Phase A — Roll-Phase (Würfeln):**
1. Der aktive Spieler bestätigt den Würfelwurf (Standard-Taste: Bestätigen/Springen). Wurde vor dem Zug ein Item mit Würfel-Modifikator genutzt (z. B. Glücks-Würfel), gilt der modifizierte Würfel; Details in [dice-movement](dice-movement.md).
2. ArenaStar führt die Würfel-Animation aus (Dauer 2,5 s): Der Würfel wird geworfen, das Ergebnis wird am Ende der Animation sichtbar und angesagt.
3. Das Wurfergebnis ist bereits beim Start der Animation festgelegt (durch den Server/Spielleiter bestimmt); die Animation ist rein kosmetisch.
4. Nach der Animation wird das Ergebnis angezeigt (Zahl + Ansage) und die Bewegungs-Phase beginnt automatisch.

**Phase B — Bewegungs-Phase (Ziehen):**
1. Der Charakter bewegt sich Feld für Feld in Bewegungsrichtung (siehe 3.4) um die gewürfelte Anzahl Felder. Jedes Feld kostet standardmäßig 0,3 s; der Spieler kann durch Gedrückthalten der Beschleunigungs-Taste (A/Enter) auf 0,12 s pro Feld verkürzen.
2. Erreicht der Charakter eine Abzweigung/Kreuzung mit noch verbleibenden Schritten, pausiert die Bewegung und der Spieler wählt die Richtung (Details in [dice-movement](dice-movement.md)).
3. Die Bewegung endet nach exakt der gewürfelten Schrittzahl auf dem Zielfeld. Die Bewegung kann nicht abgebrochen, angehalten oder vorzeitig beendet werden.
4. Das Überqueren des Startfelds ist erlaubt und zählt als Umlauf (kein Anhalten, kein automatischer Bonus; siehe [dice-movement](dice-movement.md)).

**Phase C — Feld-Effekt-Phase:**
1. Nachdem der Charakter das Zielfeld erreicht hat, wird der Feld-Effekt des Zielfelds ausgelöst.
2. Feld-Effekt-Typen: Start (kein Effekt), Sternen-Shop (Kaufoption, siehe [star-economy](star-economy.md)), Item-Shop (Kaufoption), Ereignis (Zufalls-Ereignis), Glück/Pech (Münzen ±), Münz-Bonus (Münzen +), Mini-Spiel (kein Effekt). Die Feldtypen und ihre Verteilung definieren die Kapitel [board-architecture](board-architecture.md) und die Feld-Kapitel.
3. Nach Abschluss des Feld-Effekts (inklusive aller Animationen und Münz-Änderungen) endet der Zug. Der nächste Spieler in der Zug-Reihenfolge ist an der Reihe.

**Regel der Nicht-Unterbrechbarkeit:** Während eines Zugs können andere Spieler keine Aktionen ausführen. Sie können zuschauen und (lokal) mit einer Taste kommentieren, aber keine Spielfunktionen beeinflussen.

### 3.4 Minispiel-Phase

1. Nach dem letzten Zug der Runde startet die Minispiel-Phase immer. Ausnahme: Keine — die Phase ist fester Bestandteil jeder Runde.
2. ArenaStar kündigt das Minispiel an (5 s Intro inkl. Einblendung von Name und Kategorie).
3. Alle anwesenden Spieler nehmen teil (2–8). Die Charaktere werden visuell zur Arena geführt; die Brett-Positionen bleiben unverändert gespeichert.
4. Das Minispiel dauert ca. 30 s (Standard; Abweichungen definiert das Minispiel selbst im Rahmen der [minigame-architecture](minigame-architecture.md)).
5. Nach Ende wird die Platzierung ermittelt und in Münzen umgerechnet (Tabelle in [coin-economy](coin-economy.md)). Der Verlierer-Boost ([catch-up](catch-up.md)) wird addiert.
6. Die Münz-Vergabe wird als Ergebnis-Bildschirm angezeigt (ca. 10 s), danach geht es in die Stern-Phase.

### 3.5 Stern-Phase

1. **Kauf-Abwicklung:** Spieler, die auf dem aktiven Sternen-Shop-Feld stehen und in dieser Runde noch keinen Stern gekauft haben, dürfen in Zug-Reihenfolge einen Stern kaufen (20 Münzen, optional). Käufe werden sofort abgewickelt; nach jedem Kauf wandert die Sternen-Statue gemäß [star-economy](star-economy.md) um.
2. **Sonderfall Statuen-Ziel:** Wenn die Statue durch eine Umsiedlung auf ein Feld zieht, auf dem ein Spieler steht, erhält dieser Spieler in derselben Stern-Phase eine einmalige Kaufgelegenheit (Regel und Kette in [star-economy](star-economy.md) Abschnitt 3.4).
3. **Standings-Update:** Nach allen Käufen wird die Rangfolge (Sterne, dann Münzen, dann Minispiel-Siege) neu berechnet und als Runden-Zusammenfassung eingeblendet (ca. 5 s).
4. **Runden-Ende:** Die Stern-Phase endet; damit ist die Runde abgeschlossen.

### 3.6 Runden-Grenzen

**Beginn einer Runde:**
1. Der Runden-Zähler wird um 1 erhöht.
2. ArenaStar kündigt die Runde an ("Runde X von N").
3. Pro-Runden-Zustand wird zurückgesetzt: Verbrauchte Schild-Ladungen, einmalige Modifikatoren und alle anderen Zustände, die "für diese Runde" gelten (Details in den Item-Kapiteln).
4. Der Startspieler der Runde beginnt mit seinem Zug.

**Ende einer Runde:** Die Runde endet, wenn die Stern-Phase abgeschlossen ist (inklusive Standings-Anzeige). Danach beginnt unmittelbar die nächste Runde (3.6), ohne Pause. Nach der letzten Runde (Zähler = N) folgt statt einer neuen Runde das Spielende (Bonus-Stern-Phase etc., siehe [victory-conditions](victory-conditions.md)).

### 3.7 Spieler-Reihenfolge

1. **Vorrunde (Reihenfolge-Würfeln):** Vor Runde 1 würfeln alle Spieler einmal mit dem Standard-Würfel (1–6), durchgeführt von ArenaStar. Der Spieler mit dem höchsten Ergebnis wird Startspieler; bei Gleichstand würfeln die Gleichständigen erneut, bis der Startspieler feststeht.
2. **Feste Zug-Reihenfolge:** Die Zug-Reihenfolge ist für die gesamte Partie festgelegt: Startspieler zuerst, danach die übrigen Spieler in der Reihenfolge ihrer Sitz-/Spieler-Liste (lokal: von links nach rechts; online: in der Lobby-Reihenfolge). Die Reihenfolge wird pro Runde nicht rotiert (Standard; Rotation ist als Tuning-Knob vorgesehen, siehe Sektion 7).
3. **"Wer ist als Nächstes dran":** Nach jedem Zug rückt der nächste Spieler in der festen Reihenfolge nach; nach dem letzten Spieler folgt die Minispiel-Phase (kein Zurückspringen zum Startspieler innerhalb derselben Runde).
4. **Kennzeichnung:** Der aktive Spieler wird im HUD hervorgehoben; ArenaStar benennt ihn mit Namen.

### 3.8 Bestimmung der Rundenanzahl

Die Rundenanzahl N wird bei der Partie-Erstellung bestimmt:

1. **Standard (empfohlener Wert):** N ergibt sich aus der Spielerzahl gemäß folgender Tabelle:

| Spielerzahl | Standard-Runden N |
|---|---|
| 2–3 | 10 |
| 4–5 | 9 |
| 6–8 | 8 |

2. **Manuelle Auswahl:** Die Lobby bietet eine Auswahl von N ∈ {8, 9, 10} an. Wählt der Gastgeber einen Wert, überschreibt dieser den Standardwert. Der Standardwert ist vorausgewählt (Default), kann aber geändert werden.
3. **Geltungsbereich:** N wird einmalig zu Partiebeginn festgelegt und während der Partie nicht verändert.
4. **Ziel:** Die Kombination aus Spielerzahl und N hält die Partie-Dauer im Bereich 20–30 Minuten (siehe Sektion 4).

### 3.9 Zeitbudget und Pacing

Die folgenden Budgets sind Richtwerte für die Phasen-Dauer (Messung: aktive Zeit ohne Puffer durch Bedenkzeit):

| Phase | Budget |
|---|---|
| Roll-Phase (Eingabe + Animation 2,5 s + Ansage) | 6–10 s |
| Bewegungs-Phase (durchschnittlich 3,5 Felder × 0,3 s + Pfadwahl) | 2–6 s |
| Feld-Effekt-Phase | 2–5 s |
| **Zug gesamt (Zielwert)** | **ca. 15 s** |
| Minispiel-Intro | 5 s |
| Minispiel-Spiel | 30 s |
| Minispiel-Ergebnis | 10 s |
| **Minispiel-Phase gesamt** | **ca. 45 s** |
| Stern-Phase | 10–15 s |

Es gibt **keine** harte Zeitbegrenzung für die Eingabe (Würfeln, Pfadwahl, Kaufentscheidungen) im lokalen Spiel, damit niemand unter Druck gesetzt wird. Für Online-Spiele existiert ein optionaler Zug-Timer (Tuning-Knob, Sektion 7).

### 3.10 Übergang zum Spielende

Nach Abschluss der letzten Runde (Runde N) wird nicht weitergespielt. Der Ablauf ab hier ist in [victory-conditions](victory-conditions.md) spezifiziert: Bonus-Stern-Phase → Endabrechnung → Rangliste → Siegerehrung → Statistik-Bildschirm. Die Runden-Schleife ist damit geschlossen.

## 4. Formulas

### 4.1 Rundenanzahl

`N = Standard(S)` falls keine manuelle Auswahl, sonst `N = gewählter Wert ∈ {8, 9, 10}`.

- `S` = Spielerzahl (2–8).
- `Standard(S)` = 10 für S ∈ {2,3}; 9 für S ∈ {4,5}; 8 für S ∈ {6,7,8}.
- Erwartungswerte: `N` liegt immer im Intervall [8, 10]. Die manuelle Auswahl ist auf 8, 9, 10 beschränkt.

### 4.2 Zug-Dauer

`T_Zug = T_Roll + T_Bewegung + T_Feld` mit:

- `T_Roll = T_Eingabe + 2,5 s` (Animation) + `0,5 s` (Ansage). Typisch `T_Eingabe ≈ 1–5 s`.
- `T_Bewegung = X × t_Schritt + J × t_Junction`, wobei:
  - `X` = Würfelergebnis (1–6 bzw. 1–10 mit Glücks-Würfel),
  - `t_Schritt = 0,3 s` (Standard) bzw. `0,12 s` (mit Beschleunigung),
  - `J` = Anzahl überquerter Abzweigungen in diesem Zug,
  - `t_Junction = 2 s` Durchschnittswert (Entscheidungszeit; Maximum 5 s Timeout).
- `T_Feld` = Dauer des Feld-Effekts, 2–5 s.

**Erwartungswert:** Für den Standard-Würfel (E[X] = 3,5) und ein typisches Brett mit ca. 30 % Abzweigungs-Wahrscheinlichkeit pro Zug: `E[T_Bewegung] ≈ 3,5 × 0,3 + 0,3 × 2 = 1,05 + 0,6 = 1,65 s`. Mit Beschleunigung: `≈ 0,42 + 0,6 = 1,02 s`.

### 4.3 Runden-Dauer

`T_Runde(S) = S × T_Zug + T_Minispiel + T_Stern`

Mit Zielwerten `T_Zug = 15 s`, `T_Minispiel = 45 s`, `T_Stern = 12 s`:

- `S = 2`: `T_Runde = 30 + 45 + 12 = 87 s`
- `S = 4`: `T_Runde = 60 + 45 + 12 = 117 s`
- `S = 6`: `T_Runde = 90 + 45 + 12 = 147 s`
- `S = 8`: `T_Runde = 120 + 45 + 12 = 177 s`

### 4.4 Partie-Dauer

`T_Partie = N × T_Runde(S)` zuzüglich Vorrunde (`≈ 20 s`) und Spielende (`≈ 120–180 s`, [victory-conditions](victory-conditions.md)).

**Beispielrechnungen (Zielwert-Zahlen):**

| Spieler S | Runden N (Standard) | T_Runde | T_Partie |
|---|---|---|---|
| 2 | 10 | 87 s | 10 × 87 + 150 ≈ 17,5 min |
| 3 | 10 | 102 s | 10 × 102 + 150 ≈ 19,5 min |
| 4 | 9 | 117 s | 9 × 117 + 150 ≈ 21 min |
| 5 | 9 | 132 s | 9 × 132 + 150 ≈ 22,3 min |
| 6 | 8 | 147 s | 8 × 147 + 150 ≈ 22,1 min |
| 8 | 8 | 177 s | 8 × 177 + 150 ≈ 26,1 min |

- Akzeptanzband: `T_Partie` soll für S ≥ 4 im Bereich 20–30 min liegen. Für S = 2–3 kann die Partie etwas kürzer sein (ca. 17–20 min); dies ist zulässig, da weniger Spieler weniger Interaktion erzeugen.
- **Warnschwelle:** Übersteigt `T_Partie` im Mittel über 5 Testpartien 32 Minuten, ist die Rundenanzahl oder ein Phasen-Budget zu reduzieren (Tuning, Sektion 7).

## 5. Edge Cases

1. **Nur 2 Spieler:** Die Minispiel-Phase läuft normal ab (2 Spieler spielen das Minispiel). Der Verlierer-Boost ([catch-up](catch-up.md)) greift: Letzter Platz = Platz 2 erhält +1 Münze zusätzlich zur Auszahlung für Platz 2 (7 Münzen) → 8 Münzen.
2. **Spieler ist nicht bereit (AFK):** Es gibt keinen harten Timer im lokalen Spiel. In Online-Spielen mit aktivem Zug-Timer wird bei Ablauf automatisch mit dem Standard-Würfel gewürfelt und der Zug mit der Standard-Pfadwahl fortgesetzt ([dice-movement](dice-movement.md) Abschnitt 3.8). Bei Pfadwahl-Timeouts gilt der im Brett-Datensatz definierte Standard-Pfad.
3. **Disconnect eines Spielers:** Der getrennte Spieler wird für den Rest der Partie von einem Bot übernommen (KI-Richtlinien in [minigame-architecture](minigame-architecture.md) und [ui-overview](ui-overview.md)). Die Runden-Schleife wird nicht angehalten; die Zug-Reihenfolge bleibt unverändert.
4. **Alle Spieler beenden die Bewegung auf demselben Feld:** Zulässig. Mehrere Spieler können gleichzeitig auf einem Feld stehen (auch auf dem Sternen-Shop-Feld). Die Kauf-Abwicklung erfolgt in Zug-Reihenfolge ([star-economy](star-economy.md)).
5. **Stern-Phase ohne Käufe:** Falls niemand kauft, wandert die Statue nicht, der Spielstand wird trotzdem angezeigt, die Runde endet. Es gibt keinen "Zwangskauf".
6. **Minispiel endet im Gleichstand:** Die Platzierungs-Auflösung (inkl. geteilter Plätze) definiert [minigame-rewards](minigame-rewards.md). Die Münz-Vergabe erfolgt nach der dortigen Tabelle; geteilte Plätze teilen die Münz-Werte gemäß jener Tabelle.
7. **Letzter Spieler hat einen sehr langen Zug (Glücks-Würfel 10):** Die Runden-Dauer schwankt; der Pacing-Wert in 4.4 ist ein Mittelwert. Kein Abbruchmechanismus nötig; die Beschleunigungs-Taste kompensiert.
8. **Runden-Zähler überläuft:** N ist auf 10 begrenzt; ein Überlauf ist ausgeschlossen. Nach Runde N startet keine Runde N+1, sondern das Spielende.
9. **Partie wird mitten in einer Runde gespeichert/verlassen:** Der Spielstand speichert die Runden-Nummer und den Index des aktiven Spielers; beim Fortsetzen beginnt die Runde an derselben Position (Persistenz-Vertrag in [technical-data-structures](technical-data-structures.md)).
10. **Spieler wünscht Überspringen von Animationen:** Würfel-, Bewegungs- und Ergebnis-Animationen können per Taste übersprungen werden (Ergebnis steht bereits fest). Dies ändert nie den Spielzustand, nur die Darstellungszeit.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments (benötigte Systeme)

| System/Kapitel | Art | Status | Verwendung |
|---|---|---|---|
| `design/gdd/dice-movement.md` | Peer | Geschrieben | Definiert Würfel, Bewegung, Pfadwahl, Startfeld-Umlauf, die in der Zug-Phase referenziert werden. |
| `design/gdd/coin-economy.md` | Peer | Geschrieben | Definiert Minispiel-Auszahlungen, die die Minispiel-Phase auszahlt, und Münz-Bewegungen der Feld-Effekte. |
| `design/gdd/star-economy.md` | Peer | Geschrieben | Definiert Stern-Kauf und Statuen-Wanderung in der Stern-Phase. |
| `design/gdd/victory-conditions.md` | Peer | Geschrieben | Definiert das Spielende nach Runde N (Bonus-Sterne, Siegerehrung). |
| `design/gdd/catch-up.md` | Peer | Geschrieben | Verlierer-Boost, der in der Minispiel-Phase addiert wird; Ereignis-Felder mit Rang-Bezug. |
| `design/gdd/board-architecture.md` | Peer | Geplant (noch nicht geschrieben) | Definiert die 40-Felder-Verkettung, Abzweigungen und Feldtypen; der Kern-Loop konsumiert diese Daten. |
| `design/gdd/field-*.md` (7 Kapitel) | Peer | Geplant (noch nicht geschrieben) | Definieren die einzelnen Feld-Effekte, die in Phase C ausgelöst werden. |
| `design/gdd/minigame-architecture.md` | Peer | Geplant (noch nicht geschrieben) | Definiert den Minispiel-Vertrag (Ladezeit, Dauer, Ergebnis); die Minispiel-Phase ruft diesen Vertrag auf. |
| `design/gdd/ui-hud.md`, `ui-board.md` | Konsument | Geplant (noch nicht geschrieben) | Zeigen Runden-Anzeige, aktiven Spieler, Phasen-Fortschritt. |
| `design/gdd/technical-multiplayer.md` | Konsument | Geplant (noch nicht geschrieben) | Muss die feste Zug-Reihenfolge und den Server-entschiedenen Würfelwurf synchronisieren. |

**Hinweis zu Geplant-Status:** Die oben als "Geplant" markierten Kapitel existieren noch nicht auf der Platte. Sobald sie geschrieben werden, müssen sie in ihren Dependencies-Sektionen einen Rückverweis auf dieses Kapitel enthalten (Bidirektionalitäts-Pflicht laut bible-index.md Abschnitt 3.4).

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|---|---|
| Alle Feld-Kapitel | Definieren Effekte, die nur in Phase C eines Zugs ausgelöst werden; sie müssen die Phasen-Terminologie (Roll/Move/Feld-Effekt) dieses Dokuments übernehmen. |
| `minigame-rewards.md` | Auszahlungen werden in der Minispiel-Phase dieses Loops angewendet. |
| `ui-hud.md` | Runden-Zähler und aktiver-Spieler-Anzeige folgen der Struktur dieses Dokuments. |
| `audio-overview.md` | Musik-/SFX-Cues folgen den Phasen-Grenzen (Würfel, Landung, Minispiel, Stern-Phase). |

### 6.3 Design-Entscheidungen (dokumentierte Abweichungen/Klärungen)

1. **Mini-Spiel-Feld ohne Lande-Effekt:** Das Konzept führt den Feldtyp "Mini-Spiel" mit der Mehrheit der Felder. Dieses Kapitel legt fest: Das Minispiel ist eine feste Runden-Phase (3.4), kein Lande-Effekt. Mini-Spiel-Felder sind daher neutrale Landefelder (kein Effekt in Phase C). Das geplante Kapitel `field-minigame.md` muss dies spiegeln.
2. **Kein Umlauf-Bonus:** Das Überqueren des Startfelds gibt standardmäßig keine Münzen (anders als in Super Tux Party Legacy). Ein Umlauf-Bonus ist nur als Tuning-Knob vorgesehen (Sektion 7), nicht als Standard.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|---|---|---|---|---|
| Schritt-Zeit `t_Schritt` | Feel | 0,15–0,6 s | 0,3 s | Bestimmt das Bewegungstempo; kleiner = zügiger, größer = dramatischer. |
| Schritt-Zeit (beschleunigt) | Feel | 0,05–0,3 s | 0,12 s | Gefühl der Beschleunigungs-Taste; muss spürbar schneller als Standard sein. |
| Würfel-Animation | Feel | 1,5–4,0 s | 2,5 s | Spannungsaufbau vor dem Ergebnis; zu lang = zäh, zu kurz = wirkungslos. |
| Minispiel-Dauer | Gate | 20–45 s | 30 s | Steuert die Runden- und Partie-Dauer direkt (4.4). |
| Stern-Phase-Budget | Gate | 8–20 s | 12 s | Pacing der Runden-Zusammenfassung. |
| Zug-Timer (Online) | Gate | Aus / 15–120 s | Aus | Verhindert Ewigkeiten in Online-Partien; bei Ablauf Auto-Wurf + Standard-Pfad. |
| Abzweigungs-Timeout | Gate | 2–10 s | 5 s | Wie lange die Pfadwahl wartet, bevor der Standard-Pfad gewählt wird. |
| Rundenanzahl `N` | Gate | {8, 9, 10} | Tabelle 3.8 | Skaliert die Partie-Dauer; Kern-Knob für das 20–30-Min-Ziel. |
| Rotierende Zug-Reihenfolge | Kurve | An/Aus | Aus | Wenn An: Startspieler rotiert pro Runde um eine Position (Fairness-Experiment; ändert die Vorrunde nicht). |
| Umlauf-Bonus | Kurve | 0–10 Münzen | 0 | Optionaler Belohnungs-Anreiz pro Umlauf; bei Aktivierung mit [coin-economy](coin-economy.md) abstimmen. |

Alle Knobs liegen in externen Daten-/Konfigurationsdateien (`assets/data/`), nicht im Code. Änderungen an den Gate-Knobs erfordern eine Neuberechnung der Partie-Dauer (Formel 4.4) und eine Anpassung des Pacing-Tests (Acceptance Criteria).

## 8. Acceptance Criteria

Ein QA-Tester oder CI-Hook kann die folgenden Prüfungen ausführen (PASS/FAIL):

1. **Phasen-Reihenfolge:** In jeder Runde tritt exakt die Sequenz Zug-Phase → Minispiel-Phase → Stern-Phase auf; keine Phase fehlt und keine zusätzliche Phase existiert. PASS/FAIL.
2. **Zug-Vollständigkeit:** Jeder Spieler macht pro Runde genau einen Zug. Nach dem letzten Spieler beginnt immer die Minispiel-Phase, nicht der Startspieler erneut. PASS/FAIL.
3. **Rundenanzahl:** Für jede Spielerzahl S ∈ {2..8} startet eine Standard-Partie mit N laut Tabelle 3.8. Eine manuelle Auswahl (8/9/10) überschreibt den Standard. PASS/FAIL.
4. **Reihenfolge-Stabilität:** Die Zug-Reihenfolge bleibt über alle Runden identisch (bei Standard-Einstellung). Der Startspieler ist der Gewinner der Vorrunde (höchster Wurf; Gleichstand → Wiederholung). PASS/FAIL.
5. **Minispiel immer:** Auch wenn kein Spieler auf einem Mini-Spiel-Feld gelandet ist, wird pro Runde genau ein Minispiel gespielt. PASS/FAIL.
6. **Stern-Phase:** Die Stern-Phase zeigt den Spielstand korrekt an; Käufe werden nur für berechtigte Spieler (auf dem aktiven Sternen-Shop-Feld) abgewickelt; die Statue wandert nur nach einem Kauf. PASS/FAIL.
7. **Zeitbudget:** In 5 Testpartien (4 Spieler, Standard-Einstellungen) liegt die gemessene Partie-Dauer im Mittel im Bereich 20–30 Minuten. Kein Einzellauf überschreitet 32 Minuten (außer bei manuellen Pausen). PASS/FAIL.
8. **Pacing-Messung:** Die durchschnittliche Zug-Dauer liegt unter 20 s (Ziel 15 s); die Minispiel-Phase unter 60 s; die Stern-Phase unter 20 s. PASS/FAIL.
9. **Nicht-Unterbrechbarkeit:** Während eines Zugs kann kein anderer Spieler eine Spielfunktion auslösen (nur Zuschauen/Kommentieren). PASS/FAIL (manuell, 2 Spieler).
10. **Spielende-Übergang:** Nach Runde N startet keine Runde N+1; stattdessen beginnt die Bonus-Stern-Phase aus [victory-conditions](victory-conditions.md). PASS/FAIL.
11. **Erlebbar (Experiential):** Ein neuer Spieler versteht nach einer Testrunde ohne Anleitung, wann er an der Reihe ist und was als Nächstes passiert (Runde → Minispiel → Stern). Bestätigt durch Beobachter-Protokoll in einem Playtest mit ≥ 1 Neuling. PASS/FAIL.
