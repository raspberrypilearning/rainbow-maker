import matplotlib.pyplot as plt

# Create the figure and axes
fig, ax = plt.subplots()

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

# Adjust the view
ax.set_xlim(0, 10)
ax.set_ylim(0, 35)

# Hide the axes
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

# Add the sky background
fig.patch.set_facecolor("skyblue")
ax.set_facecolor("skyblue")

# Add a title
ax.set_title("The Rainbow Maker", fontsize=20, fontname='Humor Sans')

# Show the picture
plt.show()
