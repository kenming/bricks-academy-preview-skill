---
title: "Filter: bricks/breadcrumbs/home_label"
description: "Filters the label text used for the \"Home\" link in the Breadcrumbs element."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-breadcrumbs-home_label/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-breadcrumbs-home_label.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the label text used for the "Home" link in the Breadcrumbs element.

## Parameters

- `$home_label` (*string*): The home label text (may include HTML if an icon is used).

## Example usage

```php
add_filter( 'bricks/breadcrumbs/home_label', function( $home_label ) {
    return 'Start';
} );
```
