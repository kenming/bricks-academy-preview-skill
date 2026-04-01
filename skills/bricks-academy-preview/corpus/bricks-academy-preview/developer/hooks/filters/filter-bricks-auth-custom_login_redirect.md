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
