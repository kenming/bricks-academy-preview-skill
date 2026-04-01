Filters the query arguments used to fetch posts for the "Preview as" setting and other post selection controls in the builder.

## Parameters

- `$query_args` (*array*): Array of arguments passed to `get_posts()`.

## Example usage

```php
add_filter( 'bricks/helpers/get_posts_args', function( $query_args ) {
    // Example: Exclude 'private' posts from the selection list
    $query_args['post_status'] = 'publish';

    return $query_args;
} );
```
