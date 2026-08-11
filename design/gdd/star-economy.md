# Stern-Ökonomie — Party Arena Game Bible

> **Teil:** I — Core Game
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/bible-index.md

---

## 1. Overview

Sterne sind die **Siegwährung** von Party Arena: Gewonnen hat am Ende, wer die meisten Sterne besitzt ([victory-conditions](victory-conditions.md)). Sterne werden auf zwei Wegen vergeben: (1) durch **Kauf** am aktiven Sternen-Shop für 20 Münzen und (2) durch **Bonus-Sterne** am Spielende, bei denen aus einem Pool von 10 Kategorien 3 zufällig gezogen und vergeben werden. Dieses Kapitel definiert die vollständige Stern-Ökonomie: die 2–3 Sternen-Shop-Felder pro Brett mit genau einer aktiven Sternen-Statue, den Kauf-Ablauf inklusive der Zeitfenster, die Wanderung der Statue nach jedem Kauf (inkl. Sonderfall "Statue zieht auf besetztes Feld"), die Regel von höchstens einem Stern-Kauf pro Spieler und Runde, den Bonus-Stern-Pool mit allen Kategorien und ihren Messregeln sowie die explizite Anti-Regel, dass Sterne nicht gestohlen oder durch Items manipuliert werden können. Die Münz-Seite (wie Spieler auf 20 Münzen kommen) ist in [coin-economy](coin-economy.md) spezifiziert; dieses Kapitel beschreibt nur die Stern-Seite.

## 2. Player Fantasy

Der Stern ist der **glänzende Pokal** der Partie (MDA: Fantasy + Challenge). Er ist selten, teuer und begehrt — und er wandert. Die zentrale emotionale Erfahrung ist das **Jagen der Statue**: Man sieht, wo der Stern steht, plant die Route über Abzweigungen, zählt die Münzen zusammen und hofft, dass der Würfel die exakte Landung bringt. Jeder Kauf ist ein **Triumph-Moment** (Sensation + Kompetenz): ArenaStar überreicht den Stern mit Fanfare, die Statue verschwindet und taucht woanders wieder auf — der Besitzstand verändert sich sichtbar. Die Bonus-Sterne am Ende erzeugen die **Comeback-Hoffnung** (Challenge): Selbst wer nie genug Münzen für einen Stern hatte, kann durch Pechvogel-, Vielläufer- oder andere Kategorien noch Punkte sammeln. Die Anti-Regel "kein Stern-Diebstahl" schützt dieses Gefühl: Sterne sind unantastbar und können nie durch Items oder Events entrissen werden — der Spieler verliert einen erkauften Stern nie unfreiwillig. Das macht den Stern zur verlässlichen, verdienten Größe, um die herum die gesamte Partie aufgebaut ist.

## 3. Detailed Rules

### 3.1 Sternen-Shop-Felder und die aktive Sternen-Statue

1. Jedes Brett besitzt **2–3 Sternen-Shop-Felder** (Konzept: 2–3; die genaue Anzahl legt [board-architecture](board-architecture.md) je Insel fest).
2. **Genau eine aktive Sternen-Statue:** Zu jedem Zeitpunkt ist genau eines der Sternen-Shop-Felder das **aktive Sternen-Shop-Feld**, auf dem die Sternen-Statue steht. Die übrigen Sternen-Shop-Felder sind inaktiv (die Statue ist dort nicht sichtbar; auf ihnen ist kein Kauf möglich).
3. **Startposition:** Zu Partiebeginn wird die Statue per Gleichverteilung auf eines der Sternen-Shop-Felder gesetzt (jedes Feld gleich wahrscheinlich). Die Startposition wird einmalig gewürfelt und ist für alle Spieler sichtbar.
4. **Sichtbarkeit:** Die Position der Statue ist zu jeder Zeit für alle Spieler sichtbar (Statue + Markierung im UI). Es gibt keine verdeckten Stern-Positionen.

### 3.2 Stern-Kauf

1. **Preis:** Ein Stern kostet exakt **20 Münzen**. Es gibt keinen Mengenrabatt, keine Preissteigerung und keine Verhandlung.
2. **Kaufpflicht:** Der Kauf ist **optional**. Ein Spieler, der auf dem aktiven Sternen-Shop-Feld steht und ≥ 20 Münzen besitzt, kann kaufen, muss aber nicht (strategische Entscheidung, z. B. Münzen für Items sparen).
3. **Kauf-Fenster A (primär):** Ein Spieler, der während seines Zugs auf dem aktiven Sternen-Shop-Feld **landet**, darf in seiner Feld-Effekt-Phase kaufen. Nach erfolgreichem Kauf wandert die Statue sofort um (3.3).
4. **Kauf-Fenster B (Sonderfall):** Zieht die Statue durch eine Umsiedlung auf ein Feld, auf dem ein Spieler steht, erhält dieser Spieler in der **nächsten Stern-Phase** eine einmalige Kaufgelegenheit (Details 3.4).
5. **Exaktheit:** Ein Stern kann nur durch **exaktes Landen** auf dem aktiven Sternen-Shop-Feld gekauft werden. Vorbeiziehen (Überlaufen) berechtigt nicht zum Kauf; es gibt kein Drüber-Zählen.
6. **Ablauf:** Der Spieler bestätigt den Kauf; 20 Münzen werden abgezogen (bei weniger als 20 Münzen ist die Kauf-Option nicht wählbar, siehe [coin-economy](coin-economy.md) Abschnitt 5), der Stern wird zur Stern-Anzeige des Spielers addiert, ArenaStar inszeniert die Übergabe, die Statue wandert.
7. **Maximal ein Kauf pro Spieler und Runde:** Ein Spieler kann in einer Runde höchstens einen Stern kaufen. Dies gilt unabhängig davon, wie oft die Statue im selben Zeitraum auf sein Feld zieht (Schutz vor Kettenkäufen, siehe Edge Cases 5.6).

### 3.3 Wanderung der Sternen-Statue

1. **Auslöser:** Die Statue wandert **nur nach einem erfolgreichen Kauf**. Sie wandert nicht zeitbasiert, nicht bei Rundenbeginn und nicht ohne Kauf.
2. **Zielmenge:** Kandidaten sind alle Sternen-Shop-Felder **außer dem aktuellen** (die Statue bleibt nie an Ort und Stelle).
3. **Auswahlregel:**
   - Gibt es unter den Kandidaten mindestens ein Feld, auf dem **kein** Spieler steht, wird per Gleichverteilung unter diesen unbesetzten Kandidaten gewählt.
   - Sind **alle** Kandidaten besetzt, wird per Gleichverteilung unter allen Kandidaten gewählt.
4. **Sofortige Umsetzung:** Die Statue erscheint sofort am Ziel; das vorherige Feld wird inaktiv. Die Umsiedlung ist für alle Spieler sichtbar (kurze Animation, ca. 2 s).
5. **Kauf-Fenster B-Trigger:** Steht auf dem Zielfeld bereits ein Spieler, wird für diesen Spieler ein Kauf-Fenster B registriert (3.4).

### 3.4 Kauf-Fenster B (Statue zieht auf besetztes Feld)

1. **Auslösung:** Wird ein Spieler durch eine Umsiedlung zum Steher auf dem aktiven Sternen-Shop-Feld (3.3.5), erhält er eine einmalige Kaufgelegenheit.
2. **Zeitpunkt:** Die Kaufgelegenheit wird in der **nächsten Stern-Phase** (dieselbe Runde, falls die Umsiedlung während der Stern-Phase geschah, sonst die Stern-Phase der laufenden Runde) in Zug-Reihenfolge abgewickelt.
3. **Berechtigung:** Ein Spieler mit bereits getätigtem Stern-Kauf in dieser Runde ist **nicht** erneut berechtigt (3.2.7).
4. **Ablauf in der Stern-Phase:** Die Stern-Phase verarbeitet Kaufgelegenheiten in Zug-Reihenfolge: Zuerst werden Spieler bedient, die per Fenster A auf dem Feld stehen und noch nicht gekauft haben; danach Spieler mit Fenster B, die noch nicht gekauft haben. Nach jedem Kauf wandert die Statue erneut (3.3); dadurch können in einer Stern-Phase **mehrere** Käufe stattfinden (nacheinander), sofern verschiedene Spieler berechtigt werden.
5. **Abbruchbedingung:** Die Stern-Phase endet, wenn kein berechtigter Spieler mehr kaufen möchte (oder darf). Es wird nicht "künstlich" weitergelost.

### 3.5 Bonus-Sterne am Spielende

Die Bonus-Stern-Phase läuft nach der letzten Runde ab (Einbettung in [victory-conditions](victory-conditions.md)). Dieses Kapitel definiert den Pool, die Auswahl und die Vergabe.

**Auswahl:**
1. Aus dem Pool von **10 Kategorien** werden **genau 3 Kategorien** per Gleichverteilung **ohne Zurücklegen** gezogen (jede der `C(10,3) = 120` Kombinationen gleich wahrscheinlich).
2. Die Ziehung erfolgt **nach** der letzten Runde, für alle sichtbar (ArenaStar kündigt die Kategorien an, bevor die Sieger gezeigt werden).

**Pool (10 Kategorien mit Messregeln):**

| # | Kategorie | Messregel (wer erhält den Stern) |
|---|---|---|
| 1 | **Reichster** | Die meisten Münzen bei Spielende (Höchststand). |
| 2 | **Schnellster** | Die meisten Minispiel-Siege (Platz 1 in Minispielen). |
| 3 | **Item-Meister** | Die meisten genutzten Items (Item-Aktivierungen, nicht Käufe). |
| 4 | **Event-König** | Die meisten betretenen Ereignis-Felder (Landungen auf Ereignis-Feldern). |
| 5 | **Pechvogel** | Die meisten betretenen Glück/Pech-Felder mit **negativem** Ergebnis (Münzverlust). |
| 6 | **Kampfbereit** | Die meisten gewonnenen PvP-Interaktionen (direkte Spieler-gegen-Spieler-Wirkungen, z. B. erfolgreicher Dieb-Handschuh-Einsatz, Duell-Ereignisse; Zählung siehe 3.5.1). |
| 7 | **Vielläufer** | Die meisten zurückgelegten Felder insgesamt (Summe aller Bewegungsschritte inkl. erzwungener Rückwärtsbewegung). |
| 8 | **Entdecker** | Die meisten **verschiedenen** Felder, die je besucht (betreten) wurden (Eindeutigkeit über Feld-Index des Bretts). |
| 9 | **Glückspilz** | Die meisten betretenen Glück/Pech-Felder mit **positivem** Ergebnis (Münzgewinn). |
| 10 | **Sparfuchs** | Die höchsten **Lebenszeit-Münzeinnahmen** (Summe aller Münzgewinne aus allen Quellen über die Partie; unabhängig vom Endbestand). |

**Mess-Regeln (3.5.1):**
- **Zählzeitraum:** Alle Zähler laufen über die gesamte Partie (alle Runden). Werte werden nach der letzten Runde eingefroren.
- **PvP-Interaktionen (Kampfbereit):** Eine PvP-Interaktion ist jede Mechanik, bei der ein Spieler gezielt einen anderen Spieler als Ziel wählt oder mit ihm direkt konkurriert (Item-Einsätze mit Ziel, Duell-Ereignisse). Als "gewonnen" gilt, wenn der Effekt zugunsten des auslösenden Spielers endet (z. B. erfolgreicher Diebstahl; ein fehlgeschlagener Diebstahl bei 0 Münzen des Ziels zählt nicht als Sieg). Die meldenden Systeme (Items, Ereignisse) müssen ein Flag "PvP-Interaktion gewonnen" an die Statistik melden.
- **Glück/Pech-Zählung:** Für Pechvogel/Glückspilz zählt nur das **Ergebnis** des Glück/Pech-Felds (Münzverlust bzw. Münzgewinn), nicht die Feld-Existenz. Ein Glück/Pech-Feld mit Münzgewinn zählt für Glückspilz, eines mit Verlust für Pechvogel. Beträgt der Verlust/Gewinn 0 (Extremfall), zählt das Feld für keine der beiden Kategorien.

**Vergabe (3.5.2):**
1. Jede der 3 gezogenen Kategorien vergibt **genau 1 Bonus-Stern**.
2. **Gleichstand in einer Kategorie:** Sind zwei oder mehr Spieler in einer Kategorie gleichauf (gleicher Messwert), erhält **jeder** dieser Spieler 1 Bonus-Stern. Dies kann die Gesamtzahl vergebener Bonus-Sterne über 3 anheben (Maximum: 3 × S, wenn in jeder Kategorie alle S Spieler gleichauf sind).
3. Ein Spieler kann Bonus-Sterne aus mehreren Kategorien erhalten (kumulativ).
4. Die Bonus-Sterne werden addiert und fließen in die Endabrechnung ein ([victory-conditions](victory-conditions.md) Abschnitt 3.3).

### 3.6 Anti-Regel: Kein Stern-Diebstahl, keine Stern-Manipulation

1. **Items manipulieren nur Münzen:** Alle Items (Dieb-Handschuh, Schutzschild, Münz-Magnet, Teleporter, Glücks-Würfel) wirken auf Münzen, Bewegung, Positionen oder Würfel — **niemals** auf Sterne. Ein Item, das Sterne entziehen, duplizieren oder umverteilen würde, ist nicht zulässig.
2. **Ereignisse manipulieren keine Sterne:** Ereignis-Felder können Münzen, Positionen, Würfel oder Reihenfolge beeinflussen, aber keine Sterne entziehen oder gewähren (Ausnahme: Bonus-Sterne sind nur das Ergebnis der Endwertung, nicht von Ereignissen).
3. **Folge:** Der Stern-Bestand eines Spielers kann sich während der Partie **nur erhöhen** (durch Kauf oder am Ende durch Bonus). Er kann nie sinken. Dies ist eine harte Design-Regel.

### 3.7 Maximal- und Minimal-Sterne

1. **Kein hartes Maximum:** Es gibt keinen harten Stern-Cap. Der realistische Erwartungsbereich pro Spieler liegt bei 0–5 Sternen (siehe Sektion 4.3).
2. **Obergrenze der Anzeige/Persistenz:** Die Stern-Anzeige und die Persistenz unterstützen bis zu 99 Sterne pro Spieler (technische Grenze, weit oberhalb realistischer Werte).
3. **Minimum:** 0. Ein Spieler kann die Partie mit 0 Sternen beenden, wenn er nie gekauft hat und keine Bonus-Sterne erhält. Das ist zulässig und wird im Statistik-Bildschirm nicht als Fehler behandelt.

## 4. Formulas

### 4.1 Bonus-Kategorien-Auswahl

`A = 3`, gezogen ohne Zurücklegen aus `P = 10` Kategorien.

- Anzahl möglicher Kategorie-Sets: `C(10,3) = (10 × 9 × 8) / (3 × 2 × 1) = 120`.
- Wahrscheinlichkeit einer bestimmten Kategorie, gezogen zu werden: `3/10 = 30 %`.
- Jedes Set ist gleich wahrscheinlich: `P(Set) = 1/120`.

### 4.2 Vergebene Bonus-Sterne

`B = Σ_{c ∈ A} (Anzahl der Spieler, die in Kategorie c gleichauf auf Platz 1 liegen)`

- Minimalwert: `B = 3` (in jeder Kategorie ein eindeutiger Sieger).
- Maximalwert: `B = 3 × S` (in jeder Kategorie alle S Spieler gleichauf). Beispiel 4 Spieler: `B_max = 12`.

### 4.3 Kauf-Häufigkeit (Schätzung für Balance)

Erwartete Stern-Käufe pro Spieler in einer Partie:

`E[Sterne] ≈ (Anzahl erreichter aktiver Shop-Landungen) × P(≥ 20 Münzen beim Landen)`

Richtwerte aus Playtest-Zielen:
- Bei Standard-Würfel (1–6) und 40-Felder-Brett mit 2–3 Shop-Feldern erreicht ein Spieler den aktiven Shop **durchschnittlich 1,5- bis 3-mal** pro Partie (inkl. Fenster B).
- Da die Statue nach jedem Kauf wandert, sinkt die Trefferwahrscheinlichkeit mit jedem Kauf nicht linear; die 20-Münzen-Schwelle ist der dominierende Engpass.
- **Balance-Ziel:** Über eine 4-Spieler-Partie (9–10 Runden) sollen insgesamt 3–6 Sterne gekauft werden (0,75–1,5 pro Spieler im Schnitt). Werte außerhalb von 2–8 gekauften Sternen pro Partie sind ein Balance-Signal (siehe Acceptance Criteria).

### 4.4 Erwartungswert des Sternpreises in Münz-Äquivalenten

Ein Stern kostet 20 Münzen. Bei einer durchschnittlichen Minispiel-Auszahlung von ca. 5,4 Münzen pro Minispiel (4-Spieler-Mittel über die Tabelle in [coin-economy](coin-economy.md)) entspricht ein Stern etwa **4 Minispiel-Siegen bzw. 3–4 Runden Münzeinkommen**. Dies ist die Referenz für die Münz-Balance.

## 5. Edge Cases

1. **Spieler steht auf dem aktiven Shop-Feld, hat aber weniger als 20 Münzen:** Kein Kauf möglich; die Kauf-Option wird nicht angeboten. Der Spieler verlässt das Feld beim nächsten Zug. Kein Kredit, kein Teilkauf.
2. **Spieler entscheidet sich bewusst gegen den Kauf (≥ 20 Münzen):** Zulässig. Die Statue wandert **nicht** (kein Kauf = keine Wanderung). Ein zweites Kauf-Fenster A auf demselben Feld in derselben Runde existiert nicht, da der Spieler nur einmal landet.
3. **Zwei Spieler landen in derselben Runde auf dem aktiven Shop-Feld:** Der erste (in Zug-Reihenfolge) kauft ggf. und löst die Wanderung aus. Der zweite steht dann auf einem **inaktiven** Shop-Feld; er kann nicht kaufen (Fenster A ist an die aktive Statue gebunden). Hätte der erste **nicht** gekauft, kann der zweite beim Landen normal kaufen (Statue steht noch da).
4. **Statue wandert auf ein besetztes Feld (Fenster B):** Der stehende Spieler erhält eine Kaufgelegenheit in der nächsten Stern-Phase (3.4). Lehnt er ab oder hat er < 20 Münzen, verfällt die Gelegenheit ersatzlos.
5. **Kette in der Stern-Phase:** Kauf A → Statue wandert zu Spieler B → B kauft → Statue wandert zu Spieler C … Das ist zulässig, solange jeder Spieler höchstens einmal pro Runde kauft (3.2.7). Ein Spieler, der bereits gekauft hat, wird nicht erneut berechtigt, auch wenn die Statue wieder auf sein Feld zieht.
6. **Derselbe Spieler kauft zweimal in einer Runde (Versuch):** Verhindert durch 3.2.7. Der zweite Kaufversuch wird abgelehnt; die Statue wandert nicht.
7. **Alle Sternen-Shop-Felder besetzt:** Die Statue wandert trotzdem auf ein besetztes Feld (3.3.3). Mehrere Spieler können gleichzeitig auf Shop-Feldern stehen; das ist kein Fehler.
8. **Statue startet auf einem Feld, auf dem ein Spieler steht (Partiebeginn):** Zu Partiebeginn stehen alle Spieler auf dem Startfeld; die Statue steht auf einem Shop-Feld. Sind Start- und Shop-Feld identisch (Board-Layout erlaubt das nicht, siehe [board-architecture](board-architecture.md)), wäre dies ein Datenfehler; die Statuen-Startposition wird dann auf das nächste freie Shop-Feld verschoben.
9. **Bonus-Kategorie mit Messwert 0 bei allen Spielern:** Beispiel: Kein Spieler hat je ein Glück/Pech-Feld mit negativem Ergebnis betreten (Pechvogel). Dann gilt: **Alle** Spieler sind gleichauf (alle 0). Nach der Gleichstands-Regel (3.5.2) erhielten alle Spieler je 1 Stern. **Korrektur:** Für Kategorien, in denen der Messwert des Führenden 0 ist (niemand hat die Leistung je erbracht), wird die Kategorie als "nicht erfüllt" behandelt und **neu gezogen** (einmalig aus den verbleibenden Kategorien). Ist auch die Ersatzkategorie unerfüllt, wird die zweite Ersatzkategorie gewählt; sind alle 10 unerfüllt (praktisch ausgeschlossen), verfällt der Bonus-Stern. Dies verhindert, dass ein "Niemand-hat-etwas-getan" alle Spieler belohnt.
10. **Bonus-Kategorie-Tie zwischen mehreren Spielern:** Alle Gleichaufstehenden erhalten je 1 Stern (3.5.2). Beispiel: Spieler A und B haben je 4 Pech-Felder → beide erhalten den Pechvogel-Stern.
11. **Kampfbereit-Messung ohne PvP-Mechaniken im Spiel (eigene Partie ohne PvP-Items):** Der Messwert ist bei allen 0 → Regel 9 greift (Kategorie wird neu gezogen), sofern Kampfbereit überhaupt gezogen wurde.
12. **Stern-Anzeige über 99:** In der Praxis ausgeschlossen (max. ~10 Käufe/Partie); sollte der Wert je über 99 steigen, wird er intern unbegrenzt gespeichert, im UI aber als "99+" angezeigt (Anzeige-Limit, kein Spiel-Limit).

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments (benötigte Systeme)

| System/Kapitel | Art | Status | Verwendung |
|---|---|---|---|
| `design/gdd/coin-economy.md` | Peer | Geschrieben | Liefert die Münz-Quellen und den Münzbestand; der Kauf (20 Münzen) ist eine Münz-Senke. |
| `design/gdd/core-loop.md` | Peer | Geschrieben | Definiert die Stern-Phase als Runden-Bestandteil; dieses Kapitel spezifiziert deren Inhalt. |
| `design/gdd/victory-conditions.md` | Peer | Geschrieben | Führt die Bonus-Stern-Phase und Endabrechnung aus; konsumiert die Bonus-Kategorien und Tie-Regeln. |
| `design/gdd/catch-up.md` | Peer | Geschrieben | Nutzt Bonus-Kategorien mit Aufhol-Charakter (Pechvogel, Vielläufer, Entdecker); Verweis auf deren Effekt. |
| `design/gdd/dice-movement.md` | Peer | Geschrieben | Liefert die Treffer-Wahrscheinlichkeit für Shop-Landungen (Formel 4.3). |
| `design/gdd/board-architecture.md` | Quelle | Geplant (noch nicht geschrieben) | Definiert Anzahl und Position der 2–3 Sternen-Shop-Felder je Brett. |
| `design/gdd/field-star-shop.md` | Peer | Geplant (noch nicht geschrieben) | Definiert den Feld-Effekt des Shop-Felds; muss die Kauf-Fenster A/B dieses Kapitels implementieren. |
| `design/gdd/ui-hud.md`, `ui-board.md`, `ui-shop.md` | Konsument | Geplant (noch nicht geschrieben) | Zeigen Stern-Anzeige, Statuen-Position und Kauf-Dialog. |
| `design/gdd/item-system.md` + `item-*.md` | Peer | Geplant (noch nicht geschrieben) | Müssen die Anti-Regel "keine Stern-Manipulation" (3.6) einhalten. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|---|---|
| `coin-economy.md` | Führt den Sternen-Shop als Senke (20 Münzen); Preis-Änderungen hier müssen dort gespiegelt werden. |
| `victory-conditions.md` | Endabrechnung und Tie-Breaker verwenden Sterne als Primärschlüssel. |
| `catch-up.md` | Bonus-Kategorien (Pechvogel, Vielläufer, Entdecker) sind Teil des Aufhol-Designs. |
| `field-star-shop.md` | Muss den Kauf-Ablauf (Fenster A) und die Wanderung anbinden. |
| `technical-data-structures.md` | Persistiert Stern-Bestand (0–99+), Statuen-Position und alle Bonus-Kategorie-Zähler. |

### 6.3 Design-Entscheidungen (dokumentierte Klärungen)

1. **Eine aktive Statue:** Trotz 2–3 Shop-Feldern ist immer nur **eine** Statue aktiv (wandernd). Dies entspricht dem Konzept ("Sternen-Shop wandert nach jedem Kauf") und erzeugt das Verfolgungs-Spiel.
2. **Kauf sofort bei Landung (Fenster A) statt gebündelt in der Stern-Phase:** Sofortige Käufe geben sofortiges Feedback und vermeiden den "Warte bis Rundenende"-Frust. Die Stern-Phase behandelt nur Fenster B und die Standings-Anzeige.
3. **Gleichstand in Bonus-Kategorien = alle bekommen den Stern:** Parteifreundliche, großzügige Regel; verhindert Streit und ist deterministisch testbar.
4. **Kategorie-Neuauslosung bei Messwert 0:** Verhindert den Degenerationsfall, dass eine Kategorie, die niemand erfüllt hat, allen Spielern einen Stern schenkt (Edge Case 9).

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|---|---|---|---|---|
| Stern-Preis | Kurve | 15–30 Münzen | 20 | Zentraler Balance-Hebel: bestimmt, wie oft Sterne gekauft werden (4.3). Muss mit den Münz-Quellen in [coin-economy](coin-economy.md) abgestimmt sein. |
| Anzahl aktiver Statuen | Kurve | 1–3 | 1 | Bei > 1 aktiven Statuen sinkt der Verfolgungsdruck; mit 3.1 (eine aktive Statue) bricht. Nur als experimenteller Knob. |
| Anzahl Shop-Felder pro Brett | Gate | 2–3 | 2–3 (je Insel) | Mehr Shop-Felder = mehr potenzielle Landungen; definiert [board-architecture](board-architecture.md). |
| Anzahl Bonus-Kategorien `A` | Gate | 2–5 | 3 | Mehr Kategorien = mehr Zufall im Endergebnis; weniger = berechenbarer. |
| Pool-Größe `P` | Kurve | 8–12 | 10 | Größe des Kategorie-Pools; neue Kategorien sind messbar zu definieren (3.5). |
| Gleichstands-Regel Bonus | Gate | Alle / Nur erster | Alle | "Nur erster" = bei Tie wird per Zufall einer bestimmt (unfreundlicher, aber härter kompetitiv). |
| Max. Käufe pro Spieler/Runde | Gate | 1–2 | 1 | Bei 2 könnten reiche Spieler in einer Stern-Phase doppelt kaufen; erhöht den Stern-Umlauf. |
| Kategorie-Neuauslosung | Gate | An/Aus | An | Schaltet die Degenerations-Korrektur (Edge Case 9) ab. |

## 8. Acceptance Criteria

Ein QA-Tester oder CI-Hook kann die folgenden Prüfungen ausführen (PASS/FAIL):

1. **Eine aktive Statue:** Zu jedem Zeitpunkt der Partie ist genau ein Sternen-Shop-Feld aktiv. PASS/FAIL (Autotest über alle Runden).
2. **Kauf-Preis:** Ein Stern-Kauf zieht exakt 20 Münzen ab und erhöht den Stern-Bestand um 1. Bei < 20 Münzen ist die Kauf-Option nicht verfügbar. PASS/FAIL.
3. **Wanderung nur nach Kauf:** Die Statuen-Position ändert sich ausschließlich unmittelbar nach einem erfolgreichen Kauf und nie sonst. PASS/FAIL (Autotest: keine Positionsänderung in Runden ohne Kauf).
4. **Wanderungs-Ziel:** Die Statue wandert nie auf ihr bisheriges Feld. Bei mindestens einem unbesetzten Kandidaten wandert sie nie auf ein besetztes Feld. PASS/FAIL (Autotest über 100 simulierte Käufe).
5. **Fenster B:** Steht ein Spieler auf dem Zielfeld einer Umsiedlung, erhält er in der nächsten Stern-Phase genau eine Kaufgelegenheit (sofern er diese Runde noch nicht gekauft hat). PASS/FAIL.
6. **Max. 1 Kauf pro Spieler/Runde:** Ein Spieler kann pro Runde nicht mehr als einen Stern erwerben, auch bei mehrfachen Fenster-B-Ereignissen. PASS/FAIL (Autotest mit konstruierter Kette).
7. **Bonus-Auswahl:** In jeder Partie werden genau 3 Kategorien aus dem Pool von 10 gezogen (ohne Zurücklegen). Über 120 Partien (Autotest) wird jede Kombination aus `C(10,3)` näherungsweise gleich oft gezogen (Abweichung < 20 %). PASS/FAIL.
8. **Bonus-Messung:** Die Zähler der 10 Kategorien werden korrekt geführt (Stichproben-Vergleich mit Referenz-Protokoll einer Testpartie). PASS/FAIL.
9. **Bonus-Gleichstand:** Bei Gleichstand in einer Kategorie erhalten alle Gleichaufstehenden je 1 Stern. PASS/FAIL (Testfall mit konstruiertem Tie).
10. **Degenerations-Korrektur:** Wird eine Kategorie gezogen, deren führender Messwert 0 ist, wird sie neu gezogen; keine Kategorie vergibt Sterne an "niemand hat etwas getan". PASS/FAIL (Testfall: Partie ohne Pech-Felder, Pechvogel gezogen).
11. **Anti-Regel:** In der gesamten Item- und Ereignis-Datenbank existiert kein Effekt, der Sterne entzieht, dupliziert oder umverteilt (Skript-Scan der Datenbank). PASS/FAIL.
12. **Balance-Band:** Über 5 Testpartien (4 Spieler) werden insgesamt 2–8 Sterne gekauft (Mittel 3–6). PASS/FAIL.
