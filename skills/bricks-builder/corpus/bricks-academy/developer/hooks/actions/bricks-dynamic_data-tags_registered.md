---
title: "Action: bricks/dynamic_data/tags_registered"
description: "Runs after all core dynamic data tags have been registered. This is the recommended hook for registering custom dynamic data providers or adding logic that."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-dynamic_data-tags_registered/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-dynamic_data-tags_registered.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Runs after all core dynamic data tags have been registered. This is the recommended hook for registering custom dynamic data providers or adding logic that depends on registered tags.

## Parameters

None.

## Example usage

```php
add_action( 'bricks/dynamic_data/tags_registered', function() {
    // Register custom dynamic data tags or providers here
    // Example: Bricks\Integrations\Dynamic_Data\Providers::register( 'my_custom_provider', $provider_instance );
} );
```
