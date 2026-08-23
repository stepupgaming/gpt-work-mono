#!/usr/bin/env python3
"""Slice all ten atlases into 1,000 labeled 300×300 PNG files."""
import json
import re
from pathlib import Path

from PIL import Image


root = Path(__file__).resolve().parent
manifest = json.loads((root / "clio_new_styles_manifest.json").read_text(encoding="utf-8"))
destination = root / "sliced"
destination.mkdir(exist_ok=True)

open_images = {}
for item in manifest["styles"]:
    image = open_images.setdefault(item["image"], Image.open(root / item["image"]).convert("RGB"))
    x, y = item["x"], item["y"]
    tile = image.crop((x, y, x + item["width"], y + item["height"]))
    slug = re.sub(r"[^a-z0-9]+", "-", item["name"].lower()).strip("-")
    tile.save(destination / f"{item['id']}_{slug}.png", optimize=True)

print(f"Wrote {len(manifest['styles'])} tiles to {destination}")
