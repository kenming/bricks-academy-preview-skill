The WordPress element displays various WordPress widgets with customizable styling.

## Settings

- **Widget** (select) - Type of WordPress widget to display. Options: `archives`, `calendar`, `categories`, `pages`, `recent comments`, `recent posts`, `tag cloud`, `taxonomy`. Default: `posts`.

- **Icon** (icon) - Optional icon for the widget. Available for most widget types.

- **Icon typography** (typography) - Font settings for the icon.

### Widget-specific settings

- **Show count** (checkbox) - Display item counts. Available for archives, categories, tag cloud, taxonomy.

- **Sort by** (select) - Sort order for pages. Options: `page title`, `page date`, `page modified`, `page order`, `page ID`. Available for pages.

- **Include** (select) - Specific pages to include. Available for pages.

- **Exclude** (select) - Specific pages to exclude. Available for pages.

- **Number of comments** (number) - How many recent comments to show. Available for recent comments.

- **Number of posts** (number) - How many recent posts to show. Available for recent posts.

- **Direction** (direction) - Layout direction for posts. Available for recent posts.

- **Show date** (checkbox) - Display post dates. Available for recent posts.

- **Show featured image** (checkbox) - Display post thumbnails. Available for recent posts.

- **Featured image sizes** (select) - Size of featured images. Available for recent posts.

- **Featured image width** (text) - Custom width for images. Available for recent posts.

- **Featured image height** (text) - Custom height for images. Available for recent posts.

- **Post title typography** (typography) - Font settings for post titles. Available for recent posts.

- **Post meta typography** (typography) - Font settings for post meta. Available for recent posts.

- **Taxonomy** (select) - Which taxonomy to display. Available for tag cloud and taxonomy.

### Title

- **Title** (text) - Custom title for the widget.

- **HTML tag** (select) - HTML tag for the title. Options: `p`, `h1`-`h6`. Default: `h3`.

- **Border** (border) - Border styling for the title.

- **Typography** (typography) - Font settings for the title.

:::tip[Developer reference]
See the [WordPress Schema](/developer/schema/elements/wordpress/) for the full JSON schema of this element's settings and controls.
:::
