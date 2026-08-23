---
title: "Filter: bricks/query_filters_cf_integration/register_providers"
description: "Filters custom field providers used by query filter integrations."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters_cf_integration-register_providers/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters_cf_integration-register_providers.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters custom field providers used by query filter integrations before Bricks registers their provider classes.

Bricks maps each provider key to a class named `Bricks\Integrations\Query_Filters\Field_{Provider}` using `ucfirst( $provider )`. The default provider keys are `acf` and `metabox`.

## Parameters

- `$providers` (array): Provider keys registered for query filter custom field integration.

## Example usage

```php
add_filter( 'bricks/query_filters_cf_integration/register_providers', function( $providers ) {
    $providers[] = 'myprovider';

    return $providers;
} );
```
