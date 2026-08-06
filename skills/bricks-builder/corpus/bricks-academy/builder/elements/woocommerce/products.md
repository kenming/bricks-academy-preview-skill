---
title: "Products"
description: "Displays WooCommerce products in a grid layout with customizable fields and widgets."
canonical: "https://academy.bricksbuilder.io/builder/elements/woocommerce/products/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/woocommerce/products.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-04T12:13:33.000Z"
---
Displays WooCommerce products in a grid layout with customizable fields and widgets.

## Settings

- **Columns** (number) - Number of columns. Range: 1-6. Default: 4. Supports breakpoints.
- **Gap** (number) - Spacing between products. Default: 30px.

### Query
- Product query controls (via Woocommerce_Helpers::get_product_query_controls).

### Fields
- **Content** (repeater) - Dynamic data fields to display. Default includes WooCommerce hooks and product fields like title, image, price, add to cart.
- **Link entire product** (checkbox) - Make entire product clickable if no field links exist.

### Widgets
- **Show Before Grid** (select) - Widgets to show before products grid. Options: Pagination, Result Count, Order by. Multiple selection.
- **Show After Grid** (select) - Widgets to show after products grid. Options: Pagination, Result Count, Order by. Multiple selection.
- **Sort by options** (select) - Available sorting options. Default: Default sorting. Multiple selection.
