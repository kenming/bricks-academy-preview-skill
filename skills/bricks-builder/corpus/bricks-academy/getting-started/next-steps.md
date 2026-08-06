---
title: "Next steps"
description: "See the most useful next steps after the Academy starter build, including where to deepen your Bricks, styling, and template skills."
canonical: "https://academy.bricksbuilder.io/getting-started/next-steps/"
markdownUrl: "https://academy.bricksbuilder.io/getting-started/next-steps.md"
pageType: "article"
section: "getting-started"
category: "next-steps"
lastmod: "2026-08-04T12:13:33.000Z"
---
https://youtu.be/yC2GZxZP6tc

You've made it through the essentials! You can now build professional WordPress sites with Bricks. But this is just the foundation. Bricks includes powerful advanced features you haven't touched yet.

This article maps out what's next. For each feature, you'll learn:
- **What it is** - Clear explanation
- **Why it matters** - Real-world benefits
- **When you'll need it** - What problems it solves
- **Where to learn more** - Links to detailed guides

You don't need to learn everything at once. Build projects, encounter challenges, then learn the features that solve those specific problems. This is how you master Bricks naturally.

## How to best learn Bricks

**Don't try to memorize everything**. Instead:

1. **Build real projects** - Personal site, client work, passion projects
2. **Encounter problems** - "I need consistent CTAs across 20 pages..." or "This accordion needs to work everywhere..."
3. **Learn the solution** - "Ah, Components solve this!"
4. **Apply it** - Build it, break it, understand it
5. **Repeat** - Each project teaches something new

You'll master Bricks by using it, not by reading about it. These resources exist when you need them.

## Advanced features roadmap

### Components

**What it is:** Reusable elements that sync across your entire site. Create a card design once, use it everywhere. Update the component, and every instance updates automatically.

**Why it matters:** Ensures consistency and speeds up maintenance. Need to change button colors on 50 cards? Edit one component instead of 50 individual cards.

**When you'll need it:**
- Building card layouts used across multiple pages
- Creating reusable CTAs, testimonials, or team member cards
- When you find yourself copying and pasting the same design repeatedly

**Key difference from templates:** Templates control entire page layouts. Components control individual elements or small groups of elements. Use components for repeating design elements, templates for page structure.

**Where to learn more:** [Components documentation](/builder/features/components/)

### Style Manager

**What it is:** The central hub for managing your site's design system. Opened via the **Styles** icon in the toolbar or `Cmd/Ctrl + .`, it organizes theme styles, classes, CSS variables, colors, typography scales, spacing scales, and framework settings into a single interface.

**Why it matters:** Instead of hunting through different panels, you manage all your design tokens and reusable styles in one place. Define a color palette, set up fluid typography, create spacing scales, and manage classes — all from the same popup.

**When you'll need it:**
- Managing design tokens (colors, spacing, typography) across large sites
- Client sites where brand colors might change
- When you want more flexibility than theme styles offer
- Setting up a consistent design system from the start

**Combines with:** Theme styles and global classes. The Style Manager is where you define variables, classes, and scales — then reference them throughout your designs.

**Where to learn more:** [Style Manager documentation](/builder/features/style-manager/)

### Element interactions

**What it is:** Trigger actions (show/hide elements, toggle classes, start animations) based on user events (click, hover, scroll, form submit).

**Why it matters:** Create interactive experiences without writing JavaScript. Build accordions, tabs, modals, animated reveals, and more visually.

**When you'll need it:**
- Building custom accordions or tabs
- Creating show/hide functionality
- Adding scroll-triggered animations
- Opening popups on button clicks

**Examples:**
- Click a button → Show a hidden div
- Hover over an image → Fade in caption
- Scroll to element → Trigger animation
- Form submission → Show success message

**Where to learn more:** [Interactions documentation](/builder/features/interactions/)

### Element conditions

**What it is:** Show or hide elements based on conditions (user role, custom field value, query string, date, etc.).

**Why it matters:** Create dynamic layouts that adapt to context. Show admin-only content to logged-in admins. Display sale banners only during promotion periods. Show different CTAs based on custom field values.

**When you'll need it:**
- Membership sites (show content based on user role)
- Conditional pricing (show special offers to specific users)
- Dynamic templates (display different layouts based on post meta)
- A/B testing (show different versions based on query parameters)

**Powerful combination:** Element conditions + dynamic data + query loops = incredibly flexible templates.

**Where to learn more:** [Element Conditions documentation](/builder/features/element-conditions/)

### External APIs and custom integrations

**What it is:** Pull data from external services (weather APIs, stock tickers, social media feeds, custom databases) and display it in Bricks.

**Why it matters:** Connect your site to any service with an API. Display real-time data, integrate with third-party platforms, or build custom dashboards.

**When you'll need it:**
- Displaying live data (weather, currency rates, stock prices)
- Integrating with CRMs or custom systems
- Building complex dashboards

**Requires:** Some PHP knowledge to fetch and format API data, then use dynamic data to display it.

**Where to learn more:** [Dynamic Data API integrations documentation](/builder/dynamic-content/dynamic-data/)

### Query filters (advanced)

**What it is:** Real-time AJAX filtering for query loops. Users can search, filter by category, adjust price ranges, and sort results without page reloads.

**Why it matters:** Creates powerful, interactive search and filter experiences. Essential for e-commerce, directories, and large content libraries.

**When you'll need it:**
- WooCommerce shops (filter products by category, price, attributes)
- Directories (search and filter team members, locations, services)
- Large blogs (filter posts by category, tag, date)

**Available filters:**
- Live search
- Checkboxes (categories, tags, custom taxonomies)
- Radio buttons
- Select dropdowns
- Range sliders (price, dates)
- Date pickers

**Where to learn more:** [Query Filters documentation](/builder/dynamic-content/query-filters/)

### WooCommerce builder

**What it is:** Dedicated elements and templates for building custom WooCommerce shops. Complete control over product layouts, shop pages, cart, checkout, and account pages.

**Why it matters:** Default WooCommerce templates are generic. With Bricks, you design every aspect of the shopping experience to match your brand.

**When you'll need it:**
- Building e-commerce sites
- Customizing product pages beyond what themes offer
- Creating unique shop layouts

**Includes:**
- Product elements (price, add to cart, images, galleries, tabs)
- Shop templates (product archives, single products, cart, checkout)
- WooCommerce dynamic data tags
- Query filters for products

**Where to learn more:** [WooCommerce Builder documentation](/integrations/woocommerce/woocommerce-builder/)

### Custom code and hooks

**What it is:** Extend Bricks with your own PHP, CSS, and JavaScript. Use WordPress hooks to modify Bricks behavior programmatically.

**Why it matters:** When visual tools reach their limits, code gives you infinite flexibility. Build custom functionality, integrate with plugins, or create unique features.

**When you'll need it:**
- Adding custom functionality beyond Bricks' GUI
- Integrating with custom plugins or systems
- Building highly specialized templates

**Requires:** PHP, JavaScript, and WordPress development knowledge.

**Where to learn more:** [Hooks and Filters documentation](/developer/hooks/filters/)

### Popups

**What it is:** Build custom modals and popups that appear on any trigger (click, scroll, exit intent, time delay, etc.).

**Why it matters:** Create newsletter signups, promotional offers, video modals, login forms, or any overlay content with complete design control.

**When you'll need it:**
- Newsletter signup popups
- Video lightboxes
- Exit-intent offers
- Terms and conditions modals
- Custom login/register forms

**Combines with:** Interactions to control when and how popups appear.

**Where to learn more:** [Popups documentation](/builder/features/popup-builder/)

### Font manager

**What it is:** Upload and manage custom fonts (self-hosted or from services) directly in Bricks. Organize font families, weights, and styles.

**Why it matters:** Use any font you want, not just Google Fonts. Better performance with self-hosted fonts. Complete control over typography.

**When you'll need it:**
- Using brand-specific fonts
- Optimizing performance by self-hosting fonts
- Accessing fonts not available on Google Fonts

**Where to learn more:** [Font Manager documentation](/builder/styling/font-manager/)

### Keyboard shortcuts

**What it is:** Speed up your workflow with keyboard shortcuts for common actions.

**Why it matters:** Professionals use shortcuts. They're faster than clicking through menus repeatedly.

**Common shortcuts:**
- `Cmd/Ctrl + K` - Command panel (search elements, actions)
- `Cmd/Ctrl + D` - Duplicate selected element
- `Cmd/Ctrl + Z` - Undo
- `Cmd/Ctrl + Shift + Z` - Redo
- `Cmd/Ctrl + B` - Toggle responsive breakpoints
- `Delete` - Delete selected element

**When you'll need it:** Every project. Learn shortcuts gradually as you work.

**Where to learn more:** [Keyboard Shortcuts documentation](/builder/interface/keyboard-shortcuts/)

## Learning path by site type

Different projects need different features. Here's what to prioritize:

### Building a blog or content site

**Priority features:**
1. Dynamic data and query loops (essential)
2. Templates (single post, archive)
3. Theme styles (consistent typography)
4. Search functionality (query filters)

**Nice-to-haves:**
- Components (for reusable post cards)
- Popups (newsletter signups)
- Interactions (animated reveals)

### Building an e-commerce site

**Priority features:**
1. WooCommerce builder
2. Query loops (product grids)
3. Query filters (product filtering)
4. Templates (product pages, shop pages)

**Nice-to-haves:**
- Components (reusable product cards)
- Interactions (quick view modals)
- Popups (sale announcements)

### Building a business/portfolio site

**Priority features:**
1. Theme styles (brand consistency)
2. Global classes (reusable styles)
3. Components (team members, testimonials)
4. Templates (service pages, case studies)

**Nice-to-haves:**
- Interactions (portfolio galleries)
- Element conditions (role-based content)
- Popups (contact forms)

### Building a membership/community site

**Priority features:**
1. Element conditions (restrict content by role)
2. Templates (member profiles, directories)
3. Dynamic data (user-specific content)
4. Query loops (member lists)

**Nice-to-haves:**
- Custom code (advanced restrictions)
- Interactions (member dashboard features)

## Your next project

The best way to solidify what you've learned:

**Build a complete site from scratch.** Include:
- A homepage (static design)
- A blog with posts (template + dynamic data + query loop)
- An about page
- A contact page
- Header and footer templates

This project touches everything you've learned and prepares you for client work.

**Tips:**
- Start with wireframes or sketches
- Use theme styles from the beginning
- Create global classes for common patterns
- Test responsive behavior as you build
- Preview frequently on actual devices

## Community and resources

You're not alone in learning Bricks:

**Official resources:**
- [Bricks Academy](https://academy.bricksbuilder.io) - Comprehensive documentation
- [Bricks YouTube Channel](https://youtube.com/bricksbuilder) - Video tutorials
- [Bricks Changelog](https://bricksbuilder.io/changelog) - New features and updates

**Community:**
- [Bricks Facebook Group](https://facebook.com/groups/bricksbuilder) - Active community, Q&A
- [Bricks Forum](https://forum.bricksbuilder.io) - Official support forum

**Pro tip:** When you encounter issues, search the forum first. Most problems have been solved by the community already.

## A final word

You've completed the getting started series. You now have the foundational knowledge to build professional WordPress sites with Bricks.

But mastery doesn't come from reading. It comes from building, breaking, fixing, and building again. Each project teaches you something new. Each challenge reveals a feature you didn't know you needed.

**Start building.** The best learning happens when you're solving real problems.

**Don't aim for perfection.** Your first sites won't be masterpieces. That's normal. Every professional started where you are now.

**Stay curious.** When you see a site with a cool feature, ask yourself: "How would I build that in Bricks?" Then try building it.

**Enjoy the process.** Bricks is a powerful tool, but it's also fun. You're building websites visually, seeing changes instantly, and bringing ideas to life. That's pretty awesome.

Welcome to the Bricks community. We're excited to see what you build.

Now go make something great.
