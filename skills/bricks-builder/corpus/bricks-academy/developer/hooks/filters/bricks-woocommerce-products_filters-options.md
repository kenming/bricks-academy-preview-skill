---
title: "Filter: bricks/woocommerce/products_filters/options"
description: "Allows you to modify the options available in the WooCommerce Products Filter element."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-products_filters-options/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-products_filters-options.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Allows you to modify the options available in the WooCommerce Products Filter element.

## Parameters

- `$options` (array): An array of options, where each option is an associative array with `id` and `name`.
- `$settings` (array): The element settings.

## Example usage

```php
add_filter( 'bricks/woocommerce/products_filters/options', function( $options, $settings ) {
    // Add a custom "All" option to the beginning
    array_unshift( $options, [
        'id'   => 'all',
        'name' => 'All Products',
    ] );

    return $options;
}, 10, 2 );
```
