The Bricks [Query Loop](/builder/dynamic-content/query-loop/) supports 3 types of queries by default (Posts, Terms and Users). But it can be extended to support any other query. To return a custom query result, Bricks can be extended using the WP filter `bricks/query/run` like so:

```php
add_filter( 'bricks/query/run', function( $results, $query_obj ) {
    if ( $query_obj->object_type !== 'my_query_type' ) {
	return $results;
    }

    // Perform the query
    // Assign the results to $results (array)

    return $results;
}, 10, 2 );
```

The filter callback receives two arguments:

- `$results` is the results array (empty by default). The loop will iterate through this array.
- `$query_obj` is an instance of the `\Bricks\Query` class object

Note: This hook should be used to add different types of query results. If you want to alter the posts, terms, or users query, use the following hooks:

- **Posts**: [`bricks/posts/query_vars`](/developer/hooks/filters/filter-bricks-posts-query_vars/)
- **Terms**: [bricks/terms/query_vars](/developer/hooks/filters/filter-bricks-terms-query_vars/)
- **Users**: [bricks/users/query_vars](/developer/hooks/filters/filter-bricks-users-query_vars/)

Related hooks:

- To add a query type to the Query control use [`bricks/setup/control_options`](/developer/hooks/filters/filter-bricks-setup-control_options/)
- To manage the object on every loop iteration use [`bricks/query/loop_object`](/developer/hooks/filters/filter-bricks-query-loop_object/)
