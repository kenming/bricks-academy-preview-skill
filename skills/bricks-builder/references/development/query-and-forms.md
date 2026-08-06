# Query Loop and Forms

## Query Loop

Query controls vary by element, object type, integration, and Bricks version.

1. Create a minimal query in the Builder.
2. Inspect the saved query envelope and runtime query variables.
3. Search the Academy corpus for the object type and relevant hook.
4. Apply filters only to the intended element or query.
5. Test no-results, pagination/load-more, permissions, and cache behavior.

Do not assume WooCommerce or custom-field relationships are universal core object types. Feature flags and integrations can add controls and behavior.

## Forms

Form fields and submit actions are repeaters with type-specific settings. Available actions can depend on site settings and integrations.

1. Build one field/action of each required type in the UI.
2. Inspect only its generated settings.
3. Verify server-side validation/action hooks in the active version.
4. Test success, validation failure, authorization failure, upload failure, and repeated submission.

Treat all submitted values as untrusted. Sanitize by destination, validate permissions and nonces where applicable, restrict uploads, and keep credentials outside element data and public repositories.

Avoid disabling capability checks for create/update operations without an explicit security review.
