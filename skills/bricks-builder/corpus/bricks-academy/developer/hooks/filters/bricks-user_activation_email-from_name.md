---
title: "Filter: bricks/user_activation_email/from_name"
description: "Filters the sender name for Bricks user activation emails."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-user_activation_email-from_name/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-user_activation_email-from_name.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the sender name for Bricks user activation emails.

## Parameters

- `$from_name` (string): The email sender name.
- `$user_id` (int): The user ID receiving the activation email.

## Example usage

```php
add_filter( 'bricks/user_activation_email/from_name', function( $from_name, $user_id ) {
    return get_bloginfo( 'name' );
}, 10, 2 );
```
