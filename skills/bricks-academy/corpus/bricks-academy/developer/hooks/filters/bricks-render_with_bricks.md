---
title: "Filter: bricks/render_with_bricks"
description: "Determines whether a specific post or page should be rendered using Bricks. If this filter returns false, Bricks will yield control to the default WordPress."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-render_with_bricks/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-render_with_bricks.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Determines whether a specific post or page should be rendered using Bricks. If this filter returns `false`, Bricks will yield control to the default WordPress template loader or another builder.

## Parameters

- `$render` (*bool|null*): Whether to render with Bricks. Default is `null` (Bricks decides based on settings).
- `$post_id` (*int*): The ID of the post being checked.

## Example usage

```php
add_filter( 'bricks/render_with_bricks', function( $render, $post_id ) {
    // Example: Disable Bricks rendering for posts with a specific meta value
    if ( get_post_meta( $post_id, 'disable_bricks', true ) ) {
        return false;
    }

    return $render;
}, 10, 2 );
```
