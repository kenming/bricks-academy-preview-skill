---
title: "Filter: bricks/query_filters/custom_field_index_rows"
description: "Filters the index rows generated for a custom field in the Query Filters system. This allows providers (like ACF, Meta Box) or custom code to handle how complex."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-custom_field_index_rows/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-custom_field_index_rows.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the index rows generated for a custom field in the Query Filters system. This allows providers (like ACF, Meta Box) or custom code to handle how complex field data is indexed for filtering.

## Parameters

- `$rows` (*array*): Array of index rows. Each row is an associative array representing a filterable value.
- `$object_id` (*int*): The ID of the object (post, term, user) being indexed.
- `$meta_key` (*string*): The meta key of the custom field.
- `$provider` (*string*): The data provider (e.g., `acf`, `metabox`).
- `$object_type` (*string*): The type of object (`post`, `term`, `user`).

## Example usage

```php
add_filter( 'bricks/query_filters/custom_field_index_rows', function( $rows, $object_id, $meta_key, $provider, $object_type ) {
    // Example: Index a custom serialized field
    if ( $meta_key === 'my_serialized_field' ) {
        $value = get_post_meta( $object_id, $meta_key, true );
        // ... parse value ...
        $rows[] = [
            'filter_value' => 'parsed_value',
            'filter_value_display' => 'Display Value',
            // ... other required fields ...
        ];
    }

    return $rows;
}, 10, 5 );
```
