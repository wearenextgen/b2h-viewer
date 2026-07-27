import json
import struct
import sys
from pathlib import Path


JSON_CHUNK = 0x4E4F534A
BIN_CHUNK = 0x004E4942


def read_glb(path):
    data = Path(path).read_bytes()
    magic, version, total_length = struct.unpack_from("<III", data, 0)
    if magic != 0x46546C67 or version != 2 or total_length != len(data):
        raise ValueError("Expected a valid glTF 2.0 binary file")
    offset = 12
    chunks = {}
    while offset < total_length:
        chunk_length, chunk_type = struct.unpack_from("<II", data, offset)
        chunks[chunk_type] = data[offset + 8 : offset + 8 + chunk_length]
        offset += 8 + chunk_length
    document = json.loads(chunks[JSON_CHUNK].decode("utf-8").rstrip("\x00 "))
    return document, chunks[BIN_CHUNK]


def padded(data, byte, alignment=4):
    return data + byte * ((-len(data)) % alignment)


def strip_textures(document, binary):
    image_views = {image["bufferView"] for image in document.get("images", []) if "bufferView" in image}
    old_views = document.get("bufferViews", [])
    kept_indices = [index for index in range(len(old_views)) if index not in image_views]
    remap = {old: new for new, old in enumerate(kept_indices)}
    rebuilt = bytearray()
    new_views = []
    for old_index in kept_indices:
        view = dict(old_views[old_index])
        start = view.get("byteOffset", 0)
        payload = binary[start : start + view["byteLength"]]
        while len(rebuilt) % 4:
            rebuilt.append(0)
        view["byteOffset"] = len(rebuilt)
        rebuilt.extend(payload)
        new_views.append(view)
    document["bufferViews"] = new_views
    for accessor in document.get("accessors", []):
        if "bufferView" in accessor:
            accessor["bufferView"] = remap[accessor["bufferView"]]
    for mesh in document.get("meshes", []):
        for primitive in mesh.get("primitives", []):
            primitive["material"] = 0
    document["materials"] = [{
        "name": "B2H Bottle Base",
        "pbrMetallicRoughness": {
            "baseColorFactor": [0.93, 0.92, 0.90, 1.0],
            "metallicFactor": 0.04,
            "roughnessFactor": 0.36,
        },
        "doubleSided": False,
    }]
    for key in ("images", "textures", "samplers", "extensionsUsed", "extensionsRequired"):
        document.pop(key, None)
    document["buffers"] = [{"byteLength": len(rebuilt)}]
    return document, bytes(rebuilt)


def strip_unused_texcoords(document, binary):
    removed_accessors = set()
    for mesh in document.get("meshes", []):
        for primitive in mesh.get("primitives", []):
            texcoord = primitive.get("attributes", {}).pop("TEXCOORD_0", None)
            if texcoord is not None:
                removed_accessors.add(texcoord)
    if not removed_accessors:
        return document, binary

    views = document["bufferViews"]
    accessors = document["accessors"]
    removals_by_view = {}
    for accessor_index in removed_accessors:
        accessor = accessors[accessor_index]
        if accessor.get("componentType") != 5126 or accessor.get("type") != "VEC2":
            continue
        removals_by_view[accessor["bufferView"]] = {
            "offset": accessor.get("byteOffset", 0),
            "size": 8,
            "count": accessor["count"],
        }

    rebuilt = bytearray()
    for view_index, view in enumerate(views):
        start = view.get("byteOffset", 0)
        payload = binary[start : start + view["byteLength"]]
        removal = removals_by_view.get(view_index)
        if removal and "byteStride" in view:
            stride = view["byteStride"]
            offset = removal["offset"]
            size = removal["size"]
            payload = b"".join(
                payload[row * stride : row * stride + offset]
                + payload[row * stride + offset + size : (row + 1) * stride]
                for row in range(removal["count"])
            )
            view["byteStride"] = stride - size
            view["byteLength"] = len(payload)
            for accessor in accessors:
                if accessor.get("bufferView") == view_index and accessor.get("byteOffset", 0) > offset:
                    accessor["byteOffset"] -= size
        while len(rebuilt) % 4:
            rebuilt.append(0)
        view["byteOffset"] = len(rebuilt)
        rebuilt.extend(payload)

    accessor_remap = {}
    compact_accessors = []
    for old_index, accessor in enumerate(accessors):
        if old_index in removed_accessors:
            continue
        accessor_remap[old_index] = len(compact_accessors)
        compact_accessors.append(accessor)
    for mesh in document.get("meshes", []):
        for primitive in mesh.get("primitives", []):
            if "indices" in primitive:
                primitive["indices"] = accessor_remap[primitive["indices"]]
            primitive["attributes"] = {
                name: accessor_remap[index] for name, index in primitive.get("attributes", {}).items()
            }
    document["accessors"] = compact_accessors
    document["buffers"] = [{"byteLength": len(rebuilt)}]
    return document, bytes(rebuilt)


def write_glb(path, document, binary):
    json_bytes = padded(json.dumps(document, separators=(",", ":")).encode("utf-8"), b" ")
    bin_bytes = padded(binary, b"\x00")
    total = 12 + 8 + len(json_bytes) + 8 + len(bin_bytes)
    output = bytearray(struct.pack("<III", 0x46546C67, 2, total))
    output.extend(struct.pack("<II", len(json_bytes), JSON_CHUNK))
    output.extend(json_bytes)
    output.extend(struct.pack("<II", len(bin_bytes), BIN_CHUNK))
    output.extend(bin_bytes)
    Path(path).write_bytes(output)


def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: strip_glb_textures.py input.glb output.glb")
    document, binary = read_glb(sys.argv[1])
    document, binary = strip_textures(document, binary)
    document, binary = strip_unused_texcoords(document, binary)
    write_glb(sys.argv[2], document, binary)


if __name__ == "__main__":
    main()
