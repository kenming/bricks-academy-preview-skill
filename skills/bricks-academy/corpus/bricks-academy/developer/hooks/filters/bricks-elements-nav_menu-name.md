---
title: "Filter: bricks/elements/nav_menu/name"
description: "Filters a nav menu label shown in the Nav Menu element."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-elements-nav_menu-name/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-elements-nav_menu-name.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters a nav menu label shown in the Nav Menu element. Use it to adjust menu names in the builder, for example by appending language or site context.

## Parameters

- `$name` (string): The menu name.
- `$menu` (WP_Term): The nav menu term object.

## Example usage

```php
add_filter( 'bricks/elements/nav_menu/name', function( $name, $menu ) {
    return $name . ' (' . $menu->term_id . ')';
}, 10, 2 );
```
