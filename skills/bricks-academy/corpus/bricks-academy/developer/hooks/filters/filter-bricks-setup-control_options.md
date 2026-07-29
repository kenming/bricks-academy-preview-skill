---
title: "Filter: bricks/setup/control_options"
description: "Bricks offers a WordPress filter to add or remove control options. The control options are used throughout Bricks and allow you to manage the options of the:"
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-setup-control_options/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-setup-control_options.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Bricks offers a WordPress filter to add or remove control options. The control options are used throughout Bricks and allow you to manage the options of the:

- Template Types (e.g. Header, Footer, Single, Section...)
- Background position, repeat, attachment or size
- Button sizes
- Button or Heading styles
- Border styles
- Font weight and style
- CSS position
- Query types (e.g. Posts, Terms, Users, ..)
- Query order by, compare, operator and value type
- Image Sizes
- Taxonomies
- User roles

To manage any of these options or add new ones, use the WP hook `bricks/setup/control_options` like so:

```php
add_filter( 'bricks/setup/control_options', function( $control_options ) {
    $control_options['templateTypes']['my_template_type'] = esc_html__( 'My Template Type', 'my-plugin' );

    return $control_options;
} );
```

Note: the above example adds a new template type. To learn about other Bricks controls, visit the [Controls section](/developer/controls/).
