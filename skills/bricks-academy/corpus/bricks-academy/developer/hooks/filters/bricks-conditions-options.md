---
title: "Filter: bricks/conditions/options"
description: "Filters the condition options available in the element conditions interface. This allows you to add custom conditions that users can select to control element."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-conditions-options/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-conditions-options.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the condition options available in the element conditions interface. This allows you to add custom conditions that users can select to control element visibility.

## Parameters

- `$options` (*array*): Array of condition options. Each option defines the condition key, label, group, comparison operators, and value input type.

## Example usage

```php
add_filter( 'bricks/conditions/options', function( $options ) {
    // Add a custom 'Is Weekend' condition
    $options[] = [
        'key'     => 'is_weekend',
        'group'   => 'other', // Or a custom group created via bricks/conditions/groups
        'label'   => esc_html__( 'Is Weekend', 'my-plugin' ),
        'compare' => [
            'type'        => 'select',
            'options'     => [
                '==' => esc_html__( 'is', 'bricks' ),
            ],
        ],
        'value'   => [
            'type'    => 'select',
            'options' => [
                'true'  => esc_html__( 'True', 'bricks' ),
                'false' => esc_html__( 'False', 'bricks' ),
            ],
        ],
    ];

    return $options;
} );
```
