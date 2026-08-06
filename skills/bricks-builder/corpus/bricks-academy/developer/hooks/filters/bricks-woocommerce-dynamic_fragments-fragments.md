---
title: "Filter: bricks/woocommerce/dynamic_fragments/fragments"
description: "Filters WooCommerce dynamic fragments before the AJAX response is sent."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-dynamic_fragments-fragments/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-dynamic_fragments-fragments.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters WooCommerce dynamic fragments before Bricks returns the AJAX response.

## Parameters

- `$fragments` (array): Selector-keyed fragment HTML.
- `$targets` (array): Mounted fragment targets from the current page.

## Example usage

```php
add_filter( 'bricks/woocommerce/dynamic_fragments/fragments', function( $fragments, $targets ) {
    return $fragments;
}, 10, 2 );
```
