---
title: "Filter: bricks/rtl_languages"
description: "Filters the list of language codes that Bricks considers right-to-left (RTL). This affects the layout direction of the builder interface when a specific locale."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-rtl_languages/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-rtl_languages.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the list of language codes that Bricks considers right-to-left (RTL). This affects the layout direction of the builder interface when a specific locale is active.

## Parameters

- `$languages` (*array*): Array of RTL language codes (e.g., `['ar', 'he', 'fa']`).

## Example usage

```php
add_filter( 'bricks/rtl_languages', function( $languages ) {
    // Add a custom RTL language code
    $languages[] = 'abc';

    return $languages;
} );
```
