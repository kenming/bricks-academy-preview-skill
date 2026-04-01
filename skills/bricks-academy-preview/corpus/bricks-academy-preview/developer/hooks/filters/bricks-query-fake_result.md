Filters the results of a "fake" query execution. Fake queries are auxiliary queries run by Bricks (e.g., to count total results for filters without pagination) that mirror the main query but with modified parameters (like `posts_per_page = -1`).

## Parameters

- `$results` (*array*): The query results (e.g., array of WP_Post objects or IDs).
- `$query` (*object*): The Bricks Query instance.

## Example usage

```php
add_filter( 'bricks/query/fake_result', function( $results, $query ) {
    // Example: Manipulate the results for a specific query ID
    if ( $query->id === 'my_filtered_loop' ) {
        // Custom logic to modify results
    }

    return $results;
}, 10, 2 );
```
