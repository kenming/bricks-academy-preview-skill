Enables a limit on the number of taxonomies queried when fetching terms for builder controls. This is useful for sites with a very large number of taxonomies to prevent memory exhaustion.

## Parameters

- `$enable_limit` (*bool*): Whether to limit the number of queried taxonomies. Default is `false`.

## Example usage

```php
add_filter( 'bricks/get_terms_options/enable_limit', function( $enable_limit ) {
    // Enable the limit to improve performance on sites with many taxonomies
    return true;
} );
```
