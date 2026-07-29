---
title: "Action: bricks_before_header"
description: "Runs before Bricks renders the header template."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-before_header/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-before_header.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Runs before Bricks renders the header template. Use it to output markup or run logic immediately before header rendering.

## Example usage

```php
add_action( 'bricks_before_header', function() {
    echo '<div class="top-strip">Free shipping this week</div>';
} );
```
