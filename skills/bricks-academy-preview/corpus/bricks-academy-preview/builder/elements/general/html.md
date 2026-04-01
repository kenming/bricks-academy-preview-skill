The **HTML** element outputs **raw HTML** from a single code field. In the theme it is marked **deprecated** (`deprecated` flag): prefer the [Code](/builder/elements/general/code/) element, blocks, or native elements for new layouts so you keep validation, security, and editor consistency.

It exists for **backward compatibility** and for the **Gutenberg** block mapping (`core/html`) when converting content.

## Settings

- **Raw HTML** (code) — HTML source, editor mode `text/html`. Default includes a sample heading and paragraph.

If the field is empty, the element shows a “No HTML markup defined” placeholder on the front end.

:::tip[Developer reference]
See the [HTML Schema](/developer/schema/elements/html/) for the full JSON schema of this element's settings and controls.
:::
