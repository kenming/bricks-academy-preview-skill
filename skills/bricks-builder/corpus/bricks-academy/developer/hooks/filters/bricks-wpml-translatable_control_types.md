---
title: "Filter: bricks/wpml/translatable_control_types"
description: "Add Bricks control types, including selected code fields, to WPML translation jobs."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-wpml-translatable_control_types/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-wpml-translatable_control_types.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
The `bricks/wpml/translatable_control_types` filter controls which Bricks control types WPML includes in its translation jobs.

Bricks includes `text`, `textarea`, `editor`, `repeater`, and `link` controls by default. The `code` type is excluded because automatic or manual translation can change executable PHP, JavaScript, HTML, or CSS. Add it only for fields whose complete value needs to differ between languages.

The filter applies to element controls and Page Settings. Page Settings use a synthetic element with the name `page-settings`, which lets a callback target page-level custom code without exposing every code control on the site.

## Parameters

- `$types` (array): Control types currently exposed to WPML.
- `$element` (array): The current Bricks element. For Page Settings, its `name` is `page-settings` and its `id` is `pageSettings`.
- `$control` (array|null): The current control definition.
- `$key` (string): The current control key or repeater field key.

## Translate the PHP and HTML field of Code elements

This example exposes only the `code` field of the Code element. Its CSS and JavaScript fields remain excluded.

```php
add_filter( 'bricks/wpml/translatable_control_types', function( $types, $element, $control, $key ) {
    if ( ( $element['name'] ?? '' ) === 'code' && $key === 'code' ) {
        $types[] = 'code';
    }

    return array_unique( $types );
}, 10, 4 );
```

## Translate a Page Settings custom-code field

The following callback exposes only **Page Settings → Custom code → Header scripts**. Other page-level CSS and script fields continue to use the source-language value.

```php
add_filter( 'bricks/wpml/translatable_control_types', function( $types, $element, $control, $key ) {
    $is_page_settings = ( $element['name'] ?? '' ) === 'page-settings';

    if ( $is_page_settings && $key === 'customScriptsHeader' ) {
        $types[] = 'code';
    }

    return array_unique( $types );
}, 10, 4 );
```

Available page-level custom-code keys are:

- `customCss`
- `customScriptsHeader`
- `customScriptsBodyHeader`
- `customScriptsBodyFooter`

After adding the filter, update the source page and send its translation to WPML again. The opted-in code field then appears in the WPML translation job. Review the translated value before publishing, especially when automatic translation is enabled, because a changed quote, variable, selector, or function name can break the code.
