import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

#read data
df = pd.read_csv('exports/characters_transformed.csv')
names = df['name'].to_list()
number_of_episodes = df['no_ep'].to_list()

# create the figure and axes
n = 5
fig, ax = plt.subplots()
bars = ax.bar(names[:n],number_of_episodes[:n])
plt.subplots_adjust(bottom=0.25)

# create slider axis and slider
ax_slider = plt.axes(arg=[0.25,0.1,0.65,0.03], facecolor='lightgoldenrodyellow')
slider = Slider(ax_slider, label='Character Number', valmin=1, valmax=10, valinit=n, valstep=1)

# function to update the chart
def update(val):
    n = slider.val
    ax.cla()
    bars = ax.bar(names[:n],number_of_episodes[:n])
    fig.canvas.draw_idle()
 
# connect sliders to the update function
slider.on_changed(update)

# create a reset button
resetax = plt.axes([0.8, 0.9, 0.1, 0.04])
button = Button(resetax, 'Reset', color='lightgoldenrodyellow', hovercolor='0.975')

# function to reset the sliders and chart
def reset(event):
    slider.reset()

# connect the reset button
button.on_clicked(reset)

plt.show()
