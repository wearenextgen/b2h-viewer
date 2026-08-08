# B2H product assets and launch homepage

Live homepage preview: <https://wearenextgen.github.io/b2h-viewer/>

The repository now includes the B2H launch homepage: a scroll-controlled product story in which each package starts on its front label, completes one full turn, then rolls out as the next product and native desktop/mobile environment enter. It is a homepage interaction, not a manually controlled 3D viewer.

## Homepage files

- `index.html` — standalone GitHub Pages preview
- `homepage.css` — responsive desktop/mobile layout and visual treatment
- `homepage.js` — scroll choreography, model/label setup, lazy asset loading, product copy and links
- `home-assets/backgrounds/` — separate 16:9 and 9:16 product environments
- `home-assets/floaters/` — real-alpha tablets, large droplets, and powder scoops
- `OPENCART-HOMEPAGE-HANDOFF.md` — developer integration map and QA notes
- `opencart-homepage.twig` — OpenCart homepage template handoff

The individual viewer pages below remain available as model/label QA references.

The homepage uses one restrained studio-light rig across every package, including
the black performance range. On desktop the product stage is intentionally offset
to the right of the copy; the mobile and tablet layouts recenter it automatically.

## Omega-3

- `omega3_final.glb` — exact B2H bottle body with a clean measured ribbed closure
- `label.png` — runtime label wrap retained separately from the bottle geometry
- `scripts/optimize_omega_bottle.py` — source-preserving web optimization
- `scripts/repair_omega_neck.py` — deterministic replacement for the damaged scan neck/cap only

## Whey Protein 2kg

- `whey-vanilla.html` — Vanilla viewer
- `whey-chocolate.html` — Chocolate viewer
- `whey-2kg.glb` — shared corrected-proportion Hunyuan/Blender base mesh
- `whey-vanilla-label.png` / `whey-chocolate-label.png` — separate wrap meshes at runtime

## Creatine Monohydrate 300g

- `creatine.html` — interactive Creatine pouch viewer
- `creatine-300g.glb` — Hunyuan pouch with separate conforming packaging artwork mesh
- `creatine-viewer.js` — responsive Three.js controls and lighting

## Rebuild and QA scripts

- `scripts/build_creatine_hunyuan.py` — imports the exact blank pouch and builds the independent packaging wrap
- `scripts/inspect_glb.py` — geometry/material inventory
- `scripts/render_glb_turnaround.py` — deterministic front/angle/back QA renders
