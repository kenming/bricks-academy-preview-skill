This filter allows you to include your custom query loop supported element to generate the children styles in Bricks. (@since 1.9.2)

```php
add_filter( 'bricks/assets/generate_css_from_element', function( $element_name, $current_element, $css_type ) {
  // $css_type is a string (e.g. header, footer, content, etc.)
  // Add your custom element name so the looping children styles are generated.
  if ( ! in_array( 'my-custom-element-name', $element_name ) ) {
    $element_name[] = 'my-custom-element-name';
  }

  return $element_name;
}, 10, 3 );
```
