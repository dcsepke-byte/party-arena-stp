# Party Arena — Projekt-Log

> Automatisch gepflegtes Log. Jeder Eintrag dokumentiert: was gemacht wurde,
> was verifiziert wurde, welche Fehler gefunden/gefixt wurden, und der aktuelle Stand.
> Letzte Aktualisierung: 2026-08-12

---

## 2026-08-12 — Render-Deploy (Web-Version für Handy)

### Was passiert ist
- **Render-Projekt `party-arena-godot` erstellt** (statische Site, `srv-d9u0llh42hec73990b2g`)
- **Live-URL:** https://party-arena-godot.onrender.com
- Render-Key in `/opt/data/.env` gespeichert (`RENDER_API_KEY`)
- Build-Command installiert Godot 4.7.1 + Export-Templates und baut den Web-Export direkt auf Render (umgeht GitHub-100MB-Limit)

### Verifiziert
- ✅ Spiel lädt im Browser (WebGL 2.0, Canvas 1280x577)
- ✅ Alle 7 Boards laden (KDEValley, dschungeltempel, frostgipfel, mechanik-stadt, sonnenstrand, sternenzitadelle, test, wolkenwerk, zuckerwald)
- ✅ 12+ Minigames laden (alle Kategorien)
- ✅ 8 Charaktere laden (bloom, bolt, brix, koko, momo, nixie, pip, tiko)
- ✅ Items laden

### Offene Fehler (aus Browser-Konsole)
- ❌ `sound_button.gd`: Preload `rollover2.wav` / `click1.wav` fehlt → Parse-Fehler
- ❌ `main_menu.gd`: Preload `edit.png` / `delete.png` fehlt → Parse-Fehler
- ❌ Item-Icons (`coinmagnet`, `luckydice`, etc.): "No loader found" → fehlende `.import`-Dateien
- **Ursache:** `.import`-Dateien wurden beim Cleanup gelöscht, aber Godot braucht sie für den Export

### Nächster Schritt
- `.import`-Dateien wiederherstellen (475 Stück aus Original-Repo kopiert, aber `.gitignore` blockt sie)
- `.gitignore` anpassen, damit `.import`-Dateien getrackt werden
- Re-Deploy + Konsole erneut prüfen

---

## 2026-08-12 — Render-Deploy (Fortsetzung)

### Was passiert ist
- `.import`-Dateien wiederhergestellt (475 Stück) + `.gitignore` angepasst (`.import` wird getrackt)
- Re-Deploy auf Render (Commit `593e19c`)

### Verifiziert
- ✅ Spiel lädt (WebGL 2.0, keine JS-Fehler)
- ✅ Alle 7 Boards, 12+ Minigames, 8 Charaktere, Items laden

### Verbleibende Fehler (aus Browser-Konsole)
- ❌ `rollover2.wav` / `click1.wav`: "Unrecognized binary resource file" → `.import`-Datei zeigt auf falschen Hash-Pfad
- ❌ `edit.png` / `delete.png`: "Compressed texture file is corrupt" → `.ctex`-Cache fehlt
- ❌ Item-Icons: "No loader found" → `.import`-Dateien fehlen für die neuen Items

### Kernproblem (ehrlich)
**Godot Headless importiert Assets nicht korrekt** (dokumentiertes Limit). Die `.import`-Dateien referenzieren Cache-Dateien (`.ctex`/`.sample`), die im Headless-Export nie erzeugt werden. Das blockiert das Hauptmenü (sound_button.gd, main_menu.gd).

### Lösungsansatz
- Die fehlenden Assets (Sounds, Icons) sind **nicht kritisch für die Spiellogik** — sie blockieren nur das Hauptmenü
- Option A: Assets manuell als `.import`-Dateien mit korrekten Pfaden anlegen
- Option B: Die Preloads in `sound_button.gd`/`main_menu.gd` auf vorhandene Assets umbiegen
- Option C: Godot-Editor (GUI) auf Dannys Rechner für korrekten Import nutzen

---

## 2026-08-12 — Render-Deploy (Fix: Preloads robust)

### Was passiert ist
- `sound_button.gd`: Preloads → Laufzeit-Load mit Fallback (kein Crash bei fehlendem Import-Cache)
- `main_menu.gd`: `edit.png`/`delete.png` Preloads → `_load_icon()` (robust)
- Commit `1297769`, gepusht auf `dev`

### Entscheidung (Danny: Option 3)
- **Hermes:** fixe die kritischen Preloads (erledigt)
- **Danny:** öffnet das Projekt einmal im Godot-Editor (GUI) für den sauberen Asset-Import
- Danach läuft der Export vollständig (Sounds, Icons, Texturen korrekt eingepackt)

---

## 2026-08-11 — CI-Bot-Test + Konzept-Gegencheck

### Was passiert ist
- **CI-Bot-Test-Workflow** eingerichtet (`.github/workflows/bot-test.yml`) — läuft bei jedem Push auf `dev`
- **GitHub-Repo bereinigt:** LFS-Tracking entfernt (GitHub hat kein LFS-Backend), Assets als normale Dateien, GLBs verkleinert
- **Konzept-Gegencheck:** 64/64 Checks gegen Game Bible grün

### Verifiziert (alle Tests grün)
- ✅ Feldverteilung: 40/40
- ✅ Stern-Mechanik: 244/244
- ✅ Items: 90/90
- ✅ Minigames: 355/355
- ✅ Charaktere: 132/132
- ✅ Branches, Boards, Ereignisse: PASS
- ✅ Konzept-Gegencheck: 64/64

### Gefundene & gefixte Bugs
- `player_board.gd`: Mixed tabs/spaces (Parse-Fehler)
- `player_info.gd`: `diff`-Typinferenz (2 Stellen)
- `star.png` fehlte komplett (Stern-Icon)
- 5 Item-Icons fehlten
- Tests nutzten absolute Pfade → relative Pfade (CI-kompatibel)
- `set -e` + `pipefail` für echte Fehlererkennung

### Wichtige Erkenntnis
- **Godot Headless kann keine Assets importieren** (Fonts, Texturen, `.ctex`) — dokumentiertes Limit
- Deshalb testet der CI die Spiellogik über Python-Unit-Tests, nicht den vollen 3D-Render

---

## 2026-08-11 — Komplette Kern-Umsetzung (Milestones 1-6)

### Was umgesetzt wurde
| Milestone | Inhalt | Status |
|---|---|---|
| 1 | Feldtypen (7 Typen) | ✅ verifiziert |
| 2 | Stern-Mechanik (STAR_COST=20, wandert) | ✅ verifiziert |
| 3 | Items (5 Stück) | ✅ verifiziert |
| 4 | Minigames (12 Stück, 5 Kategorien) | ✅ verifiziert |
| 5 | Charaktere (8 Arenians + 3D-Modelle) | ✅ verifiziert |
| 6 | Boards (7 Inseln, 40 Felder) | ✅ verifiziert |
| 6b | Abzweigungs-Logik (Hauptpfad 32 + 2×4) | ✅ verifiziert |
| 6c | Ereignis-Logik + Sonderregeln | ✅ verifiziert |

### 3D-Charaktere (Blender, prozedural)
- 8 Arenians: Brix (Stein-Golem, eckig), Nixie (Echse), Pip (Eichhörnchen), Koko (Panda, weiß), Tiko (Tukan), Bolt (Roboter, eckig), Bloom (Kaktus), Momo (Waschbär)
- Stil: große Köpfe, große Augen, Toy-like, gemäß Game Bible
- Subsurf + Bevel + PBR-Materialien

### Ehrliche Hinweise
- 3D-Assets sind prozedurale Platzhalter (echte Insel-Grafiken zeichnet Danny)
- UI/UX-Screens existieren, aber Verfeinerung nach Game Bible (ArenaStar-Kommentator, 30s-Timer) offen
- Audio spezifiziert, aber Assets fehlen teils
