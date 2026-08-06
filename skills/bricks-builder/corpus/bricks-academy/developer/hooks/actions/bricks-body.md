---
title: "Action: bricks_body"
description: "Runs after the document head closes. Bricks uses it to print the opening body tag and body-start output."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-body/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-body.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Runs in `header.php` after the document head closes and before the site-wrapper and header hooks.

Bricks attaches its opening `<body>` tag callback to this hook at priority `1`. Default-priority callbacks run after the opening body tag and after Bricks has printed body-start scripts and skip links.

## Example usage

```php
add_action( 'bricks_body', function() {
    echo '<div id="body-integration-root"></div>';
} );
```
