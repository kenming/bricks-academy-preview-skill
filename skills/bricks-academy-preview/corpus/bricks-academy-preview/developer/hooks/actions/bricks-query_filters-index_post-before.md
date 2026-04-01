Runs before a post is indexed for Query Filters. This action is triggered during the indexing process for a specific post.

## Parameters

- `$post_id` (*int*): The ID of the post being indexed.

## Example usage

```php
add_action( 'bricks/query_filters/index_post/before', function( $post_id ) {
    // Perform actions before indexing a post, e.g., logging or checking conditions
    // error_log( "Starting indexing for post ID: $post_id" );
    
    // Maybe register custom dynamic data providers if needed for indexing
} );
```
