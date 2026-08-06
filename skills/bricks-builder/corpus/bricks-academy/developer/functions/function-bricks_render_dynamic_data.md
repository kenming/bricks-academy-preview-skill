---
title: "Function: bricks_render_dynamic_data"
description: "Use the bricks_render_dynamic_data() helper to resolve dynamic tags inside a content string in your own custom code."
canonical: "https://academy.bricksbuilder.io/developer/functions/function-bricks_render_dynamic_data/"
markdownUrl: "https://academy.bricksbuilder.io/developer/functions/function-bricks_render_dynamic_data.md"
pageType: "article"
section: "developer"
category: "functions"
lastmod: "2026-08-04T12:13:33.000Z"
---
This helper function will render the dynamic data tags inside of a content string (@since 1.5.5).

```php
echo bricks_render_dynamic_data( $content, $post_id, $context );
```

### Parameters:

- `$content` - a string containing dynamic data tags (required)
- `$post_id` - the post id if needed (default: current post id)
- `$context` - the context where the data is used after rendered: *text*, *link*, *image*, *media* (default: *text*)

### Return:

The string after replacing the dynamic data tags with their content.

Example:

```php
echo bricks_render_dynamic_data('My Post Title: {post_title}');
```
