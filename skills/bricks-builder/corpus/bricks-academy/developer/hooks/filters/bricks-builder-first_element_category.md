---
title: "Filter: bricks/builder/first_element_category"
description: "Filters the default expanded element category in the Bricks builder panel. This allows you to prioritize specific element categories based on the post type or."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-builder-first_element_category/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-builder-first_element_category.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the default expanded element category in the Bricks builder panel. This allows you to prioritize specific element categories based on the post type or ID being edited.

## Parameters

- `$category` (*string|bool*): The category name to expand by default (e.g., `layout`, `basic`, `single`). Default is `false`.
- `$post_id` (*int*): The ID of the post being edited.
- `$post_type` (*string*): The post type of the post being edited.

## Example usage

```php
add_filter( 'bricks/builder/first_element_category', function( $category, $post_id, $post_type ) {
    // Example: Expand 'woocommerce' category for product templates
    if ( $post_type === 'product' ) {
        return 'woocommerce';
    }

    return $category;
}, 10, 3 );
```
