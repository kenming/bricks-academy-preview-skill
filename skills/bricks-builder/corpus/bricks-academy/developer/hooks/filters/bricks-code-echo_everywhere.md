---
title: "Filter: bricks/code/echo_everywhere"
description: "Determines whether the {echo:} dynamic data tag should be parsed recursively if it appears within the output of another dynamic data tag. By default, this is."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-code-echo_everywhere/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-code-echo_everywhere.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Determines whether the `{echo:}` dynamic data tag should be parsed recursively if it appears within the output of another dynamic data tag. By default, this is disabled for security and performance reasons.

## Parameters

- `$echo_everywhere` (*bool*): Whether to allow recursive parsing of `{echo:}` tags. Default is `false`.

## Example usage

```php
add_filter( 'bricks/code/echo_everywhere', function( $echo_everywhere ) {
    // Enable recursive parsing of {echo:} tags
    // WARNING: Use with caution as this may lead to infinite loops or security vulnerabilities
    return true;
} );
```
