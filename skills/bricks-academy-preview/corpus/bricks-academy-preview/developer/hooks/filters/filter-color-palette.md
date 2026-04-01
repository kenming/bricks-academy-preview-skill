Place and customize the following filter to display a different default color palette for the color control.

```php
add_filter( 'bricks/builder/color_palette', function( $colors ) {
  // Option #1: Add an individual color
    $colors[] = [
      'hex' => '#3ce77b',
      'rgb' => 'rgba(60, 231, 123, 0.56)',
    ];

  // Option #2: Override entire color palette
  $colors = [
    ['hex' => '#3ce77b'],
    ['hex' => '#f1faee'],
    ['hex' => '#a8dadc'],
    ['hex' => '#457b9d'],
    ['hex' => '#1d3557'],
  ];

  return $colors;
} );
```
