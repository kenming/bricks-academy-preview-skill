Bricks 1.4 with its improved & slimmer DOM structure now requires to add the element ID, root classes, and other element root HTML attributes directly inside the `render()` function. You can programmatically manipulate the returns element root attributes like so:

```php
add_filter( 'bricks/element/set_root_attributes', function( $attributes, $element ) {
    // Add CSS class 'heading-bg' to every heading element
    if ( $element->name === 'heading' ) {
        $attributes['class'][] = 'heading-bg';
    }

    return $attributes;
}, 10, 2 );
```

The filter callback receives 2 arguments:

- `$attributes` – an associative array of the element root attributes, grouped by the attribute name (e.g. "class", "data-animation", ...)
- `$element` - the Bricks element [object](/developer/elements/create-your-own-elements/)

**NOTE**: This filter doesn't work in builder & already possible with *[bricks/element/render_attributes](/developer/hooks/filters/filter-bricks-element-render_attributes/)*
