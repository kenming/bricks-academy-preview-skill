---
title: "Filter: bricks/wpml/exclude_controls_from_translation"
description: "Filters Bricks control keys excluded from WPML translation."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-wpml-exclude_controls_from_translation/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-wpml-exclude_controls_from_translation.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters Bricks control keys excluded from WPML translation. Return the control keys that should not be translated for the current element/control context.

## Parameters

- `$excluded_keys` (array): Control keys excluded from translation.
- `$element` (array): The Bricks element data.
- `$control` (array): The control definition.
- `$key` (string): The current control key or repeater field key.

## Example usage

```php
add_filter( 'bricks/wpml/exclude_controls_from_translation', function( $excluded_keys, $element, $control, $key ) {
    $excluded_keys[] = 'my_untranslated_control';

    return $excluded_keys;
}, 10, 4 );
```
