# wireframe.py

import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.arange(-10, 10, 0.1)
y = np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(x, y)

Z = np.add(-np.power(X, 3), np.power(Y, 4))

surf = ax.plot_wireframe(X, Y, Z)

plt.show()
