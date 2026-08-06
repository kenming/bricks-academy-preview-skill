---
title: "Filter: bricks/form/recaptcha_score_threshold"
description: "Filters the minimum score required for Google reCAPTCHA v3 validation in Bricks forms. Scores range from 0.0 (likely a bot) to 1.0 (likely a human)."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-form-recaptcha_score_threshold/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-form-recaptcha_score_threshold.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the minimum score required for Google reCAPTCHA v3 validation in Bricks forms. Scores range from 0.0 (likely a bot) to 1.0 (likely a human).

## Parameters

- `$score` (*float*): The minimum score threshold. Default is `0.5`.

## Example usage

```php
add_filter( 'bricks/form/recaptcha_score_threshold', function( $score ) {
    // Increase threshold to 0.8 for stricter validation
    return 0.8;
} );
```
