---
title: "Filter: bricks/woocommerce/predefined_elements/remote_url"
description: "Filters the remote URL for WooCommerce predefined element presets."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-predefined_elements-remote_url/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-predefined_elements-remote_url.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the remote URL Bricks uses to fetch WooCommerce predefined element presets. Return an empty string to keep remote fetching disabled.

When a URL is returned, Bricks appends `schemaVersion`, `site`, and `time` query arguments before making the request.

## Parameters

- `$remote_url` (string): The remote preset endpoint URL.

## Example usage

```php
add_filter( 'bricks/woocommerce/predefined_elements/remote_url', function( $remote_url ) {
    return 'https://example.com/bricks-woo-presets.json';
} );
```
