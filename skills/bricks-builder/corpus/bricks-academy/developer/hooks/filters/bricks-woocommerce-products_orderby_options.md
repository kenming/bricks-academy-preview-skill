---
title: "Filter: bricks/woocommerce/products_orderby_options"
description: "Filters WooCommerce product order-by options used by Bricks."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-products_orderby_options/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-products_orderby_options.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters WooCommerce product order-by options used by Bricks controls.

## Parameters

- `$options` (array): Order-by option keys and labels.

## Example usage

```php
add_filter( 'bricks/woocommerce/products_orderby_options', function( $options ) {
    $options['title'] = esc_html__( 'Sort by title', 'my-plugin' );

    return $options;
} );
```
