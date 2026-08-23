---
title: "Filter: bricks_query_max_items_in_builder"
description: "Filters builder query results for custom object types when Bricks applies the builder max-results limit."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks_query_max_items_in_builder/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks_query_max_items_in_builder.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters dynamic query results in the builder when Bricks applies the builder query max-results limit.

Bricks handles built-in `post`, `term`, `user`, and supported provider object types internally. This filter runs for custom query object types that Bricks does not know how to trim itself.

## Parameters

- `$result` (mixed): The current query result.
- `$query_instance` (Bricks\Query): The Bricks query instance.
- `$builder_query_max_results` (int): The maximum number of results Bricks allows in the builder.

## Example usage

```php
add_filter( 'bricks_query_max_items_in_builder', function( $result, $query_instance, $builder_query_max_results ) {
    if ( is_array( $result ) ) {
        return array_slice( $result, 0, $builder_query_max_results );
    }

    return $result;
}, 10, 3 );
```
