---
title: "Filter: bricks/frontend/render_element"
description: "The bricks/frontend/renderelement filter allows you to modify the HTML output of any element in Bricks on the frontend. This powerful hook can be used for a."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-frontend-render_element/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-frontend-render_element.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
The `bricks/frontend/render_element` filter allows you to modify the HTML output of any element in Bricks on the frontend. This powerful hook can be used for a variety of customization tasks, such as adding comments, modifying content, or dynamically adjusting HTML. (@since 2.0)

```php
add_filter( 'bricks/frontend/render_element', function( $html, $element ) {
    // Do not modify the HTML in the builder
    if (
        bricks_is_builder_main() ||
        bricks_is_builder_iframe() ||
        bricks_is_builder_call()
    ) {
        return $html;
    }

    // Add comments before and after an element with a specific ID
    if ( $element->id === 'regxve' ) {
        $html = '<!-- Start of the element -->' . $html . '<!-- End of the element -->';
    }

    // Modify the content of a Basic Text element
    if ( $element->id === 'wtktgp' ) {
        // Replace "|" with ">>" in the HTML
        $html = str_replace( '|', '>>', $html );
    }

    return $html;
}, 10, 2 );

```
