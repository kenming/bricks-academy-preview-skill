---
title: "Action: bricks/query/after_loop"
description: "If you are creating a custom query loop or a custom plugin, you might want to perform some additional tasks like setting/resetting specific data after the loop."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/action-bricks-query-after_loop/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/action-bricks-query-after_loop.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
If you are creating a custom query loop or a custom plugin, you might want to perform some additional tasks like setting/resetting specific data after the loop runs. (`@since 1.7.2`)

```php
// Perform certain action after the loop of query element oklvcq
add_action( 'bricks/query/after_loop', function( $query, $args ) {
  if ( $query->element_id !== 'oklvcq' ) {
    return;
  }
  // $args is an array of the element settings
  // Perform your own logic here

}, 10, 2 );
```
