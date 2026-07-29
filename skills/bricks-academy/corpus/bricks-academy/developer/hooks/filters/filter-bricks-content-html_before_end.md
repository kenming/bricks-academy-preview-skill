---
title: "Filter: bricks/content/html_before_end"
description: "Available since version 1.6, this filter allows you to customize or insert HTML strings before closing main tag."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-content-html_before_end/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-content-html_before_end.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Available since version 1.6, this filter allows you to customize or insert HTML strings before closing `main` tag.

```php
add_filter( 'bricks/content/html_before_end', function( $html_after_begin, $bricks_data, $attributes, $tag ) {

    if ( $tag !== 'main' ) {
      return $html_after_begin;
    }

    // Insert custom popup HTML
    $my_popup_html = '<div class="my_popup">This is my popup</div>';

    return $html_after_begin . $my_popup_html;
}, 10, 4 );
```
