Filters the array of active templates (header, footer, content, popup) that Bricks has determined should be rendered for the current page.

## Parameters

- `$active_templates` (*array*): Array of active template IDs, keyed by template type (e.g., `header`, `footer`, `content`, `popup`).
- `$post_id` (*int*): The current post ID being rendered.
- `$content_type` (*string*): The type of content being rendered (e.g., `content`, `archive`, `search`, `error`).

## Example usage

```php
add_filter( 'bricks/active_templates', function( $active_templates, $post_id, $content_type ) {
    // Example: Use a specific header template (ID: 1234) for single posts
    if ( is_single() ) {
        $active_templates['header'] = 1234;
    }

    return $active_templates;
}, 10, 3 );
```
