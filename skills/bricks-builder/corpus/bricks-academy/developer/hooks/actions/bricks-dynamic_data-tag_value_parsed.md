---
title: "Action: bricks/dynamic_data/tag_value_parsed"
description: "Runs after Bricks parses a dynamic data tag value."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-dynamic_data-tag_value_parsed/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-dynamic_data-tag_value_parsed.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Runs after Bricks parses a dynamic data tag value. This action is for observing or reacting to the parsed value; it does not change the returned value.

## Parameters

- `$value` (mixed): The parsed dynamic data value.
- `$tag` (string): The parsed tag name.
- `$original_tag` (string): The original dynamic data tag before parsing.
- `$args` (array): Parsed tag arguments.
- `$post` (WP_Post|int|null): The post context used while parsing.
- `$context` (string): The render context, such as text, link, or image.
- `$provider` (string|null): The provider that resolved the tag, when available.

## Example usage

```php
add_action( 'bricks/dynamic_data/tag_value_parsed', function( $value, $tag, $original_tag, $args, $post, $context, $provider ) {
    // Log or inspect parsed dynamic data values.
}, 10, 7 );
```
