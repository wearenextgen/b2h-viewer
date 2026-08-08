import bmesh
import bpy
import math
import os
import sys


def arg_path(index, default):
    argv = sys.argv
    if "--" in argv:
        args = argv[argv.index("--") + 1:]
        if len(args) > index:
            return os.path.abspath(args[index])
    return os.path.abspath(default)


def lathe_object(name, rings, segments, material, ribs=0, ridge=0.0):
    vertices = []
    faces = []
    for z, radius in rings:
        for i in range(segments):
            theta = math.tau * i / segments
            rib_offset = ridge * (0.5 + 0.5 * math.cos(ribs * theta)) if ribs else 0.0
            r = radius + rib_offset
            vertices.append((r * math.cos(theta), r * math.sin(theta), z))
    for ring in range(len(rings) - 1):
        start = ring * segments
        next_start = (ring + 1) * segments
        for i in range(segments):
            j = (i + 1) % segments
            faces.append((start + i, start + j, next_start + j, next_start + i))
    bottom_center = len(vertices)
    vertices.append((0.0, 0.0, rings[0][0]))
    top_center = len(vertices)
    vertices.append((0.0, 0.0, rings[-1][0]))
    for i in range(segments):
        j = (i + 1) % segments
        faces.append((bottom_center, j, i))
        top = (len(rings) - 1) * segments
        faces.append((top_center, top + i, top + j))

    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(material)
    for polygon in mesh.polygons:
        polygon.use_smooth = True
    return obj


source_path = arg_path(0, "omega3_final.glb")
output_path = arg_path(1, "omega3_final.glb")

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=source_path)
source = next(obj for obj in bpy.context.scene.objects if obj.type == "MESH")
source.name = "Omega3_Exact_Bottle_Body"
bpy.context.view_layer.objects.active = source
source.select_set(True)
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

# The photo-to-3D source is exact through the bottle shoulder, but its neck and
# cap contain scan artefacts. Preserve the label-bearing body, remove only that
# malformed upper section, then reconstruct the same standard ribbed closure
# at the measured source dimensions.
mesh_edit = bmesh.new()
mesh_edit.from_mesh(source.data)
cut = [vertex for vertex in mesh_edit.verts if vertex.co.z > 0.835]
bmesh.ops.delete(mesh_edit, geom=cut, context="VERTS")
mesh_edit.to_mesh(source.data)
mesh_edit.free()
source.data.update()

material = bpy.data.materials.get("Neutral_White_Bottle")
if material is None:
    material = bpy.data.materials.new("Neutral_White_Bottle")
material.diffuse_color = (0.82, 0.81, 0.79, 1.0)
material.use_nodes = True
bsdf = material.node_tree.nodes.get("Principled BSDF")
bsdf.inputs["Base Color"].default_value = (0.82, 0.81, 0.79, 1.0)
bsdf.inputs["Roughness"].default_value = 0.52

lathe_object(
    "Omega3_Clean_Shoulder_And_Neck",
    [
        (0.827, 0.252),
        (0.839, 0.246),
        (0.853, 0.235),
        (0.863, 0.231),
        (0.870, 0.238),
    ],
    160,
    material,
)

lathe_object(
    "Omega3_Ribbed_Cap",
    [
        (0.866, 0.253),
        (0.874, 0.259),
        (0.888, 0.259),
        (1.010, 0.259),
        (1.024, 0.255),
        (1.030, 0.247),
    ],
    192,
    material,
    ribs=48,
    ridge=0.0045,
)

os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
bpy.ops.export_scene.gltf(
    filepath=output_path,
    export_format="GLB",
    export_apply=True,
    export_draco_mesh_compression_enable=True,
    export_draco_mesh_compression_level=6,
    export_draco_position_quantization=14,
    export_draco_normal_quantization=10,
)
