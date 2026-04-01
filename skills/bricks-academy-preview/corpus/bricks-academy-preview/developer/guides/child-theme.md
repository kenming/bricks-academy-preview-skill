:::note
Please do not edit any of the Bricks theme core files directly, as updating the theme will cause all your changes to be lost.
:::

Instead, use the Bricks child theme to make modifications and overwrite files. You can download the Bricks child theme directly from your [Bricks account](https://my.bricksbuilder.io/).

Upload this child theme ZIP file (bricks-child.zip) like any other WordPress theme. Go to **Appearance → Themes** and activate **Bricks Child Theme**. You can add your own styles to **style.css**.

## How To Enqueue Scripts (JS) & Styles (CSS)

In order to load your files only on the front end & the canvas and not in the builder panel (as your custom CSS might affect the builder), you have to check against `bricks_is_builder_main()` like this:

```php
add_action( 'wp_enqueue_scripts', function() {
  // Code & check below enqueues your files on the canvas & frontend, not the builder panel. Otherwise custom CSS might affect builder)
  if ( ! bricks_is_builder_main() ) {
    wp_enqueue_style( 'bricks-child', get_stylesheet_uri(), ['bricks-frontend'], filemtime( get_stylesheet_directory() . '/style.css' ) );
  }
} );
```

You can learn more about how a Child Theme works by visiting the official WordPress Codex: [https://developer.wordpress.org/themes/advanced-topics/child-themes/](https://developer.wordpress.org/themes/advanced-topics/child-themes/)

The `functions.php` file of a child theme, unlike `style.css`, does not override the `functions.php` file of the parent theme. Instead, it is loaded in addition to the parent theme's `functions.php`, right before the parent file.
