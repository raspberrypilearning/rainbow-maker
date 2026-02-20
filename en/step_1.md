<h2 class="c-project-heading--task">Make your first rainbow stripe</h2>

--- task ---

Run the code to see what happens, then add some data to draw your first red stripe.

--- /task ---

<h2 class="c-project-heading--explainer">A library for colourful art</h2>

You’re going to use a powerful graphing library called <strong>Matplotlib</strong> — but instead of graphs, you’ll make a rainbow! 🌈  
When you first press <strong>Run</strong>, you’ll just see an empty window — your blank canvas.  

Next, you’ll add some data to draw the red arc of your rainbow.

<div class="c-project-code">

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 7-8,14
---
# Rainbow data
sky = [0, 1, 2, 3, 4]
red = [10, 24, 31, 24, 10]

# Make each new colour


# Draw the rainbow
ax.plot(sky, red,    color='red',    linewidth=9)
--- /code ---

</div>

<div class="c-project-output">

<img src="/images/rainbow-red-jagged.png" alt="A red, slightly jagged arc drawn across the window." />

</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Try changing the numbers in <code>red</code> — bigger numbers make the arc higher!  
You can also change <code>color='red'</code> to another colour name like <code>'green'</code> or <code>'pink'</code>.

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

- Did you spell <code>color</code> the American way (with no “u”)?  
- If nothing appears, check that you wrote <code>ax.plot(...)</code> exactly as shown.  
- Make sure your lists use square brackets: <code>[ ]</code> not <code>( )</code>.

</div>