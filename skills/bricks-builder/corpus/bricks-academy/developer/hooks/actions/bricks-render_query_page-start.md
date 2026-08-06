---
title: "Action: bricks/render_query_page/start"
description: "Runs at the start of the AJAX query page rendering process (loadquerypage endpoint - used for infinite scroll/pagination). This action allows you to execute."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-render_query_page-start/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-render_query_page-start.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Runs at the start of the AJAX query page rendering process (`load_query_page` endpoint - used for infinite scroll/pagination). This action allows you to execute custom logic before the query page content is generated.

## Parameters

- `$request_data` (*array*): The request data parameters (e.g., queryElementId, postId, page, queryVars, etc.).

## Example usage

```php
add_action( 'bricks/render_query_page/start', function( $request_data ) {
    // Access request data
    // $page = $request_data['page'] ?? 1;
    
    // Example: Switch language for multilingual plugins
    // if ( isset( $request_data['lang'] ) ) {
    //     // Switch language logic
    // }
} );
```
