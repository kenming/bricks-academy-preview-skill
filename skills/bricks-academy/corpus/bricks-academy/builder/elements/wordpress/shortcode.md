---
title: "Shortcode"
description: "The Shortcode element executes WordPress shortcodes within your Bricks pages."
canonical: "https://academy.bricksbuilder.io/builder/elements/wordpress/shortcode/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/wordpress/shortcode.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-07-29T10:15:35.000Z"
---
The Shortcode element executes WordPress shortcodes within your Bricks pages.

## Settings

- **Shortcode** (textarea) - Enter the shortcode to execute, including the square brackets (e.g., `[gallery ids="72,73,74,75" columns="3"]`). Supports dynamic data.

- **Don't render in builder** (checkbox) - Show a placeholder instead of rendering the shortcode in the builder. Useful for shortcodes that slow down the builder or cause conflicts.

- **Placeholder: Width** (number with units) - Width of the placeholder when "Don't render in builder" is enabled.

- **Placeholder: Height** (number with units) - Height of the placeholder when "Don't render in builder" is enabled.

:::tip[Developer reference]
See the [Shortcode Schema](/developer/schema/elements/shortcode/) for the full JSON schema of this element's settings and controls.
:::
