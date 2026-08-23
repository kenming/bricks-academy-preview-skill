---
title: "Filter: bricks/database/bricks_get_all_templates_by_type_args"
description: "Filters the query arguments used to retrieve all Bricks templates. This is primarily used by multilingual plugins (like WPML and Polylang) to ensure only."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-database-bricks_get_all_templates_by_type_args/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-database-bricks_get_all_templates_by_type_args.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the query arguments used to retrieve all Bricks templates. This is primarily used by multilingual plugins (like WPML and Polylang) to ensure only templates in the current language are fetched.

## Parameters

- `$args` (*array*): Array of arguments passed to `get_posts()`.

## Example usage

```php
add_filter( 'bricks/database/bricks_get_all_templates_by_type_args', function( $args ) {
    // Example: Include private templates
    $args['post_status'] = [ 'publish', 'private' ];

    return $args;
} );
```
