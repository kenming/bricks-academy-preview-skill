Starting with Bricks 1.3.7 you may manipulate the HTML** **attributes of a given element using the following filter:

```php
add_filter( 'bricks/element/render_attributes', function( $attributes, $key, $element ) {
    if ( isset( $element->settings['my_setting'] )
       && $element->settings['my_setting'] == 'xpto' ) {
        $attributes[ $key ]['data-xpto'] = 'my data';
    }

    return $attributes;
}, 10, 3 );
```

The filter callback receives 3 arguments:

- `$attributes` - an associative array of the element attributes, grouped by the $key identifier
- `$key` - the HTML element identifier to render attributes for
- `$element` - the Bricks element object (since Bricks 1.5)

Since Bricks 1.4, if you need to get access to the `$is_frontend` value (whether the element is rendering in the frontend or in the builder), please use the global function `bricks_is_frontend()`.

Since Bricks 1.5, the `$settings` and `$name` arguments are deprecated. You may use the callback 3rd argument to get those: `$element->settings` and `$element->name`.
