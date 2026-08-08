import bpy
import math
import sys
from pathlib import Path
from mathutils import Vector


def parse_args():
    if "--" not in sys.argv:
        raise SystemExit(
            "usage: blender --background --python build_creatine_hunyuan.py -- "
            "source.glb front.png back.png output.blend output.glb qa_dir"
        )
    args = sys.argv[sys.argv.index("--") + 1 :]
    if len(args) != 6:
        raise SystemExit("expected source, front label, back label, blend, glb, qa directory")
    return [Path(arg).resolve() for arg in args]


def world_bounds(objects):
    points = [obj.matrix_world @ vertex.co for obj in objects for vertex in obj.data.vertices]
    return (
        Vector((min(p.x for p in points), min(p.y for p in points), min(p.z for p in points))),
        Vector((max(p.x for p in points), max(p.y for p in points), max(p.z for p in points))),
    )


def make_principled(name, color, roughness=0.3):
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    material.diffuse_color = (*color, 1.0)
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (*color, 1.0)
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = 0.0
    bsdf.inputs["IOR"].default_value = 1.46
    return material


def make_label_material(name, image_path):
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    bsdf = nodes.get("Principled BSDF")
    image_node = nodes.new("ShaderNodeTexImage")
    image_node.name = f"{name}_Artwork"
    image_node.label = "Exact supplier artwork on separate wrapper mesh"
    image_node.image = bpy.data.images.load(str(image_path), check_existing=False)
    image_node.image.colorspace_settings.name = "sRGB"
    image_node.interpolation = "Linear"
    links.new(image_node.outputs["Color"], bsdf.inputs["Base Color"])
    links.new(image_node.outputs["Alpha"], bsdf.inputs["Alpha"])
    bsdf.inputs["Roughness"].default_value = 0.52
    bsdf.inputs["Metallic"].default_value = 0.0
    bsdf.inputs["IOR"].default_value = 1.46
    if "Specular IOR Level" in bsdf.inputs:
        bsdf.inputs["Specular IOR Level"].default_value = 0.18
    if "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = 0.02
    material.surface_render_method = "DITHERED"
    return material


def create_grid(name, x_min, x_max, z_min, z_max, y, x_steps, z_steps, front):
    vertices = []
    uv = []
    for zi in range(z_steps + 1):
        v = zi / z_steps
        z = z_min + (z_max - z_min) * v
        for xi in range(x_steps + 1):
            u = xi / x_steps
            x = x_min + (x_max - x_min) * u
            vertices.append((x, y, z))
            uv.append((u if front else 1.0 - u, v))

    faces = []
    for zi in range(z_steps):
        for xi in range(x_steps):
            a = zi * (x_steps + 1) + xi
            b = a + 1
            d = (zi + 1) * (x_steps + 1) + xi
            c = d + 1
            faces.append((a, b, c, d) if front else (a, d, c, b))

    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    uv_layer = mesh.uv_layers.new(name="ArtworkUV")
    for polygon in mesh.polygons:
        for loop_index in polygon.loop_indices:
            vertex_index = mesh.loops[loop_index].vertex_index
            uv_layer.data[loop_index].uv = uv[vertex_index]

    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    return obj


def shrink_to_pouch(obj, target, front):
    modifier = obj.modifiers.new("Conform_To_Hunyuan_Pouch", "SHRINKWRAP")
    modifier.target = target
    modifier.wrap_method = "PROJECT"
    modifier.wrap_mode = "ON_SURFACE"
    modifier.use_project_x = False
    modifier.use_project_y = True
    modifier.use_project_z = False
    modifier.use_positive_direction = front
    modifier.use_negative_direction = not front
    modifier.project_limit = 0.8
    modifier.offset = 0.0015
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.modifier_apply(modifier=modifier.name)
    obj.select_set(False)


def create_gusset(name, front, back, x_steps, z_steps, material):
    vertices = []
    faces = []

    def add_strip(front_indices, back_indices):
        base = len(vertices)
        for fi, bi in zip(front_indices, back_indices):
            vertices.append(tuple(front.data.vertices[fi].co))
            vertices.append(tuple(back.data.vertices[bi].co))
        for i in range(len(front_indices) - 1):
            a = base + i * 2
            faces.append((a, a + 1, a + 3, a + 2))

    left_front = [zi * (x_steps + 1) for zi in range(z_steps + 1)]
    left_back = [zi * (x_steps + 1) for zi in range(z_steps + 1)]
    right_front = [zi * (x_steps + 1) + x_steps for zi in range(z_steps + 1)]
    right_back = [zi * (x_steps + 1) + x_steps for zi in range(z_steps + 1)]
    bottom_front = list(range(x_steps + 1))
    bottom_back = list(range(x_steps + 1))
    top_front = [z_steps * (x_steps + 1) + xi for xi in range(x_steps + 1)]
    top_back = [z_steps * (x_steps + 1) + xi for xi in range(x_steps + 1)]

    add_strip(left_front, left_back)
    add_strip(right_front, right_back)
    add_strip(bottom_front, bottom_back)
    add_strip(top_front, top_back)

    mesh = bpy.data.meshes.new(f"{name}_Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(material)
    return obj


def look_at(obj, point):
    obj.rotation_euler = ((Vector(point) - obj.location).to_track_quat("-Z", "Y")).to_euler()


source_path, front_path, back_path, blend_path, glb_path, qa_dir = parse_args()
blend_path.parent.mkdir(parents=True, exist_ok=True)
glb_path.parent.mkdir(parents=True, exist_ok=True)
qa_dir.mkdir(parents=True, exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(source_path))
base_meshes = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
if not base_meshes:
    raise SystemExit("Hunyuan source contains no mesh")

base = base_meshes[0]
base.name = "Creatine_Black_Pouch_Base"
base.data.name = "Creatine_Black_Pouch_Geometry"

# Keep the Hunyuan-generated physical form but remove every generated marking.
base_material = make_principled("Unprinted_Matte_Black_Pouch", (0.004, 0.005, 0.007), 0.48)
base.data.materials.clear()
base.data.materials.append(base_material)
for polygon in base.data.polygons:
    polygon.use_smooth = True

# 1.5M faces are useful for source generation, but excessive for a browser.
decimate = base.modifiers.new("Web_Optimized_120k_Target", "DECIMATE")
decimate.decimate_type = "COLLAPSE"
decimate.ratio = 0.085
decimate.use_collapse_triangulate = True
bpy.context.view_layer.objects.active = base
base.select_set(True)
bpy.ops.object.modifier_apply(modifier=decimate.name)
base.select_set(False)

bmin, bmax = world_bounds([base])
width = bmax.x - bmin.x
depth = bmax.y - bmin.y
height = bmax.z - bmin.z

# The printed wrapper sits below the zipper and above the lower gusset.
x_min = bmin.x + width * 0.055
x_max = bmax.x - width * 0.055
z_min = bmin.z + height * 0.075
z_max = bmin.z + height * 0.855
x_steps = 64
z_steps = 92

front_wrap = create_grid(
    "Creatine_Packaging_Front", x_min, x_max, z_min, z_max,
    bmin.y - depth * 0.65, x_steps, z_steps, True
)
back_wrap = create_grid(
    "Creatine_Packaging_Back", x_min, x_max, z_min, z_max,
    bmax.y + depth * 0.65, x_steps, z_steps, False
)
front_wrap.data.materials.append(make_label_material("Exact_Creatine_Front_Artwork", front_path))
back_wrap.data.materials.append(make_label_material("Exact_Creatine_Back_Artwork", back_path))
shrink_to_pouch(front_wrap, base, True)
shrink_to_pouch(back_wrap, base, False)

gusset_material = make_principled("Packaging_Black_Gusset", (0.004, 0.005, 0.007), 0.35)
gusset = create_gusset("Creatine_Packaging_Gusset", front_wrap, back_wrap, x_steps, z_steps, gusset_material)

# Join only the packaging sections. The base pouch remains a separate object.
bpy.ops.object.select_all(action="DESELECT")
for obj in (front_wrap, back_wrap, gusset):
    obj.select_set(True)
bpy.context.view_layer.objects.active = front_wrap
bpy.ops.object.join()
wrapper = bpy.context.object
wrapper.name = "Creatine_Packaging_Wrap"
wrapper.data.name = "Creatine_Independent_Label_Wrap_Mesh"
for polygon in wrapper.data.polygons:
    polygon.use_smooth = True

# Neutral studio QA setup.
scene = bpy.context.scene
scene.render.engine = "BLENDER_EEVEE_NEXT"
scene.render.resolution_x = 900
scene.render.resolution_y = 1100
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = "PNG"
scene.render.film_transparent = False
scene.view_settings.look = "AgX - Medium High Contrast"
if scene.world is None:
    scene.world = bpy.data.worlds.new("Studio_World")
scene.world.color = (0.018, 0.019, 0.024)

center = (bmin + bmax) / 2
bpy.ops.object.camera_add()
camera = bpy.context.object
camera.name = "QA_Camera"
camera.data.type = "ORTHO"
camera.data.ortho_scale = height * 1.25
scene.camera = camera


def add_area(name, location, energy, size, color):
    bpy.ops.object.light_add(type="AREA", location=location)
    light = bpy.context.object
    light.name = name
    light.data.energy = energy
    light.data.shape = "DISK"
    light.data.size = size
    light.data.color = color
    look_at(light, center)


add_area("Studio_Key", center + Vector((2.4, -2.8, 2.2)), 320, 2.8, (1.0, 0.99, 0.97))
add_area("Studio_Fill", center + Vector((-2.3, -1.5, 1.0)), 105, 2.6, (0.84, 0.92, 1.0))
add_area("Studio_Rim", center + Vector((1.8, 2.5, 1.5)), 175, 2.0, (0.84, 0.94, 1.0))

qa_views = {
    "qa-creatine-front": Vector((0.0, -2.2, center.z)),
    "qa-creatine-front-right": Vector((1.55, -1.55, center.z)),
    "qa-creatine-back": Vector((0.0, 2.2, center.z)),
}
for name, location in qa_views.items():
    camera.location = location
    look_at(camera, center)
    scene.render.filepath = str(qa_dir / f"{name}.png")
    bpy.ops.render.render(write_still=True)

# Remove QA-only objects before delivery.
for obj in list(scene.objects):
    if obj.type in {"CAMERA", "LIGHT"}:
        bpy.data.objects.remove(obj, do_unlink=True)

bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
bpy.ops.export_scene.gltf(
    filepath=str(glb_path),
    export_format="GLB",
    use_selection=False,
    export_apply=True,
    export_yup=True,
    export_image_format="AUTO",
    export_draco_mesh_compression_enable=True,
    export_draco_mesh_compression_level=8,
    export_draco_position_quantization=14,
    export_draco_normal_quantization=10,
    export_draco_texcoord_quantization=12,
)

triangles = sum(len(poly.vertices) - 2 for obj in (base, wrapper) for poly in obj.data.polygons)
print("DELIVERY", glb_path)
print("BASE_OBJECT", base.name)
print("WRAPPER_OBJECT", wrapper.name)
print("TOTAL_TRIANGLES", triangles)
