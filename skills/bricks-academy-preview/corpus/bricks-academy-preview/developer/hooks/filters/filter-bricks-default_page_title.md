Since 1.8, Bricks automatically adds default page titles to all non-Bricks pages. However, if you wish to customize or remove this default page title, you can utilize this filter.

Returning an empty string, disables the default page title.

```php
add_filter( 'bricks/default_page_title', function( $title, $post_id ) {
  // If slug of current page is 'my-page': Return empty page title
  if ( is_page( 'my-page' ) ) {
    $title = '';
  }

  return $title;
}, 10, 2 );
```
