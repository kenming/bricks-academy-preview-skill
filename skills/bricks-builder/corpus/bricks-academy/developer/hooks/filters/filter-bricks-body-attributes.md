---
title: "Filter: bricks/body/attributes"
description: "Filter the HTML attributes Bricks adds to the body tag on the frontend."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-body-attributes/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-body-attributes.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filter to add HTML attributes to the `body` tag (@since 1.5).

```php
add_filter( 'bricks/body/attributes', function( $attributes ) {
  // Add 'data-is-body' HTML attribute to footer with value 'y'
  $attributes['data-is-body'] = 'y';

  return $attributes;
} );
```
