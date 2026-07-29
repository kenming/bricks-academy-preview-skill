---
title: "Filter: bricks/assets/generate_css_from_element"
description: "Add custom element names to Bricks CSS generation so looped child styles are included for supported custom elements."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-assets-generate_css_from_element/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-assets-generate_css_from_element.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
This filter allows you to include your custom query loop supported element to generate the children styles in Bricks. (@since 1.9.2)

## Parameters

- `$element_names` (array): Additional loop-capable element names. Defaults to an empty array.
- `$current_element` (array): The element currently being processed for CSS generation.
- `$css_type` (string): The CSS generation area, such as `header`, `footer`, or `content`.

```php
add_filter( 'bricks/assets/generate_css_from_element', function( $element_names, $current_element, $css_type ) {
  // $css_type is a string (e.g. header, footer, content, etc.)
  // Add your custom element name so the looping children styles are generated.
  if ( ! in_array( 'my-custom-element-name', $element_names ) ) {
    $element_names[] = 'my-custom-element-name';
  }

  return $element_names;
}, 10, 3 );
```
