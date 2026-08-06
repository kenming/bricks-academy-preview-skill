---
title: "Pricing tables"
description: "The Pricing Tables element creates responsive pricing table layouts with customizable headers, pricing information, feature lists, and call-to-action buttons."
canonical: "https://academy.bricksbuilder.io/builder/elements/general/pricing-tables/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/general/pricing-tables.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-04T12:13:33.000Z"
---
The Pricing Tables element creates responsive pricing table layouts with customizable headers, pricing information, feature lists, and call-to-action buttons.

## Settings

- **Pricing tables** (repeater) - Configure multiple pricing tables. Each table includes:

  - **Show under** (select) - Which tab to display the table under. Options: `Tab 1`, `Tab 2`. Default: `Tab 1`.

  - **Table background** (background) - Background styling for the table.

  - **Table border** (border) - Border styling for the table.

  - **Table box shadow** (box-shadow) - Shadow effect for the table.

  ### Header

  - **Title** (text) - Table title. Placeholder: `Title`.

  - **Subtitle** (text) - Table subtitle. Placeholder: `Subtitle`.

  - **Padding** (spacing) - Header padding.

  - **Background color** (color) - Header background color.

  - **Border** (border) - Header border styling.

  - **Title typography** (typography) - Title font settings.

  - **Subtitle typography** (typography) - Subtitle font settings.

  ### Pricing

  - **Padding** (spacing) - Pricing section padding.

  - **Price prefix** (text) - Text before price (e.g., currency symbol).

  - **Price** (text) - Main price amount.

  - **Price suffix** (text) - Text after price.

  - **Price meta** (text) - Additional pricing info (e.g., "per month").

  - **Meta typography** (typography) - Price meta font settings.

  - **Price typography** (typography) - Price font settings.

  - **Background color** (color) - Pricing section background.

  - **Border** (border) - Pricing section border.

  - **Original price** (text) - Strikethrough original price.

  - **Original price typography** (typography) - Original price font settings.

  ### Features

  - **Padding** (spacing) - Features section padding. Default: 10px top, 30px right, 10px bottom, 30px left.

  - **Features** (textarea) - Feature list, one per line.

  - **Alignment** (justify-content) - Feature text alignment. Default: `Center`.

  - **Icon** (icon) - Icon for features.

  - **Icon color** (color) - Feature icon color.

  - **Icon size** (number with units) - Feature icon size.

  - **Icon position** (select) - Icon placement. Options: `Right`, `Left`. Default: `Left`.

  - **Background color** (color) - Features section background.

  - **Border** (border) - Features section border.

  - **Typography** (typography) - Features text font settings.

  ### Footer

  - **Padding** (spacing) - Footer padding.

  - **Background color** (color) - Footer background color.

  - **Border** (border) - Footer border styling.

  ### Button

  - **Button text** (text) - Call-to-action button text. Placeholder: `Button text`.

  - **Link** (link) - Button destination. Placeholder: `https://yoursite.com`.

  - **Width** (number with units) - Button width.

  - **Size** (select) - Button size options.

  - **Style** (select) - Button style. Default: `None`.

  - **Background color** (color) - Button background color.

  - **Border** (border) - Button border styling.

  - **Typography** (typography) - Button text font settings.

  ### Additional info

  - **Additional info** (textarea) - Extra information below button.

  - **Typography** (typography) - Additional info font settings.

  ### Ribbon

  - **Text** (text) - Ribbon label text.

  - **Position** (select) - Ribbon placement. Options: `Left`, `Right`. Default: `Right`.

  - **Background color** (color) - Ribbon background color.

  - **Typography** (typography) - Ribbon text font settings.

- **Columns** (number) - Number of columns for table layout. Minimum: 1.

- **Spacing** (number with units) - Gap between tables. Default: 30px.

- **Align tables** (align-items) - Vertical alignment of tables. Default: `Stretch`.

## Tabs

- **Show tabs** (checkbox) - Enable tabbed pricing layout.

- **Tab 1 label** (text) - First tab label. Placeholder: `Monthly`.

- **Tab 2 label** (text) - Second tab label. Placeholder: `Yearly`.

- **Default tab** (select) - Initially active tab. Options: `Tab 1`, `Tab 2`. Default: `Tab 1`.

- **Alignment** (justify-content) - Tab alignment. Default: `Center`.

- **Margin** (spacing) - Tabs container margin.

- **Background** (color) - Tabs container background.

- **Border** (border) - Tabs container border.

- **Box shadow** (box-shadow) - Tabs container shadow.

### Tab

- **Width** (number with units) - Individual tab width.

- **Margin** (spacing) - Individual tab margin.

- **Padding** (spacing) - Individual tab padding.

- **Background** (color) - Tab background color.

- **Border** (border) - Tab border styling.

- **Box shadow** (box-shadow) - Tab shadow.

- **Typography** (typography) - Tab text font settings.

- **Active background** (color) - Active tab background color.

- **Active border** (border) - Active tab border styling.

- **Active box shadow** (box-shadow) - Active tab shadow.

- **Active typography** (typography) - Active tab text font settings.

:::tip[Developer reference]
See the [Pricing Tables Schema](/developer/schema/elements/pricing-tables/) for the full JSON schema of this element's settings and controls.
:::
