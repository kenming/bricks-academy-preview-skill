Allows you to modify the query variables for a specific object type query loop. This is a dynamic filter where `{$object_type}` is replaced by the type of object being queried (e.g., `post`, `term`, `user`).

Common variations:
- `bricks/posts/query_vars`
- `bricks/terms/query_vars`
- `bricks/users/query_vars`

## Parameters

- `$query_vars` (array): The query variables/arguments.
- `$settings` (array): The element settings.
- `$element_id` (string): The element ID.
- `$element_name` (string): The element name (available since Bricks 1.11.1).

## Example usage

```php
add_filter( 'bricks/posts/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    // Only apply to a specific element ID
    if ( $element_id !== 'brxe-abcdef' ) {
        return $query_vars;
    }

    // Modify query variables
    $query_vars['posts_per_page'] = 12;

    return $query_vars;
}, 10, 4 );
```
