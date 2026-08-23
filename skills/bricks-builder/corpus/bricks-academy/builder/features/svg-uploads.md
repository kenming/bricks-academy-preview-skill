---
title: "SVG Uploads"
description: "Enable SVG uploads in Bricks, understand the security tradeoffs, and manage SVG assets inside the builder workflow."
canonical: "https://academy.bricksbuilder.io/builder/features/svg-uploads/"
markdownUrl: "https://academy.bricksbuilder.io/builder/features/svg-uploads.md"
pageType: "article"
section: "builder"
category: "features"
lastmod: "2026-08-20T13:12:40.000Z"
---
WordPress does not allow SVG file uploads by default because SVG is an XML-based image format that can contain malicious code. SVG files are especially risky when they come from unknown sources or are uploaded by untrusted users.

## How to enable SVG support

You can enable SVG uploads by user role under **Bricks > Settings > General > SVG uploads**.

Bricks only lists roles that can edit posts. When a role is enabled, Bricks grants that role the `bricks_upload_svg` capability and adds `svg` and `svgz` to the allowed upload MIME types for users with that capability.

You can also override SVG upload access for an individual user from the user's WordPress profile. An individual user setting can enable or disable SVG uploads separately from the user's role default.

Once SVG uploads are enabled for a user, Bricks tries to sanitize uploaded SVG files during the WordPress upload process.

:::note
No built-in SVG sanitizer can guarantee that every malicious SVG will be made safe. Upload SVG files only from trusted sources, and enable SVG uploads only for users you trust.
:::

## What Bricks sanitizes

Bricks sanitizes uploaded files whose upload type is `image/svg+xml`.

During upload, Bricks:

- Allows `.svg` and `.svgz` uploads for users with SVG upload capability.
- Runs SVG uploads through the `enshrined/svg-sanitize` sanitizer library.
- Minifies the sanitized SVG output.
- Detects gzipped SVG content, decodes it for sanitization, and re-encodes it afterward.
- Blocks the upload with an error message if sanitization fails.
- Removes the forced 1px image dimensions WordPress can assign to SVG attachments.

SVG media uploads are different from the **SVG element > Source: Code** workflow. Pasted SVG source code in the SVG element is treated as executable Bricks code, requires code execution capability, and requires a valid code signature.

## Bypass sanitization {#bypass-sanitization}

Although it is wise to sanitize SVG files uploaded to WordPress, there may be situations where you want to bypass the Bricks SVG sanitizer because another trusted process handles sanitization.

To bypass Bricks SVG sanitization, use the `bricks/svg/bypass_sanitization` filter:

```php
add_filter( 'bricks/svg/bypass_sanitization', function( $bypass, $file ) {
  // Perform your own checks before bypassing Bricks sanitization.

  return $bypass;
}, 10, 2 );
```

Filter callback parameters:

- `$bypass` is a boolean. Return `true` to bypass Bricks sanitization.
- `$file` is the uploaded file array from `$_FILES`.

To bypass Bricks SVG sanitization for every SVG upload:

```php
add_filter( 'bricks/svg/bypass_sanitization', '__return_true' );
```

Only bypass sanitization when you fully control the SVG source or run another trusted sanitizer before the file is stored.

## Sanitizer allowed tags and attributes {#allowed-tags-attributes}

The sanitizer uses the default allowed tags and attributes from the `enshrined/svg-sanitize` library. In some edge cases, you may need to allow additional SVG tags or attributes. In high-security environments, you may want to narrow the allowed lists.

Bricks exposes two filters:

```php
add_filter( 'bricks/svg/allowed_tags', function( $tags ) {
    $tags[] = 'filter'; // Allow the "filter" tag.

    return $tags;
} );
```

```php
add_filter( 'bricks/svg/allowed_attributes', function( $attributes ) {
    $attributes[] = 'filterUnits'; // Allow the "filterUnits" attribute.

    return $attributes;
} );
```

Use these filters carefully. Allowing extra SVG tags or attributes can reintroduce security risk, especially for attributes that can reference external resources or execute script-like behavior.

## Security checklist

Before enabling SVG uploads:

- Enable SVG uploads only for trusted roles or trusted individual users.
- Upload SVG files only from trusted sources.
- Keep sanitization enabled unless you have another trusted sanitizer in place.
- Review any custom allowed tags or attributes.
- Do not treat media-upload SVG sanitization as protection for SVG element source code; SVG element source code uses the code execution and code signature security model.
