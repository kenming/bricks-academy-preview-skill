---
title: "Action: bricks/render_query_result/start"
description: "Runs at the start of the AJAX query result rendering process (queryresult endpoint - used for filters, live search, etc.). This action allows you to execute."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-render_query_result-start/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-render_query_result-start.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Runs at the start of the AJAX query result rendering process (`query_result` endpoint - used for filters, live search, etc.). This action allows you to execute custom logic before the query result content is generated.

## Parameters

- `$request_data` (*array*): The request data parameters (e.g., queryElementId, postId, filters, etc.).

## Example usage

```php
add_action( 'bricks/render_query_result/start', function( $request_data ) {
    // Access request data
    // $filters = $request_data['filters'] ?? [];
    
    // Example: Switch language for multilingual plugins
    // if ( isset( $request_data['lang'] ) ) {
    //     // Switch language logic
    // }
} );
```
