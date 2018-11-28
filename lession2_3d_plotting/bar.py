# bar.py

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.collections import PolyCollection
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')

np.random.seed(59)
month = np.arange(1, 12)
years = [2016, 2017, 2018, 2019]

def get_color(value_array):
    color = []
    for v in value_array:
        if (v < 50):
            color.append('y')
        elif (v < 100):
            color.append('g')
        elif (v < 150):
            color.append('b')
        elif (v < 200):
            color.append('c')
        elif (v < 250):
            color.append('m')
        else:
            color.append('r')
    return color

for year, c in zip(years, ['b','c','r','m']):
    value = np.random.rand(len(month)) * 300
    ax.bar(month, value, year, zdir='y', color=get_color(value), alpha=0.7)
    for i in np.arange(0, 12):
        ax.bar

ax.set_xlabel('Month')
ax.set_xticks(np.arange(1, 13))
ax.set_ylabel('Year')
ax.set_yticks(np.arange(2016, 2020))
ax.set_zlabel('Precipitation')

plt.show()
