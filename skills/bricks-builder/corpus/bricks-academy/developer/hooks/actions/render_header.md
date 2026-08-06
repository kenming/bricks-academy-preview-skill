---
title: "Action: render_header"
description: "Runs at the header render position. Bricks attaches its default header renderer to this action."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/render_header/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/render_header.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Runs in `header.php` between `bricks_before_header` and `bricks_after_header`.

Bricks attaches its frontend header renderer to this action by default. Use this hook only when you need to add low-level output at the header render position. To modify the generated header HTML, use the `bricks/render_header` filter instead.

## Example usage

```php
add_action( 'render_header', function() {
    echo '<div class="after-render-header"></div>';
}, 20 );
```
