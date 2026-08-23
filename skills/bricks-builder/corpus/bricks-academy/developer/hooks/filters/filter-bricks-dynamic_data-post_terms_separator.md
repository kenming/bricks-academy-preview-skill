---
title: "Filter: bricks/dynamic_data/post_terms_separator"
description: "Programmatically set the post term separator like so:"
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-dynamic_data-post_terms_separator/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-dynamic_data-post_terms_separator.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Programmatically set the post term separator like so:

```php
add_filter( 'bricks/dynamic_data/post_terms_separator', function( $sep, $post, $taxonomy ) {
  return ' : ';
}, 10, 3 );
```
