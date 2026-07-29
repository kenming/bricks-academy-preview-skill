---
title: "Filter: bricks/code/allow_execution"
description: "An alternative to the Disable code execution setting under Bricks > Settings > Builder Access. You can use this PHP filter to disable/enable code execution."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-code-allow_execution/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-code-allow_execution.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
An alternative to the **Disable code execution** setting under `Bricks > Settings > Builder Access`. You can use this PHP filter to disable/enable code execution programmatically.

![](imgs/disallow-code-execution-hook-26717915d0.png)

```php
add_filter( 'bricks/code/allow_execution', function( $allow ) {
  // Only allows to return false to disable code execution programmatically
  return false;
} );
```
