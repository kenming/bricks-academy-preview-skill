Filters the list of allowed MIME types for custom font uploads in the Bricks Custom Fonts manager.

## Parameters

- `$mime_types` (*array*): Array of file extensions and their corresponding MIME types (e.g., `['woff2' => 'font/woff2']`).

## Example usage

```php
add_filter( 'bricks/custom_fonts/mime_types', function( $mime_types ) {
    // Add support for OTF fonts
    $mime_types['otf'] = 'font/otf';

    return $mime_types;
} );
```
