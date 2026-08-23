---
title: "Filter: bricks/ajax/get_pages_args"
description: "Filters the query arguments used when searching for pages or posts within the Bricks builder (e.g., in link controls or populate content settings)."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-ajax-get_pages_args/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-ajax-get_pages_args.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the query arguments used when searching for pages or posts within the Bricks builder (e.g., in link controls or populate content settings).

## Parameters

- `$query_args` (*array*): Array of arguments passed to `get_posts()`.

## Example usage

```php
add_filter( 'bricks/ajax/get_pages_args', function( $query_args ) {
    // Example: Exclude specific post IDs from the search results
    $query_args['post__not_in'] = [ 12, 34, 56 ];

    return $query_args;
} );
```
