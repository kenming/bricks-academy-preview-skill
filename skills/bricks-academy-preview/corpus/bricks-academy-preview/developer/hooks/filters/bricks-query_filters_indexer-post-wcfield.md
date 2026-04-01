A specialized hook for the Query Filters Indexer to generate index rows for WooCommerce product fields (like price, stock status, rating) when processing a filter job.

## Parameters

- `$rows` (*array*): Array of index rows to be inserted. Default is `[]`.
- `$post` (*WP_Post|int*): The product object or ID being indexed.
- `$filter_id` (*string*): The ID of the filter element.
- `$filter_settings` (*array*): The settings of the filter element.

## Example usage

```php
add_filter( 'bricks/query_filters_indexer/post/wcField', function( $rows, $post, $filter_id, $filter_settings ) {
    // This filter is typically used internally by Bricks to handle WooCommerce fields.
    // However, you could hook into it to index custom WooCommerce product data via the 'wcField' source.
    
    // Check if indexing a specific custom WC field
    if ( isset( $filter_settings['sourceFieldType'] ) && $filter_settings['sourceFieldType'] === 'my_custom_wc_field' ) {
        // ... generate and return rows ...
    }

    return $rows;
}, 10, 4 );
```
