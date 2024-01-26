import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.font_manager as fm
import numpy as np

# Set the font properties
paper_font = fm.FontProperties(fname='Times_New_Roman_Normal.ttf', size = 16)

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

ax.set_xlabel('This is the x axis', fontproperties=paper_font, size = 20)
ax.set_ylabel('This is the y axis', fontproperties=paper_font, size = 20)
ax.set_title("Different kinds of plots!! so cool", fontproperties=paper_font, size = 28)


for label in ax.get_xticklabels():
    label.set_fontproperties(paper_font)

for label in ax.get_yticklabels():
    label.set_fontproperties(paper_font)

#make legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles = handles, labels = labels, prop=paper_font)


plt.show()

# Second plot: color map
fig, ax = plt.subplots()

data = np.random.random((10, 10))
img = ax.imshow(data, cmap='viridis')
colorbar = fig.colorbar(img, ax=ax, label='Color Map')  # Add colorbar to the figure
# Set font properties for colorbar label
colorbar.set_label('Color Map', fontproperties=paper_font)


ax.set_xlabel('This is the x axis', fontproperties=paper_font, size = 20)
ax.set_ylabel('This is the y axis', fontproperties=paper_font, size = 20)
ax.set_title("Color map plot", fontproperties=paper_font, size = 28)

for label in ax.get_xticklabels():
    label.set_fontproperties(paper_font)

for label in ax.get_yticklabels():
    label.set_fontproperties(paper_font)

plt.show()


