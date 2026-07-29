---
title: "Filter submit"
description: "Creates submit/reset buttons for filter forms. Provides control over when filters are applied - either as a submit button to apply all filters at once, or as a."
canonical: "https://academy.bricksbuilder.io/builder/elements/filter/filter-submit/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/filter/filter-submit.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-07-29T10:15:35.000Z"
---
Creates submit/reset buttons for filter forms. Provides control over when filters are applied - either as a submit button to apply all filters at once, or as a reset button to clear all active filters. Supports redirection to specific URLs after submission.

## Settings

- **Target query** (query-list) - Select the query this filter should target. Only post queries are supported in this version.
- **URL parameter** (text) - Define a unique, more readable URL parameter name for this filter.
- **Action** (select) - Button behavior. Options: Submit (apply filters), Reset (clear filters).
- **Redirect to** (text) - URL to redirect to after applying filters (Submit action only).
- **Open in new tab** (checkbox) - Open redirect URL in new tab (Submit action only).
- **Hide if no active filter** (checkbox) - Hide the reset button when no filters are active. Adds .brx-no-active-filter class for styling (Reset action only).
- **Button** - Settings for the submit/reset button.
  - **Text** (text) - Button text. Default: Filter.
  - **Size** (select) - Button size preset. Options: Default, Small, Medium, Large, Extra Large.
  - **Style** (select) - Button style. Options: None, Primary, Secondary, Success, Info, Warning, Danger, Dark, Light. Default: Primary.
  - **Circle** (checkbox) - Make button circular.
  - **Outline** (checkbox) - Use outline button style.
  - **Icon** (icon) - Icon to display on the button.
  - **Icon color** (color) - Color of the button icon.
  - **Icon size** (number) - Size of the button icon.

:::tip[Developer reference]
See the [Filter - Submit / Reset Schema](/developer/schema/elements/filter-submit/) for the full JSON schema of this element's settings and controls.
:::
