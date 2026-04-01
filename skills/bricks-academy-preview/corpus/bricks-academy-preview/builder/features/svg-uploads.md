WordPress, by default, does not allow SVG file uploads as this XML-based file format can contain malicious code. It can be especially dangerous when downloaded from unknown/untrusted sources or by untrusted users.

## How to enable SVG support

You can enable SVG uploads on a user role basis under **Bricks > Settings > SVG Uploads** (tab: General). Once enabled Bricks will try to sanitize any SVG file uploads.

:::note
It is important to note that no built-in SVG sanitizer has a 100% guarantee to remove all malicious code. You should therefore download SVG files only from trusted sources, and only enable SVG uploads for user roles that you trust to follow this rule.
:::

## Bypass sanitization {#bypass-sanitization}

Although it is wise to sanitize all the SVG files uploaded to WordPress, there could be a situation where you don't want to rely on the Bricks SVG sanitizer. To bypass the sanitization logic, Bricks provides the hook `bricks/svg/bypass_sanitization`, and you could use it like so:

```php
add_filter( 'bricks/svg/bypass_sanitization', function( $bypass, $file ) {
  // Perform some logic to decide to bypass or not the sanitization

  return $bypass;
}, 10, 2 );
```

Filter callback parameters:

- `$bypass` is a boolean variable (`true` = bypass)
- `$file` represents a single element of the $\_FILES array

If you just want to bypass the sanitization without conditions you could use this shorthand approach:

```php
add_filter( 'bricks/svg/bypass_sanitization', '__return_true' );
```

## Sanitizer allowed tags and attributes {#allowed-tags-attributes}

The sanitizer uses a predefined list of allowed tags and attributes. In some edge cases you would like to upload SVG files that contain other tags and attributes and therefore you need to include them in the allowed list. Or, you may want to narrow the allowed tags and attributes for high security reasons. To manage these lists, Bricks has two different filters:

```php
add_filter( 'bricks/svg/allowed_tags', function( $tags ) {
    $tags[] = 'filter'; // Allow the "filter" tag

    return $tags;
} );
```

```php
add_filter( 'bricks/svg/allowed_attributes', function( $attributes ) {
    $attributes[] = 'filterUnits'; // Allow the "filterUnits" attribute

    return $attributes;
} );
```
