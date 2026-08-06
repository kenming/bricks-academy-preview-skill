---
title: "Filter: bricks/password_protection/cookie_expires"
description: "Adjust the expiration time for the password cookie used by the password protection template. By default, when a password is set in the template settings, the."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-password_protection-cookie-expires/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-password_protection-cookie-expires.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Adjust the expiration time for the password cookie used by [the password protection template](/builder/features/password-protection/). By default, when a password is set in the template settings, the cookie expires after **10 days**. This filter allows you to customize how long the cookie remains valid.

## Example Usage:

```php
add_filter( 'bricks/password_protection/cookie_expires', function( $expire ) {
    // Set cookie expiration to 1 hour (3600 seconds)
    return time() + 3600;
} );
```

In this example, the password cookie will expire after 1 hour, requiring users to re-enter the password if they revisit the page after that time.

**Parameters:**

- `$expire` (int): The default expiration timestamp for the password cookie, which is set to **10 days**.

**Return:**

- (int): The Unix timestamp for when the cookie should expire.
