---
title: "Action: bricks_meta_tags"
description: "Runs in the document head before wp_head()."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-meta_tags/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-meta_tags.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Runs in the document head before `wp_head()`. Use it to output meta tags that should be controlled through the Bricks header template flow.

## Example usage

```php
add_action( 'bricks_meta_tags', function() {
    echo '<meta name="theme-color" content="#111111">';
} );
```
