---
title: "Filter: bricks/dynamic_data/exclude_tags"
description: "Dynamic data tags are strings with a special syntax wrapped by curly brackets. Sometimes this syntax has conflicts with other plugins which cause a specific tag."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-dynamic_data-exclude_tags/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-dynamic_data-exclude_tags.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Dynamic data tags are strings with a special syntax wrapped by curly brackets. Sometimes this syntax has conflicts with other plugins which cause a specific tag to be removed by the content.

Since Bricks 1.3.5 it is possible to exclude a list of tags from the Bricks dynamic data logic using the following PHP snippet in your `functions.php` file:

```php
add_filter( 'bricks/dynamic_data/exclude_tags', function( $tags ) {
    return [
        'my_specific_tag',
        'my_other_specific_tag'
    ];
});
```

Adding this code to your child theme will prevent Bricks from replacing these tags with an empty string.
