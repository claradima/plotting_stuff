# Template macro for Python with the SNO+ plot style using Sans Serif (standard font in matplotlib, ok for slides but NOT publications)
# Written by Clara Dima (c.dima@sussex.ac.uk); contact me or Ana Sofia Inacio for comments/suggestions
# Tested with python 3.10.12
#
# General rules:
# - Every figure that shows SNO+ data needs to be marked (embedded on the figure) with “SNO+ Preliminary”
# - Data should be black points with error bars (where a single data series is shown)
# - MC should be a blue histogram (where a single model is shown)
# - Any fit function (not based on MC) should be red (when a single fit is shown)
# - Consistency in labelling: normalized R3 axes should be labelled "R^3 / R_AV^3"
# - Isotropy should be #beta_14 (i.e. the greek symbol, not the word)
# - No box around legend
# - For publication purposes, the favoured font type has been Times (New) Roman
#
# For plots that compare multiple data series (e.g. optics at different wavelengths) or multiple models or fits, 
# appropriately different colours, markers, line styles should be used to differentiate and clearly labelled in the legend.
# Check https://www.cta-observatory.org/wp-content/uploads/2020/10/CTA_ColourBlindness_BestPractices-1.pdf 
# for colorblind friendly color palletes and other guidelines
#
# When saving the figures, always choose to save in PDF format as it is a scalable vector graphic and can be scaled 
# infinitely without losing quality.
#
# Specific analyses may produce plots which require styles different than the ones exemplified here. Trying as much
# as possible to follow the style rules where possible will certainly make the approval process easier.
#
# To test the style and see the examples, run
# python3 python_plots_sans.py


import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.font_manager as fm
import numpy as np
from matplotlib.ticker import MultipleLocator

# Setting font parameters globally
# Note - can only do this with sans serif because it already exists in matplotlib; it doesn't work for Times New Roman where we need font file

plt.rcParams['font.family'] = 'sans-serif'
# set default font size
plt.rcParams['font.size'] = 12
# set title font size
plt.rcParams['axes.titlesize'] = 20
# set axis label font size
plt.rcParams['axes.labelsize'] = 16
# set tick label size on x and y axis
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14
# set legend font size
plt.rcParams['legend.fontsize'] = 12

#set other global parameters with rcParams -- copy whole block below before plotting code to set plotting template globally

# set height and width of big markings on axis x
plt.rcParams['xtick.major.size'] = 6
plt.rcParams['xtick.major.width'] = 1.6
# set height and width of small markings on axis x
plt.rcParams['xtick.minor.size'] = 3
plt.rcParams['xtick.minor.width'] = 1.6
# set height and width of big markings on axis y
plt.rcParams['ytick.major.size'] = 6
plt.rcParams['ytick.major.width'] = 1.6
# set height and width of small markings on axis y
plt.rcParams['ytick.minor.size'] = 3
plt.rcParams['ytick.minor.width'] = 1.6
# set thickness of axes
plt.rcParams['axes.linewidth'] = 1.6
# set plot background color
plt.rcParams['figure.facecolor'] = 'white'
# set plot aspect ratio -- change according to needs
plt.rcParams['figure.figsize'] = (8.5, 6.5)
# set padding (between ticks and axis label)
plt.rcParams['xtick.major.pad'] = '6'
plt.rcParams['ytick.major.pad'] = '6'
# set padding (between plot and title)
plt.rcParams['axes.titlepad'] = 12
# set markings on axis to show on the inside of the plot, can change if needed
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

# define custom styles -- add **set_style to plot, as shown in EXAMPLE PLOT 1 below
histogram_style = {
    'histtype': 'step',
    'color': 'blue',
    'alpha': 0.7,
    'linewidth': 1.5
}

scatter_style = {
    'marker': 's',
    'color': 'black',
    's': 25
}

errorbar_style = {
    'linestyle': 'None',
    'color': 'black',
    'capsize': 1.5
}

line_plot_style = {
    'linestyle': '-',
    'color': 'red',
    'linewidth': 2
}


# Example data for plotting
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 6, 8, 10, 9, 6.6, 7, 8.5, 3]
y_2 = [1.3, 3.1, 5, 6, 9, 8, 6.5, 6, 7, 3.5]

# EXAMPLE PLOT 1: hist, scatter, line, all on the same plot

fig, ax = plt.subplots()
# can add figsize here if globally set size is not suitable, such as:
# fig, ax = plt.subplots(figsize=(18, 10))

ax.minorticks_on()

# for any of the plot types below, if you don't want to use the globally set parameters, copy parameters individually instead of writing **set_style and adjust values how you want 

# plot histogram
ax.hist(y, **histogram_style, label='Histogram')
# plot line
ax.plot(x, y_2, **line_plot_style, label='Line Plot')
# scatter plot / data points
ax.scatter(x, y, **scatter_style, label='Scatter')
# plot error bars; can add param xerr to show x error as well
ax.errorbar(x, y, yerr=0.5, **errorbar_style, label='Errorbar')

# set titles 
ax.set_xlabel('This is the x axis')
ax.set_ylabel('This is the y axis')
ax.set_title("Different kinds of plots!! so cool")
# show legend; legend parameters set globally, remove box around legend
ax.legend(frameon=False)



# adjusting the frequency of major ticks by changing number below;  larger number - less dense ticks
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))

# add SNO+ Preliminary label
ax.text(7.35, 10, "SNO+ Preliminary")

plt.show()

# save pdf
plt.savefig("example1D_Sans.pdf", format="pdf")

# EXAMPLE PLOT 2: color map
fig, ax = plt.subplots()
# can add figsize here if globally set size is not suitable, such as:
# fig, ax = plt.subplots(figsize=(18, 10))


# generate some random data points
data = np.random.random((30, 30))

# plot as color map
# viridis is the default and it is colorblind friendly :)

img = ax.imshow(data, cmap='viridis')

# show color map
# pad sets the distance between plot and color bar
# aspect sets aspect ratio of color bar;  increase the number to make it less thick
fig.colorbar(img, ax=ax, label='Color Map',pad=0.01, aspect = 12)

ax.set_xlabel('This is the x axis')
ax.set_ylabel('This is the y axis')
ax.set_title("Color map plot")

# add SNO+ Preliminary label
ax.text(7.35, 10, "SNO+ Preliminary")

plt.show()
plt.savefig("example2D_Sans.pdf", format="pdf")
