---
title: "Filter: bricks/user_activation_email/content"
description: "Filters the content for Bricks user activation emails."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-user_activation_email-content/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-user_activation_email-content.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the content for Bricks user activation emails.

## Parameters

- `$content` (string): The email content.
- `$user_id` (int): The user ID receiving the activation email.

## Example usage

```php
add_filter( 'bricks/user_activation_email/content', function( $content, $user_id ) {
    return $content;
}, 10, 2 );
```
