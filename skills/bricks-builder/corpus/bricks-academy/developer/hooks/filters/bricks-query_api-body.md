---
title: "Filter: bricks/query_api/body"
description: "Filters the body used by a Query API element request."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_api-body/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_api-body.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the body data used by a Query API element request before Bricks adds it to the HTTP request.

Bricks only builds a body for request methods that support one in the Query API implementation, currently `POST`.

## Parameters

- `$body_data` (string|array|null): The request body data Bricks has built.
- `$element_id` (string): The Query API element ID.
- `$query_api` (object): The Query API integration instance.

## Example usage

```php
add_filter( 'bricks/query_api/body', function( $body_data, $element_id, $query_api ) {
    return $body_data;
}, 10, 3 );
```
