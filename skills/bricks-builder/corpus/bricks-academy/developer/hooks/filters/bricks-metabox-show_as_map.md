---
title: "Filter: bricks/metabox/show_as_map"
description: "Determines whether a Meta Box map field should be rendered as a map (using rwmbmeta()) or as raw latitude/longitude coordinates when used in dynamic data."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-metabox-show_as_map/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-metabox-show_as_map.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Determines whether a Meta Box map field should be rendered as a map (using `rwmb_meta()`) or as raw latitude/longitude coordinates when used in dynamic data.

## Parameters

- `$show_as_map` (*bool*): Whether to render as a map. Default is `false` (renders coordinates).
- `$field` (*array*): The Meta Box field settings array.
- `$post` (*WP_Post*): The current post object.

## Example usage

```php
add_filter( 'bricks/metabox/show_as_map', function( $show_as_map, $field, $post ) {
    // Example: Render as map for a specific field ID
    if ( $field['id'] === 'my_map_field' ) {
        return true;
    }

    return $show_as_map;
}, 10, 3 );
```
