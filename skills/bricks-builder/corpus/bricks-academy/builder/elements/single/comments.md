---
title: "Comments"
description: "The Comments element displays post comments and comment form. It offers two display modes: custom styling with full control over appearance, or default."
canonical: "https://academy.bricksbuilder.io/builder/elements/single/comments/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/single/comments.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-04T12:13:33.000Z"
---
The Comments element displays post comments and comment form. It offers two display modes: custom styling with full control over appearance, or default WordPress styling.

## Settings

### Source

- **Source** (select) - Choose comment display mode. Options: Bricks (custom styling), WordPress (WordPress default styling). Default: Bricks.

### Custom styling controls

When **Source** is set to "Bricks", the following controls are available for customizing the comment display and form:

#### Title

- **Show title** (checkbox) - Display comments section title. Default: true.

- **HTML tag** (select) - HTML tag for title. Options: div, h1-h6. Default: h3. Only available when Show title is enabled.

- **Typography** (typography) - Title typography. Controls `font` property for `.comments-title` selector. Only available when Show title is enabled.

#### Avatar

- **Show avatar** (checkbox) - Display commenter avatars. Default: true.

- **Size** (number with units) - Avatar dimensions. Default: 60px. Triggers re-render.

- **Border** (border) - Avatar border settings. Controls `border` property for `.avatar` selector.

- **Box shadow** (box-shadow) - Avatar shadow settings. Controls `box-shadow` property for `.avatar` selector.

#### Comment

- **Author: HTML tag** (select) - HTML tag for commenter names. Options: div, h1-h6. Default: h5. Triggers re-render.

- **Author: Typography** (typography) - Commenter name typography. Controls `font` property for `.comment-author .fn` selector.

- **Meta: Typography** (typography) - Comment meta typography. Controls `font` property for `.comment-meta` selector.

- **Content: Typography** (typography) - Comment content typography. Controls `font` property for `.comment-content` selector.

#### Form

##### Form title

- **Show** (checkbox) - Display comment form title. Default: true.

- **HTML tag** (select) - HTML tag for form title. Options: div, h1-h6. Default: h4. Triggers re-render. Only available when Show is enabled.

- **Text** (text) - Form title text. Default placeholder: "Leave your comment". Only available when Show is enabled.

##### Label

- **Show** (checkbox) - Display form field labels. Default: true.

- **Typography** (typography) - Label typography. Controls `font` property for `label` selector. Only available when Show is enabled.

- **Placeholder typography** (typography) - Placeholder text typography. Controls `font` property for `::placeholder` selector. Only available when Show is enabled.

##### Cookie consent

- **Show** (checkbox) - Display cookie consent checkbox.

- **Required** (checkbox) - Make cookie consent required. Only available when Show is enabled.

- **Text** (text) - Cookie consent text. Only available when Show is enabled.

##### Fields

- **Fields** (select, multiple) - Form fields to display. Options: Name, Email, Website. Default: Name, Email, Website.

##### Field styling

- **Background color** (color) - Form field background color. Controls `background-color` property for `.form-group input` and `.form-group textarea` selectors.

- **Border** (border) - Form field border settings. Controls `border` property for `.form-group input` and `.form-group textarea` selectors.

- **Typography** (typography) - Form field typography. Controls `font` property for `.form-group input` and `.form-group textarea` selectors.

- **Textarea: Resize** (select) - Textarea resize behavior. Options: None, Vertical, Horizontal, Both. Default: Vertical. Controls `resize` property for `.form-group textarea` selector.

#### Submit button

- **Text** (text) - Submit button text. Default placeholder: "Submit Comment". Supports dynamic data.

- **Size** (select) - Button size. Options from button sizes control options. Default placeholder: "Default".

- **Style** (select) - Button style. Options from styles control options. Default: primary.

- **Background** (color) - Button background color. Controls `background-color` property for `.bricks-button` selector.

- **Border** (border) - Button border settings. Controls `border` property for `.bricks-button` selector.

- **Typography** (typography) - Button typography. Controls `font` property for `.bricks-button` selector.

### WordPress default styling

When **Source** is set to "WordPress", the element uses your theme's default comment styling and form layout. No additional styling controls are available - WordPress handles all comment display through the standard `comments_template()` function.

:::tip[Developer reference]
See the [Comments Schema](/developer/schema/elements/post-comments/) for the full JSON schema of this element's settings and controls.
:::
