---
title: "Filter: bricks/query/result_count"
description: "Filter the result count Bricks reports for a query object before pagination or related UI uses that total."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result_count/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result_count.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
This filter allows you to modify the query result count (@since 1.8).

```php
add_filter( 'bricks/query/result_count', function( $result_count, $query_obj ) {
  // Return: Element ID is not "lbsijo", nor is it a post query
  if( $query_obj->element_id !== 'lbsijo' || $query_obj->object_type !== 'post' ) {
    return $result_count;
  }

  // Perform your logic here
  // Use $query_obj->query_result to access the query result
  $new_count = 123;
  return $new_count;
}, 10, 2 );
```
