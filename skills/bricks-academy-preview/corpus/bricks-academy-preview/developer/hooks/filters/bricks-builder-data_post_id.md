Filters the post ID used by Bricks to retrieve page data (header, content, footer). This allows you to programmatically change the source of the Bricks data for the current page request.

## Parameters

- `$post_id` (*int*): The current post ID.

## Example usage

```php
add_filter( 'bricks/builder/data_post_id', function( $post_id ) {
    // Example: Use a specific post ID for a custom route
    if ( get_query_var( 'my_custom_route' ) ) {
        return 123; // ID of the post/template to use
    }

    return $post_id;
} );
```
