---
title: "Filter: bricks/filter_element/count_source_{filter_source}"
description: "Filters indexed count data for a specific custom filter source."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-count_source-filter_source/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-count_source-filter_source.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters indexed count data for a specific custom filter source. The `{$filter_source}` portion of the hook name should be replaced with the actual `filterSource` key, such as `wcField` or a custom source.

Built-in `taxonomy`, `wpField`, and `customField` sources are handled before this dynamic filter runs.

## Parameters

- `$count_source` (*array*): Indexed count rows. Each row can include `filter_value`, `filter_value_display`, `filter_value_id`, `filter_value_parent`, and `count`.
- `$element` (*object*): The filter element instance.

## Example usage

```php
add_filter( 'bricks/filter_element/count_source_wcField', function( $count_source, $element ) {
    foreach ( $count_source as &$row ) {
        if ( isset( $row['filter_value'] ) && $row['filter_value'] === 'featured' ) {
            $row['count'] = 999;
        }
    }
    unset( $row );

    return $count_source;
}, 10, 2 );
```
