---
title: "Filter: bricks/builder/standard_fonts"
description: "Place and customize the following filter to display a different set of web-safe fonts in the typography control."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-standard-fonts/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-standard-fonts.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Place and customize the following filter to display a different set of web-safe fonts in the typography control.

```php
add_filter( 'bricks/builder/standard_fonts', function( $standard_fonts ) {
  // Option #1: Add individual standard font
  $standard_fonts[] = 'Verdana';

  // Option #2: Replace all standard fonts
  $standard_fonts = [
    'Georgia',
    'Times New Roman',
    'Verdana',
  ];

  return $standard_fonts;
} );
```
