---
title: "Filter: bricks/render_header"
description: "Filters the rendered HTML of the Bricks header template. This allows you to wrap the header in custom markup or modify its output before it is echoed to the."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-render_header/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-render_header.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the rendered HTML of the Bricks header template. This allows you to wrap the header in custom markup or modify its output before it is echoed to the page.

## Parameters

- `$header_html` (*string*): The rendered HTML of the header.

## Example usage

```php
add_filter( 'bricks/render_header', function( $header_html ) {
    // Example: Add a notification bar before the header
    $notification = '<div class="notification-bar">Welcome!</div>';
    
    return $notification . $header_html;
} );
```
