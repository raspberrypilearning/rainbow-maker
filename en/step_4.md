<h2 class="c-project-heading--task">Build the full rainbow</h2>

--- task ---

Use the same pattern to add the rest of the rainbow colours.

--- /task ---

<h2 class="c-project-heading--explainer">Repeat the pattern</h2>

You’ve already made `orange` by subtracting 1 from every value in `red`.

You can keep using the same idea to build the rest of the rainbow.  
Each new colour should be just a little bit lower than the one above it.

Add these new colour lists, then draw each one.

<div class="c-project-code">

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 6
line_highlights: 11-15,21-24
---
# Rainbow data
sky = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
red = [10, 18, 24, 28, 30, 31, 30, 28, 24, 18, 10]

# Make each new colour
orange = [y - 1 for y in red]
yellow = [y - 1 for y in orange]
green  = [y - 1 for y in yellow]
blue   = [y - 1 for y in green]
purple = [y - 1 for y in blue]

# Draw the rainbow
ax.plot(sky, red,    color='red',    linewidth=9)
ax.plot(sky, orange, color='orange', linewidth=9)
ax.plot(sky, yellow, color='yellow', linewidth=9)
ax.plot(sky, green,  color='green',  linewidth=9)
ax.plot(sky, blue,   color='blue',   linewidth=9)
ax.plot(sky, purple, color='purple', linewidth=9)
--- /code ---

</div>

<div class="c-project-output">

![A white graph with visible axes showing six thick curved stripes forming a rainbow: red, orange, yellow, green, blue, and purple.](images/step_4.jpg)

</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Notice the pattern:
- Each colour is made from the one above it.
- Each line uses the same `sky` values.

Coding is often about spotting patterns and repeating them!

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

- All your lists must be the same length as `sky`.
- Make sure each colour is plotted with `ax.plot(...)`.
- Check your spelling of colour names inside `' '`.

</div>