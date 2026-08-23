---
title: "Filter: bricks/active_templates"
description: "Filter the active Bricks templates applied to the current request so you can add, remove, or swap templates programmatically."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-active_templates/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-active_templates.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Modify the templates applied on a page programmatically (`@since 1.8.4`)

This is an alternative to setting an active template via the [bricks/screen_conditions/scores](/developer/hooks/filters/filter-bricks-screen_conditions-scores/) filter.

:::note
Please note that this filter is executed after `bricks/screen_conditions/scores`
:::

## Example: Do not use the Single template if the post has been edited with Bricks {#exclude-default-template-if-post-edit-by-bricks}

In this example, we want to exclude the single post from utilizing a template if it contains Bricks data (Edit with Bricks).

```php
add_filter( 'bricks/active_templates', 'set_my_active_templates', 10, 3 );
function set_my_active_templates( $active_templates, $post_id, $content_type ) {
  // Return if single post $content_type is not 'content'
  if ( $content_type !== 'content' ) {
    return $active_templates;
  }

  // Return: Current post type is not 'post'
  $post_type = get_post_type( $post_id );

  if ( $post_type !== 'post' ) {
    return $active_templates;
  }

  /**
   * $active_templates is an array with different important keys
   *
   * $active_templates['header'] is the header template ID, set it to 0 if do not want to use any template
   * $active_templates['content'] is the content template ID, set it to current post ID if do not want to use any template
   * $active_templates['footer'] is the footer template ID, set it to 0 if do not want to use any template
   *
   * $active_templates['search'] is the search template ID, will only be used if $content_type is 'search'
   * $active_templates['archive'] is the archive template ID, will only be used if $content_type is 'archive'
   * $active_templates['error] is the error template ID, will only be used if $content_type is 'error'
  */

  // Check if the current post has Bricks data, return value is an array
  $bricks_data = \Bricks\Database::get_data( $post_id, 'content' );

  if ( count( $bricks_data ) > 0 ) {
    // Has Bricks data: Don't use any template, set the $active_templates['content'] to current post ID
    $active_templates['content'] = $post_id;

    // To disable header & footer (e.g. landing page) set $active_templates['header'] & $active_templates['footer'] to 0
    $active_templates['header'] = 0;
    $active_templates['footer'] = 0;
  }

  return $active_templates;
}
```

## Example: Change a single template based on a custom field {#single-template-via-custom-field}

There is a scenario like having multiple single templates for a custom post type. Using this filter, you can decide which template to apply based on a custom field.

```php
add_filter( 'bricks/active_templates', 'set_active_templates_by_custom_field', 10, 3 );

function set_active_templates_by_custom_field( $active_templates, $post_id, $content_type ) {
  // Return if single post $content_type is not 'content'
  if ( $content_type !== 'content' ) {
    return $active_templates;
  }

  // Return: Current post type is not 'project'
  $post_type = get_post_type( $post_id );

  if ( $post_type !== 'project' ) {
    return $active_templates;
  }

  // Get the custom field value from Metabox
  $value = absint( rwmb_meta( 'use_template_id' ) );

  // Value not empty: Set $active_templates['content'] to the value
  if ( $value > 0 ) {
    $active_templates['content'] = $value;
    // If single template, the page settings will be used, so no need to set header and footer
  }

  return $active_templates;
}
```

## Example: Disable active template in the builder {#disable-active-template-in-builder}

Since Bricks 1.12, templates applied to a page are now also displayed in the Builder. Previously, only the *Post Content* element was visible, making it difficult to style surrounding elements. If you prefer the old behavior and want to disable the applied template *only inside the builder*, you can use this filter:

```php
add_filter( 'bricks/active_templates', 'disable_template_in_builder', 10, 3 );

function disable_template_in_builder( $active_templates, $post_id, $content_type ) {
  // Only run my logic in the Builder
  if ( bricks_is_builder() ) {
    $active_templates['content'] = 0;
  }

  return $active_templates;
}
```

### Explanation:

- This function runs only when Bricks is in **Builder mode** (`bricks_is_builder()`).
- It prevents the active single template from applying inside the Builder by setting `$active_templates['content'] = 0`.
- The frontend remains unaffected; the template is still used when viewing the post/page normally.
- This effectively disables the new **outer Post Content elements visibility** introduced in **Bricks 1.12**, restoring the previous Builder behavior.
