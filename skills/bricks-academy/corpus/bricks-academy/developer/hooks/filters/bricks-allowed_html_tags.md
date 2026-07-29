---
title: "Filter: bricks/allowed_html_tags"
description: "Filters the list of allowed HTML tags that can be used when selecting a \"Custom\" HTML tag in element settings. This ensures that custom tags are sanitized."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-allowed_html_tags/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-allowed_html_tags.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the list of allowed HTML tags that can be used when selecting a "Custom" HTML tag in element settings. This ensures that custom tags are sanitized correctly.

## Parameters

- `$allowed_html_tags` (*array*): Array of allowed HTML tag names.

## Example usage

```php
add_filter( 'bricks/allowed_html_tags', function( $allowed_html_tags ) {
    // Add 'marquee' to the list of allowed tags
    $allowed_html_tags[] = 'marquee';

    return $allowed_html_tags;
} );
```
