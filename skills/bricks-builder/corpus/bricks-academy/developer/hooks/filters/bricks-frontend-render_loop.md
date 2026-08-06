---
title: "Filter: bricks/frontend/render_loop"
description: "Filters the HTML output of a query loop iteration. This allows you to modify the content of each item rendered within a loop."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-frontend-render_loop/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-frontend-render_loop.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the HTML output of a query loop iteration. This allows you to modify the content of each item rendered within a loop.

## Parameters

- `$output` (*string*): The rendered HTML of the loop item.
- `$element` (*array*): The element data array.
- `$container` (*object*): The container element instance managing the loop.

## Example usage

```php
add_filter( 'bricks/frontend/render_loop', function( $output, $element, $container ) {
    // Example: Wrap each loop item in a custom div
    return '<div class="my-custom-loop-wrapper">' . $output . '</div>';
}, 10, 3 );
```
