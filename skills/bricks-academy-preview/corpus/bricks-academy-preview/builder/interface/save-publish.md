Bricks, by default, automatically saves your builder changes every 60 seconds.

To adjust or disable the autosave interval go to **Bricks > Settings > Builder** in your WordPress admin area.

Bricks detects unsaved changes and will show you a prompt to help prevent data loss in case you reload the builder by accident.

To manually save your changes click the **Save** (disk) icon at the very right of the builder toolbar. Or use the [keyboard shortcut](/builder/interface/keyboard-shortcuts/) CMD/CTRL + S.

**Bricks creates a revision/snapshot** every time builder data is saved using the standard WordPress Revisions API ([learn more about revisions](/builder/interface/revisions/)).

Designing a stunning website or writing compelling content is hard. That's why Bricks celebrates every saved change by displaying a random save message to keep your spirit up :)

You can, of course, customize those save messages via the [bricks/builder/save_messages](/developer/hooks/filters/filter-save-messages/) filter.

## Publishing A Page

When an unpublished page (draft) is saved the status does not change by itself. So once your page is ready to be published click the **Publish** (power) icon in the builder toolbar.
