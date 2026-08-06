---
title: "Filter: bricks/get_template_authors"
description: "Filters the list of authors displayed in the Bricks template manager. This allows you to customize which authors are selectable when filtering templates."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_template_authors/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_template_authors.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the list of authors displayed in the Bricks template manager. This allows you to customize which authors are selectable when filtering templates.

## Parameters

- `$authors` (*array*): Array of author display names.

## Example usage

```php
add_filter( 'bricks/get_template_authors', function( $authors ) {
    // Example: Remove 'admin' from the authors list
    if ( ( $key = array_search( 'admin', $authors ) ) !== false ) {
        unset( $authors[ $key ] );
    }

    return $authors;
} );
```
