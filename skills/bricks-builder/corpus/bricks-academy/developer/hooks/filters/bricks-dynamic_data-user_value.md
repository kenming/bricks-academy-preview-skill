---
title: "Filter: bricks/dynamic_data/user_value"
description: "Filters the value returned by {wpuser...} dynamic data tags (e.g., {wpuseremail}, {wpuserrole})."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-user_value/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-user_value.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the value returned by `{wp_user_...}` dynamic data tags (e.g., `{wp_user_email}`, `{wp_user_role}`).

## Parameters

- `$value` (*mixed*): The value of the user field.
- `$field_type` (*string*): The specific user field being retrieved (e.g., `email`, `login`, `first_name`, `last_name`, `bio`, `picture`, `role`, `registered_date`).
- `$filters` (*array*): Array of modifiers applied to the tag.

## Example usage

```php
add_filter( 'bricks/dynamic_data/user_value', function( $value, $field_type, $filters ) {
    // Example: Capitalize the user role
    if ( $field_type === 'role' && is_string( $value ) ) {
        return ucfirst( $value );
    }

    return $value;
}, 10, 3 );
```
