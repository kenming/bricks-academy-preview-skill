---
title: "Custom JavaScript events in Bricks"
description: "Work with Bricks custom JavaScript events so scripts can respond to builder and frontend interactions more reliably."
canonical: "https://academy.bricksbuilder.io/developer/guides/custom-javascript-events-in-bricks/"
markdownUrl: "https://academy.bricksbuilder.io/developer/guides/custom-javascript-events-in-bricks.md"
pageType: "article"
section: "developer"
category: "guides"
lastmod: "2026-08-20T13:12:40.000Z"
---
Bricks dispatches custom JavaScript events for several frontend actions. Use these events when your own scripts need to respond to Bricks forms, popups, query filters, AJAX updates, tabs, accordions, or other interactive elements.

## Form element events

- [bricks/form/submit](/builder/features/interactions/#trigger-form-submit) Emitted before an AJAX call for form submission is made.
- [bricks/form/success](/builder/features/interactions/#trigger-form-success) Emitted after a successful form submission AJAX call is returned.
- [bricks/form/error](/builder/features/interactions/#trigger-form-error) Emitted after an error in the form submission AJAX call is returned.

## Tabs / Tabs (Nestable) element events

- [bricks/tabs/changed](#bricks-tabs-changed-code): Emitted after click on a tab title (`@since 1.9.8`)

<span id="bricks-tabs-changed-code"></span>

```php
// Listen for the 'bricks/tabs/changed' event
document.addEventListener('bricks/tabs/changed', (event) => {
  // Extract information from the event detail
  const { elementId, activeIndex, activeTitle, activePane } = event.detail;

  // Only target elementID lwxvfh
  if( elementId !== 'lwxvfh' ) {
    return;
  }

  // Example: Log the details to the console
  console.log(`Tabs Changed - Element ID: ${elementId}, Active Index: ${activeIndex}, Active Title: ${activeTitle}, Active Pane: ${activePane}`);

  // Your custom logic here
  // For example, update the UI based on the tab change
});
```

## Accordion / Accordion (Nestable) element events

- [bricks/accordion/open](#bricks-accordion-open-code): Emitted after an accordion item is opened/expanded via click action (`@since 1.9.8`)
- [bricks/accordion/close](#bricks-accordion-close-code): Emitted after an accordion item is closed/collapsed via click action (`@since 1.9.8`)

<span id="bricks-accordion-open-code"></span>

```php
// Listen for the 'bricks/accordion/open' event
document.addEventListener('bricks/accordion/open', (event) => {
  // Extract information from the event detail
  const { elementId, openItem } = event.detail;

  // Only target elementID qwe3th
  if( elementId !== 'qwe3th' ) {
    return;
  }

  // Example: Log the details to the console
  console.log(`Accordion Opened - Element ID: ${elementId}, Open Item ID: ${openItem}`);

  // Your custom logic here
  // For example, update the UI based on the accordion item being opened
});

```

<span id="bricks-accordion-close-code"></span>

```php
// Listen for the 'bricks/accordion/close' event
document.addEventListener('bricks/accordion/close', (event) => {
  // Extract information from the event detail
  const { elementId, closeItem } = event.detail;

  // Only target elementID qwe3th
  if( elementId !== 'qwe3th' ) {
    return;
  }

  // Example: Log the details to the console
  console.log(`Accordion Closed - Element ID: ${elementId}, Closed Item ID: ${closeItem}`);

  // Your custom logic here
  // For example, update the UI based on the accordion item being closed
});
```

## Animation events

- [bricks/animation/end/\{animationId\}](/builder/features/interactions/#bricks-animation-end-code): Emitted when a specified animation (identified by `{animationId}`) completes its playback.

## Popup events

- [bricks/popup/open](/builder/features/popup-builder/#bricks-popup-open-close-code) Emitted after popup opened.
- [bricks/popup/close](/builder/features/popup-builder/#bricks-popup-open-close-code) Emitted after popup closed.
- [bricks/ajax/popup/start](/builder/features/popup-builder/#ajax-events) Emitted before making an AJAX popup call.
- [bricks/ajax/popup/end](/builder/features/popup-builder/#ajax-events) Emitted after completing an AJAX popup call.
- [bricks/ajax/popup/loaded](/builder/features/popup-builder/#ajax-events) Emitted after adding AJAX popup content to the DOM.

### AJAX popup open event sequence

1. bricks/ajax/popup/start
2. bricks/ajax/popup/end
3. bricks/ajax/popup/loaded
4. bricks/popup/open

## Bricks AJAX events

:::note
Bricks AJAX = Infinite Scroll, Load More, AJAX Pagination, or Query Filter.
:::

- [bricks/ajax/start](#bricks-ajax-start-code): Emitted before a Bricks AJAX call is made.
- [bricks/ajax/end](#bricks-ajax-end-code): Emitted after completing a Bricks AJAX call.
- [bricks/ajax/pagination/completed](#bricks-ajax-pagination-completed-code): Emitted after an AJAX pagination call is completed.
- [bricks/ajax/load_page/completed](#bricks-ajax-load_page-completed-code): Emitted after an Infinite scroll AJAX call is completed.
- [bricks/ajax/query_result/completed](#bricks-ajax-query_result-completed-code): Emitted after a Query filter AJAX call is completed.
- [bricks/ajax/nodes_added](#bricks-ajax-nodes_added-code): Emitted after Bricks adds new AJAX result nodes to the DOM. The event detail contains the `queryId`. (`@since 1.11.1`)
- [bricks/ajax/query_result/displayed](#bricks-ajax-query_result-displayed-code): Emitted after adding all filtered results to the DOM.
- [bricks/filter/submit/start](#bricks-filter-submit-start-code): Emitted when a Filter - Submit element starts an AJAX filter submission. The event detail contains the `queryId` and `filterId`. (`@since 2.4`)
- [bricks/filter/submit/end](#bricks-filter-submit-end-code): Emitted when a Filter - Submit AJAX filter submission finishes. The event detail contains the `queryId` and `filterId`. (`@since 2.4`)

### Infinite scroll event sequence

1. bricks/ajax/start
2. bricks/ajax/nodes_added
3. bricks/ajax/end
4. bricks/ajax/load_page/completed

### AJAX pagination event sequence

1. bricks/ajax/start
2. bricks/ajax/nodes_added
3. bricks/ajax/end
4. bricks/ajax/pagination/completed

:::note
The `bricks/ajax/pagination/completed` event is only emitted for standalone AJAX pagination. If the Pagination element targets a query that uses Bricks Query Filters, this event is not emitted. In this case, listen for the Query Filter events instead.
:::

### AJAX query filter event sequence

1. bricks/ajax/start
2. bricks/ajax/end
3. bricks/ajax/query_result/completed
4. bricks/ajax/nodes_added
5. bricks/ajax/query_result/displayed

### Filter submit event sequence

The `bricks/filter/submit/start` and `bricks/filter/submit/end` events are specific to the Filter - Submit element. They run only for AJAX filter submissions that refresh the current page results. They are not emitted when the Submit element redirects to another URL.

1. bricks/filter/submit/start
2. bricks/ajax/start
3. bricks/ajax/end
4. bricks/ajax/query_result/completed
5. bricks/ajax/nodes_added
6. bricks/ajax/query_result/displayed
7. bricks/filter/submit/end

Use these events when your script should react only to a deliberate submit action, not to every query filter AJAX request.



<span id="bricks-ajax-start-code"></span>

```php
document.addEventListener('bricks/ajax/start', (event) => {
  // Get the queryId from the event
  const queryId = event.detail.queryId || false;

  if (!queryId) {
    return;
  }

  // Your custom logic here
  // For example, initiate a loader or update UI to indicate AJAX request start
});
```



<span id="bricks-ajax-end-code"></span>

```php
document.addEventListener('bricks/ajax/end', (event) => {
  // Get the queryId from the event
  const queryId = event.detail.queryId || false;

  if (!queryId) {
    return;
  }

  // Your custom logic here
  // For example, initiate a loader or update UI to indicate AJAX request end
});
```



<span id="bricks-ajax-pagination-completed-code"></span>

```php
document.addEventListener('bricks/ajax/pagination/completed', (event) => {
  // Extract queryId from the event detail
  const queryId = event.detail.queryId;

  // Your custom logic here
  // For example, handle the completed pagination for the specific queryId
});
```



<span id="bricks-ajax-load_page-completed-code"></span>

```php
document.addEventListener('bricks/ajax/load_page/completed', (event) => {
  // Extract information from the event detail
  const { queryTrailElement, queryId } = event.detail;

  // Your custom logic here
  // For example, handle the completed AJAX page load for the specific queryId and queryTrailElement
});
```



<span id="bricks-ajax-query_result-completed-code"></span>

```php
document.addEventListener('bricks/ajax/query_result/completed', (event) => {
  // Extract information from the event detail
  const queryId = event.detail.queryId;

  // Your custom logic here
});
```



<span id="bricks-ajax-nodes_added-code"></span>

```php
document.addEventListener('bricks/ajax/nodes_added', (event) => {
  // Extract queryId from the event detail
  const queryId = event.detail.queryId;

  // Your custom logic here
  // For example, initialize scripts that need the new AJAX result nodes to exist first
});
```



<span id="bricks-ajax-query_result-displayed-code"></span>

```php
document.addEventListener('bricks/ajax/query_result/displayed', (event) => {
  // Extract information from the event detail
  const queryId = event.detail.queryId;

  // Your custom logic here
});
```



<span id="bricks-filter-submit-start-code"></span>

```php
document.addEventListener('bricks/filter/submit/start', (event) => {
  const { queryId, filterId } = event.detail;

  // Only react to the Filter - Submit element with Bricks ID xnueeh
  if (filterId !== 'xnueeh') {
    return;
  }

  // Your custom logic here
});
```



<span id="bricks-filter-submit-end-code"></span>

```php
document.addEventListener('bricks/filter/submit/end', (event) => {
  const { queryId, filterId } = event.detail;

  // Only react to the target query with Bricks ID kpmnav
  if (queryId !== 'kpmnav') {
    return;
  }

  // Your custom logic here
});
```

## Mega menu events

- [bricks/megamenu/repositioned](#bricks-megamenu-repositioned-code): Emitted after a mega menu submenu is repositioned on the frontend. The event detail contains the `menuItem` and `submenu`. (`@since 2.0`)

<span id="bricks-megamenu-repositioned-code"></span>

```php
document.addEventListener('bricks/megamenu/repositioned', (event) => {
  const { menuItem, submenu } = event.detail;

  // Your custom logic here
  // For example, update third-party scripts inside the repositioned submenu
});
```
