# New style preview atlas

Ten labeled 10×10 PNG sheets containing 1,000 new style concepts. The 397 names in the referenced Clio library were excluded by normalized exact-name comparison.

## Deterministic slicing

- Sheet size: **3000×3000 px**
- Grid: **10 columns × 10 rows**
- Cell size: **300×300 px**
- Origin: top-left
- Ordering: row-major
- Cell rectangle: `x = column * 300`, `y = row * 300`, `width = 300`, `height = 300`

The JSON and CSV manifests provide the exact image filename, sheet, index, row, column, pixel rectangle, stable ID, and style name for every card.

Run `python slice_atlas.py` beside the sheets to write all 1,000 labeled cards into `sliced/` automatically.
