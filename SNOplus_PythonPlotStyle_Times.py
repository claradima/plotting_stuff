# Template macro for Python with the SNO+ plot style using Times New Roman (for publications)
# Written by Clara Dima (c.dima@sussex.ac.uk); contact me or Ana Sofia Inacio for comments/suggestions
# Tested with python 3.10.12
# Requires the Times_New_Roman_Normal.ttf file 
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
# python3 python_plots_times.py

import os
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.font_manager as fm
import numpy as np
from matplotlib.ticker import MultipleLocator

# set the font from font file
# most font parameters not set globally (unlike in the sans script) because this doesn't work when using a separate font file

personal_path = os.path.dirname(os.path.realpath(__file__))
font_file = 'Times_New_Roman_Normal.ttf'
font_path = personal_path + '/' + font_file

# the size here only affects the tick labels because everything else is set for individual plots
paper_font = fm.FontProperties(fname=font_path, size = 24)

# set position of axis labels
plt.rcParams["xaxis.labellocation"] = 'right'
plt.rcParams["yaxis.labellocation"] = 'top'

# set global parameters with rcParams -- copy whole block below before plotting code to set plotting template globally

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

# set ticks on both sides of x and y axes
plt.rcParams['xtick.top'] = True
plt.rcParams['xtick.bottom'] = True
plt.rcParams['ytick.left'] = True
plt.rcParams['ytick.right'] = True

# define custom styles -- add **set_style to plot, as shown in EXAMPLE PLOT 1 below

# each of these are pretty self-explanatory, can modify them if needed e.g. can set custom markers and colors if different data types are plotted

histogram_style = {
    'histtype': 'step', 
    'color': 'blue',
    'alpha': 0.7,
    'linewidth': 2
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
    'linewidth': 2.5
}

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

# NOTE: The Times New Roman font file does not include greek characters, and is not compatible with mathtext
# For these cases, use the command math_fontfamily = 'stix' as exemplified below, which should result
# in math characters aesthetically similar to TNR
ax.set_xlabel(r'${\Delta}$R (m)', fontproperties=paper_font, math_fontfamily = 'stix', size = 26)
ax.set_ylabel(r'${\alpha \beta \gamma}$', fontproperties=paper_font, math_fontfamily = 'stix', size = 26)

#ax.set_title("Different kinds of plots!! so cool", fontproperties=paper_font, size = 22)

# set font for labels for ticks on both axes; size set in definition of paper_font (it's best not to change it but can change it there if really needed)
for label in ax.get_xticklabels():
    label.set_fontproperties(paper_font)

for label in ax.get_yticklabels():
    label.set_fontproperties(paper_font)

# show legend; remove box around legend, set font properties
ax.legend(frameon=False, prop=fm.FontProperties(fname=font_path, size = 16))

# adjusting the frequency of major ticks on each axis by changing number below, larger number - less dense ticks
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))

# add SNO+ Preliminary label
# parameters: x posiiton of label, y position, text, color, font, font size
# change position and color so that it's visible
# try to leave fontsize as it is for consistency, but can make smaller to suit the plot
ax.text(5.8, 10, "SNO+ Preliminary", color = 'black', fontproperties=paper_font, size = 26)


# there is an issue with saving the plots if you use plt.show() first
# uncomment line below to show plot without saving if needed
#plt.show()

# save to pdf
plt.savefig("example1D_Times.pdf", format="pdf")

# EXAMPLE PLOT 2: color map
fig, ax = plt.subplots()

#can add figsize here if globally set size is not suitable, such as:
#fig, ax = plt.subplots(figsize=(18, 10))

# generate some data to plot
# generate x and y coordinates for a grid
x = np.linspace(0, 1, 30)  # adjust range as needed
y = np.linspace(0, 1, 30)  # adjust range as needed
X, Y = np.meshgrid(x, y)

# arbitrary function of coordinates to plot
data = (X + Y) / 2

# plot as a color map
# viridis is the default and it is colorblind-friendly :)
fig, ax = plt.subplots()
img = ax.imshow(data, cmap='viridis')

# show color map
# pad sets the distance between plot and color bar
# aspect sets aspect ratio of color bar;  increase the number to make it less thick
colorbar = fig.colorbar(img, ax=ax, label='Color Map', pad=0.01, aspect = 12)

# set font properties for colorbar label
colorbar.set_label('Color Map', fontproperties=paper_font)

#set font of tick labels of colorbar

for ticklabel in colorbar.ax.get_yticklabels():
	ticklabel.set_fontproperties(paper_font)

# for Times New Roman, need to set font sizes here instead of as a global params
# NOTE: The Times New Roman font file does not include greek characters, and is not compatible with mathtext
# For these cases, use the command math_fontfamily = 'stix' as exemplified below, which should result
# in math characters aesthetically similar to TNR
ax.set_xlabel(r'${\Delta}$R (m)', fontproperties=paper_font, math_fontfamily = 'stix', size = 26)
ax.set_ylabel(r'${\alpha \beta \gamma}$', fontproperties=paper_font, math_fontfamily = 'stix', size = 26)

#ax.set_title("Color map plot", fontproperties=paper_font, size = 22)

for label in ax.get_xticklabels():
    label.set_fontproperties(paper_font)

for label in ax.get_yticklabels():
    label.set_fontproperties(paper_font)

# add SNO+ Preliminary label
# parameters: x posiiton of label, y position, text, color, font size
# change position and color so that it's visible
# try to leave fontsize as it is for consistency, but can make smaller to suit the plot
ax.text(2.5, 3.5, "SNO+ Preliminary",color = 'white', fontproperties=paper_font, size = 26)

# there is an issue with saving the plots if you use plt.show() first
# uncomment line below to show plot without saving if needed
#plt.show()

# save to pdf
plt.savefig("example2D_Times.pdf", format="pdf")
