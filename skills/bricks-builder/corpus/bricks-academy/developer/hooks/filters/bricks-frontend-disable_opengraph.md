---
title: "Filter: bricks/frontend/disable_opengraph"
description: "Determines whether Bricks should generate and output Open Graph meta tags (e.g., og:title, og:image). Use this to disable Bricks' Open Graph implementation if."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-frontend-disable_opengraph/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-frontend-disable_opengraph.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Determines whether Bricks should generate and output Open Graph meta tags (e.g., `og:title`, `og:image`). Use this to disable Bricks' Open Graph implementation if you are using a third-party SEO plugin that already handles this.

## Parameters

- `$disable` (*bool*): Whether to disable Open Graph tags.

## Example usage

```php
add_filter( 'bricks/frontend/disable_opengraph', function( $disable ) {
    // Example: Disable Open Graph tags on 'product' post type
    if ( is_singular( 'product' ) ) {
        return true;
    }

    return $disable;
} );
```
