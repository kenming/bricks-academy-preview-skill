---
title: "Filter: bricks/query_filters/custom_field_meta_query"
description: "Filters the metaquery generated for a custom field filter in the Query Filters system. This allows you to customize how the filtering logic is applied to the."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-custom_field_meta_query/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-custom_field_meta_query.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the `meta_query` generated for a custom field filter in the Query Filters system. This allows you to customize how the filtering logic is applied to the main query.

## Parameters

- `$meta_query` (*array*): The generated `meta_query` array (e.g., `['key' => '...', 'value' => '...', 'compare' => '...']`).
- `$filter` (*array*): The active filter data, including settings and selected values.
- `$provider` (*string*): The data provider (e.g., `acf`, `metabox`).
- `$query_id` (*string*): The ID of the query loop being filtered.

## Example usage

```php
add_filter( 'bricks/query_filters/custom_field_meta_query', function( $meta_query, $filter, $provider, $query_id ) {
    // Example: Change comparison to 'LIKE' for a specific field
    if ( $filter['settings']['fieldName'] === 'my_text_field' ) {
        $meta_query['compare'] = 'LIKE';
    }

    return $meta_query;
}, 10, 4 );
```
