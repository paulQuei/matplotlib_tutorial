# surface_files.py

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.gca(projection='3d')

x = np.arange(-10, 10, 0.1)
y = np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(x, y)

Z = np.add(-np.power(X, 4), np.power(Y, 4))

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.plot_surface(X, Y, Z, cmap=cm.hsv)

for angle in range(95, 180, 3):
    ax.set_zlabel("Angle: " + str(angle))
    ax.view_init(30, angle)
    filename = "./" + str(angle) + ".png"
    plt.savefig(filename)
    print("Save " + filename + " finish")