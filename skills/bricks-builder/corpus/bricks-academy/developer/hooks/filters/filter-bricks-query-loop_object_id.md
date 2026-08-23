---
title: "Filter: bricks/query/loop_object_id"
description: "Bricks will use \\Bricks\\Query::getloopobjectid() to retrieve the looping iteration's object ID."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-loop_object_id/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-loop_object_id.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Bricks will use `\Bricks\Query::get_loop_object_id()` to retrieve the looping iteration's object ID.

This static function is used in many places. Especially when trying to parse dynamic data.  By default, Bricks uses the looping ID if the looping object is a WP_Post, WP_Term, or WP_User object. This filter allows you to change the ID conditionally.

```php
// Change the object_id if the current looping query type is myCustomQueryType
add_filter( 'bricks/query/loop_object_id', function( $object_id, $object, $query_id ) {
    $query_object_type = \Bricks\Query::get_query_object_type( $query_id );
    if ( $query_object_type !== 'myCustomQueryType' ) {
	return $object_id;
    }

    // Set my loop_object_id
    $new_id = my_custom_function_to_transform_the_id( $object_id );
    return $new_id;
}, 10, 3 );
```

### Related hooks:

- [bricks/setup/control_options](/developer/hooks/filters/filter-bricks-setup-control_options/): To add a custom query type to the Query control
- [bricks/query/loop_object](/developer/hooks/filters/filter-bricks-query-loop_object/): To manage the object on every loop iteration
