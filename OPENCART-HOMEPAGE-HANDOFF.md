# B2H OpenCart homepage handoff

## Intended behavior

This is a normal homepage hero sequence, not a product viewer. The visitor has no drag, zoom, orbit, or playback controls. Scrolling alone drives the choreography:

1. A product enters front-facing and stops in the visual center.
2. The next section of scroll turns it through one complete 360-degree rotation.
3. After the full turn, the package continues rotating and rolls out to the left.
4. The next product, its background, and its foreground elements roll in from the right.
5. Desktop uses native 16:9 art; mobile uses independently composed 9:16 art.

There is no 3D loader, loading copy, progress UI, or viewer language in the page.

## OpenCart installation

Place this repository's runtime files under a public folder such as:

```text
catalog/view/javascript/b2h-home/
├── homepage.css
├── homepage.js
├── home-assets/
├── *.glb
└── *-label.png / label.png
```

Use `opencart-homepage.twig` as the starting template. In a standard OpenCart installation this is normally adapted into `catalog/view/template/common/home.twig`; commercial themes may override that path. Keep the active theme's existing header/footer variables and replace only its homepage content area.

`homepage.js` resolves all models, labels, backgrounds, and foreground effects relative to its own URL, so the directory can move without rewriting every asset path. The two HTML logo paths in the Twig file use `catalog/view/javascript/b2h-home/` explicitly.

## Developer edits required

- Replace the placeholder `https://b2h.gr/` values in the `products` array with the final OpenCart product routes.
- Decide whether the theme's global header should overlay the hero or be replaced by the compact hero top bar on the homepage only.
- Keep the first CTA as `ΓΝΩΡΙΣΤΕ ΤΗ ΝΕΑ ΣΕΙΡΑ`; use `ΔΕΙΤΕ ΤΟ ΠΡΟΪΟΝ` for product-level slides.
- Keep `Add to Cart` on the product page or a later product grid, not inside every rotating hero slide.
- Preserve the front-angle values in the `products` array. They were visually checked per package type.

## Asset logic

- Product geometry remains live so scroll can turn it accurately.
- There are no pointer handlers on the canvas; the product cannot be manipulated.
- Backgrounds and product models are loaded only when the current/next slide needs them.
- Black packages use a stronger product-specific halo and a soft grounding shadow.
- Pills, droplets, and powder scoops are separate true-alpha assets with their own parallax motion.
- The bottle-ribbon overlay was intentionally removed. Only the generated product environments remain behind the product.

## Launch messaging

The launch system uses one persistent announcement—`Η ΝΕΑ ΣΕΙΡΑ ΕΙΝΑΙ ΕΔΩ`—and one action at a time. The first action introduces the range; subsequent actions lead to the relevant product. This is deliberate: the hero encourages discovery, while commercial actions belong deeper in the journey.

## QA checklist

- Desktop: verify at 1440×900 and 1920×1080.
- Mobile: verify at 390×844 and 430×932.
- Every product must begin on its front artwork before rotation.
- Confirm one full rotation completes before the roll-out portion starts.
- Confirm no product overlaps the mobile headline or CTA.
- Confirm dark packages retain visible edge separation from the background.
- Confirm all final OpenCart product links before launch.
- Test on a real iPhone/Safari and Android/Chrome device, not only responsive emulation.

## Performance notes

The page caps pixel density, loads the first two models immediately, and preloads the next product while the visitor scrolls. For production, serve GLB, PNG, JavaScript, and CSS files with long-lived cache headers and Brotli/Gzip where applicable. Keep the CDN import map or bundle Three.js into the theme's asset pipeline.
