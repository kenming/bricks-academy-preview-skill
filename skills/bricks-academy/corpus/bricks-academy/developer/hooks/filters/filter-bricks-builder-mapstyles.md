---
title: "Filter: bricks/builder/map_styles"
description: "Filter the custom map styles available to the Bricks Map element in the builder."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-builder-mapstyles/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-builder-mapstyles.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
This filter allows you to define your own custom map styles for the **Map** element.

The example below shows how we added a custom map style from
[https://snazzymaps.com/style/38/shades-of-grey](https://snazzymaps.com/style/38/shades-of-grey) to the builder.

The best resource for professional predefined map styles is available under
[https://snazzymaps.com/explore](https://snazzymaps.com/explore). Open any map style and copy&paste the code under "JAVASCRIPT STYLE ARRAY" as shown in the example below.

```php
add_filter( 'bricks/builder/map_styles', function( $map_styles ) {
  // Example: Custom map style from: https://snazzymaps.com/style/38/shades-of-grey
  $map_styles['shadesOfGrey'] = [
    'label' => esc_html__( 'Shades of grey', 'bricks' ),
    'style' => '[ { "featureType": "all", "elementType": "labels.text.fill", "stylers": [ { "saturation": 36 }, { "color": "#000000" }, { "lightness": 40 } ] }, { "featureType": "all", "elementType": "labels.text.stroke", "stylers": [ { "visibility": "on" }, { "color": "#000000" }, { "lightness": 16 } ] }, { "featureType": "all", "elementType": "labels.icon", "stylers": [ { "visibility": "off" } ] }, { "featureType": "administrative", "elementType": "geometry.fill", "stylers": [ { "color": "#000000" }, { "lightness": 20 } ] }, { "featureType": "administrative", "elementType": "geometry.stroke", "stylers": [ { "color": "#000000" }, { "lightness": 17 }, { "weight": 1.2 } ] }, { "featureType": "landscape", "elementType": "geometry", "stylers": [ { "color": "#000000" }, { "lightness": 20 } ] }, { "featureType": "poi", "elementType": "geometry", "stylers": [ { "color": "#000000" }, { "lightness": 21 } ] }, { "featureType": "road.highway", "elementType": "geometry.fill", "stylers": [ { "color": "#000000" }, { "lightness": 17 } ] }, { "featureType": "road.highway", "elementType": "geometry.stroke", "stylers": [ { "color": "#000000" }, { "lightness": 29 }, { "weight": 0.2 } ] }, { "featureType": "road.arterial", "elementType": "geometry", "stylers": [ { "color": "#000000" }, { "lightness": 18 } ] }, { "featureType": "road.local", "elementType": "geometry", "stylers": [ { "color": "#000000" }, { "lightness": 16 } ] }, { "featureType": "transit", "elementType": "geometry", "stylers": [ { "color": "#000000" }, { "lightness": 19 } ] }, { "featureType": "water", "elementType": "geometry", "stylers": [ { "color": "#000000" }, { "lightness": 17 } ] } ]'
];

  return $map_styles;
} );
```
