---
title: "Filter: bricks/fix_filter_element_db"
description: "Allows plugins to intercept and handle the database update process for filter elements on a per-post basis. If the filter returns true, Bricks will skip its."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-fix_filter_element_db/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-fix_filter_element_db.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Allows plugins to intercept and handle the database update process for filter elements on a per-post basis. If the filter returns `true`, Bricks will skip its default update logic for that post.

## Parameters

- `$handled` (*bool*): Whether the update has been handled. Default is `false`.
- `$post_id` (*int*): The ID of the post being processed.
- `$template_type` (*string*): The template type of the post.

## Example usage

```php
add_filter( 'bricks/fix_filter_element_db', function( $handled, $post_id, $template_type ) {
    // Example: Skip processing for a specific post ID
    if ( $post_id === 1234 ) {
        return true;
    }

    return $handled;
}, 10, 3 );
```
