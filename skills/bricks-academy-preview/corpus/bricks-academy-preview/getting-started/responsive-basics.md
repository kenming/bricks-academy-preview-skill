Earlier in the series we focused on building on desktop first, without worrying about smaller screens. Now it is time to take that same page and make it work everywhere.

Over half your visitors use phones or tablets. Responsive design means your layouts adjust gracefully to any screen size. This article covers how Bricks handles that.

## Understanding breakpoints

Breakpoints are screen width thresholds where your design adapts. Bricks includes four defaults:

| Breakpoint | Screen width | What it targets |
| --- | --- | --- |
| Desktop | Base (no limit) | Laptops, large monitors |
| Tablet portrait | < 992px | iPads, tablets |
| Mobile landscape | < 768px | Phones in landscape |
| Mobile portrait | < 478px | Phones in portrait |

Click the device icons in the toolbar to switch between breakpoints. The canvas resizes to show you what users on that screen size will see.

**How inheritance works:** Styles you set on Desktop apply to all breakpoints automatically. When you switch to a smaller breakpoint and change a value, that change applies to that breakpoint and anything smaller. You only override what needs to change — you do not redefine everything from scratch.

For example: set a Container's direction to `Row` on Desktop. Switch to Mobile landscape and change it to `Column`. Desktop and Tablet stay side-by-side. Mobile landscape and portrait stack vertically.

Bricks uses desktop-first by default (design large, refine smaller). Most users stick with this since it is easier to think "scale down" than "scale up."

## The responsive workflow

Let's make the hero section we built earlier responsive.

### 1. Check tablet

Click the **Tablet portrait** icon in the toolbar and look at your design. Common things to check:

- Does the two-column layout still feel comfortable, or does it feel cramped?
- Is the padding still proportional to the screen size?

### 2. Adjust spacing

Your Section has 80px padding. On tablets that is a lot of vertical space.

1. Select the Section
2. Make sure you are on the **Tablet portrait** breakpoint
3. Change **Padding** top/bottom to `60`

Desktop keeps 80px. Tablet and smaller use 60px.

### 3. Switch to mobile and stack the columns

On a phone, the two-column hero (text left, image right) is too cramped. Let's stack it.

1. Click **Mobile landscape** in the toolbar
2. Select the **Container** inside the hero section
3. Under **Layout**, change **Direction** from `Row` to `Column`

The text and image now stack vertically on mobile. Desktop and tablet stay side-by-side. This is the most common responsive technique: horizontal on large screens, vertical on small.

### 4. Check mobile portrait

Click **Mobile portrait** for the smallest view. Reduce padding a bit further if needed (around `32`). Check that buttons are large enough to tap comfortably.

## Hiding elements on specific breakpoints

Sometimes you want an element visible on desktop but hidden on mobile.

1. Select the element
2. Switch to the breakpoint where it should disappear
3. Under **Layout**, set **Display** to `None`

The element hides at that breakpoint and smaller, stays visible everywhere else.

## Two approaches to handling values across screen sizes

So far we have been manually setting a value (like `60px` padding) at each breakpoint. This works well for layout decisions like stacking columns or adjusting spacing.

But there is a second approach, especially useful for things like font sizes and spacing scales: instead of picking specific values at each breakpoint, you define a minimum and a maximum and let the browser smoothly calculate everything in between based on screen width. No breakpoints needed for those values at all.

For example: a heading that is always at least 24px on the smallest screen and never more than 48px on the widest. Between those two extremes, it scales automatically.

Bricks has this built in. The **Style Manager** (the same popup you used for Theme Styles) has dedicated **Typography** and **Spacing** tabs where you can generate these fluid scales as CSS variables. You set up the scale once, apply the variables to your elements, and responsiveness for those values is handled automatically.

This is a more advanced topic and not something you need right now. But it is worth knowing the two approaches exist:

- **Hard values at each breakpoint** — explicit, manual, great for layout
- **Fluid scaling** — define a range, let the browser do the math, great for typography and spacing

For a deeper look: [Fluid Typography](/builder/styling/fluid-typography)

## Testing your design

The builder canvas gives you a preview, but always test on real devices or browser dev tools.

**In the builder:** Use the breakpoint switcher. You can also drag the canvas edges to check intermediate widths.

**In the browser:**
1. Click **Preview** in the toolbar to open the front end
2. Open browser dev tools (`F12` or `Cmd/Ctrl + Shift + I`)
3. Enable **Responsive Design Mode**
4. Test at various widths

Real device testing reveals things emulation misses — touch target size, actual font legibility, performance on slower phones.

## Custom breakpoints

Bricks' four defaults cover most sites. If you need a breakpoint at a specific width (say, a wide desktop at 1440px), you can add one.

Go to **Bricks > Settings > General**, enable **Custom breakpoints**, then add them from the breakpoint manager in the builder.

## Troubleshooting

**Changes on mobile are not showing on the front end.**
Save the page, then hard-refresh the browser (`Cmd/Ctrl + Shift + R`).

**Styles I set on desktop are changing when I switch breakpoints.**
You likely overrode them on a smaller breakpoint earlier. Inheritance goes downward only — changes on mobile do not affect desktop.

**Layout breaks at a width between two breakpoints.**
Test widths like 850px (between Tablet 992px and Mobile landscape 768px). If something breaks there, either adjust your layout to be more flexible or add a custom breakpoint.

## What you've learned

- How breakpoints work and how styles inherit downward
- How to adjust spacing and stack columns on smaller screens
- How to hide elements on specific breakpoints
- The two approaches to responsive values: hard breakpoint overrides vs. fluid scaling
- How to test your design across screen sizes
