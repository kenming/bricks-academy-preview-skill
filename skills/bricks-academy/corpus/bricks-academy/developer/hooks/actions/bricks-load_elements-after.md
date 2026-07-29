---
title: "Action: bricks/load_elements/after"
description: "Runs after Bricks loads element classes."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-load_elements-after/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-load_elements-after.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Runs after Bricks loads element classes. Use it to restore integration state after element labels, controls, or classes are initialized.

## Example usage

```php
add_action( 'bricks/load_elements/after', function() {
    // Restore state after Bricks loads element classes.
} );
```
