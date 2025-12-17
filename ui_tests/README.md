# TEST CASE 1 - LOGO VERIFICATION

## Test Case Objective

The goal of this test case is to validate that the website logo is displayed, ensuring branding is correctly rendered for the user.

## Key Observations

### 1. Purpose of the test case

The test case checks if the logo is present and visible on the page.

### 2. Locator strategy used

A CSS selector is used to locate the logo image element efficiently.

### 3. Handling multiple images

The page contains multiple `<img>` elements. Using `:first-of-type` ensures that the test selects the intended logo image rather than other decorative images.

### 4. Targeting the correct element

The selector navigates through the sticky header section to find the correct logo element in a structured and reliable way.

### 5. Optimizing the CSS selector

Initially, auto-generated selectors were lengthy and complex. The final CSS selector is simplified and precise, making it more maintainable.

### 6. Performing the visibility check

Selenium’s `is_displayed()` method checks whether the logo is actually visible to the user on the page.

### 7. Reporting results for success

If the logo is displayed, the test prints a confirmation message and the test case is considered passed.

### 8. Reporting results for failure

If the logo is not displayed, the test prints a failure message, indicating that the test case did not pass.

---

# TEST CASE 2 - NAVIGATION

## Test Case Objective

The goal of this test is to validate that a user can successfully navigate away from the current page by clicking the **“LET’S TALK”** call-to-action button, using reliable waits and safe URL verification.

## Key Observations:

### 1. Purpose of the test case

The test case verifies the navigation flow of the application by ensuring that clicking a specific button leads to a page change.

### 2. Target UI element

The test focuses on a button visually labeled **“LET’S TALK”**, which is intended to trigger navigation.

### 3. Locator strategy used

A CSS selector (`span.elementor-button-text`) is used to locate all button text elements rendered by the Elementor framework.

### 4. Collecting multiple elements

Since multiple buttons share the same class, all matching elements are collected into a list instead of targeting a single element directly.

### 5. Filtering the correct button

A `for` loop iterates through the list of elements, extracting and evaluating the visible text of each button to identify the intended one.

### 6. Handling special characters in text

The button label contains a curly apostrophe (`’`) instead of a standard ASCII apostrophe (`'`), which can make exact string matching unreliable.

### 7. Avoiding brittle text matching

To prevent failures due to character encoding differences, the test avoids matching the full button text exactly.

### 8. Using partial text matching

The keyword **“talk”** is used (case-insensitive) to reliably identify the correct button regardless of special characters.

### 9. Understanding DOM hierarchy

The visible text is contained within a `<span>` element that is nested inside the actual clickable element.

### 10. Navigating to the clickable parent

The script moves up the DOM hierarchy to reach the grandparent element that represents the clickable button container.

### 11. Performing the click action

Once the correct clickable parent element is identified, Selenium performs a click operation to trigger navigation.

### 12. Using explicit wait instead of `time.sleep()`

Instead of using a fixed delay, the test uses Selenium’s `WebDriverWait` to wait until the URL changes. This ensures the script waits only as long as necessary and adapts to different network or browser speeds.

### 13. Safer URL verification

The current URL is checked using `startswith` rather than exact matching. This allows minor variations like query parameters or trailing slashes without failing the test.

### 14. Determining test result

If the current URL starts with the expected base URL, the navigation is considered successful; otherwise, the test reports a failure.

---

# TEST CASE 3 - FORM FILLING

## Objective

The goal of this test case is to reliably automate filling the **Book Demo** form on the website using Selenium with Python. This form is **JavaScript‑heavy and dynamically re‑renders**, which makes simple automation approaches unreliable if not handled carefully.

## Key Challenge

This page does **not behave like a static HTML form**:

* The form uses heavy JavaScript 
* Some inputs trigger **DOM re‑rendering** when text is entered
* Because of this, Selenium can lose focus or type into the wrong field
* Fixed delays (`time.sleep`) may work sometimes and fail other times

## Strategy Used

### 1. Explicit Waits (Instead of Fixed Sleeps)

* `WebDriverWait` with Selenium Expected Conditions is used
* Elements are interacted with **only when they are ready**
* This avoids random failures due to timing issues

### 2. Scroll and Focus Before Interaction

Before interacting with any field:

* The element is scrolled into the **center of the screen** using JavaScript
* The element is explicitly focused

This prevents:

* Header/footer overlap
* Clicking invisible or partially visible elements

## Input Handling Approach

Not all input fields behave the same. Based on behavior, inputs are handled in **two different ways**.

### A. Normal Inputs (send_keys)

Used for fields that behave like standard inputs:

* Name
* Email
* Phone

**Method used:**

* `element_to_be_clickable`
* `clear()`
* `send_keys()`

These fields correctly accept values using Selenium’s normal typing.


### B. JavaScript‑Heavy Inputs (JS Injection)

Used for fields that **do not accept values reliably** with `send_keys`:

* Company
* Message

**Why send_keys fails here:**

* These fields are managed by JavaScript
* Typing triggers DOM re‑rendering
* The page listens for specific JS events (`input`, `change`)

**Solution used:**

* Set the value directly using JavaScript
* Manually dispatch `input` and `change` events

This ensures the page **recognizes the value as valid user input**.


## Dropdown Handling

* The dropdown is handled using Selenium’s `Select` class
* Interaction happens **only after the form stabilizes** following JS input
* `element_to_be_clickable` is used to ensure reliability

## Why This Approach Is Reliable

* Elements are always located **fresh before interaction**
* Explicit waits handle variable JS execution time
* JavaScript injection is used **only where necessary**
* No ActionChains are used for typing (avoids focus drift)

This combination prevents:

* Text entering the wrong field
* Inputs being skipped
* Intermittent or flaky test behavior
---

