# contour.py

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.arange(-10, 10, 0.1)
y = np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(x, y)

Z = np.add(-np.power(X, 4), np.power(Y, 4))

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.plot_wireframe(X, Y, Z, alpha=0.1)
ax.contour(X, Y, Z, cmap=cm.Accent, linewidths=2)

plt.show()