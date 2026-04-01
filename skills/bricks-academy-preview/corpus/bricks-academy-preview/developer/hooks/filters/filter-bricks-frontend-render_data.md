The filter allows you to modify the rendered content for different areas like header, content, and footer before it's displayed on the frontend.

```php
add_filter( 'bricks/frontend/render_data', function( $content, $post, $area ) {
  // Do something

  return $content;
}, 10, 3 );
```

The filter callback receives three parameters:

- `$content`: The HTML content that's about to be returned. It's a string type.
- `$post`: The post object for which the content is being generated. It's an instance of the WP_Post class.
- `$area`: A string defining the area of the page currently being rendered (e.g., 'header', 'content', 'footer'). Available since version 1.5.4.

## Example: Add a unique ID to each heading

The following example demonstrates how to add a unique ID attribute to each heading in the generated content.

```php
add_filter('bricks/frontend/render_data', function($content, $post, $area) {
  // Iterate over each heading tag
  $content = preg_replace_callback(
    '/(<h[1-6](.*?))>(.*?)(<\/h[1-6]>)/i',
    function($matches) {
      // Add 'id' attribute if it doesn't exist
      if (strpos($matches[2], 'id=') === false) {
        // Use heading's content as the ID
        $matches[0] = $matches[1] . ' id="' . sanitize_title($matches[3])
        . '">' . $matches[3] . $matches[4];
      }

      // Return the (potentially) modified heading tag
      return $matches[0];
    },
    $content // Content to modify
  );

  // Return modified content
  return $content;
}, 10, 3);
```

In this example, a callback function is defined within the add_filter function call targeting the `bricks/frontend/render_data` filter. This callback function modifies every heading tag present in the content to include a unique ID attribute. This can be useful for navigation purposes, such as creating a table of contents.
