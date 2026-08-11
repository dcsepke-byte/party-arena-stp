# Party Arena — Game Concept

**Engine:** Godot 4 (Super Tux Party Fork)
**Status:** Finales Konzept, Grundlage für CCGS-Entwicklung

## Elevator Pitch

> Bis zu 8 Arenians würfeln sich durch die Inseln von Aethonia, gewinnen Münzen in verrückten Minispielen und kaufen davon Sterne. Nach 8–10 Runden gewinnt, wer die meisten Sterne hat.

## Kern-Entscheidungen

| Entscheidung | Wert |
|---|---|
| Spieldauer | 8–10 Runden, 20–30 Min |
| Spielerzahl | 2–8 |
| Siegbedingung | Meiste Sterne nach letzter Runde + Bonus-Sterne |
| Feld-Anzahl | 40 Felder Hauptpfad |
| Stern-Kauf | 20 Münzen am Sternen-Shop, wandert nach Kauf |
| Catch-up | Ereignis-Felder, Bonus-Sterne, Verlierer-Boost |
| Minispiel-Dauer | ~30 Sekunden |
| Art-Style | Cartoon, Toy-like, High Saturation, keine realistischen Texturen |

## Welt: Aethonia

Magischer Kontinent, Bewohner lieben Wettkämpfe. 7 schwebende Inseln + Sternenzitadelle:

| # | Insel | Thema | Farben |
|---|---|---|---|
| 1 | Sonnenstrand | Urlaub & Wasser | Türkis, Sandgelb, Korallenrot |
| 2 | Zuckerwald | Süßigkeiten | Rosa, Schokobraun, Mintgrün |
| 3 | Wolkenwerk | Schwebende Himmel | Hellblau, Weiß, Regenbogen |
| 4 | Frostgipfel | Eis & Schnee | Eisblau, Weiß, Violett |
| 5 | Dschungeltempel | Ruinen | Dschungelgrün, Gold, Braun |
| 6 | Mechanik-Stadt | Spielzeug-Technik | Silber, Orange, Gelb |
| 7 | Sternenzitadelle | Finale | Gold, Tiefblau, Magenta |

## Charaktere (8 Arenians)

| Name | Typ | Heimat | Persönlichkeit | Farbe |
|---|---|---|---|---|
| Brix | Stein-Golem | Mechanik-Stadt | mutig, tollpatschig | Orange #ff6a00 |
| Nixie | Axolotl | Sonnenstrand | neugierig, wasseraffin | Türkis #00f0ff |
| Pip | Flieg. Eichhörnchen | Wolkenwerk | schnell, frech | Gelb #ffd34e |
| Koko | Panda | Zuckerwald | freundlich, stark | Rosa #ff4d6d |
| Tiko | Vogel | Dschungeltempel | chaotisch, lustig | Grün #2bffb9 |
| Bolt | Roboter | Mechanik-Stadt | logisch, präzise | Blau #3a86ff |
| Bloom | Kaktus | Dschungeltempel | ruhig, humorvoll | Lila #7b2ff7 |
| Momo | Waschbär | Frostgipfel | clever, trickreich | Pink #ff3cac |

## Spielmechanik (Runden-Ablauf)

Für jeden Spieler: Würfeln (1–6) → Ziehen → Feld-Effekt → (nach allen Zügen) Minispiel → Stern-Phase.

## Feld-Typen (40er-Pfad)

| Typ | Anzahl | Effekt |
|---|---|---|
| Start | 1 | Alle beginnen hier |
| Sternen-Shop | 2–3 | Stern kaufen (20 Münzen), wandert |
| Item-Shop | 2 | Item kaufen |
| Ereignis | 5–6 | Zufalls-Effekt |
| Glück/Pech | 3 | Münzen +/- |
| Münz-Bonus | 4 | Bonus-Münzen |
| Mini-Spiel | Rest | löst Minispiel aus |

## Items

Glücks-Würfel (5, 1–10), Stern-Teleporter (8), Schutzschild (6), Münz-Magnet (4), Dieb-Handschuh (10).

## Minispiele (Kategorien)

Geschicklichkeit, Reaktion, Puzzle/Logik, Rechnen/Wort, Kooperation. ~30 Sek., Platzierungen → Münzen.

## Maskottchen

ArenaStar — leuchtender Stern mit Krone, moderiert, erklärt Regeln, verteilt Belohnungen.

## Designprinzipien

1. Sofort verständlich
2. Überzeichnet statt realistisch
3. Interaktiv wirkend
4. Wiedererkennbar

## Arbeitsteilung

- **Danny:** Vorgaben, Design, zeichnet Welt/Figuren/Tiles (Aseprite)
- **Hermes/CCGS:** Spielkonzept, komplette Programmierung (Mechanik, Server, Minispiele, Karten)
