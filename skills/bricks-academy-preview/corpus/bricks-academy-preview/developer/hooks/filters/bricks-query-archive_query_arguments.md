Filters the list of `WP_Query` arguments that are preserved from the main WordPress query when "Is main query" is enabled in a query loop. This ensures that essential archive parameters (like pagination, taxonomy terms) are passed to the Bricks query.

## Parameters

- `$arguments` (*array*): Array of `WP_Query` argument keys (e.g., `post_type`, `posts_per_page`, `tax_query`).

## Example usage

```php
add_filter( 'bricks/query/archive_query_arguments', function( $arguments ) {
    // Example: specific custom query var from the main query
    $arguments[] = 'my_custom_var';

    return $arguments;
} );
```
