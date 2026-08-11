#!/usr/bin/env python3
"""Generiert das Party Arena Game Bible Review-Dashboard — NATIVE Version.
Verwendet NUR native HTML-Elemente, die in jedem Browser funktionieren (auch
Telegram In-Browser, der JavaScript blockiert):
- <details>/<summary> für Auf-/Zuklappen (kein JS nötig)
- Anker-Links (<a href="#section-N">) für Navigation (kein JS nötig)
- Native Checkboxen
JS nur für Fortschrittsanzeige (progressive enhancement — wenn JS blockiert
ist, funktionieren Kapitel + Abhaken trotzdem, nur ohne Fortschrittsbalken).
"""
import html
import re
from pathlib import Path

GDD_DIR = Path("/opt/data/SuperTuxParty/design/gdd")
OUT = Path("/opt/data/SuperTuxParty/design/gdd/review-dashboard.html")

# (Name, [Kapitel], ist_uebersicht)
PARTS = [
    ("📑 Übersicht", [], True),
    ("Meta", [
        ("bible-index", "Game Bible Index", "Übersicht aller Kapitel"),
        ("vision-pillars", "Vision & Pillars", "Kern-Emotionen und Spielprinzipien"),
        ("glossary", "Glossar", "Fachbegriffe und Definitionen"),
        ("systems-index", "Systems Index", "Zerlegung in Subsysteme"),
    ]),
    ("Core", [
        ("core-loop", "Kern-Loop", "Der Spiel-Rhythmus (Würfeln→Ziehen→Minispiel→Stern)", False, True),
        ("star-economy", "Star Economy", "Sterne kaufen (20 Münzen), wandern nach Kauf", False, True),
        ("dice-movement", "Würfel & Bewegung", "1-6 Würfel, Bewegung entlang des Pfads", False, True),
        ("victory-conditions", "Siegbedingungen", "Meiste Sterne + Bonus-Sterne", False, True),
        ("catch-up", "Catch-up-Mechanismen", "Verlierer-Boost, damit niemand aufgibt", False, True),
        ("coin-economy", "Münz-Wirtschaft", "Münzen verdienen und ausgeben", False, True),
    ]),
    ("Board", [
        ("board-architecture", "Board-Architektur", "40-Felder-Hauptpfad", True, True),
        ("field-start", "Start-Feld", "Alle beginnen hier"),
        ("field-star-shop", "Sternen-Shop", "Stern kaufen, wandert danach", True, True),
        ("field-item-shop", "Item-Shop", "Items kaufen"),
        ("field-event", "Ereignis-Felder", "Zufalls-Effekte"),
        ("field-luck", "Glück/Pech-Felder", "Münzen +/-"),
        ("field-coin-bonus", "Münz-Bonus-Felder", "Bonus-Münzen"),
        ("field-minigame", "Mini-Spiel-Felder", "Lösen das nächste Minispiel aus"),
    ]),
    ("Items", [
        ("item-system", "Item-System", "Grundsystem für Items", False, True),
        ("item-luckydice", "Glücks-Würfel", "(5 Münzen) Würfelt 1-10"),
        ("item-teleporter", "Stern-Teleporter", "(8 Münzen) Zum Sternen-Shop"),
        ("item-shield", "Schutzschild", "(6 Münzen) Ignoriert 1 negatives Ereignis"),
        ("item-coinmagnet", "Münz-Magnet", "(4 Münzen) +3 Münzen"),
        ("item-thiefglove", "Dieb-Handschuh", "(10 Münzen) Stiehlt 5 Münzen"),
    ]),
    ("Minigames", [
        ("minigame-architecture", "Minigame-Architektur", "Wie Minispiele integriert werden", True, True),
        ("minigame-categories", "5 Minigame-Kategorien", "Geschick, Reaktion, Puzzle, Rechnen, Koop"),
        ("minigame-rewards", "Belohnungs-System", "Platzierungen → Münzen"),
        ("minigame-template", "Minigame-Template", "Standardstruktur jedes Minispiels", False, True),
    ]),
    ("Charaktere", [
        ("characters-overview", "8 Arenians — Übersicht", "Alle spielbaren Charaktere", True, True),
        ("character-brix", "Brix (Golem)", "Mechanik-Stadt, mutig, orange"),
        ("character-nixie", "Nixie (Axolotl)", "Sonnenstrand, neugierig, türkis"),
        ("character-pip", "Pip (Eichhörnchen)", "Wolkenwerk, schnell, gelb"),
        ("character-koko", "Koko (Panda)", "Zuckerwald, freundlich, rosa"),
        ("character-tiko", "Tiko (Vogel)", "Dschungeltempel, chaotisch, grün"),
        ("character-bolt", "Bolt (Roboter)", "Mechanik-Stadt, logisch, blau"),
        ("character-bloom", "Bloom (Kaktus)", "Dschungeltempel, ruhig, lila"),
        ("character-momo", "Momo (Waschbär)", "Frostgipfel, clever, pink"),
    ]),
    ("Welt", [
        ("world-overview", "Welt-Übersicht", "Aethonia — 7 Inseln + Sternenzitadelle", True, True),
        ("world-sonnenstrand", "Sonnenstrand", "Urlaub & Wasser, türkis"),
        ("world-zuckerwald", "Zuckerwald", "Süßigkeiten, rosa"),
        ("world-wolkenwerk", "Wolkenwerk", "Schwebende Himmel, hellblau"),
        ("world-frostgipfel", "Frostgipfel", "Eis & Schnee, eisblau"),
        ("world-dschungeltempel", "Dschungeltempel", "Ruinen, dschungelgrün"),
        ("world-mechanik-stadt", "Mechanik-Stadt", "Spielzeug-Technik, silber"),
        ("world-sternenzitadelle", "Sternenzitadelle", "Finale, gold", False, True),
    ]),
    ("UI/UX", [
        ("ui-overview", "UI-Übersicht", "Alle Screens und Menüs", False, True),
        ("ui-mainmenu", "Hauptmenü", "Start, Character-Select, Settings"),
        ("ui-hud", "HUD", "Anzeige während des Spiels"),
        ("ui-board", "Board-UI", "Spielbrett, Felder, Aktionen"),
        ("ui-shop", "Shop-UI", "Sternen- und Item-Shop"),
        ("ui-character-select", "Charakter-Auswahl", "Arenians wählen"),
        ("ui-accessibility", "Accessibility", "Barrierefreiheit, Touch"),
    ]),
    ("Audio", [
        ("audio-overview", "Audio-Übersicht", "Musik, SFX, Voice"),
        ("audio-music", "Musik", "Themen je Insel"),
        ("audio-sfx", "Sound-Effekte", "Feedback für Aktionen"),
        ("audio-voice", "Voice / ArenaStar", "Sprachausgabe des Maskottchens"),
    ]),
    ("Narrative", [
        ("narrative-overview", "Narrative-Übersicht", "Geschichte und Flavor"),
        ("narrative-arena-star", "ArenaStar", "Maskottchen, moderiert, erklärt Regeln"),
        ("narrative-flavor", "Flavor-Texte", "Charakter-Beschreibungen, Items, Felder"),
    ]),
    ("Technical", [
        ("technical-architecture", "Architektur", "Godot 4 Struktur, Module", True, True),
        ("technical-multiplayer", "Multiplayer", "2-8 Spieler, Netcode, Server-Autorität", True, True),
        ("technical-fork-strategy", "Fork-Strategie", "Was bleibt aus STP, was wird neu gebaut", True, True),
        ("technical-data-structures", "Datenstrukturen", "Boards, Felder, Items, Spieler-Zustand", False, True),
        ("technical-performance", "Performance", "Mobile-Optimierung, FPS"),
    ]),
]

def md_to_html(md_text):
    lines = md_text.split("\n")
    out = []
    in_code = False
    for line in lines:
        s = line.rstrip()
        if s.strip().startswith("```"):
            if in_code:
                out.append("</pre>"); in_code = False
            else:
                out.append("<pre>"); in_code = True
            continue
        if in_code:
            out.append(html.escape(s)); continue
        s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
        s = re.sub(r'\*(.+?)\*', r'<em>\1</em>', s)
        s = re.sub(r'`(.+?)`', r'<code>\1</code>', s)
        if re.match(r'^#{1,4} ', s):
            level = len(re.match(r'^(#+)', s).group(1))
            out.append(f"<h{min(level,4)}>{s[level+1:]}</h{min(level,4)}>")
        elif s.strip().startswith(("- ", "* ")):
            out.append(f"<li>{s.strip()[2:]}</li>")
        elif re.match(r'^\d+\. ', s.strip()):
            out.append(f"<li>{re.sub(r'^\d+\. ','',s.strip())}</li>")
        elif s.strip() == "":
            if out and out[-1] != "<br>": out.append("<br>")
        elif s.strip().startswith("|"):
            out.append(html.escape(s))
        else:
            out.append(f"<p>{s}</p>")
    if in_code: out.append("</pre>")
    res = "".join(out)
    res = re.sub(r'(<li>.*?</li>\s*)+', lambda m: "<ul>"+m.group(0)+"</ul>", res, flags=re.DOTALL)
    res = re.sub(r'<li>', '<li style="margin-left:18px;margin-bottom:3px">', res)
    return res

def build():
    total = 0
    for entry in PARTS:
        if len(entry) == 3: continue
        total += len(entry[1])

    # Nav-Leiste (native Anker-Links)
    nav_links = []
    for i, entry in enumerate(PARTS):
        if len(entry) == 3:
            nav_links.append(f'<a class="nav" href="#top">📑 {html.escape(entry[0])}</a>')
        else:
            nav_links.append(f'<a class="nav" href="#sec-{i}">{html.escape(entry[0])}<span class="nav-count" id="nc-{i}">0/{len(entry[1])}</span></a>')
    nav_html = "".join(nav_links)

    # Sektionen
    sections_html = []
    # Übersichts-Sektion
    toc_links = "".join(
        f'<a class="toc-link" href="#sec-{i}">📂 {html.escape(PARTS[i][0])} <span>({len(PARTS[i][1])} Kapitel)</span></a>'
        for i in range(1, len(PARTS)) if len(PARTS[i]) != 3
    )
    sections_html.append(f'''
<section id="sec-0">
  <h2 class="sec-title">📑 Inhaltsverzeichnis</h2>
  <div class="toc-box">{toc_links}</div>
</section>''')

    for i, entry in enumerate(PARTS):
        if len(entry) == 3: continue
        name, chapters = entry[0], entry[1]
        chaps_html = []
        for item in chapters:
            fname, title = item[0], item[1]
            desc = item[2] if len(item)>2 else ""
            crit = item[3] if len(item)>3 else False
            hi = item[4] if len(item)>4 else False
            md_path = GDD_DIR / f"{fname}.md"
            content = "<p class='muted'><em>(Datei fehlt)</em></p>"
            if md_path.exists():
                content = md_to_html(md_path.read_text(encoding="utf-8"))
            tags = ""
            if crit: tags += '<span class="tag crit">Kritisch</span> '
            if hi: tags += '<span class="tag hi">Kern</span> '
            chaps_html.append(f'''
<details class="chapter" data-fname="{fname}">
  <summary>
    <label class="chk" onclick="event.stopPropagation()">
      <input type="checkbox" data-fname="{fname}" onchange="toggleCheck(this)">
      <span class="chkmark"></span>
    </label>
    <span class="chapter-title">{html.escape(title)} {tags}</span>
    <span class="chapter-desc">{html.escape(desc)}</span>
  </summary>
  <div class="chapter-content">{content}</div>
</details>''')
        sections_html.append(f'''
<section id="sec-{i}">
  <h2 class="sec-title">{html.escape(name)}</h2>
  {"".join(chaps_html)}
</section>''')

    html_doc = f'''<!DOCTYPE html>
<html lang="de"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Party Arena — Game Bible Review</title><style>
:root{{--bg:#0f1117;--card:#1a1c25;--card2:#22252f;--gold:#e8b04b;--green:#4ade80;--red:#f87171;--text:#e5e7eb;--muted:#9ca3af;--border:#2a2d3a}}
*{{margin:0;padding:0;box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{background:var(--bg);color:var(--text);font-family:-apple-system,Segoe UI,Roboto,sans-serif;padding-bottom:80px}}
header{{padding:20px 16px;background:linear-gradient(135deg,#1a1c25,#2a2d3a);border-bottom:2px solid var(--gold);position:sticky;top:0;z-index:30}}header h1{{font-size:1.25em;color:var(--gold)}}header p{{color:var(--muted);font-size:.85em;margin-top:4px}}
/* Native Navigationsleiste (Anker-Links, kein JS) */
.navbar{{background:var(--card);border-bottom:2px solid var(--border);position:sticky;top:62px;z-index:20;display:flex;overflow-x:auto;padding:6px 8px;gap:4px}}
.nav{{color:var(--muted);text-decoration:none;padding:8px 12px;border-radius:6px;white-space:nowrap;font-size:.85em;font-weight:600;flex-shrink:0}}
.nav:hover{{background:var(--card2);color:var(--gold)}}
.nav-count{{font-size:.7em;margin-left:4px;background:#3a2e1e;color:var(--gold);padding:1px 6px;border-radius:8px}}
.container{{max-width:820px;margin:0 auto;padding:16px}}
.progress-wrap{{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:14px;margin:16px 0;text-align:center}}
.progress-bar{{background:var(--card2);border-radius:6px;height:14px;overflow:hidden;margin-bottom:8px}}.progress-fill{{background:var(--gold);height:100%;width:0%;transition:width .3s}}.progress-text{{color:var(--muted);font-size:.9em}}
.info{{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:14px;margin:16px 0;font-size:.88em;color:var(--muted)}}.info strong{{color:var(--text)}}
section{{margin:24px 0;scroll-margin-top:120px}}
.sec-title{{color:var(--gold);font-size:1.1em;margin:16px 0 10px;border-bottom:2px solid var(--gold);padding-bottom:6px}}
.toc-box{{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:14px}}.toc-link{{display:block;color:var(--text);text-decoration:none;padding:8px 0;font-size:.95em;border-bottom:1px solid var(--border)}}.toc-link:last-child{{border:none}}.toc-link:hover{{color:var(--gold)}}.toc-link span{{color:var(--muted);font-size:.8em}}
/* Native <details> Kapitel */
details.chapter{{background:var(--card);border:1px solid var(--border);border-radius:8px;margin:8px 0;overflow:hidden}}
details.chapter summary{{list-style:none;display:flex;align-items:center;gap:12px;padding:12px;cursor:pointer;font-weight:600}}
details.chapter summary::-webkit-details-marker{{display:none}}
details.chapter summary:after{{content:'▾';color:var(--gold);margin-left:auto;font-size:1em}}
details.chapter[open] summary:after{{content:'▴'}}
.chapter-title{{flex:1}}.chapter-desc{{color:var(--muted);font-size:.8em;font-weight:400;margin-top:2px;display:block}}
/* Checkbox (native, mit Styling) */
.chk{{display:inline-flex;align-items:center;gap:8px;flex-shrink:0;cursor:pointer}}
.chk input[type=checkbox]{{display:none}}
.chkmark{{width:24px;height:24px;border:2px solid #4a4d5a;border-radius:6px;display:inline-block;position:relative}}
.chk input:checked + .chkmark{{background:var(--gold);border-color:var(--gold)}}
.chk input:checked + .chkmark::after{{content:'✓';position:absolute;top:-2px;left:4px;color:#1a1c25;font-size:17px;font-weight:bold}}
.chapter-content{{padding:14px;border-top:1px solid var(--border);background:var(--card2);font-size:.88em;line-height:1.6}}
.chapter-content p{{margin:4px 0}}.chapter-content h1,.chapter-content h2,.chapter-content h3,.chapter-content h4{{color:var(--gold);margin:12px 0 6px}}
.chapter-content pre{{background:#000;border-radius:6px;padding:10px;overflow-x:auto;font-size:.8em;color:#a5f3fc;white-space:pre-wrap;word-break:break-word}}
.chapter-content code{{background:#000;border-radius:3px;padding:1px 4px;color:#a5f3fc;font-size:.9em}}
.tag{{border-radius:4px;padding:2px 6px;font-size:.7em;font-weight:700;margin-left:4px}}.tag.crit{{background:#3a1e1e;color:var(--red)}}.tag.hi{{background:#1e3a2a;color:var(--green)}}
.cta{{position:fixed;bottom:0;left:0;right:0;background:var(--card);border-top:2px solid var(--border);padding:12px 16px;text-align:center;z-index:30}}
.cta button{{background:var(--gold);color:#1a1c25;border:none;border-radius:8px;padding:12px 28px;font-size:1em;font-weight:700;cursor:pointer}}.cta button:disabled{{background:#3a3d4a;color:var(--muted);cursor:not-allowed}}
.review-box{{display:none;margin:16px 0;background:var(--card);border:2px solid var(--red);border-radius:10px;padding:14px}}
.review-box textarea{{width:100%;height:90px;background:var(--card2);color:var(--text);border:1px solid var(--border);border-radius:6px;padding:10px;font-size:.9em;resize:vertical}}
.review-box button{{margin-top:8px;background:var(--red);color:#fff;border:none;border-radius:6px;padding:10px 18px;font-weight:600;cursor:pointer}}
</style></head><body>
<header id="top"><h1>🎮 Party Arena — Game Bible Review</h1><p>{total} Kapitel — über die Navigationsleiste springen, Kapitel aufklappen und abhaken.</p></header>
<div class="navbar">{nav_html}</div>
<div class="container">
  <div class="progress-wrap">
    <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
    <div class="progress-text" id="progressText">0 von {total} Kapiteln freigegeben</div>
  </div>
  <div class="info"><strong>📖 So funktioniert's:</strong> Nutze die <strong>Navigationsleiste oben</strong> zum Springen zwischen Themen. Tippe auf ein Kapitel zum Lesen, setze den ✓-Haken zum Freigeben. Nicht abgehakte Kapitel → CCGS fragt aktiv nach.<br><br>
  <strong>Legende:</strong> <span class="tag crit">Kritisch</span> = Lücke aus Session 1, <span class="tag hi">Kern</span> = Kern-Mechanik</div>
  {"".join(sections_html)}
  <div class="review-box" id="reviewBox"><strong>⚠️ Du hast Kapitel nicht freigegeben. Was soll anders gemacht werden?</strong>
    <textarea id="reviewText" placeholder="z.B. 'Stern soll 15 Münzen kosten', 'Nur 6 Spieler'..."></textarea>
    <button onclick="sendReview()">📨 Feedback senden</button></div>
</div>
<div class="cta"><button id="confirmBtn" onclick="confirmAll()" disabled>✅ Alle {total} Kapitel bestätigen</button></div>
<script>
var TOTAL={total};
function load(){{try{{return JSON.parse(localStorage.getItem('partyarena-bible-review')||'{{}}');}}catch(e){{return{{}};}}}}
function save(s){{try{{localStorage.setItem('partyarena-bible-review',JSON.stringify(s));}}catch(e){{}}}}
function toggleCheck(cb){{var s=load();var fn=cb.getAttribute('data-fname');if(cb.checked)s[fn]=true;else delete s[fn];save(s);updateAll();}}
function updateAll(){{var s=load();var c=0;document.querySelectorAll('details.chapter').forEach(function(d){{if(s[d.getAttribute('data-fname')])c++;}});var pct=TOTAL?Math.round(c/TOTAL*100):0;document.getElementById('progressFill').style.width=pct+'%';document.getElementById('progressText').textContent=c+' von '+TOTAL+' Kapiteln freigegeben';document.getElementById('confirmBtn').disabled=c!==TOTAL;}}
function restore(){{var s=load();document.querySelectorAll('details.chapter').forEach(function(d){{var cb=d.querySelector('input[type=checkbox]');if(s[d.getAttribute('data-fname')])cb.checked=true;}});updateAll();}}
if(document.readyState!=='loading')restore();else document.addEventListener('DOMContentLoaded',restore);
function confirmAll(){{document.getElementById('reviewBox').style.display='none';document.getElementById('confirmBtn').textContent='✅ Alle Kapitel bestätigt!';document.getElementById('confirmBtn').disabled=true;}}
function sendReview(){{var txt=document.getElementById('reviewText').value.trim();if(!txt)return;var s=load();var pending=[];document.querySelectorAll('details.chapter').forEach(function(d){{if(!s[d.getAttribute('data-fname')])pending.push(d.querySelector('.chapter-title').textContent.trim());}});document.getElementById('reviewText').value='';document.getElementById('reviewBox').style.display='none';alert('✅ Feedback gesendet');console.log('Feedback:',txt,'| Offene:',pending);}}
</script></body></html>'''

    OUT.write_text(html_doc, encoding="utf-8")
    print(f"Native Dashboard geschrieben: {OUT}")
    print(f"Kapitel: {total}, Größe: {OUT.stat().st_size/1024:.0f} KB")

if __name__ == "__main__":
    build()
