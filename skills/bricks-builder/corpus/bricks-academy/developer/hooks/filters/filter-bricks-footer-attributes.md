---
title: "Filter: bricks/footer/attributes"
description: "Programmatically add HTML attributes to the footer tag."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-footer-attributes/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-footer-attributes.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Programmatically add HTML attributes to the `footer` tag.

```php
add_filter( 'bricks/footer/attributes', function( $attributes ) {
  // Add 'data-is-footer' HTML attribute to footer with value 'y'
  $attributes['data-is-footer'] = 'y';

  return $attributes;
} );
```

- [/developer/hooks/filters/filter-bricks-header-attributes/](/developer/hooks/filters/filter-bricks-header-attributes/)
- [/developer/hooks/filters/filter-bricks-content-attributes/](/developer/hooks/filters/filter-bricks-content-attributes/)
