# Technische Performance-Ziele und Optimierung — Party Arena

> **Status:** Proposed
> **Version:** 2.0.0
> **Letzte Anderung:** 2026-08-11
> **Abhangigkeiten:** technical-architecture.md, technical-multiplayer.md, technical-data-structures.md

---

## 1. Overview

Party Arena ist ein visuell charmantes, aber technisch genusames Spiel. Der Cartoon-Stil mit Toon-Shading (Cel-Shading) und begrenzter Geometrie erlaubt breite Hardware-Unterstutzung — von integrierten GPUs auf Laptops bis hin zu mobilen Geraten und der Nintendo Switch 2. Dieses Dokument definiert die Performance-Budgets, Optimierungs-Strategien und Test-Methodik.

### Leistungs-Philosophie

| Prinzip | Beschreibung |
|---|---|
| **Breite Zuganglichkeit** | Das Spiel muss auf schwacher Hardware (Intel UHD 620, 8GB RAM) mit 60 FPS laufen. Party-Spiele leben von lokalen Multiplayer-Sessions auf unterschiedlichsten Geraten. |
| **Visuelle Klarheit uber Realismus** | Cartoon-Grafik braucht keine teuren Effekte. Kein Raytracing, kein SSAO, keine Screen-Space-Reflections. Das spart Budget fur das Wesentliche: 8 Spieler gleichzeitig. |
| **Deterministisches Frame-Budget** | Das Spiel lauft mit fester Framerate (60 FPS Desktop, 30 FPS Mobile/Konsole). Kein "Unlocked" Framerate-Modus — das Frame-Budget ist heilig. |
| **Progressive Optimierung** | Nicht vorzeitig optimieren. Erst messen (Profiler), dann optimieren. Performance-Tests ab Phase 4 der Fork-Strategie. |
| **Kein Kompromiss bei 8 Spielern** | Das Spiel MUSS mit 8 Spielern laufen. Wenn ein Feature die Performance unter 60 FPS druckt, wird es vereinfacht oder entfernt — nicht die Spielerzahl reduziert. |
| **Fallback-Modi statt Ausschluss** | Schwache Hardware wird nicht ausgeschlossen. Das Spiel erkennt automatisch die Hardware-Leistung und aktiviert abgestufte Fallback-Modi (reduzierte Auflosung, weniger Partikel, keine Schatten). |

### Ziel-Plattformen

| Plattform | Prioritat | Ziel-FPS | Ziel-Auflosung | Ziel-Hardware | Renderer |
|---|---|---|---|---|---|
| **Windows (Desktop)** | Primar | 60 FPS | 1920×1080 | Intel i5-8250U, 8GB RAM, Intel UHD 620 | Forward+, Vulkan |
| **Linux (Desktop)** | Primar | 60 FPS | 1920×1080 | Wie Windows (gleiche Hardware-Klasse) | Forward+, Vulkan |
| **macOS (Desktop)** | Primar | 60 FPS | 1920×1080 | Apple M1 (oder Intel i5 Aquivalent) | Forward+, Metal |
| **Steam Deck** | Sekundar (Post-Launch) | 60 FPS | 1280×800 | Steam Deck LCD/OLED (Zen 2 + RDNA 2) | Forward+, Vulkan |
| **Nintendo Switch 2** | Sekundar (Post-Launch) | 30 FPS | 1080p Docked / 720p Handheld | Switch 2 Hardware (Ziel-Spec) | Forward Mobile, Vulkan |
| **iOS / Android** | Sekundar (Post-Launch) | 30 FPS | Native (ca. 1080p) | Snapdragon 7 Gen 2 / Apple A15 | Forward Mobile, Vulkan/Metal |

---

## 2. Player Fantasy

Performance ist fur den Spieler dann perfekt, wenn er sie nicht bemerkt.

### Was der Spieler erlebt

- **Flussiges Gameplay:** Kein Ruckeln, kein Tearing (VSync an), keine sichtbaren Frame-Drops. Das Spiel fuhlt sich geschmeidig an — jede Animation, jede Bewegung, jede UI-Reaktion lauft ohne sichtbare Verzogerung.
- **Schnelle Reaktion:** Eingaben (Wurfeln, Item-Auswahl, Minispiel-Steuerung) werden sofort umgesetzt. Kein spurbarer Input-Lag. Maximal 0,5 Sekunden zwischen Eingabe und visuellem/horbarem Feedback.
- **Sauberes Bild:** Keine flimmernden Kanten (TAA aktiv), keine Auflosungseinbruche (stabile Render-Skalierung). Der Cartoon-Look bleibt auch bei niedrigeren Einstellungen konsistent.
- **Kurze Ladezeiten:** Minispiele laden in unter 2 Sekunden. Das Spiel startet in unter 5 Sekunden. Board-Wechsel in unter 3 Sekunden. Kein Storendes Warten.
- **Lokaler Multiplayer ohne Einbu"sen:** 4-Spieler-Splitscreen lauft genauso flussig wie Single-Player. 8-Spieler-Shared-Screen lauft mit vollen 60 FPS. Kein "jetzt ruckelt es, weil mehr Spieler da sind".
- **Automatische Anpassung:** Das Spiel erkennt schwache Hardware und passt die Einstellungen automatisch an. Der Spieler muss nichts konfigurieren (kann aber im Options-Menu manuell anpassen).

### Was der Spieler NICHT merken soll

- Kein "Dynamic Resolution Scaling" wahrend des Spiels. Die Auflosung wird einmal zu Beginn gesetzt und bleibt stabil.
- Keine Pop-in-Effekte (Modelle oder Texturen, die plotzlich auftauchen). LOD-Ubergange sind sanft und kaum sichtbar.
- Kein "Jitter" oder "Stutter" durch Garbage Collection. Godot's Reference Counting ist deterministisch — es gibt keine GC-Pausen.
- Keine Audio-Aussetzer oder Knackser. Audio lauft in eigenem Thread und wird nie durch Game-Logik blockiert.
- Keine sichtbaren Kompromisse bei 8 Spielern. Das Spiel sieht mit 8 Spielern genauso gut aus wie mit 2.

### Was der Entwickler merkt

- **Klare Budgets:** Jedes System wei"ss, wie viel Frame-Zeit es beanspruchen darf. Bei Uberschreitung: Profiler-Ausgabe, Optimierung.
- **CI-gestutzte Regression:** Auch ohne GPU in CI werden Performance-Metriken gemessen (Frame-Zeit, GDScript-Aufrufe, Allokationen). Build schlagt fehl, wenn Budgets uberschritten werden.
- **Einfache Skalierung:** `scaling_3d_scale` (0.5–1.0) erlaubt schnelle Performance-Anpassung ohne Code-Anderungen. Auto-Tuning erkennt Hardware und setzt passende Werte.

---

## 3. Detailed Rules

### 3.1 Performance-Budget (Frame-Budget)

#### 3.1.1 Desktop-Budget (60 FPS = 16.67ms pro Frame)

| System | Budget (ms) | Anteil | Beschreibung |
|---|---|---|---|
| **Rendering (GPU)** | 8.0 | 48 % | Draw Calls, Shader, Rasterisierung, Post-Processing. Gemessen uber GPU-Profiler (RenderDoc/Godot). |
| **Game-Logik (CPU)** | 3.0 | 18 % | Board-Logik (Controller, NodeBoard, Events), State-Updates, RPC-Verarbeitung. |
| **GDScript (CPU)** | 3.0 | 18 % | Skript-Ausfuhrung (_process, _physics_process), UI-Updates, Animation-Tree. |
| **Audio (CPU)** | 1.0 | 6 % | Audio-Mixing, Streaming von Musik, SFX-Instanziierung. |
| **Reserve (CPU+GPU)** | 1.67 | 10 % | Puffer fur Spitzen (Partikel-Burst, viele Spieler auf einem Feld), OS-Overhead, Godot-Interna. |

**Budget-Uberschreitung:** Wenn eine Komponente ihr Budget uberschreitet, wird eine Warnung geloggt (`[PERF] Budget uberschritten: Rendering 9.2ms/8.0ms`). Bei Uberschreitung in mehr als 5 % der Frames: Automatische Skalierung (Render-Skalierung um 0.1 reduzieren).

#### 3.1.2 Mobile/Konsole Budget (30 FPS = 33.33ms pro Frame)

| System | Budget (ms) | Anteil | Beschreibung |
|---|---|---|---|
| **Rendering (GPU)** | 18.0 | 54 % | Gro"sseres Budget fur schwuchere GPU. Low-Quality-Shader, reduzierter LOD-Abstand. |
| **Game-Logik (CPU)** | 5.0 | 15 % | Leicht erhohtes Budget fur langsamere CPU. |
| **GDScript (CPU)** | 5.0 | 15 % | Leicht erhoht. Static Typing hilft hier besonders. |
| **Audio (CPU)** | 2.0 | 6 % | Etwas mehr Budget fur mobile Audio-Pipelines. |
| **Reserve (CPU+GPU)** | 3.33 | 10 % | Gro"sserer Puffer fur mobile Hintergrundprozesse, Energiesparmodi. |

### 3.2 Speicher-Budget

#### 3.2.1 RAM-Budget (1.5 GB Maximum)

| Komponente | Typische Nutzung (MB) | Maximum (MB) | Beschreibung |
|---|---|---|---|
| Godot Engine (Baseline) | 150 | 200 | Engine-Overhead, Rendering-Context, Input, Audio. |
| Board + Plugins | 100 | 150 | Board-Geometrie (20K Tris), Texturen (2048² BC7), Plugin-Code. Nur das aktive Board ist geladen. |
| 8 Charakter-Modelle + Texturen | 80 | 120 | 10 MB pro Charakter (LOD0 5000 Tris + Texturen 1024²). LOD1 wird bei Bedarf aus LOD0 generiert (kein separates Modell im RAM). |
| Minispiel-PCK-Cache | 100 | 150 | 12 Minispiele im RAM-Cache, je 5–10 MB (Code + Assets). |
| Audio (Musik + SFX) | 80 | 120 | Musik-Streaming (ca. 3 MB pro Track × 17 Tracks = 51 MB aktiv, Rest gestreamt), SFX-Cache (haufige SFX im RAM). |
| UI-Texturen | 50 | 80 | Menus, HUD, Ladebildschirme, Icons (unkomprimiert fur Scharfe). |
| Netzwerk-Buffer | 20 | 40 | ENet-Puffer, RPC-Queues, State-Snapshots. |
| Godot-Interna | 120 | 200 | Node-Trees (bis zu 1000 Nodes), Signal-Connections, Variablen. |
| Reserve | 100 | 200 | OS-Overhead, Memory-Fragmentierung, Shared Libraries. |
| **Gesamt** | **~800** | **< 1500** | Ziel: 800 MB typisch, 1.5 GB niemals uberschreiten. |

#### 3.2.2 VRAM-Budget (512 MB Maximum)

| Komponente | Typische Nutzung (MB) | Maximum (MB) | Beschreibung |
|---|---|---|---|
| Board-Texturen (2048², BC7) | 30 | 50 | Board-Atlas-Textur + Tiling-Texturen. 1× 2048² = 16 MB BC7. |
| Charakter-Texturen (1024², BC7) | 20 | 40 | 8 Charaktere × 1 Diffuse-Textur, je ca. 2.5 MB BC7. |
| UI-Texturen | 20 | 40 | UI-Atlas unkomprimiert fur Scharfe. |
| Shadow Maps | 16 | 32 | DirectionalLight Shadow Map (1024²) + bis zu 4 OmniLight Shadow Maps (512²). |
| Render-Targets (Split-Views) | 30 | 60 | 4 Viewports a 960×540 = 4 × 2 MB RGBA8 = 8 MB. Plus Depth-Buffer. |
| LUT-Texturen | 1 | 2 | Color-Grading LUT (32×32×32 3D-Textur), Ramp-Textur (32×1 1D-Textur). |
| Partikel-Texturen | 5 | 10 | Flipbook-Texturen (128×128), ca. 20 Texturen. |
| Godot-Interna | 50 | 100 | Framebuffer, Z-Buffer, Stencil, temporare Render-Targets. |
| Reserve | 127 | 178 | Fur dynamische Allokation, Render-Doc-Abweichungen. |
| **Gesamt** | **~300** | **< 512** | Ziel: 300 MB typisch, 512 MB Max. |

#### 3.2.3 Festplatten-Budget (Installation)

| Komponente | Grosse (MB) | Beschreibung |
|---|---|---|
| Godot-Engine + Game-Code | 80 | Exportiertes Binary + Core-Scripts (.pck). |
| Board-Plugins (8) | 200 | 8 Inseln, je ca. 25 MB (Modelle + Texturen + Audio). |
| Charakter-Plugins (8) | 160 | 8 Arenians, je ca. 20 MB (Modelle + Texturen + Voice). |
| Item-Plugins (5) | 25 | 5 Items, je ca. 5 MB (Modelle + Icons + Sounds). |
| Minispiel-Plugins (12) | 300 | 12 Minispiele, je ca. 25 MB (Szene + Assets). |
| Audio (Musik) | 80 | 17 Musik-Tracks (8 Board + 3 Menu + 6 Minispiel). |
| UI-Texturen | 40 | Alle UI-Assets. |
| Fonts | 15 | 5 Schriftarten (2 UI + 3 Effekt). |
| Ubersetzungen | 5 | 6 .po-Dateien. |
| Sonstiges | 95 | Icon, Splash, Config, Zertifikate. |
| **Gesamt Installation** | **~1000** | Ziel: < 2 GB. |

### 3.3 Ladezeit-Budget

| Ladevorgang | Budget (Sekunden) | Beschreibung |
|---|---|---|
| **Spielstart (kalt, SSD)** | 5.0 s | Vom Doppelklick bis Hauptmenu. Inkl. Godot-Engine-Init, Plugin-Discovery, UI-Ladung. |
| **Spielstart (kalt, HDD)** | 10.0 s | Wie oben, aber mit langsameren Disk-I/O. |
| **Board laden** | 3.0 s | Von Board-Auswahl bis erster spielbarer Frame. Inkl. Board-Geometrie, Texturen, 8 Charaktere instanziieren. |
| **Minispiel laden** | 2.0 s | Von Trigger bis spielbar. Inkl. Plugin-PCK aus Cache laden und Szene instanziieren. |
| **Minispiel laden (Worst-Case, 12. Minispiel)** | 3.0 s | Etwas langer, da PCK-Cache evtl. verdrangt wurde. Neu-Ladung von Disk. |
| **Speicher laden** | 1.0 s | SaveGame-Datei parsen und State wiederherstellen. |
| **Menu-Ubergange** | 0.3 s | Zwischen Menus (z.B. Hauptmenu → Optionen). Instant fur den Spieler. |

### 3.4 Rendering (GPU)

#### 3.4.1 Godot 4 Renderer-Konfiguration

**Desktop (Forward+):**
- **Backend:** Vulkan (Linux, Windows), Metal (macOS, automatisch via Godot).
- **Forward+ Clustered Rendering:** Default in Godot 4. Bietet gute Balance aus Performance und Qualitat fur Cartoon-Stil.
- **Anti-Aliasing:** TAA (Temporal Anti-Aliasing) + optional MSAA 2× oder 4×.
- **VSync:** Aktiviert (konfigurierbar). Mailbox-Modus fur niedrigsten Input-Lag.
- **Auflosung:** 1920×1080 nativ. Render-Skalierung: 0.5–1.0.

**Mobile/Konsole (Forward Mobile):**
- **Backend:** Vulkan (Android, Switch 2), Metal (iOS).
- **Forward Mobile Renderer:** Optimiert fur Mobile-GPUs (weniger Features, kleinere Bandbreite).
- **Anti-Aliasing:** MSAA 2× (kein TAA auf Mobile — zu teuer).
- **Schatten:** Nur DirectionalLight (Hard Shadows). Keine OmniLight-Shadows.

#### 3.4.2 Draw-Call-Budget

| Szene | Max Draw Calls | Beschreibung |
|---|---|---|
| Hauptmenu | 50 | Einfache UI + 3D-Hintergrund (ArenaStar schwebend). |
| Lobby / Charakter-Auswahl | 80 | UI + 8 Charakter-Vorschaumodelle. |
| Board (1 Spieler) | 150 | Board-Geometrie (~30 Draw Calls) + 1 Charakter (~8) + Dekoration (~40) + UI (~30) + Sonstiges (~42). |
| Board (4 Spieler, Splitscreen) | 350 | Board + 4 Charaktere + Dekoration. Splitscreen: Mehrere Kameras, aber Godot frustum-culled pro Viewport — effektiv weniger Draw Calls als 4× Single-View. |
| Board (8 Spieler, Shared Screen) | 500 | Board + 8 Charaktere + Dekoration. Alle Charaktere im selben Viewport. GPU Instancing reduziert Draw Calls fur identische Geometrie. |
| Minispiel (Durchschnitt) | 200 | Minispiel-spezifische Geometrie + 8 Charaktere. Variiert pro Minispiel. |

**Draw-Call-Reduzierung durch GPU Instancing:** Identische Feld-Modelle (40 Felder pro Board) werden via `MultiMeshInstance3D` gerendert — reduziert Draw Calls von 40 auf 1. Gleiches gilt fur Props/Dekorationen (Palmen, Steine, etc.).

#### 3.4.3 Wichtige Godot 4 Projekt-Einstellungen

```
[rendering]

# Renderer
rendering/renderer/rendering_method = "forward_plus"
rendering/renderer/rendering_method.mobile = "mobile"

# Anti-Aliasing
rendering/anti_aliasing/quality/msaa_2d = 2
rendering/anti_aliasing/quality/msaa_3d = 2
rendering/anti_aliasing/quality/use_taa = true
rendering/anti_aliasing/quality/screen_space_aa = 0  # Deaktiviert

# Skalierung
rendering/scaling_3d/mode = "bilinear"
rendering/scaling_3d/scale = 1.0  # Runtime-Override 0.5–1.0

# Schatten (niedrig fur Performance)
rendering/lights_and_shadows/directional_shadow/size = 1024
rendering/lights_and_shadows/directional_shadow/mode = 0  # Hard shadows only
rendering/lights_and_shadows/positional_shadow/size = 512

# Limits (angepasst fur Cartoon-Stil)
rendering/limits/opengl/max_renderable_elements = 100000
rendering/limits/opengl/max_lights_per_object = 4
rendering/limits/cluster_builder/max_clustered_elements = 256

# Texturen
rendering/textures/default_filters/use_nearest_mipmap_filter = false
rendering/textures/vram_compression/cache_gzip = true

# Keine teuren Effekte
rendering/environment/ssao/quality = 0           # Aus
rendering/environment/ssil/quality = 0            # Aus
rendering/environment/screen_space_reflection/roughness_quality = 0  # Aus
rendering/environment/glow/upscale_mode = 0       # Aus
rendering/environment/volumetric_fog/use_filter = 0  # Aus
```

#### 3.4.4 LOD (Level of Detail)

Charakter-Modelle haben **2 LOD-Stufen**. Godot's automatisches LOD-System wird NICHT verwendet — stattdessen manuelles Mesh-Swapping (bessere Kontrolle uber Tris-Zahl und Ubergang).

| LOD-Stufe | Distanz von Kamera (Einheiten) | Tris (Charakter) | Tris (Board-Props) | Verwendung |
|---|---|---|---|---|
| LOD0 (Hoch) | 0 – 20 | Max 5000 | Max 20000 (voll) | Nahaufnahme: Charakter-Auswahl, aktiver Spieler, Splitscreen-Nah-View |
| LOD1 (Niedrig) | > 20 | Max 1500 | Max 10000 (reduziert) | Entfernte Charaktere, andere Spieler im Splitscreen, Shared-Screen-Distanz |

**LOD-Wechsel:** Sanft via Transparenz-Blending uber 2 Einheiten (18–20 = Crossfade LOD0→LOD1). Der Ubergang ist fur den Spieler kaum sichtbar (Cartoon-Stil verzeiht leichte Unsch"arfe).

**Board-LOD:** Board-Modelle haben kein LOD (immer voll aufgelost). Die 20K Tris pro Board sind statisch und werden via GPU Instancing optimiert — LOD wurde mehr Komplexitat bringen als es spart.

#### 3.4.5 Frustum Culling

Godot 4 fuhrt automatisches Frustum Culling durch (Kamera-Frustum). Keine manuelle Konfiguration notig. Bei Splitscreen: Jede Split-View hat ihre eigene Kamera mit eigenem Frustum → Culling ist effektiver (jede Kamera rendert nur das in ihrem Sichtfeld).

#### 3.4.6 Occlusion Culling

**NICHT implementiert.** Begrundung:
- Das Board ist meistens vollstandig sichtbar (Top-Down-ahnliche Perspektive, ~60° Winkel).
- Wenig Geometrie, die andere Geometrie verdecken konnte (flaches Board-Design, keine engen Korridore).
- Occlusion-Culling-Setup (Portal-System, Occluder-Geometrie) kostet Entwicklungszeit, die fur 8-Spieler-Optimierung besser genutzt wird.

### 3.5 Shader

#### 3.5.1 Toon-Shader (Cel-Shading) — Charaktere

Alle Charakter-Modelle verwenden einen einheitlichen Toon-Shader mit Ramp-Textur. Dies ist der zentrale visuelle Stil von Party Arena.

**Shader-Spezifikation:**
- **Typ:** `StandardMaterial3D` mit `shading_mode = 0` (Unshaded) + manueller Diffuse-Berechnung per Shader-Code fur Cel-Look.
- **Ramp-Textur:** Eine eindimensionale Textur mit 32×1 Pixeln, die 2–3 Farbtone definiert. Der Shader berechnet den Diffuse-Winkel (N·L) und mappt ihn auf die Ramp-Textur: Winkel < 0.3 → Schatten-Farbe, Winkel 0.3–0.7 → Mittel-Farbe, Winkel > 0.7 → Highlight-Farbe.
- **Outlines:** Keine Geometry-Shader-Outlines (teuer, unzuverlassig auf Mobile). Stattdessen: **Inverted-Hull-Methode** — jedes Charakter-Modell hat eine zweite, leicht vergrosserte Mesh-Hulle mit invertierten Normalen, schwarz eingefarbt. Einmalig im 3D-Modell hinterlegt, kein Runtime-Shader-Aufwand.
- **Schatten:** Nur DirectionalLight-Schatten (Hard-Shadow-Modus, Shadow-Map 1024²). Keine weichen Schatten (PCF) — das wurde dem Cartoon-Stil widersprechen und Performance kosten.
- **Shader-Komplexitat:** Unter 50 Shader-Instruktionen. Extrem leicht auf der GPU. L"auft selbst auf integrierten GPUs (Intel UHD 620) mit >100 FPS fur ein einzelnes Modell.

**Begrundung fur Toon-Shader statt PBR:**
- PBR (Metallic/Roughness/Albedo/Normal) ist visueller Overkill fur einen Cartoon-Stil und kostet das 3–5-fache an GPU-Zeit.
- Toon-Shader ist visuell passend (Spielzeug-Look) UND performanter.
- Konsistenter Look auf allen Plattformen (PBR variiert je nach Beleuchtung und Tonemapping).
- Ramp-Textur erlaubt einfaches, globales Umfarben des Cel-Looks (nur Ramp-Textur austauschen, nicht jedes Material).

#### 3.5.2 Board-Shader

Board-Modelle verwenden `StandardMaterial3D` mit reduzierten Einstellungen:
- `metallic = 0.0` — Keine metallischen Oberflachen (alles ist Spielzeug: Holz, Filz, Plastik, Bonbon).
- `roughness = 1.0` — Vollstandig diffus, keine Glanzlichter (Cartoon-Boards brauchen keine Specular-Highlights).
- `shading_mode = 1` — Per-Pixel (nicht Per-Vertex), fur bessere Qualitat der Feld-Texturen bei akzeptablen Kosten (Per-Pixel ist Standard und billig).
- **Keine** Normal-Maps — flache Texturen reichen fur Cartoon-Stil.
- **Keine** Height-Maps — kein Parallax-Mapping.
- **Keine** Ambient-Occlusion-Maps — AO wird nicht gebraucht.

#### 3.5.3 Post-Processing-Shader (Fullscreen)

Die Post-Processing-Pipeline ist minimalistisch — nur zwei Effekte, beide extrem billig (< 0.2ms zusammen).

**Aktivierte Effekte:**
1. **Color Grading (LUT):** 32×32×32 3D-LUT-Textur. Standard-LUT ist neutral. Jedes Board kann eine eigene LUT laden (z.B. warmere Farben fur Sonnenstrand, kuhlere fur Frostgipfel). Kosten: < 0.1ms.
2. **Vignette:** Godot-eigener Vignette-Effekt (`Environment.adjustment_color_correction`). Intensity: 0.3, Opacity: 0.5. Weiche Abdunklung der Bildschirmrander, lenkt Fokus auf das Board-Zentrum. Kosten: < 0.1ms.

**Deaktivierte Effekte (und warum):**

| Effekt | Gesch"atzte Kosten | Grund fur Deaktivierung |
|---|---|---|
| SSAO (Screen Space Ambient Occlusion) | ~2.0ms | Cartoon-Stil braucht keine Ambient Occlusion. Spielzeug-Welt hat keine realistischen Schattenwurfe. |
| SSIL (Screen Space Indirect Lighting) | ~2.0ms | Nicht notig bei simpler Beleuchtung (DirectionalLight + wenige OmniLights). |
| SSR (Screen Space Reflections) | ~1.5ms | Keine spiegelnden Oberflachen im Spiel (alles diffus). |
| Glow / Bloom | ~0.5ms | Passt nicht zum Cartoon-Stil (zu "glowy", verschwommen). Partikel liefern eigene Glow-Texturen. |
| DOF (Depth of Field) | ~1.0ms | Nicht notig — das Board ist immer scharf (flaches Layout). |
| Motion Blur | ~0.5ms | Subjektiv storend in einem Party-Spiel mit schnellen Bewegungen. |
| FXAA / SSAA | ~0.3ms | TAA + MSAA reichen fur unseren Stil. |
| Adjustments (Brightness/Contrast/Saturation) | ~0.2ms | Wird via LUT abgedeckt. Zus"atzliche Effekte wurden doppelt kosten. |

### 3.6 Asset-Optimierung

#### 3.6.1 3D-Modelle

| Asset-Typ | Max Tris (LOD0) | Max Tris (LOD1) | Max Vertices | Format | Begrundung |
|---|---|---|---|---|---|
| Charakter (Arenian) | 5000 | 1500 | 3500/1000 | `.glb` (GLTF Binary) | Genug fur Cartoon-Charakter mit runden Formen, Accessoires und Inverted-Hull-Outline. |
| Board (komplett, 40 Felder) | 20000 | 10000 | 15000/7000 | `.glb` | Flaches Design, wenig Vertikale. 40 Felder à ~300 Tris + Dekoration à ~8000 Tris. |
| Item (3D-Modell) | 500 | — | 350 | `.glb` | Kleine Objekte: Wurfel, Schild, Magnet, Wirbel, Handschuh. Kein LOD notig. |
| ArenaStar | 2000 | — | 1500 | `.glb` | Zentrales Board-Element. Ofter sichtbar, daher hohere Qualitat. Kein LOD. |
| Props/Dekoration | 300–1000 | 100–300 | variabel | `.glb` | Palmen, Fackeln, Steine, Blumen, etc. MultiMeshInstance3D fur Instancing. |

#### 3.6.2 Texturen

| Textur-Typ | Max Auflosung | Kompression (Desktop) | Kompression (Mobile) | Format |
|---|---|---|---|---|
| Charakter-Diffuse | 1024×1024 | BC7 | ETC2 | `.webp` Quelle → Godot-Import |
| Charakter-Normal | Keine | — | — | Cartoon-Stil braucht keine Normal-Maps |
| Board-Haupttextur | 2048×2048 | BC7 | ETC2 | `.webp` Quelle |
| Board-Tiling-Texturen | 512×512 | BC7 | ETC2 | Wiederholende Texturen (Sand, Gras, Lava, Eis, Wolken) |
| UI-Elemente | 256–512 | VRAM unkomprimiert | ASTC 4×4 | `.webp` / `.png` |
| Partikel (Flipbook) | 128×128 | BC7 | ETC2 | Kleine Texturen, viele Frames |
| Ramp-Textur (Toon) | 32×1 Pixel | Keine (zu klein) | Keine | 1D-LUT, unkomprimiert fur Genauigkeit |
| Color LUT | 32×32×32 | Keine (zu klein) | Keine | 3D-LUT, unkomprimiert fur Genauigkeit |
| Thumbnails (Menu) | 512×288 | BC7 | ASTC | Minispiel- und Board-Vorschau |

#### 3.6.3 Textur-Import-Einstellungen (Godot)

- **Mipmaps:** Aktiviert fur alle Texturen grosser als 64px (Standard).
- **Filter:** Linear (Bilinear) fur alle Texturen.
- **Anisotropic Filtering:** 4× (Standard, konfigurierbar in Video-Optionen: 2× / 4× / 8×).
- **VRAM Compression:** BC7 (Desktop), ETC2 (Mobile). ASTC 4×4 fur UI auf Mobile.
- **Lossy Quality:** 0.85 (85 % — akzeptabler Qualitatsverlust fur deutliche Grossenreduktion).

#### 3.6.4 Audio

| Typ | Codec | Bitrate | Kanale | Sample-Rate | Ziel-Grosse pro Datei |
|---|---|---|---|---|---|
| Musik (Board, 3–5 Min.) | OGG Vorbis | 128 kbps | Stereo | 44100 Hz | ~3 MB |
| Musik (Menu, 3–4 Min.) | OGG Vorbis | 128 kbps | Stereo | 44100 Hz | ~1.5 MB |
| Musik (Minispiel, 1–2 Min.) | OGG Vorbis | 96 kbps | Stereo | 44100 Hz | ~1.5 MB |
| SFX (UI) | OGG Vorbis | 64 kbps | Mono | 44100 Hz | < 100 KB |
| SFX (Gameplay) | OGG Vorbis | 96 kbps | Mono | 44100 Hz | < 300 KB |
| Stimme (Arenians) | OGG Vorbis | 96 kbps | Mono | 44100 Hz | < 200 KB pro Line |

**Audio-Pooling:** Haufig verwendete SFX (UI-Klicks, Schritte, Munzen-Sammeln) werden nach dem ersten Laden im RAM gehalten. Weniger haufige SFX werden nach Bedarf von Disk gestreamt und dann verworfen.

#### 3.6.5 Partikel-System

- **Engine:** `GPUParticles3D` (nicht `CPUParticles3D`). GPU-Partikel sind massiv schneller, da die Simulation auf der GPU lauft.
- **Max gleichzeitige Partikel global:** 100. Dies schliesst ALLE aktiven Partikel-Systeme ein — Munz-Effekte, Stern-Funken, Event-Effekte, Minispiel-Effekte, Konfetti bei Siegerehrung.
- **Partikel-Pooling:** Partikel-Systeme werden nicht standig erstellt/zerstort, sondern aus einem vorinitialisierten Pool aktiviert (`set_emitting(true)`) und deaktiviert (`set_emitting(false)`).
- **Max Partikel pro System:** 30 (z.B. ein Munz-Regen-System hat 30 Partikel, 8 gleichzeitige = 240 — wurde das Limit uberschreiten. Daher: Max 3 gleichzeitige Munz-Systeme).
- **Prioritat:** Aktiver Spieler → andere Spieler. Partikel-Systeme des aktiven Spielers werden nie deaktiviert.
- **Pool-Uberlauf:** Wenn das 100-Partikel-Limit erreicht ist und ein weiteres System aktiviert werden soll, wird das alteste inaktive System gestoppt (seine Partikel sterben sofort).

### 3.7 GDScript-Performance

#### 3.7.1 Vermeidbare Performance-Fallen

| Falle | Problem | Vermeidungs-Strategie | Gesch"atzter Impact |
|---|---|---|---|
| `get_node()` in `_process()` | Jeder `get_node()`-Aufruf traversiert den Node-Baum (kostet ~0.01ms). In `_process()` bei 60fps summiert sich das. | Nodes einmal in `@onready var _node = $Path/To/Node` cachen. | Bis zu 0.5ms/Frame bei 50 get_node-Aufrufen. |
| String-Operationen in Loops | Jede `String.format()` erzeugt neue Strings (Allokation). | Strings vor Loops erstellen. `+` bevorzugen, `format()` nur auserhalb von Loops. | 0.1–0.3ms/Frame bei intensiven String-Ops. |
| Viele `_process()` Nodes | Jede Node mit `_process(delta)` kostet CPU, auch wenn sie nichts tut. | Keine `_process()` auf reinen UI-Elementen. Nur Game-Logik und Animationen. | 0.05ms pro leerer _process-Node. |
| Dictionary-Zugriff in heissen Loops | `.get(key, default)` hat Overhead durch Default-Erzeugung. | Direkten Key-Zugriff (`dict[key]`) nutzen, Existenz vorher prufen. | 0.02ms pro 1000 .get()-Aufrufe. |
| Tiefe Node-Hierarchien | `get_node()` traversiert jeden Schritt der Hierarchie. | Flache Szenen: max 4 Ebenen tief. Keine `../../`-Pfade. | 0.01ms pro Hierarchie-Ebene. |
| RPC-Overhead | Jeder RPC serialisiert, sendet, empfangt und deserialisiert Daten. | RPCs bundeln: Statt 8 einzelne `_rpc_sync_player` → ein `_rpc_sync_all_players` mit Array. | Bis zu 1ms/Frame bei 8 einzelnen RPCs. |
| `var_to_bytes()` in heissen Pfaden | Serialisierung ist teuer (0.1–0.5ms). | Nur fur Server-State-Updates verwenden (nicht fur jeden Minispiel-Input). | 0.1–0.5ms pro Aufruf. |

#### 3.7.2 Static Typing — Performance-Vorteil

Alle GDScript-Funktionen MUSSEN statische Typen verwenden. Dies ist nicht nur Code-Qualitat, sondern auch Performance:

- **Static-Typed GDScript lauft bis zu 50 % schneller** als Dynamic-Typed (laut Godot-eigener Dokumentation, bestatigt durch Benchmarks).
- Der Compiler kann optimierte Bytecode-Pfade fur statisch typisierte Variablen verwenden — kein Runtime-Type-Check bei jedem Variablenzugriff.
- Keine Variant-Boxing/Unboxing-Operationen.

**Durchsetzung:** CI-Script pruft alle `.gd`-Dateien auf `func name(...):` ohne `-> ReturnType`. Fehlende Typen → Build-Fehler. Bereits angewendet: Der Skill-Pitfall #1 Fix (Commit `f7d7c94`) hat `:=` durch `:Type` ersetzt.

#### 3.7.3 Garbage Collection / Memory Management

Godot verwendet **Reference Counting** (keinen Tracing-GC). Das bedeutet:

- **Kein "Stop-the-World"-GC-Pause.** Objekte werden sofort freigegeben, wenn der letzte Reference verschwindet. Ideal fur Echtzeit-Spiele.
- **ABER:** Zyklische Referenzen werden **NIE** freigegeben (Memory Leak). Vermeide Zyklen: Parent halt Child-Referenz, Child halt NIEMALS Parent-Referenz.
- **Stattdessen:** Verwende `weakref()` fur optionale Ruckwarts-Referenzen. Beispiel: Child kennt Parent? → `var _parent_ref: WeakRef = weakref(parent)`. Zugriff: `var parent = _parent_ref.get_ref()`.
- **Minispiel-Cleanup:** Nach jedem Minispiel: `queue_free()` auf das Root-Node des Minispiels. Godot freed rekursiv alle Children. Kein manuelles Aufraumen notig.
- **Signal-Verbindungen trennen:** Vor `queue_free()` alle Signal-Connections mit `disconnect()` trennen, um Dangling-References zu vermeiden.

### 3.8 Splitscreen-Optimierung

Splitscreen (2–4 Spieler) ist das teuerste Rendering-Szenario: Jede Split-View rendert die gesamte Szene aus ihrer Perspektive.

#### 3.8.1 Viewport-Optimierungen

| Optimierung | Beschreibung | Ersparnis |
|---|---|---|
| **Reduzierte Sichtweite** | Jeder Split-Viewport hat reduzierte Render-Distanz (`camera.far = 50.0` statt 100.0). Entfernte Felder werden nicht gerendert. | ~10 % GPU |
| **Eigenes Frustum Culling** | Jeder Viewport hat eigene Kamera → Frustum Culling arbeitet pro Split. Nur was im jeweiligen Sichtfeld liegt, wird gerendert. | ~15 % GPU (2P) bis ~30 % GPU (4P) |
| **Reduzierte Auflosung** | Split-Views rendern in niedrigerer Auflosung: 4-Split → 960×540 pro View (nur 25 % der Pixel von Fullscreen). | ~40 % GPU (4P vs. 4× Fullscreen) |
| **Geteilte Beleuchtung** | Lichter werden NUR einmal berechnet (nicht pro Viewport). Godot's Forward+ Clustered Lighting ist Viewport-ubergreifend. | ~5 % GPU |
| **Kein Post-Processing pro Split** | Vignette und Color-Grading werden nur auf den finalen zusammengesetzten Frame angewandt, nicht pro Split-View. | ~2 % GPU |

#### 3.8.2 Splitscreen-Formate und Kosten

| Spieler | Split-Layout | Effektive Auflosung pro View | Relativer Rendering-Aufwand (vs. 1P Fullscreen) |
|---|---|---|---|
| 1 (Fullscreen) | 1920×1080 | 1920×1080 | 1.0× (Baseline) |
| 2 (Horizontal) | Je 960×1080 | 960×1080 | ~1.2× (zwei Kameras, aber jeweils halbe Breite → ~60 % der Pixel gesamt) |
| 3 (1 oben, 2 unten) | Oben: 1920×720, Unten: je 960×360 | Gemischt | ~1.3× |
| 4 (2×2 Grid) | Je 960×540 | 960×540 | ~1.5× (vier Kameras, aber nur 25 % der Pixel von Fullscreen → effektiv ~50 % der GPU-Last von 4× Fullscreen) |
| 5–8 (Shared Screen) | 1920×1080 | 1920×1080 (eine Kamera) | 1.0× (wie Single-Player — gunstigster Modus) |

**Shared-Screen-Strategie (5–8 Spieler):** Nur EINE Kamera. Die Kamera folgt dem aktiven Spieler mit weichem Tween (Lerp 0.1). Alle 8 Spieler-Figuren sind auf dem gleichen Bildschirm sichtbar. Dies ist die einfachste und performanteste Losung fur grosse Gruppen.

### 3.9 Minispiel-Ladezeiten

#### 3.9.1 Plugin-Lademechanismus

1. **Beim Spielstart:** Alle 12 Minispiel-PCKs werden in einen RAM-Cache geladen. PCK-Parsing dauert ~0.5s pro PCK × 12 = 6s gesamt (parallel zum Board-Intro, fur Spieler unsichtbar).
2. **Preloading:** Wahrend der `MOVE`-Phase des letzten Spielers vor der Minispiel-Phase wird das erwartete Minispiel im Hintergrund vorbereitet (Szenen-Ressourcen aus PCK extrahieren, aber noch nicht instanziieren).
3. **Bei Trigger:** Minispiel-Szene wird aus dem Cache instanziiert. Kein Disk-I/O. Reine Node-Baum-Erstellung und `_ready()`-Chain.
4. **Async Loading (Fallback):** Falls ein Minispiel nicht im Cache ist (z.B. sehr gross, wurde verdrangt): `ResourceLoader.load_threaded_request()` (STP hat diesen Mechanismus bereits in `global.gd`). Laden im Hintergrund-Thread, Haupt-Thread blockiert nicht.

#### 3.9.2 Ladezeit-Budget (Minispiel)

| Schritt | Budget (ms) | Beschreibung |
|---|---|---|
| PCK im Cache finden | < 1 | Bereits im RAM. Hash-Lookup. |
| `ResourceLoader.load()` | < 500 | Szene aus PCK laden und parsen. |
| `instantiate()` | < 100 | Node-Baum erstellen (rekursiv). |
| `_ready()`-Chain | < 500 | Initialisierung der Minispiel-Nodes. |
| Texturen/Models auf GPU laden | < 800 | GPU-Upload (parallel zum `_ready()`). |
| **Gesamt** | **< 2000** | Unter 2.0 s Ziel. |

### 3.10 8-Spieler-spezifische Optimierungen

8 Spieler gleichzeitig auf dem Board (Shared Screen) bedeutet: 8 Charakter-Modelle + 8 Player-HUDs + 8-fache State-Updates.

#### 3.10.1 GPU-Optimierungen

| Optimierung | Beschreibung | Ersparnis |
|---|---|---|
| **GPU Instancing** | Identische Geometrie (Feld-Modelle, Props) wird via `MultiMeshInstance3D` gerendert. Godot merged Draw Calls automatisch. 40 Felder → 1 Draw Call. | ~30–40 Draw Calls eingespart |
| **Character Material Instancing** | Alle 8 Arenians teilen das gleiche Toon-Shader-Material (Ramp-Textur, Parameter). Nur Diffuse-Textur und Akzentfarbe unterscheiden sich (via Shader-Parameter, kein separates Material pro Charakter). | ~8 Draw Calls eingespart |
| **Shadow-Reduktion** | Max 4 Schatten-werfende Lichter gleichzeitig. DirectionalLight-Schatten hat Prioritat 1. OmniLights werfen KEINE Schatten. | ~2ms GPU |
| **Partikel-Begrenzung** | Max 100 Partikel global. Charakter-nahe Partikel (Munz-Effekte) haben Prioritat. Hintergrund-Partikel (Ambiente) werden bei 8P reduziert. | ~0.5ms GPU |

#### 3.10.2 CPU-Optimierungen

| Optimierung | Beschreibung | Ersparnis |
|---|---|---|
| **State-Update Batching** | Server sendet ALLE 8 Spieler-Updates in EINEM RPC (`_rpc_sync_all_players` mit Array von PlayerData). Statt 8 einzelner RPCs → 1 RPC. | ~1ms CPU (Netzwerk-Serialisierung) |
| **HUD-Update Throttling** | Player-HUD wird nur bei tatsachlicher Anderung aktualisiert (nicht jedes Frame). Anderungs-Flag `hud_dirty` pro Spieler. UI-Update nur wenn Flag true. | ~0.5ms CPU (UI-Rendering) |
| **Animation LOD** | Entfernte Charaktere (nicht der aktive Spieler) spielen Animationen mit reduzierter Framerate (15 FPS statt 30 FPS). Fur das Auge kaum sichtbar (Distanz > 15 Einheiten). | ~0.3ms CPU (Animation-Blending) |
| **AI-Spieler-Optimierung** | KI-gesteuerte Spieler (Disconnect-Ersatz) fuhren vereinfachte Logik aus: Wurfeln (1 Random-Aufruf), Bewegen (keine Pfadwahl — erster Pfad), Shop (kein Kauf — pass), Minispiel (kein Input — automatisch Letzter). | Pro KI-Spieler: ~0.1ms statt ~0.5ms fur menschlichen Spieler. |

### 3.11 Speicher-Management

#### 3.11.1 Memory-Leak-Pravention

Drei kritische Regeln verhindern Memory Leaks:

1. **Alle Nodes.queue_free() nach Minispiel:** Nach jedem Minispiel wird das Root-Node des Minispiels mit `queue_free()` entfernt. Godot lost rekursiv alle Children auf. Kein manuelles `free()` notig.

2. **ResourceLoader-Pfade nicht duplizieren:** `ResourceLoader.load("res://path")` erzeugt einen neuen Resource-Handle. Wird derselbe Pfad mehrfach geladen, ohne den alten zu verwerfen, entstehen Duplikate im Speicher. Regel: Jeder Pfad wird EINMAL geladen und das Ergebnis gecached. Plugins nutzen den Cache in `plugin_system.gd`.

3. **Signal-Verbindungen trennen bei Node-Entfernung:** Vor `queue_free()` alle Signal-Connections mit `disconnect()` trennen. Andernfalls bleiben Dangling-References auf das entfernte Node bestehen (kein echtes Leak, aber "stale references", die nie aufgeraumt werden).

#### 3.11.2 Speicher-Monitoring (Entwickler-Tools)

| Tool | Was es misst | Verfugbarkeit |
|---|---|---|
| Godot Debugger → Monitors → Memory | RAM-Nutzung, Node-Count, Resource-Count, Texture-Memory | Editor (Debug-Build) |
| `--show-memory` Debug-Flag | Zeigt RAM/VRAM-Nutzung als Overlay im Spiel | Debug-Build |
| CI Memory-Test | Misst RAM nach 100 Runden mit 8 KI-Spielern. RAM muss stabil sein (±10 MB). | CI-Pipeline (Xvfb) |
| `OS.get_static_memory_usage()` | Godot-interne Speicher-Statistik | Laufzeit (Debug) |

---

## 4. Formulas

### 4.1 FPS-Berechnung und Budget-Prufung

```
Target-Frame-Zeit (Desktop) = 1.0 / 60.0 = 0.01667 s = 16.67 ms
Target-Frame-Zeit (Mobile)  = 1.0 / 30.0 = 0.03333 s = 33.33 ms

Budget-Prufung (pro Frame):
    if delta > target_frame_time + 0.002:  # 2ms Toleranz
        log_warning("Budget uberschritten: %.2f ms (Ziel: %.2f ms)" % [delta*1000, target_frame_time*1000])
        consecutive_violations += 1
    else:
        consecutive_violations = 0

    if consecutive_violations > 90:  # 1.5 Sekunden bei 60fps
        trigger_auto_scale_down()    # Render-Skalierung um 0.1 reduzieren
```

`delta` = tatsachliche Frame-Zeit in Sekunden (von Godot's `_process(delta)`).
`target_frame_time` = Ziel-Frame-Zeit basierend auf Plattform (60 FPS = 16.67ms, 30 FPS = 33.33ms).
`consecutive_violations` = Anzahl aufeinanderfolgender Budget-Uberschreitungen. Dient der Hysterese (verhindert standiges Hin- und Herschalten).

### 4.2 Draw-Call-Schatzung (pro Frame)

```
estimated_draw_calls = base + (characters * 8) + props + ui + post_processing

Wobei:
    base = 100 + (board_complexity * 10)  # Board-Geometrie. board_complexity 1–5.
    characters = active_characters  # 1–8
        8 = Draw Calls pro Charakter (Mesh + Material + Outline-Hull)
    props = 30  # Dekoration (Palmen, Steine, etc. — via MultiMeshInstance3D)
    ui = 30  # HUD-Elemente (statisch, nur bei Anderung)
    post_processing = 2  # Color-Grading + Vignette

Beispiele:
    1 Spieler, einfaches Board:  100 + (1*8) + 30 + 30 + 2 = 170
    8 Spieler, komplexes Board:  100 + (8*8) + 30 + 30 + 2 = 226
    4 Spieler Splitscreen:       ~350 (4× frustum-culled Render-Pass)

Budget: 500 Draw Calls Maximum. Tatsachlich erwartet: 150–250.
```

### 4.3 Speicher-Schatzung (RAM)

```
estimated_ram_mb = engine + board + characters + minigame_cache + audio + ui + network + internals + reserve

Wobei:
    engine = 150           # Godot Baseline
    board = 100            # Aktives Board + Texturen
    characters = 10 * 8    # 8 Charaktere (Modell + Texturen pro Charakter)
    minigame_cache = 100   # 12 Minispiele im RAM
    audio = 80             # Musik-Streaming + SFX-Cache
    ui = 50                # UI-Texturen unkomprimiert
    network = 20           # ENet-Puffer + RPC-Queues
    internals = 120        # Godot-Interna (Nodes, Signals, Variablen)
    reserve = 100          # OS-Overhead + Puffer

Total typisch: 800 MB
Total Maximum: 1500 MB (1.5 GB)
```

### 4.4 Ladezeit-Schatzung (Minispiel)

```
estimated_load_time_s = (disk_io + instantiate + ready + gpu_upload) / 1000.0

Wobei:
    disk_io = 0            # ms (Cache-Hit = 0, Cache-Miss = minigame_pck_size_mb * 10)
    instantiate = 100      # ms (Node-Baum rekursiv erstellen)
    ready = 500            # ms (_ready-Chain aller Nodes)
    gpu_upload = pck_size_mb * 50  # ms (Texturen/Models auf GPU ubertragen)

Beispiele:
    5 MB Minispiel, Cache-Hit:  (0 + 100 + 500 + 250) / 1000 = 0.85 s
    10 MB Minispiel, Cache-Hit: (0 + 100 + 500 + 500) / 1000 = 1.10 s
    10 MB Minispiel, Cache-Miss: (10*10 + 100 + 500 + 500) / 1000 = 1.20 s
```

### 4.5 Auto-Tuning-Performance-Level

```
performance_level = detect_hardware_level()

detect_hardware_level():
    vram_mb = RenderingServer.get_video_adapter_vram()
    gpu_name = RenderingServer.get_video_adapter_name().to_lower()

    if vram_mb < 256:
        return 0  # ULTRA_LOW
    elif vram_mb < 512 or "uhd" in gpu_name or "intel" in gpu_name:
        return 1  # LOW
    elif vram_mb < 2048:
        return 2  # MEDIUM
    else:
        return 3  # HIGH
```

---

## 5. Edge Cases

1. **Frame-Drop-Kaskade:** Ein Frame uberschreitet das Budget (z.B. 25ms statt 16.67ms). Der nachste Frame versucht, die verlorene Zeit aufzuholen. **Verhalten:** Godot ubergibt immer das tatsachliche Delta in `_process(delta)`. Frame-Drops sind isoliert — ein langsamer Frame fuhrt nicht zu mehreren langsamen Frames. Teure Operationen (Plugin-Laden, State-Deserialisierung) werden NIE im Haupt-Thread ausgefuhrt — nur wahrend Ladebildschirmen oder via `ResourceLoader.load_threaded_request()` im Hintergrund-Thread.

2. **Splitscreen mit 4 Spielern auf Minimum-Hardware:** 4-Spieler-Splitscreen auf Intel UHD 620 mit 60 FPS Ziel. **Risiko:** 4× Rendering konnte 60 FPS gefahrden. **Mitigation (abgestuft):**
   - Stufe 1: Reduziere `scaling_3d_scale` auf 0.8 (automatisch, wenn FPS < 55 fur >2 Sekunden).
   - Stufe 2: Reduziere LOD-Distanz: LOD1 ab 10 Einheiten (statt 20). Weniger hochauflosende Modelle.
   - Stufe 3: Deaktiviere Schatten komplett (`DirectionalLight.shadow_enabled = false`). Grosste Ersparnis (~2ms).
   - Stufe 4 (letzte Moglichkeit): Reduziere Ziel-FPS auf 30 FPS fur Splitscreen-Modus. Zeige Warnung: "Performance-Modus aktiv (30 FPS)".

3. **Speicher-Leak durch zyklische Referenzen:** Ein Minispiel erstellt Objekte mit zyklischen Referenzen (A halt Ref auf B, B halt Ref auf A). Godot's Reference-Counting gibt diese NIE frei. **Pravention:** Code-Review-Regel: Keine zyklischen Referenzen. `weakref()` fur optionale Ruckwarts-Referenzen. Minispiel-Cleanup: `queue_free()` auf Root-Node. Memory-Profiling nach jedem Minispiel (RAM muss auf Pre-Minigame-Level sinken).

4. **Audio-Streaming-Unterbrechung:** Wahrend eines Minispiels muss die Board-Musik stoppen und Minispiel-Musik starten. Harte Unterbrechung klingt schlecht. **Verhalten:** Crossfade uber 500ms: Board-Musik fadet aus, Minispiel-Musik fadet ein. Audio-Thread-Last steigt kurzfristig (2 Streams gleichzeitig), aber Audio-Budget (1ms) reicht.

5. **Viele Partikel-Gleichzeitigkeit:** 8 Spieler sammeln gleichzeitig Munzen ein → 8 Munz-Partikel-Systeme aktiv. **Verhalten:** Pool-Limit = 100 Partikel global. Jedes Munz-System hat 10 Partikel → 8×10 = 80 (im Budget). Wenn ein 9. System aktiviert wurde (88 Partikel → uberschritten): Das alteste System des am wenigsten relevanten Spielers wird deaktiviert. Prioritat: Aktiver Spieler > nahe Spieler > entfernte Spieler.

6. **VSync und Input-Lag:** VSync verhindert Screen-Tearing, fuhrt aber potenziell Input-Lag ein (1–2 Frames = 16–33ms). **Losung:** VSync ist standardmassig aktiviert. Godot's "Mailbox"-VSync-Modus wird verwendet (niedrigster Lag). Im Options-Menu deaktivierbar. Fur Minispiele: Input wird im `_process()` gepollt, nicht im `_input()` (reduziert Lag um 1 Frame).

7. **GDScript-Performance bricht bei 8 KI-Spielern ein:** Ein Benchmark mit 8 KI-Spielern im Stress-Test zeigt erhohte GDScript-Zeit. **Mitigation:** KI-Logik ist vereinfacht. KI fuhrt keine aufwandigen Berechnungen aus (keine Pfad-Optimierung, keine Item-Strategie). KI-Zug dauert < 0.1ms (vs. menschlicher Zug mit UI-Interaktion: ~0.5ms). 8 KI-Spieler sind performanter als 8 menschliche.

8. **Textur-Upload auf GPU blockiert Haupt-Thread:** Beim ersten Laden einer Textur muss sie auf die GPU hochgeladen werden — das blockiert den Haupt-Thread kurz. **Mitigation:** Texturen werden wahrend Ladebildschirmen vorgeladen (nicht wahrend des Gameplays). `ResourceLoader.load_threaded_request()` ladt im Hintergrund-Thread (Textur-Daten im RAM), der GPU-Upload erfolgt im Haupt-Thread, ist aber kurz (< 1ms pro Textur bei 1024²).

9. **Low-Quality-Fallback aktiviert sich ungewollt:** Ein kurzer Frame-Drop (z.B. durch OS-Hintergrundprozess) lost die Auto-Skalierung aus. **Verhalten:** Hysterese: Erst nach 90 aufeinanderfolgenden Frame-Drops (1.5s bei 60fps) wird skaliert. Kurze Aussetzer werden ignoriert. Skalierung wird nach 5 Sekunden stabiler FPS wieder zuruckgenommen.

10. **Mobile: App wird in Hintergrund geschoben:** Auf iOS/Android wird das Spiel pausiert, wenn die App in den Hintergrund geht. **Verhalten:** Godot's `NOTIFICATION_WM_FOCUS_OUT` wird emittiert. Spiel pausiert (kein `_process`-Tick). Audio stoppt. Beim Zuruckkehren: Spiel setzt fort (kein Neustart). Im Online-Modus: Client disconnect nach 30s Inaktivitat.

---

## 6. Dependencies

### 6.1 Interne Abhangigkeiten

| Performance-Aspekt | Abhangigkeit | Grund |
|---|---|---|
| Draw-Call-Budget | `technical-architecture.md` (Renderer-Wahl: Forward+) | Forward+ definiert Draw-Call-Kosten. |
| Speicher-Budget | `technical-data-structures.md` (PlayerData, BoardData, FieldData) | Datenstrukturen belegen RAM. |
| Minispiel-Ladezeit | `technical-fork-strategy.md` (Plugin-System) | Minispiele sind Plugins (.pck/.zip). |
| Splitscreen-Performance | `technical-multiplayer.md` (8P-Erweiterung) | Splitscreen hangt von Spielerzahl und Viewport-Konfiguration ab. |
| LOD-System | Asset-Pipeline (3D-Modelle, `assets/models/`) | LOD-Modelle mussen von Artists erstellt werden. |
| Auto-Tuning | `client/menus/options_menu.gd` (Video-Einstellungen) | Auto-Tuning beeinflusst dieselben Parameter wie das Options-Menu. |
| Shader (Toon, Board) | `assets/textures/` (Ramp-Textur) | Ramp-Textur ist Input fur den Toon-Shader. |

### 6.2 Externe Abhangigkeiten

| Abhangigkeit | Zweck |
|---|---|
| Godot 4.2 Profiler | Frame-Zeit-Analyse (CPU, GPU), GDScript-Funktionsaufruf-Zahlung, Signal-Count. |
| Godot Debugger → Monitors | Speicher-Tracking (RAM, VRAM), Node-Count, Resource-Count. |
| Vulkan Validation Layers | GPU-Debugging (optional, nur bei Grafikproblemen). |
| RenderDoc | GPU-Frame-Capture und Draw-Call-Analyse (optional, nur bei Grafikproblemen). |
| Xvfb (CI) | Headless-Rendering fur automatisierte Performance-Tests (CPU-seitig). GPU-Tests sind in CI nicht moglich. |
| `benchmark.gd` (Custom) | Automatisierte Performance-Test-Szene: 8 KI-Spieler, 100 Runden, alle Minispiele. Misst Frame-Zeit, RAM, Ladezeiten. |

### 6.3 Keine externen Performance-Tools

- **Kein** Superluminal / Tracy / Optick (C++ Profiler) — GDScript-only Profiling via Godot's integrierten Profiler reicht fur unseren Scope.
- **Kein** PIX / GPUView (Windows GPU Tools) — zu komplex fur ein Cartoon-Spiel, Overkill.
- **Kein** Instruments (macOS) — optional fur macOS-Entwickler, aber nicht Pflicht.

---

## 7. Tuning Knobs

### 7.1 Grafik-Einstellungen (Video-Optionen-Menu)

| Einstellung | Optionen | Standard | Performance-Impact |
|---|---|---|---|
| **Auflosung** | 1280×720, 1600×900, 1920×1080, 2560×1440 | 1920×1080 | Linear: 4K = 4× Pixel von 1080p = ~2.5× GPU-Last. |
| **Vollbild** | Fenster, Randlos, Vollbild | Randlos | Minimal (Vollbild kann 1–3 % schneller sein als Fenster). |
| **VSync** | Aus, An | An | Kein Performance-Impact (verhindert nur Tearing). |
| **Anti-Aliasing** | Aus, MSAA 2×, MSAA 4×, TAA | TAA | MSAA 4×: ~1.5ms. TAA: ~0.5ms. |
| **Render-Skalierung** | 0.5, 0.6, 0.7, 0.8, 0.9, 1.0 | 1.0 | Gro"sster Hebel: 0.5 = ~25 % GPU-Last (50 % × 50 % = 25 % Pixel). |
| **Schatten** | Aus, Niedrig (1024), Mittel (2048) | Niedrig | Niedrig→Aus: ~2ms Ersparnis. Mittel: ~1ms teurer. |
| **Textur-Qualitat** | Niedrig (1/2 Aufl.), Mittel (3/4), Hoch (voll) | Hoch | Beeinflusst VRAM-Nutzung, kaum GPU-Last-Anderung. |
| **Partikel** | Aus, Wenige (50), Normal (100) | Normal | Wenige = 50 % Partikel → ~0.2ms Ersparnis. Aus = keine Partikel. |

### 7.2 Performance-Auto-Tuning (Runtime)

Das Spiel erkennt automatisch die Hardware-Leistung und setzt passende Einstellungen. Die Erkennung geschieht beim ersten Spielstart und ist im Options-Menu uberschreibbar.

| Level | Erkennungskriterium | Render-Skalierung | Schatten | AA | Partikel | Textur-Qualitat |
|---|---|---|---|---|---|---|
| **0 (Ultra-Low)** | VRAM < 256 MB ODER "uhd" im GPU-Namen | 0.6 | Aus | Aus | Wenige (50) | Niedrig |
| **1 (Low)** | VRAM < 512 MB ODER "intel" im GPU-Namen | 0.8 | Niedrig (1024) | TAA | Normal (100) | Mittel |
| **2 (Medium)** | VRAM < 2048 MB | 1.0 | Niedrig (1024) | TAA + MSAA 2× | Normal (100) | Hoch |
| **3 (High)** | VRAM >= 2048 MB | 1.0 | Mittel (2048) | TAA + MSAA 4× | Normal (100) | Hoch |

### 7.3 Developer-Debug-Flags (fur Profiling, nicht im Release)

| Flag | Beschreibung |
|---|---|
| `--show-fps` | Zeigt FPS-Counter als Overlay (Ecke oben-rechts). Farbe: Grun >55, Gelb 30–55, Rot <30. |
| `--show-draw-calls` | Zeigt Draw-Call-Zahler pro Frame. |
| `--show-memory` | Zeigt RAM/VRAM-Nutzung als Overlay. |
| `--profile-gdscript` | Aktiviert Godot's GDScript-Profiler (Ausgabe in Konsole nach Spielende). |
| `--stress-test-8p` | Simuliert 8 KI-Spieler fur Performance-Tests (automatisch, keine Eingabe notig). |
| `--fixed-seed 12345` | Fixiert den Zufalls-Seed fur reproduzierbare Performance-Tests. |
| `--skip-minigames` | Uberspringt Minispiele (automatisch generierte Ergebnisse). Fur Board-only-Performance-Tests. |

### 7.4 CI-Performance-Schwellwerte

| Metrik | Warnung | Fehler (Block) | Beschreibung |
|---|---|---|---|
| Frame-Zeit (Durchschnitt, 8P-Stress-Test) | > 10ms | > 16.67ms | Gemessen uber 100 Runden im Headless-Modus (Xvfb). Nur CPU-seitig. |
| GDScript-Funktionsaufrufe pro Frame | > 500 | > 1000 | Gemittelt uber die Stress-Test-Dauer. |
| RAM (Peak) | > 1.2 GB | > 1.5 GB | Maximale RAM-Nutzung wahrend des Tests. |
| RAM (Leak-Test) | Anstieg > 50 MB uber Testdauer | Anstieg > 100 MB | RAM nach 100 Runden minus RAM zu Beginn. |
| Minispiel-Ladezeit (Durchschnitt) | > 2.0s | > 2.5s | Gemittelt uber alle 12 Minispiele. |
| Minispiel-Ladezeit (Worst-Case) | > 2.5s | > 3.0s | Das langsamste der 12 Minispiele. |
| Board-Ladezeit | > 3.0s | > 4.0s | Vom Board-Select bis zum ersten spielbaren Frame. |

---

## 8. Acceptance Criteria

### 8.1 Desktop-Performance

- [ ] **AC-PF-001:** 60 FPS stabil (Durchschnitt >= 59 FPS) auf Intel i5-8250U, 8GB RAM, Intel UHD 620, 1920×1080, 8 Spieler Shared Screen, 10 Runden inkl. aller Minispiele. Gemessen uber eine vollstandige Partie.
- [ ] **AC-PF-002:** 60 FPS stabil auf gleicher Hardware mit 4-Spieler-Splitscreen (2×2, je 960×540).
- [ ] **AC-PF-003:** 60 FPS stabil in ALLEN 12 Minispielen mit 8 Spielern.
- [ ] **AC-PF-004:** Frame-Zeit uberschreitet in < 1 % der Frames das Budget (16.67ms). Gemessen uber eine volle 10-Runden-Partie.
- [ ] **AC-PF-005:** Draw Calls < 500 in allen Spielszenarien (Board 8P Shared Screen ist das teuerste Szenario).
- [ ] **AC-PF-006:** Framerate bricht im Splitscreen-Modus (2–4P) nicht unter 55 FPS ein.

### 8.2 Speicher

- [ ] **AC-PF-007:** RAM-Nutzung < 1.5 GB wahrend einer 10-Runden-Partie mit 8 Spielern inkl. aller Minispiele.
- [ ] **AC-PF-008:** RAM-Nutzung sinkt nach jedem Minispiel-Ende auf Pre-Minigame-Niveau (±10 MB). Kein kontinuierlicher RAM-Anstieg uber die Spieldauer (Memory-Leak-Test).
- [ ] **AC-PF-009:** VRAM-Nutzung < 512 MB auf Intel UHD 620 im 8-Spieler-Shared-Screen-Modus.
- [ ] **AC-PF-010:** RAM-Nutzung nach 100 Runden KI-Stress-Test < 1.5 GB und innerhalb von ±50 MB der Nutzung nach 10 Runden.

### 8.3 Ladezeiten

- [ ] **AC-PF-011:** Spielstart (kalt, SSD): < 5 Sekunden bis zum Hauptmenu. Gemessen vom Prozess-Start bis zum ersten interaktiven Frame.
- [ ] **AC-PF-012:** Spielstart (kalt, HDD): < 10 Sekunden.
- [ ] **AC-PF-013:** Board laden: < 3 Sekunden von Board-Auswahl bis zum ersten spielbaren Frame.
- [ ] **AC-PF-014:** Minispiel laden (Durchschnitt): < 2 Sekunden. Gemittelt uber alle 12 Minispiele.
- [ ] **AC-PF-015:** Minispiel laden (Worst-Case): < 3 Sekunden. Das langsamste Minispiel.
- [ ] **AC-PF-016:** Menu-Ubergang (z.B. Hauptmenu → Optionen): < 0.5 Sekunden. Fuhlt sich instant an.

### 8.4 Anti-Aliasing und Visuelle Qualitat

- [ ] **AC-PF-017:** TAA ist aktiv. Keine sichtbaren flimmernden Kanten bei Stillstand auf 1920×1080.
- [ ] **AC-PF-018:** Toon-Shader ist auf allen Charakter-Modellen aktiv (Cel-Shading mit 2–3 Tonen sichtbar). Verifiziert durch Sichtprufung: Harte Ubergange zwischen Schatten/Mittel/Highlight auf Charakteren.
- [ ] **AC-PF-019:** Keine Screen-Tearing-Effekte (VSync an, getestet auf 60Hz Monitor).
- [ ] **AC-PF-020:** LOD-Ubergang (LOD0→LOD1) ist fur das blosse Auge nicht storend (Transparenz-Blend uber 2 Einheiten, getestet bei verschiedenen Kamerawinkeln).

### 8.5 Audio

- [ ] **AC-PF-021:** Musik-Ducking: Musik wird um 6 dB abgesenkt, wenn SFX abgespielt werden. Subjektiv horbar, aber nicht storend.
- [ ] **AC-PF-022:** Audio-Crossfade zwischen Board- und Minispiel-Musik: Kein harter Cut, sanfter Ubergang (500ms Fade).
- [ ] **AC-PF-023:** Kein Knacken/Poppen bei Sound-Effekten (kein DC-Offset, Fades an Start/Ende von Samples < 5ms).
- [ ] **AC-PF-024:** Keine Audio-Aussetzer bei Frame-Drops (Audio lauft in eigenem Thread).

### 8.6 Assets

- [ ] **AC-PF-025:** Alle Charakter-Modelle: Max 5000 Tris (LOD0), Max 1500 Tris (LOD1). Verifiziert durch Modell-Inspektion in Blender/Godot.
- [ ] **AC-PF-026:** Alle Board-Modelle (komplett): Max 20000 Tris. Verifiziert durch Modell-Inspektion.
- [ ] **AC-PF-027:** Alle Charakter-Texturen: Max 1024×1024, BC7-komprimiert. Keine 2048² oder grossere Texturen fur Charaktere.
- [ ] **AC-PF-028:** Alle Board-Texturen: Max 2048×2048, BC7-komprimiert.
- [ ] **AC-PF-029:** Alle Audio-Dateien: OGG Vorbis. Musik: 128kbps Stereo. SFX: 64–96kbps Mono. Stimme: 96kbps Mono. Keine unkomprimierten WAV-Dateien im Build.

### 8.7 Partikel

- [ ] **AC-PF-030:** Max 100 gleichzeitige Partikel global. Uberschreitung wird vom Pool-System verhindert (alteste Systeme werden deaktiviert).
- [ ] **AC-PF-031:** Alle Partikel-Systeme verwenden `GPUParticles3D` (nicht `CPUParticles3D`). Verifiziert durch Code-Review.

### 8.8 Shader und Post-Processing

- [ ] **AC-PF-032:** Nur Color-Grading (LUT) und Vignette sind als Post-Processing aktiv. Verifiziert in `project.godot`: SSAO, SSIL, SSR, Glow, DOF, Motion Blur sind deaktiviert.
- [ ] **AC-PF-033:** Toon-Shader: Ramp-Textur (32×1 Pixel) wird fur Cel-Shading verwendet. Verifiziert durch Sichtprufung und Shader-Code-Inspektion.
- [ ] **AC-PF-034:** Outlines sind via Inverted-Hull-Methode realisiert (kein Geometry-Shader). Verifiziert durch Modell-Inspektion: Charakter-Modelle haben doppelte Geometrie mit invertierten Normalen.

### 8.9 Splitscreen

- [ ] **AC-PF-035:** 2-Spieler-Splitscreen: >= 58 FPS auf Minimum-Hardware (Intel UHD 620).
- [ ] **AC-PF-036:** 4-Spieler-Splitscreen: >= 55 FPS auf Minimum-Hardware.
- [ ] **AC-PF-037:** 5–8 Spieler (Shared Screen): >= 60 FPS auf Minimum-Hardware (performanter als Splitscreen, da nur eine Kamera).
- [ ] **AC-PF-038:** Split-Viewports rendern in reduzierter Auflosung (960×540 bei 4-Split) und mit reduziertem `camera.far`.

### 8.10 Performance-Testing (CI und Automatisiert)

- [ ] **AC-PF-039:** CI-Test (Xvfb, Headless): Durchschnittliche Frame-Zeit < 10ms (CPU-seitig, ohne GPU). Build schlagt fehl bei Uberschreitung.
- [ ] **AC-PF-040:** 10-Runden-Spiel (8P, alle Minispiele, KI-gesteuert): RAM-Nutzung steigt nicht kontinuierlich an (Leak-Test bestanden: RAM Ende − RAM Start < 50 MB).
- [ ] **AC-PF-041:** 100-Runden-Stress-Test (8 KI-Spieler): Keine Crashes, keine Standbilder, RAM stabil.
- [ ] **AC-PF-042:** GDScript-Funktionsaufrufe pro Frame < 500 im Durchschnitt (gemessen uber Stress-Test).

### 8.11 Auto-Tuning

- [ ] **AC-PF-043:** Auto-Tuning erkennt schwache Hardware korrekt (Intel UHD 620 → Level 1 "Low").
- [ ] **AC-PF-044:** Auto-Tuning lost keine ungewollte Skalierung aus (Hysterese: erst nach >90 aufeinanderfolgenden Frame-Drops).
- [ ] **AC-PF-045:** Bei manueller Einstellung im Options-Menu wird Auto-Tuning deaktiviert (manuelle Einstellungen haben Vorrang).

### 8.12 Mobile/Konsole (Post-Launch Ziele)

- [ ] **AC-PF-046:** Steam Deck: 60 FPS stabil auf 1280×800 mit Medium-Einstellungen (Level 2).
- [ ] **AC-PF-047:** Snapdragon 7 Gen 2 (Android): 30 FPS stabil auf nativer Auflosung mit Forward Mobile Renderer und Low-Einstellungen (Level 1).
- [ ] **AC-PF-048:** Switch 2 (Ziel): 30 FPS stabil auf 1080p Docked / 720p Handheld, Forward Mobile Renderer.

---

> **Nachste Datei:** `README.md` — Master-Index fur design/gdd/
> **Vollstandige GDD-Referenz:** `bible-index.md`, `systems-index.md`
> **Vorherige Dateien:** `technical-architecture.md`, `technical-multiplayer.md`, `technical-fork-strategy.md`, `technical-data-structures.md`
> **Ubergeordnet:** `game-concept.md`, `vision-pillars.md`, `core-loop.md`
