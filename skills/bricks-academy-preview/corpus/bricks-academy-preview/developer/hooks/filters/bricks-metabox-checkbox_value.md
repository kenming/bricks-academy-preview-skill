Filters the output value of a Meta Box checkbox field when rendered via Bricks dynamic data. By default, Bricks converts truthy values to "Yes" and falsy values to "No".

## Parameters

- `$value` (*string*): The processed value (e.g., "Yes" or "No").
- `$original_value` (*mixed*): The raw value from the database.
- `$field` (*array*): The Meta Box field settings array.
- `$post` (*WP_Post*): The current post object.

## Example usage

```php
add_filter( 'bricks/metabox/checkbox_value', function( $value, $original_value, $field, $post ) {
    // Example: Return "Active" or "Inactive"
    return $original_value ? 'Active' : 'Inactive';
}, 10, 4 );
```
