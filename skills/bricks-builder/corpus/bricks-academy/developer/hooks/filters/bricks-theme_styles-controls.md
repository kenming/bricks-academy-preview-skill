---
title: "Filter: bricks/theme_styles/controls"
description: "Filters the individual controls available within the Theme Styles settings. This allows you to add custom fields to existing Theme Style groups or to your own."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-theme_styles-controls/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-theme_styles-controls.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the individual controls available within the Theme Styles settings. This allows you to add custom fields to existing Theme Style groups or to your own custom groups.

## Parameters

- `$controls` (*array*): Associative array of controls.

## Example usage

```php
add_filter( 'bricks/theme_styles/controls', function( $controls ) {
    // Add a custom color control to the 'colors' group
    $controls['myCustomColor'] = [
        'group' => 'colors', // Target existing group
        'label' => esc_html__( 'My Custom Color', 'my-plugin' ),
        'type'  => 'color',
    ];

    return $controls;
} );
```
