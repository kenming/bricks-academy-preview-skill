---
title: "Filter: bricks/woocommerce/predefined_elements/generated_payload"
description: "Filters a generated WooCommerce predefined element payload."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-predefined_elements-generated_payload/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-predefined_elements-generated_payload.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters a generated WooCommerce predefined element payload before Bricks returns it.

## Parameters

- `$response` (array): The generated payload response.
- `$preset` (string): The preset ID being generated.
- `$context` (array): Generation context for the preset.

## Example usage

```php
add_filter( 'bricks/woocommerce/predefined_elements/generated_payload', function( $response, $preset, $context ) {
    return $response;
}, 10, 3 );
```
