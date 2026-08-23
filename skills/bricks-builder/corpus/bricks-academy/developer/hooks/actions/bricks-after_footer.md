---
title: "Action: bricks_after_footer"
description: "Runs after Bricks renders the footer and before the site wrapper closes."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-after_footer/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-after_footer.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Runs after Bricks renders the footer and before the site wrapper closes. Use it when custom output needs to appear immediately after the footer template.

## Example usage

```php
add_action( 'bricks_after_footer', function() {
    echo '<div class="after-footer-note">Footer add-on output</div>';
} );
```
