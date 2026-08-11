#!/usr/bin/env python3
"""Regeneriert nur Brix und Bolt (eckiger, größer, mit Bauch)."""
import sys
sys.path.insert(0, "/opt/data/SuperTuxParty/design")
# Importiere die build-Funktionen aus dem Hauptskript
import importlib.util
spec = importlib.util.spec_from_file_location("gen", "/opt/data/SuperTuxParty/design/generate_characters.py")
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)

gen.build_brix()
gen.build_bolt()
print("DONE: Brix + Bolt regeneriert")
