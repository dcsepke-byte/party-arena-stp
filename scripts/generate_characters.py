#!/usr/bin/env python3
"""Generate the 8 Arenian character plugins for Milestone 5."""

import json
import os
import struct
import zlib

BASE_DIR = "/opt/data/SuperTuxParty"
CHARACTERS_DIR = os.path.join(BASE_DIR, "plugins", "characters")

CHARACTERS = [
    {
        "id": "brix",
        "name": "Brix",
        "type": "Stein-Golem",
        "home": "Mechanik-Stadt",
        "personality": "mutig, tollpatschig, gutherzig",
        "color_hex": "#ff6a00",
        "color_rgb": (1.0, 0.415686, 0.0),
    },
    {
        "id": "nixie",
        "name": "Nixie",
        "type": "Axolotl",
        "home": "Sonnenstrand",
        "personality": "neugierig, wasseraffin, verspielt",
        "color_hex": "#00f0ff",
        "color_rgb": (0.0, 0.941176, 1.0),
    },
    {
        "id": "pip",
        "name": "Pip",
        "type": "Fliegendes Eichhörnchen",
        "home": "Wolkenwerk",
        "personality": "schnell, frech, immer in Bewegung",
        "color_hex": "#ffd34e",
        "color_rgb": (1.0, 0.827451, 0.305882),
    },
    {
        "id": "koko",
        "name": "Koko",
        "type": "Panda",
        "home": "Zuckerwald",
        "personality": "freundlich, stark, gemütlich",
        "color_hex": "#ff4d6d",
        "color_rgb": (1.0, 0.301961, 0.427451),
    },
    {
        "id": "tiko",
        "name": "Tiko",
        "type": "Vogel (Tukan)",
        "home": "Dschungeltempel",
        "personality": "chaotisch, lustig, Feder-Wirbel",
        "color_hex": "#2bffb9",
        "color_rgb": (0.168627, 1.0, 0.725490),
    },
    {
        "id": "bolt",
        "name": "Bolt",
        "type": "Roboter",
        "home": "Mechanik-Stadt",
        "personality": "logisch, präzise, liebenswert",
        "color_hex": "#3a86ff",
        "color_rgb": (0.227451, 0.525490, 1.0),
    },
    {
        "id": "bloom",
        "name": "Bloom",
        "type": "Kaktus",
        "home": "Dschungeltempel (Oasen-Rand)",
        "personality": "ruhig, humorvoll, Stacheln nur Deko",
        "color_hex": "#7b2ff7",
        "color_rgb": (0.482353, 0.184314, 0.968627),
    },
    {
        "id": "momo",
        "name": "Momo",
        "type": "Waschbär",
        "home": "Frostgipfel",
        "personality": "clever, trickreich, Schabernack",
        "color_hex": "#ff3cac",
        "color_rgb": (1.0, 0.235294, 0.674510),
    },
]


def write_png(filepath: str, r: int, g: int, b: int, size: int = 256) -> None:
    """Write a simple solid-color PNG file."""
    # Build raw image data (RGBA, row by row)
    raw_data = b""
    for y in range(size):
        raw_data += b"\x00"  # filter byte (None)
        for x in range(size):
            # Add a subtle border for visibility
            border = 4
            if x < border or x >= size - border or y < border or y >= size - border:
                # Darker border
                raw_data += bytes([max(0, r - 60), max(0, g - 60), max(0, b - 60), 255])
            else:
                raw_data += bytes([r, g, b, 255])

    def create_chunk(chunk_type: bytes, data: bytes) -> bytes:
        chunk = chunk_type + data
        return struct.pack(">I", len(data)) + chunk + struct.pack(">I", zlib.crc32(chunk) & 0xFFFFFFFF)

    png = b"\x89PNG\r\n\x1a\n"
    png += create_chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0))
    png += create_chunk(b"IDAT", zlib.compress(raw_data))
    png += create_chunk(b"IEND", b"")

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "wb") as f:
        f.write(png)


def write_tscn(filepath: str, char_id: str, rgb: tuple) -> None:
    """Write a minimal Godot 4 character.tscn with placeholder mesh."""
    r, g, b = rgb

    # Unity/Godot compatible color string with 4 decimal precision
    color_str = f"Color({r:.6f}, {g:.6f}, {b:.6f}, 1)"

    content = f"""[gd_scene load_steps=5 format=3]

[ext_resource type="Script" path="res://common/scripts/character.gd" id="1"]

[sub_resource type="StandardMaterial3D" id="2"]
albedo_color = {color_str}

[sub_resource type="BoxMesh" id="3"]
size = Vector3(0.6, 1.2, 0.6)
material = SubResource("2")

[sub_resource type="CapsuleShape3D" id="4"]
radius = 0.6
height = 1.2

[node name="{char_id}" type="Node3D"]
script = ExtResource("1")
animations = NodePath("AnimationTree")
collision_shape = NodePath("Shape3D")

[node name="PlaceholderMesh" type="MeshInstance3D" parent="."]
mesh = SubResource("3")

[node name="Shape3D" type="CollisionShape3D" parent="."]
transform = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0.6, 0)
shape = SubResource("4")

[node name="AnimationTree" type="AnimationTree" parent="."]

[node name="AnimationPlayer" type="AnimationPlayer" parent="."]
"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def write_json(filepath: str, char: dict) -> None:
    """Write character.json metadata file."""
    metadata = {
        "name": char["name"],
        "type": char["type"],
        "home": char["home"],
        "personality": char["personality"],
        "color_hex": char["color_hex"],
    }
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
        f.write("\n")


def main():
    print("=== Generating 8 Arenian Character Plugins ===")

    for char in CHARACTERS:
        char_dir = os.path.join(CHARACTERS_DIR, char["id"])
        print(f"\n  Creating {char['name']} ({char['id']})...")
        print(f"    Color: {char['color_hex']}")
        print(f"    Type: {char['type']}")
        print(f"    Home: {char['home']}")

        # Create character.tscn
        tscn_path = os.path.join(char_dir, "character.tscn")
        write_tscn(tscn_path, char["id"], char["color_rgb"])
        print(f"    ✓ character.tscn")

        # Create character.json
        json_path = os.path.join(char_dir, "character.json")
        write_json(json_path, char)
        print(f"    ✓ character.json")

        # Create icon.png (256x256 colored square)
        icon_path = os.path.join(char_dir, "icon.png")
        r, g, b = char["color_rgb"]
        write_png(icon_path, int(r * 255), int(g * 255), int(b * 255))
        print(f"    ✓ icon.png")

    # Handle Tux-IP removal: rename character.tscn to character.tscn.legacy
    print("\n=== Removing Tux-IP from selection ===")
    legacy_chars = ["Tux", "Godette", "Beastie", "Green Tux"]
    for legacy in legacy_chars:
        legacy_dir = os.path.join(CHARACTERS_DIR, legacy)
        tscn_path = os.path.join(legacy_dir, "character.tscn")
        legacy_path = os.path.join(legacy_dir, "character.tscn.legacy")
        if os.path.exists(tscn_path):
            os.rename(tscn_path, legacy_path)
            print(f"  ✓ {legacy}: character.tscn → character.tscn.legacy")
        else:
            print(f"  ⚠ {legacy}: character.tscn not found (already removed?)")

    print("\n=== DONE ===")
    print(f"Generated {len(CHARACTERS)} character plugins in {CHARACTERS_DIR}")


if __name__ == "__main__":
    main()
