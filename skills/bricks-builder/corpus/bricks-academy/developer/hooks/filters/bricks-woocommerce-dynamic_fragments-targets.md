---
title: "Filter: bricks/woocommerce/dynamic_fragments/targets"
description: "Filters WooCommerce dynamic fragment targets before rendering."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-dynamic_fragments-targets/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-dynamic_fragments-targets.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters WooCommerce dynamic fragment targets before Bricks renders the fragments.

## Parameters

- `$targets` (array): Mounted fragment targets from the current page.

## Example usage

```php
add_filter( 'bricks/woocommerce/dynamic_fragments/targets', function( $targets ) {
    return $targets;
} );
```
