---
title: "Filter: bricks/dynamic_data/do_action_context"
description: "Filters the action context used by the dynamic data do_action tag."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-do_action_context/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-do_action_context.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the action context used when Bricks resolves a dynamic data `{do_action}` tag. Use it to change the action name, pass arguments, or skip execution.

## Parameters

- `$action_context` (array): Action context with action, args, requested_action, and skip keys.
- `$filters` (array): Dynamic data filters parsed from the tag.
- `$context` (string): The dynamic data render context.
- `$post` (WP_Post|int|null): The current post context.

## Example usage

```php
add_filter( 'bricks/dynamic_data/do_action_context', function( $action_context, $filters, $context, $post ) {
    if ( $action_context['requested_action'] === 'my_public_alias' ) {
        $action_context['action'] = 'my_private_action';
        $action_context['args']   = [ get_the_ID() ];
    }

    return $action_context;
}, 10, 4 );
```
