---
title: "Filter: bricks/builder/supported_post_types"
description: "Filters the list of post types that are enabled for editing with Bricks. This checks whether the builder should load for the current post type."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-builder-supported_post_types/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-builder-supported_post_types.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the list of post types that are enabled for editing with Bricks. This checks whether the builder should load for the current post type.

## Parameters

- `$supported_post_types` (*array*): Array of supported post type slugs (e.g., `['page', 'post', 'my_cpt']`).
- `$current_post_type` (*string*): The post type of the post being accessed.

## Example usage

```php
add_filter( 'bricks/builder/supported_post_types', function( $supported_post_types, $current_post_type ) {
    // Example: Always allow 'my_custom_post_type' to be edited with Bricks
    if ( $current_post_type === 'my_custom_post_type' && ! in_array( 'my_custom_post_type', $supported_post_types ) ) {
        $supported_post_types[] = 'my_custom_post_type';
    }

    return $supported_post_types;
}, 10, 2 );
```
