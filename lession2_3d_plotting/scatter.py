# scatter.py

import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')

count = 100
range = 100

xs = np.random.rand(count) * range
ys = np.random.rand(count) * range
zs = np.random.rand(count) * range

ax.scatter(xs, ys, zs, s=zs, c=zs)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
