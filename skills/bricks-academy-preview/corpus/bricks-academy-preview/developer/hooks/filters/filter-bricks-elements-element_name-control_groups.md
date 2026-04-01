Since Bricks 1.4 it is possible to add custom control groups to a specific element like so:

```php
add_filter( 'bricks/elements/heading/control_groups', function( $control_groups ) {
    $control_groups['custom_controls'] = [
        'tab'      => 'content', // or 'style'
        'title'    => esc_html__( 'Custom controls', 'my_plugin' ),
    ];

    return $control_groups;
} );
```

Note: the above example adds a new control group with the title "**Custom controls**" to the **heading** element, using the filter `bricks/elements/**heading**/control_groups`. To learn about other Bricks controls visit the [Topic: Controls](https://academy.bricksbuilder.io/topic/controls/).
