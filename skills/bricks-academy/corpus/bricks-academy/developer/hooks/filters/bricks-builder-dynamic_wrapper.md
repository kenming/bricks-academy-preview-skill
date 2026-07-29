---
title: "Filter: bricks/builder/dynamic_wrapper"
description: "Filters the dynamic wrappers available in the Bricks builder. Dynamic wrappers are used to inject content before or after specific hooks in the builder canvas."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-builder-dynamic_wrapper/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-builder-dynamic_wrapper.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the dynamic wrappers available in the Bricks builder. Dynamic wrappers are used to inject content before or after specific hooks in the builder canvas (e.g., WooCommerce hooks).

## Parameters

- `$dynamic_wrapper` (*array*): Array of dynamic wrappers.

## Example usage

```php
add_filter( 'bricks/builder/dynamic_wrapper', function( $dynamic_wrapper ) {
    // Add a custom dynamic wrapper
    $dynamic_wrapper[] = [
        'name' => 'my_custom_wrapper',
        'title' => esc_html__( 'My Custom Wrapper', 'my-plugin' ),
        'hooks' => [
            'before' => 'my_custom_action_before',
            'after'  => 'my_custom_action_after',
        ],
    ];

    return $dynamic_wrapper;
} );
```
