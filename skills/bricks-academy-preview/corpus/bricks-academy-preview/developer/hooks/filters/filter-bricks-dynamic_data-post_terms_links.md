When rendering the terms assigned to a post using the dynamic data tag `{post_terms_my_taxonomy}`, Bricks wraps each term with a link to the term archive page. To disable this default behavior, you may hook into the `bricks/dynamic_data/post_terms_links` filter, like so:

```php
// Disable links for all the {post_terms_my_taxonomy} tags
add_filter( 'bricks/dynamic_data/post_terms_links', '__return_false' );
```

or, for a specific taxonomy:

```php
add_filter( 'bricks/dynamic_data/post_terms_links', function( $has_links, $post, $taxonomy) {
  // Disable links for my_custom_tax taxonomy
  return $taxonomy !== 'my_custom_tax';
}, 10, 3);
```
