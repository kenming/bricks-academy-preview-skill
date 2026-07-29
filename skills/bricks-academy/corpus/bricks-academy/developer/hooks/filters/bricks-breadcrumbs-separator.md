---
title: "Filter: bricks/breadcrumbs/separator"
description: "Filters the separator HTML displayed between items in the Breadcrumbs element."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-breadcrumbs-separator/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-breadcrumbs-separator.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the separator HTML displayed between items in the Breadcrumbs element.

## Parameters

- `$separator` (*string*): The HTML string for the breadcrumb separator (e.g., a span containing text or an icon).

## Example usage

```php
add_filter( 'bricks/breadcrumbs/separator', function( $separator ) {
    // Change separator to a custom character
    return '<span class="bricks-breadcrumbs-separator"> &raquo; </span>';
} );
```
