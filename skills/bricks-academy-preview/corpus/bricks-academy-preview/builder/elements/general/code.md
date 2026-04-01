The Code element allows you to add and execute PHP, HTML, CSS, or JavaScript code with syntax highlighting and optional code execution.

## Settings

### Code Execution

Available only for users with code execution permissions:

- **Execute code** (checkbox) - Run the code on your site instead of displaying it. Only add code you consider safe.

- **Parse dynamic data** (checkbox) - Parse dynamic data tags within the code. Only available when execute code is enabled.

- **Suppress PHP errors** (checkbox) - Hide PHP errors from displaying. Add "brx_code_errors" as a URL parameter to show errors if needed. Only available when execute code is enabled.

- **Render without wrapper** (checkbox) - Render on the frontend without the div wrapper. Style tab settings won't apply when this is enabled. Only available when execute code is enabled.

### Code Editors

Available when code execution is disabled or not allowed:

- **PHP & HTML** (code editor) - PHP and HTML code editor with syntax highlighting. Supports dynamic data and variables. Default example includes HTML heading and PHP date output.

- **CSS** (code editor) - CSS code editor with syntax highlighting. CSS is automatically wrapped in style tags. Supports dynamic data and variables.

- **JavaScript** (code editor) - JavaScript code editor with syntax highlighting. JavaScript is automatically wrapped in script tags. Supports dynamic data.

### Syntax Highlighting

Available when code execution is disabled:

- **Theme** (select) - Code syntax highlighting theme. Options: `github` (light), `tomorrow` (light), `tomorrow-night` (dark), `tranquil-heart` (dark). Default: None. Can also be set globally via theme styles.

:::tip[Developer reference]
See the [Code Schema](/developer/schema/elements/code/) for the full JSON schema of this element's settings and controls.
:::
