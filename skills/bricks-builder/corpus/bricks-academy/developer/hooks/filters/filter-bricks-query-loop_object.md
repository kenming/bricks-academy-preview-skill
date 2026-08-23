---
title: "Filter: bricks/query/loop_object"
description: "The Bricks Query Loop supports 3 types of queries by default (Posts, Terms, and Users). But it can be extended to support any other query. While iterating."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-loop_object/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-loop_object.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
The Bricks [Query Loop](/builder/dynamic-content/query-loop/) supports 3 types of queries by default (Posts, Terms, and Users). But it can be extended to support [any other query](/developer/hooks/filters/filter-bricks-query-run/). While iterating through the query results, the iteration object could be manipulated using the `bricks/query/loop_object` like so:

```php
add_filter( 'bricks/query/loop_object', function( $loop_object, $loop_key, $query_obj ) {
    if ( $query_obj->object_type !== 'my_query_type' ) {
	return $loop_object;
    }

    // Perform some logic, for example:
    // global $post;
    // $post = get_post( $loop_object );
    // setup_postdata( $post );

    return $loop_object;
}, 10, 3 );
```

The filter callback receives two arguments:

- `$loop_object` is the current loop iteration value (from the results array)
- `$loop_key` is the current loop iteration key (from the results array)
- `$query_obj` is an instance of the `\Bricks\Query` class object

Related hooks:

- To add a query type to the Query control use [`bricks/setup/control_options`](/developer/hooks/filters/filter-bricks-setup-control_options/)
- To perform the custom query type and output the results use [`bricks/query/run`](/developer/hooks/filters/filter-bricks-query-run/)
