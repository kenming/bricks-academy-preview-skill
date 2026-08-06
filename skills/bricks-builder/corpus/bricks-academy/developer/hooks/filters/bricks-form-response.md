---
title: "Filter: bricks/form/response"
description: "Filters the JSON response sent to the browser after a Bricks form submission. This allows you to customize the success message, redirection URL, or add extra."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-form-response/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-form-response.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the JSON response sent to the browser after a Bricks form submission. This allows you to customize the success message, redirection URL, or add extra data to the response.

## Parameters

- `$response` (*array*): The response data array (e.g., `['type' => 'success', 'message' => '...', 'redirectUrl' => '...']`).
- `$form` (*object*): The Form integration instance.

## Example usage

```php
add_filter( 'bricks/form/response', function( $response, $form ) {
    // Example: Append a "Thank you" note to the success message
    if ( isset( $response['type'] ) && $response['type'] === 'success' ) {
        $response['message'] .= ' ' . esc_html__( 'Thank you for contacting us!', 'my-domain' );
    }

    return $response;
}, 10, 2 );
```
