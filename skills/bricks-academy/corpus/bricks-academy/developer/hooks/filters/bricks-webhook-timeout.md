---
title: "Filter: bricks/webhook/timeout"
description: "Allows you to modify the timeout duration (in seconds) for webhook requests triggered by the Form element."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-webhook-timeout/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-webhook-timeout.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Allows you to modify the timeout duration (in seconds) for webhook requests triggered by the Form element.

## Parameters

- `$timeout` (int): The timeout duration in seconds. Default is `15`.

## Example usage

```php
add_filter( 'bricks/webhook/timeout', function( $timeout ) {
    // Increase timeout to 30 seconds
    return 30;
} );
```
