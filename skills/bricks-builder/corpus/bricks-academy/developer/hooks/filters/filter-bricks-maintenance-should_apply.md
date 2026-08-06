---
title: "Filter: bricks/maintenance/should_apply"
description: "Override whether Bricks maintenance mode or coming-soon mode should be applied for the current request."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-maintenance-should_apply/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-maintenance-should_apply.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Use this filter `(@since 2.0)` to override whether maintenance mode should be enforced for the current request.

By default, Bricks checks if the user is in the admin area or builder, if the current page is the login page, if the user can bypass maintenance, or if the current post is in the excluded list.

This filter runs *after* all of those checks have passed, giving you a final opportunity to apply custom logic before showing the maintenance or coming soon page.

## Parameters:

- `$apply_maintenance` (bool): Whether maintenance mode should apply. Defaults to `true` after all core checks pass.
- `$mode` (string): The current maintenance mode. Either `'maintenance'` or `'coming_soon'`.

## Return:

- `(bool)`: `true` to apply maintenance mode, `false` to bypass it.

## Example Usage:

In the following example, anyone with the correct `preview_key` in the URL (e.g. `https://domain.com?preview_key=letmein123`) will bypass maintenance mode. This is especially useful for sharing a live preview with clients or collaborators without requiring login access.

```php
add_filter( 'bricks/maintenance/should_apply', function( $apply_maintenance, $mode ) {
    $valid_key = 'letmein123';

    // Bypass maintenance mode if a valid preview key is present in the URL
    if ( isset( $_GET['preview_key'] ) && $_GET['preview_key'] === $valid_key ) {
        return false;
    }

    // Keep default behavior for all other cases
    return $apply_maintenance;
}, 10, 2 );
```

### Improved version with cookie persistence:

You can improve this behavior further by **persisting the preview access across page loads** using a cookie. Otherwise, the user would only bypass maintenance on the first page they visit (where the key is present in the URL), and get blocked again when navigating elsewhere.

```php
add_filter( 'bricks/maintenance/should_apply', function( $apply_maintenance, $mode ) {
    $valid_key   = 'letmein123';
    $cookie_name = 'bricks_preview_key';

    // Check preview key in URL
    if ( isset( $_GET['preview_key'] ) && $_GET['preview_key'] === $valid_key ) {
        // Set a cookie for 1 hour
        setcookie( $cookie_name, $valid_key, time() + HOUR_IN_SECONDS, COOKIEPATH, COOKIE_DOMAIN );
        return false;
    }

    // Check cookie on subsequent requests
    if ( isset( $_COOKIE[ $cookie_name ] ) && $_COOKIE[ $cookie_name ] === $valid_key ) {
        return false;
    }

    return $apply_maintenance;
}, 10, 2 );
```
