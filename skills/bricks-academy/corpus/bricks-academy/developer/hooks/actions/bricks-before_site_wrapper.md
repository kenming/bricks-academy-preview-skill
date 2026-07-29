---
title: "Action: bricks_before_site_wrapper"
description: "Runs in header.php before the header render action. Bricks uses it to open the builder wrapper."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-before_site_wrapper/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-before_site_wrapper.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Runs in `header.php` after `bricks_body` and before `bricks_before_header`.

In the builder, Bricks uses this hook to open the `.brx-body` wrapper around the builder frame. On the frontend, it is a general position before the header render flow.

## Example usage

```php
add_action( 'bricks_before_site_wrapper', function() {
    echo '<div class="before-site-wrapper">';
} );
```
