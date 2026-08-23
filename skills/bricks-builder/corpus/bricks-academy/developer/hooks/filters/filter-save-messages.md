---
title: "Filter: bricks/builder/save_messages"
description: "Place and customize the following filter to display different save message every time you manually save your progress when editing with Bricks."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-save-messages/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-save-messages.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Place and customize the following filter to display different save message every time you manually save your progress when editing with Bricks.

```php
add_filter( 'bricks/builder/save_messages', function( $messages ) {
  // Option #1: Append individual save message to existing message collection
    $messages[] = 'Yasss';

  // Option #2: Replace all existing builder save messages
    $messages = [
      'Done',
      'Cool',
      'High five!',
    ];

  return $messages;
} );
```
