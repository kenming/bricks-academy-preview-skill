Filters the query arguments used by `Templates::get_templates_query()` to retrieve Bricks templates. This allows you to customize which templates are fetched, for example, to support multilingual plugins or custom filtering.

## Parameters

- `$query_vars` (*array*): Array of arguments passed to `WP_Query`.

## Example usage

```php
add_filter( 'bricks/get_templates/query_vars', function( $query_vars ) {
    // Example: Exclude templates with a specific meta key
    $query_vars['meta_query'][] = [
        'key'     => 'my_exclude_key',
        'compare' => 'NOT EXISTS',
    ];

    return $query_vars;
} );
```
