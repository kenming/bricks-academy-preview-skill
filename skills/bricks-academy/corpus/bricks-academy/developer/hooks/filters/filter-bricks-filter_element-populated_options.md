---
title: "Filter: bricks/filter_element/populated_options"
description: "The bricks/filterelement/populatedoptions PHP filter allows you to modify the populated options of Filter - Select, Filter - Radio, and Filter - Checkbox."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-filter_element-populated_options/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-filter_element-populated_options.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
The` bricks/filter_element/populated_options` PHP filter allows you to modify the populated options of **Filter - Select**, **Filter - Radio**, and **Filter - Checkbox** elements **before** they are rendered into HTML. `(@since 2.0.2)`

This is useful if you want to:

- Add/remove certain options
- Reorder options (based on complicated custom requirement)
- Change display text or values

### Example:

The following example removes the "biography" option from a filter element with the ID `uzehuy`:

```php
/**
 * $options is an array of options that are populated by the element
 * 'value' is the value of the option
 * 'text' is the display text of the option
 * 'is_all' exists and is true if the option is the "All" option
 * 'is_placeholder' exist and is true if the option is a placeholder option
 */
add_filter( 'bricks/filter_element/populated_options', function( $options, $element ) {
  if ( $element->id === 'uzehuy' ) {
    // Remove the options that value is 'biography'
    $options = array_filter( $options, function( $option ) {
      return $option['value'] !== 'biography';
    } );
  }

  return $options;
}, 10, 2 );
```
