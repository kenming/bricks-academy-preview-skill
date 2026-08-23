---
title: "Filter: bricks/element/maybe_set_aria_current_page"
description: "Filters the boolean value that determines whether to add the aria-current=\"page\" attribute to a link element. This is used to indicate that a link points to the."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-element-maybe_set_aria_current_page/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-element-maybe_set_aria_current_page.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the boolean value that determines whether to add the `aria-current="page"` attribute to a link element. This is used to indicate that a link points to the currently active page.

## Parameters

- `$set_aria_current` (*bool*): Whether the link matches the current page.
- `$url` (*string*): The URL of the link being checked.

## Example usage

```php
add_filter( 'bricks/element/maybe_set_aria_current_page', function( $set_aria_current, $url ) {
    // Example: Consider a link active if it matches a specific query parameter
    if ( isset( $_GET['section'] ) && strpos( $url, 'section=' . $_GET['section'] ) !== false ) {
        return true;
    }

    return $set_aria_current;
}, 10, 2 );
```
