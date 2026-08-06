---
title: "Audio"
description: "The Audio element embeds audio files with a customizable player interface."
canonical: "https://academy.bricksbuilder.io/builder/elements/media/audio/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/media/audio.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-04T12:13:33.000Z"
---
The Audio element embeds audio files with a customizable player interface.

## Settings

- **Source** (select) - The audio source type. Options: `file` (media library), `external` (external URL), `dynamic` (dynamic data). Default: `file`.

- **File** (audio) - Select an audio file from the media library. Available when source is "file".

- **External URL** (text) - Enter an external audio file URL. Available when source is "external".

- **Dynamic Data** (text with dynamic data) - Select audio from dynamic data source. Available when source is "dynamic".

- **Custom title** (text) - Override the audio title. Not available for external sources.

- **Show artist** (checkbox) - Display the artist name from audio metadata. Not available for external sources or when custom title is set.

- **Show title** (checkbox) - Display the audio title from metadata. Not available for external sources or when custom title is set.

- **Autoplay** (checkbox) - Automatically play the audio on page load. Note: Autoplay is blocked in most modern browsers.

- **Loop** (checkbox) - Loop the audio playback.

- **Tag** (select) - HTML tag for the audio title. Options: `p`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`. Default: `p`.

- **Preload** (select) - Audio preload behavior. Options: `none`, `metadata`, `auto`. Default: `none`.

- **Theme** (select) - Audio player color theme. Options: `light`, `dark`. Default: `light`.

:::tip[Developer reference]
See the [Audio Schema](/developer/schema/elements/audio/) for the full JSON schema of this element's settings and controls.
:::
