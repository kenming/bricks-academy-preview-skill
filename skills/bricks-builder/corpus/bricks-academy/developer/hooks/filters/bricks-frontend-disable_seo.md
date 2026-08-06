---
title: "Filter: bricks/frontend/disable_seo"
description: "Determines whether Bricks should generate and output SEO meta tags (e.g., description, keywords, robots) and modify the document title. Use this to disable."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-frontend-disable_seo/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-frontend-disable_seo.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Determines whether Bricks should generate and output SEO meta tags (e.g., description, keywords, robots) and modify the document title. Use this to disable Bricks' built-in SEO features if you are using a dedicated SEO plugin.

## Parameters

- `$disable` (*bool*): Whether to disable SEO tags.

## Example usage

```php
add_filter( 'bricks/frontend/disable_seo', function( $disable ) {
    // Example: Always disable Bricks SEO features
    return true;
} );
```
