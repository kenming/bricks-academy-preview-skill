---
title: "Filter: bricks/dynamic_data/format_value"
description: "Filters the final processed value of any dynamic data tag before it is rendered. This is a powerful filter that runs for every dynamic tag, allowing you to."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-format_value/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-format_value.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the final processed value of any dynamic data tag before it is rendered. This is a powerful filter that runs for every dynamic tag, allowing you to globally modify outputs based on context or tag name.

## Parameters

- `$value` (*mixed*): The processed value of the dynamic tag.
- `$tag` (*string*): The dynamic data tag (e.g., `post_title`, `my_custom_tag`).
- `$post_id` (*int*): The ID of the post context.
- `$filters` (*array*): Array of modifiers/arguments applied to the tag (e.g., `['fallback' => '...']`).
- `$context` (*string*): The context where the tag is being rendered (e.g., `text`, `link`, `image`, `video`, `object`, `media`).

## Example usage

```php
add_filter( 'bricks/dynamic_data/format_value', function( $value, $tag, $post_id, $filters, $context ) {
    // Example: Add a suffix to the post title when used in text context
    if ( $tag === 'post_title' && $context === 'text' ) {
        return $value . ' | My Site';
    }

    return $value;
}, 10, 5 );
```
