The specificity of default Bricks styles has always been a balancing act. While we aim to keep these styles as non-intrusive as possible, providing a blank canvas for users to build upon, achieving this solely through selector specificity has its limitations. In some cases, it’s been challenging for users to override specific selectors, even when desired.

Bricks 1.12 introduces a promising solution to this longstanding issue through [CSS cascade layers](https://developer.mozilla.org/en-US/docs/Web/CSS/@layer), which as of December 2024 reach an impressive 96% browser support and "Widely available" Baseline.

Since Bricks 2.0, this feature has been **enabled by default**. You can disable it from **Bricks Settings > Performance > Cascade layer**, though it is not recommended.

This feature leverages cascade layers to define how Bricks' default styles interact with other styles on the page.

## How it works

This feature introduces **two cascade layers**:

- **`bricks.reset`** (a lower-priority layer): This sublayer is empty, providing a safety net for advanced users. Bricks itself does not apply any styles in this layer.
- **`bricks`**: This layer contains all of Bricks' default styles, making them easier to override using un-layered styles or styles in higher-priority user-defined layers.

Here’s an example to illustrate the problem and the solution:

### The problem: Selector specificity

In the default Bricks styles, a common pattern might look like this:

```php
[class*="brxe-"] {
    max-width: 100%;
}
```

If you tried to override this with a general element selector, such as:

```php
div {
    max-width: 400px;
}
```

…the override wouldn't work because the attribute selector `[class*="brxe-"]` has a higher specificity then the `div`.

One potential workaround could be wrapping Bricks' attribute selectors in `:where()` to reduce specificity:

```php
:where([class*="brxe-"]) {
    max-width: 100%;
}
```

However, this approach would require wrapping every selector, which is not only complex but also impractical at scale.

### The solution: Cascade layers

With cascade layers, we can simply define the default styles within a layer named `bricks`.

Styles outside this layer (un-layered) or in a higher-priority layer automatically precede the default Bricks styles.

Here's how the layers are structured:

```php
@layer bricks.reset;

@layer bricks {
    [class*="brxe-"] {
        max-width: 100%;
    }
    /* Other default Bricks styles */
}
```

Now, when you add your own styles outside the `bricks` layer, like this:

```php
div {
    max-width: 400px;
}
```

…they will precede the default Bricks styles because un-layered styles and higher-priority layers take precedence, regardless of the selector.

### The role of `bricks.reset` {#bricks-reset}

The `bricks.reset` sublayer ensures flexibility when overriding default Bricks styles.

Normally, styles in the `bricks` layer are easy to override, but if a default style uses `!important`, the cascade order flips, making it harder to override with un-layered styles or higher-priority layers. You can learn more about this behaviour [here](https://css-tricks.com/css-cascade-layers/#aa-establishing-a-layer-order).

The `bricks.reset` layer, being lower priority, provides a fallback for safely defining custom styles in these rare cases. While we aim to avoid using `!important` in our default styles unless absolutely required, this sublayer is there as a safeguard.

## Why this matters

By moving default Bricks styles into a dedicated cascade layer, we ensure:

1. **Easier overrides**: Un-layered or higher-priority layered styles can override the default Bricks styles without battling selector specificity.
2. **Simplified maintenance**: Instead of manually tweaking every selector's specificity, cascade layers offer a clean, scalable solution.

## Resources

- **Kevin Powell's YouTube video on cascade layers**: [A look at CSS Cascade Layers](https://www.youtube.com/watch?v=NDNRGW-_1EE)
- **In-depth guide on CSS cascade layers**: [CSS-Tricks: Cascade Layers Guide](https://css-tricks.com/css-cascade-layers/)
