---
title: "Filter: bricks/auth/custom_login_redirect"
description: "This filter allows customization of the redirect page ID for the login page."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-auth-custom_login_redirect/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-auth-custom_login_redirect.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
This filter allows customization of the redirect page ID for the login page.

## Example Usage:

```php
add_filter( 'bricks/auth/custom_login_redirect', function( $selected_login_page_id ) {
    return /* New login page ID */;
});
```

**Parameters:**

- `$selected_login_page_id` (int|false): The ID of the custom login page if set; otherwise, `false`.

**Return:**

- (int|false): The custom page ID for login redirection, or `false` if no custom page is designated.
