Filters the list of Bricks query object types that support the "Is main query" setting (archive loop). By default, only 'post' queries are supported.

## Parameters

- `$object_types` (*array*): Array of supported query object types (e.g., `['post']`).

## Example usage

```php
add_filter( 'bricks/query/archive_query_supported_object_types', function( $object_types ) {
    // Example: Enable "Is main query" for user loops (if implementing custom archive logic)
    $object_types[] = 'user';

    return $object_types;
} );
```
