---
title: "Filter: bricks/metabox/taxonomy/show_as_link"
description: "Determines whether Meta Box taxonomy fields retrieved via dynamic data should be rendered as links to the term archives."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-metabox-taxonomy-show_as_link/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-metabox-taxonomy-show_as_link.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Determines whether Meta Box taxonomy fields retrieved via dynamic data should be rendered as links to the term archives.

## Parameters

- `$show_as_link` (*bool*): Whether to render as links. Default is `true`.
- `$value` (*mixed*): The raw value of the taxonomy field.
- `$field` (*array*): The Meta Box field settings array.

## Example usage

```php
add_filter( 'bricks/metabox/taxonomy/show_as_link', function( $show_as_link, $value, $field ) {
    // Disable links for a specific taxonomy field
    if ( $field['id'] === 'my_taxonomy_field' ) {
        return false;
    }

    return $show_as_link;
}, 10, 3 );
```
