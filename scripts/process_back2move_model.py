"""Prepare the Hunyuan Back2Move bottle for the Three.js product viewer.

Run with Blender in background mode:

    blender --background --python scripts/process_back2move_model.py -- \
      --input path/to/hunyuan.fbx \
      --output path/to/back2move.glb \
      --blend-output path/to/back2move.blend
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import bpy
from mathutils import Vector


def parse_args() -> argparse.Namespace:
    argv = sys.argv
    argv = argv[argv.index("--") + 1 :] if "--" in argv else []
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--blend-output", type=Path)
    parser.add_argument("--target-faces", type=int, default=100_000)
    parser.add_argument("--width-scale", type=float, default=1.0)
    parser.add_argument(
        "--cap-start-ratio",
        type=float,
        default=0.886,
        help="Normalized height at which the metal cap begins.",
    )
    return parser.parse_args(argv)


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for collection in (bpy.data.meshes, bpy.data.materials, bpy.data.cameras, bpy.data.lights):
        for item in list(collection):
            if item.users == 0:
                collection.remove(item)


def make_principled_material(
    name: str,
    base_color: tuple[float, float, float, float],
    metallic: float,
    roughness: float,
) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    principled = material.node_tree.nodes.get("Principled BSDF")
    principled.inputs["Base Color"].default_value = base_color
    principled.inputs["Metallic"].default_value = metallic
    principled.inputs["Roughness"].default_value = roughness
    return material


def mesh_world_bounds(obj: bpy.types.Object) -> tuple[Vector, Vector]:
    world_vertices = [obj.matrix_world @ vertex.co for vertex in obj.data.vertices]
    minimum = Vector(
        (
            min(vertex.x for vertex in world_vertices),
            min(vertex.y for vertex in world_vertices),
            min(vertex.z for vertex in world_vertices),
        )
    )
    maximum = Vector(
        (
            max(vertex.x for vertex in world_vertices),
            max(vertex.y for vertex in world_vertices),
            max(vertex.z for vertex in world_vertices),
        )
    )
    return minimum, maximum


def main() -> None:
    args = parse_args()
    input_path = args.input.expanduser().resolve()
    output_path = args.output.expanduser().resolve()
    blend_output = args.blend_output.expanduser().resolve() if args.blend_output else None
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if blend_output:
        blend_output.parent.mkdir(parents=True, exist_ok=True)

    clear_scene()
    bpy.ops.import_scene.fbx(filepath=str(input_path))

    mesh_objects = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
    if not mesh_objects:
        raise RuntimeError("The FBX did not contain a mesh.")

    bottle = max(mesh_objects, key=lambda obj: len(obj.data.polygons))
    for obj in list(bpy.context.scene.objects):
        if obj != bottle:
            bpy.data.objects.remove(obj, do_unlink=True)

    bottle.name = "Back2Move_Bottle"
    bottle.data.name = "Back2Move_Bottle_Geometry"
    bpy.context.view_layer.objects.active = bottle
    bottle.select_set(True)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    bottle.scale.x = args.width_scale
    bottle.scale.y = args.width_scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    minimum, maximum = mesh_world_bounds(bottle)
    dimensions = maximum - minimum

    # Center horizontally and place the base on Z=0.
    bottle.location -= Vector(
        (
            (minimum.x + maximum.x) / 2,
            (minimum.y + maximum.y) / 2,
            minimum.z,
        )
    )
    bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)

    original_faces = len(bottle.data.polygons)
    if original_faces > args.target_faces:
        decimate = bottle.modifiers.new("Web mesh reduction", "DECIMATE")
        decimate.decimate_type = "COLLAPSE"
        decimate.ratio = max(0.01, args.target_faces / original_faces)
        decimate.use_collapse_triangulate = True
        bpy.context.view_layer.objects.active = bottle
        bpy.ops.object.modifier_apply(modifier=decimate.name)

    white = make_principled_material(
        "Back2Move_MatteWhite",
        (0.91, 0.91, 0.89, 1.0),
        metallic=0.0,
        roughness=0.46,
    )
    silver = make_principled_material(
        "Back2Move_BrushedSilver",
        (0.60, 0.62, 0.64, 1.0),
        metallic=0.92,
        roughness=0.26,
    )
    bottle.data.materials.clear()
    bottle.data.materials.append(white)
    bottle.data.materials.append(silver)

    minimum, maximum = mesh_world_bounds(bottle)
    cap_start = minimum.z + (maximum.z - minimum.z) * args.cap_start_ratio
    for polygon in bottle.data.polygons:
        polygon.use_smooth = True
        world_center = bottle.matrix_world @ polygon.center
        polygon.material_index = 1 if world_center.z >= cap_start else 0

    # Weighted normals keep the broad bottle sides smooth after decimation.
    weighted_normal = bottle.modifiers.new("Weighted normals", "WEIGHTED_NORMAL")
    weighted_normal.keep_sharp = True
    weighted_normal.weight = 45

    if blend_output:
        bpy.ops.wm.save_as_mainfile(filepath=str(blend_output))

    bpy.ops.object.select_all(action="DESELECT")
    bottle.select_set(True)
    bpy.context.view_layer.objects.active = bottle
    bpy.ops.export_scene.gltf(
        filepath=str(output_path),
        export_format="GLB",
        use_selection=True,
        export_apply=True,
        export_materials="EXPORT",
        export_normals=True,
        export_draco_mesh_compression_enable=True,
        export_draco_mesh_compression_level=6,
    )

    final_minimum, final_maximum = mesh_world_bounds(bottle)
    print(
        "BACK2MOVE_EXPORT",
        {
            "input": str(input_path),
            "output": str(output_path),
            "faces_before": original_faces,
            "faces_after": len(bottle.data.polygons),
            "vertices_after": len(bottle.data.vertices),
            "bounds_min": tuple(round(value, 6) for value in final_minimum),
            "bounds_max": tuple(round(value, 6) for value in final_maximum),
            "cap_start_z": round(cap_start, 6),
        },
    )


if __name__ == "__main__":
    main()
