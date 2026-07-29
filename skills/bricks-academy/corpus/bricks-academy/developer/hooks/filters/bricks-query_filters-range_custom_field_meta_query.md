---
title: "Filter: bricks/query_filters/range_custom_field_meta_query"
description: "Filters the metaquery generated for a range filter (slider) targeting a custom field. This allows you to customize how the range comparison is performed (e.g.,."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-range_custom_field_meta_query/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-range_custom_field_meta_query.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the `meta_query` generated for a range filter (slider) targeting a custom field. This allows you to customize how the range comparison is performed (e.g., handling decimal values, changing the data type).

## Parameters

- `$meta_query` (*array*): The generated `meta_query` array (e.g., `['key' => '...', 'value' => [min, max], 'compare' => 'BETWEEN', 'type' => 'NUMERIC']`).
- `$filter` (*array*): The active filter data, including settings and selected min/max values.
- `$provider` (*string*): The data provider (e.g., `acf`, `metabox`).
- `$query_id` (*string*): The ID of the query loop being filtered.

## Example usage

```php
add_filter( 'bricks/query_filters/range_custom_field_meta_query', function( $meta_query, $filter, $provider, $query_id ) {
    // Example: Change type to 'DECIMAL' for precise price filtering
    if ( $filter['settings']['fieldName'] === 'product_price' ) {
        $meta_query['type'] = 'DECIMAL(10,2)';
    }

    return $meta_query;
}, 10, 4 );
```
