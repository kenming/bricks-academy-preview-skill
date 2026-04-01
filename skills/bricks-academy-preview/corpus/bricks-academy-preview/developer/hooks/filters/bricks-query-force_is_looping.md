Forces `Bricks\Query::is_looping()` to return `true`. This is useful in AJAX contexts (like popups) where you need to simulate being inside a query loop to correctly render dynamic data that depends on the loop context.

## Parameters

- `$force` (*bool*): Whether to force the is_looping state. Default is `false`.
- `$query_id` (*string*): The ID of the query being checked.
- `$element_id` (*string*): The ID of the element being checked.

## Example usage

```php
add_filter( 'bricks/query/force_is_looping', function( $force, $query_id, $element_id ) {
    // Example: Force looping for a specific element ID
    if ( $element_id === 'my_element_id' ) {
        return true;
    }

    return $force;
}, 10, 3 );
```
