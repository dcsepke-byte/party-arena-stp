#!/usr/bin/env python3
"""Rendert Previews der 8 Arenians mit Cycles (CPU) für Review."""
import bpy
import os

CHARACTERS = ["brix", "nixie", "pip", "koko", "tiko", "bolt", "bloom", "momo"]
BASE = "/opt/data/SuperTuxParty/plugins/characters"
PREVIEW_DIR = "/opt/data/SuperTuxParty/design/character-previews"
os.makedirs(PREVIEW_DIR, exist_ok=True)

def setup_render():
    scene = bpy.context.scene
    scene.render.engine = 'CYCLES'
    scene.cycles.samples = 24
    scene.render.resolution_x = 512
    scene.render.resolution_y = 512
    # Welt-Hintergrund
    if scene.world is None:
        scene.world = bpy.data.worlds.new('World')
    scene.world.use_nodes = True
    bg = scene.world.node_tree.nodes.get("Background")
    if bg:
        bg.inputs[0].default_value = (0.06, 0.06, 0.09, 1.0)

def render_character(name):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    setup_render()
    # GLB importieren
    glb_path = os.path.join(BASE, name, f"{name}.glb")
    bpy.ops.import_scene.gltf(filepath=glb_path)
    # Objekt zentrieren
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='BOUNDS')
    # Kamera
    cam_data = bpy.data.cameras.new("cam")
    cam_data.lens = 35
    cam = bpy.data.objects.new("cam", cam_data)
    bpy.context.collection.objects.link(cam)
    cam.location = (3.5, -3.5, 2.5)
    cam.rotation_euler = (1.1, 0, 0.785)
    bpy.context.scene.camera = cam
    # Licht
    light_data = bpy.data.lights.new("light", type='SUN')
    light_data.energy = 3.0
    light = bpy.data.objects.new("light", light_data)
    bpy.context.collection.objects.link(light)
    light.rotation_euler = (0.785, 0, 0.5)
    # Render
    out = os.path.join(PREVIEW_DIR, f"{name}.png")
    bpy.context.scene.render.filepath = out
    bpy.ops.render.render(write_still=True)
    print(f"RENDERED: {out}")

for name in CHARACTERS:
    try:
        render_character(name)
    except Exception as e:
        print(f"ERROR rendering {name}: {e}")

print("DONE: Alle Previews gerendert")
