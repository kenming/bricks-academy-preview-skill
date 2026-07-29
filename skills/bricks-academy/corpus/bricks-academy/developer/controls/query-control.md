---
title: "Query Control"
description: "Reference for the Bricks Query control, including its options, CSS mapping, and usage in custom elements."
canonical: "https://academy.bricksbuilder.io/developer/controls/query-control/"
markdownUrl: "https://academy.bricksbuilder.io/developer/controls/query-control.md"
pageType: "article"
section: "developer"
category: "controls"
lastmod: "2026-07-29T10:15:35.000Z"
---
The query control lets you set query arguments to retrieve items of any post type. Use the returned value to set up a custom `WP_Query` to render the matching posts in any way you want.

```php
class Prefix_Element_Posts extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleQueryArgs'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Posts', 'bricks' ),
      'type' => 'query',
      // Default required for query to populate
      'default' => [
        'post_type' => 'post',
      ],
    ];
  }

  // Render element HTML
  public function render() {
    $query_args = $this->settings['exampleQueryArgs'];
    $posts_query = new WP_Query( $query_args );

    // Standard WordPress loop
    if ( $posts_query->have_posts() ) :
      while ( $posts_query->have_posts() ) : $posts_query->the_post();
        // Render post title and thumbnail
        the_title( '<h5>', '</h5>' );
        the_post_thumbnail( 'thumbnail' );
      endwhile;

      wp_reset_postdata();
    else :
     esc_html_e( 'No posts matched your criteria.', 'bricks' );
    endif;
  }
}
```

### Resources

- [https://codex.wordpress.org/Class_Reference/WP_Query#Parameters](https://codex.wordpress.org/Class_Reference/WP_Query#Parameters)
