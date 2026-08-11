# ArenaStar — Party Arena Game Bible

> **Teil:** IX — Narrative (9.2)
> **Status:** Geschrieben
> **Stand:** 2026-08-11
> **Quelle:** design/gdd/game-concept.md, design/gdd/glossary.md, design/gdd/narrative-overview.md, design/gdd/vision-pillars.md

---

## 1. Overview

ArenaStar ist **der unbestrittene Star der Party Arena** — das Maskottchen, der Gastgeber und die zentrale narrative Figur des Spiels. Er ist ein leuchtender, goldener Stern mit schwebender Krone, der seit Äonen die Wettkämpfe auf Aethonia moderiert. Er ersetzt das Legacy-Maskottchen aus Super Tux Party vollständig (`glossary.md`, Legacy-Umbenennungstabelle) und ist der einzige wiederkehrende Charakter, der in jeder Partie präsent ist. ArenaStar ist der **narrative Anker** aus `narrative-overview.md` §1: Er erklärt Regeln, moderiert Minispiele, kommentiert Ereignisse, führt durch die Shops, feiert Erfolge, tröstet bei Pech und krönt den Sieger.

Seine Persönlichkeit ist die eines **charismatischen, unermüdlich positiven Showmasters**: Er feuert alle Spieler an, nie nur den Führenden, wird nie ungeduldig und findet für jeden Moment den passenden Kommentar. Er ist **allwissend über Aethonia** (`narrative-overview.md` §3.2.3) — die Stimme der Welt, die Spielfakten und Weltgeschichten frei verbindet.

ArenaStar ist ausdrücklich **kein Companion**: Er sitzt nicht auf der Schulter eines Spielers und begleitet niemanden individuell. Er moderiert die **gesamte Show** und gehört damit allen gleichermaßen. Dieses Kapitel spezifiziert Identität, Persönlichkeit, Rollen, Sprechweise, emotionale Bandbreite, das 3D-Modell, den Dialog-Vertrag und die Tuning-Parameter des Maskottchens.

## 2. Player Fantasy

ArenaStar erzeugt das Gefühl, **auf der Bühne einer großen, fröhlichen Spielshow zu stehen**. Der Spieler ist nicht bloß Teilnehmer einer Brettspiel-Partie, sondern Gast einer Show, deren Gastgeber ihn namentlich begrüßt, seine Erfolge bejubelt und seine Momente kommentiert. Die zentrale emotionale Versprechung lautet: **"Egal, ob du führst oder zurückliegst — du gehörst dazu, und es ist schön, dich hier zu haben."**

Konkret soll der Spieler erleben:

1. **Willkommen sein:** ArenaStar begrüßt jede Episode, nennt die Insel und sorgt für einen festlichen Einstieg.
2. **Gefeiert werden:** Ein Stern-Kauf, ein Minispiel-Sieg oder ein glückliches Ereignis werden sichtbar und hörbar bejubelt — für **jeden** Spieler, auch für den Letztplatzierten.
3. **Getröstet werden:** Bei Pech gibt es Mitgefühl, nie Schadenfreude. Der Ton ist: "Schade — aber die nächste Runde kommt bestimmt!"
4. **Orientierung haben:** ArenaStar erklärt Regeln beim ersten Auftreten (Tutorial Light) und kündigt an, was als Nächstes passiert. Er macht das Spiel **sofort verständlich** (Pillar, `vision-pillars.md`), ohne dass es sich wie Unterricht anfühlt.
5. **Nie gedrängt werden:** ArenaStar sagt nie "Beeil dich!". Bei langem Zögern macht er eine sanfte, liebevolle Bemerkung, die zum Lachen bringt statt zu hetzen.

Für Erwachsene ist ArenaStar die **personifizierte gute Laune der Show** — eine liebevoll übertriebene Moderator-Figur (Pillar "Überzeichnet"), deren positive Energie ansteckt. Für Kinder ab 6 ist er ein verlässlicher, freundlicher Begleiter der Show, dessen Sätze kurz, klar und vorhersehbar sind.

## 3. Detailed Rules

### 3.1 Identität und Kernaussage

1. **Was er ist:** Ein leuchtender, goldener Stern mit schwebender Krone. Er ist eine Show-Figur, keine Gottheit, kein Magier und kein Lehrer — aber er ist der lebende Mittelpunkt der Arena und von Aethonia.
2. **Kernaussage:** **"Ich bin die Party Arena. Willkommen bei der besten Show aller Zeiten — deiner!"** ArenaStar existiert, um Wettkämpfe zu feiern und alle Teilnehmer glänzen zu lassen.
3. **Alter/Ewigkeit:** Er moderiert "seit Äonen". Diese Ewigkeit erklärt seine Allwissenheit und seine Gelassenheit — er hat schon unzählige Wettkämpfe gesehen, aber jede einzelne Episode feiert er, als wäre es die erste.
4. **Verhältnis zur Welt:** ArenaStar wohnt auf der Sternenzitadelle (`glossary.md`, "Sternenzitadelle") und wacht über die "ewige Flamme des Wettkampfs". Von dort fliegt er zu jeder Insel, um Episoden zu moderieren.
5. **Marken-/IP-Status:** ArenaStar ist Eigen-IP und ersetzt das STP-Maskottchen vollständig (kein Legacy-Element bleibt aktiv; siehe `technical-fork-strategy.md` und `glossary.md` §3.3).

### 3.2 Persönlichkeit (verbindliche Charakterzüge)

| # | Charakterzug | Regel | Erlaubt | Verboten |
|---|--------------|-------|---------|----------|
| 1 | Charismatischer Showmaster | ArenaStar führt die Show mit Wärme und Energie; er ist der Grund, warum sich das Spiel wie eine Show anfühlt. | Große Gesten, Jubel, feierliche Ansagen | Blasse, monotone Moderation |
| 2 | Immer positiv | Jede Aussage hat einen positiven oder versöhnlichen Kern. | "Weiter so!", "Das wird noch!", "Stark!" | Negativismus, Miesmacherei |
| 3 | Niemals sarkastisch oder gemein | Es gibt keine versteckte Bosheit, keine Spitzen und keine ironische Herabwürdigung. | Ehrliche Begeisterung | Sarkasmus, Ironie auf Spielerkosten, bissige Bemerkungen |
| 4 | Feuert ALLE Spieler an | Er kommentiert Erfolge und Pech **jedes** Spielers, nicht nur des Führenden. | Jubel für jeden Spieler; Trost für jeden Rückstand | Einseitige Favorisierung |
| 5 | Hat für jeden Moment einen Kommentar | Jede Spielphase hat passende, vorproduzierte Kommentare (Katalog in 3.8). | Treffende, kurze Kommentare | Stille bei wichtigen Momenten (Stern-Kauf, Sieg, großes Pech) |
| 6 | Wird nie ungeduldig | Es gibt keinen Zeitdruck in Worten. "Beeil dich!" und ähnliche Formulierungen sind verboten. | Geduldige Aufforderungen | "Beeil dich!", "Na endlich!", Seufzen, Augenrollen |
| 7 | Sanfte Scherze bei langem Zögern | Nach einer definierten Wartezeit darf ArenaStar eine **liebevolle**, nie hetzende Bemerkung machen. | "Ich zähle die Sterne, bis du bereit bist ..." | Hetze, Druck, Beschämung |
| 8 | Allwissend über Aethonia | ArenaStar kennt jede Insel, jeden Bewohner, jede Geschichte. Er darf Fakten frei einstreuen. | Welt-Fakten in Kommentaren, Lade-Fakten | Falschaussagen über die Welt (Kontinuitätsfehler) |

**Verbindliche Konsequenz von Zug 6 und 7:** Die Eingabe wird durch ArenaStar **nie** blockiert oder zeitlich erzwungen. Seine Scherze sind rein auditiv/textuell und laufen parallel zur weiterhin möglichen Eingabe (siehe 3.3.7 und Formel 4.5).

### 3.3 Rolle im Spiel

ArenaStar hat genau **sieben** klar abgegrenzte Rollen. Jede Rolle definiert, wann und wie er auftritt:

**Rolle 1 — Tutorial Light (Regeln erklären):**
1. Beim **ersten Auftreten** einer Mechanik (Würfeln, Feld-Effekt, Item, Stern-Kauf, Minispiel) erklärt ArenaStar sie in einem kurzen Satz.
2. Die Erklärung folgt dem Muster "Was passiert + Was du tun kannst": z. B. "Du würfelst! Je höher die Zahl, desto weiter geht's!"
3. Er erklärt **durch Spielen**, nicht durch Vortrag (`vision-pillars.md`, "Regeln durch Beispiele"). Es gibt kein separates Tutorial-Menü.
4. Wiederholungen derselben Mechanik in späteren Partien werden **nicht** erneut erklärt (oder nur auf Anforderung); die Erklär-Logik merkt sich, was bereits erklärt wurde (Persistenz in `technical-data-structures.md`).

**Rolle 2 — Minispiel-Moderation:**
1. **Ankündigung:** ArenaStar kündigt das Minispiel an (Name, Kategorie, Intro, 5 s gemäß `core-loop.md` §3.4).
2. **Countdown:** Er zählt den Minispiel-Start herunter ("3, 2, 1 ... los!") in energetischer Tonlage.
3. **Ergebnis:** Er verkündet die Platzierung, gratuliert dem/den Siegern und feuert alle anderen an.
4. **Team-Modus:** Bei 2v2/1v3-Teams gratuliert er Teams, nicht Einzelpersonen, und betont den Zusammenhalt.

**Rolle 3 — Event-Kommentar:**
1. Beim Auslösen eines Ereignis-Felds kommentiert ArenaStar das Ereignis (Text-Vertrag in `narrative-flavor.md` §3.4: Name + Kommentar + Beschreibung).
2. Positive Ereignisse feiert er, negative rahmt er humorvoll-tröstlich ("Oh-oh! Aber Kopf hoch!"). Nie lacht er über den betroffenen Spieler.

**Rolle 4 — Shop-Führung:**
1. **Sternen-Shop:** ArenaStar begrüßt den Spieler am Sternen-Shop und erklärt den Stern-Kauf ("20 Münzen, ein Stern — ein fairer Tausch!").
2. **Item-Shop:** Er stellt die angebotenen Items kurz vor und kommentiert den Kauf ("Ein Schutzschild! Gute Wahl!").
3. Er tritt als **physisches Modell** an den Shop-Punkten auf (3.6) und verlässt den Punkt nach Abschluss des Kaufs wieder.

**Rolle 5 — Siegerehrung (Krönung):**
1. Nach der Endabrechnung (`victory-conditions.md`) krönt ArenaStar den Sieger mit einer feierlichen Ansage und der Siegerpose-Inszenierung (`characters-overview.md` §3.8).
2. Er gratuliert **allen** Spielern nach Platzierung, mit besonderem Trost für den letzten Platz, der nie bloßgestellt wird.
3. Verabschiedung mit der Catchphrase "Bis zum nächsten Mal, Arenianer!" (`narrative-flavor.md`-Vokabular, siehe 3.4.4).

**Rolle 6 — Physische Board-Präsenz:**
1. ArenaStar erscheint als **3D-Modell** auf dem Board an genau drei Punkten: **Startfeld** (Anmoderation), **Sternen-Shop** (Kauf), **Minispiel-Einstieg** (Ankündigung).
2. Er fliegt **geschmeidig von Punkt zu Punkt** — er teleportiert nie (Ausnahme: schneller Szenenwechsel beim Überspringen, siehe 3.6.6).
3. Außerhalb dieser Punkte ist ArenaStar **nicht** dauerhaft auf dem Board zu sehen (kein Schwebender-Helfer hinter den Spielern).

**Rolle 7 — Reaktions-Verstärker (ohne Eingabe-Blockade):**
1. ArenaStar reagiert auf Spielmomente (Jubel bei Stern, Trost bei Pech), verstärkt aber **nicht jede Kleinigkeit** (Anti-Spam-Regel, Formel 4.4).
2. Seine Reaktionen blockieren die Eingabe nie länger als 3 Sekunden (Pillar "Interaktiv wirkend", `vision-pillars.md` §5.8).

### 3.4 Sprechweise

#### 3.4.1 Die Dialog-Formel

Jede ArenaStar-Äußerung folgt der Grundformel:

**`Anrede + Aussage + Ermutigung`**

- **Anrede:** Direkte Ansprache des Spielers (Name oder Charaktername) oder der Gruppe ("Arenianer!", "Spieler 3!").
- **Aussage:** Die Information oder der Kommentar zum Moment ("Du hast einen Stern gekauft!", "Das Minispiel beginnt!").
- **Ermutigung:** Ein positiver, nach vorn gerichteter Abschluss ("Weiter so!", "Gleich geht's weiter!", "Stark gemacht!").

**Beispiel:** "Spieler 3! Du hast einen Stern gekauft! Weiter so!"

Regeln zur Formel:
1. **Nicht jeder Satz ist dreiteilig.** Bei schnellen Kommentaren (Countdown, kurze Ereignisse) dürfen Teile entfallen (z. B. nur "Aussage + Ermutigung"). Die Formel ist der Standard, nicht ein Schema, das jede Zeile starr erfüllen muss.
2. **Anrede-Pflicht bei persönlichen Momenten:** Bei Kauf, Sieg, großem Pech und Trost wird der Spieler **namentlich** angesprochen (Name aus der Lobby oder Charaktername).
3. **Gruppen-Anrede:** Bei Phasenansagen (Minispiel-Start, Runden-Ende) spricht ArenaStar die Gruppe an ("Arenianer!").

#### 3.4.2 Vokabular

ArenaStar verwendet ein festes, positives Vokabular. Kernbegriffe (Markensprache, in `glossary.md` und `narrative-flavor.md` dokumentiert):

- **"funkelnd"** — für alles Glänzende, Schöne, Erfolgreiche.
- **"fantastisch"** — Standard-Lob.
- **"Arenianer"** — die Anrede für alle Teilnehmer und Bewohner.
- **"Sternen-stark"** — Superlativ für besondere Leistungen ("Sternen-stark gespielt!").
- Weitere Standardbegriffe: glänzend, leuchtend, großartig, wunderbar, spannend, los geht's, geschafft, weiter so.

Regeln:
1. **Keine komplizierten Wörter:** Vokabular ist auf Lesealter 6+ ausgelegt (Formel 4.6). Fachbegriffe der Mechanik (Münzen, Sterne, Item, Shop, Ereignis) sind erlaubt, weil sie ikonisch gelernt werden.
2. **Konsistenz:** Die Kernbegriffe werden nicht synonym ersetzt (kein "toll" statt "fantastisch" im selben Kontext, ohne Grund).
3. **Keine negativen Superlative:** "schrecklich", "furchtbar", "katastrophal" sind verboten; Pech wird mit "oh-oh", "hoppla", "na so was" gerahmt.

#### 3.4.3 Verbotene Ausdrücke

Die folgenden Ausdrücke sind für ArenaStar **verboten** (auch als "Scherz"):

1. **Zeitdruck:** "Beeil dich!", "Komm schon!", "Endlich!", "Na also!", "Wie lange noch?"
2. **Herabsetzung:** "Zu langsam", "Das war nichts", "Du schaffst es nie", jede Form von Spott über Spieler.
3. **Sarkasmus/Ironie:** Jede Aussage, die das Gegenteil des Gesagten meint und auf Spielerkosten geht.
4. **Gewalt/Konflikt:** Die Begriffe aus `narrative-overview.md` §3.7 (besiegen, kämpfen, Feind, Rache).
5. **Gönnerhaftigkeit:** "Nicht schlecht für dich", "Immerhin".

#### 3.4.4 Catchphrases

ArenaStar hat **vier** feste Catchphrases mit definiertem Einsatz:

| Catchphrase | Einsatz | Häufigkeit |
|-------------|---------|------------|
| "Willkommen in der PARTY ARENA!" | Anmoderation jeder Episode | 1× pro Episode (bei aktivem Intro) |
| "Würfeln, Ziehen, Gewinnen!" | Übergang zur Zug-Phase, Rundenbeginn | max. 1× pro Runde |
| "Jeder Stern zählt!" | Stern-Phase, nach Stern-Kauf oder bei Rückstand | max. 1× pro Runde |
| "Bis zum nächsten Mal, Arenianer!" | Verabschiedung nach der Siegerehrung | 1× pro Episode |

Regeln:
1. Catchphrases werden **nicht** aneinandergereiht (max. eine pro Phase).
2. Sie dürfen lokalisiert **sinngleich** übersetzt werden, bleiben aber als Markensprache erkennbar.
3. Wiederholungs-Schutz: Dieselbe Catchphrase erscheint nie zweimal innerhalb von 3 Minuten (außer bei sehr langen Runden, dann max. 1× pro Runde).

### 3.5 Emotionale Bandbreite

ArenaStar hat sechs definierte Emotions-Zustände. Jeder Zustand hat einen Auslöser, eine Tonlage und eine minimale Textmenge (Katalog-Anforderung in 3.8):

| # | Emotion | Auslöser | Tonlage | Beispielzeile |
|---|---------|----------|---------|---------------|
| 1 | **Begeistert** (Standard) | Reguläre Moderation, Ansagen, Jubel | warm, energiegeladen, laut | "Fantastisch! Was für ein Zug!" |
| 2 | **Überrascht** (!) | Unerwartetes Ereignis, hoher Würfelwurf, Überraschungs-Comeback | aufgeregt, höher, schneller | "Wow! Das habe ich nicht kommen sehen!" |
| 3 | **Mitfühlend** | Pech, Münzverlust, Diebstahl, Minispiel-Niederlage | leise, warm, tröstlich | "Oh-oh. Aber Kopf hoch, Arenianer! Gleich geht's weiter!" |
| 4 | **Feierlich** | Stern-Kauf, Minispiel-Sieg, Siegerehrung | getragen, festlich, groß | "Spieler 3! Ein Stern! Jeder Stern zählt!" |
| 5 | **Ermutigend** | Rückstand, letzter Platz, Comeback-Situation | zuversichtlich, ruhig, stützend | "Du liegst zurück — aber die Show ist noch nicht vorbei!" |
| 6 | **Energetisch** | Minispiel-Countdown, Renn-Momente, Endspurt | sehr schnell, laut, rhythmisch | "3, 2, 1 ... LOS!" |

Regeln:
1. **Standard ist Begeistert.** Alle anderen Zustände sind temporäre Abweichungen für den jeweiligen Moment und kehren danach zum Standard zurück.
2. **Mitfühlend darf nie in Mitleid kippen:** Es geht um Trost und Zuversicht, nicht um Bedauern ("Oh, du Ärmster" ist verboten).
3. **Ermutigend bei Rückstand wird jedem Spieler gleichwertig angeboten** — auch dem Führenden, wenn er plötzlich zurückfällt.
4. **Emotions-Wechsel sind sichtbar und hörbar:** Tonlage, Mimik (Augen), Leucht-Intensität und Musik-Feedback wechseln mit dem Zustand (3.6.5).

### 3.6 3D-Modell

#### 3.6.1 Kern-Spezifikation

| Eigenschaft | Wert |
|-------------|------|
| Objekt | Schwebender Stern mit schwebender Krone |
| Größe | **~0,5 Einheiten** Durchmesser (Schwankung ± 10 %, also 0,45–0,55) |
| Höhe über Grund | schwebt bei ~1,8 Einheiten über dem Board (deutlich über den Charakteren, die 1,2 Einheiten hoch sind) |
| Krone | schwebt **über** dem Stern (Abstand ~0,15 Einheiten), rotiert langsam und unabhängig |
| Licht | Emissive-Leuchten in Gold (`#ffd700`-Basis), Puls im Takt der Musik |
| Hände | zwei kurze "Lichtstrahlen" seitlich, zum Gestikulieren |
| Bewegung | fliegt geschmeidig von Punkt zu Punkt; keine Teleportation |

#### 3.6.2 Silhouette und Wiedererkennbarkeit

1. ArenaStar muss die **Silhouetten-Schwelle** `S(x) ≥ 90` aus `vision-pillars.md` §4.2 erfüllen: Als reiner Schattenriss (Stern + Krone) ist er auf einen Blick erkennbar und von allen Charakteren und Insel-Symbolen unterscheidbar.
2. Die **Krone** ist sein einzigartiges Markenzeichen (kein anderer Charakter trägt eine Krone). Sie darf auch in Miniatur nicht verschwinden.
3. Seine Signaturfarbe Gold ist exklusiv für ihn (keine Kollision mit Charakter- oder Insel-Farben; Farbabstand `ΔHue ≥ 30°`, `vision-pillars.md` §4.4).

#### 3.6.3 Animationen und Verhalten

| Zustand | Beschreibung |
|---------|--------------|
| `idle` | sanftes Schweben mit leichtem Auf-und-ab; Krone rotiert langsam; Licht pulsiert im Musiktakt. |
| `fly` | gleitet geschmeidig mit leichter Kurve (S-Kurve), Lichtschweif hinter sich; Ankunft mit sanftem Abbremsen. |
| `gesture` | Lichtstrahl-Hände heben sich (Jubel, Erklären); kleine Funken bei Betonung. |
| `surprised` | kurzes Aufzucken, Licht blinkt hell auf, Krone kippt leicht. |
| `sympathy` | Senken der Hände, Licht wird warm und weicher, Stern neigt sich leicht zum Spieler. |
| `celebrate` | schnelles Kreisen, helles Leuchten, Funkenregen (Stern-Kauf, Sieg). |

Regeln:
1. **Fliegen statt Teleportieren:** Jeder Ortswechsel ist eine sichtbare Flugbewegung (Dauer 0,8–1,5 s je nach Distanz). Teleportation ist nur beim **Überspringen** erlaubt (Spieler drückt Überspringen-Taste) und wird als schnelles Aufblitzen inszeniert.
2. **Musik-Takt:** Das Leuchten pulsiert mit dem Takt des Insel-Themas (Kopplung an `audio-music.md`). Bei Pause oder stummgeschalteter Musik pulsiert es mit einem Default-Takt (100 BPM).
3. **Emotions-Zustände** sind über Licht (Helligkeit, Farbe), Haltung und Hände sichtbar (3.5).

#### 3.6.4 Auftritts-Punkte auf dem Board

1. **Startfeld:** ArenaStar erscheint bei der Anmoderation, begrüßt, erklärt kurz die Insel (Flavor-Text optional) und fliegt nach dem ersten Würfelwurf davon.
2. **Sternen-Shop:** ArenaStar steht über dem aktiven Sternen-Shop-Feld, solange ein Kauf möglich ist. Nach dem Kauf (oder wenn der Spieler den Shop verlässt) fliegt er zum nächsten Einsatz.
3. **Minispiel-Einstieg:** ArenaStar erscheint zur Minispiel-Ankündigung, führt die Spieler visuell zur Arena und verschwindet beim Minispiel-Start (die Minispiel-Szene hat ihre eigene ArenaStar-Darstellung oder eine einfache Countdown-UI).

#### 3.6.5 Sichtbarkeit und Performance

1. **Split-Screen (8 Spieler):** Das 3D-Modell von ArenaStar wird nur in der **aktiven Kameraperspektive** und in Hauptansichten dargestellt; in kleinen Split-Ansichten erscheint er als Icon/Symbol oder gar nicht, um Sichtbarkeit zu erhalten (Kamera-Regeln in `ui-board.md`).
2. **Performance:** Das Modell ist low-poly (Cartoon/Toy, `vision-pillars.md` §3.2) mit einem Emissive-Material. Partikel (Funken, Lichtschweif) sind budgetiert (≤ 200 Partikel gleichzeitig, `technical-performance.md`).
3. **Zugänglichkeit (reduzierte Bewegung):** Alle Flug- und Puls-Animationen respektieren die Einstellung "reduzierte Bewegung" aus `ui-accessibility.md` (dann: langsameres Pulsieren oder statisches Leuchten, kürzere Flugstrecken).

#### 3.6.6 Kein Companion

1. ArenaStar ist **nie** dauerhaft an einen Spieler gebunden. Er folgt keinem Charakter, sitzt auf keiner Schulter und fliegt nicht neben einem Spieler her.
2. Er gehört der **gesamten Show**: Seine Präsenz ist an die definierten Auftritts-Punkte (3.6.4) und die Moderations-Momente (3.3) gebunden.
3. Ausnahme (rein visuell): In der Siegerehrung fliegt er einmalig zum Sieger, um ihn zu "krönen" (Krone-Schwebepose über dem Siegerkopf, dann zurück in die Mitte).

### 3.7 Nicht-Blockade der Eingabe

1. ArenaStar-Kommentare sind **parallel zur Eingabe** möglich. Sie blockieren die Spieler-Eingabe nie länger als 3 Sekunden (`vision-pillars.md` §5.8, Tuning-Knob "ArenaStar-Blockierzeit").
2. Alle Kommentare sind **überspringbar** (eine Taste bricht die aktuelle Zeile/Animation ab; der Spielzustand ändert sich nicht).
3. Bei **Überspringen-Wiederholungen** (Spieler drückt mehrfach) wird der Kommentar abgebrochen und **nicht erneut** getriggert, bis der nächste definierte Moment kommt (Anti-Spam, Formel 4.4).

### 3.8 Dialog-Katalog (Vertrag und Mindestumfang)

ArenaStar-Dialoge werden als **lokalisierte Textdaten** gepflegt (Dateien unter `assets/data/narrative/arena_star/*.csv` bzw. `.json`), nicht im Code. Jede Zeile hat eine stabile **ID** (z. B. `as_star_buy_01`), eine Emotions-Kategorie (3.5), einen Trigger (Kauf, Sieg, Pech, ...) und die lokalisierte Zeichenkette mit benannten Platzhaltern.

**Mindestumfang (Anzahl eindeutiger Zeilen je Kategorie):**

| Kategorie | Trigger | Mindestzeilen | Beispiel-Trigger |
|-----------|---------|---------------|------------------|
| Begrüßung | Anmoderation | 4 | "Willkommen in der PARTY ARENA!" |
| Regel-Erklärung | Tutorial Light (je Mechanik) | je Mechanik ≥ 2 | Würfeln, Bewegung, Item, Stern, Minispiel |
| Phasen-Ansage | Rundenbeginn, Minispiel, Stern-Phase | je Phase ≥ 3 | "Runde 3 von 8!" |
| Stern-Kauf | Stern gekauft | 4 | "Spieler {player_name}! Ein Stern! Jeder Stern zählt!" |
| Item-Kauf | Item gekauft | 4 | "Ein Schutzschild! Gute Wahl!" |
| Minispiel-Sieg | Spieler gewinnt Minispiel | 4 | "Fantastisch! Platz 1 für {player_name}!" |
| Minispiel-Niederlage | Spieler verliert Minispiel | 4 | "Knapp! Nächstes Mal holst du dir den Sieg!" |
| Pech | Münzverlust, negatives Ereignis | 4 | "Oh-oh! Aber Kopf hoch, {player_name}!" |
| Ermutigung | Rückstand, letzter Platz | 4 | "Du liegst zurück — aber die Show ist noch nicht vorbei!" |
| Sieg (Episode) | Gesamtsieg | 4 | "Der Champion der Party Arena ist ... {player_name}!" |
| Trost (letzter Platz) | Letzter Platz der Episode | 3 | "Letzter Platz? Pah! Hauptsache, du warst dabei!" |
| Countdown | Minispiel-Start | 3 | "3, 2, 1 ... LOS!" |
| Verabschiedung | Episodenende | 3 | "Bis zum nächsten Mal, Arenianer!" |
| Sanfter Scherz | Zögern (Timeout-Wartezeit) | 4 | "Ich zähle derweil die Sterne ..." |

**Regeln:**
1. Jede Zeile nutzt benannte Platzhalter (`{player_name}`, `{item_count}`, `{round}`), nie feste Namen.
2. Keine Zeile überschreitet das Budget aus Formel 4.2.
3. Fehlt zu einem Trigger eine Zeile, greift eine **Fallback-Zeile** (eine generische, emotions-passende Zeile je Kategorie). Fallbacks sind Pflicht (Minimum 1 je Kategorie).
4. Der konkrete Zeilenbestand wächst mit der Content-Pflege; der Katalog ist eine Vertrags-Anforderung, kein einmaliges Artefakt.

### 3.9 Sprachausgabe und Text

1. **Voice (optional):** Falls die Sprachausgabe aktiviert ist (`audio-voice.md`), werden ArenaStar-Zeilen gesprochen. Stimm-Charakter: warm, hell, übertrieben freundlich, klar artikuliert (Lesealter 6+). Ziel-Lautstärke und Format nach `audio-voice.md`.
2. **Text-Bubbles:** Unabhängig von Voice wird jede Zeile als Text-Bubble/Untertitel angezeigt (Barrierefreiheit). Voice ist Zusatz, Text ist Pflicht.
3. **Lokalisierung:** Zeilen sind lokalisationstauglich: keine Idiome, die nicht übersetzbar sind; Platzhalter statt eingebetteter Namen; Längen flexibel (Budget +20 % für Übersetzungen, `narrative-overview.md` §5.5).
4. **Wiedergabe-Queue:** Zwei ArenaStar-Zeilen werden nie gleichzeitig gespielt (Prioritäts-Queue in `audio-voice.md`); eine neue Zeile wartet, bis die aktuelle beendet oder übersprungen ist.

## 4. Formulas

### 4.1 Dialog-Formel (Struktur)

Eine reguläre ArenaStar-Zeile `Z` setzt sich aus bis zu drei Segmenten zusammen:

`Z = A ⊕ S ⊕ E`

- `A` = Anrede (Spielername, Charaktername oder Gruppen-Anrede), optional,
- `S` = Aussage/Kommentar (Pflicht),
- `E` = Ermutigung/Abschluss, optional,
- `⊕` = Verkettung mit natürlicher Interpunktion.

Erwartungswerte: In persönlichen Momenten (Kauf, Sieg, Pech) gilt `A` und `E` als Pflicht; in Phasen-Ansagen genügt `S ⊕ E`. Formel-Hinweis: `A` und `E` sind optional, aber mindestens ein positiver Abschluss (`E`) oder ein positiver Kern in `S` muss vorhanden sein (Ton-Regel "immer positiv", §3.2.2).

### 4.2 Zeilen-Längenbudget

`Länge(Z) ≤ 120 Zeichen`, `Wörter(Z) ≤ 20`, geschätzte Sprech-/Lesezeit `t(Z) ≤ 8 s` (Formel `t = W / 2,5` aus `narrative-overview.md` §4.1).

- Erwartungswert: Eine Standard-Kommentarzeile hat 8–14 Wörter (Sprechdauer 3–6 s); Erklär-Zeilen dürfen bis 20 Wörter haben. Die Catchphrase "Willkommen in der PARTY ARENA!" hat 5 Wörter / 33 Zeichen / ~2 s.
- Überschreitung: Zeilen über 120 Zeichen oder 20 Wörter sind Blocker (UI-Überlauf, `ui-overview.md`; zu lange Voice-Lines).

### 4.3 Kommentar-Frequenz (Anti-Spam)

`K_Phase ≤ 3` Kommentare pro Spielphase (Zug-Phase, Minispiel-Phase, Stern-Phase) und `K_Minute ≤ 6` Kommentare pro Minute im Schnitt.

- Erwartungswert: In einer 20-minütigen Episode (4 Spieler) erscheinen ca. 60–100 ArenaStar-Momente — genug, um die Show lebendig zu halten, ohne zu nerven.
- Grenze: Überschreitet die Dichte 8 Kommentare/Minute, werden weitere Kommentare bis zur nächsten Phase zurückgehalten.

### 4.4 Wiederholungs- und Überspring-Schutz

- **Zeilen-Wiederholung:** Dieselbe Zeile `Z` erscheint nicht zweimal innerhalb von 10 Minuten, solange mindestens eine Alternativzeile derselben Kategorie existiert. Formal: Wähle `Z_t` aus Kategorie `C`, mit `Z_t ≠ Z_{t-1}`, bevorzugt `Z` mit ältestem letzten Einsatz.
- **Überspringen:** Wird `Z` abgebrochen, gilt `Z` als "benutzt" für 10 Minuten (kein sofortiger Neu-Trigger).

### 4.5 Blockierzeit

`T_Block = t_Ende_Animation − t_Beginn_Text ≤ 3 s` für jede ArenaStar-Interaktion, die die Eingabe verzögert.

- Erwartungswert: Regel-Erklärungen und Trost-Momente blockieren 1,5–3 s; Jubel- und Kauf-Momente 0,5–1,5 s (parallel zur weiterlaufenden Eingabe).
- Grenze: Jede Blockade über 3 s wird automatisch abgebrochen (Tuning-Knob in Sektion 7).

### 4.6 Vokabular-Schwierigkeit

Für jede Zeile gelten die Lesbarkeits-Grenzen aus `narrative-overview.md` §4.3: `R ≤ 9` Wörter/Satz und `T ≤ 10 %` Wörter mit > 10 Buchstaben.

- Erwartungswert: "Willkommen in der PARTY ARENA!" hat `R = 5`, `T = 0 %` (PARTY ARENA zählt als 2 Wörter mit 5/5 Buchstaben).
- Der Markenname "PARTY ARENA" und der Eigenname "ArenaStar" sind von der Längen-Regel ausgenommen (Eigennamen zählen nicht zu `T`), müssen aber in einem Atemzug lesbar sein.

### 4.7 Emotionale Verteilung

Für den gesamten Zeilenkatalog gilt ein Mindestanteil positiver Zustände:

- `Begeistert + Feierlich + Energetisch ≥ 60 %` aller Zeilen,
- `Mitfühlend + Ermutigend ≤ 30 %`,
- `Überrascht ≤ 10 %`.

- Erwartungswert: Von 100 Katalog-Zeilen sind ≥ 60 positiv, ≤ 30 tröstlich/ermutigend, ≤ 10 überrascht. Die Verteilung stellt sicher, dass ArenaStar als "immer positiv" wahrgenommen wird (Persönlichkeitszug 2).

## 5. Edge Cases

1. **Spieler ohne vergebenen Namen:** Hat ein Spieler keinen Lobby-Namen, verwendet ArenaStar den Charakternamen ("Brix! Du hast einen Stern gekauft!"). Fehlt auch der (theoretisch nicht möglich), fällt die Anrede auf "Arenianer!".
2. **Alle 8 Spieler sind aktiv:** ArenaStar muss alle Spieler anfeuern, ohne einzelne zu bevorzugen. Die Auswahl des Kommentar-Ziels wechselt fair (Round-Robin über die Spieler; Formel in der Text-Logik). Bei Gruppen-Momenten (Minispiel) spricht er die Gruppe an, nicht Einzelne.
3. **Letzter Platz bei der Siegerehrung:** ArenaStar tröstet den letzten Platz mit einer eigenen Kategorie ("Trost letzter Platz", §3.8) — niemals mit der Sieger- oder Jubel-Zeile. Bloßstellung ist ausgeschlossen.
4. **Spieler zögert sehr lange (AFK):** Nach der definierten Wartezeit (Tuning-Knob, Standard 10 s) macht ArenaStar genau **einen** sanften Scherz (§3.2.7). Danach keine weiteren Kommentare bis zur nächsten Phase; das Spiel erwartet die Eingabe weiterhin geduldig (kein automatischer Würfelwurf durch ArenaStar im lokalen Spiel; Online-Timer-Regeln in `core-loop.md` §5.2 bleiben unberührt).
5. **Zwei Trigger gleichzeitig (z. B. Stern-Kauf und Minispiel-Sieg):** Die Text-Logik priorisiert: Sieg/Kauf (Feierlich) > Pech (Mitfühlend) > Ansage (Begeistert) > Fakt (Standard). Es wird genau eine Zeile gespielt; die zweite wird in die nächste Pause verschoben oder verworfen.
6. **Zeilen-Kategorie erschöpft (alle Zeilen in 10-Minuten-Fenster benutzt):** Es greift die **Fallback-Zeile** der Kategorie (§3.8, Regel 3). Fallbacks sind immer vorhanden und dürfen nie leer sein.
7. **Voice deaktiviert:** Alle Trigger spielen weiter als Text-Bubbles; die Text-Logik ist identisch. Kein Funktionsverlust (`audio-voice.md`).
8. **ArenaStar-Modell im Split-Screen:** In kleinen Ansichten wird das 3D-Modell nicht gerendert (Icon/kein Modell, §3.6.5.1). Die Text-Bubbles und der Audio-Kommentar laufen unabhängig davon weiter.
9. **Reduzierte-Bewegung-Einstellung:** Flug- und Puls-Animationen werden verlangsamt oder statisch dargestellt (§3.6.5.3). Text und Audio bleiben unverändert.
10. **Überspringen während einer Blockade:** Der Spieler kann jede ArenaStar-Blockade überspringen; der Spielzustand ändert sich nicht. Nach dem Überspringen wird die Zeile als "benutzt" markiert (§4.4).
11. **Kollision mit Spieler-Erklärungen:** Erklärt ArenaStar eine Mechanik, die ein Spieler bereits kennt, ist das kein Fehler — die Erklär-Logik wiederholt sie nur beim **ersten Auftreten** (§3.3 Rolle 1); Wiederholungen erfolgen nur auf Anforderung (z. B. Hilfemenü).
12. **Mehrere Shops gleichzeitig (Sternen- und Item-Shop im selben Zug):** ArenaStar moderiert **einen** Shop pro Zug in der festen Reihenfolge (zuerst der besuchte Shop). Es gibt keinen Doppel-Dialog.
13. **Farbfehlsichtige Spieler:** Das Leuchten von ArenaStar ist zusätzlich über die **Form** (Stern + Krone) erkennbar; der Emotions-Zustand wird über Form/Text zusätzlich zur Lichtfarbe kommuniziert (`ui-accessibility.md`).

## 6. Dependencies

### 6.1 Abhängigkeiten dieses Dokuments

| Benötigt von `narrative-arena-star.md` | Art | Verwendung |
|------------------------------------------|-----|------------|
| `design/gdd/narrative-overview.md` | Peer | Liefert das Episode-Modell, die Ton-Regeln, die Gewaltfreiheit und den Platzierungs-Katalog, die dieses Kapitel einhält. |
| `design/gdd/glossary.md` | Peer | Definiert ArenaStar als Begriff und die Legacy-Umbenennung des STP-Maskottchens. |
| `design/gdd/vision-pillars.md` | Peer | Liefert die Blockierzeit-Grenze (3 s), Silhouetten-Schwelle und den Anti-Pfeiler "kein textlastiges Spiel". |
| `design/gdd/characters-overview.md` | Peer | Liefert die Spieler-Repräsentation (Charaktere, Porträts), die ArenaStar in Ansprachen nutzt. |
| `design/gdd/core-loop.md` | Peer | Definiert die Phasen (Zug, Minispiel, Stern), in denen ArenaStar moderiert. |
| `design/gdd/victory-conditions.md` | Peer | Definiert die Siegerehrung, in der ArenaStar krönt und verabschiedet. |

### 6.2 Systeme, die von diesem Dokument abhängen

| System | Art der Abhängigkeit |
|--------|----------------------|
| `narrative-flavor.md` | Referenziert ArenaStar-Kommentare in Event- und Item-Texten; muss dessen Sprechweise (3.4) und Vokabular einhalten. |
| `audio-voice.md` | Steuert die Sprachausgabe (Samples, Queue) für ArenaStar-Zeilen; übernimmt die Zeilen aus dem Katalog (3.8). |
| `ui-mainmenu.md`, `ui-character-select.md`, `ui-shop.md`, `ui-board.md` | Stellen ArenaStar-Modell, Text-Bubbles und Auftritts-Punkte dar. |
| `minigame-architecture.md` | Löst die Moderation (Ankündigung, Countdown, Ergebnis) aus; die Minispiel-Szene nutzt die Countdown-Zeilen. |
| Lade-Bildschirm | Zeigt ArenaStar-Grüsse und Lade-Fakten; nutzt das Vokabular. |
| `technical-data-structures.md` | Persistiert den Erklär-Fortschritt (Tutorial Light) und den Zeilen-Katalog. |

### 6.3 Bidirektionalität

`narrative-overview.md` verweist auf dieses Kapitel (Master-Dokument), dieses Kapitel verweist zurück auf `narrative-overview.md` und `narrative-flavor.md`. Die `ui-*.md`- und `audio-*.md`-Kapitel müssen ArenaStar als Moderator referenzieren und die hier definierten Auftritts-Punkte und Zeilen-Trigger umsetzen. Wird die Sprechweise (3.4) oder der Katalog-Umfang (3.8) geändert, sind `audio-voice.md`, `narrative-flavor.md` und die UI-Kapitel synchron zu prüfen.

## 7. Tuning Knobs

| Knob | Kategorie | Gültiger Bereich | Standard | Auswirkung |
|------|-----------|------------------|----------|------------|
| Blockierzeit `T_Block` | Gate | 1–5 s | 3 s | Maximale Dauer einer ArenaStar-Interaktion, die Eingabe verzögert. Größer = mehr Inszenierung, riskiert Trägheit. |
| Kommentar-Frequenz `K_Phase` | Feel | 1–6 Kommentare/Phase | 3 | Lebendigkeit der Moderation. Höher = mehr Show, riskiert Nerven. |
| Kommentar-Frequenz `K_Minute` | Feel | 2–10/Minute | 6 | Globale Dichte; Anti-Spam-Schwelle. |
| Wartezeit bis sanfter Scherz | Feel | 5–30 s | 10 s | Nach welcher Zöger-Dauer ArenaStar eine liebevolle Bemerkung macht. |
| Zeilen-Wiederholungssperre | Kurve | 5–20 Minuten | 10 | Wie lange eine benutzte Zeile pausiert, bevor sie erneut gewählt werden kann. |
| Emotions-Verteilung (positiv/tröstlich/überrascht) | Kurve | je ± 10 % | 60/30/10 | Steuert die wahrgenommene Grundstimmung des Maskottchens. |
| Vokabular-Schwelle `T` | Kurve | 5–20 % | 10 % | Erlaubter Anteil langer Wörter; Eigennamen ausgenommen. |
| Modellgröße | Feel | 0,4–0,7 Einheiten | 0,5 | Sichtbarkeit auf dem Board; muss unter der Flughöhe und über den Charakteren bleiben. |
| Leucht-Intensität | Feel | 0,5–1,5 (Emissive-Skalierung) | 1,0 | Wie stark ArenaStar leuchtet; darf die Lesbarkeit des Boards nicht stören. |
| Modell-Präsenz im Split-Screen | Gate | `Modell` / `Icon` / `aus` | `Icon` in kleinen Ansichten | Steuert, ob das 3D-Modell in kleinen Split-Ansichten gerendert wird. |

Alle Knobs liegen in Daten- und Konfigurationsdateien (`assets/data/narrative/arena_star/`, `assets/data/` für Modell-Parameter), nicht im Code. Änderungen an `T_Block` oder `K_Phase` erfordern eine Neuvalidierung der Formeln 4.3 und 4.5.

## 8. Acceptance Criteria

Ein QA-Tester (oder CI-Hook) kann die folgenden Prüfungen ausführen (PASS/FAIL):

1. **Persönlichkeits-Regeln:** In 50 zufällig abgespielten ArenaStar-Momenten (Stichprobe über alle Kategorien) enthält keine Zeile Sarkasmus, Herabsetzung, Zeitdruck ("Beeil dich!") oder einen verbotenen Begriff aus `narrative-overview.md` §3.7. PASS/FAIL.
2. **Formel-Einhaltung:** Persönliche Momente (Kauf, Sieg, Pech) enthalten Anrede + Aussage + Ermutigung (Formel 4.1); Phasen-Ansagen enthalten mindestens Aussage + positiven Abschluss. PASS/FAIL.
3. **Zeilen-Budget:** Keine Zeile überschreitet 120 Zeichen / 20 Wörter / 8 s Sprech-/Lesezeit (4.2). PASS/FAIL.
4. **Lesbarkeit:** Für jede Zeile gilt `R ≤ 9` und `T ≤ 10 %` (4.6; Eigennamen ausgenommen). PASS/FAIL.
5. **Emotions-Verteilung:** Der Katalog erfüllt die Verteilung aus 4.7 (≥ 60 % positiv). PASS/FAIL.
6. **Katalog-Mindestumfang:** Jede Kategorie aus §3.8 hat ihre Mindestzeilenzahl plus mindestens eine Fallback-Zeile; alle Zeilen haben stabile IDs und benannte Platzhalter. PASS/FAIL.
7. **Alle Spieler werden angesprochen:** In einer simulierten 4-Spieler-Partie feiert/tröstet ArenaStar nachweislich alle Spieler (Round-Robin), nicht nur den Führenden. Beobachter-Protokoll. PASS/FAIL.
8. **Blockierzeit:** Keine ArenaStar-Interaktion blockiert die Eingabe länger als 3 s (4.5); jede Blockade ist überspringbar, ohne den Spielzustand zu verändern. PASS/FAIL.
9. **Anti-Spam:** In einer aufgezeichneten Partie überschreitet die Kommentar-Dichte nie 8/Minute und 3/Phase (4.3); dieselbe Zeile erscheint nicht zweimal innerhalb von 10 Minuten (4.4). PASS/FAIL.
10. **Sanfter Scherz bei Zögern:** Ein Testspieler wartet 10+ s bei der Würfel-Eingabe; ArenaStar macht genau einen liebevollen, nicht hetzenden Kommentar; danach keine weiteren. PASS/FAIL.
11. **3D-Modell:** Das Modell (0,45–0,55 Einheiten, schwebende Krone, Lichtstrahl-Hände) lädt in Godot 4.2 fehlerfrei; es fliegt zwischen Startfeld, Sternen-Shop und Minispiel-Einstieg (keine Teleportation im Normalbetrieb); Leuchten pulsiert im Musiktakt. PASS/FAIL.
12. **Silhouetten-Test:** ArenaStar erreicht `S(x) ≥ 90` als Schattenriss in Miniatur (Stern + Krone, `vision-pillars.md` §4.2). PASS/FAIL.
13. **Kein Companion:** In einer kompletten Partie folgt ArenaStar keinem Spieler dauerhaft; er tritt nur an den 3 Auftritts-Punkten und in Moderations-Momenten auf. PASS/FAIL.
14. **Tutorial Light:** Beim ersten Auftreten einer Mechanik erklärt ArenaStar sie in einem kurzen Satz; in späteren Partien wird dieselbe Erklärung nicht erneut automatisch gezeigt (Persistenz). PASS/FAIL.
15. **Erlebbar (Experiential):** Ein neuer Spieler (≥ 6 Jahre) kann nach einer Testrunde beschreiben, dass "der Stern" ihn angespornt und nie ausgelacht hat; Playtest-Fragebogen, Ziel: Median ≥ 4 von 5 für "ArenaStar macht die Show besser". PASS/FAIL.
