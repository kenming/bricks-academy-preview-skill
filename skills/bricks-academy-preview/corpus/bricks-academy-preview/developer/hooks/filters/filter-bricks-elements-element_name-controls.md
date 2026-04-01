Since Bricks 1.3.2 it is possible to add custom controls to any element like so:

```php
add_filter( 'bricks/elements/posts/controls', function( $controls ) {
    $controls['ignoreStickyPosts'] = [
        'tab'      => 'content',
        'group'    => 'query',
        'label'    => esc_html__( 'Ignore Sticky Posts', 'my_plugin' ),
        'type'     => 'checkbox'
    ];

    return $controls;
} );
```

Note: the above example adds a new checkbox to the **posts** element, using the filter `bricks/elements/**posts**/controls`. To learn about other Bricks controls visit the [Topic: Controls](https://academy.bricksbuilder.io/topic/controls/).

You might also be interested in the filter [`bricks/posts/query_vars`](/developer/hooks/filters/filter-bricks-posts-query_vars/) to manipulate the posts element query.
