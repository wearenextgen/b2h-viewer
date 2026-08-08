import bpy
import sys
from pathlib import Path
from mathutils import Vector


if "--" not in sys.argv:
    raise SystemExit("usage: blender --background --python optimize_omega_bottle.py -- source.glb output.glb")
args = sys.argv[sys.argv.index("--") + 1 :]
if len(args) != 2:
    raise SystemExit("expected source and output paths")
source_path, output_path = (Path(value).resolve() for value in args)
output_path.parent.mkdir(parents=True, exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(source_path))
meshes = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
if len(meshes) != 1:
    raise SystemExit(f"expected one mesh, found {len(meshes)}")
body = meshes[0]
body.name = "Omega3_Bottle_Body"

world_vertices = [body.matrix_world @ vertex.co for vertex in body.data.vertices]
z_min = min(vertex.z for vertex in world_vertices)
z_max = max(vertex.z for vertex in world_vertices)
cap_threshold = z_min + (z_max - z_min) * 0.72

# Preserve much more geometry on the detailed cap and neck than on the smooth body.
bpy.context.view_layer.objects.active = body
body.select_set(True)
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action="DESELECT")
bpy.ops.object.mode_set(mode="OBJECT")
for polygon in body.data.polygons:
    center_world = body.matrix_world @ polygon.center
    polygon.select = center_world.z >= cap_threshold
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.separate(type="SELECTED")
bpy.ops.object.mode_set(mode="OBJECT")

parts = [obj for obj in bpy.context.selected_objects if obj.type == "MESH"]
if len(parts) != 2:
    raise SystemExit(f"cap separation produced {len(parts)} mesh parts")
parts.sort(key=lambda obj: max((obj.matrix_world @ vertex.co).z for vertex in obj.data.vertices))
lower, cap = parts
lower.name = "Omega3_Bottle_Lower"
cap.name = "Omega3_Bottle_Cap_And_Neck"

for obj, ratio, name in (
    (lower, 0.13, "Body_Web_Optimization"),
    (cap, 0.70, "Cap_Detail_Preservation"),
):
    modifier = obj.modifiers.new(name, "DECIMATE")
    modifier.decimate_type = "COLLAPSE"
    modifier.ratio = ratio
    modifier.use_collapse_triangulate = True
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_apply(modifier=modifier.name)
    for polygon in obj.data.polygons:
        polygon.use_smooth = True

material = bpy.data.materials.new("Neutral_White_Bottle")
material.use_nodes = True
bsdf = material.node_tree.nodes.get("Principled BSDF")
bsdf.inputs["Base Color"].default_value = (0.89, 0.88, 0.86, 1)
bsdf.inputs["Roughness"].default_value = 0.46
for obj in (lower, cap):
    obj.data.materials.clear()
    obj.data.materials.append(material)

bpy.ops.object.select_all(action="DESELECT")
lower.select_set(True)
cap.select_set(True)
bpy.context.view_layer.objects.active = lower
bpy.ops.object.join()
model = bpy.context.object
model.name = "Omega3_Exact_Bottle"
model.data.name = "Omega3_Exact_Bottle_Geometry"

bpy.ops.export_scene.gltf(
    filepath=str(output_path),
    export_format="GLB",
    export_apply=True,
    export_yup=True,
    export_draco_mesh_compression_enable=True,
    export_draco_mesh_compression_level=8,
    export_draco_position_quantization=14,
    export_draco_normal_quantization=10,
)

triangles = sum(len(poly.vertices) - 2 for poly in model.data.polygons)
print("DELIVERY", output_path)
print("TRIANGLES", triangles)
