---
title: "Filter: bricks/polylang/builder_ajax_params"
description: "Filters the Polylang AJAX parameters injected into builder media requests."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-polylang-builder_ajax_params/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-polylang-builder_ajax_params.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the Polylang AJAX parameters injected into builder media requests. Use it to add or adjust language-aware parameters for the media library in the builder.

## Parameters

- `$params` (array): Parameters added to media AJAX requests.
- `$post_id` (int): The current builder post ID.

## Example usage

```php
add_filter( 'bricks/polylang/builder_ajax_params', function( $params, $post_id ) {
    $params['lang'] = pll_current_language();

    return $params;
}, 10, 2 );
```
