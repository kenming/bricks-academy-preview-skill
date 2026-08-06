---
title: "Action: bricks/database/get_all_templates_by_type/after_query"
description: "Runs after Bricks queries templates by type."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-database-get_all_templates_by_type-after_query/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-database-get_all_templates_by_type-after_query.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Runs after Bricks performs the uncached `get_posts()` query for all published Bricks templates. Use it to restore integration query context after Bricks has fetched template IDs.

This action does not run when Bricks returns templates from object cache or the in-memory `Database::$all_templates` cache.

## Parameters

- `$template_ids` (array): Template IDs returned by the query.
- `$args` (array): The query arguments used to fetch templates.

## Example usage

```php
add_action( 'bricks/database/get_all_templates_by_type/after_query', function( $template_ids, $args ) {
    // Restore custom query or language context here.
}, 10, 2 );
```
