---
title: "Filter: bricks/screen_conditions/scores"
description: "Bricks selects the template & theme style for a specific page according to the conditions you've defined."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-screen_conditions-scores/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-screen_conditions-scores.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Bricks selects the template & theme style for a specific page according to the conditions you've defined.

Internally this is done via a scoring system from 0 to 10. 0 is the least specific. 10 being the most specific (e.g. specific post ID).

For each template/theme style condition that could apply to a certain context, the template/theme style earns a specific score. After analyzing all templates/theme styles, Bricks chooses the one with the highest score.

If you need to add new template conditions using the filter [`builder/settings/template/controls_data`](/developer/hooks/filters/filter-builder-settings-type-controls_data/) or `bricks/theme_styles/controls` for theme styles, you then need to hook into the scoring logic to score the templates/theme styles based on the custom conditions.

This is where the `bricks/screen_conditions/scores` filter comes in handy, like so:

```php
add_filter( 'bricks/screen_conditions/scores', function( $scores, $condition, $post_id, $preview_type ) {
  // Run custom logic to score the template/theme style $condition
  // $scores[] = 5;

  return $scores;
}, 10, 4 );
```

**Example 1: Add the score for a specific author role in an author archive template**

After adding the control using the [`builder/settings/template/controls_data`](/developer/hooks/filters/filter-builder-settings-type-controls_data/) (check example 1), we now need to hook in `bricks/screen_conditions/scores` to score the template based on the condition, like so:

```php
add_filter( 'bricks/screen_conditions/scores', function( $scores, $condition, $post_id, $preview_type ) {
  if ( is_author() && $condition['main'] === 'archiveType' && isset( $condition['archiveType'] ) && in_array( 'author', $condition['archiveType'] ) && isset( $condition['archiveAuthorRoles'] ) ) {
    $user = get_queried_object();

    if ( ! empty( $user->roles ) && is_array( $user->roles ) ) {
      foreach ( $user->roles as $role_name ) {
        if ( in_array( $role_name, $condition['archiveAuthorRoles'] ) ) {
          $scores[] = 9;
        }
      }
    }
  }

  return $scores;
}, 10, 4 );
```
