---
title: "Action: bricks/filter_element/before_set_data_source_from_custom_field"
description: "Runs before setting the data source for a filter element that uses a custom field. This hook allows you to modify the filter element instance before the custom."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-filter_element-before_set_data_source_from_custom_field/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-filter_element-before_set_data_source_from_custom_field.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Runs before setting the data source for a filter element that uses a custom field. This hook allows you to modify the filter element instance before the custom field data is processed.

## Parameters

- `$filter_element` (*Bricks\Filter_Element*): The filter element instance.

## Example usage

```php
add_action( 'bricks/filter_element/before_set_data_source_from_custom_field', function( $filter_element ) {
    // You can access $filter_element properties here, for example:
    // $settings = $filter_element->settings;
    
    // Example: modify settings before processing
    // $filter_element->settings['customFieldKey'] = 'modified_key';
} );
```
