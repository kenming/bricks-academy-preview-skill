---
title: "Action: bricks/dynamic_data/before_do_action"
description: "Runs before the dynamic data {doaction:myhook} tag is processed. This allows you to execute code before a specific doaction tag is rendered."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-dynamic_data-before_do_action/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-dynamic_data-before_do_action.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Runs before the dynamic data `{do_action:my_hook}` tag is processed. This allows you to execute code before a specific `do_action` tag is rendered.

## Parameters

- `$action` (_string_): The action name specified in the tag (e.g. `my_hook` in `{do_action:my_hook}`).
- `$filters` (_array_): Array of filters applied to the tag.
- `$context` (_string_): The context in which the tag is being rendered (e.g., 'text').
- `$post` (_WP_Post|null_): The current post object, or null.

## Example usage

```php
add_action( 'bricks/dynamic_data/before_do_action', function( $action, $filters, $context, $post ) {
    if ( $action === 'my_custom_hook' ) {
        // Code to run before 'my_custom_hook' is processed via dynamic data
        error_log( 'Starting processing my_custom_hook' );
    }
}, 10, 4 );
```
