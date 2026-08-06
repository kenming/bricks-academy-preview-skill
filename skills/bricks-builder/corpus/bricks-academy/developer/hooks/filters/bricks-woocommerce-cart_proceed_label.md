---
title: "Filter: bricks/woocommerce/cart_proceed_label"
description: "Allows you to modify the text of the \"Proceed to checkout\" button in the WooCommerce Cart element."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-cart_proceed_label/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-cart_proceed_label.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Allows you to modify the text of the "Proceed to checkout" button in the WooCommerce Cart element.

## Parameters

- `$label` (string): The button text. Default is "Proceed to checkout".

## Example usage

```php
add_filter( 'bricks/woocommerce/cart_proceed_label', function( $label ) {
    return 'Go to Checkout';
} );
```
