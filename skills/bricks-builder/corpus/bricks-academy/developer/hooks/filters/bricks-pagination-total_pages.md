---
title: "Filter: bricks/pagination/total_pages"
description: "The bricks/pagination/totalpages filter allows you to modify the total number of pages used in the pagination logic of Bricks Builder. In this example, we'll."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-pagination-total_pages/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-pagination-total_pages.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
The `bricks/pagination/total_pages` filter allows you to modify the total number of pages used in the pagination logic of Bricks Builder. In this example, we'll demonstrate how to customize the total pages value based on custom loop results. `@since 2.2`

Related hooks:

- `bricks/pagination/custom_logic`
- `bricks/pagination/current_page`

```php
add_filter( 'bricks/pagination/total_pages', function( $total_page, $query_settings, $element ) {
  $query_object_type = $query_settings['query']['objectType'] ?? false;

  // If not my custom loop, return original value
  if( $query_object_type !== 'my_custom_loop' ) {
    return $total_page;
  }

  // You can access the element settings via $element->settings

  // My result stored in a global variable
  global $my_custom_loop_results;

  if ( ! $my_custom_loop_results ) {
    return $total_page;
  }

  // My predefined items per page
  $post_per_page = 3;

  return ceil( count( $my_custom_loop_results ) / $post_per_page );
}, 10, 3);
```
