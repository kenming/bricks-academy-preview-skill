---
title: "Action: bricks_after_header"
description: "Runs after Bricks renders the header template."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-after_header/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-after_header.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Runs after Bricks renders the header template. Use it for output or setup that should happen directly after the site header.

## Example usage

```php
add_action( 'bricks_after_header', function() {
    echo '<div class="after-header-banner">Announcement</div>';
} );
```
