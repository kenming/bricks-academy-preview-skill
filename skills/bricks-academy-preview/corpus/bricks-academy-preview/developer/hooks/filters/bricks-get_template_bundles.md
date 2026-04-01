Filters the list of template bundles displayed in the Bricks template manager. Template bundles are a custom taxonomy used to categorize templates.

## Parameters

- `$bundles` (*array*): Associative array of template bundles, where the key is the term slug and the value is the term name.

## Example usage

```php
add_filter( 'bricks/get_template_bundles', function( $bundles ) {
    // Example: Rename a specific bundle
    if ( isset( $bundles['my-bundle'] ) ) {
        $bundles['my-bundle'] = 'My Renamed Bundle';
    }

    return $bundles;
} );
```
