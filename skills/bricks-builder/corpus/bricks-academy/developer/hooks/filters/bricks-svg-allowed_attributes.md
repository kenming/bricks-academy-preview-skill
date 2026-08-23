---
title: "Filter: bricks/svg/allowed_attributes"
description: "Filters the list of allowed SVG attributes during sanitization. This is used by the Bricks SVG sanitizer to ensure that uploaded or rendered SVGs do not contain."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-svg-allowed_attributes/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-svg-allowed_attributes.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the list of allowed SVG attributes during sanitization. This is used by the Bricks SVG sanitizer to ensure that uploaded or rendered SVGs do not contain malicious attributes.

## Parameters

- `$attributes` (*array*): Array of allowed SVG attributes.

## Example usage

```php
add_filter( 'bricks/svg/allowed_attributes', function( $attributes ) {
    // Example: Allow 'data-custom' attribute
    $attributes[] = 'data-custom';

    return $attributes;
} );
```
