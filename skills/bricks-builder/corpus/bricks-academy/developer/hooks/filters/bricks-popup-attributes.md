---
title: "Filter: bricks/popup/attributes"
description: "Filters the HTML attributes of the popup container. This allows you to add custom classes, data attributes, or other attributes to the popup element."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-popup-attributes/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-popup-attributes.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the HTML attributes of the popup container. This allows you to add custom classes, data attributes, or other attributes to the popup element.

## Parameters

- `$attributes` (*array*): Array of HTML attributes (e.g., `class`, `data-popup-id`).
- `$popup_id` (*int*): The ID of the popup template.

## Example usage

```php
add_filter( 'bricks/popup/attributes', function( $attributes, $popup_id ) {
    // Example: Add a custom class to a specific popup
    if ( $popup_id === 1234 ) {
        $attributes['class'][] = 'my-custom-popup-class';
        $attributes['data-custom-attr'] = 'value';
    }

    return $attributes;
}, 10, 2 );
```
