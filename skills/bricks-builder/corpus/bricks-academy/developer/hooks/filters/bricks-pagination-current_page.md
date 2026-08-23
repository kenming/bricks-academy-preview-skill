---
title: "Filter: bricks/pagination/current_page"
description: "The bricks/pagination/currentpage filter allows you to modify the current page number used in the pagination logic of Bricks Builder. In this example, we'll."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-pagination-current_page/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-pagination-current_page.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
The `bricks/pagination/current_page` filter allows you to modify the current page number used in the pagination logic of Bricks Builder. In this example, we'll demonstrate how to customize the current page value based on query variables for a custom loop. `@since 2.2`

You can use `\Bricks\Helpers::get_ajax_current_page()` helper function to retrieve the Bricks AJAX pagination endpoint current page value inside your custom query logic.

Related hooks:

- `bricks/pagination/custom_logic`
- `bricks/pagination/total_pages`

```php
add_filter( 'bricks/pagination/current_page', function( $current_page, $query_settings, $element ) {
  $query_object_type = $query_settings['query']['objectType'] ?? false;

  // If not my custom loop, return original value
  if( $query_object_type !== 'my_custom_loop' ) {
    return $current_page;
  }

  // You can access the element settings via $element->settings

  // Change current page based on query var
  if ( \Bricks\Helpers::get_ajax_current_page() ) {
    $current_page = \Bricks\Helpers::get_ajax_current_page();
  } elseif ( get_query_var( 'page' ) ) {
    // Check for 'page' on static front page
    $current_page = get_query_var( 'page' );
  } elseif ( get_query_var( 'paged' ) ) {
    $current_page = get_query_var( 'paged' );
  } else {
    $current_page = 1;
  }

  return $current_page;
}, 10, 3);
```
