Filters the query arguments used when searching for pages or posts within the Bricks builder (e.g., in link controls or populate content settings).

## Parameters

- `$query_args` (*array*): Array of arguments passed to `get_posts()`.

## Example usage

```php
add_filter( 'bricks/ajax/get_pages_args', function( $query_args ) {
    // Example: Exclude specific post IDs from the search results
    $query_args['post__not_in'] = [ 12, 34, 56 ];

    return $query_args;
} );
```
