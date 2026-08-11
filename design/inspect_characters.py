import json, struct, os

def inspect_glb(path):
    with open(path, 'rb') as f:
        data = f.read()
    if len(data) < 20 or data[:4] != b'glTF':
        return None
    # JSON-Chunk liegt nach dem 12-Byte-Header (magic+version+length) + 12-Byte-Chunk-Header
    json_len, json_type = struct.unpack('<II', data[12:20])
    if json_type != 0x4E4F534A:
        return None
    json_bytes = data[20:20+json_len]
    return json.loads(json_bytes)

for name in ['brix','nixie','pip','koko','tiko','bolt','bloom','momo']:
    path = f'plugins/characters/{name}/{name}.glb'
    if not os.path.exists(path):
        print(f'{name}: DATEI FEHLT'); continue
    gltf = inspect_glb(path)
    if not gltf:
        print(f'{name}: KEIN VALIDES GLB'); continue
    meshes = gltf.get('meshes', [])
    nodes = gltf.get('nodes', [])
    materials = gltf.get('materials', [])
    prim_count = sum(len(m.get('primitives', [])) for m in meshes)
    names = [n.get('name','?') for n in nodes if n.get('name')]
    expected_parts = {
        'brix': ['body','head','hand','arm','leg','eye','moss','fuge'],
        'nixie': ['body','head','gill','eye','drop','mouth','tail','arm'],
        'pip': ['body','head','ear','eye','tail','wing','leg'],
        'koko': ['body','head','ear','eye','patch','nose','stripe','arm','leg'],
        'tiko': ['body','head','beak','eye','rainbow','crest','leg','wing'],
        'bolt': ['body','head','antenna','eye','gear','niet','rust','arm','leg','mouth'],
        'bloom': ['body','eye','mouth','petal','flower','spike','arm'],
        'momo': ['body','head','ear','eye','mask','nose','tail','bag','arm','leg'],
    }
    missing = [p for p in expected_parts.get(name, []) if not any(p in n for n in names)]
    print(f'{name}: prims={prim_count} nodes={len(nodes)} mats={len(materials)}  (Datei {os.path.getsize(path)//1024} KB)')
    print(f'   Namen: {names}')
    print(f'   FEHLENDE Teile: {missing if missing else "KEINE (alle da)"}')
    print()
