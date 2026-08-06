---
title: "Filter: bricks/dynamic_data/render_content"
description: "Filter the content string that Bricks parses for dynamic data tags before those tags are resolved into output values."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-render_content/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-render_content.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the content passed through Bricks' dynamic data parser. Bricks attaches its own parser callback to this filter, so calling `apply_filters( 'bricks/dynamic_data/render_content', ... )` resolves dynamic tags such as `{post_title}` into their output values.

Use `add_filter()` on this hook when you need to adjust content before or after Bricks resolves dynamic data. Use `apply_filters()` when you need to parse a custom string through the same dynamic data pipeline.

## Parameters

- `$content` (*string*): The content string containing dynamic tags.
- `$post` (*WP_Post*): The post context.
- `$context` (*string*): The context where the content is used (e.g., `text`).

## Example usage

```php
$content = 'Hello {post_title}';
$post_id = 123;
$post    = get_post( $post_id );

// Manually parse dynamic data in a string
$parsed_content = apply_filters( 'bricks/dynamic_data/render_content', $content, $post, 'text' );

// Output: Hello My Post Title
echo $parsed_content;
```
