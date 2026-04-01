Filters the URL of an uploaded file displayed in the Form Submissions table in the admin area. This is useful if you have customized the upload directory and the auto-generated URL is incorrect.

## Parameters

- `$file_url` (*string*): The generated URL for the file.
- `$file` (*array*): Array containing file information (e.g., `file` path, `name`, `type`).
- `$field_key` (*string*): The ID of the form field.

## Example usage

```php
add_filter( 'bricks/form/submission-table/file_url', function( $file_url, $file, $field_key ) {
    // Example: Fix URL for files in a custom 'secure-uploads' directory
    if ( strpos( $file['file'], 'secure-uploads' ) !== false ) {
        return site_url( '/secure-uploads/' . basename( $file['file'] ) );
    }

    return $file_url;
}, 10, 3 );
```
