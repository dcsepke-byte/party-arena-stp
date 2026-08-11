# Vision & Pillars — Party Arena Game Bible

> **Teil:** 0 — Meta & Vision
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md (Abschnitt "Designprinzipien")

---

## 1. Overview

Dieses Kapitel definiert die vier Design-Pfeiler von Party Arena: **Sofort verständlich**, **Überzeichnet statt realistisch**, **Interaktiv wirkend** und **Wiedererkennbar**. Die Pfeiler sind die höchste Entscheidungsinstanz des Projekts: Jede Design-, Art-, UI- oder Audio-Entscheidung wird an ihnen gemessen. Für jeden Pfeiler wird konkret spezifiziert, was er für Design-Entscheidungen bedeutet, welche Entscheidungen er ausschließt und welche Beispiele ihn illustrieren. Zusätzlich werden Anti-Pfeiler definiert (was Party Arena bewusst nicht ist), eine formale Konfliktlösung zwischen Pfeilern festgelegt und der verpflichtende "2-Minuten-Test" als Qualitätsprotokoll beschrieben. Die Pfeiler ersetzen die impliziten Stil-Vorlieben des Konzepts durch prüfbare Regeln, an die sich alle nachfolgenden Kapitel halten müssen.

## 2. Player Fantasy

Die vier Pfeiler beschreiben zusammen das Gefühl, das jeder Moment in Party Arena auslösen soll: **"Ich verstehe das sofort, es sieht fröhlich und spielzeughaft aus, es reagiert auf jeden meiner Schritte, und ich kann jeden Charakter und jede Insel auf einen Blick auseinanderhalten."** Der Spieler soll sich nie verloren, nie gelangweilt und nie im Ungewissen fühlen. Konkret:

- **Sofort verständlich** erzeugt Kompetenz-Gefühl (Self-Determination Theory): Man fühlt sich vom ersten Moment an fähig, mitzuspielen — ohne Nachschlagen.
- **Überzeichnet statt realistisch** erzeugt Freude und Abgrenzung vom Alltag: Die Welt ist eine spielzeughafte Bühne, auf der alles größer, bunter und lustiger ist als im echten Leben (MDA-Aesthetic "Sensation" und "Fantasy").
- **Interaktiv wirkend** erzeugt Autonomie und Agency: Jede Eingabe hat eine sichtbare, hörbare, unmittelbare Antwort. Nichts fühlt sich taub oder träge an.
- **Wiedererkennbar** erzeugt Vertrautheit und Orientierung: Figuren, Inseln und Items sind sofort identifizierbar, auch bei schnellen Kamerafahrten, Split-Screen-Kleinheit oder aus dem Augenwinkel.

Zusammengefasst verspricht der Erlebnis-Kern: *"Party Arena fühlt sich an wie ein hochwertiges Spielzeug, das auf Berührung reagiert und niemals verwirrt."*

## 3. Detailed Rules

### 3.1 Pfeiler 1 — Sofort verständlich

**Definition:** Jeder Spieler, egal ob erfahren oder Neuling, kann ohne Anleitung verstehen, was gerade passiert und was als Nächstes zu tun ist. Die Schwelle ist: **Ein Spieler kann nach 2 Minuten Beobachtung oder einem einzigen Test-Zug mitspielen.** Komplexität wird schrittweise eingeführt und nie durch Text, sondern durch Spielhandlung erklärt.

#### 3.1.1 Konkrete Bedeutung für Design-Entscheidungen

1. **Eine Aktion pro Moment:** Jeder Spielzustand bietet genau eine primäre Handlung (würfeln, kaufen, Pfad wählen, Item nutzen). Warte-Situationen zeigen klar an, *wessen* Zug es ist und *was* erwartet wird (HUD-Hervorhebung, ArenaStar-Hinweis).
2. **Symbole statt Text:** Münzen, Sterne, Items und Feld-Effekte werden primär durch Icons und Piktogramme kommuniziert; Text ist Ergänzung, nie Voraussetzung. Icons folgen einem festen Vokabular aus `glossary.md`.
3. **Regeln durch Beispiele:** Neue Mechaniken (Item-Effekt, Ereignis, Bonus-Stern) werden im ersten Auftreten durch eine kurze, spielbare Demonstration oder durch ArenaStar-Moderation gezeigt, bevor sie voll wirken.
4. **Konsistente Metaphern:** Die gesamte Ökonomie folgt einer einzigen, durchgängigen Metapher ("Sammle Münzen, kaufe Sterne, gewinne mit den meisten Sternen"). Keine zweite, widersprüchliche Metapher einführen.
5. **Vorhersehbarkeit der Werte:** Zahlen sind klein, ganzzahlig und in einem überschaubaren Bereich (Münzen 1–100, Sterne 0–10, Würfel 1–6). Komplexe Mathematik (Prozentwerte, negative Werte) erscheint nur dort, wo ein Icon sie bereits erklärt.

#### 3.1.2 Was dieser Pfeiler ausschließt

- Keine Regeln, die nur aus dem Handbuch oder Tutorial verständlich sind (kein "verstecktes Regelwerk").
- Keine konkurrierenden Wirtschaftssysteme mit eigener Metaphorik.
- Keine Aktionen ohne sichtbare Konsequenz (siehe Pfeiler 3).
- Keine Zahlenformate, die ein Spieler im Kopf umrechnen muss (z. B. "kostet 0,75 Sterne").
- Keine Entscheidungen ohne Informationsbasis (der Spieler muss alle relevanten Fakten sehen, bevor er wählt).

#### 3.1.3 Beispiele

- Der Stern-Kauf zeigt das Stern-Symbol, den Preis "20" mit Münz-Symbol und einen Knopf "Kaufen" — kein Fließtext nötig.
- Ein Ereignis-Feld zeigt vor dem Effekt ein großes Icon mit einem Wort ("Regenbogen", "Sturm") und spielt die Wirkung animiert vor.
- Der aktive Spieler ist auf dem HUD mit leuchtender Umrandung und einem Pfeil über der Figur markiert; das Würfel-Symbol pulsiert als Aufforderung.

### 3.2 Pfeiler 2 — Überzeichnet statt realistisch

**Definition:** Die Darstellung ist konsequent cartoonhaft, spielzeughaft und übertrieben. Alles ist größer, runder, bunter und ausdrucksstärker als in der Realität. Es gibt keinerlei Streben nach Realismus in Geometrie, Material, Licht oder Animation.

#### 3.2.1 Konkrete Bedeutung für Design-Entscheidungen

1. **High Saturation:** Farben sind gesättigt und klar voneinander getrennt; Pastelltöne nur als Akzent. Jede Insel hat eine eigene, kräftige Farbidentität (siehe `game-concept.md`).
2. **Toy-like Materialität:** Oberflächen wirken wie Spielzeug (Plastik, Filz, Holz, Bonbon, glänzender Lack), nie wie Foto-Texturen. Dies gilt für Board, Charaktere, Items und UI.
3. **Übertriebene Proportionen:** Charaktere haben große Köpfe, große Augen, kurze Gliedmaßen. Emotionen werden durch Deformation übertrieben (Staunen = riesige Augen, Trauer = zusammensackende Schultern).
4. **Übertriebene Animation:** Jede Bewegung hat Vorbereitung (Anticipation), Übertreibung (Squash & Stretch) und Nachklang (Follow-through). Ein Würfelwurf ist ein Ereignis, kein Statistik-Vorgang.
5. **Komische Gewalt / Konflikt:** Negative Effekte (Münzverlust, Diebstahl) werden slapstickhaft inszeniert (Staubwolke, "Plötz"-Geräusch, übertriebenes Stolpern), damit sie ärgerlich, aber nie bedrohlich wirken.
6. **Keine realistischen Konsequenzen:** Verlieren führt zu komischen Trotz-Animationen, nie zu düsteren oder gewalttätigen Bildern. Der Ton bleibt familienfreundlich.

#### 3.2.2 Was dieser Pfeiler ausschließt

- Keine photorealistischen Texturen, keine PBR-Materialien mit Realismus-Anspruch, keine echten Fotos.
- Keine realistischen Proportionen, keine anatomisch korrekten Bewegungen.
- Keine blutigen, düsteren oder angsteinflößenden Darstellungen.
- Keine tristen, ungesättigten Farbpaletten (Ausnahme: bewusste, kurze Kontraste wie Nacht-Feld-Effekt, dann mit klarer Spielzeug-Ästhetik).
- Keine "ernsten" Kamera- oder Licht-Inszenierungen, die aus dem Spielzeug-Feeling fallen.

#### 3.2.3 Beispiele

- Ein Stein (Brix) besteht aus glatten, abgerundeten Spielzeugblöcken mit leuchtend oranger Farbe — nicht aus realistischer Gesteinsstruktur.
- Münzen sind dicke, glänzende Goldmedaillen mit Stern-Prägung; beim Einsammeln springen sie mit einer Feder-Squash-Animation.
- Die Frostgipfel-Insel besteht aus glitzernden, zuckerartigen Eiswürfeln mit weißen Filz-Wolken — nicht aus fotorealistischem Schnee.

### 3.3 Pfeiler 3 — Interaktiv wirkend

**Definition:** Das Spiel fühlt sich lebendig und reagiert auf jede Eingabe. Nichts ist passiv: Jeder Klick, jeder Tastendruck, jede Bewegung hat eine sofortige, sichtbare und/oder hörbare Rückmeldung. Leerlauf ist mit Leben gefüllt (Idle-Animationen, umherziehende Effekte, ArenaStar-Reaktionen).

#### 3.3.1 Konkrete Bedeutung für Design-Entscheidungen

1. **Mikro-Feedback-Pflicht:** Jede erfolgreiche Eingabe bestätigt sich innerhalb von **0,5 Sekunden** (Icons reagieren, Buttons färben sich, Sounds spielen). Jede fehlgeschlagene Eingabe gibt ebenfalls ein klares negatives Feedback (kein stummes Ignorieren).
2. **Sichtbarkeit der Wirkung:** Jede Zustandsänderung (Münzen, Sterne, Items, Position) wird animiert: Münzen fliegen zum Kontostand, Sterne schweben zum Spielerporträt, Items springen ins Inventar.
3. **Hover- und Fokus-Zustände:** Alle interaktiven Elemente (Buttons, Felder, Items im Shop) haben ausgeprägte Hover-/Fokus-Zustände mit Bewegung (Vergrößerung, Aufhellung, Wackeln).
4. **Lebendige Welt:** Das Board lebt auch ohne Eingabe: animierte Wasserfälle, wackelnde Blumen, vorbeiziehende Wolken, zuckende NPCs. Kein Standbild-Eindruck.
5. **ArenaStar als Reaktions-Verstärker:** Das Maskottchen kommentiert wichtige Momente mit kurzen Animationen und Sounds (Jubel bei Stern-Kauf, Trost bei Pech), verstärkt aber nicht jede Kleinigkeit, um nicht zu nerven.
6. **Wartezeit-Überbrückung:** Bei fremden Zügen oder Ladezeiten läuft Unterhaltung (Mini-Idle-Szenen, Dreh-Animationen), nie ein eingefrorener Bildschirm ohne Status.

#### 3.3.2 Was dieser Pfeiler ausschließt

- Keine toten Eingaben (Buttons ohne Reaktion, Klicks ohne Konsequenz).
- Keine langen, nicht überspringbaren Sequenzen ohne Feedback.
- Keine statischen Bildschirme während fremder Spielerzüge ohne Hinweis auf den Wartezustand.
- Keine Aktionen, deren Wirkung erst nach mehreren Sekunden oder gar nicht sichtbar wird.
- Kein "lebloses" UI ohne Hover-/Fokus-Verhalten.

#### 3.3.3 Beispiele

- Der Würfel-Button wackelt beim Hovern, beim Drücken schrumpft er kurz (Pressed-Feedback) und der Würfel im Zentrum animiert den Wurf mit Sound.
- Beim Münzgewinn fliegen Münzen vom Feld zum Kontostand des Spielers und das Porträt hüpft; der Zähler dreht mit einem "Klick"-Sound pro Münze.
- Bei Item-Kauf öffnet sich das Inventar mit einer Spring-Animation, das neue Item glüht kurz auf und der Kauf-Sound bestätigt.

### 3.4 Pfeiler 4 — Wiedererkennbar

**Definition:** Jeder Charakter, jede Insel, jedes Item und jeder Feldtyp hat eine unverwechselbare Silhouette, Farbidentität und Gestalt, sodass Identifikation auch ohne Text, bei kleinen Darstellungen, aus dem Augenwinkel und unter Zeitdruck gelingt.

#### 3.4.1 Konkrete Bedeutung für Design-Entscheidungen

1. **Silhouetten-Test:** Jedes zentrale Objekt (Charakter, Item, Stern, Münze, Feld-Icon, Insel-Logo) muss in reiner Silhouette (schwarz auf weiß) eindeutig erkennbar sein. Das gilt auch in Miniatur (Split-Screen, Charakter-Auswahl, HUD).
2. **Eine Signaturfarbe pro Charakter:** Jeder Arenian hat genau eine dominante Signaturfarbe (Brix Orange, Nixie Türkis, Pip Gelb, Koko Rosa, Tiko Grün, Bolt Blau, Bloom Lila, Momo Pink). Diese Farbe wiederholt sich auf Figur, Porträt, HUD-Elementen und UI-Akzenten.
3. **Eine Formsprache pro Insel:** Jede Insel hat ein eigenes Form- und Farbvokabular (Sonnenstrand: rund, türkis/sand; Zuckerwald: zuckrig, rosa/braun; etc.), das sich in Feld-Modellen, Hintergründen und Mini-Spiel-Ästhetik wiederholt.
4. **Feld-Typen über Form + Icon:** Feld-Typen sind nicht nur über Farbe, sondern über eine zusätzliche, eindeutige Form oder ein Icon unterscheidbar (Stern = Sternform, Münze = runde Medaille, Item = Geschenkbox, Ereignis = Blitz/Ausrufezeichen). Dies sichert Farbblindheit-Zugänglichkeit.
5. **Items mit klarer Form:** Items haben ikonische Formen (Glücks-Würfel = Würfel mit Stern, Teleporter = Wirbel, Schild = Schild mit Stern, Magnet = Hufeisenmagnet mit Münze, Handschuh = Handschuh mit Diebes-Optik).

#### 3.4.2 Was dieser Pfeiler ausschließt

- Keine zwei Charaktere mit ähnlicher Silhouette oder verwechselbarer Signaturfarbe.
- Keine Insel-Layouts, die ohne Text nicht der richtigen Insel zuordenbar sind.
- Keine Feld-Typen, die sich nur durch Farbe unterscheiden.
- Keine Items, deren Icons bei Miniaturgröße ineinander übergehen.
- Keine generischen Formen ohne Wiedererkennungswert (Standard-Kugel, Standard-Quader) für zentrale Objekte.

#### 3.4.3 Beispiele

- Koko (Panda) ist in Miniatur sofort erkennbar: runde, schwarz-weiße Bärenform mit rosa Schleife — auch ohne Gesicht.
- Der Sternen-Shop trägt immer eine goldene Stern-Statue, die über dem Feld schwebt; man erkennt ihn auf dem ganzen Board an der Sternform, nicht an der Farbe.
- Die 8 Charaktere sind im Charakter-Auswahl-Bildschirm als Silhouetten-Reihe darstellbar, und jeder ist eindeutig zuordenbar.

### 3.5 Anti-Pfeiler (Was Party Arena NICHT ist)

Diese Ausschlüsse verhindern Scope-Creep und bewahren die Pfeiler:

1. **Kein Skill-basiertes Wettkampf-Spiel:** Party Arena ist kein E-Sport. Skill in Minispielen bringt Vorteile, aber Glück (Würfel, Karten) bleibt bestimmend. Ein geschickter Spieler gewinnt nicht immer; eine Partie mit Großeltern und Kindern bleibt spannend und freundlich. *Schützt: Sofort verständlich, Überzeichnet.*
2. **Kein textlastiges oder narrativ schweres Spiel:** Keine langen Dialoge, keine verzweigten Storys, keine Lektüre-Pflicht. Erzählung ist Deko und Moderation, nie Hindernis. *Schützt: Sofort verständlich, Interaktiv wirkend.*
3. **Keine realistische oder düstere Ästhetik:** Keine fotorealistischen Shader, keine Horror- oder Gewalt-Elemente, keine düsteren Farbwelten. *Schützt: Überzeichnet.*
4. **Keine P2W- oder Echtgeld-Mechaniken:** Kein Kaufen von Vorteilen, keine Lootboxen, keine zeitbasierten Sperren. Der Fork übernimmt die STP-Politik der vollständigen Offline-/Lokal-Spielbarkeit. *Schützt: Sofort verständlich, Fairness.*
5. **Kein 30-Sekunden-Minispiel, das länger dauert:** Dauer und Komplexität der Minispiele sind hart gedeckelt; kein Minispiel erfordert vorheriges Üben oder Regelstudium. *Schützt: Sofort verständlich, Zugänglichkeit.*

### 3.6 Konfliktlösung zwischen Pfeilern

Pfeiler können in Spannung geraten (z. B. "Überzeichnete Animation" gegen "Sofort verständlich", wenn ein Effekt zu lang dauert). Es gilt eine feste Prioritätsreihenfolge:

1. **Sofort verständlich** hat immer Vorrang: Wenn eine Entscheidung Verständnis gefährdet, wird sie abgelehnt oder vereinfacht, auch wenn sie einen anderen Pfeiler besser bedienen würde.
2. Danach gilt **Interaktiv wirkend** vor **Überzeichnet** vor **Wiedererkennbar**: Lebendigkeit schlägt Stil, Stil schlägt Wiedererkennung, aber Wiedererkennung darf nie unter die Schwelle von 3.4.1 fallen.
3. Zusätzlich gilt die **Sekundär-Regel:** Wenn zwei Optionen die Pfeiler gleich gut bedienen, gewinnt die Option mit geringerer Implementierungskomplexität (schützt den Produktionsumfang).

Jede Entscheidung, die einen Pfeiler verletzt, um einen anderen zu stärken, muss im Review-Log des betroffenen Kapitels dokumentiert werden (siehe `bible-index.md`, Regel 3.1.2).

### 3.7 Der 2-Minuten-Test (Qualitätsprotokoll)

Der 2-Minuten-Test ist das verpflichtende Prüfprotokoll für Pfeiler 1 (und indirekt alle anderen):

1. **Szenario A (Neuling):** Eine Person, die Party Arena nie gesehen hat, beobachtet eine laufende Partie für 2 Minuten. Danach muss sie ohne Nachfragen sagen können: (a) wer dran ist, (b) was dieser Spieler tun soll, (c) wozu Münzen und Sterne dienen.
2. **Szenario B (Erstzug):** Dieselbe Person spielt einen eigenen Zug. Sie muss ohne Hilfe erkennen, welche Aktion möglich ist (würfeln), und die Konsequenz ihres Würfels verstehen.
3. **Szenario C (Miniatur):** In Split-Screen-Darstellung (8 Spieler, kleine Ansichten) werden alle Spieler, der aktive Spieler und der Sternen-Shop korrekt identifiziert.
4. **Auswertung:** Besteht ein Szenario nicht, ist die verantwortliche Mechanik/UI zu überarbeiten, bevor sie als "fertig" gilt. Der Test wird in jedem Playtest mit mindestens einer Testperson ausgeführt und im Review-Log dokumentiert.

## 4. Formulas

### 4.1 Pfeiler-Score für Design-Entscheidungen

Bei strittigen Entscheidungen wird jede Option `x` anhand eines gewichteten Pfeiler-Scores bewertet:

`P(x) = 4·v₁(x) + 3·v₂(x) + 2·v₃(x) + 1·v₄(x)`

mit:
- `v₁(x)` = Erfüllungsgrad "Sofort verständlich" (0 = verletzt den Pfeiler, 1 = erfüllt ihn voll),
- `v₂(x)` = Erfüllungsgrad "Interaktiv wirkend" (0–1),
- `v₃(x)` = Erfüllungsgrad "Überzeichnet statt realistisch" (0–1),
- `v₄(x)` = Erfüllungsgrad "Wiedererkennbar" (0–1).

Gültigkeitsbereich: `v ∈ [0,1]`, ganzzahlige Zwischenschritte (0; 0,5; 1) reichen für die Dokumentation. `P(x)` liegt damit in `[0,10]`.

- **Entscheidungsregel:** Gewählt wird die Option mit dem höchsten `P(x)`.
- **Veto-Regel:** `v₁(x) = 0` ist ein Veto — eine Option, die "Sofort verständlich" verletzt, wird **nie** gewählt, unabhängig von `P(x)`.
- **Beispiel:** Option A (kurze, klare Würfel-Animation): `v₁=1, v₂=1, v₃=0,5, v₄=1` → `P = 4+3+1+1 = 9`. Option B (lange, filmreife Würfel-Sequenz): `v₁=0, v₂=1, v₃=1, v₄=1` → `P = 0+3+2+1 = 6`, außerdem Veto wegen `v₁=0`. Gewählt wird A.

### 4.2 Silhouetten-Prüfwert

`S(x) = e_identifiziert / e_gesamt × 100`, wobei:
- `e_gesamt` = Anzahl der Testpersonen,
- `e_identifiziert` = Anzahl der Testpersonen, die das Objekt `x` in reiner Silhouette und in Miniatur (≤ 64 px Höhe) korrekt benennen.

- Akzeptanzregel: Für Charaktere, Items, Feld-Icons und Insel-Logos muss `S(x) ≥ 90` gelten. `S(x) < 90` bedeutet: Silhouette überarbeiten.

### 4.3 Feedback-Latenz

`F = t_aktion − t_anzeige`, wobei:
- `t_aktion` = Zeitpunkt der Spieler-Eingabe,
- `t_anzeige` = Zeitpunkt der ersten sichtbaren/hörbaren Bestätigung.

- Zielwert: `F ≤ 0,5 s` für alle primären Interaktionen (Pfeiler 3, Regel 3.3.1.1). Werte über 0,5 s werden als Tuning-Knob-Defekt behandelt.

### 4.4 Farbeindeutigkeit

`C = Anzahl der Signaturfarben / Anzahl der Charaktere = 8/8 = 1,0` (sowie analog für Inseln: 7/7 + Zitadelle).

- Akzeptanzregel: Zwei verschiedene Charaktere (bzw. Inseln) dürfen in ihrem dominanten Farbwert (Hue) nicht weniger als `ΔHue = 30°` auseinanderliegen. Dies wird in `world-overview.md` bzw. `characters-overview.md` je Insel/Charakter dokumentiert.

## 5. Edge Cases

1. **Pfeiler-Konflikt ohne klare Rangfolge:** Falls eine Entscheidung durch die Rangfolge (3.6) nicht eindeutig entschieden wird (z. B. beide Optionen gleichwertig `P`), greift die Sekundär-Regel (geringere Implementierungskomplexität). Bleibt es unklar, entscheidet der Creative Director; die Entscheidung wird im Review-Log dokumentiert.
2. **Neue Mechanik, die das Verständnis gefährdet:** Wird eine neue Mechanik vorgeschlagen, die den 2-Minuten-Test nicht besteht, wird sie nicht verworfen, sondern zerlegt: Sie wird in verständliche Teilschritte aufgeteilt, oder sie wird als späte, optionale Mechanik (z. B. ab Runde 5) eingeführt, wo der Spieler bereits gefestigt ist. Erst wenn beide Pfade scheitern, wird sie gestrichen.
3. **Legacy-Inhalte aus Super Tux Party:** STP-Mechaniken (Nolok, GNU, Sara-Moderation) werden nicht 1:1 übernommen. Sie werden entweder umgedeutet (Ereignis-Felder übernehmen Nolok-/GNU-Effekte ohne die Charaktere) oder entfernt. Jede Übernahme muss die Rebranding-Prüfung aus `glossary.md` bestehen.
4. **Farben bei Farbblindheit:** Da Feld-Typen und Charaktere über Farbe *und* Form unterscheidbar sind (3.4.1.4), ist der Ausfall einer einzelnen Farbe kein Blocker. Geprüft wird mit den drei häufigen Farbblindheits-Simulationen (Protanopie, Deuteranopie, Tritanopie) — mindestens 5 Szenen pro Insel.
5. **Übertreibung vs. Spieldauer:** Eine überzeichnete Animation darf den Spielfluss nicht bremsen. Alle nicht-interaktiven Animationen haben ein Zeitbudget (Standard ≤ 3 s); Überschreitungen sind mit einem Tuning-Knob belegbar (siehe 7).
6. **Wiedererkennbarkeit bei 8 Spielern im Split-Screen:** Bei 8 gleichzeitig sichtbaren Charakteren in kleinen Ansichten wird die Signaturfarbe zusätzlich durch Form (Kopf-Silhouette) und Namensschild gestützt. Verwechslungsgefahr wird mit dem Silhouetten-Prüfwert `S(x) ≥ 90` in Split-Screen-Größe gemessen.
7. **Idle-Belebung vs. Ablenkung:** Die lebendige Welt (3.3.1.4) darf nicht vom aktiven Spielzug ablenken. Hintergrund-Animationen bleiben in Helligkeit, Bewegungstempo und Sättigung unterhalb des aktiven Spielgeschehens (Design-Regel "Vordergrund darf Vorder- sein").
8. **ArenaStar-Moderation bei 8 Spielern:** Kommentare dürfen den Spielzug nicht verzögern. ArenaStar-Reaktionen laufen parallel zur nächsten Eingabemöglichkeit oder sind überspringbar; sie blockieren nie länger als 3 Sekunden die Eingabe.

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `vision-pillars.md` | Art | Verwendung |
|----------------------------------|-----|------------|
| `design/gdd/game-concept.md` | Quelle | Liefert die vier Designprinzipien (Abschnitt "Designprinzipien"), die hier zu prüfbaren Regeln ausgebaut werden. |
| `design/gdd/glossary.md` | Peer | Definiert Begriffe wie "Silhouette", "Signaturfarbe", "Mikro-Feedback", auf die dieser Text verweist. |
| `design/gdd/world-overview.md` | Nachgeordnet | Muss die Insel-Farbidentitäten (Farbwerte, Formsprache) gemäß Pfeiler 4 spezifizieren. |
| `design/gdd/characters-overview.md` | Nachgeordnet | Muss die Charakter-Silhouetten und Signaturfarben gemäß Pfeiler 4 spezifizieren. |
| `.claude/rules/design-docs.md` | Regelwerk | Definiert den 8-Sektionen-Standard, dem auch dieses Dokument folgt. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| Alle Gameplay-Kapitel (Core Loop, Board & Fields, Items, Minigames) | Müssen die Pfeiler in ihren Regeln spiegeln (z. B. Mikro-Feedback-Pflicht in jedem Feld-Effekt). |
| UI/UX-Kapitel (`ui-*.md`) | Müssen die 2-Minuten-Test-Kriterien und die Interaktivitäts-Regeln (3.3) einhalten. |
| World- und Character-Kapitel | Müssen Silhouetten- und Farbregeln (3.4) für ihre Objekte konkretisieren. |
| Audio-Kapitel (`audio-*.md`) | Müssen die Feedback-Pflicht (0,5 s-Latenz) und den Cartoon-Ton unterstützen. |
| Art-Assets (nicht GDD) | Jedes Asset (3D-Modell, Sprite, Icon) muss die Silhouetten- und Sättigungsvorgaben erfüllen. |

### 6.3 Bidirektionalität

Die Pfeiler sind das Dach: Sie spezifizieren "was" für alle Kapitel, und jedes Kapitel liefert der Pfeiler-Definition Rückmeldung durch konkrete Beispiele und, falls nötig, durch dokumentierte Ausnahmen. Wird in einem Kapitel eine Ausnahme von einem Pfeiler nötig, wird sie in diesem Dokument in Sektion 5 als Edge Case ergänzt oder als Design-Entscheidung vermerkt.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Gewichte `w₁…w₄` in Formel 4.1 | Kurve | `w₁≥w₂≥w₃≥w₄`, Summe ≤ 10 | `4,3,2,1` | Steuert die Priorität der Pfeiler bei Entscheidungen. |
| Feedback-Latenz `F` | Feel | 0,10–0,50 s | ≤ 0,50 s | Bestimmt die gefühlte Reaktivität jeder Interaktion. |
| Silhouetten-Schwelle `S` | Gate | 75–100 % | ≥ 90 % | Definiert, ab wann ein Objekt als "wiedererkennbar" gilt. |
| Animations-Zeitbudget nicht-interaktiver Szenen | Feel | 1–5 s | ≤ 3 s | Begrenzt Überzeichnung, damit sie den Spielfluss nicht bremst. |
| ArenaStar-Blockierzeit | Gate | 0–5 s | ≤ 3 s | Maximale Dauer, die ArenaStar die Eingabe blockieren darf. |
| Farbabstand `ΔHue` | Kurve | ≥ 30° | ≥ 30° | Sichert minimale Unterscheidbarkeit der Signaturfarben. |
| 2-Minuten-Test-Stichprobe | Kurve | 1–5 Testpersonen | 1 | Mindestanzahl neuer Testpersonen pro Playtest für den 2-Minuten-Test. |

Änderungen an den Gewichten oder Schwellen sind nur mit dokumentierter Begründung zulässig und müssen im Review-Log festgehalten werden, da sie alle nachgelagerten Kapitel beeinflussen.

## 8. Acceptance Criteria

Ein QA-Tester (oder ein Playtest-Moderator) kann folgende Prüfungen ausführen:

1. **2-Minuten-Test Szenario A:** Eine Testperson ohne Vorkenntnisse beobachtet 2 Minuten eine laufende Partie und beantwortet danach korrekt: (a) wer dran ist, (b) was zu tun ist, (c) wozu Münzen und Sterne dienen. PASS/FAIL.
2. **2-Minuten-Test Szenario B:** Eine Testperson ohne Vorkenntnisse absolviert einen eigenen Zug und erkennt ohne Hilfe Würfel-Aktion und Wurf-Konsequenz. PASS/FAIL.
3. **2-Minuten-Test Szenario C:** In einem 8-Spieler-Split-Screen identifiziert eine Testperson alle Charaktere, den aktiven Spieler und den Sternen-Shop korrekt. PASS/FAIL.
4. **Silhouetten-Test:** Alle 8 Charaktere, alle 6 Item-Icons, alle 7 Feld-Icons und alle 7 Insel-Logos erreichen `S(x) ≥ 90` in reiner Silhouette und ≤ 64 px Höhe. PASS/FAIL.
5. **Farbabstand:** Die dominanten Hue-Werte der 8 Signaturfarben und der 7 Insel-Farbwelten liegen jeweils ≥ 30° auseinander (Formel 4.4). PASS/FAIL.
6. **Feedback-Latenz:** Bei 20 Stichproben primärer Interaktionen (würfeln, kaufen, Item nutzen, Pfad wählen) beträgt `F ≤ 0,5 s`. PASS/FAIL.
7. **Animations-Budget:** Keine nicht-interaktive Animation überschreitet 3 s; keine ArenaStar-Blockade überschreitet 3 s. PASS/FAIL.
8. **Farbblindheit:** 5 ausgewählte Szenen pro Insel bleiben unter Protanopie-, Deuteranopie- und Tritanopie-Simulation funktional (Feld-Typen und Charaktere über Form/Icon unterscheidbar). PASS/FAIL.
9. **Anti-Pfeiler-Einhaltung:** Kein Review-Log und keine Kapitel-Entscheidung führt dauerhaft zu P2W-, Echtgeld-, Skill-lastigen oder textlastigen Mechaniken; Verstöße sind als Blocker zu behandeln. PASS/FAIL.
10. **Erlebbar (Experiential):** Playtest-Gruppen (mindestens 4 Personen, gemischte Spielerfahrung) bewerten die Partie im Schnitt als "sofort verständlich" und "lebendig" (Skala 1–5, Zielmedian ≥ 4). PASS/FAIL.
