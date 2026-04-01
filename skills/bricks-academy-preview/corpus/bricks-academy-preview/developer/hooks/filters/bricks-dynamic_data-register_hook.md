Filters the WordPress action hook used to register Bricks dynamic data providers and tags.

## Parameters

- `$hook` (*string*): The action hook name. Defaults to `init`.

## Example usage

```php
add_filter( 'bricks/dynamic_data/register_hook', function( $hook ) {
    // Register dynamic data on 'wp_loaded' instead of 'init'
    return 'wp_loaded';
} );
```
