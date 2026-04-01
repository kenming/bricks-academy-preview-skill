Determines whether the ACF Google Map field dynamic data should be rendered as a formatted address or as latitude/longitude coordinates.

## Parameters

- `$show_as_address` (*bool*): Whether to render as an address. Defaults to `true` if ACF version >= 5.6.8.
- `$value` (*array*): The raw value of the ACF Google Map field.
- `$field` (*array*): The ACF field settings.

## Example usage

```php
add_filter( 'bricks/acf/google_map/show_as_address', function( $show_as_address, $value, $field ) {
    // Force showing latitude and longitude instead of address
    return false;
}, 10, 3 );
```
