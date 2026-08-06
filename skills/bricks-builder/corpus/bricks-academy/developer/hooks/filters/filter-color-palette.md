---
title: "Filter: bricks/builder/color_palette"
description: "Place and customize the following filter to display a different default color palette for the color control."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-color-palette/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-color-palette.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Place and customize the following filter to display a different default color palette for the color control.

```php
add_filter( 'bricks/builder/color_palette', function( $colors ) {
  // Option #1: Add an individual color
    $colors[] = [
      'hex' => '#3ce77b',
      'rgb' => 'rgba(60, 231, 123, 0.56)',
    ];

  // Option #2: Override entire color palette
  $colors = [
    ['hex' => '#3ce77b'],
    ['hex' => '#f1faee'],
    ['hex' => '#a8dadc'],
    ['hex' => '#457b9d'],
    ['hex' => '#1d3557'],
  ];

  return $colors;
} );
```
