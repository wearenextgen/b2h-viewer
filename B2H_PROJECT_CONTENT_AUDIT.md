# B2H Project Content Audit

## Source Reviewed

- `source-material/B2H-υλικο-για-εντυπα-b2c.docx`
- `b2h-interactive-gallery.html`
- Product artwork under `/Users/gtsiranidi/Dropbox/Clients/physical therapy/PRODUCTS`

The Word document contains complete marketing-copy blocks for nine products. Each block includes an introduction, benefits, product rationale, formulation or ingredient information, intended audience, usage guidance, and supporting claims or disclaimers where supplied.

## Products Covered by the New Copy

| Website product | Source copy name | Local artwork | 3D model | Current readiness |
| --- | --- | ---: | ---: | --- |
| Back2Vitamin | B2H Multivitamin Complex | 3 images | No | Copy complete; needs 3 more benefit images |
| Omega-3 | B2H Omega-3 | Extensive image library | 2 GLB files | Benefits design complete; copy requires reconciliation |
| Magnesium | B2H Magnesium Ultra Complex | 3 images | No | Copy complete; needs 3 more benefit images |
| Back2Move | B2H Joint Support | 3 images | No | Copy complete; needs 3 more benefit images |
| Back2Sleep | B2H Sleep | 16 images | No | Copy and images ready |
| Back2Balance | B2H Stress Balance | 7 images | No | Copy and images ready |
| D3 + K2 | B2H Vitamin D3 + K2 | 4 images | No | Copy complete; needs 2 more benefit images |
| Creatine | B2H Creatine | No product folder found | No | Copy complete; artwork missing |
| Whey Protein | B2H Whey Protein | No product folder found | No | Copy complete; artwork missing |

## Correct Reusable Section System

Every product should use the same interaction language as Omega-3 without being a literal visual duplicate.

### Section 01 - Benefits

- Six image cards in two rows
- Click-to-reveal image overlays
- Magnetic drag with snap-back and viewport limits
- Compact selectable fact controls
- Four shaped benefit cards
- One supporting feature image
- No standalone section title above the experience

This is the section already designed for Omega-3.

### Section 02 - Why Choose It

- Product rationale and differentiators from the supplied copy
- Interactive ingredient or formula cards
- Short supporting copy instead of repeating the Section 01 benefit list
- No standalone section title

### Section 03 - Formula, Quality, and Who It Is For

- Ingredient or composition details
- Quality, purity, bioavailability, or production facts only when supplied
- Ideal-user categories
- Clickable shapes/cards using the product palette
- Packaging or ingredient close-up imagery
- No standalone section title

### Section 04 - How to Use

- Exact serving amount when supplied
- Timing and preparation
- Interactive daily-routine or step cards
- Warnings and disclaimer copy
- Shared interactive bottle model with the correct product label
- Four rounded supporting-image cards around the bottle
- No standalone section title

The 3D model belongs here, directly beneath the existing usage information, matching the product-page navigation and keeping the formula section lighter.

## Information Conflicts and Gaps

### Omega-3

The new Word document supports these primary benefits:

- Normal heart function
- Maintenance of normal brain function
- Maintenance of normal vision
- High-quality EPA and DHA
- High-purity Omega-3 fatty acids

The current `b2h-interactive-gallery.html` additionally promotes:

- Joint health and mobility
- Triglyceride support imagery
- Restoring the Ω3/Ω6 nutritional balance

Those additional points do not appear in the new supplied Omega-3 block. The current design can remain, but its visible claims should be reconciled with the approved source before publication. The eye/vision card already matches the new copy and should remain.

### Dosage Precision

Exact instructions currently supplied:

- Multivitamin: 1 tablet daily, preferably with the main meal
- D3 + K2: 3-4 sprays daily
- Sleep: 30-60 minutes before sleep, but the amount still refers to the package
- Whey Protein: 1 scoop with water or milk, but the liquid quantity is not supplied

Omega-3, Magnesium, Joint Support, Stress Balance, and Creatine still refer to the recommended serving shown on the package. Their Section 04 designs must not invent quantities.

### Claims and Compliance

- The supplied copy includes EFSA wording for several products.
- Testing, certification, sourcing, absorption, and purity claims must remain limited to the exact wording provided.
- The Whey Protein block does not include the same full supplement disclaimer shown in several other product blocks; confirm the final legal copy before publishing Section 04.

## Image Production Requirements

All benefits sections require six image cards.

- Ready now: Omega-3, Back2Sleep, Back2Balance
- Needs 2 additional images: D3 + K2
- Needs 3 additional images: Back2Vitamin, Magnesium, Back2Move
- Needs a complete image set: Creatine, Whey Protein

Bottle mockups can support Sections 02 and 03 but should not be counted as six distinct lifestyle/benefit images unless the compositions are genuinely different.

## 3D Model Inventory

Only Omega-3 currently has model files:

- `Ω3/3d model/omega3 lower.glb`
- `Ω3/3d model/omega3 1mil.glb`

No other GLB, GLTF, FBX, OBJ, or USDZ product files were found in the current product library.

The reusable viewer should therefore be built once inside Section 02 with a configurable model URL, label texture, camera position, and fallback poster image. Products without a model should display the poster image until their GLB is delivered.

## Build Decision

Use one shared visual system and one shared JavaScript interaction pattern, but keep each product's content and palette data-driven. This avoids maintaining nine unrelated copies of the same drag, reveal, fact-selector, and 3D-viewer code.
