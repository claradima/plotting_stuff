# Example code with the SNO+ collaboration plot style adapted to Python
# Requires the file Times_New_Roman_Normal.ttf
# By Ana Sofia Inacio (ainacio@lip.pt)
# This example was tested with Python-3.9
# In case of problems, contact me or Jeanne Wilson (jeanne.wilson@kcl.ac.uk)

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.ticker import MultipleLocator

import sys

import matplotlib.font_manager as fm
prop_font = fm.FontProperties(fname='Times_New_Roman_Normal.ttf',size = 28)

#matplotlib.rcParams.update({'font.family': 'serif'})
matplotlib.rcParams.update({'font.size': 28})
matplotlib.rcParams.update({'font.style': "normal"})

matplotlib.rcParams['xtick.major.size'] = 10
matplotlib.rcParams['xtick.major.width'] = 2
matplotlib.rcParams['xtick.minor.size'] = 5
matplotlib.rcParams['xtick.minor.width'] = 1
matplotlib.rcParams['ytick.major.size'] = 10
matplotlib.rcParams['ytick.major.width'] = 2
matplotlib.rcParams['ytick.minor.size'] = 5
matplotlib.rcParams['ytick.minor.width'] = 1
matplotlib.rcParams['axes.linewidth'] = 5 #set the value globally
matplotlib.rcParams['figure.facecolor'] = 'white'
matplotlib.rcParams['figure.figsize'] = 18, 10
matplotlib.rcParams['xtick.major.pad']='12'
matplotlib.rcParams['ytick.major.pad']='12'

# Example:
x = [1,2,3,4,5]
y = [1,2,3,4,5]

fig = plt.subplot(111)
ax1 = plt.gca()
##ax1.ticklabel_format(style='sci', scilimits=(0,0), axis='y',fontproperties=prop_font) 
#ax1.ticklabel_format(axis='y',style=prop_font) 
ax1.set_xlabel('X axis',fontproperties=prop_font,size = 32,x=1, ha='right')
ax1.set_ylabel('Y axis',fontproperties=prop_font,size = 32,y=1, ha='right')

ax1.plot(x, y, label="This is an example")

for label in ax1.get_xticklabels():
    label.set_fontproperties(prop_font)

for label in ax1.get_yticklabels():
    label.set_fontproperties(prop_font)


# make legend
handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles, labels,loc='upper left', fancybox=False, numpoints=1,prop=prop_font,frameon=False)

ax1.minorticks_on()

ax1.get_xaxis().set_tick_params(which='both',direction='in', width=1)
ax1.get_yaxis().set_tick_params(which='both',direction='in', width=1)
ax1.xaxis.set_ticks_position('both')






plt.show()
