---
title: "Filter: bricks/comments/author_tag"
description: "Filters the HTML tag used to wrap the comment author's name in the comments list."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-comments-author_tag/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-comments-author_tag.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the HTML tag used to wrap the comment author's name in the comments list.

## Parameters

- `$tag` (*string*): The HTML tag name. Defaults to `h5`.

## Example usage

```php
add_filter( 'bricks/comments/author_tag', function( $tag ) {
    // Change author name tag to 'span'
    return 'span';
} );
```
