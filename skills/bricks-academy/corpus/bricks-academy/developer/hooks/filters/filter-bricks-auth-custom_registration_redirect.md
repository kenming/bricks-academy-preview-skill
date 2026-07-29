---
title: "Filter: bricks/auth/custom_registration_redirect"
description: "This filter allows for the customization of the redirect page ID for the registration page."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-auth-custom_registration_redirect/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-auth-custom_registration_redirect.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
This filter allows for the customization of the redirect page ID for the registration page.

## Example Usage:

```php
add_filter( 'bricks/auth/custom_registration_redirect', function( $selected_registration_page_id ) {
    return /* New registration page ID */;
});
```

**Parameters:**

- `$selected_registration_page_id` (int|false): The ID of the custom registration page if set; otherwise, `false`.

**Return:**

- (int|false): The custom page ID for registration redirection, or `false` if no custom page is set.
