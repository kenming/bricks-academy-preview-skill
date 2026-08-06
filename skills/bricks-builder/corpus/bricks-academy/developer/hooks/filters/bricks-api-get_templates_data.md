---
title: "Filter: bricks/api/get_templates_data"
description: "Filters the data returned by the Bricks REST API endpoint /get-templates-data/. This endpoint is used to retrieve templates, authors, bundles, tags, and other."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-api-get_templates_data/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-api-get_templates_data.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the data returned by the Bricks REST API endpoint `/get-templates-data/`. This endpoint is used to retrieve templates, authors, bundles, tags, and other assets for the template library.

## Parameters

- `$templates_data` (*array*): Array containing:
    - `templates` (*array*): List of template data.
    - `authors` (*array*): List of template authors.
    - `bundles` (*array*): List of template bundles.
    - `tags` (*array*): List of template tags.
    - `globalVariables` (*array*): Global variables.
    - `colorPalette` (*array*): Color palettes.
    - `timestamp` (*int*): Current timestamp.
    - `date` (*string*): Formatted date.
    - `get` (*array*): URL parameters from the request.

## Example usage

```php
add_filter( 'bricks/api/get_templates_data', function( $templates_data ) {
    // Example: Remove a specific template bundle by name
    if ( ! empty( $templates_data['bundles'] ) ) {
        foreach ( $templates_data['bundles'] as $key => $bundle ) {
            if ( $bundle === 'Deprecated Bundle' ) {
                unset( $templates_data['bundles'][ $key ] );
            }
        }
    }

    return $templates_data;
} );
```
