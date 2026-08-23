---
title: "Filter: bricks/get_element_data/maybe_from_post_id"
description: "Provide an alternate post ID for Bricks element-data lookups when custom elements reference content stored in another post or template."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-get_element_data-maybe_from_post_id/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-get_element_data-maybe_from_post_id.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
The `bricks/get_element_data/maybe_from_post_id` filter, available `@since 1.11`, allows you to specify an additional post ID from which to retrieve element data. This can be useful when dealing with custom elements that reference templates, posts, or external data sources, where the target element is not found within the standard element set. (Especially when dealing with Code element + Signed signature)

### When to Use

This filter is useful when working with custom elements that reference data from other templates or posts. For example, if you have a custom element that stores additional Bricks content in another post or template, and there is a code element with a signed signature located there, Bricks may not render the code element on the frontend because it doesn't know where to retrieve the signature. This filter allows you to specify the correct post or template to ensure that all elements are properly rendered.

```php
add_filter( 'bricks/get_element_data/maybe_from_post_id', function( $id, $element_data ) {
  // Check if the element is my custom element and has custom_template_id set on the control
  if ( isset( $element_data['name'] ) && $element_data['name'] === 'my-custom-element' && ! empty( $element_data['settings']['custom_template_id'] ) ) {
    $id = $element_data['settings']['custom_template_id'];
  }

  return $id;
}, 10, 2 );

```
