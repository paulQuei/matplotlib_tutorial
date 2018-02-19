# test8.py

import matplotlib.pyplot as plt
import numpy as np

data = [np.random.randint(0, n, n) for n in [3000, 4000, 5000]]
labels = ['3K', '4K', '5K']
bins = [0, 100, 500, 1000, 2000, 3000, 4000, 5000]

plt.hist(data, bins=bins, label=labels)
plt.legend()

plt.show()
