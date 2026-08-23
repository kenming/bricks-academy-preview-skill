---
title: "Save & Publish"
description: "Understand how saving and publishing work in Bricks, including drafts, updates, and when frontend changes go live."
canonical: "https://academy.bricksbuilder.io/builder/interface/save-publish/"
markdownUrl: "https://academy.bricksbuilder.io/builder/interface/save-publish.md"
pageType: "article"
section: "builder"
category: "interface"
lastmod: "2026-08-20T13:12:40.000Z"
---
Bricks, by default, automatically creates an autosave every 60 seconds when the current builder area has unsaved element changes.

Autosave creates a backup copy of the elements on the canvas. It does not save global data such as components, classes, or variables. Autosaves can be restored under **Manage > History / Revisions** from the builder toolbar.

To adjust or disable the autosave interval go to **Bricks > Settings > Builder** in your WordPress admin area. The default interval is 60 seconds, and the minimum interval is 15 seconds.

Bricks detects unsaved changes and will show you a prompt to help prevent data loss in case you reload the builder by accident.

To manually save your changes click the **Save** (disk) icon at the very right of the builder toolbar. Or use the [keyboard shortcut](/builder/interface/keyboard-shortcuts/) CMD/CTRL + S.

**Bricks creates a revision/snapshot** when changed Bricks data or page settings are saved using the standard WordPress Revisions API ([learn more about revisions](/builder/interface/revisions/)).

Designing a stunning website or writing compelling content is hard. That's why Bricks celebrates every saved change by displaying a random save message to keep your spirit up :)

You can, of course, customize those save messages via the [bricks/builder/save_messages](/developer/hooks/filters/filter-save-messages/) filter.

## Publishing A Page

When an unpublished page (draft) is saved the status does not change by itself. So once your page is ready to be published click the **Publish** (power) icon in the builder toolbar.
