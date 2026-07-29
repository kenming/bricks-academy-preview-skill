---
title: "Action: bricks/load_elements/before"
description: "Runs before Bricks loads element classes."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-load_elements-before/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-load_elements-before.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Runs before Bricks loads element classes. Use it to prepare integration state before element labels, controls, or classes are initialized.

## Example usage

```php
add_action( 'bricks/load_elements/before', function() {
    // Prepare state before Bricks loads element classes.
} );
```
