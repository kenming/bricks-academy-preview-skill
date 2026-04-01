This filter is distinct from other authentication-related filters in that it provides a broad scope for customizing redirections during authentication processes. Unlike specific filters for [login](/developer/hooks/filters/filter-bricks-auth-custom_login_redirect/), [registration](/developer/hooks/filters/filter-bricks-auth-custom_registration_redirect/), [lost password](/developer/hooks/filters/filter-bricks-auth-custom_lost_password_redirect/), or [reset password pages](/developer/hooks/filters/filter-bricks-auth-custom_reset_password_redirect/), this filter applies to any authentication-related URL.

**Functionality:**

This filter allows overriding the default redirect URL based on custom conditions across various authentication scenarios. It offers flexibility to redirect users to different pages depending on the context or specific requirements of the authentication process.

## Example Usage:

```php
add_filter( 'bricks/auth/custom_redirect_url', function( $custom_redirect_url, $current_url_path ) {
    if ( /* custom condition based on $current_url_path */ ) {
        return 'https://example.com/custom-redirect';
    }
    return $custom_redirect_url;
}, 10, 2 );
```

In this example, the redirection URL changes based on the current URL path, allowing for a dynamic and contextual redirection strategy.

**Parameters:**

- `$custom_redirect_url` (string|null): The initial redirect URL.
- `$current_url_path` (string): The current URL path being accessed.

**Return:**

- (string|null): The URL to redirect to, or null to follow default logic.
