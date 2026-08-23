---
title: "Filter: bricks/auth/custom_reset_password_redirect"
description: "This filter provides a way to change the redirect page ID for the reset password page."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-auth-custom_reset_password_redirect/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-auth-custom_reset_password_redirect.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
This filter provides a way to change the redirect page ID for the reset password page.

## Example Usage:

```php
add_filter( 'bricks/auth/custom_reset_password_redirect', function( $selected_reset_password_page_id ) {
    return /* New reset password page ID */;
});
```

**Parameters:**

- `$selected_reset_password_page_id` (int|false): The ID of the custom reset password page if set; otherwise, `false`.

**Return:**

- (int|false): The custom page ID for reset password redirection, or `false` if no custom page is specified.
