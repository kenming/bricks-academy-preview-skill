Filters the query arguments used to retrieve all Bricks templates. This is primarily used by multilingual plugins (like WPML and Polylang) to ensure only templates in the current language are fetched.

## Parameters

- `$args` (*array*): Array of arguments passed to `get_posts()`.

## Example usage

```php
add_filter( 'bricks/database/bricks_get_all_templates_by_type_args', function( $args ) {
    // Example: Include private templates
    $args['post_status'] = [ 'publish', 'private' ];

    return $args;
} );
```
