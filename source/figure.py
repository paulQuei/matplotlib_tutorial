# figures.py

import matplotlib.pyplot as plt
import numpy as np

data = np.arange(100, 201)
plt.plot(data)

data2 = np.arange(200, 301)
plt.figure()
plt.plot(data2)

plt.show()