Filters the allowed argument keys (modifiers) that can be parsed in dynamic data tags (e.g., `{post_title:my_key}`). This allows you to introduce custom arguments for your dynamic tags.

## Parameters

- `$allowed_keys` (*array*): Array of allowed argument keys. Defaults include `fallback`, `fallback-image`, `sanitize`, `exclude`, `start-at`, `pad`, `key`, `is-array`, `date`, `from`, `to`.

## Example usage

```php
add_filter( 'bricks/dynamic_data/allowed_keys', function( $allowed_keys ) {
    // Add 'limit' as an allowed argument key
    $allowed_keys[] = 'limit';

    return $allowed_keys;
} );
```
