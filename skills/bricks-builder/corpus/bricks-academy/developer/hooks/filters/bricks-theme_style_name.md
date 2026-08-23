---
title: "Filter: bricks/theme_style_name"
description: "Filters the name of the Theme Style used when generating the CSS file name. This allows you to sanitize or modify the name before it is used in the file system."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-theme_style_name/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-theme_style_name.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the name of the Theme Style used when generating the CSS file name. This allows you to sanitize or modify the name before it is used in the file system.

## Parameters

- `$name` (*string*): The theme style name.
- `$theme_style` (*array*): The theme style data array.

## Example usage

```php
add_filter( 'bricks/theme_style_name', function( $name, $theme_style ) {
    // Example: Prefix theme style file names
    return 'custom-prefix-' . $name;
}, 10, 2 );
```
