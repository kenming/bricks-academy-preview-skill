---
title: "Filter: bricks/get_templates/query_vars"
description: "Filters the query arguments used by Templates::gettemplatesquery() to retrieve Bricks templates. This allows you to customize which templates are fetched, for."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_templates-query_vars/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_templates-query_vars.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the query arguments used by `Templates::get_templates_query()` to retrieve Bricks templates. This allows you to customize which templates are fetched, for example, to support multilingual plugins or custom filtering.

## Parameters

- `$query_vars` (*array*): Array of arguments passed to `WP_Query`.

## Example usage

```php
add_filter( 'bricks/get_templates/query_vars', function( $query_vars ) {
    // Example: Exclude templates with a specific meta key
    $query_vars['meta_query'][] = [
        'key'     => 'my_exclude_key',
        'compare' => 'NOT EXISTS',
    ];

    return $query_vars;
} );
```
