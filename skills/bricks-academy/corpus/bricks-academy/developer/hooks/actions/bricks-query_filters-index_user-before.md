---
title: "Action: bricks/query_filters/index_user/before"
description: "Runs before a user is indexed for Query Filters. This action is triggered during the indexing process for a specific user."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-query_filters-index_user-before/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-query_filters-index_user-before.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Runs before a user is indexed for Query Filters. This action is triggered during the indexing process for a specific user.

## Parameters

- `$user_id` (*int*): The ID of the user being indexed.

## Example usage

```php
add_action( 'bricks/query_filters/index_user/before', function( $user_id ) {
    // Perform actions before indexing a user
    // error_log( "Starting indexing for user ID: $user_id" );
    
    // Maybe register custom dynamic data providers if needed for indexing
} );
```
