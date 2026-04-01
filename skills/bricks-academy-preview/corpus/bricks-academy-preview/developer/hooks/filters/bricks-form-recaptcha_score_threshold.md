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
