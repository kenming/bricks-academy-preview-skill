---
title: "Filter: bricks/woocommerce/predefined_elements/local_presets"
description: "Filters local WooCommerce predefined element presets."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-predefined_elements-local_presets/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-predefined_elements-local_presets.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters local WooCommerce predefined element presets after Bricks loads JSON presets.

## Parameters

- `$presets` (array): Local preset payloads.

## Example usage

```php
add_filter( 'bricks/woocommerce/predefined_elements/local_presets', function( $presets ) {
    return $presets;
} );
```
