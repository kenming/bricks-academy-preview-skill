---
title: "Filter: bricks/form/tinymce_settings"
description: "Filters the TinyMCE configuration settings for \"Rich Text\" fields in Bricks forms. This allows you to customize the toolbar, menus, and other editor options."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-form-tinymce_settings/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-form-tinymce_settings.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the TinyMCE configuration settings for "Rich Text" fields in Bricks forms. This allows you to customize the toolbar, menus, and other editor options.

## Parameters

- `$settings` (*array*): Array of TinyMCE settings.

## Example usage

```php
add_filter( 'bricks/form/tinymce_settings', function( $settings ) {
    // Example: Disable the menubar
    $settings['menubar'] = false;

    // Example: Simplify the toolbar
    $settings['toolbar'] = 'bold italic underline | bullist numlist | link unlink';

    return $settings;
} );
```
