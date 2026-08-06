---
title: "Filter: bricks/query_filters/datepicker_custom_field_meta_query"
description: "Filters the metaquery generated for a datepicker filter targeting a custom field. This allows you to customize how date comparisons are handled (e.g., date."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-datepicker_custom_field_meta_query/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-datepicker_custom_field_meta_query.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the `meta_query` generated for a datepicker filter targeting a custom field. This allows you to customize how date comparisons are handled (e.g., date formats, range logic) for specific fields.

## Parameters

- `$meta_query` (*array*): The generated `meta_query` array (e.g., `['key' => '...', 'value' => '...', 'type' => 'DATE']`).
- `$filter` (*array*): The active filter data, including settings and parsed dates.
- `$provider` (*string*): The data provider (e.g., `acf`, `metabox`).
- `$query_id` (*string*): The ID of the query loop being filtered.

## Example usage

```php
add_filter( 'bricks/query_filters/datepicker_custom_field_meta_query', function( $meta_query, $filter, $provider, $query_id ) {
    // Example: Change type to 'NUMERIC' for timestamp fields stored as numbers
    if ( $filter['settings']['fieldName'] === 'my_timestamp_field' ) {
        if ( isset( $meta_query['type'] ) ) {
            $meta_query['type'] = 'NUMERIC';
        } elseif ( isset( $meta_query[0] ) ) {
            // Handle range query (array of arrays)
            foreach ( $meta_query as $key => $clause ) {
                if ( is_int( $key ) ) {
                    $meta_query[ $key ]['type'] = 'NUMERIC';
                }
            }
        }
    }

    return $meta_query;
}, 10, 4 );
```
