---
title: "Filter: bricks/query/run_fake"
description: "Defines the results of a \"fake\" query execution for custom or unsupported query types. This is used when calculating filter counts or other logic that requires."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-run_fake/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-run_fake.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Defines the results of a "fake" query execution for custom or unsupported query types. This is used when calculating filter counts or other logic that requires querying all potential results without pagination.

## Parameters

- `$results` (*array*): The query results array (default `[]`).
- `$query` (*object*): The Bricks Query instance.

## Example usage

```php
add_filter( 'bricks/query/run_fake', function( $results, $query ) {
    // Example: Provide all results for a custom 'my_api' query type
    if ( $query->object_type === 'my_api' ) {
        // Fetch all IDs from your API
        return [ 1, 2, 3, 4, 5 ]; 
    }

    return $results;
}, 10, 2 );
```
