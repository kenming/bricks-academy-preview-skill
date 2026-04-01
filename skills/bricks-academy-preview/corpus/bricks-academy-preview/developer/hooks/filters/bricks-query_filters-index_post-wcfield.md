A specialized hook for indexing WooCommerce product fields (like price, stock status, rating) when a product is saved. This allows the Query Filters index to stay updated with WooCommerce product data.

## Parameters

- `$rows` (*array*): Array of index rows to be inserted.
- `$post_id` (*int*): The ID of the product (post) being indexed.
- `$elements` (*array*): Array of filter elements targeting this product.

## Example usage

```php
add_filter( 'bricks/query_filters/index_post/wcField', function( $rows, $post_id, $elements ) {
    // This filter is typically used internally by Bricks to handle WooCommerce fields.
    // However, you could hook into it to index custom WooCommerce product data.
    
    // Example: Index a custom product property
    $product = wc_get_product( $post_id );
    if ( $product ) {
        // ... generate index rows ...
    }

    return $rows;
}, 10, 3 );
```
