If you use the dynamic data tag `{read_more}` you'll get an anchor tag (link) to the post with the label "Read more" by default. To change this label use the following code:

```php
add_filter( 'bricks/dynamic_data/read_more', function( $label, $post ) {
   return 'My New Label';
}, 10, 2 );
```

Read more about [Dynamic Data](/builder/dynamic-content/dynamic-data/) in the Bricks academy.
