# line.py

import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
z = np.add(x, y)

ax.plot(x, y, z)
plt.show()
