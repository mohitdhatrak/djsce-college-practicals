# matplotlib

import matplotlib.pyplot as plt
import numpy as np

x1 = np.array(["A", "B", "C", "D"])
y1 = np.array([3, 8, 1, 10])
plt.bar(x1, y1)
plt.show()

z1 = np.array([35, 25, 25, 15])
plt.pie(z1)
plt.show()

x2 = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y2 = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
plt.scatter(x2, y2)
plt.show()

z2 = np.random.normal(170, 10, 250)
plt.hist(z2)
plt.show()
