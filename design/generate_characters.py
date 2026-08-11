#!/usr/bin/env python3
"""V3: Die 8 Arenians — professionell stylisiert mit Subdivision + Bevel + PBR.
Gemäß blender-headless-assets Skill (Professional Stylized Workflow):
- Subdivision Surface modifier (Level 2) auf Köpfe/Körper → weiche, runde Formen
- Bevel modifier → abgerundete Kanten (Toy-Look, keine harten Ecken)
- Höhere Segment-Zahlen für glatte Kugeln
- PBR-Materialien (Noise-Roughness, Subsurface für organisch)
- Mehr Details pro Charakter
"""
import bpy
import os
import math

OUT_DIR = "/opt/data/SuperTuxParty/plugins/characters"

def c(hexstr):
    h = hexstr.lstrip('#')
    return tuple(int(h[i:i+2], 16)/255.0 for i in (0, 2, 4)) + (1.0,)

def clear_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)

def mat(name, color, rough=0.45, subsurf=0.2, emit=0.0, emit_color=None, metal=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = rough
        bsdf.inputs["Subsurface Weight"].default_value = subsurf
        bsdf.inputs["Metallic"].default_value = metal
        if emit > 0:
            bsdf.inputs["Emission Strength"].default_value = emit
            bsdf.inputs["Emission Color"].default_value = emit_color or color
    return m

def smooth(obj, levels=2, bevel=0.02):
    """Subdivision Surface + Bevel für weiche, abgerundete Toy-Formen."""
    if levels > 0:
        sub = obj.modifiers.new("Subsurf", 'SUBSURF')
        sub.levels = levels
        sub.render_levels = levels
        sub.subdivision_type = 'SIMPLE' if 'SIMPLE' in dir(sub) else 'CATMULL_CLARK'
    if bevel > 0:
        bev = obj.modifiers.new("Bevel", 'BEVEL')
        bev.width = bevel
        bev.segments = 3
        bev.limit_method = 'ANGLE'
        bev.angle_limit = math.radians(30)
    return obj

def prim(type_, name, color, scale=(1,1,1), loc=(0,0,0), rough=0.45, subsurf=0.2,
         emit=0.0, emit_color=None, metal=0.0, seg=48, smooth_levels=1, bevel=0.02):
    if type_ == "sphere":
        bpy.ops.mesh.primitive_uv_sphere_add(radius=1.0, location=loc, segments=seg, ring_count=32)
    elif type_ == "box":
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=loc)
    elif type_ == "cyl":
        bpy.ops.mesh.primitive_cylinder_add(radius=1.0, depth=1.0, location=loc, vertices=seg)
    elif type_ == "cone":
        bpy.ops.mesh.primitive_cone_add(radius1=1.0, depth=1.0, location=loc, vertices=seg)
    elif type_ == "torus":
        bpy.ops.mesh.primitive_torus_add(location=loc, major_radius=1.0, minor_radius=0.3, major_segments=48, minor_segments=24)
    obj = bpy.context.active_object
    obj.name = name
    obj.scale = scale
    m = mat(f"{name}_mat", color, rough, subsurf, emit, emit_color, metal)
    if obj.data.materials:
        obj.data.materials[0] = m
    else:
        obj.data.materials.append(m)
    smooth(obj, smooth_levels, bevel)
    return obj

def limb(name, color, scale, loc, rot=(0,0,0), rough=0.45, subsurf=0.2, smooth_levels=1):
    o = prim("cyl", name, color, scale, loc, rough, subsurf, smooth_levels=smooth_levels, bevel=0.02)
    o.rotation_euler = rot
    return o

def export(name):
    # Modifier anwenden (Subsurf/Bevel) für sauberes GLB
    bpy.ops.object.select_all(action='SELECT')
    for obj in bpy.context.selected_objects:
        bpy.context.view_layer.objects.active = obj
        for mod in obj.modifiers:
            try:
                bpy.ops.object.modifier_apply(modifier=mod.name)
            except Exception:
                pass
    out = os.path.join(OUT_DIR, name, f"{name}.glb")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    bpy.ops.export_scene.gltf(filepath=out, export_format='GLB', use_selection=True)
    print(f"EXPORTED: {out}")

# ═══════════════════════════════════════════════════════════
# BRIX — Stein-Golem (eckig, massiv, übergroße Hände, Moos)
# ═══════════════════════════════════════════════════════════
def build_brix():
    clear_scene()
    ORANGE = c("#ff6a00"); MOOS = c("#5a8f3c"); FUG = c("#6b4a2f"); EYE = c("#fff3b0")
    # Körper: breiter, massiver, ECKIGER Rumpf (KEIN Subsurf → bleibt eckig)
    body = prim("box", "brix_body", ORANGE, (1.1, 0.9, 1.0), (0, 0, 0.7), rough=0.5, subsurf=0.15, smooth_levels=0, bevel=0.02)
    # Ziegelstein-Muster auf dem Rumpf (versetzte Steinreihen mit Fugen)
    # 3 Reihen, jede Reihe 3-4 Ziegel, versetzt — auf der Vorderseite (y=0.3)
    brick_rows = [
        # (y-offset, z-offset, anzahl, start_x)
        (0.3, 0.95, 3, -0.4),   # oberste Reihe
        (0.3, 0.7, 4, -0.5),    # mittlere Reihe (versetzt)
        (0.3, 0.45, 3, -0.4),   # untere Reihe
    ]
    for yoff, zoff, count, start_x in brick_rows:
        for i in range(count):
            bx = start_x + i * 0.28
            # Ziegel: hellerer Stein mit dunkler Fuge drumherum
            prim("box", f"brix_brick_{zoff}_{i}", c("#ff8c3a"), (0.24, 0.06, 0.18), (bx, yoff, zoff), rough=0.5, subsurf=0.15, smooth_levels=0, bevel=0.01)
    # Kopf: groß, eckig, sitzt direkt auf dem Rumpf (KEIN Subsurf)
    head = prim("box", "brix_head", ORANGE, (0.75, 0.65, 0.65), (0, 0, 1.55), rough=0.5, subsurf=0.15, smooth_levels=0, bevel=0.02)
    # Übergroße eckige Hände (seitlich, KEIN Subsurf)
    prim("box", "brix_hand_l", ORANGE, (0.5, 0.38, 0.38), (-0.95, 0, 0.65), rough=0.5, subsurf=0.15, smooth_levels=0, bevel=0.02)
    prim("box", "brix_hand_r", ORANGE, (0.5, 0.38, 0.38), (0.95, 0, 0.65), rough=0.5, subsurf=0.15, smooth_levels=0, bevel=0.02)
    # Arme (eckig, seitlich, KEIN Subsurf)
    limb("brix_arm_l", ORANGE, (0.38, 0.38, 0.5), (-0.75, 0, 0.95), rough=0.5, smooth_levels=0)
    limb("brix_arm_r", ORANGE, (0.38, 0.38, 0.5), (0.75, 0, 0.95), rough=0.5, smooth_levels=0)
    # Beine (eckig, kurz, breit, KEIN Subsurf)
    limb("brix_leg_l", FUG, (0.38, 0.38, 0.4), (-0.3, 0, 0.2), rough=0.6, smooth_levels=0)
    limb("brix_leg_r", FUG, (0.38, 0.38, 0.4), (0.3, 0, 0.2), rough=0.6, smooth_levels=0)
    # Moos-Flecken
    prim("sphere", "brix_moss_l", MOOS, (0.25, 0.2, 0.15), (-0.6, 0, 1.25), rough=0.8, subsurf=0.0, smooth_levels=1, bevel=0)
    prim("sphere", "brix_moss_r", MOOS, (0.25, 0.2, 0.15), (0.6, 0, 1.25), rough=0.8, subsurf=0.0, smooth_levels=1, bevel=0)
    prim("sphere", "brix_moss_back", MOOS, (0.3, 0.14, 0.18), (0, -0.45, 1.15), rough=0.8, subsurf=0.0, smooth_levels=1, bevel=0)
    # Leuchtende Augen (auf dem Kopf bei 1.55)
    prim("sphere", "brix_eye_l", EYE, (0.14, 0.12, 0.14), (-0.2, 0.35, 1.7), emit=1.0, emit_color=EYE, smooth_levels=1, bevel=0)
    prim("sphere", "brix_eye_r", EYE, (0.14, 0.12, 0.14), (0.2, 0.35, 1.7), emit=1.0, emit_color=EYE, smooth_levels=1, bevel=0)
    # Fugen (eckige Risse)
    prim("box", "brix_fuge1", FUG, (0.77, 0.07, 0.07), (0, 0, 1.25), rough=0.6, smooth_levels=0, bevel=0)
    prim("box", "brix_fuge2", FUG, (0.07, 0.6, 0.07), (0, 0, 0.9), rough=0.6, smooth_levels=0, bevel=0)
    export("brix")

# ═══════════════════════════════════════════════════════════
# NIXIE — Axolotl (Kiemen-Krone, Wassertropfen, schlank)
# ═══════════════════════════════════════════════════════════
def build_nixie():
    clear_scene()
    TURK = c("#00f0ff"); KIEM = c("#a8f8ff"); AUG = c("#1a3a4a"); TROP = c("#d0faff")
    # Echsen-Körper: horizontal, langgestreckt, kriechend am Boden
    body = prim("sphere", "nixie_body", TURK, (0.5, 0.3, 0.35), (0, 0, 0.3), subsurf=0.35, smooth_levels=1)
    # Kopf: vorne, flach, echsen-artig
    head = prim("sphere", "nixie_head", TURK, (0.3, 0.28, 0.28), (0.5, 0, 0.3), subsurf=0.35, smooth_levels=1)
    # Schnauze (Echsen-Maul)
    prim("sphere", "nixie_snout", TURK, (0.18, 0.15, 0.15), (0.75, 0, 0.28), subsurf=0.3, smooth_levels=1)
    # Kiemen (seitlich am Kopf, wie bei einer Echse)
    for i, (dx, dy, dz) in enumerate([(-0.1, 0.15, 0.1), (-0.15, 0, 0.0), (-0.1, -0.15, -0.1)]):
        prim("cone", f"nixie_gill_l{i}", KIEM, (0.1, 0.1, 0.25), (0.4+dx, dy, 0.35+dz), subsurf=0.2, smooth_levels=1, bevel=0)
    for i, (dx, dy, dz) in enumerate([(-0.1, 0.15, 0.1), (-0.15, 0, 0.0), (-0.1, -0.15, -0.1)]):
        prim("cone", f"nixie_gill_r{i}", KIEM, (0.1, 0.1, 0.25), (0.4+dx, dy, 0.35+dz), subsurf=0.2, smooth_levels=1, bevel=0)
    # Augen (oben auf dem Kopf)
    prim("sphere", "nixie_eye_l", AUG, (0.1, 0.08, 0.1), (0.5, 0.12, 0.45), subsurf=0.1, smooth_levels=1, bevel=0)
    prim("sphere", "nixie_eye_r", AUG, (0.1, 0.08, 0.1), (0.5, -0.12, 0.45), subsurf=0.1, smooth_levels=1, bevel=0)
    prim("sphere", "nixie_glint_l", c("#ffffff"), (0.03, 0.02, 0.03), (0.53, 0.12, 0.48), smooth_levels=1, bevel=0)
    prim("sphere", "nixie_glint_r", c("#ffffff"), (0.03, 0.02, 0.03), (0.53, -0.12, 0.48), smooth_levels=1, bevel=0)
    # Wassertropfen auf dem Kopf
    prim("sphere", "nixie_drop", TROP, (0.07, 0.07, 0.09), (0.5, 0, 0.6), subsurf=0.5, smooth_levels=1, bevel=0)
    # 4 kurze Beine (Echsen-Beine, seitlich)
    for side in [-1, 1]:
        limb(f"nixie_leg_f{side}", TURK, (0.08, 0.08, 0.2), (0.3, side*0.25, 0.15), subsurf=0.3, smooth_levels=1)
        limb(f"nixie_leg_b{side}", TURK, (0.08, 0.08, 0.2), (-0.3, side*0.25, 0.15), subsurf=0.3, smooth_levels=1)
    # Langer Schwanz (Echsen-Schwanz, nach hinten)
    for i in range(4):
        prim("sphere", f"nixie_tail_{i}", TURK, (0.12 - i*0.02, 0.12 - i*0.02, 0.2 - i*0.03), (-0.5 - i*0.2, 0, 0.2), subsurf=0.3, smooth_levels=1)
    export("nixie")

# ═══════════════════════════════════════════════════════════
# PIP — Eichhörnchen (buschiger Schwanz, Flughäute)
# ═══════════════════════════════════════════════════════════
def build_pip():
    clear_scene()
    GELB = c("#ffd34e"); FLUG = c("#ffe89b"); AUG = c("#3a2a10")
    body = prim("sphere", "pip_body", GELB, (0.32, 0.3, 0.42), (0, 0, 0.7), subsurf=0.35, smooth_levels=1)
    head = prim("sphere", "pip_head", GELB, (0.34, 0.32, 0.34), (0, 0, 1.32), subsurf=0.35, smooth_levels=1)
    # Spitze Ohren
    prim("cone", "pip_ear_l", GELB, (0.11, 0.11, 0.22), (-0.22, 0, 1.62), subsurf=0.2, smooth_levels=1, bevel=0)
    prim("cone", "pip_ear_r", GELB, (0.11, 0.11, 0.22), (0.22, 0, 1.62), subsurf=0.2, smooth_levels=1, bevel=0)
    prim("sphere", "pip_earin_l", FLUG, (0.06, 0.06, 0.09), (-0.22, 0, 1.62), smooth_levels=1, bevel=0)
    prim("sphere", "pip_earin_r", FLUG, (0.06, 0.06, 0.09), (0.22, 0, 1.62), smooth_levels=1, bevel=0)
    # Kulleraugen
    prim("sphere", "pip_eye_l", AUG, (0.12, 0.1, 0.12), (-0.13, 0.27, 1.38), subsurf=0.1, smooth_levels=1, bevel=0)
    prim("sphere", "pip_eye_r", AUG, (0.12, 0.1, 0.12), (0.13, 0.27, 1.38), subsurf=0.1, smooth_levels=1, bevel=0)
    prim("sphere", "pip_glint_l", c("#ffffff"), (0.04, 0.03, 0.04), (-0.1, 0.31, 1.42), smooth_levels=1, bevel=0)
    prim("sphere", "pip_glint_r", c("#ffffff"), (0.04, 0.03, 0.04), (0.16, 0.31, 1.42), smooth_levels=1, bevel=0)
    # Buschiger Schwanz
    prim("sphere", "pip_tail", GELB, (0.28, 0.22, 0.44), (0, -0.38, 0.6), subsurf=0.3, smooth_levels=1)
    prim("sphere", "pip_tail_tip", FLUG, (0.17, 0.13, 0.22), (0, -0.44, 0.95), subsurf=0.3, smooth_levels=1)
    # Flughäute (Patagien)
    prim("sphere", "pip_wing_l", FLUG, (0.22, 0.06, 0.17), (-0.42, 0, 0.85), subsurf=0.2, smooth_levels=1)
    prim("sphere", "pip_wing_r", FLUG, (0.22, 0.06, 0.17), (0.42, 0, 0.85), subsurf=0.2, smooth_levels=1)
    limb("pip_leg_l", GELB, (0.09, 0.09, 0.22), (-0.13, 0, 0.2), subsurf=0.3)
    limb("pip_leg_r", GELB, (0.09, 0.09, 0.22), (0.13, 0, 0.2), subsurf=0.3)
    export("pip")

# ═══════════════════════════════════════════════════════════
# KOKO — Panda (Kugel, große Ohren, Zuckerstangen-Bauch)
# ═══════════════════════════════════════════════════════════
def build_koko():
    clear_scene()
    ROSA = c("#ff4d6d"); WEISS = c("#ffffff"); AUG = c("#2a1a2a")
    # Körper: kugelig, WEISS (Panda)
    body = prim("sphere", "koko_body", WEISS, (0.52, 0.48, 0.57), (0, 0, 0.7), subsurf=0.3, smooth_levels=1)
    # Zuckerstangen-Streifen (rosa, auf dem weißen Bauch)
    for i in range(4):
        prim("box", f"koko_stripe{i}", ROSA, (0.42, 0.06, 0.06), (0, 0.1, 0.48 + i*0.11), rough=0.4, smooth_levels=1, bevel=0.02)
    head = prim("sphere", "koko_head", WEISS, (0.47, 0.44, 0.47), (0, 0, 1.5), subsurf=0.3, smooth_levels=1)
    # Große SCHWARZE Ohren (Panda)
    prim("sphere", "koko_ear_l", AUG, (0.22, 0.22, 0.22), (-0.37, 0, 1.92), subsurf=0.3, smooth_levels=1)
    prim("sphere", "koko_ear_r", AUG, (0.22, 0.22, 0.22), (0.37, 0, 1.92), subsurf=0.3, smooth_levels=1)
    # Schwarze Augenpartie (Panda-Maske)
    prim("sphere", "koko_patch_l", AUG, (0.2, 0.11, 0.2), (-0.16, 0.37, 1.58), subsurf=0.2, smooth_levels=1, bevel=0)
    prim("sphere", "koko_patch_r", AUG, (0.2, 0.11, 0.2), (0.16, 0.37, 1.58), subsurf=0.2, smooth_levels=1, bevel=0)
    prim("sphere", "koko_eye_l", AUG, (0.11, 0.09, 0.11), (-0.16, 0.43, 1.58), subsurf=0.1, smooth_levels=1, bevel=0)
    prim("sphere", "koko_eye_r", AUG, (0.11, 0.09, 0.11), (0.16, 0.43, 1.58), subsurf=0.1, smooth_levels=1, bevel=0)
    prim("sphere", "koko_glint_l", c("#ffffff"), (0.04, 0.03, 0.04), (-0.14, 0.47, 1.62), smooth_levels=1, bevel=0)
    prim("sphere", "koko_glint_r", c("#ffffff"), (0.04, 0.03, 0.04), (0.18, 0.47, 1.62), smooth_levels=1, bevel=0)
    prim("sphere", "koko_nose", AUG, (0.09, 0.07, 0.09), (0, 0.43, 1.42), subsurf=0.1, smooth_levels=1, bevel=0)
    # Arme/Beine: schwarz (Panda-Pfoten)
    limb("koko_arm_l", AUG, (0.13, 0.13, 0.26), (-0.52, 0, 0.72), subsurf=0.3)
    limb("koko_arm_r", AUG, (0.13, 0.13, 0.26), (0.52, 0, 0.72), subsurf=0.3)
    limb("koko_leg_l", AUG, (0.16, 0.16, 0.22), (-0.21, 0, 0.15), subsurf=0.3)
    limb("koko_leg_r", AUG, (0.16, 0.16, 0.22), (0.21, 0, 0.15), subsurf=0.3)
    export("koko")

# ═══════════════════════════════════════════════════════════
# TIKO — Tukan (übergroßer Schnabel, Regenbogen-Brust, Stelzenbeine)
# ═══════════════════════════════════════════════════════════
def build_tiko():
    clear_scene()
    GRUEN = c("#2bffb9"); SCHN = c("#ffb703"); SCHN2 = c("#fb8500"); AUG = c("#1a2a2a")
    body = prim("sphere", "tiko_body", GRUEN, (0.42, 0.37, 0.52), (0, 0, 0.9), subsurf=0.25, smooth_levels=1)
    # Regenbogen-Brust
    for i, col in enumerate([c("#ff4d6d"), c("#ffb703"), c("#ffd34e"), GRUEN, c("#3a86ff")]):
        prim("sphere", f"tiko_rainbow{i}", col, (0.36 - i*0.03, 0.31 - i*0.03, 0.09), (0, 0.1, 0.68 + i*0.11), subsurf=0.2, smooth_levels=1)
    head = prim("sphere", "tiko_head", GRUEN, (0.32, 0.3, 0.32), (0, 0, 1.5), subsurf=0.25, smooth_levels=1)
    # Übergroßer Schnabel
    prim("cone", "tiko_beak", SCHN, (0.22, 0.17, 0.55), (0, 0.37, 1.38), subsurf=0.1, smooth_levels=1, bevel=0)
    prim("cone", "tiko_beak_tip", SCHN2, (0.13, 0.11, 0.22), (0, 0.52, 1.1), subsurf=0.1, smooth_levels=1, bevel=0)
    prim("sphere", "tiko_eye_l", AUG, (0.11, 0.09, 0.11), (-0.22, 0.26, 1.58), subsurf=0.1, smooth_levels=1, bevel=0)
    prim("sphere", "tiko_eye_r", AUG, (0.11, 0.09, 0.11), (0.22, 0.26, 1.58), subsurf=0.1, smooth_levels=1, bevel=0)
    prim("sphere", "tiko_glint_l", c("#ffffff"), (0.04, 0.03, 0.04), (-0.2, 0.3, 1.62), smooth_levels=1, bevel=0)
    prim("sphere", "tiko_glint_r", c("#ffffff"), (0.04, 0.03, 0.04), (0.24, 0.3, 1.62), smooth_levels=1, bevel=0)
    prim("cone", "tiko_crest", c("#ff4d6d"), (0.09, 0.09, 0.22), (0, 0, 1.85), subsurf=0.2, smooth_levels=1, bevel=0)
    # Stelzenbeine
    limb("tiko_leg_l", c("#fb8500"), (0.09, 0.09, 0.52), (-0.16, 0, 0.3), subsurf=0.1, smooth_levels=1)
    limb("tiko_leg_r", c("#fb8500"), (0.09, 0.09, 0.52), (0.16, 0, 0.3), subsurf=0.1, smooth_levels=1)
    prim("sphere", "tiko_wing_l", GRUEN, (0.17, 0.11, 0.32), (-0.42, 0, 0.9), subsurf=0.2, smooth_levels=1)
    prim("sphere", "tiko_wing_r", GRUEN, (0.17, 0.11, 0.32), (0.42, 0, 0.9), subsurf=0.2, smooth_levels=1)
    export("tiko")

# ═══════════════════════════════════════════════════════════
# BOLT — Roboter (kantig, Antenne, Zahnrad-Rücken, Nieten, Rost)
# ═══════════════════════════════════════════════════════════
def build_bolt():
    clear_scene()
    BLAU = c("#3a86ff"); ZAHN = c("#ffb703"); NIET = c("#d4d4d4"); ROST = c("#a4603a"); AUG = c("#eaf4ff")
    # Rumpf: rechteckig, größer, höher (KEIN Subsurf → bleibt eckig)
    body = prim("box", "bolt_body", BLAU, (0.6, 0.5, 0.9), (0, 0, 0.7), rough=0.2, subsurf=0.05, smooth_levels=0, bevel=0.02)
    # Bauchplatte (heller, sichtbar)
    prim("box", "bolt_belly", c("#5a9dff"), (0.4, 0.1, 0.6), (0, 0.3, 0.7), rough=0.2, subsurf=0.05, smooth_levels=0, bevel=0.02)
    # Kopf: rechteckig, sitzt direkt auf dem Rumpf (KEIN Subsurf)
    head = prim("box", "bolt_head", BLAU, (0.5, 0.42, 0.5), (0, 0, 1.4), rough=0.2, subsurf=0.05, smooth_levels=0, bevel=0.02)
    # Antenne mit Kugelspitze
    limb("bolt_antenna", NIET, (0.05, 0.05, 0.35), (0, 0, 1.85), rough=0.2, smooth_levels=1)
    prim("sphere", "bolt_antenna_tip", c("#ff0000"), (0.1, 0.1, 0.1), (0, 0, 2.1), emit=1.0, emit_color=c("#ff0000"), smooth_levels=1, bevel=0)
    # Display-Gesicht: runde Augen
    prim("sphere", "bolt_eye_l", AUG, (0.14, 0.12, 0.14), (-0.15, 0.35, 1.48), emit=0.6, emit_color=AUG, smooth_levels=1, bevel=0)
    prim("sphere", "bolt_eye_r", AUG, (0.14, 0.12, 0.14), (0.15, 0.35, 1.48), emit=0.6, emit_color=AUG, smooth_levels=1, bevel=0)
    prim("box", "bolt_mouth", AUG, (0.18, 0.05, 0.05), (0, 0.35, 1.3), emit=0.3, emit_color=AUG, smooth_levels=0, bevel=0)
    # Zahnrad-Rücken (größer)
    for i, (dx, dy) in enumerate([(-0.25, -0.25), (0.25, -0.25), (0, -0.3)]):
        prim("torus", f"bolt_gear{i}", ZAHN, (0.16, 0.16, 0.07), (dx, dy, 0.9), rough=0.3, metal=0.3)
    # Nieten
    for pos in [(-0.3, 0.25, 0.45), (0.3, 0.25, 0.45), (-0.3, -0.25, 0.45), (0.3, -0.25, 0.45)]:
        prim("sphere", f"bolt_niet_{pos[0]}_{pos[1]}", NIET, (0.07, 0.07, 0.07), pos, rough=0.2, metal=0.3, smooth_levels=1, bevel=0)
    prim("box", "bolt_rust", ROST, (0.6, 0.5, 0.1), (0, 0, 0.4), rough=0.7, smooth_levels=0, bevel=0)
    # Arme/Beine (mechanisch, eckig, KEIN Subsurf)
    limb("bolt_arm_l", BLAU, (0.15, 0.15, 0.42), (-0.5, 0, 0.9), rough=0.2, smooth_levels=0)
    limb("bolt_arm_r", BLAU, (0.15, 0.15, 0.42), (0.5, 0, 0.9), rough=0.2, smooth_levels=0)
    prim("sphere", "bolt_hand_l", NIET, (0.13, 0.13, 0.13), (-0.5, 0, 0.65), rough=0.2, metal=0.3, smooth_levels=1, bevel=0)
    prim("sphere", "bolt_hand_r", NIET, (0.13, 0.13, 0.13), (0.5, 0, 0.65), rough=0.2, metal=0.3, smooth_levels=1, bevel=0)
    limb("bolt_leg_l", BLAU, (0.15, 0.15, 0.35), (-0.2, 0, 0.2), rough=0.2, smooth_levels=0)
    limb("bolt_leg_r", BLAU, (0.15, 0.15, 0.35), (0.2, 0, 0.2), rough=0.2, smooth_levels=0)
    prim("sphere", "bolt_foot_l", NIET, (0.15, 0.2, 0.1), (-0.2, 0.05, 0.05), rough=0.2, metal=0.3, smooth_levels=1, bevel=0)
    prim("sphere", "bolt_foot_r", NIET, (0.15, 0.2, 0.1), (0.2, 0.05, 0.05), rough=0.2, metal=0.3, smooth_levels=1, bevel=0)
    export("bolt")

# ═══════════════════════════════════════════════════════════
# BLOOM — Kaktus (Kugel, Blume, Augen auf Körper)
# ═══════════════════════════════════════════════════════════
def build_bloom():
    clear_scene()
    LILA = c("#7b2ff7"); BLUET = c("#ff4d6d"); MITTE = c("#ffd34e"); STACH = c("#5a1fd0"); AUG = c("#eae0ff")
    body = prim("sphere", "bloom_body", LILA, (0.52, 0.5, 0.57), (0, 0, 0.7), subsurf=0.35, smooth_levels=1)
    prim("sphere", "bloom_eye_l", AUG, (0.14, 0.12, 0.14), (-0.16, 0.42, 0.85), subsurf=0.1, smooth_levels=1, bevel=0)
    prim("sphere", "bloom_eye_r", AUG, (0.14, 0.12, 0.14), (0.16, 0.42, 0.85), subsurf=0.1, smooth_levels=1, bevel=0)
    prim("sphere", "bloom_pupil_l", c("#2a1a2a"), (0.06, 0.05, 0.06), (-0.16, 0.48, 0.85), smooth_levels=1, bevel=0)
    prim("sphere", "bloom_pupil_r", c("#2a1a2a"), (0.06, 0.05, 0.06), (0.16, 0.48, 0.85), smooth_levels=1, bevel=0)
    prim("torus", "bloom_mouth", c("#2a1a2a"), (0.11, 0.11, 0.09), (0, 0.42, 0.68))
    # Blume auf Kopf
    for i in range(8):
        ang = i * math.pi / 4
        prim("sphere", f"bloom_petal{i}", BLUET, (0.13, 0.09, 0.22),
             (math.cos(ang)*0.22, math.sin(ang)*0.22, 1.4), subsurf=0.2, smooth_levels=1)
    prim("sphere", "bloom_flower_c", MITTE, (0.16, 0.16, 0.13), (0, 0, 1.45), subsurf=0.2, smooth_levels=1)
    # Plüsch-Stacheln
    for i, (dx, dy, dz) in enumerate([(-0.42, 0, 0.5), (0.42, 0, 0.5), (-0.37, 0, 1.0), (0.37, 0, 1.0), (0, 0.3, 0.3), (0, -0.3, 0.3)]):
        prim("sphere", f"bloom_spike{i}", STACH, (0.07, 0.07, 0.07), (dx, dy, dz), subsurf=0.3, smooth_levels=1, bevel=0)
    limb("bloom_arm_l", LILA, (0.13, 0.13, 0.27), (-0.52, 0, 0.72), subsurf=0.3)
    limb("bloom_arm_r", LILA, (0.13, 0.13, 0.27), (0.52, 0, 0.72), subsurf=0.3)
    prim("sphere", "bloom_hand_l", LILA, (0.11, 0.11, 0.11), (-0.57, 0, 0.55), subsurf=0.3, smooth_levels=1, bevel=0)
    prim("sphere", "bloom_hand_r", LILA, (0.11, 0.11, 0.11), (0.57, 0, 0.55), subsurf=0.3, smooth_levels=1, bevel=0)
    export("bloom")

# ═══════════════════════════════════════════════════════════
# MOMO — Waschbär (Maske, gestreifter Schwanz, Umhängetasche)
# ═══════════════════════════════════════════════════════════
def build_momo():
    clear_scene()
    GRAU = c("#8a8a8a"); STREIF = c("#2a2a2a"); MASKE = c("#1a1a1a"); AUG = c("#ffe89b"); TASCHE = c("#c96a8a")
    # Körper: schlank, GRAU (Waschbär)
    body = prim("sphere", "momo_body", GRAU, (0.42, 0.37, 0.52), (0, 0, 0.7), subsurf=0.35, smooth_levels=1)
    # Kopf: grau
    head = prim("sphere", "momo_head", GRAU, (0.37, 0.35, 0.37), (0, 0, 1.42), subsurf=0.35, smooth_levels=1)
    # Spitze Ohren (grau, mit heller Innenfläche)
    prim("cone", "momo_ear_l", GRAU, (0.13, 0.13, 0.22), (-0.27, 0, 1.72), subsurf=0.2, smooth_levels=1, bevel=0)
    prim("cone", "momo_ear_r", GRAU, (0.13, 0.13, 0.22), (0.27, 0, 1.72), subsurf=0.2, smooth_levels=1, bevel=0)
    prim("sphere", "momo_earin_l", c("#ffe89b"), (0.06, 0.06, 0.09), (-0.27, 0, 1.72), smooth_levels=1, bevel=0)
    prim("sphere", "momo_earin_r", c("#ffe89b"), (0.06, 0.06, 0.09), (0.27, 0, 1.72), smooth_levels=1, bevel=0)
    # Schwarze Diebes-Maske (Waschbär-Maske)
    prim("sphere", "momo_mask", MASKE, (0.32, 0.13, 0.16), (0, 0.32, 1.48), subsurf=0.2, smooth_levels=1, bevel=0)
    prim("sphere", "momo_eye_l", AUG, (0.09, 0.07, 0.09), (-0.13, 0.38, 1.48), emit=0.4, emit_color=AUG, smooth_levels=1, bevel=0)
    prim("sphere", "momo_eye_r", AUG, (0.09, 0.07, 0.09), (0.13, 0.38, 1.48), emit=0.4, emit_color=AUG, smooth_levels=1, bevel=0)
    prim("sphere", "momo_nose", MASKE, (0.07, 0.06, 0.07), (0, 0.38, 1.3), smooth_levels=1, bevel=0)
    # Weiße Schnauze (Waschbär)
    prim("sphere", "momo_snout", c("#e8e8e8"), (0.12, 0.1, 0.1), (0, 0.35, 1.25), subsurf=0.2, smooth_levels=1, bevel=0)
    # Gestreifter Schwanz (grau/schwarz, 5 Streifen)
    for i in range(5):
        col = STREIF if i % 2 == 0 else GRAU
        prim("sphere", f"momo_tail_{i}", col, (0.13, 0.13, 0.16), (0, -0.37, 0.4 + i*0.13), subsurf=0.3, smooth_levels=1)
    # Umhängetasche
    prim("box", "momo_bag", TASCHE, (0.22, 0.13, 0.22), (0.32, 0, 0.85), rough=0.6, smooth_levels=1, bevel=0.03)
    limb("momo_strap", TASCHE, (0.04, 0.04, 0.42), (0.16, 0, 1.05), rot=(0, 0, 0.5), rough=0.6)
    # Arme/Beine (grau, dunkle Pfoten)
    limb("momo_arm_l", GRAU, (0.11, 0.11, 0.27), (-0.42, 0, 0.72), subsurf=0.3)
    limb("momo_arm_r", GRAU, (0.11, 0.11, 0.27), (0.42, 0, 0.72), subsurf=0.3)
    prim("sphere", "momo_paw_l", STREIF, (0.09, 0.09, 0.09), (-0.45, 0, 0.55), subsurf=0.3, smooth_levels=1, bevel=0)
    prim("sphere", "momo_paw_r", STREIF, (0.09, 0.09, 0.09), (0.45, 0, 0.55), subsurf=0.3, smooth_levels=1, bevel=0)
    limb("momo_leg_l", GRAU, (0.13, 0.13, 0.27), (-0.16, 0, 0.2), subsurf=0.3)
    limb("momo_leg_r", GRAU, (0.13, 0.13, 0.27), (0.16, 0, 0.2), subsurf=0.3)
    prim("sphere", "momo_foot_l", STREIF, (0.12, 0.15, 0.08), (-0.16, 0.05, 0.05), subsurf=0.3, smooth_levels=1, bevel=0)
    prim("sphere", "momo_foot_r", STREIF, (0.12, 0.15, 0.08), (0.16, 0.05, 0.05), subsurf=0.3, smooth_levels=1, bevel=0)
    export("momo")

builders = {
    "brix": build_brix, "nixie": build_nixie, "pip": build_pip, "koko": build_koko,
    "tiko": build_tiko, "bolt": build_bolt, "bloom": build_bloom, "momo": build_momo,
}
for name, fn in builders.items():
    try:
        fn()
    except Exception as e:
        print(f"ERROR building {name}: {e}")
print("DONE: Alle 8 Arenians (V3, Subsurf+Bevel+PBR) generiert")
