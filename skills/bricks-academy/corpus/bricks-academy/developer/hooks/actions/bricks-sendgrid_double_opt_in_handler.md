---
title: "Action: bricks_sendgrid_double_opt_in_handler"
description: "Runs before the SendGrid form action adds a new contact."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-sendgrid_double_opt_in_handler/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-sendgrid_double_opt_in_handler.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Runs before the SendGrid form action adds a new contact. Use it to trigger a custom double opt-in flow with the subscriber data Bricks collected.

## Parameters

- `$new_subscriber_data` (array): Subscriber data prepared for SendGrid, including the email address and optional first or last name.

## Example usage

```php
add_action( 'bricks_sendgrid_double_opt_in_handler', function( $new_subscriber_data ) {
    // Send a custom double opt-in email here.
}, 10, 1 );
```
