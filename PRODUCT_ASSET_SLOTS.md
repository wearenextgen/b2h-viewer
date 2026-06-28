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

No image or model replacement is required. This section uses the interactive formula graphic and approved ingredient information.

## Section 03 - Formula and Quality

Open `03-formula-quality.html` and replace:

```js
const IMAGE_URL = '';
```

Use one horizontal formula, ingredient, packaging, or laboratory-style image.

## Section 04 - How to Use + 3D Bottle

Open `04-how-to-use.html` and replace:

```js
const USAGE_IMAGE_URLS = [
  '', '', '', ''
];
```

Replace the four empty strings with public HTTPS image URLs. The shared 3D bottle and product-specific label URLs are already configured.

The 3D viewer supports drag rotation, zoom, auto-rotation, responsive sizing, progressive loading, and a designed error state.

## Required Image Counts Per Product

- Six benefit-card images
- One formula/quality image
- Four rounded images around the usage-section 3D bottle
- One shared optimized GLB bottle model
- One horizontal PNG label texture per product

Total recommended visual assets per product: **11 images plus 1 label PNG**. The GLB bottle is shared by all products.
