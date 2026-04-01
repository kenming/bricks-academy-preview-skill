Bricks offers a range of custom JavaScript events that you can leverage to enhance the functionality and interactivity of your website. These events allow you to respond to specific actions or changes within your Bricks-powered site. Let's explore the custom events available in Bricks:

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
- [bricks/ajax/query_result/displayed](#bricks-ajax-query_result-displayed-code): Emitted after adding all filtered results to the DOM.

### Infinite scroll event sequence

1. bricks/ajax/start
2. bricks/ajax/end
3. bricks/ajax/load_page/completed

### AJAX pagination event sequence

1. bricks/ajax/start
2. bricks/ajax/end
3. bricks/ajax/pagination/completed

### AJAX filter event sequence

1. bricks/ajax/start
2. bricks/ajax/end
3. bricks/ajax/query_result/completed
4. bricks/ajax/query_result/displayed



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



<span id="bricks-ajax-query_result-displayed-code"></span>

```php
document.addEventListener('bricks/ajax/query_result/displayed', (event) => {
  // Extract information from the event detail
  const queryId = event.detail.queryId;

  // Your custom logic here
});
```
