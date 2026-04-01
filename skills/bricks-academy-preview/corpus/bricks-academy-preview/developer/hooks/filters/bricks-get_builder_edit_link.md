Filters the "Edit with Bricks" URL generated for a post. This allows you to append custom query parameters or modify the link structure.

## Parameters

- `$url` (*string*): The "Edit with Bricks" URL.
- `$post_id` (*int*): The ID of the post.

## Example usage

```php
add_filter( 'bricks/get_builder_edit_link', function( $url, $post_id ) {
    // Example: Append a custom parameter to the builder URL
    return add_query_arg( 'my_param', 'value', $url );
}, 10, 2 );
```
