Place and customize the following filter to display a different set of web-safe fonts in the typography control.

```php
add_filter( 'bricks/builder/standard_fonts', function( $standard_fonts ) {
  // Option #1: Add individual standard font
  $standard_fonts[] = 'Verdana';

  // Option #2: Replace all standard fonts
  $standard_fonts = [
    'Georgia',
    'Times New Roman',
    'Verdana',
  ];

  return $standard_fonts;
} );
```
