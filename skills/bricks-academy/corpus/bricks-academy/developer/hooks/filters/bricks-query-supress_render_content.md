---
title: "Filter: bricks/query/supress_render_content"
description: "Determines whether to suppress the rendering of the query loop content. This is used by the \"Live Search\" feature to prevent rendering initial results on page."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-supress_render_content/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-supress_render_content.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Determines whether to suppress the rendering of the query loop content. This is used by the "Live Search" feature to prevent rendering initial results on page load if they are going to be immediately replaced by AJAX results.

## Parameters

- `$suppress` (*bool*): Whether to suppress rendering.
- `$query` (*object*): The Bricks Query instance.

## Example usage

```php
add_filter( 'bricks/query/supress_render_content', function( $suppress, $query ) {
    // Example: Suppress content rendering for a specific query ID on mobile devices
    if ( $query->id === 'heavy_query' && wp_is_mobile() ) {
        return true;
    }

    return $suppress;
}, 10, 2 );
```
