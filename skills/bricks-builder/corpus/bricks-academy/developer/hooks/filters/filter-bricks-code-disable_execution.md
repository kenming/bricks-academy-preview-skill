---
title: "Filter: bricks/code/disable_execution"
description: "This PHP filter allows you to disable code execution within the Bricks builder programmatically."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-code-disable_execution/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-code-disable_execution.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
This PHP filter allows you to disable code execution within the Bricks builder programmatically.

It takes precedence over the [`bricks/code/allow_execution`](/developer/hooks/filters/filter-bricks-code-allow_execution/) filter and any settings configured in `Bricks > Settings > Custom code > Code execution`.

```php
add_filter( 'bricks/code/disable_execution', function( $disable ) {
  // Returning true disables code execution programmatically
  return true;
} );
```

Use this filter to enforce stricter security by disabling code execution, regardless of other configurations on your site.
