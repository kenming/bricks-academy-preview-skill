---
title: "Filter: bricks/dynamic_data/read_more"
description: "If you use the dynamic data tag {readmore} you'll get an anchor tag (link) to the post with the label \"Read more\" by default. To change this label use the."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-dynamic_data-read_more/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-dynamic_data-read_more.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
If you use the dynamic data tag `{read_more}` you'll get an anchor tag (link) to the post with the label "Read more" by default. To change this label use the following code:

```php
add_filter( 'bricks/dynamic_data/read_more', function( $label, $post ) {
   return 'My New Label';
}, 10, 2 );
```

Read more about [Dynamic Data](/builder/dynamic-content/dynamic-data/) in the Bricks academy.
