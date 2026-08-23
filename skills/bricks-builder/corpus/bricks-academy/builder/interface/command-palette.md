---
title: "Command Palette"
description: "Use the Bricks Command Palette to run common actions, navigate faster, and insert element structures with keyboard-driven workflows."
canonical: "https://academy.bricksbuilder.io/builder/interface/command-palette/"
markdownUrl: "https://academy.bricksbuilder.io/builder/interface/command-palette.md"
pageType: "article"
section: "builder"
category: "interface"
lastmod: "2026-08-20T13:12:40.000Z"
---
Bricks 2.0 introduces the **Command Palette**, a powerful new feature that gives you instant keyboard-driven access to core functionality inside the builder.

## How to launch it

Click the command `⌘` icon in the builder toolbar or use the `CMD/CTRL + K` keyboard shortcut to open the Command Palette, which appears as an overlay, allowing you to type and filter commands across three distinct scopes.

## Scope: Builder {#builder}

Navigate to key parts of the builder from a growing list of targets such as classes, variables, templates, theme styles, settings, etc.

![](imgs/bricks-2.0-command-palette-scope-builder-5a92e2d9cb.png)

## Scope: Post Types {#post-types}

This scope lets you browse the registered post types your builder capability can access, create new posts when your user can edit posts, or duplicate existing posts.

The scope auto-selects the post type that you are currently editing. So if you are editing a Bricks template the "Template (Bricks)" post type will be selected. If you edit a "Page", then "Page" is selected and so on.

![](imgs/bricks-2.0-command-palette-scope-post-types-332f376ff0.png)

## Scope: Elements {#elements}

The "Elements" scope will dramatically speed up your workflow by allowing you to insert multiple elements with specific structure in a single action.

By mastering the Emmet-like syntax, you can create complex layouts in seconds rather than minutes, making your design process significantly more efficient.

With practice, this feature becomes second nature and an essential part of your Bricks Builder toolkit, especially for quickly creating common page structures and element combinations that you use frequently, which you can also save for instant access to use whenever needed.

![](imgs/bricks-2.0-command-palette-scope-elements-b819731a2d.png)

### Insert single element

To insert a single element simply type its name, such as "Section", then `ARROW`-navigate to it in the elements list, and insert it by pressing `ENTER` or just click on the element name.

### Insert element structure

Each element starts with an **@** symbol.

The element name that the command bar requires is displayed in square brackets in the results list:



![](imgs/bricks-2.0-command-palette-element-name-173506e9d7.png)

<figcaption>

Text link element command: `@text-link`

</figcaption>



### Supported operators

Use the following operators to define nested structure, siblings, a multiplier, or to move back up one nesting level.

| Symbol | Meaning |
| --- | --- |
| `@` | Bricks element name (e.g. `@heading`) |
| `>` | Nest inside |
| `+` | Insert element as sibling |
| `*` | How often to insert the element |
| `^` | Move one level up before inserting the next element |

### Element structure example

`@section * 2 > @heading + @text + @button`
This creates the following structure *(two times because of the multiplier: `* 2`)*:

- `Section`
 └ `Container`
   ├ `Heading`
   ├ `Text`
   └ `Button`

### Quick element insertion

:::note
After selecting an element from the search results, its name is added to your query with the `@` prefix, allowing you to quickly build complex queries:
:::

1. Type `@` to activate insertion mode
2. Select an element (e.g., "section")
3. Type `>` for a child element
4. Continue building your structure
5. Click your element structture
  - Click the "Insert" button that appears next to your query
  - Press `CMD/CTRL + ENTER`

### Save element structures

Instead of typing out your favorite structures by hand every time can just save them by clicking the "Save" button next to the command bar. Your structures are stored in this browser's `localStorage`, so they are local to that browser/profile and are not synced between users or devices.



![](imgs/bricks-2.0-command-palette-saved-element-structures-c07f1ea50e.png)

<figcaption>

List of saved element structures

</figcaption>



To delete a structure, mouseover the structure item in the list, and click the "Delete" icon.

## Keyboard shortcuts

| **Keyboard shortcut** | **Action** |
| --- | --- |
| `CMD/CTRL + K` | Open/close the command palette |
| `ESC` | Close the command palette |
| `TAB > ENTER` (to enter selected scope) | Navigate between search and scopes |
| `#` (as the first character in the search input) | Enter scope “Builder” |
| `/` (as the first character in the search input) | Enter scope “Post Types” |
| `+` or `@` (as the first character in the search input) | Enter scope “Elements” |
| `/0-9` (forward slash followed by number) | Navigate to a specific post type |
| `ARROW UP/DOWN` + ENTER | Navigate to a search result and open it |

## Notes

Bricks remembers your last selected scope, even after builder reload (stored in your localStorage).

The "Pages" panel remains available from the builder toolbar. The Command Palette is an additional fast way to browse, create, duplicate, and open posts.

The docs entry is also accessible from the "Builder" scope.
