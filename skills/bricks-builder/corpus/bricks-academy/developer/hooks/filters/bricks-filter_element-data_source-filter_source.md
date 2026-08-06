---
title: "Filter: bricks/filter_element/data_source_{filter_source}"
description: "Filters the data source (options) for a specific filter source. The {$filtersource} portion of the hook name should be replaced with the actual source name."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-data_source-filter_source/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-data_source-filter_source.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the data source (options) for a specific filter source. The `{$filter_source}` portion of the hook name should be replaced with the actual source name.

Built-in `taxonomy`, `wpField`, and `customField` sources are handled before this dynamic filter runs. Use this hook for custom filter sources that Bricks does not populate internally.

## Parameters

- `$data_source` (*array*): Array of filter options. Each option should be an associative array with keys like `value`, `text`, `class`, etc.
- `$element` (*object*): The filter element instance.

## Example usage

```php
// Populate options for a custom source 'my_source'
add_filter( 'bricks/filter_element/data_source_my_source', function( $data_source, $element ) {
    $data_source[] = [
        'value' => 'option_1',
        'text'  => 'Option 1',
    ];

    $data_source[] = [
        'value' => 'option_2',
        'text'  => 'Option 2',
    ];

    return $data_source;
}, 10, 2 );
```
