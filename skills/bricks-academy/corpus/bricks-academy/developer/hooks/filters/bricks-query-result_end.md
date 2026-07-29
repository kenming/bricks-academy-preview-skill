---
title: "Filter: bricks/query/result_end"
description: "Filters the ending index used when slicing the query results. This allows you to control which portion of the results is displayed, useful for custom pagination."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-result_end/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-result_end.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the ending index used when slicing the query results. This allows you to control which portion of the results is displayed, useful for custom pagination or limit logic.

## Parameters

- `$end` (*int*): The ending index for the result slice.
- `$query` (*object*): The Bricks Query instance.

## Example usage

```php
add_filter( 'bricks/query/result_end', function( $end, $query ) {
    // Example: Limit results to 5 for a specific query ID
    if ( $query->id === 'my_limited_query' ) {
        return 5;
    }

    return $end;
}, 10, 2 );
```
