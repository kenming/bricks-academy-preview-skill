Filters the query arguments used by the Query Filters indexer to find objects (posts, terms, users) that need to be indexed.

## Parameters

- `$args` (*array*): The query arguments (for `WP_Query`, `WP_Term_Query`, or `WP_User_Query`).
- `$filter_source` (*string*): The source of the filter data (e.g., `wpField`, `customField`).
- `$filter_settings` (*array*): The settings of the filter element being indexed.
- `$query_type` (*string*): The type of query being run (`wp_query`, `wp_term_query`, `wp_user_query`).

## Example usage

```php
add_filter( 'bricks/query_filters/index_args', function( $args, $filter_source, $filter_settings, $query_type ) {
    // Example: Include 'private' posts when indexing
    if ( $query_type === 'wp_query' ) {
        $args['post_status'] = [ 'publish', 'private' ];
    }

    return $args;
}, 10, 4 );
```
