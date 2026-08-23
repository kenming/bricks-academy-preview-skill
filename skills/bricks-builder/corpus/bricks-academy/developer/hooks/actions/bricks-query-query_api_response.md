---
title: "Action: bricks/query/query_api_response"
description: "Runs after a Query API request is performed. This action allows you to inspect or process the response from the API query."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-query-query_api_response/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-query-query_api_response.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Runs after a Query API request is performed. This action allows you to inspect or process the response from the API query.

## Parameters

- `$response` (*array|WP_Error*): The response from the API request.
- `$element_id` (*string*): The element ID associated with the query.

## Example usage

```php
add_action( 'bricks/query/query_api_response', function( $response, $element_id ) {
    if ( is_wp_error( $response ) ) {
        error_log( 'Query API Error for element ' . $element_id . ': ' . $response->get_error_message() );
        return;
    }
    
    // Process successful response
    // $data = $response;
    // Do something with $data
}, 10, 2 );
```
