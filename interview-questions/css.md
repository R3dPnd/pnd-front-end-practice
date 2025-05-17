# Top CSS Interview Questions

## 1. What is the difference between display: none and visibility: hidden?

**display: none**

- Removes element from the document flow
- Takes up no space
- Cannot be animated
- Element is not accessible to screen readers
- Child elements are also hidden

**visibility: hidden**

- Element remains in document flow
- Takes up space
- Can be animated
- Element is not visible but still accessible to screen readers
- Child elements can be made visible

**Example:**

```css
.hidden-display {
  display: none;
}

.hidden-visibility {
  visibility: hidden;
}

/* Child element can be visible even if parent is visibility: hidden */
.hidden-visibility .child {
  visibility: visible;
}
```

## 2. Explain CSS Selectors and their specificity

**Selector Types (in order of specificity):**

1. Inline styles (1000)
2. IDs (100)
3. Classes, attributes, pseudo-classes (10)
4. Elements, pseudo-elements (1)

**Common Selectors:**

```css
/* Element selector */
div { }

/* Class selector */
.class-name { }

/* ID selector */
#id-name { }

/* Attribute selector */
[type="text"] { }

/* Pseudo-class */
:hover { }

/* Pseudo-element */
::before { }

/* Combinators */
div > p { }  /* Direct child */
div + p { }  /* Adjacent sibling */
div ~ p { }  /* General sibling */
div p { }    /* Descendant */
```

## 3. What is the CSS Box Model and how does box-sizing affect it?

**Box Model Components:**

- Content
- Padding
- Border
- Margin

**Box-Sizing Values:**

```css
/* content-box (default) */
.element {
  box-sizing: content-box;
  width: 100px;
  padding: 20px;
  border: 5px solid;
  /* Total width = 100px + (2 * 20px) + (2 * 5px) = 150px */
}

/* border-box (recommended) */
.element {
  box-sizing: border-box;
  width: 100px;
  padding: 20px;
  border: 5px solid;
  /* Total width = 100px (includes padding and border) */
}
```

## 4. What are CSS Variables (Custom Properties) and how do they work?

**Definition and Usage:**

```css
:root {
  --primary-color: #007bff;
  --spacing-unit: 8px;
  --font-family: 'Arial', sans-serif;
}

.element {
  color: var(--primary-color);
  padding: calc(var(--spacing-unit) * 2);
  font-family: var(--font-family);
}

/* Fallback values */
.element {
  color: var(--primary-color, #000);
}

/* Scoped variables */
.theme-dark {
  --primary-color: #fff;
  --background-color: #000;
}
```

## 5. Explain CSS Flexbox and its properties

**Main Properties:**

```css
.container {
  display: flex;
  
  /* Direction */
  flex-direction: row | row-reverse | column | column-reverse;
  
  /* Wrapping */
  flex-wrap: nowrap | wrap | wrap-reverse;
  
  /* Justify content (main axis) */
  justify-content: flex-start | flex-end | center | space-between | space-around;
  
  /* Align items (cross axis) */
  align-items: stretch | flex-start | flex-end | center | baseline;
  
  /* Align content (multiple lines) */
  align-content: flex-start | flex-end | center | space-between | space-around;
}

.item {
  /* Growth */
  flex-grow: 0;
  
  /* Shrink */
  flex-shrink: 1;
  
  /* Basis */
  flex-basis: auto;
  
  /* Shorthand */
  flex: 0 1 auto;
}
```

## 6. What is CSS Grid and how does it differ from Flexbox?

**Grid vs Flexbox:**

- Grid: 2D layout (rows and columns)
- Flexbox: 1D layout (row OR column)

**Grid Properties:**

```css
.container {
  display: grid;
  
  /* Define columns */
  grid-template-columns: repeat(3, 1fr);
  
  /* Define rows */
  grid-template-rows: auto 1fr auto;
  
  /* Gap between items */
  gap: 20px;
  
  /* Areas */
  grid-template-areas:
    "header header header"
    "sidebar main main"
    "footer footer footer";
}

.item {
  /* Position in grid */
  grid-column: 1 / 3;
  grid-row: 1 / 2;
  
  /* Area name */
  grid-area: header;
}
```

## 7. What are CSS Pseudo-classes and Pseudo-elements?

**Pseudo-classes:**

```css
/* State-based */
:link { }
:visited { }
:hover { }
:active { }
:focus { }

/* Structural */
:first-child { }
:last-child { }
:nth-child(n) { }
:only-child { }

/* Form-based */
:checked { }
:disabled { }
:required { }
```

**Pseudo-elements:**

```css
/* ::before and ::after */
.element::before {
  content: "";
  /* styles */
}

.element::after {
  content: "";
  /* styles */
}

/* Other pseudo-elements */
::first-line { }
::first-letter { }
::selection { }
```

## 8. Explain CSS Transitions and Animations

**Transitions:**

```css
.element {
  transition: property duration timing-function delay;
  
  /* Shorthand */
  transition: all 0.3s ease-in-out;
  
  /* Multiple properties */
  transition: 
    background-color 0.3s ease,
    transform 0.5s ease-in;
}

/* Trigger */
.element:hover {
  background-color: blue;
  transform: scale(1.1);
}
```

**Animations:**

```css
@keyframes slide {
  0% {
    transform: translateX(0);
  }
  50% {
    transform: translateX(100px);
  }
  100% {
    transform: translateX(0);
  }
}

.element {
  animation: slide 2s ease-in-out infinite;
  
  /* Individual properties */
  animation-name: slide;
  animation-duration: 2s;
  animation-timing-function: ease-in-out;
  animation-iteration-count: infinite;
  animation-direction: alternate;
  animation-delay: 1s;
  animation-fill-mode: forwards;
}
```

## 9. What are CSS Media Queries and how do they work?

**Basic Structure:**

```css
/* Basic media query */
@media screen and (max-width: 768px) {
  .container {
    width: 100%;
  }
}

/* Multiple conditions */
@media screen and (min-width: 768px) and (max-width: 1024px) {
  .container {
    width: 750px;
  }
}

/* Device orientation */
@media (orientation: landscape) {
  .container {
    flex-direction: row;
  }
}

/* Print styles */
@media print {
  .no-print {
    display: none;
  }
}
```

## 10. What are CSS Preprocessors and what are their main features?

**Main Features:**

1. Variables
2. Nesting
3. Mixins
4. Functions
5. Operations
6. Imports

**SASS/SCSS Example:**

```scss
// Variables
$primary-color: #007bff;
$spacing: 20px;

// Mixins
@mixin flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

// Functions
@function calculate-width($n) {
  @return $n * $spacing;
}

// Nesting
.card {
  padding: $spacing;
  
  &-header {
    color: $primary-color;
  }
  
  &-body {
    @include flex-center;
    width: calculate-width(5);
  }
  
  &:hover {
    transform: scale(1.05);
  }
}

// Operations
.container {
  width: 100% - 20px;
  margin: $spacing / 2;
}

// Imports
@import 'variables';
@import 'mixins';
```

---

**Remember to:**

- Understand the cascade and specificity
- Know browser compatibility
- Be familiar with modern CSS features
- Understand performance implications
- Know debugging techniques
- Be aware of CSS best practices
- Understand responsive design principles
- Know CSS architecture patterns
- Be familiar with CSS frameworks
- Understand CSS optimization techniques
