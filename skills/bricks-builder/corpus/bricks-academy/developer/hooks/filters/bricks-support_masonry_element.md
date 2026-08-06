---
title: "Filter: bricks/support_masonry_element"
description: "Filters the list of element names that support the Masonry layout option. By default, this includes section, container, block, and div."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-support_masonry_element/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-support_masonry_element.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the list of element names that support the Masonry layout option. By default, this includes `section`, `container`, `block`, and `div`.

## Parameters

- `$element_names` (*array*): Array of element names (slugs) that support Masonry.

## Example usage

```php
add_filter( 'bricks/support_masonry_element', function( $element_names ) {
    // Enable Masonry support for a custom element
    $element_names[] = 'my-custom-grid';

    return $element_names;
} );
```
