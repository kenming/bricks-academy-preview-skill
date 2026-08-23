---
title: "Filter: bricks/woocommerce/predefined_elements/remote_payload"
description: "Filters the remote WooCommerce predefined elements payload."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-predefined_elements-remote_payload/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-predefined_elements-remote_payload.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the remote WooCommerce predefined elements payload after Bricks decodes the response and before it validates/caches the payload.

## Parameters

- `$remote_payload` (array|mixed): Decoded remote payload data.

## Example usage

```php
add_filter( 'bricks/woocommerce/predefined_elements/remote_payload', function( $remote_payload ) {
    return $remote_payload;
} );
```
