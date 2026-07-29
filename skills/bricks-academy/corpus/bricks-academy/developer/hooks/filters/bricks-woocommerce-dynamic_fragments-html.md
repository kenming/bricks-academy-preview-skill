---
title: "Filter: bricks/woocommerce/dynamic_fragments/html"
description: "Filters rendered HTML for a WooCommerce dynamic fragment."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-dynamic_fragments-html/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-dynamic_fragments-html.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters rendered HTML for a single WooCommerce dynamic fragment.

## Parameters

- `$html` (string): Rendered fragment HTML.
- `$target` (array): The fragment target being rendered.
- `$render_data` (array): Bricks render data used for the fragment.

## Example usage

```php
add_filter( 'bricks/woocommerce/dynamic_fragments/html', function( $html, $target, $render_data ) {
    return $html;
}, 10, 3 );
```
