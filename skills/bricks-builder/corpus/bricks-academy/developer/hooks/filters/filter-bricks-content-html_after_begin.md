---
title: "Filter: bricks/content/html_after_begin"
description: "Available since version 1.6, this filter allows you to customize or insert HTML strings after main tag, before rendering bricks data."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-content-html_after_begin/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-content-html_after_begin.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Available since version 1.6, this filter allows you to customize or insert HTML strings after `main` tag, before rendering bricks data.

```php
add_filter( 'bricks/content/html_after_begin', function( $html_after_begin, $bricks_data, $attributes, $tag ) {

    if ( $tag !== 'main' ) {
      return $html_after_begin;
    }

    // Insert custom div after the main tag
    $my_additional_html = '<div class="my_notification">This is my notification</div>';

    return $html_after_begin . $my_additional_html;
}, 10, 4 );
```
