---
title: "Filter: bricks/get_the_title"
description: "Filters the page title returned by Helpers::getthetitle(). This function determines the appropriate title based on the context (single post, archive, search."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_the_title/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_the_title.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the page title returned by `Helpers::get_the_title()`. This function determines the appropriate title based on the context (single post, archive, search results, etc.).

## Parameters

- `$title` (*string*): The generated page title.
- `$post_id` (*int*): The ID of the current post or template.

## Example usage

```php
add_filter( 'bricks/get_the_title', function( $title, $post_id ) {
    // Example: Add a prefix to the title for search results
    if ( is_search() ) {
        return 'Searching: ' . $title;
    }

    return $title;
}, 10, 2 );
```
