---
title: "Filter: bricks/resolve_attachment_id"
description: "Filters an attachment ID before Bricks uses it for frontend output."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-resolve_attachment_id/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-resolve_attachment_id.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters an attachment ID before Bricks uses it for frontend output. This is useful for multilingual plugins or media integrations that need to resolve translated attachment IDs.

Bricks casts the filtered value with `absint()`. If the filtered value is empty or invalid, Bricks keeps the original attachment ID so image output does not break.

## Parameters

- `$attachment_id` (int): The attachment post ID Bricks is about to use.

## Example usage

```php
add_filter( 'bricks/resolve_attachment_id', function( $attachment_id ) {
    return $attachment_id;
} );
```
