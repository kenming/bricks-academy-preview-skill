Filters the ending index used when slicing the query results. This allows you to control which portion of the results is displayed, useful for custom pagination or limit logic.

## Parameters

- `$end` (*int*): The ending index for the result slice.
- `$query` (*object*): The Bricks Query instance.

## Example usage

```php
add_filter( 'bricks/query/result_end', function( $end, $query ) {
    // Example: Limit results to 5 for a specific query ID
    if ( $query->id === 'my_limited_query' ) {
        return 5;
    }

    return $end;
}, 10, 2 );
```
