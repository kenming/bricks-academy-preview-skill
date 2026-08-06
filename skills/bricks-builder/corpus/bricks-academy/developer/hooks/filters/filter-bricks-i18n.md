---
title: "Filter: bricks/builder/i18n"
description: "Place and customize the following filter to add translatable string to the builder."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-i18n/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-i18n.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Place and customize the following filter to add translatable string to the builder.

```php
add_filter( 'bricks/builder/i18n', function( $i18n ) {
  // Example: Provide translatable string for element category 'custom'
  $i18n['custom'] = esc_html__( 'Custom', 'bricks' );

  return $i18n;
} );
```
