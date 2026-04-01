Filters the list of authors displayed in the Bricks template manager. This allows you to customize which authors are selectable when filtering templates.

## Parameters

- `$authors` (*array*): Array of author display names.

## Example usage

```php
add_filter( 'bricks/get_template_authors', function( $authors ) {
    // Example: Remove 'admin' from the authors list
    if ( ( $key = array_search( 'admin', $authors ) ) !== false ) {
        unset( $authors[ $key ] );
    }

    return $authors;
} );
```
