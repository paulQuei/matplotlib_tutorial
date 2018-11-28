# poly.py

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.collections import PolyCollection
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')

np.random.seed(59)
month = np.arange(0, 13)
years = [2016, 2017, 2018, 2019]

precipitation = []
for year in years:
    value = np.random.rand(len(month)) * 300
    value[0], value[-1] = 0, 0
    precipitation.append(list(zip(month, value)))

poly = PolyCollection(precipitation, facecolors=['b','c','r','m'])
poly.set_alpha(0.7)

ax.add_collection3d(poly, zs=years, zdir='y')
ax.set_xlabel('Month')
ax.set_xlim3d(0, 12)
ax.set_ylabel('Year')
ax.set_ylim3d(2015, 2020)
ax.set_zlabel('Precipitation')
ax.set_zlim3d(0, 300)

plt.show()
