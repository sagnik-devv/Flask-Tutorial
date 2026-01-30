# Jinja2 Templates: The Ultimate Guide

Jinja2 is the generic template engine shipped with Flask. It allows you to write HTML code that contains "holes" where you can inject dynamic data (variables) and logic (loops, conditions).

## 1. The Core Delimiters
Jinja2 uses special characters to distinguish Python-like code from standard HTML:

- `{{ ... }}` : **Expressions** (Variables). Used to print something to the screen.
- `{% ... %}` : **Statements** (Logic). Used for control instructions like loops and if-statements.
- `{# ... #}` : **Comments**. These are not visible in the final HTML page.

---

## 2. Variables
Variables are passed from your Python `app.py` to your HTML template using `render_template()`.

**Python Code:**
```python
@app.route('/profile')
def profile():
    user_info = {'username': 'Sagnik', 'age': 25}
    return render_template('profile.html', user=user_info)
```

**Template Code (`profile.html`):**
```html
<h1>Welcome, {{ user.username }}!</h1>
<p>Age: {{ user.age }}</p>
```

---

## 3. Control Structures (Logic)

### A. If Statements
You can show or hide HTML blocks based on conditions.

```html
{% if user.age >= 18 %}
    <p>Status: <span class="badge">Adult</span></p>
{% else %}
    <p>Status: <span class="badge">Minor</span></p>
{% endif %}
```

### B. For Loops
Used to iterate over lists or dictionaries.

**Python:** `items = ['Apple', 'Banana', 'Cherry']`

**Template:**
```html
<ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>
```

**Special Loop Variables:**
Inside a loop, Jinja gives you special variables:
- `loop.index`: Current iteration (1-based counting).
- `loop.index0`: Current iteration (0-based counting).
- `loop.first`: True if this is the first item.
- `loop.last`: True if this is the last item.

---

## 4. Filters
Filters modify variables before they are rendered. You act on them using a pipe symbol (`|`).

- **`capitalize`**: Capitalize the first letter. `{{ "hello" | capitalize }}` -> "Hello"
- **`upper`**: Make all uppercase. `{{ "hello" | upper }}` -> "HELLO"
- **`length`**: Get length of list/string. `{{ items | length }}` -> 3
- **`safe`**: **CRITICAL**. Tells Jinja that this variable contains safe HTML and it should be rendered as real HTML, not text.
  ```html
  {{ "<b>Bold Text</b>" | safe }}  <!-- Renders bold text properly -->
  ```
- **`default`**: Use a fallback if the variable is missing. `{{ username | default('Guest') }}`

---

## 5. Template Inheritance (The "Base" Pattern)
This is the most powerful feature. It allows you to have one `base.html` with your consistent Header/Footer/CSS, and other pages just "fill in the blanks".

**Step 1: Create `base.html`**
This file defines blocks that children can override.
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My App{% endblock %}</title>
</head>
<body>
    <nav>My Navbar</nav>

    <div class="content">
        {% block content %}
        <!-- Child pages will inject content here -->
        {% endblock %}
    </div>

    <footer>Copyright 2026</footer>
</body>
</html>
```

**Step 2: Create `child.html`**
This file "extends" the base.
```html
{% extends "base.html" %}

{% block title %}User Profile{% endblock %}

{% block content %}
    <h1>This is the Profile Page</h1>
    <p>It automatically gets the navbar and footer!</p>
{% endblock %}
```

---

## 6. Micros & Includes (Advanced)

### Include
Inserts another template file into the current one. Useful for repeated widgets like a sidebar or a card.
```html
{% include 'sidebar.html' %}
```

### Macros
Macros are like functions for templates.
```html
{% macro input(name, value='', type='text') %}
    <input type="{{ type }}" name="{{ name }}" value="{{ value }}">
{% endmacro %}

<!-- Usage -->
{{ input('username') }}
{{ input('password', type='password') }}
```
