# Party Arena — Game Bible

> **Stand:** 2026-08-11
> **Status:** Komplett — alle 65 Kapitel geschrieben
> **Quelle:** design/gdd/bible-index.md

---

## Willkommen zur Party Arena Game Bible

Dies ist der **Master-Index** der vollständigen Design-Dokumentation von Party Arena. Die Game Bible umfasst **65 Kapitel in 11 Teilen** — von den Meta-Grundlagen über alle Gameplay-Systeme bis zur technischen Architektur. Jedes Kapitel ist eine eigenständige Datei im Verzeichnis `design/gdd/` und folgt dem verbindlichen **8-Sektionen-Standard**: Overview, Player Fantasy, Detailed Rules, Formulas, Edge Cases, Dependencies, Tuning Knobs, Acceptance Criteria.

**Einstiegspunkte:**
- Neu im Projekt? → [Bible-Index](bible-index.md) für Kapitelliste, Konventionen und Fortschritt
- Design-Frage? → [System-Index](systems-index.md) für die technische Systemzerlegung
- Begriff gesucht? → [Glossar](glossary.md) für alle Fachbegriffe
- Spielidee verstehen? → [Game Concept](game-concept.md) in 5 Minuten

---

## Teil 0 — Meta & Vision

Die Grundpfeiler: Was ist Party Arena, woran glauben wir, wie sprechen wir darüber?

| # | Datei | Beschreibung |
|---|-------|-------------|
| 0.1 | [Bible-Index](bible-index.md) | Master-Index der gesamten Game Bible: Kapitelliste, Konventionen, Fortschritts-Tracker. |
| 0.2 | [Vision Pillars](vision-pillars.md) | Die 4 Design-Pfeiler: Sofort verständlich, Überzeichnet, Interaktiv wirkend, Wiedererkennbar. |
| 0.3 | [Glossar](glossary.md) | Vollständiges Glossar aller Fachbegriffe inkl. Legacy-Umbenennungen. |
| 0.4 | [System-Index](systems-index.md) | Komplette Systemzerlegung: Verantwortlichkeiten, Abhängigkeiten, Godot-Zuordnung. |

---

## Teil I — Core Game

Der Kern-Loop und die Fundamental-Ökonomie: Würfeln, Ziehen, Sterne kaufen, gewinnen.

| # | Datei | Beschreibung |
|---|-------|-------------|
| 1.1 | [Core Loop](core-loop.md) | Der verschachtelte Kern-Loop: Mikro (Würfeln–Ziehen–Feld), Meso (Runde–Minispiel–Stern), Makro (8–10 Runden). |
| 1.2 | [Star Economy](star-economy.md) | Die Stern-Ökonomie: Sternpreis (20 Münzen), wandernde Sternen-Statue, Kaufregeln. |
| 1.3 | [Dice & Movement](dice-movement.md) | Würfel- und Bewegungssystem: W1–6, Modifikatoren, Pfadwahl an Abzweigungen. |
| 1.4 | [Victory Conditions](victory-conditions.md) | Siegbedingungen: meiste Sterne, Bonus-Sterne, Gleichstands-Regeln. |
| 1.5 | [Catch-Up](catch-up.md) | Catch-Up-Mechaniken: Ereignisse mit Aufhol-Effekten, Verlierer-Boost, Bonus-Sterne. |
| 1.6 | [Coin Economy](coin-economy.md) | Die Münz-Ökonomie: Quellen, Senken, Fluss-Bilanz über 8–10 Runden. |

---

## Teil II — Board & Fields

Das Spielfeld: 40 Felder, 7 Feldtypen, Ereignisse, Shops, Landmarken.

| # | Datei | Beschreibung |
|---|-------|-------------|
| 2.1 | [Board Architecture](board-architecture.md) | Board-Architektur: 40-Felder-Pfad, Feld-Verkettung, Aufbau-Regeln. |
| 2.2 | [Field: Start](field-start.md) | Startfeld: Positionierung, Start-Versatz, Rückkehr aufs Startfeld. |
| 2.3 | [Field: Star Shop](field-star-shop.md) | Sternen-Shop: Stern-Kauf (20 Münzen), Statuen-Wanderung. |
| 2.4 | [Field: Item Shop](field-item-shop.md) | Item-Shop: Sortiment, Einkauf, Inventar-Limit, Ersetzungs-Regel. |
| 2.5 | [Field: Event](field-event.md) | Ereignis-Feld: Zufalls-Ereignisse, positive/negative/neutrale Effekte. |
| 2.6 | [Field: Luck](field-luck.md) | Glück/Pech-Feld: Münz-Gewinn/-Verlust, Wahrscheinlichkeiten. |
| 2.7 | [Field: Coin Bonus](field-coin-bonus.md) | Münz-Bonus-Feld: fester Bonus, Mehrfachbesuch, Interaktion mit Items. |
| 2.8 | [Field: Minigame](field-minigame.md) | Mini-Spiel-Feld: Auslösung nach allen Zügen, Team-Bildung. |

---

## Teil III — Items

Die 5 Items: Würfel-Manipulation, Teleport, Schutz, Münz-Boost, Diebstahl.

| # | Datei | Beschreibung |
|---|-------|-------------|
| 3.1 | [Item System](item-system.md) | Item-System: Definition, Typen, Inventar, Nutzungs-Zeitpunkt. |
| 3.2 | [Item: Lucky Dice](item-luckydice.md) | Glücks-Würfel: W1–10, Kosten 5, strategische Verwendung. |
| 3.3 | [Item: Teleporter](item-teleporter.md) | Stern-Teleporter: sofort zur Sternen-Statue, Kosten 8. |
| 3.4 | [Item: Shield](item-shield.md) | Schutzschild: blockt nächsten negativen Effekt, Kosten 6. |
| 3.5 | [Item: Coin Magnet](item-coinmagnet.md) | Münz-Magnet: doppelte Münz-Erträge, Kosten 4, Stapel-Regel. |
| 3.6 | [Item: Thief Glove](item-thiefglove.md) | Dieb-Handschuh: stiehlt Münzen vom Gegner, Kosten 10. |

---

## Teil IV — Minigames

30-Sekunden-Minispiele: Architektur, Kategorien, Belohnungen, Design-Template.

| # | Datei | Beschreibung |
|---|-------|-------------|
| 4.1 | [Minigame Architecture](minigame-architecture.md) | Minigame-Architektur: Plugin-Vertrag, Ladevorgang, Ergebnisübermittlung. |
| 4.2 | [Minigame Categories](minigame-categories.md) | 5 Kategorien: Geschicklichkeit, Reaktion, Puzzle, Rechnen, Kooperation. |
| 4.3 | [Minigame Rewards](minigame-rewards.md) | Belohnungs-System: Münzen nach Platzierung, Team-Boni, Auszahlungs-Tabellen. |
| 4.4 | [Minigame Template](minigame-template.md) | Design-Template: Pflicht-Sektionen, 30 s Dauer, Input-Mapping, Fairness-Checkliste. |

---

## Teil V — Characters

Die 8 Arenians: Stein-Golem, Axolotl, Flughörnchen, Panda, Vogel, Roboter, Kaktus, Waschbär.

| # | Datei | Beschreibung |
|---|-------|-------------|
| 5.1 | [Characters Overview](characters-overview.md) | Charakter-System: Auswahlprozess, Animationsvertrag, Balance-Philosophie. |
| 5.2 | [Brix](character-brix.md) | Brix (Stein-Golem, Mechanik-Stadt): mutig, tollpatschig, Orange. |
| 5.3 | [Nixie](character-nixie.md) | Nixie (Axolotl, Sonnenstrand): neugierig, wasseraffin, Türkis. |
| 5.4 | [Pip](character-pip.md) | Pip (Flughörnchen, Wolkenwerk): schnell, frech, Gelb. |
| 5.5 | [Koko](character-koko.md) | Koko (Panda, Zuckerwald): freundlich, stark, Rosa. |
| 5.6 | [Tiko](character-tiko.md) | Tiko (Vogel, Dschungeltempel): chaotisch, lustig, Grün. |
| 5.7 | [Bolt](character-bolt.md) | Bolt (Roboter, Mechanik-Stadt): logisch, präzise, Blau. |
| 5.8 | [Bloom](character-bloom.md) | Bloom (Kaktus, Dschungeltempel): ruhig, humorvoll, Lila. |
| 5.9 | [Momo](character-momo.md) | Momo (Waschbär, Frostgipfel): clever, trickreich, Pink. |

---

## Teil VI — World

Die 7 Inseln von Aethonia plus Sternenzitadelle: jedes Board mit 40 Feldern, eigenem Thema, eigener Musik.

**Übersicht:** [World Overview](world-overview.md) — Aethonia als schwebender Kontinent, Inselfreischaltung, Board-Architektur-Rahmen.

| # | Datei | Insel | Schwierigkeit | Thema | Musik-Stil |
|---|-------|-------|---------------|-------|------------|
| 6.1 | [World Overview](world-overview.md) | — | — | Rahmenregeln für alle Inseln | — |
| 6.2 | [Sonnenstrand](world-sonnenstrand.md) | ★☆☆☆☆ | Urlaub & Wasser | Steel Drums, Ukulele |
| 6.3 | [Zuckerwald](world-zuckerwald.md) | ★★☆☆☆ | Süßigkeiten | Glockenspiel, Fagott |
| 6.4 | [Wolkenwerk](world-wolkenwerk.md) | ★★★☆☆ | Schwebende Himmel | Harfe, Flöte |
| 6.5 | [Frostgipfel](world-frostgipfel.md) | ★★★☆☆ | Eis & Schnee | Celesta, Tremolo-Strings |
| 6.6 | [Dschungeltempel](world-dschungeltempel.md) | ★★★★☆ | Ruinen & Abenteuer | Marimba, Bongos |
| 6.7 | [Mechanik-Stadt](world-mechanik-stadt.md) | ★★★★☆ | Spielzeug-Technik | Marimba/Xylophon, Tuba |
| 6.8 | [Sternenzitadelle](world-sternenzitadelle.md) | ★★★★★ | Finale & Endgame | Orchester, Chor |

**Schwierigkeits-Rampe:**
1. Sonnenstrand: Einsteiger — keine Sonderregeln, milde Effekte, Preisstufe 0
2. Zuckerwald: Anfänger — erste Sonderregeln (Floß-Fahrt), Preisstufe 0
3. Wolkenwerk: Mittel — Windkanal-Zufall, Rutsche, Preisstufe 1
4. Frostgipfel: Mittel — verdeckte Eishöhlen-Felder, Eisglätte-Rutsch, Preisstufe 1
5. Dschungeltempel: Gehoben — Führenden-Fluch, Letzten-Goldrausch, Preisstufe 2
6. Mechanik-Stadt: Gehoben — Rohrpost-Teleport, Förderband-Fabrik, Preisstufe 2
7. Sternenzitadelle: Finale — Kosmische Drift, Geister-Felder, Bonus-Stern, Preisstufe 3

---

## Teil VII — UI/UX

Menüs, HUD, Board-UI, Charakterauswahl, Zugänglichkeit.

| # | Datei | Beschreibung |
|---|-------|-------------|
| 7.1 | [UI Overview](ui-overview.md) | UI-Gesamtsystem: Screens-Fluss, Design-Tokens, Controller-Navigation. |
| 7.2 | [Main Menu](ui-mainmenu.md) | Hauptmenü: Spiel starten, Lobby, Optionen, ArenaStar-Präsenz. |
| 7.3 | [HUD](ui-hud.md) | HUD im Board-Spiel: Spielerleiste, Würfel, Runden, Schritte. |
| 7.4 | [Board UI](ui-board.md) | Board-UI: Feld-Beschriftungen, Pfadwahl-Pfeile, Stern-Statue, Kamera. |
| 7.5 | [Shop UI](ui-shop.md) | Shop-UI: Sternen-Shop und Item-Shop, Preise, Kauf-Bestätigung. |
| 7.6 | [Character Select](ui-character-select.md) | Charakter-Auswahl: 8 Arenians, Vorschau, Farben, Mehrspieler. |
| 7.7 | [Accessibility](ui-accessibility.md) | Zugänglichkeit: Kontrast, Farbblindheit, Remapping, reduzierte Bewegung. |

---

## Teil VIII — Audio

Musik, Sound-Effekte, Sprachausgabe, dynamische Übergänge.

| # | Datei | Beschreibung |
|---|-------|-------------|
| 8.1 | [Audio Overview](audio-overview.md) | Audio-Gesamtsystem: Bus-Struktur, Lautstärke, Audio-Branding. |
| 8.2 | [Music](audio-music.md) | Musik: 7 Insel-Themen, Menü-Musik, Minispiel-Musik, dynamische Übergänge. |
| 8.3 | [Sound Effects](audio-sfx.md) | SFX: Würfel, Bewegung, Münzen, Items, Minispiele, UI-Klicks. |
| 8.4 | [Voice](audio-voice.md) | Sprachausgabe: ArenaStar-Moderation, Regel-Erklärungen, Sieg-Sprüche. |

---

## Teil IX — Narrative

Rahmenhandlung, ArenaStar als Maskottchen, Flavor-Texte.

| # | Datei | Beschreibung |
|---|-------|-------------|
| 9.1 | [Narrative Overview](narrative-overview.md) | Narrative Strategie: leichte Rahmenhandlung, Tone of Voice. |
| 9.2 | [ArenaStar](narrative-arena-star.md) | ArenaStar: Persönlichkeit, Dialogstil, Moderations-Rolle. |
| 9.3 | [Flavor Texts](narrative-flavor.md) | Flavor-Texte: Feld-Texte, Item-Beschreibungen, Sprüche. |

---

## Teil X — Technical

Architektur, Multiplayer, Fork-Strategie, Datenstrukturen, Performance.

| # | Datei | Beschreibung |
|---|-------|-------------|
| 10.1 | [Technical Architecture](technical-architecture.md) | Gesamtarchitektur: Node-Baum, Scene-Struktur, Datenfluss. |
| 10.2 | [Multiplayer](technical-multiplayer.md) | Multiplayer: ENet, Server-Autorität, RPCs, 8-Spieler-Skalierung. |
| 10.3 | [Fork Strategy](technical-fork-strategy.md) | Fork-Strategie: Übernahme, Modifikation, Entfernung aus Super Tux Party. |
| 10.4 | [Data Structures](technical-data-structures.md) | Datenstrukturen: Spielerzustand, Board, Items, Savegame-Format. |
| 10.5 | [Performance](technical-performance.md) | Performance-Budgets: FPS, Draw Calls, Speicher, Ladezeiten. |

---

## Teil XI — Master-Index

Diese Datei.

| # | Datei | Beschreibung |
|---|-------|-------------|
| 11.1 | [README.md](README.md) | Link-Master mit allen 65 Kapiteln als klickbare Verzeichnisstruktur. |

---

## Status-Übersicht

| Teil | Kapitel | Geschrieben | Geplant | In Arbeit |
|------|--------|------------|---------|-----------|
| 0 — Meta & Vision | 4 | 4 | 0 | 0 |
| I — Core Game | 6 | 6 | 0 | 0 |
| II — Board & Fields | 8 | 8 | 0 | 0 |
| III — Items | 6 | 6 | 0 | 0 |
| IV — Minigames | 4 | 4 | 0 | 0 |
| V — Characters | 9 | 9 | 0 | 0 |
| VI — World | 8 | 8 | 0 | 0 |
| VII — UI/UX | 7 | 7 | 0 | 0 |
| VIII — Audio | 4 | 4 | 0 | 0 |
| IX — Narrative | 3 | 3 | 0 | 0 |
| X — Technical | 5 | 5 | 0 | 0 |
| XI — Master-Index | 1 | 1 | 0 | 0 |
| **Gesamt** | **65** | **65** | **0** | **0** |

---

## Wie benutze ich die Game Bible?

1. **Orientierung:** Starte mit dem [Game Concept](game-concept.md), um das Spiel in 5 Minuten zu verstehen.
2. **Tiefe:** Lies den [Bible-Index](bible-index.md) für die vollständige Kapitelliste mit Konventionen.
3. **Fachfrage:** Suche im [System-Index](systems-index.md) nach dem relevanten System und folge dem Link.
4. **Begriff:** Schlage unbekannte Begriffe im [Glossar](glossary.md) nach.
5. **Insel:** Vergleiche die [World-Übersicht](world-overview.md) und die einzelnen Insel-Kapitel.
6. **Review:** Jedes `[geschrieben]`-Kapitel durchläuft `/design-review`; Ergebnisse in `design/gdd/reviews/`.

## Design-Prinzipien (Kurzfassung)

1. **Sofort verständlich** — Ein neuer Spieler versteht das Spiel in ≤ 2 Minuten.
2. **Überzeichnet statt realistisch** — Cartoon, Toy-like, High Saturation.
3. **Interaktiv wirkend** — Kein Objekt ohne Reaktion auf Spieler-Input.
4. **Wiedererkennbar** — Jedes Element ist an Silhouette, Farbe und Sound eindeutig identifizierbar.

→ Details in [Vision Pillars](vision-pillars.md).

## ArenaStar

ArenaStar ist das Maskottchen und der Moderator von Party Arena — ein leuchtender Stern mit Krone. Er moderiert jede Partie, erklärt Regeln, kommentiert Ereignisse und krönt den Sieger. In der Sternenzitadelle (seiner Heimat) erscheint er als gigantisches Hologramm. Alle seine Sprüche sind in [Narrative: ArenaStar](narrative-arena-star.md) und [Audio: Voice](audio-voice.md) dokumentiert.

---

*Party Arena Game Bible — Version 1.0 — 65/65 Kapitel geschrieben*

🤖 Generated with [Claude Code](https://claude.com/claude-code)
Co-Authored-By: Claude <noreply@anthropic.com>
