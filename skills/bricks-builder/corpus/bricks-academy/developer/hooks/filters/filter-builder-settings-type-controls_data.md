---
title: "Filter: builder/settings/{type}/controls_data"
description: "Register custom controls for the Bricks Page Settings or Template Settings panels in the builder."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-builder-settings-type-controls_data/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-builder-settings-type-controls_data.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
This filter allows you to add new controls to the Page Settings or Template Settings panels in the builder.

To manage the **Template Settings** controls use the `builder/settings/template/controls_data` hook like so:

```php
add_filter( 'builder/settings/template/controls_data', function( $data ) {
  // Do something

  return $data;
} );
```

To manage the **Page Settings** controls use the `builder/settings/page/controls_data` hook like so:

```php
add_filter( 'builder/settings/page/controls_data', function( $data ) {
  // Do something

  return $data;
} );
```

**Example: Add a control to select the user roles in the author archive template type template condition**

```php
add_filter( 'builder/settings/template/controls_data', function( $data ) {
  // Get all the site user roles
  $all_roles = wp_roles()->roles;

  $roles = [];

  foreach ( $all_roles as $role => $role_data ) {
    $roles[ $role ] = $role_data['name'];
  }

  // Add control to select the user roles for an author archive template type
  $data['controls']['templateConditions']['fields']['archiveAuthorRoles'] = [
    'type'        => 'select',
    'label'       => esc_html__( 'Author roles', 'bricks' ),
    'options'     => $roles,
    'multiple'    => true,
    'placeholder' => esc_html__( 'Select role', 'bricks' ),
    'description' => esc_html__( 'Leave empty to apply template to all roles.', 'bricks' ),
    'required'    => [ 'archiveType', '=', 'author' ],
  ];

  return $data;
} );
```
