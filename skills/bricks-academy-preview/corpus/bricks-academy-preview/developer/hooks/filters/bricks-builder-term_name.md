Filters the term name displayed in the Bricks builder interface (e.g., in taxonomy pickers).

## Parameters

- `$term_name` (*string*): The formatted term name (e.g., `Term Name (Taxonomy Label)`).
- `$term_id` (*int|string*): The ID of the term.
- `$taxonomy` (*string*): The slug of the taxonomy.

## Example usage

```php
add_filter( 'bricks/builder/term_name', function( $term_name, $term_id, $taxonomy ) {
    // Example: Add the term ID to the name
    return $term_name . ' [ID: ' . $term_id . ']';
}, 10, 3 );
```
