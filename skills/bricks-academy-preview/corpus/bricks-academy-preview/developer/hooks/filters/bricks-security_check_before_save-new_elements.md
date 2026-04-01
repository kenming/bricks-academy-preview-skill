Filters the array of new elements before they are saved to the database, specifically during the security check process (e.g., when validating `{echo:}` tags). This allows you to inspect or modify the element data before it persists.

## Parameters

- `$new_elements` (*array*): Array of new element data structures.
- `$old_elements_indexed` (*array*): Array of existing elements, indexed by their ID, for comparison.

## Example usage

```php
add_filter( 'bricks/security_check_before_save/new_elements', function( $new_elements, $old_elements_indexed ) {
    // Example: Loop through new elements and log changes
    foreach ( $new_elements as $element ) {
        // Custom logic here
    }

    return $new_elements;
}, 10, 2 );
```
