Runs after the `Bricks\Frontend::render_data` method has finished generating the HTML for a set of elements. This action is undocumented in the official docs but useful for re-adding plugin actions/filters that were removed in `bricks/frontend/before_render_data` or performing cleanup.

## Parameters

- `$elements` (_array_): The array of elements that were rendered.
- `$area` (_string_): The area being rendered (e.g., 'content', 'header', 'footer').

## Example usage

```php
add_action( 'bricks/frontend/after_render_data', function( $elements, $area ) {
    // Restore actions/filters removed in before_render_data
    // add_filter( 'the_content', 'my_plugin_content_filter' );

    // Example: Log render completion
    // error_log( "Finished rendering area: $area" );
} );
```
