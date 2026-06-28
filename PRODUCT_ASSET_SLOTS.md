# B2H Asset Replacement Guide

The twelve generated section files are under `products/omega-3`, `products/multivitamin`, and `products/magnesium`.

## Section 01 - Benefits

Open `01-benefits.html` and replace the six entries in:

```js
const IMAGE_URLS = [
  '', '', '', '', '', ''
];
```

Use public HTTPS image URLs. The layout, click overlays, magnetic dragging, snap-back behavior, responsive two-row arrangement, and fact selector are already finished.

Omega-3 already contains its six current public image URLs.

## Section 02 - Why Choose

Open `02-why-choose.html` and replace:

```js
const MODEL_URL = '';
const POSTER_URL = '';
```

- `MODEL_URL`: public HTTPS URL to the final `.glb` file
- `POSTER_URL`: optional product-render image shown while the model loads

The 3D viewer already supports drag rotation, zoom, auto-rotation, shadows, responsive sizing, and a designed fallback state.

## Section 03 - Formula and Quality

Open `03-formula-quality.html` and replace:

```js
const IMAGE_URL = '';
```

Use one horizontal formula, ingredient, packaging, or laboratory-style image.

## Section 04 - How to Use

Open `04-how-to-use.html` and replace:

```js
const PRODUCT_IMAGE_URL = '';
```

Use a transparent or clean product render when possible.

## Required Image Counts Per Product

- Six benefit-card images
- One optional 3D poster image
- One formula/quality image
- One product render for the usage section
- One GLB model

Total recommended visual assets per product: **9 images plus 1 GLB model**.

