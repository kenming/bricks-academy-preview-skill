---
title: "Filter: bricks/acf/taxonomy/show_as_link"
description: "Determines whether the ACF Taxonomy field dynamic data output should be rendered as links to the term archives."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-acf-taxonomy-show_as_link/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-acf-taxonomy-show_as_link.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Determines whether the ACF Taxonomy field dynamic data output should be rendered as links to the term archives.

## Parameters

- `$show_as_link` (*bool*): Whether to render as links. Defaults to `true`.
- `$value` (*mixed*): The raw value of the ACF Taxonomy field.
- `$field` (*array*): The ACF field settings.

## Example usage

```php
add_filter( 'bricks/acf/taxonomy/show_as_link', function( $show_as_link, $value, $field ) {
    // Disable links for taxonomy terms
    return false;
}, 10, 3 );
```
