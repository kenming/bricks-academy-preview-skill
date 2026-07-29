---
title: "Filter: bricks/render_footer"
description: "Filters the rendered HTML of the Bricks footer template. This allows you to wrap the footer in custom markup or modify its output before it is echoed to the."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-render_footer/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-render_footer.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the rendered HTML of the Bricks footer template. This allows you to wrap the footer in custom markup or modify its output before it is echoed to the page.

## Parameters

- `$footer_html` (*string*): The rendered HTML of the footer.

## Example usage

```php
add_filter( 'bricks/render_footer', function( $footer_html ) {
    // Example: Wrap the footer in a custom container
    return '<div class="custom-footer-wrapper">' . $footer_html . '</div>';
} );
```
