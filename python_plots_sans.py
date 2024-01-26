# Example code with the SNO+ collaboration plot style adapted to Python
# Requires the file Times_New_Roman_Normal.ttf

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.font_manager as fm
import numpy as np

# Set the font properties - different for paper/slides
# Sans serif already exists in matplotlib but Times New Roman doesn't
# So maybe we don't need font file for sans serif, just use the times new roman one?
# Although it doesn't really seem to work ...

#Setting font parameters -- this is for presentations, where sans serif is ok

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 12          # Default font size
plt.rcParams['axes.titlesize'] = 20    # Title font size
plt.rcParams['axes.labelsize'] = 16    # Axis label font size
plt.rcParams['xtick.labelsize'] = 12   # X-axis tick label font size
plt.rcParams['ytick.labelsize'] = 12   # Y-axis tick label font size
plt.rcParams['legend.fontsize'] = 16   # Legend font size

# Define custom styles
histogram_style = {
    'histtype': 'step',
    'color': 'blue',
    'alpha': 0.7,
    'linewidth': 1.5
}

scatter_style = {
    'marker': 'o',
    'color': 'black',
    's': 50
}

errorbar_style = {
    'linestyle': 'None',
    'color': 'black',
    'capsize': 5
}

line_plot_style = {
    'linestyle': '-',
    'color': 'red',
    'linewidth': 1.5
}

# Set global rcParams
plt.rcParams['xtick.major.size'] = 10
plt.rcParams['xtick.major.width'] = 1.5
plt.rcParams['xtick.minor.size'] = 5
plt.rcParams['xtick.minor.width'] = 1
plt.rcParams['ytick.major.size'] = 10
plt.rcParams['ytick.major.width'] = 1.5
plt.rcParams['ytick.minor.size'] = 5
plt.rcParams['ytick.minor.width'] = 1
plt.rcParams['axes.linewidth'] = 1.5  # set the value globally
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['figure.figsize'] = (18, 10)
plt.rcParams['xtick.major.pad'] = '12'  # set padding (between ticks and axis label)
plt.rcParams['ytick.major.pad'] = '12'

# Example data for plotting
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 6, 8, 10, 9, 6.6, 7, 8.5, 3]

# First plot: hist, scatter, line
fig, ax = plt.subplots(figsize=(18, 10))

ax.minorticks_on()
ax.hist(y, **histogram_style, label='Histogram')

ax.scatter(x, y, **scatter_style, label='Scatter')
ax.errorbar(x, y, yerr=0.5, **errorbar_style, label='Errorbar')
ax.plot(x, y, **line_plot_style, label='Line Plot')

ax.set_xlabel('This is the x axis')
ax.set_ylabel('This is the y axis')
ax.set_title("Different kinds of plots!! so cool")
ax.legend()
plt.show()

# Second plot: color map
fig, ax = plt.subplots(figsize=(10, 10))

data = np.random.random((10, 10))
img = ax.imshow(data, cmap='viridis')
fig.colorbar(img, ax=ax, label='Color Map')  # Add colorbar to the figure

ax.set_xlabel('This is the x axis')
ax.set_ylabel('This is the y axis')
ax.set_title("Color map plot")
plt.show()

#Comments

"""
For color-blind friendly plots

Color maps: default is viridis, which is already color blind friendly -- maybe just write in instructions that people shouldn't change it and just use the default?

If you have different types of data points, use different markers if possible, not just different colors

Sometimes we need multiple lines to be plotted in the same plot; should set colorblind friendly color cycle?
"""

"""
Should add instructions for how to use template 

Something like: if you need x type of plot, copy these lines, adjust these parameters if needed, try doing this to account for color blindness

Lines ... (stuff that sets sizes of font and axis width and stuff) should not be changed
"""
'''
Do we ever need to add captions for plots? Should set style for those as well?
'''

'''
I think the title and axis label fonts are a bit too small for this plot size
'''


'''
Other differences between paper/slides plots? 
'''
