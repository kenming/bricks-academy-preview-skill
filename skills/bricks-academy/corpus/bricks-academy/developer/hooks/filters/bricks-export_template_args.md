---
title: "Filter: bricks/export_template_args"
description: "Filters the URL arguments used for the \"Export Template\" link in the Bricks templates list table."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-export_template_args/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-export_template_args.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the URL arguments used for the "Export Template" link in the Bricks templates list table.

## Parameters

- `$args` (*array*): Array of query arguments for the export URL (e.g., `action`, `nonce`, `templateId`).
- `$post_id` (*int*): The ID of the template being exported.

## Example usage

```php
add_filter( 'bricks/export_template_args', function( $args, $post_id ) {
    // Example: Add a custom parameter to the export URL
    $args['my_param'] = 'value';

    return $args;
}, 10, 2 );
```
