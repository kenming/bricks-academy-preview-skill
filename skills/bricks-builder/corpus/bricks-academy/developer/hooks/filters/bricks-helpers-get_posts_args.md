---
title: "Filter: bricks/helpers/get_posts_args"
description: "The bricks/helpers/getpostsargs filter allows you to modify the query arguments used when Bricks retrieves posts in the builder via AJAX."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-helpers-get_posts_args/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-helpers-get_posts_args.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
The `bricks/helpers/get_posts_args` filter allows you to modify the query arguments used when Bricks retrieves posts in the **builder via AJAX**.

This includes scenarios such as:

- Searching posts or pages in the link-type control
- Searching posts, pages, or custom post types in the populate content dropdown

This hook gives you full control over the underlying `WP_Query` arguments before the query is executed.

:::note
This filter affects multiple builder features globally. Incorrect modifications may break expected behavior in post selection controls.
:::

## Parameters

- `$query_args` (*array*): Array of arguments passed to `get_posts()`.

## Example: Exclude media from builder search

When WordPress queries with `post_type` set to `any`, the results may include attachments. This example excludes media items unless the caller explicitly requests the `attachment` post type.

```php
add_filter( 'bricks/helpers/get_posts_args', function( $query_args ) {
    // If no post type is provided, treat it as "any" for safety.
    $post_type_arg = $query_args['post_type'] ?? 'any';

    // Detect whether the caller explicitly requested the attachment post type.
    $has_attachment = false;

    if ( is_array( $post_type_arg ) ) {
        $has_attachment = in_array( 'attachment', $post_type_arg, true );
    } else {
        $has_attachment = ( $post_type_arg === 'attachment' );
    }

    // If attachment was explicitly requested, do nothing.
    if ( $has_attachment ) {
        return $query_args;
    }

    // Get all public post types once. We only use this when expanding "any".
    $public_post_types = array_values(
        array_diff(
            get_post_types( [ 'public' => true ], 'names' ),
            [ 'attachment' ]
        )
    );

    // CASE 1: post_type = 'any'
    if ( $post_type_arg === 'any' ) {
        $query_args['post_type'] = $public_post_types;
    }

    // CASE 2: post_type is an array
    elseif ( is_array( $post_type_arg ) ) {
        $normalized_post_types = array_diff( $post_type_arg, [ 'attachment' ] );

        // Defensive handling: if "any" exists in the array, replace it with
        // all public post types except attachment.
        if ( in_array( 'any', $normalized_post_types, true ) ) {
            $normalized_post_types = array_diff( $normalized_post_types, [ 'any' ] );
            $normalized_post_types = array_merge( $normalized_post_types, $public_post_types );
        }

        $query_args['post_type'] = array_values( array_unique( $normalized_post_types ) );
    }

    return $query_args;
} );
```
