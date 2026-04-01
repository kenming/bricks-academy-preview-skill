Filters the cache key used to store and retrieve the list of all Bricks templates. This allows plugins to create unique cache entries based on context (e.g., current language).

## Parameters

- `$cache_key` (*string*): The default cache key (e.g., `all_templates_{timestamp}`).

## Example usage

```php
add_filter( 'bricks/database/get_all_templates_cache_key', function( $cache_key ) {
    // Example: Append current language code to cache key
    if ( defined( 'ICL_LANGUAGE_CODE' ) ) {
        $cache_key .= '_' . ICL_LANGUAGE_CODE;
    }

    return $cache_key;
} );
```
