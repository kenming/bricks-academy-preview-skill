---
title: "Team members"
description: "The Team Members element displays a responsive grid of team member profiles with images, names, titles, and descriptions."
canonical: "https://academy.bricksbuilder.io/builder/elements/general/team-members/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/general/team-members.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-20T13:12:40.000Z"
---
The Team Members element displays a responsive grid of team member profiles with images, names, titles, and descriptions.

## Settings

### Team members

- **Team members** (repeater) - Add team member profiles. Each member has:
  - **Image** (image) - Profile photo.
  - **Title** (text) - Name of the team member.
  - **Subtitle** (text) - Job title or role.
  - **Content** (textarea) - Description or bio.

### Layout

- **Columns** (number) - Number of columns in the grid (1-6). Controls `grid-template-columns` with `repeat(%s, 1fr)`.

- **Gap** (number with units) - Spacing between team member cards. Controls `gap` property. Default placeholder: `20`.

- **Background** (color) - Background color of member cards. Applied to `.member` selector.

- **Border** (border) - Border styling for member cards. Applied to `.member` selector.

- **Box shadow** (box-shadow) - Shadow effect for member cards. Applied to `.member` selector.

### Image

- **Image position** (select) - Position of the image relative to content. Options: `top`, `right`, `left`, `bottom`. Default: `top`.

- **Image ratio** (select) - Aspect ratio for images. Options from swiper image ratio controls.

- **Width** (number with units) - Width of the images. Applied to `.image` selector.

- **Margin** (spacing) - Margin around the images. Applied to `.image` selector.

- **Border** (border) - Border styling for images. Applied to `.image` selector.

### Content

- **Padding** (spacing) - Padding inside the content area. Applied to `.content` selector. Default placeholder: `15px` (top), `0px` (right, bottom, left).

- **Text align** (text-align) - Text alignment for content. Applied to `.content` selector.

- **Title tag** (select) - HTML tag for member titles. Options: `h2`, `h3`, `h4`, `h5`, `h6`, `p`, `div`. Default: `h4`.

- **Title typography** (typography) - Font styling for member titles. Applied to `.title` selector.

- **Subtitle typography** (typography) - Font styling for member subtitles. Applied to `.subtitle` selector.

- **Description typography** (typography) - Font styling for member descriptions. Applied to `.description` selector.

:::tip[Developer reference]
See the [Team Members Schema](/developer/schema/elements/team-members/) for the full JSON schema of this element's settings and controls.
:::
