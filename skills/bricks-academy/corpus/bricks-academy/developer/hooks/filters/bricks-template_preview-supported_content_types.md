---
title: "Filter: bricks/template_preview/supported_content_types"
description: "Filters the list of content types available for selection in the \"Populate Content\" (Template Preview) setting. This allows you to add custom preview contexts."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-template_preview-supported_content_types/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-template_preview-supported_content_types.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the list of content types available for selection in the "Populate Content" (Template Preview) setting. This allows you to add custom preview contexts.

## Parameters

- `$types` (*array*): Associative array where keys are the content type IDs and values are their labels.

## Example usage

```php
add_filter( 'bricks/template_preview/supported_content_types', function( $types ) {
    // Example: Add a custom preview type
    $types['my_custom_preview'] = esc_html__( 'My Custom Preview', 'my-plugin' );

    return $types;
} );
```
