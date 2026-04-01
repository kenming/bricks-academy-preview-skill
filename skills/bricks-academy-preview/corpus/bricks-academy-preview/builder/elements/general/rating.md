The **Rating** element displays a numeric score as a row of icons (default: stars). It supports **fractional** values (e.g. `3.5` on a 5-point scale) by filling whole icons, one partial icon with a width mask, and empty icons for the remainder.

This is separate from [Product rating](/builder/elements/product/product-rating/) (WooCommerce). Use **Rating** for static or dynamic review scores anywhere on the site.

## Settings

- **Rating** (number) — Current score. Min `0`, step `0.1`. Supports dynamic data. Default: `3.5`.

- **Max. rating** (number) — Scale maximum (e.g. `5`). Min `1`. Supports dynamic data.

- **Gap** (number with units) — Space between icons (`gap` on the root).

### Icon

- **Icon** (icon) — Optional custom icon; default is the built-in star SVG.

- **Icon color: Full** (color) — Filled / active portion.

- **Icon color: Empty** (color) — Empty / inactive portion.

- **Icon size** (number with units).

### Schema

Optional **schema.org** **Review** + **Rating** JSON-LD.

- **Generate review schema** (checkbox).

When enabled, the following are required:

- **Required: Reviewed item type** (text) — e.g. `Product`, `Service`.

- **Required: Reviewed item name** (text).

Optional:

- **Optional: Review author** (text).

- **Additional item reviewed properties** (repeater) — `Property name`, `Property value`, `Value type` (`Text`, `Number`, `Nested object`).

- **Additional review properties** (repeater) — Same shape; adds fields on the **Review** object (e.g. `reviewBody`, `datePublished`).

The structured data maps your **Rating** and **Max. rating** into a `Rating` node with `bestRating` `5` (normalized from your scale).

:::tip[Developer reference]
See the [Rating Schema](/developer/schema/elements/rating/) for the full JSON schema of this element's settings and controls.
:::
