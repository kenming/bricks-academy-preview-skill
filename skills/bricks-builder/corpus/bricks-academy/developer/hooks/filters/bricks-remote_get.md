---
title: "Filter: bricks/remote_get"
description: "Filters the arguments passed to wpremoteget() when Bricks performs a remote GET request (e.g., fetching templates, community library)."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-remote_get/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-remote_get.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the arguments passed to `wp_remote_get()` when Bricks performs a remote GET request (e.g., fetching templates, community library).

## Parameters

- `$args` (*array*): Array of arguments for `wp_remote_get()` (e.g., `timeout`, `sslverify`).
- `$url` (*string*): The URL being requested.

## Example usage

```php
add_filter( 'bricks/remote_get', function( $args, $url ) {
    // Example: Increase timeout for specific API requests
    if ( strpos( $url, 'api.example.com' ) !== false ) {
        $args['timeout'] = 60;
    }

    return $args;
}, 10, 2 );
```
