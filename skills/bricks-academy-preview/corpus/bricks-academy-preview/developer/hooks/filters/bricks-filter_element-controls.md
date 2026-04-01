Filters the controls available for filter elements (e.g., Checkbox, Radio, Select, Range). This allows you to add, remove, or modify settings for these elements globally.

## Parameters

- `$controls` (*array*): Array of element controls.
- `$element` (*object*): The filter element instance.

## Example usage

```php
add_filter( 'bricks/filter_element/controls', function( $controls, $element ) {
    // Add a custom control to all filter elements
    $controls['my_custom_setting'] = [
        'tab'   => 'content',
        'group' => 'filter',
        'label' => esc_html__( 'My Custom Setting', 'my-plugin' ),
        'type'  => 'checkbox',
    ];

    return $controls;
}, 10, 2 );
```
