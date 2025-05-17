# React Interview Questions and Answers

This document contains the top 10 most commonly asked React interview questions with detailed answers.

## Table of Contents

- [React Interview Questions and Answers](#react-interview-questions-and-answers)
  - [Table of Contents](#table-of-contents)
  - [1. What is React and what are its key features?](#1-what-is-react-and-what-are-its-key-features)
    - [Key Features](#key-features)
  - [2. Explain the difference between Props and State](#2-explain-the-difference-between-props-and-state)
    - [Props (Properties)](#props-properties)
    - [State](#state)
  - [3. What are React Hooks? Explain the most commonly used ones](#3-what-are-react-hooks-explain-the-most-commonly-used-ones)
    - [Most Common Hooks](#most-common-hooks)
  - [4. Explain the Virtual DOM and how it works](#4-explain-the-virtual-dom-and-how-it-works)
    - [Process:](#process)
    - [Benefits](#benefits)
  - [5. What is the difference between controlled and uncontrolled components?](#5-what-is-the-difference-between-controlled-and-uncontrolled-components)
    - [Controlled Components](#controlled-components)
    - [Uncontrolled Components](#uncontrolled-components)
  - [6. Explain React's component lifecycle methods](#6-explain-reacts-component-lifecycle-methods)
    - [Class Component Lifecycle](#class-component-lifecycle)
    - [Functional Component Lifecycle (using useEffect)](#functional-component-lifecycle-using-useeffect)
  - [7. What is Redux and when should you use it?](#7-what-is-redux-and-when-should-you-use-it)
    - [Use when](#use-when)
    - [Key concepts](#key-concepts)
  - [8. Explain React's Context API](#8-explain-reacts-context-api)
    - [Usage](#usage)
    - [Best for](#best-for)
  - [9. What are React Fragments and when should you use them?](#9-what-are-react-fragments-and-when-should-you-use-them)
    - [Syntax](#syntax)
  - [10. Explain React's error boundaries](#10-explain-reacts-error-boundaries)
    - [Implementation](#implementation)
    - [Use cases](#use-cases)
  - [Best Practices](#best-practices)

## 1. What is React and what are its key features?

React is a JavaScript library for building user interfaces, particularly single-page applications.

### Key Features

- Virtual DOM for efficient rendering
- Component-based architecture
- One-way data flow
- JSX syntax
- React Hooks for state management
- Server-side rendering support

## 2. Explain the difference between Props and State

### Props (Properties)

- Read-only, immutable data passed from parent to child
- Used for configuration and passing data down
- Cannot be modified by the component

### State

- Mutable data managed within the component
- Can be changed using setState()
- Triggers re-rendering when updated
- Local to the component unless lifted up

## 3. What are React Hooks? Explain the most commonly used ones

Hooks are functions that let you use state and other React features in functional components.

### Most Common Hooks

- `useState`: Manages state in functional components
- `useEffect`: Handles side effects (like API calls, subscriptions)
- `useContext`: Accesses React context
- `useReducer`: Alternative to useState for complex state logic
- `useCallback`: Memoizes functions
- `useMemo`: Memoizes values

## 4. Explain the Virtual DOM and how it works

Virtual DOM is a lightweight copy of the actual DOM.

### Process:

1. React creates a virtual representation of the UI
2. When state changes, a new virtual DOM is created
3. React compares new virtual DOM with previous one (diffing)
4. Only the differences are updated in the real DOM

### Benefits

- Improved performance
- Reduced memory usage
- Better user experience

## 5. What is the difference between controlled and uncontrolled components?

### Controlled Components

- Form data is handled by React state
- Input values are controlled by React
- Example

```jsx
const [value, setValue] = useState('');
<input value={value} onChange={(e) => setValue(e.target.value)} />
```

### Uncontrolled Components

- Form data is handled by the DOM itself
- Use refs to access form values
- Example

```jsx
const inputRef = useRef();
<input ref={inputRef} />
```

## 6. Explain React's component lifecycle methods

### Class Component Lifecycle

- Mounting: constructor, render, componentDidMount
- Updating: shouldComponentUpdate, render, componentDidUpdate
- Unmounting: componentWillUnmount

### Functional Component Lifecycle (using useEffect)

```jsx
useEffect(() => {
  // componentDidMount
  return () => {
    // componentWillUnmount
  };
}, []); // Empty dependency array
```

## 7. What is Redux and when should you use it?

Redux is a state management library.

### Use when

- Multiple components need to share state
- State updates are complex
- Need predictable state management

### Key concepts

- Store: Single source of truth
- Actions: Describe what happened
- Reducers: Specify how state changes
- Middleware: Handle side effects

## 8. Explain React's Context API

Context provides a way to pass data through the component tree without prop drilling.

### Usage

```jsx
const MyContext = React.createContext();

// Provider
<MyContext.Provider value={someValue}>
  <Child />
</MyContext.Provider>

// Consumer
const value = useContext(MyContext);
```

### Best for

- Theme data
- User authentication
- Language preferences
- Global state that doesn't change often

## 9. What are React Fragments and when should you use them?

Fragments let you group elements without adding extra nodes to the DOM.

### Syntax

```jsx
// Long syntax
<React.Fragment>
  <ChildA />
  <ChildB />
</React.Fragment>

// Short syntax
<>
  <ChildA />
  <ChildB />
</>
```

- You need to return multiple elements
- Don't want to add extra div elements
- Need to group elements without styling

## 10. Explain React's error boundaries

Error boundaries are React components that catch JavaScript errors anywhere in their child component tree.

### Implementation

```jsx
class ErrorBoundary extends React.Component {
  state = { hasError: false };
  
  static getDerivedStateFromError(error) {
    return { hasError: true };
  }
  
  componentDidCatch(error, errorInfo) {
    // Log error to service
  }
  
  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return this.props.children;
  }
}
```

### Use cases

- Prevent entire app from crashing
- Show fallback UI
- Log errors to error reporting service

## Best Practices

- Understand the concepts deeply, not just memorize answers
- Be prepared to provide real-world examples
- Practice implementing these concepts in code
- Stay updated with the latest React features and best practices
  