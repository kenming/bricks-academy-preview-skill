---
title: "Action: bricks_after_site_wrapper"
description: "Runs in footer.php after the footer render action and before wp_footer(). Bricks uses it to close the builder wrapper."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-after_site_wrapper/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-after_site_wrapper.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Runs in `footer.php` after `bricks_after_footer` and before `wp_footer()`.

In the builder, Bricks uses this hook to close the `.brx-body` wrapper. On the frontend, Bricks also uses this position for one page navigation output when that page setting is enabled.

## Example usage

```php
add_action( 'bricks_after_site_wrapper', function() {
    echo '</div><!-- .before-site-wrapper -->';
} );
```
