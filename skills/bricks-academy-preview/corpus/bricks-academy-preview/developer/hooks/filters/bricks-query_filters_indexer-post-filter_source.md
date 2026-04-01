Filters the index rows generated for a post by the Query Filters Indexer when processing a specific filter job. The `{$filter_source}` portion of the hook name corresponds to the filter source (e.g., `wcField` or a custom source).

## Parameters

- `$rows` (*array*): Array of index rows to be inserted. Default is `[]`.
- `$post` (*WP_Post|int*): The post object or ID being indexed.
- `$filter_id` (*string*): The ID of the filter element.
- `$filter_settings` (*array*): The settings of the filter element.

## Example usage

```php
add_filter( 'bricks/query_filters_indexer/post/my_custom_source', function( $rows, $post, $filter_id, $filter_settings ) {
    // Generate index rows for custom logic
    $value = get_post_meta( $post->ID, 'my_custom_field', true );

    if ( $value ) {
        $rows[] = [
            'filter_id'            => $filter_id,
            'object_id'            => $post->ID,
            'object_type'          => 'post',
            'filter_value'         => $value,
            'filter_value_display' => $value,
        ];
    }

    return $rows;
}, 10, 4 );
```
