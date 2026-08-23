---
title: "Bricks CLI"
description: "Use Bricks CLI commands through WP-CLI to run builder-related maintenance tasks from the command line."
canonical: "https://academy.bricksbuilder.io/developer/guides/bricks-cli/"
markdownUrl: "https://academy.bricksbuilder.io/developer/guides/bricks-cli.md"
pageType: "article"
section: "developer"
category: "guides"
lastmod: "2026-08-20T13:12:40.000Z"
---
Bricks 1.8.1+ integrates with the [WP-CLI](https://wp-cli.org/) (WordPress Command Line Interface). Allowing you to perform specific tasks from your server's command line interface instead of the GUI (Graphical User Interface).

### Regenerates CSS Files

Requires the Bricks "CSS loading method" to be set to "external files".

`wp bricks regenerate_assets`
