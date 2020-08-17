import matplotlib.pyplot as plt
import numpy as np

x = np.array([i for i in range(-1, 1400)])
y = np.full(1401, -1)
z = np.full(1401, -1)
w = np.full(1401, -1)
v = np.full(1401, -1)

y = np.array([j for j in range(-1, 1400)])
print(y)
plt.scatter(x, y, label='skitscat', color='k', s=5)
plt.scatter(x, z, label='skitscat', color='m', s=5)
plt.scatter(x, w, label='skitscat', color='r', s=5)
plt.scatter(x, v, label='skitscat', color='g', s=5)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('digree centrality surface')
plt.legend()
plt.show()
