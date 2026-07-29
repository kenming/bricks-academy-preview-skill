---
title: "Filter: bricks/conditions/groups"
description: "Filters the condition groups available in the element conditions interface. This allows you to add new categories for your custom conditions."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-conditions-groups/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-conditions-groups.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the condition groups available in the element conditions interface. This allows you to add new categories for your custom conditions.

## Parameters

- `$groups` (*array*): Array of condition groups. Each group has a `name` and `label`.

## Example usage

```php
add_filter( 'bricks/conditions/groups', function( $groups ) {
    // Add a custom condition group
    $groups[] = [
        'name'  => 'my_custom_group',
        'label' => esc_html__( 'My Custom Group', 'my-plugin' ),
    ];

    return $groups;
} );
```
