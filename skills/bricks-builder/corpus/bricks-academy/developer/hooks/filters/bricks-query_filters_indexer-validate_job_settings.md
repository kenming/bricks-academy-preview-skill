---
title: "Filter: bricks/query_filters_indexer/validate_job_settings"
description: "Validates the settings of a filter job before the Query Filters Indexer processes it. This is used for unknown or custom filter sources to ensure they have the."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters_indexer-validate_job_settings/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters_indexer-validate_job_settings.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Validates the settings of a filter job before the Query Filters Indexer processes it. This is used for unknown or custom filter sources to ensure they have the necessary configuration.

## Parameters

- `$validate` (*bool*): Whether the settings are valid. Default is `false` for unknown sources.
- `$filter_source` (*string*): The source of the filter data (e.g., `wcField`, `customSource`).
- `$filter_settings` (*array*): The settings of the filter element.

## Example usage

```php
add_filter( 'bricks/query_filters_indexer/validate_job_settings', function( $validate, $filter_source, $filter_settings ) {
    // Validate settings for a custom source
    if ( $filter_source === 'my_custom_source' ) {
        // Check if required 'my_key' setting is present
        return ! empty( $filter_settings['my_key'] );
    }

    return $validate;
}, 10, 3 );
```
