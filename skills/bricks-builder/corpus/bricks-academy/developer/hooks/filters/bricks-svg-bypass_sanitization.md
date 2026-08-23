---
title: "Filter: bricks/svg/bypass_sanitization"
description: "Determines whether to bypass the SVG sanitization process when uploading SVG files. This can be useful if you need to upload SVGs with complex features (like."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-svg-bypass_sanitization/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-svg-bypass_sanitization.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Determines whether to bypass the SVG sanitization process when uploading SVG files. This can be useful if you need to upload SVGs with complex features (like animations or scripts) that the sanitizer would normally strip out, but it comes with security risks.

## Parameters

- `$bypass` (*bool*): Whether to bypass sanitization. Default is `false`.
- `$file` (*array*): Array containing file information (e.g., `tmp_name`, `type`).

## Example usage

```php
add_filter( 'bricks/svg/bypass_sanitization', function( $bypass, $file ) {
    // Example: Bypass sanitization for trusted users only
    if ( current_user_can( 'administrator' ) ) {
        return true;
    }

    return $bypass;
}, 10, 2 );
```
