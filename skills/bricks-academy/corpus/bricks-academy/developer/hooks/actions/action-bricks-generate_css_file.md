---
title: "Action: bricks/generate_css_file"
description: "If your CSS loading method is set to External files, this hook will be triggered when a CSS file is generated in Bricks. Developers can use this hook to trigger."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/action-bricks-generate_css_file/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/action-bricks-generate_css_file.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
If your CSS loading method is set to **External files**, this hook will be triggered when a CSS file is generated in Bricks. Developers can use this hook to trigger other actions related to CSS file generation. It's useful for instructing a cache plugin to clear the cache when a CSS file is generated. (`@since 1.9.5`)



```php
/**
  * $type : 'global-color-palettes' | 'global-elements' | 'theme-styles' | 'global-custom-css' | 'post'
  * $file_name : The generated CSS file name
*/
add_action( 'bricks/generate_css_file', function( $type, $file_name ) {
  error_log( 'Generated CSS file: ' . $type . ' - ' . $file_name );
}, 10, 2 );
```



**Parameters:**

- `$type` (string): Possible strings `global-color-palettes` `global-elements` `theme-styles` `global-custom-css` `post`
- `$file_name` (string): The generated CSS file name
