---
title: "Filter: bricks/link_css_selectors"
description: "Use this filter in your child theme to overwrite/extend the CSS selectors the \"Theme Styles > Link\" settings are applied to like this (since Bricks 1.10 also."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-link_css_selectors/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-link_css_selectors.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Use this filter in your child theme to overwrite/extend the CSS selectors the "Theme Styles > Link" settings are applied to like this (since Bricks 1.10 also available in the builder):

```php
add_filter( 'bricks/link_css_selectors', function( $link_css_selectors ) {
    // Add CSS link styles to .my-custom-element a
    $link_css_selectors[] = '.my-custom-element a';

    // OR return new list of CSS link selectors
    // $link_css_selectors = ['.link-wrapper a', '.link-wrapper-2 a'];

    return $link_css_selectors; // Array of selectors link styles are applied to
} );
```

:::note
If the theme styles link styles do not apply to your custom selectors, force the regeneration of the theme styles by changing and saving the link color, the padding, or the text decoration, for example. Your new selectors will then be available.
:::
