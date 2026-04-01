Filters the list of dynamic data tags available in the builder's dynamic data picker. This allows you to register your custom dynamic tags so they appear in the UI.

## Parameters

- `$tags` (*array*): Array of dynamic data tag definitions.

## Example usage

```php
add_filter( 'bricks/dynamic_tags_list', function( $tags ) {
    $tags[] = [
        'name'  => '{my_custom_tag}',
        'label' => esc_html__( 'My Custom Tag', 'my-plugin' ),
        'group' => 'My Plugin Group',
    ];

    return $tags;
} );
```
