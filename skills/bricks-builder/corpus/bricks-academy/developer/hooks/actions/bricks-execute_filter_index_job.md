---
title: "Action: bricks_execute_filter_index_job"
description: "Runs before a query filter index job is executed."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-execute_filter_index_job/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-execute_filter_index_job.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Runs before a query filter index job is executed. Bricks uses this point so integrations can prepare context, such as switching language, before indexing starts.

## Parameters

- `$job` (array): The index job data that is about to be processed.

## Example usage

```php
add_action( 'bricks_execute_filter_index_job', function( $job ) {
    // Prepare integration context before this index job runs.
}, 10, 1 );
```
