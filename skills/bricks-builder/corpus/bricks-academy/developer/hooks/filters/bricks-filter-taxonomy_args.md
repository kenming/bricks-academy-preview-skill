---
title: "Filter: bricks/filter/taxonomy_args"
description: "Filters the arguments passed to getterms() when generating options for taxonomy-based filter elements (e.g., Checkbox, Radio, Select filters)."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter-taxonomy_args/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter-taxonomy_args.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the arguments passed to `get_terms()` when generating options for taxonomy-based filter elements (e.g., Checkbox, Radio, Select filters).

## Parameters

- `$args` (*array*): Array of arguments for `get_terms()`.
- `$element` (*object*): The filter element instance.

## Example usage

```php
add_filter( 'bricks/filter/taxonomy_args', function( $args, $element ) {
    // Example: Exclude specific term IDs from the filter options
    $args['exclude'] = [ 1, 2, 3 ];

    return $args;
}, 10, 2 );
```
