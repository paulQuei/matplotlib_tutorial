# pie.py

import matplotlib.pyplot as plt
import numpy as np

labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

data = np.random.rand(7)

plt.pie(data, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.legend()

plt.show()