Quadtree Art

Files added:
- `quadtree.py` - quadtree decomposition functions for images.
- `quadtree_art.py` - CLI to generate quadtree-based images using `Pillow`.

Quick start (from `Projects/project_3`):

```powershell
python quadtree_art.py --input apple.jpg --output art.png --min-size 8 --var 800
```

Adjust `--min-size` and `--var` to change the level of detail. Lower `--var` -> more subdivisions.
