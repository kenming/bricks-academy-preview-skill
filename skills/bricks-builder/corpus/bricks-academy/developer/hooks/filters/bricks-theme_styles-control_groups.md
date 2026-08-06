---
title: "Filter: bricks/theme_styles/control_groups"
description: "Filters the control groups available in the Theme Styles settings panel. This allows you to add new sections or tabs to organize custom Theme Style controls."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-theme_styles-control_groups/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-theme_styles-control_groups.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the control groups available in the Theme Styles settings panel. This allows you to add new sections or tabs to organize custom Theme Style controls.

## Parameters

- `$control_groups` (*array*): Associative array of control groups.

## Example usage

```php
add_filter( 'bricks/theme_styles/control_groups', function( $control_groups ) {
    // Add a new control group for 'My Plugin'
    $control_groups['my_plugin'] = [
        'title' => esc_html__( 'My Plugin Settings', 'my-plugin' ),
        'tab'   => 'content', // or 'style'
    ];

    return $control_groups;
} );
```
