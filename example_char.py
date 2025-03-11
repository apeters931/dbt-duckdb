import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button

# Initial data
categories = ['A', 'B', 'C', 'D']
initial_values = [10, 15, 7, 12]

# Create the figure and axes
fig, ax = plt.subplots()
bars = ax.bar(categories, initial_values)
plt.subplots_adjust(bottom=0.25)

# Create slider axes
ax_slider1 = plt.axes([0.25, 0.1, 0.65, 0.03])
ax_slider2 = plt.axes([0.25, 0.05, 0.65, 0.03])

# Create sliders
slider1 = Slider(ax_slider1, 'Bar A & B', 0, 30, valinit=10)
slider2 = Slider(ax_slider2, 'Bar C & D', 0, 30, valinit=7)

# Function to update the chart
def update(val):
    bars[0].set_height(slider1.val)
    bars[1].set_height(slider1.val)
    bars[2].set_height(slider2.val)
    bars[3].set_height(slider2.val)
    fig.canvas.draw_idle()

# Connect sliders to the update function
slider1.on_changed(update)
slider2.on_changed(update)

# Create a reset button
resetax = plt.axes([0.8, 0.9, 0.1, 0.04])
button = Button(resetax, 'Reset', color='lightgoldenrodyellow', hovercolor='0.975')

# Function to reset the sliders and chart
def reset(event):
    slider1.reset()
    slider2.reset()

# Connect the reset button
button.on_clicked(reset)

plt.show()