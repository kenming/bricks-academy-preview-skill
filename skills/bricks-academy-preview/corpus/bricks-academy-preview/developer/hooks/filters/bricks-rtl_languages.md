Filters the list of language codes that Bricks considers right-to-left (RTL). This affects the layout direction of the builder interface when a specific locale is active.

## Parameters

- `$languages` (*array*): Array of RTL language codes (e.g., `['ar', 'he', 'fa']`).

## Example usage

```php
add_filter( 'bricks/rtl_languages', function( $languages ) {
    // Add a custom RTL language code
    $languages[] = 'abc';

    return $languages;
} );
```
