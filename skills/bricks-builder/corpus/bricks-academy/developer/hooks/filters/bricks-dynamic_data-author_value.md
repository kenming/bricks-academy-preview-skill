---
title: "Filter: bricks/dynamic_data/author_value"
description: "Filters the value returned by {author...} dynamic data tags (e.g., {authorname}, {authoremail})."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-author_value/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-author_value.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the value returned by `{author_...}` dynamic data tags (e.g., `{author_name}`, `{author_email}`).

## Parameters

- `$value` (*string*): The value of the author field.
- `$field_type` (*string*): The specific author field being retrieved (e.g., `name`, `email`, `bio`, `website`, `avatar`).
- `$filters` (*array*): Array of modifiers applied to the tag (e.g., `['fallback' => '...']`).

## Example usage

```php
add_filter( 'bricks/dynamic_data/author_value', function( $value, $field_type, $filters ) {
    // Example: Append text to author bio
    if ( $field_type === 'bio' ) {
        return $value . ' [Verified Author]';
    }

    return $value;
}, 10, 3 );
```
