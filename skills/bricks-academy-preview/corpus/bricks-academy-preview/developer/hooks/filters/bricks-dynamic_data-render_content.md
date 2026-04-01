Filters the content to be parsed for dynamic data tags. This is the main filter used to resolve dynamic tags (e.g., `{post_title}`) into their actual values.

## Parameters

- `$content` (*string*): The content string containing dynamic tags.
- `$post` (*WP_Post*): The post context.
- `$context` (*string*): The context where the content is used (e.g., `text`).

## Example usage

```php
$content = 'Hello {post_title}';
$post_id = 123;
$post    = get_post( $post_id );

// Manually parse dynamic data in a string
$parsed_content = apply_filters( 'bricks/dynamic_data/render_content', $content, $post, 'text' );

// Output: Hello My Post Title
echo $parsed_content;
```
