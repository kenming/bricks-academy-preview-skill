---
title: "Filter: bricks/is_layout_element"
description: "Allows to define your custom elements as a layout element, so they are recognised like the section, container, block, div elements and use the same controls."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-is_layout_element/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-is_layout_element.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Allows to define your custom elements as a layout element, so they are recognised like the section, container, block, div elements and use the same controls like query loop, flex controls, shape divider, etc.

```php
add_filter( 'bricks/is_layout_element', function( $layout_element_names ) {
    // Mark your custom element "custom_box" as a layout element
    $layout_element_names[] = 'custom_box';

    return $layout_element_names;
} );
```
