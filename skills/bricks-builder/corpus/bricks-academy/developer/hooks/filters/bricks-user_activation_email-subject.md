---
title: "Filter: bricks/user_activation_email/subject"
description: "Filters the subject for Bricks user activation emails."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-user_activation_email-subject/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-user_activation_email-subject.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the subject for Bricks user activation emails.

## Parameters

- `$subject` (string): The email subject.
- `$user_id` (int): The user ID receiving the activation email.

## Example usage

```php
add_filter( 'bricks/user_activation_email/subject', function( $subject, $user_id ) {
    return '[Site access] Activate your account';
}, 10, 2 );
```
