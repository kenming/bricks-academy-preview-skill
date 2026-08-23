---
title: "Action: render_footer"
description: "Runs at the footer render position. Bricks attaches its default footer renderer to this action."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/render_footer/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/render_footer.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Runs in `footer.php` between `bricks_before_footer` and `bricks_after_footer`.

Bricks attaches its frontend footer renderer to this action by default. Use this hook only when you need to add low-level output at the footer render position. To modify the generated footer HTML, use the `bricks/render_footer` filter instead.

## Example usage

```php
add_action( 'render_footer', function() {
    echo '<div class="after-render-footer"></div>';
}, 20 );
```
