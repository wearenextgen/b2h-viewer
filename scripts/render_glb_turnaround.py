import bpy
import math
import sys
from pathlib import Path
from mathutils import Vector


def args_after_dashes():
    if "--" not in sys.argv:
        raise SystemExit("usage: blender --background --python render_glb_turnaround.py -- model.glb out_dir")
    args = sys.argv[sys.argv.index("--") + 1 :]
    if len(args) != 2:
        raise SystemExit("expected model path and output directory")
    return Path(args[0]).resolve(), Path(args[1]).resolve()


def look_at(obj, point):
    obj.rotation_euler = ((Vector(point) - obj.location).to_track_quat("-Z", "Y")).to_euler()


model_path, output_dir = args_after_dashes()
output_dir.mkdir(parents=True, exist_ok=True)
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(model_path))

meshes = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
if not meshes:
    raise SystemExit("no mesh in model")

all_world = [obj.matrix_world @ v.co for obj in meshes for v in obj.data.vertices]
bmin = Vector((min(v.x for v in all_world), min(v.y for v in all_world), min(v.z for v in all_world)))
bmax = Vector((max(v.x for v in all_world), max(v.y for v in all_world), max(v.z for v in all_world)))
center = (bmin + bmax) / 2
height = bmax.z - bmin.z

for obj in meshes:
    material = bpy.data.materials.new(name="QA_Matte_Black")
    material.diffuse_color = (0.008, 0.009, 0.012, 1)
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (0.006, 0.007, 0.009, 1)
    bsdf.inputs["Roughness"].default_value = 0.30
    bsdf.inputs["Metallic"].default_value = 0.0
    obj.data.materials.clear()
    obj.data.materials.append(material)

scene = bpy.context.scene
scene.render.engine = "BLENDER_EEVEE_NEXT"
scene.render.resolution_x = 640
scene.render.resolution_y = 800
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = "PNG"
scene.render.film_transparent = False
scene.view_settings.look = "AgX - Medium High Contrast"
if scene.world is None:
    scene.world = bpy.data.worlds.new("QA_World")
scene.world.color = (0.025, 0.025, 0.032)

bpy.ops.object.camera_add()
camera = bpy.context.object
camera.data.type = "ORTHO"
camera.data.ortho_scale = height * 1.28
scene.camera = camera

def area(name, location, energy, size, color):
    bpy.ops.object.light_add(type="AREA", location=location)
    light = bpy.context.object
    light.name = name
    light.data.energy = energy
    light.data.shape = "DISK"
    light.data.size = size
    light.data.color = color
    look_at(light, center)


area("Key", center + Vector((2.1, -2.7, 2.1)), 820, 2.5, (1.0, 0.98, 0.95))
area("Fill", center + Vector((-2.2, -1.2, 0.7)), 500, 2.2, (0.78, 0.90, 1.0))
area("Rim", center + Vector((1.4, 2.2, 1.3)), 650, 1.6, (0.80, 0.94, 1.0))

views = {
    "front": (0.0, -2.2, center.z),
    "front-right": (1.55, -1.55, center.z),
    "right": (2.2, 0.0, center.z),
    "back": (0.0, 2.2, center.z),
}

for name, location in views.items():
    camera.location = Vector(location)
    look_at(camera, center)
    scene.render.filepath = str(output_dir / f"{name}.png")
    bpy.ops.render.render(write_still=True)
