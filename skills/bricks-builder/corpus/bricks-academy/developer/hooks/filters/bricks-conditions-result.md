---
title: "Filter: bricks/conditions/result"
description: "Filters the boolean result of a condition check. This filter is used to implement the logic for custom conditions or to override existing condition logic."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-conditions-result/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-conditions-result.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the boolean result of a condition check. This filter is used to implement the logic for custom conditions or to override existing condition logic.

## Parameters

- `$result` (*bool*): The result of the condition evaluation.
- `$condition_key` (*string*): The key of the condition being evaluated (e.g., `user_role`, `my_custom_condition`).
- `$condition` (*array*): The condition settings (contains `compare`, `value`, etc.).

## Example usage

```php
add_filter( 'bricks/conditions/result', function( $result, $condition_key, $condition ) {
    // Logic for custom 'is_weekend' condition
    if ( $condition_key === 'is_weekend' ) {
        $is_weekend = ( date( 'N' ) >= 6 );
        $value      = isset( $condition['value'] ) ? $condition['value'] : 'true';

        // Check if condition value matches current state
        if ( $value === 'true' ) {
            return $is_weekend;
        } else {
            return ! $is_weekend;
        }
    }

    return $result;
}, 10, 3 );
```
