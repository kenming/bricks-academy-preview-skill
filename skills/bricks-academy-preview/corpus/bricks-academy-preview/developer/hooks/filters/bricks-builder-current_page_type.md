Filters the detected current page type stored in `Database::$page_data['current_page_type']`. This value is used by Bricks to determine the context for dynamic data and other logic.

## Parameters

- `$page_type` (*string*): The detected page type (e.g., `post`, `archive`, `search`, `author`, `404`, `term`, `user`).

## Example usage

```php
add_filter( 'bricks/builder/current_page_type', function( $page_type ) {
    // Example: Treat a custom endpoint as an archive
    if ( get_query_var( 'my_custom_archive' ) ) {
        return 'archive';
    }

    return $page_type;
} );
```
