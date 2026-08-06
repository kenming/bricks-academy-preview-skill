---
title: "Logo"
description: "The Logo element displays your site logo with support for regular, inverse, and dark-mode logo variants, custom dimensions, and fallback text."
canonical: "https://academy.bricksbuilder.io/builder/elements/media/logo/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/media/logo.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-04T12:13:33.000Z"
---
The Logo element displays your site logo and can switch between logo variants for dark mode and sticky headers.

## Settings

- **Logo** (image) - Select the main logo image from the media library. Minimum dimension should be twice the logo height/width for proper retina display. For SVG logos, set height and width in px values.

- **Logo inverse** (image) - Alternative logo image for sticky scrolling headers. Only available when the main logo is set.

- **Logo dark mode** (image) - Alternative logo image used when dark mode is active. Only available when the main logo is set.

- **Height** (number with units) - Logo height. Maximum: 400. Default: `auto`. Only available when logo is set.

- **Width** (number with units) - Logo width. Maximum: 999. Default: `auto`. Only available when logo is set.

- **Text** (text) - Fallback text displayed if logo image isn't set or available. Default: Site name from WordPress settings.

- **Loading** (select) - Image loading behavior. Options: `eager`, `lazy`. Default: `eager`.

- **Link to** (link) - Configure where the logo links. Default: Site home page.

## Logo variants

Logo variants are available starting in Bricks 2.4. Add them in the Logo element settings under **Logo variants**.

When [dark mode](/builder/features/color-manager/#using-dark-mode) is active and **Logo dark mode** is configured, Bricks swaps the main logo image for the dark-mode logo. If no dark-mode logo is configured, the main logo stays visible.

If the Logo element is inside a sticky header and **Logo inverse** is configured, the inverse logo is used while the header is scrolling. This takes priority over the dark-mode logo during the sticky scrolling state.

:::tip[Developer reference]
See the [Logo Schema](/developer/schema/elements/logo/) for the full JSON schema of this element's settings and controls.
:::
