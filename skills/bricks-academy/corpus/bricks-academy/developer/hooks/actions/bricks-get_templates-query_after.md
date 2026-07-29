---
title: "Action: bricks/get_templates/query_after"
description: "Runs after Bricks queries templates."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-get_templates-query_after/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-get_templates-query_after.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Runs after Bricks performs the uncached `WP_Query` inside `Templates::get_templates_query()`. Use it to restore integration context after the internal template query has run.

This action does not run when Bricks returns the template query from object cache.

## Parameters

- `$query` (WP_Query): The template query object.
- `$merged_args` (array): The query arguments after Bricks merges custom and default values.

## Example usage

```php
add_action( 'bricks/get_templates/query_after', function( $query, $merged_args ) {
    // Restore custom query context after template lookup.
}, 10, 2 );
```
