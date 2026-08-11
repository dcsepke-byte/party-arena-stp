# Glossar — Party Arena Game Bible

> **Teil:** 0 — Meta & Vision
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/session-1-analysis.md

---

## 1. Overview

Dieses Glossar definiert die verbindliche Terminologie von Party Arena. Es umfasst alle Fachbegriffe des Spiels (Welt, Charaktere, Ökonomie, Felder, Items, Minispiele, UI, Audio, Technik) sowie die Design- und Theoriefachbegriffe, die in den Kapiteln der Game Bible verwendet werden. Zusätzlich enthält es die offizielle **Legacy-Umbenennungstabelle**, die alle Begriffe aus dem Super-Tux-Party-Fork (Cookies, Cakes, Sara, Nolok, GNU, etc.) auf die neuen Party-Arena-Begriffe abbildet und damit das Rebranding verbindlich macht. Jedes Kapitel der Bible ist verpflichtet, die Begriffe exakt in dieser Definition zu verwenden; Abweichungen sind als Rebranding-Fehler zu behandeln.

## 2. Player Fantasy

Das Glossar soll sich beim Lesen anfühlen wie ein verlässliches Nachschlagewerk, das nie zweideutig ist: Man findet einen Begriff, versteht sofort seine genaue Bedeutung, sieht ein konkretes Beispiel aus dem Spiel und erkennt verwandte Begriffe. Die Lese-Erfahrung ist die eines **gemeinsamen Vokabulars** — Designer, Artists, Programmierer und Tester sprechen dieselbe Sprache, und Missverständnisse durch uneinheitliche Begriffe (etwa "Feld" vs. "Space" vs. "Node") verschwinden. Für das Team erzeugt das Glossar **Sicherheit und Vertrauen**: Jeder kann einen Begriff nachschlagen, ohne jemanden fragen zu müssen, und die Legacy-Tabelle schafft Klarheit darüber, welche alten Super-Tux-Party-Begriffe im Projekt nicht mehr verwendet werden dürfen.

## 3. Detailed Rules

### 3.1 Verwendungsregeln

1. Die Begriffe dieses Glossars sind **verbindlich** für alle Kapitel der Bible, alle UI-Texte, alle Dialoge und alle Code-Bezeichner (in Übersetzungen ohne Code-Pflicht).
2. Bei mehreren möglichen Begriffen ist der **bevorzugte Begriff** fett markiert; Alternativen sind als "Synonyme" gelistet und werden als veraltet betrachtet, sofern nichts anderes angegeben ist.
3. Die Legacy-Tabelle (3.3) markiert STP-Begriffe als `[entfernt]` oder `[umbenannt]`. `[umbenannt]`-Begriffe dürfen im Projekt **nicht mehr aktiv** verwendet werden; `[entfernt]`-Begriffe bezeichnen Systeme, die ersatzlos gestrichen wurden.
4. Jede Erweiterung des Glossars (neuer Begriff) wird alphabetisch einsortiert und mit Datum im Metadaten-Block des Dokuments vermerkt.

### 3.2 Alphabetische Begriffssammlung

#### A

**Aethonia** — Die Spielwelt: ein magischer Kontinent aus schwebenden Inseln, dessen Bewohner Wettkämpfe über alles lieben. Aethonia umfasst 7 schwebende Inseln plus die Sternenzitadelle (7+1). *Beispiel:* Jede Partie spielt auf einer der Inseln von Aethonia. *Verwandt:* [[Insel]], [[Sternenzitadelle]].

**AI-Spieler** (Synonym: Computergegner, Bot) — Ein Spielerplatz, der nicht von einem Menschen, sondern von der KI gesteuert wird. AI-Spieler würfeln, kaufen, wählen Pfade und spielen Minispiele automatisch; ihre Schwierigkeit ist einstellbar (Leicht/Normal/Schwer). *Verwandt:* [[Lobby]], [[Schwierigkeit]].

**ArenaStar** — Das Maskottchen und der Moderator von Party Arena: ein leuchtender, goldener Stern mit Krone. Er erklärt Regeln, moderiert Minispiele, kündigt Stern-Phasen an, verteilt Belohnungen und kommentiert Spielereignisse. Er ersetzt "Sara" aus Super Tux Party vollständig. *Verwandt:* [[Sara]], [[Moderator]], [[Stern]].

**Arenian** (Singular/Plural identisch) — Sammelbezeichnung für die 8 spielbaren Charaktere von Party Arena (Brix, Nixie, Pip, Koko, Tiko, Bolt, Bloom, Momo). Arenians sind die Bewohner Aethonias. *Verwandt:* [[Charakter]].

**Autonomie** — Design-Ziel aus der Selbstbestimmungstheorie (SDT): Spieler sollen echte, bedeutsame Wahlmöglichkeiten haben (z. B. Item kaufen oder sparen, Pfad wählen, Ereignis-Risiko eingehen). Fehlt Autonomie, fühlen sich Entscheidungen wie "falsche Wahlmöglichkeiten" an. *Verwandt:* [[Kompetenz]], [[Flow]].

**Aesthetics** (MDA) — Eine der drei Ebenen des MDA-Modells: die *gewünschten Emotionen* des Spielers (Sensation, Fantasy, Challenge, Fellowship, Discovery, Expression, Submission). Design beginnt bei der Ziel-Aesthetic und arbeitet rückwärts zu Dynamik und Mechanik. *Verwandt:* [[MDA]], [[Dynamik]], [[Mechanik]].

#### B

**Bartle-Taxonomie** — Klassifikation von Spielertypen nach Richard Bartle (Achiever, Explorer, Socializer, Killer/Competitor). Wird in der Bible zur Zielgruppen-Validierung genutzt; Party Arena bedient primär Achiever (Sterne/Progression), Socializer (Party-Modus) und Explorer (Ereignisse/Boards). *Verwandt:* [[Quantic Foundry]].

**Board** — Siehe [[Insel]]. Der Begriff "Board" wird in technischen Kontexten verwendet (z. B. Board-Loader); im Spiel-Text bevorzugt: "Insel".

**Board-Loader** — Technisches System, das Insel-Dateien (Boards) aus dem Plugin-Verzeichnis lädt und in die Szene einfügt. Aus STP übernommen, für 7+1 Inseln erweitert. *Verwandt:* [[Plugin]], [[Insel]].

**Bonus-Stern** — Ein Stern, der erst **nach** der letzten Runde in der Siegerehrung vergeben wird. Er belohnt Leistungen, die nicht direkt mit der Stern-Ökonomie zusammenhängen (z. B. "meiste Münzen am Ende", "meiste gewonnene Minispiele", "meiste Feld-Besuche"). Bonus-Sterne sind das wichtigste Catch-Up- und Comeback-Instrument. *Verwandt:* [[Stern]], [[Catch-Up]], [[Sieg]].

**Bus (Audio)** — Technischer Audiokanal (Master, Musik, SFX, Voice, UI), über den Lautstärke und Effekte gesteuert werden. Jeder Sound ist einem Bus zugeordnet; die Bus-Struktur ist in `audio-overview.md` spezifiziert. *Verwandt:* [[Sound-Effekt]].

#### C

**Cake** — Legacy-Begriff aus Super Tux Party (Kuchen als Siegwährung). **Umbenannt** zu [[Stern]]. *Siehe auch:* [[Legacy-Umbenennungstabelle]].

**Catch-Up** — Sammelbegriff für alle Mechaniken, die einen zurückliegenden Spieler unterstützen, um Partien spannend zu halten: Ereignis-Felder mit Aufhol-Effekten, Verlierer-Boost (zusätzliche Münzen/Items für die letzten Plätze), Bonus-Sterne in der Endphase. *Verwandt:* [[Bonus-Stern]], [[Verlierer-Boost]].

**Charakter** — Einer der 8 spielbaren Arenians mit eigenem Modell, Silhouette, Signaturfarbe, Animationen und Persönlichkeit. Charaktere haben **keine** asymmetrischen Board-Vorteile (Fairness); Unterschiede sind rein äußerlich/persönlich. *Verwandt:* [[Arenian]], [[Signaturfarbe]].

**Client** — Instanz des Spiels, die mit einem Server verbunden ist. Auf Clients laufen Darstellung und Eingabe; die Spiellogik ist server-autoritativ. *Verwandt:* [[Server]], [[Host]].

**Controller** — Godot-Knotenklasse (`Controller`) im Board-Spiel, die den Spielfluss orchestriert (Zugreihenfolge, Würfeln, Bewegung, Lande-Effekte, Minispiel-Start). Aus STP übernommen und für Party Arena modifiziert. *Verwandt:* [[NodeBoard]], [[Spielablauf]].

**Cookie** — Legacy-Begriff aus Super Tux Party (Kekse als Sekundärwährung). **Umbenannt** zu [[Münze]].

**Core Loop** — Der grundlegende, sich wiederholende Spielzyklus. In Party Arena verschachtelt: Mikro-Loop (Würfeln → Ziehen → Feld-Effekt), Meso-Loop (alle Spielerzüge → Minispiel → Belohnung), Makro-Loop (8–10 Runden → Stern-Phase → Siegerehrung). *Verwandt:* [[Runde]], [[Minispiel]].

#### D

**Dynamik** (MDA) — Die mittlere Ebene des MDA-Modells: das *entstehende Spielerverhalten* und die Muster, die aus den Regeln entstehen (z. B. "Spieler sparen Münzen für den Stern" oder "Spieler zielen den Teleporter auf die Stern-Position"). *Verwandt:* [[MDA]], [[Aesthetics]], [[Mechanik]].

**Dieb-Handschuh** — Item: stiehlt einem gewählten Gegner eine festgelegte Menge Münzen. Kosten 10 Münzen. Einsetzbar vor dem Würfeln. *Verwandt:* [[Item]], [[Münze]].

**Dschungeltempel** — Eine der 7 Inseln von Aethonia (Thema: Ruinen). Farbwelt: Dschungelgrün, Gold, Braun. Heimat von Tiko und Bloom. *Verwandt:* [[Aethonia]], [[Insel]].

#### E

**Ereignis** — Ein zufällig ausgewählter Effekt aus der Ereignis-Kartei, der beim Landen auf einem [[Ereignis-Feld]] ausgelöst wird. Ereignisse können Münzen/Items geben oder nehmen, Positionen tauschen oder den Würfel beeinflussen. *Verwandt:* [[Ereignis-Kartei]].

**Ereignis-Feld** — Feldtyp auf dem Board, der ein [[Ereignis]] auslöst. Geplant 5–6 Ereignis-Felder pro 40er-Pfad. *Verwandt:* [[Feld-Typ]].

**Ereignis-Kartei** — Die gepflegte Sammlung aller Ereignisse, aus der das Ereignis-Feld zufällig zieht. Die Kartei wird in `field-event.md` spezifiziert (Wahrscheinlichkeiten, positive/negative Balance, Catch-Up-Gewichtung). *Verwandt:* [[Ereignis]], [[Catch-Up]].

#### F

**Feld** (Synonym: Space, Node; bevorzugt: **Feld**) — Eine einzelne Position auf dem Board-Pfad, auf der ein Spieler landen kann. Jedes Feld hat einen Typ, eine Position, sichtbare/unsichtbare Eigenschaft und Verbindungen zum nächsten Feld (next/prev). 40 Felder bilden den [[Hauptpfad]] einer Insel. *Verwandt:* [[Feld-Typ]], [[NodeBoard]].

**Feld-Typ** — Die Art eines Feldes, die seinen Effekt beim Landen bestimmt. Party-Arena-Feldtypen: Start, Sternen-Shop, Item-Shop, Ereignis, Glück/Pech, Münz-Bonus, Mini-Spiel. Sie ersetzen die STP-Typen BLUE/RED/GREEN/YELLOW/SHOP. *Verwandt:* [[Feld]], [[Startfeld]].

**Flow** — Design-Konzept nach Csikszentmihalyi: Der Zustand völligen Aufgehens in einer Tätigkeit, wenn Herausforderung und Können im Gleichgewicht sind. In Party Arena wird Flow durch eine leicht ansteigende Komplexität (Sawtooth) und kurze, klare Feedback-Schleifen angestrebt. *Verwandt:* [[Kompetenz]], [[Core Loop]].

**Fork** — Die Abspaltung des Open-Source-Codes von Super Tux Party als technische Basis von Party Arena. Der Fork übernimmt Architektur und Plugin-System, ersetzt IP (Charaktere, Maskottchen, Ökonomie-Namen) und erweitert den Umfang (8 Spieler, 7+1 Inseln). *Verwandt:* [[STP]], [[technical-fork-strategy]].

**FFA** (Synonym: Jeder-gegen-Jeden) — Minispiel-Modus, in dem alle Spieler gleichzeitig gegeneinander antreten und nach Platzierung belohnt werden. *Verwandt:* [[Minispiel]], [[Platzierung]].

**Frostgipfel** — Eine der 7 Inseln von Aethonia (Thema: Eis & Schnee). Farbwelt: Eisblau, Weiß, Violett. Heimat von Momo. *Verwandt:* [[Aethonia]], [[Insel]].

**Frustra-Balance** — Balancier-Methode, bei der ein scheinbar übermächtiges Element einen versteckten Gegenspieler besitzt (z. B. der Stern-Teleporter wirkt stark, kostet aber viele Münzen und verbraucht einen Zug). *Verwandt:* [[Item]].

#### G

**Geschicklichkeit** — Eine der 5 Minigame-Kategorien: Spiele, die motorisches Können und Präzision erfordern (z. B. Zielwerfen, Balancieren). *Verwandt:* [[Minigame-Kategorie]].

**Gini-Koeffizient** — Statistisches Maß für die Ungleichverteilung von Ressourcen. In der Münz-Ökonomie wird damit geprüft, ob die Münzverteilung über die Runden gesund bleibt (Ziel: keine dauerhafte Vermögens-Konzentration). *Verwandt:* [[Münz-Ökonomie]].

**Glück-Pech-Feld** (Synonym: Glück/Pech) — Feldtyp, der beim Landen Münzen gibt (Glück) oder nimmt (Pech). Geplant 3 Felder pro 40er-Pfad. *Verwandt:* [[Feld-Typ]], [[Münze]].

**Glücks-Würfel** — Item: Ersatz-Würfel mit Wurfbereich 1–10 statt 1–6. Kosten 5 Münzen. Erhöht die Kontrolle/Spannung, birgt aber das Risiko hoher Ergebnisse, die an Sternen-Shop oder Item-Shop vorbeiführen können. *Verwandt:* [[Item]], [[Würfel]].

#### H

**Hauptpfad** — Die 40 Felder umfassende Hauptroute einer Insel, auf der sich alle Spieler bewegen. Abzweigungen (kurze Alternativ-Pfade) sind möglich; der Hauptpfad ist die Grundstruktur jeder Insel. *Verwandt:* [[Feld]], [[Insel]].

**Host** — Der Spieler/Rechner, der zugleich Server und lokaler Client ist (typisch für lokale Partien). *Verwandt:* [[Server]], [[Client]].

**HUD** — Die permanente Anzeige während des Board-Spiels: Spielerleiste (Münzen, Sterne, Items, aktiver Spieler), Rundenanzeige, Würfelanzeige, Schritt-Zähler, Ereignis-Meldungen. Spezifikation in `ui-hud.md`. *Verwandt:* [[UI]].

#### I

**Insel** (Synonym: Board) — Ein einzelnes Spielbrett von Party Arena: ein 40-Felder-Pfad mit eigener Themenwelt, Farbidentität und Atmosphäre. Es gibt 7 reguläre Inseln plus die Sternenzitadelle (7+1). *Verwandt:* [[Aethonia]], [[Hauptpfad]].

**Item** — Ein Ausrüstungsgegenstand mit Spezialeffekt, der vor dem Würfeln eingesetzt werden kann. Items werden im Item-Shop gekauft, über Ereignisse gewonnen oder aus Minispiel-Belohnungen erhalten. Standard-Items: Glücks-Würfel, Stern-Teleporter, Schutzschild, Münz-Magnet, Dieb-Handschuh. *Verwandt:* [[Item-Shop]], [[Inventar]].

**Item-Shop** — Verkaufsstelle für [[Items]] auf dem Board. Auf jeder Insel gibt es 2 Item-Shop-Felder. *Verwandt:* [[Item-Shop-Feld]].

**Item-Shop-Feld** — Feldtyp, der einen Item-Shop-Besuch auslöst. *Verwandt:* [[Feld-Typ]], [[Item-Shop]].

**Interaktiv wirkend** — Einer der 4 Design-Pfeiler: Das Spiel reagiert auf jede Eingabe mit sofortigem, sichtbarem und/oder hörbarem Feedback (Latenz ≤ 0,5 s). Kein passives Zuschauen, keine toten Eingaben. *Verwandt:* [[Pillar]].

**Inventar** — Der Item-Vorrat eines Spielers mit fester Obergrenze. Ist das Inventar voll, muss beim Kauf ein altes Item ersetzt werden. *Verwandt:* [[Item]].

#### J

**Jeder-gegen-Jeden** — Siehe [[FFA]].

#### K

**Kategorie** — Siehe [[Minigame-Kategorie]].

**Kompetenz** — Design-Ziel aus der Selbstbestimmungstheorie (SDT): Spieler müssen das Gefühl haben, ihre Fähigkeiten wachsen zu sehen, mit klarer Rückmeldung über Erfolg und Misserfolg. In Party Arena u. a. durch wachsende Vertrautheit mit Items und Minispielen bedient. *Verwandt:* [[Autonomie]], [[Flow]].

**Kooperation** — Eine der 5 Minigame-Kategorien: Spiele, in denen alle Spieler gemeinsam gegen eine Aufgabe antreten (Team-Modus, alle gewinnen oder verlieren zusammen). *Verwandt:* [[Minigame-Kategorie]].

#### L

**Lobby** — Der Raum vor Spielbeginn, in dem Spieler beitreten, Charaktere wählen, die Insel wählen und Optionen festlegen. Die Lobby unterstützt lokale und Online-Spieler sowie AI-Plätze; maximale Spielerzahl: 8. *Verwandt:* [[Lobby-Größe]].

**Lobby-Größe** — Die maximale Spieleranzahl pro Partie. In Super Tux Party hart auf 4 begrenzt; in Party Arena auf **8** erweitert (kritische Lücke, siehe `session-1-analysis.md`). *Verwandt:* [[Lobby]].

**Ludonarrative Harmonie** — Design-Prinzip: Mechanik und Erzählung müssen zusammenpassen (z. B. ArenaStar moderiert, weil das Spiel eine Arena-Fantasie ist; keine düstere Story in einem fröhlichen Spielzeug-Spiel). *Verwandt:* [[Narrative]].

#### M

**MDA** — Das Analyse-Modell von Hunicke/LeBlanc/Zubek: **M**echanik (Regeln) → **D**ynamik (entstehendes Verhalten) → **A**esthetics (Emotionen). Design läuft rückwärts: Erst die Ziel-Emotion, dann die Dynamik, dann die Regeln. *Verwandt:* [[Aesthetics]], [[Dynamik]], [[Mechanik]].

**Makro-Loop** — Die oberste Schleife des Core Loop: die gesamte Partie von der Lobby über 8–10 Runden bis zur Siegerehrung mit Bonus-Sternen. *Verwandt:* [[Core Loop]], [[Runde]].

**Mechanik** (MDA) — Die unterste Ebene des MDA-Modells: die formalen Regeln und Systeme, die das Spiel definieren (Würfel, Felder, Ökonomie). *Verwandt:* [[MDA]], [[Dynamik]].

**Mechanik-Stadt** — Eine der 7 Inseln von Aethonia (Thema: Spielzeug-Technik). Farbwelt: Silber, Orange, Gelb. Heimat von Brix und Bolt. *Verwandt:* [[Aethonia]], [[Insel]].

**Meso-Loop** — Die mittlere Schleife des Core Loop: eine vollständige Runde — alle Spieler würfeln und ziehen, danach Minispiel, danach Belohnung. *Verwandt:* [[Core Loop]], [[Runde]].

**Mikro-Loop** — Die unterste Schleife des Core Loop: der einzelne Spielzug — Würfeln, Ziehen, Feld-Effekt. *Verwandt:* [[Core Loop]].

**Minispiel** (Synonym: Mini-Game) — Ein kurzer Wettkampf zwischen den Spielern, der nach jeder Runde stattfindet. Dauer ca. 30 Sekunden; Ergebnis bestimmt die Münz-Belohnung ([[Platzierung]]). *Verwandt:* [[Minigame-Kategorie]], [[Minispiel-Feld]].

**Minispiel-Feld** — Feldtyp, der (zusammen mit allen anderen Spielerzügen der Runde) den Minispiel-Trigger setzt. Die meisten Felder des 40er-Pfads sind Minispiel-Felder ("Rest"). *Verwandt:* [[Feld-Typ]], [[Minispiel]].

**Minigame-Kategorie** — Eine der 5 Klassen von Minispielen: Geschicklichkeit, Reaktion, Puzzle/Logik, Rechnen/Wort, Kooperation. Jede Kategorie hat eigene Zugänglichkeits- und Fairness-Anforderungen. *Verwandt:* [[Minispiel]].

**Moderator** — Die Rolle von [[ArenaStar]]: Er führt durch die Partie, erklärt Regeln, kündigt Phasen an und inszeniert Belohnungen. *Verwandt:* [[ArenaStar]].

**Münze** (Synonym: Coin; bevorzugt: **Münze**) — Die Sekundärwährung von Party Arena. Münzen werden in Minispielen, auf Feldern und durch Ereignisse verdient und in Items sowie Sterne investiert. Sie ersetzen "Cookies" aus STP. *Verwandt:* [[Stern]], [[Münz-Ökonomie]].

**Münz-Bonus-Feld** — Feldtyp, der beim Landen einen festen Münz-Bonus gewährt. Geplant 4 Felder pro 40er-Pfad. *Verwandt:* [[Feld-Typ]], [[Münze]].

**Münz-Ökonomie** — Das Gesamtsystem der Münz-Quellen (Faucets) und Münz-Senken (Sinks) inklusive Fluss-Bilanz über eine Partie. Spezifikation in `coin-economy.md`. *Verwandt:* [[Münze]], [[Sink/Faucet]].

**Münz-Magnet** — Item: verdoppelt die Münz-Erträge für eine festgelegte Anzahl kommender Feld-Effekte oder Runden. Kosten 4 Münzen. *Verwandt:* [[Item]], [[Münze]].

#### N

**Narrative** — Die erzählerische Ebene des Spiels: Rahmenhandlung, Charakter-Persönlichkeiten, Insel-Atmosphäre, ArenaStar-Dialoge und Flavor-Texte. Party Arena erzählt leichtgewichtig und unterstützt die Spielmechanik, statt sie zu dominieren. *Verwandt:* [[Ludonarrative Harmonie]].

**NodeBoard** — Die Godot-Knotenklasse eines [[Feldes]] im Board. Sie speichert Typ, Sichtbarkeit, next/prev-Verbindungen, Shop-Daten und (in STP) Cake-Status. Wird für Party Arena um die neuen Feldtypen erweitert. *Verwandt:* [[Feld]], [[Controller]].

**Nolok** — Legacy-Figur aus Super Tux Party (Rivale des Maskottchens, Stör-Charakter). **Entfernt.** Seine Effekte (Geldverlust, Würfel-Modifikatoren, Solo-/Kooperations-Minispiele) werden auf das neutrale [[Ereignis-Feld]] übertragen, ohne die Figur. *Siehe auch:* [[Legacy-Umbenennungstabelle]].

**GNU** — Legacy-Begriff aus Super Tux Party (GNU-Figur als Helfer-Maskottchen). **Entfernt.** Seine Belohnungs-Minispiele werden durch reguläre Minispiel- und Ereignis-Mechaniken ersetzt. *Siehe auch:* [[Legacy-Umbenennungstabelle]].

#### O

**Onboarding** — Der Einstieg neuer Spieler: Party Arena bringt Mechaniken durch Spielen bei (erste Runde zeigt Würfel → Bewegung → Feld-Effekt), nicht durch Text-Tutorials. Der [[2-Minuten-Test]] sichert die Wirksamkeit. *Verwandt:* [[Pillar]].

#### P

**Party Arena** — Der Arbeitstitel des Spiels; Projektname des Godot-4.2-Forks von Super Tux Party. *Verwandt:* [[STP]].

**Pillar** (Synonym: Design-Pfeiler; bevorzugt: **Pillar**) — Eine der 4 grundlegenden Design-Vorgaben, an denen alle Entscheidungen gemessen werden: Sofort verständlich, Überzeichnet statt realistisch, Interaktiv wirkend, Wiedererkennbar. *Verwandt:* [[vision-pillars.md]].

**Pfadwahl** — Eine Abzweigung auf dem Board, an der der Spieler entscheidet, zu welchem nächsten Feld er geht. Die Auswahl wird durch Pfeil-UI und ggf. ArenaStar-Hinweis begleitet. *Verwandt:* [[Feld]].

**Platzierung** — Die Rangposition eines Spielers in einem Minispiel (1., 2., 3., …). Höhere Platzierung = höhere Münz-Belohnung. *Verwandt:* [[Minispiel]], [[Münze]].

**Player Fantasy** — Die beschriebene Soll-Erfahrung eines Systems: *was der Spieler fühlen soll.* Jedes Bible-Kapitel definiert in Sektion 2 seine Player Fantasy; sie ist das Ziel, gegen das alle Regeln geprüft werden. *Verwandt:* [[Pillar]].

**Plugin** — Eine austauschbare Inhalts-/Code-Einheit im STP-Fork-Format (Boards, Minispiele, Charaktere, Items). Plugins werden über den [[Plugin-Loader]] geladen. *Verwandt:* [[Board-Loader]], [[Plugin-Loader]].

**Plugin-Loader** — Das System, das alle Plugins (Boards, Minispiele, Charaktere, Items) aus `plugins/` lädt und registriert. Aus STP übernommen, unverändert. *Verwandt:* [[Plugin]].

**Puzzle/Logik** — Eine der 5 Minigame-Kategorien: Spiele, die Denken und Planen erfordern (Muster erkennen, Reihenfolgen, Rätsel). *Verwandt:* [[Minigame-Kategorie]].

#### Q

**Quantic Foundry** — Das differenziertere Motivationsmodell (Action, Social, Mastery, Achievement, Immersion, Creativity), das neben der Bartle-Taxonomie zur Zielgruppen-Validierung genutzt wird. Party Arena adressiert v. a. Excitement (Action), Competition (Social), Challenge (Mastery) und Fantasy (Immersion). *Verwandt:* [[Bartle-Taxonomie]].

#### R

**Reaktion** — Eine der 5 Minigame-Kategorien: Spiele, die schnelle Wahrnehmung und schnelle Eingabe erfordern (Reaktionstests, "Stop"-Momente). *Verwandt:* [[Minigame-Kategorie]].

**Rechnen/Wort** — Eine der 5 Minigame-Kategorien: Spiele mit leichten Rechen- oder Wortaufgaben, die im Kopf lösbar sind (kein Regelstudium nötig). *Verwandt:* [[Minigame-Kategorie]].

**Runde** (Synonym: Turn; bevorzugt: **Runde**) — Ein kompletter Durchlauf aller Spieler: Jeder Spieler macht einen Zug (Würfeln, Ziehen, Feld-Effekt). Danach folgt das Minispiel, danach die Stern-Phase. Eine Partie dauert 8–10 Runden. *Verwandt:* [[Zug]], [[Meso-Loop]].

**Rundenanzahl** — Die konfigurierte Zahl der Runden pro Partie (Standard 8–10, konfigurierbar in der Lobby). *Verwandt:* [[Runde]].

#### S

**Sara** — Legacy-Maskottchen aus Super Tux Party (Moderatorin). **Umbenannt** zu [[ArenaStar]]. *Siehe auch:* [[Legacy-Umbenennungstabelle]].

**Schutzschild** — Item: verhindert den nächsten negativen Lande-Effekt (Pech, negatives Ereignis). Kosten 6 Münzen; verbraucht sich nach einem erfolgreichen Block. *Verwandt:* [[Item]].

**Schwierigkeit** — Einstellstufe für [[AI-Spieler]] (Leicht/Normal/Schwer). Beeinflusst Entscheidungsqualität in Minispielen und Einkaufslogik. *Verwandt:* [[AI-Spieler]].

**Server** — Die autoritative Spielinstanz, die die Spiellogik berechnet und Zustände an alle [[Client]]s synchronisiert. *Verwandt:* [[Host]], [[Client]].

**Signaturfarbe** — Die eine dominante Identitätsfarbe pro [[Charakter]] bzw. [[Insel]] (Brix Orange, Nixie Türkis, Pip Gelb, Koko Rosa, Tiko Grün, Bolt Blau, Bloom Lila, Momo Pink). Sie wiederholt sich über Figur, UI und Assets und ist zentral für den Pfeiler "Wiedererkennbar". *Verwandt:* [[Wiedererkennbar]].

**Silhouette** — Die reine Außenform eines Objekts ohne Farbe/Details. Charaktere, Items, Feld-Icons und Insel-Logos müssen in Silhouette eindeutig erkennbar sein (Silhouetten-Test, Schwelle ≥ 90 %). *Verwandt:* [[Wiedererkennbar]].

**Sink/Faucet** — Ökonomie-Modell: **Faucets** erzeugen Ressourcen (Münz-Quellen), **Sinks** entfernen sie (Münz-Ausgaben). Beide müssen über die Partielänge balanciert sein, sonst entsteht Inflation oder Mangel. *Verwandt:* [[Münz-Ökonomie]].

**Sofort verständlich** — Einer der 4 Design-Pfeiler: Jeder kann nach 2 Minuten mitspielen; eine Aktion pro Moment; Symbole statt Text; konsistente Metaphern. *Verwandt:* [[Pillar]], [[Onboarding]].

**Sonnenstrand** — Eine der 7 Inseln von Aethonia (Thema: Urlaub & Wasser). Farbwelt: Türkis, Sandgelb, Korallenrot. Heimat von Nixie. *Verwandt:* [[Aethonia]], [[Insel]].

**Sound-Effekt (SFX)** — Kurzer, nicht-musikalischer Klang (Würfel, Münzen, Kauf, Bewegung). Jede primäre Interaktion hat einen SFX (Feedback-Pflicht). *Verwandt:* [[Bus]].

**Split Screen** — Die geteilte Bildschirmansicht bei lokaler Mehrspieler-Partie; bei 8 Spielern wird das Layout dynamisch aufgeteilt. *Verwandt:* [[Kamera]].

**Startfeld** — Das Feld, auf dem alle Spieler zu Spielbeginn stehen (Feldtyp "Start", 1 pro Insel). *Verwandt:* [[Feld-Typ]].

**Stern** (Synonym: Star; bevorzugt: **Stern**) — Die Hauptwährung und das Siegobjekt von Party Arena. Ein Stern kostet 20 Münzen und wird am Sternen-Shop gekauft; nach dem Kauf wandert die Stern-Statue zu einem neuen Shop-Feld. Gewonnen hat, wer nach der letzten Runde plus Bonus-Sternen die meisten Sterne besitzt. Ersetzt "Cake" aus STP. *Verwandt:* [[Münze]], [[Bonus-Stern]], [[Stern-Ökonomie]].

**Sternen-Phase** — Der Abschnitt nach dem Minispiel einer Runde, in dem gekaufte Sterne vergeben, die Stern-Statue neu positioniert und der Rundenzähler aktualisiert wird. *Verwandt:* [[Stern]].

**Sternen-Shop** — Verkaufsstelle für [[Sterne]] auf dem Board. 2–3 Sternen-Shop-Felder pro Insel; die Statue wandert nach jedem Kauf. *Verwandt:* [[Sternen-Shop-Feld]].

**Sternen-Shop-Feld** — Feldtyp, der den Sternen-Shop auslöst. *Verwandt:* [[Feld-Typ]], [[Sternen-Shop]].

**Stern-Teleporter** — Item: bewegt den Spieler sofort zur aktuellen Position der Stern-Statue. Kosten 8 Münzen. Strategisch stark; wird durch Kosten und Zugverbrauch balanciert. *Verwandt:* [[Item]], [[Stern]].

**Sternenzitadelle** — Die 8. und letzte Insel (Finale; 7+1). Thema: Feier und Sieg. Farbwelt: Gold, Tiefblau, Magenta. Sitz von ArenaStar und Ziel der großen Final-Runde. *Verwandt:* [[Aethonia]], [[Insel]].

**STP** (Super Tux Party) — Das Open-Source-Spiel (Godot), dessen Code die technische Basis von Party Arena ist. STP-Begriffe (Cookies, Cakes, Sara, Nolok, GNU) werden per Legacy-Tabelle umbenannt oder entfernt. *Verwandt:* [[Fork]].

**Sieg** — Das Partieziel: die meisten Sterne (inkl. Bonus-Sterne) nach der letzten Runde. Gleichstände werden über feste Tiebreaker entschieden (siehe `victory-conditions.md`). *Verwandt:* [[Stern]], [[Bonus-Stern]].

#### T

**Tuning Knob** — Ein konfigurierbarer Zahlenwert einer Mechanik (Preis, Dauer, Anzahl, Wahrscheinlichkeit), der in einer Data-Datei liegt und balanciert werden kann. Jedes Bible-Kapitel listet seine Tuning Knobs mit Bereich und Standard. *Verwandt:* [[Sink/Faucet]].

**Turn** — Siehe [[Zug]] und [[Runde]]. "Turn" wird in technischen Kontexten für den einzelnen Spielerzug verwendet; "Runde" für den kompletten Durchlauf.

#### U

**Überzeichnet statt realistisch** — Einer der 4 Design-Pfeiler: konsequente Cartoon-/Toy-Ästhetik, hohe Sättigung, übertriebene Proportionen und Animationen; keine realistischen Texturen oder düsteren Darstellungen. *Verwandt:* [[Pillar]].

**UI** — Die gesamte Benutzeroberfläche: Menüs, HUD, Shops, Dialoge, Charakter-Auswahl. Spezifikation in den `ui-*.md`-Kapiteln. *Verwandt:* [[HUD]].

**Unsichtbares Feld** — Ein Feld, das auf dem Board nicht als Schritt zählt (z. B. eine lange Strecke, die übersprungen wird). Bewegungsschritte werden nur auf [[sichtbarem Feld]] gezählt. *Verwandt:* [[Feld]].

**Sichtbares Feld** — Ein Feld, das als eigener Bewegungsschritt zählt und auf dem der Spieler sichtbar anhält. Die Unterscheidung sichtbar/unsichtbar steuert die Würfel-Schrittzählung. *Verwandt:* [[Feld]].

#### V

**Verlierer-Boost** — Catch-Up-Mechanik: Spieler auf den hinteren Plätzen erhalten zusätzliche Unterstützung (z. B. Bonus-Münzen, Items oder günstigere Ereignis-Optionen), um Partien offen zu halten. *Verwandt:* [[Catch-Up]].

#### W

**Wiedererkennbar** — Einer der 4 Design-Pfeiler: jedes zentrale Objekt (Charakter, Insel, Item, Feld-Typ) ist über Silhouette, Signaturfarbe und Form eindeutig identifizierbar — auch in Miniatur und Split Screen. *Verwandt:* [[Pillar]], [[Silhouette]].

**Wolkenwerk** — Eine der 7 Inseln von Aethonia (Thema: Schwebende Himmel). Farbwelt: Hellblau, Weiß, Regenbogen. Heimat von Pip. *Verwandt:* [[Aethonia]], [[Insel]].

**Würfel** (Synonym: Dice; bevorzugt: **Würfel**) — Das Zufallswerkzeug des Spiels: Standard-Würfel mit 1–6. Items wie der Glücks-Würfel ersetzen ihn zeitweise. *Verwandt:* [[Würfeln]], [[Glücks-Würfel]].

**Würfeln** — Die Aktion, den Würfel zu werfen, um die Zugweite zu bestimmen. Im Standard-Ablauf: würfeln → ziehen → Feld-Effekt. *Verwandt:* [[Würfel]], [[Zug]].

#### Z

**Zitadelle** — Siehe [[Sternenzitadelle]].

**Zug** (Synonym: Player Turn; bevorzugt: **Zug**) — Der einzelne Spielzug eines Spielers innerhalb einer [[Runde]]: würfeln, ziehen, Feld-Effekt auslösen, ggf. Item einsetzen. *Verwandt:* [[Runde]], [[Würfeln]].

**Zuckerwald** — Eine der 7 Inseln von Aethonia (Thema: Süßigkeiten). Farbwelt: Rosa, Schokobraun, Mintgrün. Heimat von Koko. *Verwandt:* [[Aethonia]], [[Insel]].

**2-Minuten-Test** — Das Qualitätsprotokoll aus `vision-pillars.md`: Eine Person ohne Vorkenntnisse muss nach 2 Minuten Beobachtung (bzw. einem eigenen Zug) verstehen, was passiert und was zu tun ist. Maßgeblich für den Pfeiler "Sofort verständlich". *Verwandt:* [[Sofort verständlich]].

### 3.3 Legacy-Umbenennungstabelle (STP → Party Arena)

| Legacy-Begriff (STP) | Neuer Begriff (Party Arena) | Status | Anmerkung |
|----------------------|-----------------------------|--------|-----------|
| Cookie / Cookies | Münze / Münzen | umbenannt | Sekundärwährung; alle Code-/UI-Namen migrieren. |
| Cake / Cakes | Stern / Sterne | umbenannt | Siegwährung; inkl. `cake_space` → `star_space`. |
| Sara | ArenaStar | umbenannt | Maskottchen/Moderatorin; alle Sara-Icons/-Dialoge ersetzen. |
| Nolok | (entfällt) | entfernt | Figur gestrichen; Effekte wandern in neutrale Ereignis-Kartei. |
| GNU | (entfällt) | entfernt | Figur gestrichen; Belohnungs-Minispiele werden reguläre Minispiele. |
| NODE_TYPES.BLUE | (aufgelöst) | entfernt | Feldtyp-Modell wird durch Party-Arena-Feldtypen ersetzt. |
| NODE_TYPES.RED | (aufgelöst) | entfernt | Siehe `field-luck.md` (Glück/Pech ersetzt Rot). |
| NODE_TYPES.GREEN | Ereignis-Feld | umbenannt | Event-Mechanik bleibt, Inhalt wird neu. |
| NODE_TYPES.YELLOW | Glück/Pech-Feld | umbenannt | Duelle werden zu neutralen Ereignissen umgebaut. |
| NODE_TYPES.SHOP | Item-Shop-Feld | umbenannt | Neuer separater Sternen-Shop kommt hinzu. |
| COOKIES_FOR_CAKE = 30 | STERN_KOSTEN = 20 | umbenannt | Sternpreis von 30 auf 20 Münzen gesenkt (Tuning-Knob). |
| LOBBY_SIZE = 4 | LOBBY_SIZE = 8 | modifiziert | 8-Spieler-Support ist kritische Lücke. |
| Minigame-Typen (FFA, 2v2, 1v3, Duel, Nolok/GNU-Solo/Coop) | FFA, 2v2, 1v3 (Nolok/GNU-Typen entfernt) | modifiziert | Duel/1v3-Sonderfälle werden durch 5 Kategorien ersetzt. |

## 4. Formulas

### 4.1 Eintrags-Maske (Strukturformel für Glossar-Einträge)

Jeder Glossar-Eintrag folgt der Maske:

`E = (B, S*, D, X, V*)`, wobei:
- `B` = bevorzugter Begriff (Pflicht),
- `S*` = Synonyme (optional, 0–n, als "Synonyme" markiert),
- `D` = Definition (Pflicht, 1–3 Sätze, eindeutig),
- `X` = Beispiel/Kontext (Pflicht, 1 Satz mit "Beispiel:"),
- `V*` = verwandte Begriffe (optional, als "Verwandt:" mit Glossar-Links).

Akzeptanzregel: Ein Eintrag ohne `B` und `D` gilt als nicht existent; `X` ist Pflicht, damit Definitionen an Beispielen prüfbar bleiben.

### 4.2 Umbenennungs-Funktion

Die Legacy-Umbenennung wird formal als Funktion `R(begriff)` definiert:

- `R(begriff ∈ Legacy-Tabelle) → neuer Begriff`, falls Status = `umbenannt`,
- `R(begriff ∈ Legacy-Tabelle) → ∅`, falls Status = `entfernt`,
- `R(begriff ∉ Legacy-Tabelle) → begriff` (unverändert).

Akzeptanzregel: Für jeden in einem Kapitel verwendeten Begriff gilt `R(begriff) ≠ ∅` und `R(begriff)` ist der im Kapitel verwendete Term. Ein Kapitel, das einen Legacy-Begriff als aktiven Term verwendet, verletzt die Regel und wird als Rebranding-Fehler (Review-Blocker) behandelt.

### 4.3 Eindeutigkeit der Signaturfarben

`ΔHue(a, b) = |Hue(a) − Hue(b)|` mod 360, wobei `a, b` zwei verschiedene Charaktere (bzw. Inseln) sind.

- Akzeptanzregel: `ΔHue ≥ 30°` für alle Paare. Für 8 Charaktere sind dies `C(8,2) = 28` Paare, für 7+1 Inseln `C(8,2) = 28` Paare. Die Prüfung erfolgt im Rahmen des Silhouetten-/Farbtests (siehe `vision-pillars.md`, Formel 4.4).

### 4.4 Glossar-Vollständigkeit

`G = n_definiert / n_referenziert × 100`, wobei:
- `n_referenziert` = Anzahl der im Glossar selbst verlinkten Begriffe (`Verwandt`-Links) plus der in Sektion 6 der Bible-Kapitel verwendeten Fachbegriffe,
- `n_definiert` = Anzahl der davon im Glossar definierten Begriffe.

- Ziel: `G = 100`. Ein verlinkter oder verwendeter Begriff ohne Glossar-Eintrag ist ein Dokumentationsdefizit (Priorität niedrig, aber vor Alpha zu beheben).

## 5. Edge Cases

1. **Begriff mit zwei Bedeutungen:** Wenn ein Begriff in zwei unterschiedlichen Kontexten verschiedene Bedeutungen hat (z. B. "Board" = Insel vs. "Board" = technische Board-Instanz), werden beide Bedeutungen im selben Eintrag getrennt geführt, oder es werden zwei Einträge mit Verweis angelegt. Eine unbemerkte Doppelbedeutung ist ein Review-Blocker, da sie Missverständnisse erzeugt.
2. **Neuer Begriff während der Entwicklung:** Neue Begriffe (z. B. ein neues Item) werden sofort eingetragen und alphabetisch einsortiert. Bis zum Eintrag darf der Begriff in Kapiteln nur mit vorläufiger Definition verwendet werden; ohne Eintrag gilt er als nicht definiert.
3. **Umbenennung eines neuen Begriffs:** Eine spätere Umbenennung (z. B. "Kuchen" → "Torte") erfordert ein Aktualisieren aller Kapitel, des Index und des Glossars in einem Zug. Alias-Formen können als "Synonyme (veraltet)" erhalten bleiben, um alte Dokumente lesbar zu halten.
4. **Kollision mit Code-Bezeichnern:** Code-Bezeichner (z. B. `COOKIES_FOR_CAKE`) sind vom Glossar-Begriff zu unterscheiden. Die Legacy-Tabelle dokumentiert die Zuordnung; ein Code-Bezeichner darf weiterhin existieren, solange sein Anzeigename dem neuen Begriff entspricht.
5. **Legacy-Begriff in Kunst-Assets:** Assets (Texturen, Icons) mit Legacy-Beschriftung (z. B. ein Keks-Icon) sind Rebranding-Fälle. Das Glossar definiert den Zielbegriff; die Migration ist in `technical-fork-strategy.md` geplant.
6. **Übersetzungsprobleme:** Falls ein deutscher Begriff in einer Zielsprache nicht existiert (z. B. "Glück-Pech-Feld"), wird der deutsche Begriff als Marken-/Systemname beibehalten und lokalisiert beschrieben. Die Entscheidung wird pro Begriff im Glossar vermerkt.
7. **Abkürzungen und Akronyme:** Jedes Akronym (MDA, SDT, FFA, STP, UI, HUD, SFX) hat einen eigenen Eintrag mit ausgeschriebener Bedeutung. Abkürzungen ohne Eintrag sind nicht zulässig.
8. **Glossar-Referenz auf nicht existierendes Kapitel:** Verlinkt ein Eintrag auf ein Kapitel, das noch nicht existiert (z. B. `coin-economy.md`), ist dies zulässig, solange der Eintrag die inhaltliche Bedeutung unabhängig erklärt. Der Link wird als "geplant" markiert und aufgelöst, sobald das Kapitel geschrieben ist.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `glossary.md` | Art | Verwendung |
|----------------------------|-----|------------|
| `design/gdd/game-concept.md` | Quelle | Liefert die Kerntaxonomie (8 Arenians, 7+1 Inseln, Items, Währungen), die hier verbindlich definiert wird. |
| `design/gdd/session-1-analysis.md` | Quelle | Liefert die Legacy-Umbenennungsliste (Cookies→Münzen, Cakes→Sterne, Sara→ArenaStar, Nolok/GNU entfernen). |
| `design/gdd/bible-index.md` | Peer | Referenziert die Begriffe; der Index erzwingt die Glossar-Verknüpfung beim ersten Vorkommen. |
| `design/gdd/vision-pillars.md` | Peer | Definiert Konzepte wie "Silhouette", "Signaturfarbe", "2-Minuten-Test", die im Glossar aufgenommen werden. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| Alle 65 Bible-Kapitel | Müssen Begriffe exakt in Glossar-Definition verwenden (Regel 3.1.1). |
| UI-Texte, Dialoge, Flavor-Texte | Müssen die Glossar-Terminologie als Anzeigenamen verwenden (z. B. "Münzen", "Sterne"). |
| `technical-fork-strategy.md` | Verwendet die Legacy-Tabelle als Migrations-Grundlage. |
| Lokalisierung | Übersetzt Anzeigenamen, hält Markennamen (Aethonia, ArenaStar, Inselnamen) unverändert. |
| `technical-data-structures.md` | Muss die Code-bezeichner-Zuordnung (4.2) konsistent zum Glossar führen. |

### 6.3 Bidirektionalität

Das Glossar ist die Terminologie-Quelle und zugleich von den Kapiteln abhängig: Neue Kapitel führen neue Begriffe ein, die ins Glossar zurückfließen (Regel 3.1.4 und 5.2). Die Schleife ist gewollt und wird über die Glossar-Vollständigkeit (4.4) überwacht.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Pflichtfelder der Eintrags-Maske | Gate | `B`, `D`, `X` Pflicht | `B,D,X` | Sichert Eindeutigkeit und Beispielhaftigkeit jedes Eintrags. |
| Farbabstand `ΔHue` | Kurve | ≥ 30° | ≥ 30° | Sichert die Unterscheidbarkeit von Signaturfarben (Formel 4.3). |
| Glossar-Vollständigkeit `G` | Kurve | 90–100 % | 100 % | Schwelle für die Terminologie-Abdeckung vor Alpha. |
| Anzahl der Legacy-Einträge | Kurve | 0–20 | 9 | Sinkt mit fortschreitendem Rebranding auf 0 (veraltete Einträge werden zu "entfernt" markiert und später gelöscht). |
| Markennamen-Schutz | Gate | Liste fix | Aethonia, ArenaStar, Inselnamen | Markennamen werden nie übersetzt; nur Markennamen in dieser Liste sind geschützt. |

## 8. Acceptance Criteria

Ein QA-Tester (oder ein Text-Review) kann folgende Prüfungen ausführen:

1. **Eintrags-Maske:** Jeder Eintrag besitzt `B`, `D` und `X` (Formel 4.1); kein Eintrag ist leer oder nur ein Stichwort. PASS/FAIL.
2. **Alphabetische Sortierung:** Alle Einträge sind innerhalb ihrer Buchstaben-Sektion alphabetisch sortiert; neue Begriffe sind korrekt einsortiert. PASS/FAIL.
3. **Legacy-Kontrolle:** In keinem `[geschrieben]`-Bible-Kapitel (außer `glossary.md` und `technical-fork-strategy.md`) treten die aktiven Legacy-Begriffe Cookie, Cake, Sara, Nolok oder GNU auf. PASS/FAIL.
4. **Begriffs-Konsistenz in UI-Beispielen:** Für 20 zufällig gewählte UI-Textbeispiele aus `ui-*.md`-Kapiteln stimmt der Anzeigename mit dem Glossar-Begriff überein. PASS/FAIL.
5. **Verlinkte Begriffe existieren:** Jeder `Verwandt`-Link im Glossar verweist auf einen existierenden Eintrag; `G = 100` (Formel 4.4). PASS/FAIL.
6. **Umbenennungs-Funktion:** Für alle in der Legacy-Tabelle gelisteten Begriffe ist `R(begriff)` korrekt angegeben (umbenannt/entfernt/modifiziert) und konsistent zu `technical-fork-strategy.md`. PASS/FAIL.
7. **Farbabstand:** Die Signaturfarben der 8 Charaktere und 8 Inseln erfüllen `ΔHue ≥ 30°` für alle Paare (Formel 4.3). PASS/FAIL.
8. **Auffindbarkeit (Experiential):** Ein Teammitglied findet nachweislich in unter 1 Minute die Definition eines ihm gestellten Begriffs (gemessen per Protokoll). PASS/FAIL.
