---
title: "Filter: bricks/query/result_start"
description: "Filters the starting index used when slicing the query results. This allows you to control where the displayed results begin, useful for custom offsets or."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-result_start/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-result_start.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the starting index used when slicing the query results. This allows you to control where the displayed results begin, useful for custom offsets or pagination.

## Parameters

- `$start` (*int*): The starting index for the result slice.
- `$query` (*object*): The Bricks Query instance.

## Example usage

```php
add_filter( 'bricks/query/result_start', function( $start, $query ) {
    // Example: Offset results by 1 for a specific query ID
    if ( $query->id === 'my_offset_query' ) {
        return $start + 1;
    }

    return $start;
}, 10, 2 );
```
