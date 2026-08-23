---
title: "Filter: bricks/breadcrumbs/items"
description: "Filters the array of breadcrumb items (HTML strings) before they are rendered in the Breadcrumbs element. This allows you to add, remove, or modify specific."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-breadcrumbs-items/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-breadcrumbs-items.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the array of breadcrumb items (HTML strings) before they are rendered in the Breadcrumbs element. This allows you to add, remove, or modify specific breadcrumb links.

## Parameters

- `$breadcrumb_items` (*array*): Array of HTML strings, where each string represents a breadcrumb item (e.g., a link or current page span).

## Example usage

```php
add_filter( 'bricks/breadcrumbs/items', function( $breadcrumb_items ) {
    // Example: Add a custom item after the Home link (assuming Home is the first item)
    $custom_item = '<a href="/custom-link/">Custom Link</a>';
    array_splice( $breadcrumb_items, 1, 0, $custom_item );

    return $breadcrumb_items;
} );
```
