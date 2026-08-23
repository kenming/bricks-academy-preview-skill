---
title: "Settings and defaults"
description: "Review the Bricks settings and defaults used in the Academy setup so your builder behavior, styling, and templates match the tutorial flow."
canonical: "https://academy.bricksbuilder.io/getting-started/settings-defaults/"
markdownUrl: "https://academy.bricksbuilder.io/getting-started/settings-defaults.md"
pageType: "article"
section: "getting-started"
category: "settings-defaults"
lastmod: "2026-08-20T13:12:40.000Z"
---
import SchemaDownload from '../../../components/SchemaDownload.astro'

https://youtu.be/LBOO77mhXI8

Before you start building pages, it helps to know that Bricks has a separate settings screen in the WordPress dashboard: **Bricks > Settings**.

These are your global Bricks settings. They affect how Bricks behaves across the site and are separate from the builder controls you will use while designing pages and templates.

Bricks tries to stay as unopinionated as possible, so there is no single "correct" setup. This preset is completely optional. If you want a simple starting point with sensible defaults for this series, import it and keep moving. If not, you can skip it and come back to the deeper settings later when a specific need comes up.

## Import the preset

1. Download the preset:

   <SchemaDownload
     href="/downloads/getting-started-bricks-settings.json"
     label="Download preset (JSON)"
     fileName="getting-started-bricks-settings.json"
   />

2. In the WordPress dashboard, go to **Bricks > Settings** → **Import Settings**.
3. Drop the JSON onto the upload area or use **Select file**.
4. Click **Import Settings**.

This preset enables:

- **Pages** only
- **Load all matching theme styles**
- **Query sort / filter / live search**
- **Custom breakpoints**
- Template thumbnails
- Toolbar logo set to **Dashboard**
- Structure actions
- Breadcrumbs
- **HTML & CSS to Bricks** with confirm-on-paste
- **Global class import manager** on conflicts
- Hover previews
- **Disable jQuery migrate**
- **Disable class chaining**
- **Preload custom fonts**

## Set it yourself

If you prefer not to import anything, that is totally fine too. The defaults are good enough to continue with the series.

When you start needing something specific, like builder access for editors, performance tweaks, template options, or API keys, you can revisit the full [Bricks Settings](/builder/setup/settings/) article.
