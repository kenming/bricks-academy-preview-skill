Available since 1.8, this filter lets you customize the query results and implement additional logic. Like modifying the post, term, or user object type. Which was previously not editable through the [`bricks/query/run`](/article/filter-bricks-query-run/) filter.

```php
// Use this filter to rearrange it by post title (PHP way instead of query orderby)
add_filter( 'bricks/query/result', function( $result, $query_obj ){
  // Return: Element ID is not "djvsvi", nor is it a post query
  if ( $query_obj->element_id !== 'djvsvi' || $query_obj->object_type !== 'post' ) {
    return $result;
  }

  // Sort by post title (descending)
  // Result is WP_Query object with posts
  if ( $result->have_posts() ) {
    $posts = $result->posts;

    usort( $posts, function( $a, $b ) {
      return strcmp( $b->post_title, $a->post_title );
    });

    $result->posts = $posts;
  }

  return $result;
}, 10, 2 );
```
