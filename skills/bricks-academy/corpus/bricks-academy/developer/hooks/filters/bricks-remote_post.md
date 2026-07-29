---
title: "Filter: bricks/remote_post"
description: "Filters the arguments passed to wpremotepost() when Bricks performs a remote POST request (e.g., verifying license, submitting form data to webhook)."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-remote_post/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-remote_post.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the arguments passed to `wp_remote_post()` when Bricks performs a remote POST request (e.g., verifying license, submitting form data to webhook).

## Parameters

- `$args` (*array*): Array of arguments for `wp_remote_post()` (e.g., `body`, `timeout`, `sslverify`).
- `$url` (*string*): The URL being requested.

## Example usage

```php
add_filter( 'bricks/remote_post', function( $args, $url ) {
    // Example: Add custom headers to webhook requests
    if ( strpos( $url, 'webhook.example.com' ) !== false ) {
        $args['headers']['X-Custom-Header'] = 'my-value';
    }

    return $args;
}, 10, 2 );
```
