---
title: "Filter: bricks/elements/{element_name}/control_groups"
description: "Since Bricks 1.4 it is possible to add custom control groups to a specific element like so:"
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-elements-element_name-control_groups/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-elements-element_name-control_groups.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Since Bricks 1.4 it is possible to add custom control groups to a specific element like so:

```php
add_filter( 'bricks/elements/heading/control_groups', function( $control_groups ) {
    $control_groups['custom_controls'] = [
        'tab'      => 'content', // or 'style'
        'title'    => esc_html__( 'Custom controls', 'my_plugin' ),
    ];

    return $control_groups;
} );
```

Note: the above example adds a new control group with the title "**Custom controls**" to the **heading** element, using the filter `bricks/elements/**heading**/control_groups`. To learn about other Bricks controls, visit the [Controls section](/developer/controls/).
