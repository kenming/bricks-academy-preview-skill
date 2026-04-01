Filters the arguments passed to the WordPress `paginate_links()` function when generating pagination output. This allows you to customize the pagination structure, text labels, and other settings.

## Parameters

- `$args` (*array*): Array of arguments for `paginate_links()`.

## Example usage

```php
add_filter( 'bricks/paginate_links_args', function( $args ) {
    // Example: Change the "Previous" and "Next" text
    $args['prev_text'] = 'Previous';
    $args['next_text'] = 'Next';

    // Example: Change the number of adjacent page links shown
    $args['mid_size'] = 3;

    return $args;
} );
```
