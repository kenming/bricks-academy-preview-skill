---
title: "Filter: bricks/elements/{element_name}/scripts"
description: "Filters the script handles registered for a specific element. Replace {element_name} with the element name."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-elements-element_name-scripts/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-elements-element_name-scripts.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the list of script handles to be loaded for a specific element. The `{$element_name}` portion of the hook name should be replaced with the element's name (e.g., `slider`, `accordion`, `my_custom_element`).

## Parameters

- `$scripts` (*array*): Array of script handles registered via `wp_register_script`.

## Example usage

```php
// Filter scripts for the 'slider' element
add_filter( 'bricks/elements/slider/scripts', function( $scripts ) {
    // Add a custom script dependency
    $scripts[] = 'my-custom-slider-script';

    return $scripts;
} );
```
