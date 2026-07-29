---
title: "Filter: bricks/theme_styles"
description: "Filters the array of Theme Styles loaded from the database. This allows you to modify, add, or remove Theme Styles programmatically."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-theme_styles/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-theme_styles.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the array of Theme Styles loaded from the database. This allows you to modify, add, or remove Theme Styles programmatically.

## Parameters

- `$styles` (*array*): Associative array of Theme Styles, where the key is the style name and the value is an array of style data.

## Example usage

```php
add_filter( 'bricks/theme_styles', function( $styles ) {
    // Example: Add a default property to all theme styles
    foreach ( $styles as $key => $style ) {
        if ( ! isset( $styles[ $key ]['settings']['typography'] ) ) {
            $styles[ $key ]['settings']['typography'] = [ 'font-size' => '16px' ];
        }
    }

    return $styles;
} );
```
