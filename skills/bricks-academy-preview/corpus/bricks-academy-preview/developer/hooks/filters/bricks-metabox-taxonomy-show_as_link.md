Determines whether Meta Box taxonomy fields retrieved via dynamic data should be rendered as links to the term archives.

## Parameters

- `$show_as_link` (*bool*): Whether to render as links. Default is `true`.
- `$value` (*mixed*): The raw value of the taxonomy field.
- `$field` (*array*): The Meta Box field settings array.

## Example usage

```php
add_filter( 'bricks/metabox/taxonomy/show_as_link', function( $show_as_link, $value, $field ) {
    // Disable links for a specific taxonomy field
    if ( $field['id'] === 'my_taxonomy_field' ) {
        return false;
    }

    return $show_as_link;
}, 10, 3 );
```
