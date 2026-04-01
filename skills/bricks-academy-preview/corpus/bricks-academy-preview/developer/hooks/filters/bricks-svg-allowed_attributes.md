Filters the list of allowed SVG attributes during sanitization. This is used by the Bricks SVG sanitizer to ensure that uploaded or rendered SVGs do not contain malicious attributes.

## Parameters

- `$attributes` (*array*): Array of allowed SVG attributes.

## Example usage

```php
add_filter( 'bricks/svg/allowed_attributes', function( $attributes ) {
    // Example: Allow 'data-custom' attribute
    $attributes[] = 'data-custom';

    return $attributes;
} );
```
