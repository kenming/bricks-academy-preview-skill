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
