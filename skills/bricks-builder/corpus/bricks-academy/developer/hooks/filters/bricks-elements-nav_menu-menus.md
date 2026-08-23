---
title: "Filter: bricks/elements/nav_menu/menus"
description: "Filters the nav menus shown in the Nav Menu element while in the builder."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-elements-nav_menu-menus/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-elements-nav_menu-menus.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the nav menus shown in the Nav Menu element while in the builder. Return an array of menu objects to override the menus Bricks loads from WordPress.

## Parameters

- `$menus` (array|null): Menus to use in the builder. Return null to let Bricks fall back to wp_get_nav_menus().

## Example usage

```php
add_filter( 'bricks/elements/nav_menu/menus', function( $menus ) {
    return wp_get_nav_menus();
} );
```
