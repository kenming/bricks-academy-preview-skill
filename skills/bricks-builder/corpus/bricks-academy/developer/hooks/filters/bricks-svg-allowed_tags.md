---
title: "Filter: bricks/svg/allowed_tags"
description: "Filters the list of allowed SVG tags during sanitization. This is used by the Bricks SVG sanitizer to ensure that uploaded or rendered SVGs do not contain."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-svg-allowed_tags/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-svg-allowed_tags.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the list of allowed SVG tags during sanitization. This is used by the Bricks SVG sanitizer to ensure that uploaded or rendered SVGs do not contain malicious tags.

## Parameters

- `$tags` (*array*): Array of allowed SVG tags.

## Example usage

```php
add_filter( 'bricks/svg/allowed_tags', function( $tags ) {
    // Example: Allow 'foreignObject' tag (use with caution!)
    $tags[] = 'foreignObject';

    return $tags;
} );
```
