---
title: "Filter: bricks/query/init_loop_index"
description: "Filter the initial Bricks loop index so paginated, infinite-scroll, or custom queries keep their loop-based output aligned."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-init_loop_index/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-init_loop_index.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
The `bricks/query/init_loop_index` filter, available `@since 1.11`, allows you to modify the initial loop index when using various query types in Bricks Builder. This filter is especially useful in cases such as infinite scroll or paginated queries, where setting the correct loop index is crucial for displaying content seamlessly across multiple pages especially when using dynamic backgound images or colors. Without this hook, the generated dynamic CSS might be applied on the incorrect element when performing infinite scroll or paginate actions.

### When to Use

This filter is particularly useful when creating a custom query type using the [bricks/setup/control_options](/developer/hooks/filters/filter-bricks-nav_menu-menu/) hook. You can implement your own logic for handling pagination and adjust the initial loop index accordingly.

```php
add_filter( 'bricks/query/init_loop_index', function ( $initial_index, $object_type, $query ) {
  // Check if the object type is 'my_custom_query'
  if ( $object_type !== 'my_custom_query' ) {
    return $initial_index;
  }

  // Add your custom logic to modify the initial loop index
  // Example: Calculate based on custom logic
  // $initial_index = custom_logic_to_calculate_index();

  return $initial_index;
}, 10, 3 );

```
