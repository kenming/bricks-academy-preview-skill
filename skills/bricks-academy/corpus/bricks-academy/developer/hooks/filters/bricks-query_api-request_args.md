---
title: "Filter: bricks/query_api/request_args"
description: "Filters the request arguments used by a Query API element."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_api-request_args/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_api-request_args.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the request arguments used by a Query API element before Bricks sends the request.

## Parameters

- `$args` (array): HTTP request arguments.
- `$element_id` (string): The Query API element ID.
- `$query_api` (object): The Query API integration instance.

## Example usage

```php
add_filter( 'bricks/query_api/request_args', function( $args, $element_id, $query_api ) {
    $args['timeout'] = 20;

    return $args;
}, 10, 3 );
```
