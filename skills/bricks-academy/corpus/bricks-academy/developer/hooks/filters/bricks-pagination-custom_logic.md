---
title: "Filter: bricks/pagination/custom_logic"
description: "Enable custom pagination logic in Bricks when your query type needs custom current-page and total-page handling."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-pagination-custom_logic/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-pagination-custom_logic.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
The `bricks/pagination/custom_logic` filter allows you to implement custom pagination logic in Bricks Builder based on specific query settings. `@since 2.2`

In this example, we'll demonstrate how to apply custom pagination logic to a custom loop.

Next, you will need to use the following 2 filters to amend the current page and total page arguments when generating HTML for the pagination:

- `bricks/pagination/current_page`
- `bricks/pagination/total_pages`

```php
// Return true if want to use custom logic, default is false
add_filter( 'bricks/pagination/custom_logic', function( $custom_logic, $query_settings, $element ) {
  $query_object_type = $query_settings['query']['objectType'] ?? false;

  // If not my custom loop, return original value
  if( $query_object_type !== 'my_custom_loop' ) {
    return $custom_logic;
  }

  // You can access the element settings via $element->settings

  return true;
}, 10, 3);

```
