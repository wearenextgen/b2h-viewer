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

## Whey Protein 2kg

- `whey-vanilla.html` — Vanilla viewer
- `whey-chocolate.html` — Chocolate viewer
- `whey-2kg.glb` — shared corrected-proportion Hunyuan/Blender base mesh
- `whey-vanilla-label.png` / `whey-chocolate-label.png` — separate wrap meshes at runtime

## Creatine Monohydrate 300g

- `creatine.html` — interactive Creatine pouch viewer
- `creatine-300g.glb` — self-contained pouch model with separate front/back artwork meshes
- `creatine-viewer.js` — responsive Three.js controls and lighting
