---
title: "Filter: bricks/dynamic_data/text_separator"
description: "Filters the separator used when joining array values in a dynamic data tag (text context). The default separator is a comma and a space (, )."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-text_separator/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-text_separator.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the separator used when joining array values in a dynamic data tag (text context). The default separator is a comma and a space (`, `).

## Parameters

- `$sep` (*string*): The separator string.
- `$tag` (*string*): The dynamic data tag.
- `$post_id` (*int*): The ID of the post context.
- `$filters` (*array*): Array of modifiers applied to the tag.

## Example usage

```php
add_filter( 'bricks/dynamic_data/text_separator', function( $sep, $tag, $post_id, $filters ) {
    // Example: Use a line break separator for a specific custom field
    if ( $tag === 'my_repeater_field' ) {
        return '<br>';
    }

    return $sep;
}, 10, 4 );
```
