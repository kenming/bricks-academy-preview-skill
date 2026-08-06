---
title: "Blog post template"
description: "Create a Bricks blog post template that pulls in post content, metadata, and featured media with dynamic data."
canonical: "https://academy.bricksbuilder.io/getting-started/blog-post-template/"
markdownUrl: "https://academy.bricksbuilder.io/getting-started/blog-post-template.md"
pageType: "article"
section: "getting-started"
category: "blog-post-template"
lastmod: "2026-08-04T12:13:33.000Z"
---
https://youtu.be/d0i85-tgjAQ

## Before you begin: sample posts

You need **at least one published blog post** to preview this template (more is better). If you already created **3 test posts with featured images** for [Query loops and dynamic data](/getting-started/query-loops-dynamic-data/), you are set.

Otherwise:

1. Go to **Posts > Add New**
2. Add a title, body content in the block editor, and a **featured image**
3. Click **Publish**

Your homepage shows a grid of posts. When you click one, you see the default WordPress template (pretty basic). Let's create a proper blog post template.

## What is a single template?

Remember in the intro to templates article when we talked about different template types? **Single** templates control the layout of individual blog posts or pages.

For blog posts, we separate design from content:
- **Design** (layout, styles) = Bricks template
- **Content** (post text, images) = WordPress block editor

This way, if you need a new design later, you just change the template without recopying all your content.

## Create the template

1. Go to **Bricks > Templates** in WordPress dashboard
2. Click **Add New**
3. Title it: "Blog Post"
4. Click **Edit with Bricks**


### Set template type and conditions

Before building, let's configure where this applies:

1. Click **Settings** (gear icon) in toolbar
2. Go to **Template Settings**
3. Set **Template Type** to `Single`
4. Under **Template Conditions**, click **Add Condition**
5. Select **Post type: Posts**
6. Add at least one element to the template, e.g. the post title element

This template now applies to all blog posts.

### Test it's working

Save the template, then open one of your test blog posts on the front end. You'll see that the page contains only the element you added. Perfect! That means our template is applied, but still incomplete.

## Build the template with a wireframe

Instead of building from scratch (which you certainly can do), let's use a wireframe template. This is also a great way to learn.

1. Click **Templates** (folder icon) in toolbar
2. Set **Source** to **Wireframes**
3. Filter by **Template Type**: select `Single`
4. Find "Article 01" (or similar)
5. Click **Insert**


When prompted to import global classes, theme styles, and color palette, click "Yes" to all.

:::note[What you are importing]
Saying **yes** here can add **reusable design assets** to your site, not just layout: **global classes**, **theme styles**, and **color palette** entries. That is normal for wireframes, but it means your site may gain styles and colors you did not build by hand yet. If you prefer to keep the site minimal, build the template yourself instead of inserting the wireframe, or skip importing these assets and style the template manually later.
:::

These assets are what make the wireframe look polished out of the box. We'll explain global classes and theme styles in upcoming articles.

:::warning[Post Content is required for the post body]
If the template does not include a **Post Content** element, the text you write in the WordPress editor will **not** appear on the front end. After you insert the wireframe, confirm a **Post Content** element exists in the structure (see [The Post Content element](#the-post-content-element) below).
:::

The wireframe inserts with a complete blog post layout!


## Examine the template

One of the best ways to learn is by looking at how someone else built something. With wireframe templates, feel free to move things around, break it, try to put it back together. If you're having trouble, just delete and re-insert!

Let's examine what we have.

### Look at the Structure Panel


You'll see sections with various elements: headings, text, images, and more.

### Notice the curly braces

See text like `{post_title}`, `{featured_image}`, `{post_date}`?

These are **dynamic data tags** - the same ones we used in the query loop!

But now they're in a different **context**.

## Understanding context

Context matters in dynamic data.

**In the query loop** (homepage): As you loop through posts, the context changes for each card. First card = post #1, second card = post #2, etc.

**In the single template**: The context is the post you're currently viewing. `{post_title}` shows the title of whatever post the visitor is on.

This is what makes templates + dynamic data so powerful. One template, infinite posts, each showing its own content.

### Key elements in the template

Look for these important elements:

**Heading with `{post_title}`** - Displays the post's title

**Image element with featured image** - Shows the post's featured image (using `{featured_image}` dynamic data)

**Post Content element** - This special element displays the actual post content you write in the WordPress block editor

**Meta data** - Author, date, categories (using tags like `{author_name}`, `{post_date}`, `{post_terms_category}`)


## The Post Content element

This element is special. It renders whatever you write in the WordPress block editor (the default WordPress editor when you create a post).

**Why keep content in WordPress editor?**

- **Content portability** - If you switch themes, content stays intact
- **Client-friendly** - Non-technical users already know this editor
- **Plugin compatibility** - SEO plugins, table of contents, etc. expect content there
- **Separation of concerns** - Design in Bricks, content in WordPress

Bricks handles the layout. WordPress handles the written content. Keep them separate: you still create and edit your posts in the normal WordPress editor, Bricks just controls how that content is presented.

## View on the front end

Open one of your test posts on the front end. Your template is now applied, and dynamic data shows that post's specific content!


Click another post. Same template, different content. Magic!

## Customize your template

Want to make changes?

1. Go to **Bricks > Templates**
2. Find "Blog Post"
3. Click **Edit with Bricks**
4. Modify colors, spacing, fonts
5. Save

All posts update automatically. One template, all posts. Change once, update everywhere.

:::tip[Try it]
Edit your blog post template. Change heading colors, adjust spacing, or rearrange elements. Save and view different posts on the front end. They all use your updated design. Add a new test post in WordPress — it automatically uses your template. This is the efficiency of templates!
:::

## What you've learned

You can now:
- Create single post templates
- Set template types and conditions
- Use wireframe templates to learn and speed up building
- Understand dynamic data context
- Use the Post Content element
- Separate design (Bricks) from content (WordPress)
- Customize templates that apply to all posts
