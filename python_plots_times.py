# Python plotting template using Times New Roman (for publications)
# This script includes some general template parameters and two example plots - one histogram + scatter with error bars + curve
# One color map plot
# To use Times New Roman font, need Times_New_Roman_Normal.ttf file 
# File included on docDB and in github repo with plotting templates https://github.com/claradima/plotting_stuff
# Script tested with python 3.10.12
# To see examples, just run python3 python_plots_times.py

# Try to stick to these quidelines if possible; for more complicated plots, try using different markers and line types to
# distinguish between different lines/ data point types, and check out https://www.cta-observatory.org/wp-content/uploads/2020/10/CTA_ColourBlindness_BestPractices-1.pdf for colorblind friendly color palletes and other guidelines

# Written by Clara Dima (c.dima@sussex.ac.uk); contact me or Ana Sofia Inacio for comments/suggestions


import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.font_manager as fm
import numpy as np
from matplotlib.ticker import MultipleLocator

# set the font from font file
paper_font = fm.FontProperties(fname='Times_New_Roman_Normal.ttf', size = 16)

# define custom styles -- add **set_style to plot, as shown in EXAMPLE PLOT 1 below

# each of these are pretty self-explanatory, can modify them if needed

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

# set global rcParams -- copy whole block below before plotting code to set plotting template globally

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

# Example data for plotting
x = [1.1, 2.5, 3.2, 4, 4.5, 6.7, 7, 8, 9, 10]
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
# plor line
ax.plot(x, y_2, **line_plot_style, label='Line Plot')
# plot scatter plot/data points
ax.scatter(x, y, **scatter_style, label='Scatter')
# plot error bars, can add param xerr to show x error as well
ax.errorbar(x, y, yerr=0.5, **errorbar_style, label='Errorbar')

# for Times New Roman, need to set font sizes here instead of as a global params
ax.set_xlabel('This is the x axis', fontproperties=paper_font, size = 20)
ax.set_ylabel('This is the y axis', fontproperties=paper_font, size = 20)
ax.set_title("Different kinds of plots!! so cool", fontproperties=paper_font, size = 22)


for label in ax.get_xticklabels():
    label.set_fontproperties(paper_font)

for label in ax.get_yticklabels():
    label.set_fontproperties(paper_font)

# make legend
handles, labels = ax.get_legend_handles_labels()

# setting legend font
ax.legend(handles = handles, labels = labels, prop=fm.FontProperties(fname='Times_New_Roman_Normal.ttf', size = 12))

# remove box around legend
ax.legend(frameon=False)

# adjusting the frequency of major ticks on each axis by changing number below, larger number - less dense ticks
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))

# add SNO+ Preliminary label
ax.text(7.35, 10, "SNO+ Preliminary", fontproperties=fm.FontProperties(fname='Times_New_Roman_Normal.ttf', size = 14))


plt.show()

# EXAMPLE PLOT 2: color map
fig, ax = plt.subplots()

#can add figsize here if globally set size is not suitable, such as:
#fig, ax = plt.subplots(figsize=(18, 10))

# generate some random data to plot
data = np.random.random((30, 30))

# plot as color map
# viridis is the default and it is colorblind friendly :)

img = ax.imshow(data, cmap='viridis')

# show color map
# pad sets the distance between plot and color bar
# aspect sets aspect ratio of color bar;  increase the number to make it less thick
colorbar = fig.colorbar(img, ax=ax, label='Color Map', pad=0.01, aspect = 12)

# set font properties for colorbar label
colorbar.set_label('Color Map', fontproperties=paper_font)
colorbar.ax.tick_params(labelsize=12)

# for Times New Roman, need to set font sizes here instead of as a global params
ax.set_xlabel('This is the x axis', fontproperties=paper_font, size = 20)
ax.set_ylabel('This is the y axis', fontproperties=paper_font, size = 20)
ax.set_title("Color map plot", fontproperties=paper_font, size = 22)

for label in ax.get_xticklabels():
    label.set_fontproperties(paper_font)

for label in ax.get_yticklabels():
    label.set_fontproperties(paper_font)

# add SNO+ Preliminary label
ax.text(7.35, 10, "SNO+ Preliminary", fontproperties=fm.FontProperties(fname='Times_New_Roman_Normal.ttf', size = 14))

plt.show()
