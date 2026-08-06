---
title: "Filter: bricks/content/tag"
description: "Filter which HTML tag Bricks uses for the #brx-content wrapper around rendered page content."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-content-tag/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-content-tag.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
The `bricks/content/tag` (@since 1.11.1) filter lets you set the HTML tag for the `#brx-content` node that your Bricks content data is wrapped in.

Make sure the HTML tag you return is an [allowed HTML tag](/developer/hooks/filters/filter-bricks-allowed_html_tags/).

## Example Usage:

```php
add_filter( 'bricks/content/tag', function( $tag ) {
    // Set #brx-content tag to 'div' (default: main)
    return 'div';
} );
```

**Parameters:**

- `$tag` (string): The default HTML tag, which is `main`.

**Return:**

- (string): The HTML tag you want to render instead of the default.
