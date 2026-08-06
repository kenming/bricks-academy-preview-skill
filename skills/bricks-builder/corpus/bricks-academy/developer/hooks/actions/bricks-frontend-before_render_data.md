---
title: "Action: bricks/frontend/before_render_data"
description: "Runs before the Bricks\\Frontend::renderdata method starts generating the HTML for a set of elements. This action is undocumented in the official docs but useful."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-frontend-before_render_data/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-frontend-before_render_data.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Runs before the `Bricks\Frontend::render_data` method starts generating the HTML for a set of elements. This action is undocumented in the official docs but useful for removing plugin actions/filters that might interfere with Bricks rendering.

## Parameters

- `$elements` (*array*): The array of elements to be rendered.
- `$area` (*string*): The area being rendered (e.g., 'content', 'header', 'footer').

## Example usage

```php
add_action( 'bricks/frontend/before_render_data', function( $elements, $area ) {
    // Remove actions/filters that interfere with Bricks rendering
    // remove_filter( 'the_content', 'my_plugin_content_filter' );
    
    // Example: Log render start
    // error_log( "Starting rendering area: $area" );
} );
```
