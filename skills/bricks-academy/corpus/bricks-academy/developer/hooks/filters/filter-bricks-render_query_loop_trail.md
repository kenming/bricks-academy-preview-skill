---
title: "Filter: bricks/render_query_loop_trail"
description: "Control whether Bricks renders the query loop trail node that frontend JavaScript uses to read query settings."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-render_query_loop_trail/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-render_query_loop_trail.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
The `bricks/render_query_loop_trail` (@since 1.11.1) filter controls the output of the query loop trail node in Bricks. This node is automatically added to each query loop and records the loop's settings, which are then accessed by frontend JavaScript to manage various query-related tasks. Once these settings are read by Bricks, the node is removed from the DOM.

For some third-party plugins, this node may not be needed—especially if they use custom AJAX endpoints to update query results independently of Bricks. Using this filter, you can control whether or not the query loop trail node is rendered.

```php
// Return true = render the query loop trail node
// Return false = skip the query loop trail node
add_filter( 'bricks/render_query_loop_trail', function( $render, $element, $query ) {
  // Do not render query loop trail node if my-custom-param parameter exists
  if ( isset( $_GET['my-custom-param'] ) ) {
    $render = false;
  }

  return $render;
}, 10, 3 );
```

In this example, if the `my-custom-param` parameter is detected in the URL, the query loop trail node will not be rendered. This can be useful for third-party plugins with custom AJAX endpoints that handle query configurations independently.
