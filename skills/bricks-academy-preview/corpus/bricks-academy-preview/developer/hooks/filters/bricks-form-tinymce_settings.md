Filters the TinyMCE configuration settings for "Rich Text" fields in Bricks forms. This allows you to customize the toolbar, menus, and other editor options.

## Parameters

- `$settings` (*array*): Array of TinyMCE settings.

## Example usage

```php
add_filter( 'bricks/form/tinymce_settings', function( $settings ) {
    // Example: Disable the menubar
    $settings['menubar'] = false;

    // Example: Simplify the toolbar
    $settings['toolbar'] = 'bold italic underline | bullist numlist | link unlink';

    return $settings;
} );
```
