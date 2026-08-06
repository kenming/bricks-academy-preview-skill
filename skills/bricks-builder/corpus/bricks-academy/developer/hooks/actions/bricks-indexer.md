---
title: "Action: bricks_indexer"
description: "Triggers the Bricks query filter indexer job runner."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-indexer/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-indexer.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Triggers the Bricks query filter indexer job runner. Bricks schedules this action with WP-Cron every five minutes and also triggers it from the background indexing AJAX endpoint.

The core indexer callback bails when the indexer is already running, then continues pending jobs until the queue is empty or server resource limits are reached.

## Example usage

```php
add_action( 'my_plugin_run_bricks_indexer', function() {
    do_action( 'bricks_indexer' );
} );
```
