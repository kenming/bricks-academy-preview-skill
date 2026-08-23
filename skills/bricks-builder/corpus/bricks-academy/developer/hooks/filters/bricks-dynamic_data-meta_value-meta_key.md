---
title: "Filter: bricks/dynamic_data/meta_value/{meta_key}"
description: "Filter the value returned for a specific custom-field key when Bricks resolves dynamic data from post meta."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-meta_value-meta_key/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-meta_value-meta_key.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the value of a specific post meta key when retrieved via dynamic data (e.g., `{cf_my_key}`). The `{$meta_key}` portion of the hook name should be replaced with your actual meta key.

## Parameters

- `$value` (*mixed*): The value of the custom field.
- `$post` (*WP_Post*): The post object.

## Example usage

```php
// Filter the value of the custom field with key 'my_price_field'
add_filter( 'bricks/dynamic_data/meta_value/my_price_field', function( $value, $post ) {
    // Example: Format the price
    return '$' . number_format( (float) $value, 2 );
}, 10, 2 );
```
