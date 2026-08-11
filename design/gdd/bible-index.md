# Bible-Index — Party Arena Game Bible

> **Teil:** 0 — Meta & Vision
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/session-1-analysis.md

---

## 1. Overview

Die Party Arena Game Bible ist die vollständige, maßgebliche Design-Dokumentation des Spiels. Sie umfasst 65 Kapitel in 11 Teilen, die vom Meta-Fundament über Core Game, Board & Fields, Items, Minigames, Characters, World, UI/UX, Audio, Narrative bis zum Technical Design alles spezifizieren, was implementiert werden muss. Dieses Dokument, der Bible-Index, ist der Einstiegspunkt: Es listet jedes Kapitel mit Dateiname und Kurzbeschreibung, definiert die Struktur- und Namenskonventionen der Bible, dokumentiert den Schreibstatus aller Kapitel und dient damit als Navigations- und Fortschrittsinstrument für das gesamte Team. Jedes Kapitel folgt verbindlich dem 8-Sektionen-Standard (Overview, Player Fantasy, Detailed Rules, Formulas, Edge Cases, Dependencies, Tuning Knobs, Acceptance Criteria) aus `.claude/rules/design-docs.md`.

## 2. Player Fantasy

Das Lesen dieses Dokuments soll sich für ein Teammitglied anfühlen wie ein guter Reiseführer durch eine große, aber übersichtliche Welt: Man weiß nach wenigen Sekunden, wo man ist, wo man hin muss und was wo zu finden ist. Die zentrale emotionale Versprechung ist **Orientierung ohne Sucharbeit**. Ein neuer Programmierer, Designer oder Artist soll in unter zwei Minuten das Kapitel finden, das seine aktuelle Frage beantwortet, und auf einen Blick sehen, ob dieses Kapitel bereits geschrieben, in Arbeit oder noch offen ist. Das Dokument erzeugt außerdem ein Gefühl von **Fortschritt und Gemeinschaftsleistung**: Jedes abgehakte Kapitel macht die Bible greifbar vollständiger, und der Fortschrittsbalken am Ende des Index ist der gemeinsame Taktgeber des Projekts. Für das Review-Wesen erfüllt der Index eine **Bündelungs-Funktion**: Er zeigt, welche Kapitel noch auf ein Design-Review warten, und macht dadurch sichtbar, wo das Projekt designseitig wirklich steht.

## 3. Detailed Rules

### 3.1 Geltungsbereich und Autorität

1. Die Game Bible ist die **Single Source of Truth** für alle Design-Entscheidungen von Party Arena. Bei Widersprüchen zwischen einem Kapitel und anderen Dateien (Code, Konzept, Issues) gilt das Kapitel der Bible als maßgeblich, sofern es nicht selbst einen expliziten Verweis auf eine noch offene Entscheidung enthält.
2. Die Quelle aller Kapitel ist das finale Konzept in `design/gdd/game-concept.md`. Kein Kapitel darf dem Konzept widersprechen, ohne die Abweichung in der Sektion **Dependencies** explizit als Design-Entscheidung zu dokumentieren.
3. Jede neue Design-Frage, die nicht durch ein bestehendes Kapitel abgedeckt ist, führt zu einem neuen Kapitel oder einer Erweiterung eines bestehenden Kapitels. Der Bible-Index wird in beiden Fällen zeitgleich aktualisiert.

### 3.2 Kapitel- und Dateinamens-Konventionen

1. **Dateinamen** sind durchgehend klein geschrieben (lowercase) und verwenden Bindestriche (kebab-case). Keine Umlaute, keine Leerzeichen, keine Sonderzeichen außer Bindestrich. Beispiel: `world-frostgipfel.md` statt `World-Frostgipfel.md`.
2. **Namensschema:** `[domäne]-[name].md`, wobei `domäne` den Teil kennzeichnet (`core`, `field`, `item`, `minigame`, `character`, `world`, `ui`, `audio`, `narrative`, `technical`) und `name` das spezifische Kapitel. Die Meta-Kapitel und der README bilden Ausnahmen (`bible-index.md`, `vision-pillars.md`, `glossary.md`, `systems-index.md`, `README.md`).
3. **Ein Kapitel = eine Datei.** Kein Kapitel wird auf mehrere Dateien aufgeteilt, und keine Datei enthält mehr als ein Kapitel. Ausnahme: `README.md` ist der reine Link-Master ohne eigenen Kapitelstatus.
4. Jede Kapiteldatei beginnt mit einem Titel-Block: `# [Titel] — Party Arena Game Bible`, gefolgt von Metadaten (`> Teil:`, `> Status:`, `> Stand:`, `> Quelle:`).
5. Die 8 Pflicht-Sektionen erscheinen in **fester Reihenfolge** mit den festen Überschriften: `## 1. Overview`, `## 2. Player Fantasy`, `## 3. Detailed Rules`, `## 4. Formulas`, `## 5. Edge Cases`, `## 6. Dependencies`, `## 7. Tuning Knobs`, `## 8. Acceptance Criteria`. Keine Sektion darf fehlen oder umbenannt werden; Unterstruktur innerhalb der Sektionen ist frei.

### 3.3 Die vollständige Kapitelliste

Status-Legende:
- **[geschrieben]** — Datei existiert in `design/gdd/` und erfüllt den 8-Sektionen-Standard.
- **[geplant]** — Kapitel ist inhaltlich spezifiziert (Konzept/Analyse vorhanden), Datei ist noch nicht geschrieben.
- **[in Arbeit]** — Datei existiert, erfüllt den Standard aber noch nicht vollständig.

#### Teil 0 — Meta & Vision (4 Kapitel)

| # | Datei | Status | Kurzbeschreibung |
|---|-------|--------|------------------|
| 0.1 | `bible-index.md` | [geschrieben] | Master-Index der gesamten Game Bible: Kapitelliste, Konventionen, Fortschritts-Tracker und Einstiegspunkt. |
| 0.2 | `vision-pillars.md` | [geschrieben] | Die 4 Design-Pfeiler (Sofort verständlich, Überzeichnet, Interaktiv wirkend, Wiedererkennbar) mit Design-Tests, Ausschlussregeln und Konfliktlösung. |
| 0.3 | `glossary.md` | [geschrieben] | Vollständiges Glossar aller Fachbegriffe inklusive Legacy-Umbenennungen von Super Tux Party. |
| 0.4 | `systems-index.md` | [geschrieben] | Komplette Systemzerlegung: Verantwortlichkeiten, Abhängigkeiten, Godot-Zuordnung, Status jedes Systems. |

#### Teil I — Core Game (6 Kapitel)

| # | Datei | Status | Kurzbeschreibung |
|---|-------|--------|------------------|
| 1.1 | `core-loop.md` | [geschrieben] | Der verschachtelte Kern-Loop: Mikro-Loop (Würfeln–Ziehen–Feld), Meso-Loop (Runde–Minispiel–Stern-Phase), Makro-Loop (8–10 Runden bis zur Siegerehrung). |
| 1.2 | `star-economy.md` | [geschrieben] | Die Stern-Ökonomie: Sternpreis (20 Münzen), wandernde Sternen-Statue, Kauf- und Neupositionierungs-Regeln, Stern als Siegwährung. |
| 1.3 | `dice-movement.md` | [geschrieben] | Würfel- und Bewegungssystem: Standard-Würfel 1–6, Würfel-Modifikatoren, Pfadwahl an Abzweigungen, Bewegungsschritte und Zwischenstopps. |
| 1.4 | `victory-conditions.md` | [geschrieben] | Siegbedingungen: meiste Sterne nach der letzten Runde, Bonus-Sterne am Spielende, Gleichstands-Regeln und Tiebreaker. |
| 1.5 | `catch-up.md` | [geschrieben] | Catch-Up-Mechaniken: Ereignis-Felder mit Aufhol-Effekten, Verlierer-Boost, Bonus-Sterne für Leistungen ohne Siegchance. |
| 1.6 | `coin-economy.md` | [geschrieben] | Die Münz-Ökonomie: Quellen (Startguthaben, Felder, Minispiele, Events), Senken (Items, Sterne, Events), Fluss-Bilanz über 8–10 Runden. |

#### Teil II — Board & Fields (8 Kapitel)

| # | Datei | Status | Kurzbeschreibung |
|---|-------|--------|------------------|
| 2.1 | `board-architecture.md` | [geschrieben] | Board-Architektur: 40-Felder-Hauptpfad, Feld-Verkettung (next/prev), sichtbare vs. unsichtbare Felder, Aufbau-Regeln je Insel. |
| 2.2 | `field-start.md` | [geschrieben] | Startfeld: Position aller Spieler zu Spielbeginn, Start-Versatz, Verhalten bei Rückkehr aufs Startfeld. |
| 2.3 | `field-star-shop.md` | [geschrieben] | Sternen-Shop-Feld: Stern-Kauf (20 Münzen), automatischer Neustart der Sternen-Statue, Positionierung im Pfad. |
| 2.4 | `field-item-shop.md` | [geschrieben] | Item-Shop-Feld: Item-Sortiment, Einkaufs-Ablauf, Inventar-Limit, Ersetzungs-Regel bei vollem Inventar. |
| 2.5 | `field-event.md` | [geschrieben] | Ereignis-Feld: zufälliges Ereignis aus der Ereignis-Kartei, positive/negative/neutrale Effekte, Catch-Up-Verzahnung. |
| 2.6 | `field-luck.md` | [geschrieben] | Glück/Pech-Feld: Münz-Gewinn oder -Verlust, Wahrscheinlichkeitsverteilung, Extremfälle bei 0 Münzen. |
| 2.7 | `field-coin-bonus.md` | [geschrieben] | Münz-Bonus-Feld: fester Münz-Bonus, Reihenfolge-Konflikt mit anderen Lande-Effekten, Interaktion mit Münz-Magnet. |
| 2.8 | `field-minigame.md` | [geschrieben] | Mini-Spiel-Feld: löst nach Abschluss aller Spielerzüge ein Minispiel aus, Team-Bildung (FFA/2v2/1v3), Moderation durch ArenaStar. |

#### Teil III — Items (6 Kapitel)

| # | Datei | Status | Kurzbeschreibung |
|---|-------|--------|------------------|
| 3.1 | `item-system.md` | [geplant] | Item-System: Item-Definition, Typen (Würfel/Platzierbar/Aktion), Inventar, Nutzungs-Zeitpunkt (vor dem Würfeln), Ser/Deserialisierung. |
| 3.2 | `item-luckydice.md` | [geplant] | Glücks-Würfel: Ersatz-Würfel mit Wurfbereich 1–10, Kosten (5 Münzen), strategische Verwendung, Regeln bei Modifikatoren. |
| 3.3 | `item-teleporter.md` | [geplant] | Stern-Teleporter: sofortige Bewegung zur aktuellen Sternen-Position, Kosten (8 Münzen), Interaktion mit Fallen und Pfadwahl. |
| 3.4 | `item-shield.md` | [geplant] | Schutzschild: verhindert den nächsten negativen Lande-Effekt, Kosten (6 Münzen), Verbrauchs-Logik und Anzeige. |
| 3.5 | `item-coinmagnet.md` | [geplant] | Münz-Magnet: doppelte Münz-Erträge für die nächsten N Feld-Effekte oder Runden, Kosten (4 Münzen), Stapel-Regel. |
| 3.6 | `item-thiefglove.md` | [geplant] | Dieb-Handschuh: stiehlt Münzen von einem gewählten Gegner, Kosten (10 Münzen), Diebstahl-Obergrenze, AI-Verhalten. |

#### Teil IV — Minigames (4 Kapitel)

| # | Datei | Status | Kurzbeschreibung |
|---|-------|--------|------------------|
| 4.1 | `minigame-architecture.md` | [geplant] | Minigame-Architektur: Plugin-Vertrag, Ladevorgang, Spieler-Zuweisung, Timer, Ergebnisübermittlung an die Münz-Ökonomie. |
| 4.2 | `minigame-categories.md` | [geplant] | Die 5 Minigame-Kategorien (Geschicklichkeit, Reaktion, Puzzle/Logik, Rechnen/Wort, Kooperation) mit Beispiel-Spielen und Zugänglichkeits-Anforderungen. |
| 4.3 | `minigame-rewards.md` | [geplant] | Belohnungs-System: Münzen nach Platzierung, Team-Boni, Auszahlungs-Tabelle für 2–8 Spieler, Balance gegen die Stern-Kosten. |
| 4.4 | `minigame-template.md` | [geplant] | Design-Template für neue Minigames: Pflicht-Sektionen, Dauer (30 s), Input-Mapping, Sieg- und Fairness-Checkliste. |

#### Teil V — Characters (9 Kapitel)

| # | Datei | Status | Kurzbeschreibung |
|---|-------|--------|------------------|
| 5.1 | `characters-overview.md` | [geschrieben] | Charakter-System-Übersicht: Auswahlprozess, Animationsvertrag, Fähigkeiten-Philosophie (keine asymmetrischen Vorteile im Board-Spiel), Charakter-Balance. |
| 5.2 | `character-brix.md` | [geschrieben] | Brix (Stein-Golem, Mechanik-Stadt): Persönlichkeit, Silhouette, Farben, Animationen, Heimat-Bezug, Sondermerkmale. |
| 5.3 | `character-nixie.md` | [geschrieben] | Nixie (Axolotl, Sonnenstrand): Persönlichkeit, Silhouette, Farben, Animationen, Heimat-Bezug, Sondermerkmale. |
| 5.4 | `character-pip.md` | [geschrieben] | Pip (Flughörnchen, Wolkenwerk): Persönlichkeit, Silhouette, Farben, Animationen, Heimat-Bezug, Sondermerkmale. |
| 5.5 | `character-koko.md` | [geschrieben] | Koko (Panda, Zuckerwald): Persönlichkeit, Silhouette, Farben, Animationen, Heimat-Bezug, Sondermerkmale. |
| 5.6 | `character-tiko.md` | [geschrieben] | Tiko (Vogel, Dschungeltempel): Persönlichkeit, Silhouette, Farben, Animationen, Heimat-Bezug, Sondermerkmale. |
| 5.7 | `character-bolt.md` | [geschrieben] | Bolt (Roboter, Mechanik-Stadt): Persönlichkeit, Silhouette, Farben, Animationen, Heimat-Bezug, Sondermerkmale. |
| 5.8 | `character-bloom.md` | [geschrieben] | Bloom (Kaktus, Dschungeltempel): Persönlichkeit, Silhouette, Farben, Animationen, Heimat-Bezug, Sondermerkmale. |
| 5.9 | `character-momo.md` | [geschrieben] | Momo (Waschbär, Frostgipfel): Persönlichkeit, Silhouette, Farben, Animationen, Heimat-Bezug, Sondermerkmale. |

#### Teil VI — World (8 Kapitel)

| # | Datei | Status | Kurzbeschreibung |
|---|-------|--------|------------------|
| 6.1 | `world-overview.md` | [geplant] | Welt-Übersicht: Aethonia als schwebender Kontinent, Inseln-Konzept, Insel-Auswahl im Menü, Verhältnis von Board-Layout und Insel-Identität. |
| 6.2 | `world-sonnenstrand.md` | [geplant] | Sonnenstrand (Urlaub & Wasser): Themen-, Farb- und Feldprofil, Board-Layout-Konzept, Atmosphäre. |
| 6.3 | `world-zuckerwald.md` | [geplant] | Zuckerwald (Süßigkeiten): Themen-, Farb- und Feldprofil, Board-Layout-Konzept, Atmosphäre. |
| 6.4 | `world-wolkenwerk.md` | [geplant] | Wolkenwerk (Schwebende Himmel): Themen-, Farb- und Feldprofil, Board-Layout-Konzept, Atmosphäre. |
| 6.5 | `world-frostgipfel.md` | [geplant] | Frostgipfel (Eis & Schnee): Themen-, Farb- und Feldprofil, Board-Layout-Konzept, Atmosphäre. |
| 6.6 | `world-dschungeltempel.md` | [geplant] | Dschungeltempel (Ruinen): Themen-, Farb- und Feldprofil, Board-Layout-Konzept, Atmosphäre. |
| 6.7 | `world-mechanik-stadt.md` | [geplant] | Mechanik-Stadt (Spielzeug-Technik): Themen-, Farb- und Feldprofil, Board-Layout-Konzept, Atmosphäre. |
| 6.8 | `world-sternenzitadelle.md` | [geplant] | Sternenzitadelle (Finale): Final-Insel, Themen-, Farb- und Feldprofil, Board-Layout-Konzept, Verhältnis zu ArenaStar. |

#### Teil VII — UI/UX (7 Kapitel)

| # | Datei | Status | Kurzbeschreibung |
|---|-------|--------|------------------|
| 7.1 | `ui-overview.md` | [geplant] | UI-Gesamtsystem: Screens-Fluss, Design-Tokens (Farben, Typografie, Abstände), Konsistenz-Regeln, Controller- und Maus-Navigation. |
| 7.2 | `ui-mainmenu.md` | [geplant] | Hauptmenü: Spiel starten, Lobby, Optionen, Charakter-Auswahl-Einstieg, ArenaStar-Präsenz, Rebranding-Vorgaben. |
| 7.3 | `ui-hud.md` | [geplant] | HUD im Board-Spiel: Spielerleiste (Münzen, Sterne, Items, aktiver Spieler), Würfelanzeige, Rundenanzeige, Schritt-Zähler. |
| 7.4 | `ui-board.md` | [geplant] | Board-UI: Feld-Beschriftungen, Pfadwahl-Pfeile, Stern-Statue-Anzeige, Kamerafokus, Split-Screen-Verhalten bei 8 Spielern. |
| 7.5 | `ui-shop.md` | [geplant] | Shop-UI: Sternen-Shop und Item-Shop, Preise, Kauf-Bestätigung, Inventar-Anzeige, AI-Kauf-Verhalten. |
| 7.6 | `ui-character-select.md` | [geplant] | Charakter-Auswahl: 8 Arenians, Vorschau, Farben, lokale Mehrspieler-Auswahl, Namensvergabe. |
| 7.7 | `ui-accessibility.md` | [geplant] | Zugänglichkeit: Kontrast, Schriftgrößen, Farbblindheit (Silhouetten statt Farben allein), Remapping, Einhand-Steuerung, reduzierte Bewegung. |

#### Teil VIII — Audio (4 Kapitel)

| # | Datei | Status | Kurzbeschreibung |
|---|-------|--------|------------------|
| 8.1 | `audio-overview.md` | [geplant] | Audio-Gesamtsystem: Bus-Struktur (Musik, SFX, Voice, UI), Lautstärke-Einstellungen, Audio-Branding im Cartoon-Stil. |
| 8.2 | `audio-music.md` | [geplant] | Musik: Insel-Themen je Board, Titel-/Menü-Musik, Minispiel-Musik, dynamische Übergänge (Runden-Höhepunkte). |
| 8.3 | `audio-sfx.md` | [geplant] | Sound-Effekte: Würfel, Bewegungsschritte, Münzen, Stern-Kauf, Item-Nutzung, Minispiel-Events, UI-Klicks, Feedback-Pflicht je Interaktion. |
| 8.4 | `audio-voice.md` | [geplant] | Sprachausgabe: ArenaStar-Moderation, Regelerklärungen, Sieg-/Niederlagen-Sprüche, Umfang, Lokalisierungs-Strategie. |

#### Teil IX — Narrative (3 Kapitel)

| # | Datei | Status | Kurzbeschreibung |
|---|-------|--------|------------------|
| 9.1 | `narrative-overview.md` | [geplant] | Narrative Gesamtstrategie: leichte Rahmenhandlung, Arena-Fantasie, Tone of Voice, Ludonarrative Harmonie mit dem Spielprinzip. |
| 9.2 | `narrative-arena-star.md` | [geplant] | ArenaStar als Maskottchen und Moderator: Persönlichkeit, Dialogstil, Moderations-Rolle, Belohnungs-Inszenierung, Voice-Vertrag. |
| 9.3 | `narrative-flavor.md` | [geplant] | Flavor-Texte: Feld- und Ereignis-Texte, Item-Beschreibungen, Charakter-Sprüche, Insel-Einleitungstexte, Tonfall- und Umfangskatalog. |

#### Teil X — Technical (5 Kapitel)

| # | Datei | Status | Kurzbeschreibung |
|---|-------|--------|------------------|
| 10.1 | `technical-architecture.md` | [geplant] | Technische Gesamtarchitektur: Node-Baum, Scene-Struktur, Client-Server-Aufteilung, Datenfluss, Schnittstellen zwischen den Systemen. |
| 10.2 | `technical-multiplayer.md` | [geplant] | Multiplayer-Design: ENet-Architektur, Server-Autorität, RPC-Verträge, 8-Spieler-Skalierung, Lobby-Synchronisation, Fehlerbehandlung. |
| 10.3 | `technical-fork-strategy.md` | [geplant] | Fork-Strategie: was aus Super Tux Party übernommen, modifiziert oder entfernt wird; Plugin-Format; Rebranding-Migration; IP-Bereinigung. |
| 10.4 | `technical-data-structures.md` | [geplant] | Datenstrukturen: Spielerzustand (Münzen, Sterne, Items, Modifikatoren), Board-Serialisierung, Item-Serialisierung, Savegame-Format, Minigame-Zustand. |
| 10.5 | `technical-performance.md` | [geplant] | Performance-Budgets: Ziel-Framerate, Draw Calls, Speicher, Ladezeiten, 8-Spieler-Split-Screen, Partikeleffekte im Cartoon-Look. |

#### Teil XI — Master-Index (1 Kapitel)

| # | Datei | Status | Kurzbeschreibung |
|---|-------|--------|------------------|
| 11.1 | `README.md` | [geplant] | Link-Master mit allen Kapiteln als klickbare Verzeichnisstruktur; der schnellste Einstieg für neue Teammitglieder und die Zielseite für Verlinkung aus dem Repository. |

### 3.4 Querverweis-Regeln

1. Jedes Kapitel verweist in **Sektion 6 (Dependencies)** bidirektional auf alle Systeme, mit denen es interagiert. Wenn Kapitel A von Kapitel B abhängt, muss auch Kapitel B auf A verweisen.
2. Alle internen Links verwenden relative Pfade zum Kapitel (z. B. `[Stern-Ökonomie](star-economy.md)`). Kein Kapitel verlinkt auf absolute Pfade oder Dateien außerhalb von `design/`.
3. Begriffe, die im Glossar definiert sind, werden beim ersten Vorkommen in einem Kapitel mit `[Begriff](glossary.md#begriff)` verlinkt.
4. Jede inhaltliche Abweichung vom Game-Konzept wird als solche markiert (siehe Regel 3.1.2) und im Index in einer separaten Zeile unterhalb der betroffenen Kapitel notiert.

### 3.5 Aktualisierungs- und Review-Prozess

1. **Neues Kapitel:** Datei nach Namenskonvention anlegen, alle 8 Sektionen ausfüllen, Status `[in Arbeit]` setzen, Zeile im Index ergänzen.
2. **Kapitel fertig:** Status auf `[geschrieben]` setzen, Datum im Metadaten-Block aktualisieren.
3. **Review:** Jedes `[geschrieben]`-Kapitel durchläuft `/design-review`; der Review-Befund wird in `design/gdd/reviews/[kapitelname]-review-log.md` protokolliert. Der Status des Kapitels im Index wird um den Review-Status ergänzt (Approved / Needs Revision).
4. **Änderungen:** Jede inhaltliche Änderung an einem geschriebenen Kapitel erfordert eine neue Review-Eintragung und eine Aktualisierung von `Stand`.

## 4. Formulas

Die folgenden Formeln machen die Struktur der Bible prüfbar. Variablen sind als Größen definiert, nicht als Code.

### 4.1 Kapitel-Gesamtzahl

Gesamtzahl der Kapitel: `T = Σ t_p` für alle Teile `p`, wobei `t_p` die Kapitelzahl des Teils `p` ist.

- Teil 0: 4; Teil I: 6; Teil II: 8; Teil III: 6; Teil IV: 4; Teil V: 9; Teil VI: 8; Teil VII: 7; Teil VIII: 4; Teil IX: 3; Teil X: 5; Teil XI: 1.
- Summe: `4+6+8+6+4+9+8+7+4+3+5+1 = 65`.
- Erwartungswerte: `T` muss ganzzahlig gleich 65 sein. Abweichungen sind nur nach dokumentierter Freigabe gültig.

### 4.2 Schreibabdeckung

`C = G / T × 100`, wobei:
- `G` = Anzahl Kapitel mit Status `[geschrieben]`,
- `T` = Gesamtzahl der Kapitel (65).

- Zielwerte: Prototyp-Meilenstein `C ≥ 40 %`, Alpha `C ≥ 80 %`, Beta `C = 100 %`.
- Beispiel: Sind alle 4 Meta-Kapitel und 11 weitere Kapitel geschrieben, gilt `G = 15`, `C = 15/65 × 100 ≈ 23 %`.

### 4.3 Sektions-Vollständigkeit

`S = s_i / 8 × 100` für jedes Kapitel `i`, wobei `s_i` die Anzahl der vorhandenen, nicht leeren Pflicht-Sektionen ist.

- Akzeptanzregel: Ein Kapitel gilt nur dann als `[geschrieben]`, wenn `S = 100` für dieses Kapitel gilt. `S < 100` bedeutet Status `[in Arbeit]`.

### 4.4 Verweis-Integrität

`R = (V_auflösbar + V_bidirektional) / V_gesamt`, wobei:
- `V_gesamt` = Anzahl aller Querverweise in allen Kapiteln,
- `V_auflösbar` = Anzahl der Verweise, deren Zielkapitel existiert,
- `V_bidirektional` = Anzahl der Verweise, deren Zielkapitel einen Rückverweis enthält.

- Akzeptanzregel: `R = 1,0` ist Pflicht vor der Alpha-Freigabe. Jeder nicht auflösbare Verweis ist ein Blocker.

### 4.5 Review-Dichte

`D = K_reviewed / T × 100`, wobei `K_reviewed` die Anzahl der Kapitel mit mindestens einem Review-Eintrag in `design/gdd/reviews/` ist.

- Ziel: Vor der Alpha-Freigabe muss für jedes `[geschrieben]`-Kapitel `D_relevant = K_reviewed / G = 1,0` gelten.

## 5. Edge Cases

1. **Kapitel fehlt im Index:** Wenn ein Kapitel geschrieben, aber nicht im Index eingetragen ist, gilt es nicht als Teil der Bible. Der Index ist die einzige maßgebliche Zählung. Ein fehlender Eintrag ist ein Blocker für die jeweilige Alpha-Freigabe.
2. **Kapitel im Index, aber Datei fehlt:** Der Index-Status wird auf `[geplant]` zurückgesetzt; die Differenz wird als `C`-Verlust in 4.2 sichtbar. Ein `[geschrieben]`-Kapitel ohne Datei ist ein Widerspruch und muss sofort korrigiert werden.
3. **Umbenennung eines Kapitels:** Beim Umbenennen muss der alte Dateiname alle Verweise aktualisieren. Der alte Name wird nicht weiterverwendet. Verwaiste Verweise (siehe 4.4) werden als Blocker behandelt.
4. **Neues System ohne eigenes Kapitel:** Wird im `systems-index.md` ein neues System eingetragen, das in der Bible kein Kapitel besitzt, so muss entweder ein neues Kapitel angelegt oder das System einem bestehenden Kapitel explizit zugeordnet werden. Andernfalls bleibt der System-Status im Index `Not Started`.
5. **Widerspruch zwischen Kapiteln:** Wenn zwei Kapitel dieselbe Größe unterschiedlich definieren (z. B. Sternpreis), gilt: das spezifischere Kapitel schlägt das allgemeinere (Feld-Kapitel schlägt Board-Kapitel, Board-Kapitel schlägt Core-Loop-Kapitel). Der Widerspruch wird im Index unter beiden Kapiteln vermerkt und in einem Review-Log aufgearbeitet.
6. **Umbenennungen aus Super Tux Party (Legacy):** Alle Legacy-Begriffe (Cookie, Cake, Sara, Nolok, GNU, BLUE/RED/GREEN-Felder) sind im `glossary.md` als veraltet markiert. Jede Verwendung eines Legacy-Begriffs in einem neuen Kapitel gilt als Rebranding-Fehler und als Review-Blocker.
7. **Kapitel mit leerer Sektion:** Eine Pflicht-Sektion darf nicht fehlen, darf aber bei nachweislich nicht anwendbaren Inhalten (z. B. "Formulas" in einem reinen Charakter-Lore-Kapitel) die explizite Angabe "Nicht anwendbar — keine Formeln definiert" enthalten. Eine komplett leere Sektion ohne Begründung setzt den Status auf `[in Arbeit]`.
8. **Gleichzeitige Bearbeitung:** Da mehrere Agenten Kapitel schreiben, kann der Index kurzzeitig inkonsistent sein. Vor jeder Freigabe wird der Index vollständig neu gezählt (Formeln 4.2–4.5); Zwischenstände sind zulässig, Freigabestände nie.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `bible-index.md` | Art | Verwendung |
|-------------------------------|-----|------------|
| `design/gdd/game-concept.md` | Quelle | Liefert die Kerndaten (Charaktere, Inseln, Ökonomie), die die Kapitelbeschreibungen referenzieren. |
| `design/gdd/session-1-analysis.md` | Quelle | Liefert die Lücken-Analyse (8-Spieler, Feldtypen, Boards), die die Priorisierung der Kapitel begründet. |
| `design/gdd/systems-index.md` | Peer | Liste der Systeme; jedes System muss einem Kapitel zuordenbar sein. |
| `design/gdd/glossary.md` | Peer | Terminologie; der Index referenziert Glossar-Begriffe. |
| `.claude/rules/design-docs.md` | Regelwerk | Definiert den 8-Sektionen-Standard, den der Index erzwingt. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| Alle 65 Bible-Kapitel | Jedes Kapitel muss im Index verzeichnet sein und die Konventionen aus Sektion 3 einhalten. |
| `README.md` | Muss dieselbe Kapitelliste als Link-Master abbilden; der Index ist die Referenzquelle für den README. |
| `design/gdd/reviews/` | Review-Logs referenzieren Kapitel per Dateiname; der Index definiert die gültigen Dateinamen. |
| CI / Hooks (`pre-commit-design-check`) | Kann den Index als Quelle für Dateinamen- und Sektions-Checks verwenden. |

### 6.3 Bidirektionalität

Die Verpflichtung ist wechselseitig: Jedes neue Kapitel muss sich im Index wiederfinden (3.5), und der Index muss aktualisiert werden, wenn ein Kapitel sich ändert. Diese Schleife ist explizit gewollt — der Index ist kein einmalig erzeugtes Artefakt, sondern der lebende Katalog der Bible.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Status eines Kapitels | Gate | `[geplant]`, `[in Arbeit]`, `[geschrieben]` | `[geplant]` | Steuert, ob ein Kapitel für Reviews und Freigaben zählt. |
| Review-Status | Gate | `None`, `In Review`, `Approved`, `Needs Revision` | `None` | Steuert die Freigabe-Reife eines Kapitels. |
| Kapitel-Gesamtzahl `T` | Kurve | 65, nur nach Freigabe änderbar | 65 | Bestimmt alle Abdeckungsformeln (4.2, 4.5). |
| Alpha-Schwelle `C ≥ 80 %` | Kurve | 60–100 % | 80 % | Definiert, wann die Bible für Alpha als vollständig gilt. |
| Verweis-Integrität `R` | Kurve | 0,90–1,00 | 1,00 | Schwelle, ab der verwaiste Links toleriert werden (Standard: keine). |
| Datumsformat in Metadaten | Feel | ISO `YYYY-MM-DD` | ISO | Sichert maschinelle Sortierbarkeit der Kapitel. |

Alle Knobs sind rein dokumentarisch; eine Änderung erfordert Konsistenz mit `glossary.md` und `systems-index.md`, da beide auf dieselben Status- und Namenskonventionen verweisen.

## 8. Acceptance Criteria

Ein QA-Tester (oder ein CI-Hook) kann die folgenden Prüfungen automatisiert oder manuell ausführen:

1. **Vollständigkeit der Liste:** Die Sektion 3.3 enthält exakt 65 Kapitelzeilen mit eindeutigen Dateinamen. Bei Zählung aller Teile (Formel 4.1) ergibt sich `T = 65`. PASS/FAIL.
2. **Datei-Existenz:** Für jedes Kapitel mit Status `[geschrieben]` existiert die Datei unter `design/gdd/[dateiname]`. PASS/FAIL.
3. **Sektions-Standard:** Jede als `[geschrieben]` markierte Datei enthält alle 8 Pflicht-Überschriften in fester Reihenfolge und keine leere Sektion ohne Begründung. PASS/FAIL.
4. **Namenskonvention:** Alle Dateinamen erfüllen das kebab-case-Schema aus 3.2 und enthalten keine Umlaute oder Leerzeichen. PASS/FAIL.
5. **Verweis-Auflösung:** Alle internen Links in allen Kapiteln zeigen auf existierende Dateien in `design/gdd/`; `R = 1,0`. PASS/FAIL.
6. **Bidirektionalität:** Für jede Dependencies-Angabe in einem Kapitel existiert die spiegelbildliche Angabe im referenzierten Kapitel (Stichprobenprüfung über mindestens 5 Kapitel pro Review). PASS/FAIL.
7. **Rebranding-Kontrolle:** In keinem `[geschrieben]`-Kapitel treten die Legacy-Begriffe Cookie, Cake, Sara, Nolok oder GNU als aktive Fachbegriffe auf (Ausnahme: explizite Erwähnung in `glossary.md` und `technical-fork-strategy.md`). PASS/FAIL.
8. **Abdeckungs-Tracker:** Die Fortschrittswerte aus 4.2–4.5 sind im Index korrekt berechnet und datiert. PASS/FAIL.
9. **Erlebbar (Experiential):** Ein neues Teammitglied findet nachweislich (gemessen per Protokoll) in unter 2 Minuten das Kapitel, das eine ihm gestellte Design-Frage beantwortet. PASS/FAIL.
