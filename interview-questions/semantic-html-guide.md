# Semantic HTML Guide

## What is Semantic HTML?

Semantic HTML means using HTML elements that clearly describe their meaning to both the browser and the developer. Instead of using generic `<div>` or `<span>` elements, semantic HTML uses elements that have specific meanings.

## Why Use Semantic HTML?

1. **Accessibility**
   - Screen readers can better interpret the page
   - Better navigation for users with disabilities
   - Improved keyboard navigation

2. **SEO Benefits**
   - Search engines better understand your content
   - Improved search rankings
   - Better content structure

3. **Maintainability**
   - Easier to understand code
   - Better code organization
   - Clearer structure

## Common Semantic Elements

### Document Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Page Title</title>
</head>
<body>
    <header>
        <!-- Site header content -->
    </header>
    
    <nav>
        <!-- Navigation menu -->
    </nav>
    
    <main>
        <!-- Main content -->
        <article>
            <!-- Self-contained content -->
        </article>
        
        <section>
            <!-- Thematic grouping of content -->
        </section>
        
        <aside>
            <!-- Sidebar content -->
        </aside>
    </main>
    
    <footer>
        <!-- Footer content -->
    </footer>
</body>
</html>
```

### Text Elements
```html
<!-- Headings -->
<h1>Main Title</h1>
<h2>Section Title</h2>
<h3>Subsection Title</h3>

<!-- Paragraphs -->
<p>Regular paragraph text</p>

<!-- Lists -->
<ul>
    <li>Unordered list item</li>
</ul>

<ol>
    <li>Ordered list item</li>
</ol>

<dl>
    <dt>Term</dt>
    <dd>Definition</dd>
</dl>

<!-- Quotes -->
<blockquote>
    <p>Block quote content</p>
    <cite>— Author Name</cite>
</blockquote>

<q>Inline quote</q>

<!-- Code -->
<code>Code snippet</code>
<pre>Preformatted text</pre>

<!-- Time -->
<time datetime="2024-03-20">March 20, 2024</time>
```

### Form Elements
```html
<form>
    <fieldset>
        <legend>Form Section</legend>
        
        <label for="name">Name:</label>
        <input type="text" id="name" name="name">
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email">
        
        <button type="submit">Submit</button>
    </fieldset>
</form>
```

### Media Elements
```html
<!-- Images -->
<figure>
    <img src="image.jpg" alt="Description">
    <figcaption>Image caption</figcaption>
</figure>

<!-- Video -->
<video controls>
    <source src="video.mp4" type="video/mp4">
    Your browser doesn't support video.
</video>

<!-- Audio -->
<audio controls>
    <source src="audio.mp3" type="audio/mpeg">
    Your browser doesn't support audio.
</audio>
```

### Interactive Elements
```html
<!-- Navigation -->
<nav>
    <ul>
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#contact">Contact</a></li>
    </ul>
</nav>

<!-- Details/Summary -->
<details>
    <summary>Click to expand</summary>
    <p>Hidden content here</p>
</details>

<!-- Dialog -->
<dialog>
    <h2>Dialog Title</h2>
    <p>Dialog content</p>
    <button onclick="this.parentElement.close()">Close</button>
</dialog>
```

## Best Practices

1. **Use Appropriate Elements**
   - Choose elements based on meaning, not appearance
   - Use CSS for styling, not HTML
   - Avoid unnecessary divs and spans

2. **Accessibility**
   - Include alt text for images
   - Use ARIA roles when necessary
   - Ensure proper heading hierarchy
   - Provide text alternatives

3. **Structure**
   - One `<h1>` per page
   - Logical heading order
   - Proper nesting of elements
   - Clear content hierarchy

4. **Forms**
   - Use `<label>` with every input
   - Group related form elements
   - Provide clear error messages
   - Use appropriate input types

## Common Mistakes to Avoid

1. **Using div for everything**
```html
<!-- Bad -->
<div class="header">...</div>
<div class="nav">...</div>

<!-- Good -->
<header>...</header>
<nav>...</nav>
```

2. **Incorrect heading hierarchy**
```html
<!-- Bad -->
<h1>Title</h1>
<h3>Subtitle</h3>
<h2>Another section</h2>

<!-- Good -->
<h1>Title</h1>
<h2>Subtitle</h2>
<h2>Another section</h2>
```

3. **Missing alt text**
```html
<!-- Bad -->
<img src="image.jpg">

<!-- Good -->
<img src="image.jpg" alt="Description of image">
```

4. **Using tables for layout**
```html
<!-- Bad -->
<table>
    <tr>
        <td>Left column</td>
        <td>Right column</td>
    </tr>
</table>

<!-- Good -->
<div class="grid">
    <div>Left column</div>
    <div>Right column</div>
</div>
```

## Benefits of Semantic HTML

1. **For Developers**
   - Easier to maintain
   - Better code readability
   - Clearer structure
   - Faster development

2. **For Users**
   - Better accessibility
   - Improved navigation
   - Better user experience
   - Faster page loads

3. **For Search Engines**
   - Better content understanding
   - Improved SEO
   - Better indexing
   - Higher rankings

Remember:
- Use elements for their intended purpose
- Consider accessibility first
- Keep structure logical and clear
- Use CSS for styling
- Test with screen readers
- Validate your HTML
- Keep learning new semantic elements 