Filters the index rows generated for a post when the filter source is unknown or handled by a third-party provider. The `{$source}` portion of the hook name corresponds to the filter source (e.g., `wcField` or a custom source).

## Parameters

- `$rows` (*array*): Array of index rows to be inserted into the database. Default is `[]`.
- `$post_id` (*int*): The ID of the post being indexed.
- `$elements` (*array*): Array of filter elements targeting this post.

## Example usage

```php
add_filter( 'bricks/query_filters/index_post/my_custom_source', function( $rows, $post_id, $elements ) {
    foreach ( $elements as $element ) {
        // Calculate filter value for this post
        $value = get_post_meta( $post_id, 'my_custom_field', true );

        if ( $value ) {
            $rows[] = [
                'filter_id'            => $element['filter_id'],
                'object_id'            => $post_id,
                'object_type'          => 'post',
                'filter_value'         => $value,
                'filter_value_display' => $value, // Optional display value
            ];
        }
    }

    return $rows;
}, 10, 3 );
```
