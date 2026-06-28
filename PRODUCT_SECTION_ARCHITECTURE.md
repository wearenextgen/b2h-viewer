# B2H Product Section Architecture

## Delivery Model

Every product is delivered as four standalone HTML snippets. Each snippet includes its own scoped HTML, CSS, and JavaScript so it can be copied into the site without depending on another product section. The sections do not need separate visible title blocks; semantic headings may remain visually hidden for accessibility.

## Section 01 - Key Benefits

Purpose: introduce the product visually and make its main benefits easy to explore.

Required content:

- Product name and section heading
- Interactive image gallery
- Three to five selectable product facts
- Full approved overview text
- Four concise benefit cards
- One separate supporting feature image
- No standalone section title

Omega-3 status: complete in `b2h-interactive-gallery.html`.

## Section 02 - Why Choose This Product

Purpose: explain why this specific formula is worth choosing rather than repeating the Section 01 benefits.

Required content:

- One strong product-positioning statement
- Formula rationale
- Primary ingredients and their role
- Product differentiators
- One or two supporting images
- A small interactive comparison, reveal, or ingredient detail
- No standalone section title

## Section 03 - Quality and Formulation

Purpose: establish trust through concrete product and manufacturing information.

Required content:

- Ingredient quality or source
- Purity and testing information
- Formulation or absorption details
- Relevant technical facts
- Certifications or evidence only when supplied
- Packaging or product close-up visual
- No standalone section title

No testing, certification, medical, or sourcing claim should be invented from the imagery.

## Section 04 - How to Use

Purpose: turn the product information into a clear daily routine.

Required content:

- Approved serving amount
- When to take it
- How to prepare or consume it
- Number of servings or duration when supplied
- Warnings and storage instructions when supplied
- Simple interactive routine, step sequence, or dosage control
- Shared 3D bottle viewer with the product-specific label texture
- Four rounded supporting-image cards around the bottle
- No standalone section title

Dosage must come from approved website copy or the final product label.

## Product Folder Layout

```text
products/
  omega-3/
    01-key-benefits.html
    02-why-choose.html
    03-quality-formulation.html
    04-how-to-use.html
    assets/
  back2sleep/
  back2balance/
  back2move/
  d3-k2/
  magnesium/
  back2vitamin/
```

## Content Needed Per Product

Before Sections 02-04 are finalized, provide:

1. Approved product description
2. Why-to-choose copy
3. Ingredient and quality facts
4. Exact usage and dosage instructions
5. Any mandatory warnings or disclaimers
6. Preferred images for each section, if already selected
