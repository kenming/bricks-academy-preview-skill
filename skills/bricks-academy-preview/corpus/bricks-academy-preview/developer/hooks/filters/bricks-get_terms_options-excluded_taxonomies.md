Filters the list of taxonomies excluded from term selection controls in the builder. This allows you to hide specific taxonomies (e.g., internal taxonomies) from the UI.

## Parameters

- `$excluded_taxonomies` (*array*): Array of taxonomy slugs to exclude. Defaults include `nav_menu`, `link_category`, `post_format`.

## Example usage

```php
add_filter( 'bricks/get_terms_options/excluded_taxonomies', function( $excluded_taxonomies ) {
    // Example: Exclude 'my_internal_taxonomy'
    $excluded_taxonomies[] = 'my_internal_taxonomy';

    return $excluded_taxonomies;
} );
```
