---
title: "Filter: bricks/code/disallow_keywords"
description: "This filter introduces another level of security when using the Code element to run code."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-code-disallow_keywords/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-code-disallow_keywords.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
This filter introduces another level of security when using the Code element to run code.

With the filter `bricks/code/disallow_keywords` you'll be able to prevent the code execution if specific keywords are found in the code, thus reducing the risk of using this element. To add keywords to this check, use the following example:

```php
add_filter( 'bricks/code/disallow_keywords', function( $keywords ) {
  $</meta>keywords[] = 'wpdb';

  return $</meta>keywords;
} );
```
