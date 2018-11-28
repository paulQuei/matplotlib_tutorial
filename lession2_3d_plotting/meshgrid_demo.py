# meshgrid_demo.py

import numpy as np

x = np.arange(1, 4)
y = np.arange(11, 16)
print(x)
print(y)

X, Y = np.meshgrid(x, y)
print(X)
print(Y)
