---
title: "Filter: bricks/content/attributes"
description: "Programmatically add HTML attributes to the main tag."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-content-attributes/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-content-attributes.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Programmatically add HTML attributes to the `main` tag.

```php
add_filter( 'bricks/content/attributes', function( $attributes ) {
  // Add 'data-is-content' HTML attribute to main with value 'y'
  $attributes['data-is-content'] = 'y';
  return $attributes;
} );
```

- [/developer/hooks/filters/filter-bricks-header-attributes/](/developer/hooks/filters/filter-bricks-header-attributes/)
- [/developer/hooks/filters/filter-bricks-header-attributes/](/developer/hooks/filters/filter-bricks-header-attributes/)
