Use this filter to customize the configuration of CodeMirror 5, the code editor used within the builder. CodeMirror 5 is used in areas such as the **Custom CSS** setting for elements and the **Code element** settings, where it provides an interface for editing HTML, CSS, JavaScript, PHP, and more.

You can refer to the [CodeMirror 5 configuration documentation](https://codemirror.net/5/doc/manual.html#config) for more details on available options.

## Example Usage:

```php
add_filter( 'bricks/builder/codemirror_config', function( $config ) {
    // Disable auto-close brackets
    $config['autoCloseBrackets'] = false;

    // Disable line numbers
    $config['lineNumbers'] = false;

    // Override default tab size
    $config['tabSize'] = 4;

    return $config;
});
```

In this example, the filter modifies the default CodeMirror configuration to:

- Disable **auto-close brackets**.
- Disable **line numbers**.
- Set the **tab size** to 4 spaces.

**Parameters:**

- `$config` *(array)*: An empty array by default. Define only the specific configurations you need, which will override the builder's default settings.

**Return:**

- *(array)*: The custom configuration array, applied alongside or in place of Bricks' defaults.
