---
title: "Filter: bricks/query/no_results_content"
description: "You can programmatically change the query loop \"no results content\" using this filter."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-no_results_content/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-no_results_content.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
You can programmatically change the query loop "no results content" using this filter.

```php
add_filter( 'bricks/query/no_results_content', function( $content, $settings, $element_id ) {

  // Check if the query element id is the one you want
  if( $element_id !== 'srixvr' ) return $content;

  // Use a bricks section template as the no results content
  $content = do_shortcode('[bricks_template id="3981"]');

  return $content;
}, 10, 3 );
```
