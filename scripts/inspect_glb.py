import bpy
import sys
from pathlib import Path


def arg_after_dashes():
    if "--" not in sys.argv:
        raise SystemExit("usage: blender --background --python inspect_glb.py -- model.glb")
    args = sys.argv[sys.argv.index("--") + 1 :]
    if not args:
        raise SystemExit("missing model path")
    return Path(args[0]).resolve()


model_path = arg_after_dashes()
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(model_path))

for obj in bpy.context.scene.objects:
    if obj.type != "MESH":
        continue
    evaluated = obj.evaluated_get(bpy.context.evaluated_depsgraph_get())
    mesh = evaluated.to_mesh()
    triangles = sum(len(poly.vertices) - 2 for poly in mesh.polygons)
    material_names = [slot.material.name if slot.material else "<none>" for slot in obj.material_slots]
    print(
        "MESH",
        obj.name,
        "vertices=", len(mesh.vertices),
        "polygons=", len(mesh.polygons),
        "triangles=", triangles,
        "dimensions=", tuple(round(v, 6) for v in obj.dimensions),
        "location=", tuple(round(v, 6) for v in obj.location),
        "rotation=", tuple(round(v, 6) for v in obj.rotation_euler),
        "world_bounds=", (
            tuple(round(min((obj.matrix_world @ v.co)[axis] for v in mesh.vertices), 6) for axis in range(3)),
            tuple(round(max((obj.matrix_world @ v.co)[axis] for v in mesh.vertices), 6) for axis in range(3)),
        ),
        "materials=", material_names,
    )
    evaluated.to_mesh_clear()

for image in bpy.data.images:
    print("IMAGE", image.name, "size=", tuple(image.size), "packed=", bool(image.packed_file))
