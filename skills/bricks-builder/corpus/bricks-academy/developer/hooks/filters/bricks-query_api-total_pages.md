---
title: "Filter: bricks/query_api/total_pages"
description: "Filters the total number of pages calculated for an external API query loop. This is useful when the API response structure for pagination doesn't match Bricks'."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_api-total_pages/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_api-total_pages.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the total number of pages calculated for an external API query loop. This is useful when the API response structure for pagination doesn't match Bricks' standard extraction logic.

## Parameters

- `$total_pages` (*int*): The calculated total number of pages.
- `$element_id` (*string*): The ID of the query element.
- `$query_api` (*object*): The `Bricks\Integrations\Query\Query_API` instance.

## Example usage

```php
add_filter( 'bricks/query_api/total_pages', function( $total_pages, $element_id, $query_api ) {
    // Example: Set total pages for a specific API query
    if ( $element_id === 'my_api_loop' ) {
        // Assume you stored the total in a custom property or need a fixed value
        return 10;
    }

    return $total_pages;
}, 10, 3 );
```
