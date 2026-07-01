from html.parser import HTMLParser
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
FILES = sorted((ROOT / "products").glob("*/*.html"))


class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.sections = 0
        self.visible_h2 = 0
        self.photo_cards = 0
        self.model_viewers = 0
        self.bottle_canvases = 0

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            self.ids.append(attributes["id"])
        if tag == "section":
            self.sections += 1
        if tag == "h2" and "sr-only" not in attributes.get("class", "").split():
            self.visible_h2 += 1
        if "photo-card" in attributes.get("class", "").split():
            self.photo_cards += 1
        if tag == "model-viewer":
            self.model_viewers += 1
        if tag == "canvas" and "bottle-canvas" in attributes.get("class", "").split():
            self.bottle_canvases += 1


def audit(path):
    content = path.read_text(encoding="utf-8")
    parser = AuditParser()
    parser.feed(content)
    errors = []
    duplicate_ids = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    if duplicate_ids:
        errors.append(f"duplicate ids: {', '.join(duplicate_ids)}")
    if parser.sections != 1:
        errors.append(f"expected 1 section, found {parser.sections}")
    if parser.visible_h2:
        errors.append("contains a visible section h2")
    if path.name == "01-benefits.html" and parser.photo_cards != 6:
        errors.append(f"expected 6 photo cards, found {parser.photo_cards}")
    if path.name == "02-why-choose.html" and parser.model_viewers:
        errors.append("3D viewer must not be in Section 02")
    if path.name == "04-how-to-use.html" and parser.bottle_canvases != 1:
        errors.append(f"expected 1 bottle canvas, found {parser.bottle_canvases}")
    if "PASTE_" in content:
        errors.append("contains an unresolved PASTE_ token")
    if not re.search(r"@media\(max-width:", content):
        errors.append("missing responsive media query")
    return errors


def main():
    if len(FILES) != 12:
        print(f"Expected 12 section files, found {len(FILES)}")
        return 1
    failed = False
    for path in FILES:
        errors = audit(path)
        relative = path.relative_to(ROOT)
        if errors:
            failed = True
            print(f"FAIL {relative}: {'; '.join(errors)}")
        else:
            print(f"PASS {relative}")
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
