---
title: "Filter: bricks/auth/custom_lost_password_redirect"
description: "This filter enables the modification of the redirect page ID for the lost password page."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-auth-custom_lost_password_redirect/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-auth-custom_lost_password_redirect.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
This filter enables the modification of the redirect page ID for the lost password page.

## Example Usage:

```php
add_filter( 'bricks/auth/custom_lost_password_redirect', function( $selected_lost_password_page_id ) {
    return /* New lost password page ID */;
});
```

**Parameters:**

- `$selected_lost_password_page_id` (int|false): The ID of the custom lost password page if set, otherwise `false`.

**Return:**

- (int|false): The new custom lost password page ID or `false` to indicate no custom page is set.
