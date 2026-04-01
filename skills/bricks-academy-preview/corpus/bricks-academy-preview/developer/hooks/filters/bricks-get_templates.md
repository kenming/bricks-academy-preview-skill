Filters the list of templates returned by the `Templates::get_templates()` method. This allows you to modify the templates array before it is returned to the builder or other parts of the application.

## Parameters

- `$templates` (*array*): Array of template data.
- `$custom_args` (*array*): The arguments used to query the templates.

## Example usage

```php
add_filter( 'bricks/get_templates', function( $templates, $custom_args ) {
    // Example: Add a custom property to all templates
    foreach ( $templates as $key => $template ) {
        $templates[ $key ]['my_custom_property'] = 'value';
    }

    return $templates;
}, 10, 2 );
```
