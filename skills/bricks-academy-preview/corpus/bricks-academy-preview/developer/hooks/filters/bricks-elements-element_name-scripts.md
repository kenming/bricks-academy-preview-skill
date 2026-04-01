Filters the list of script handles to be loaded for a specific element. The `{$element_name}` portion of the hook name should be replaced with the element's name (e.g., `slider`, `accordion`, `my_custom_element`).

## Parameters

- `$scripts` (*array*): Array of script handles registered via `wp_register_script`.

## Example usage

```php
// Filter scripts for the 'slider' element
add_filter( 'bricks/elements/slider/scripts', function( $scripts ) {
    // Add a custom script dependency
    $scripts[] = 'my-custom-slider-script';

    return $scripts;
} );
```
