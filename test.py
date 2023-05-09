import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import numpy as np

dx = dy = 1

# Khởi tạo trục tọa độ 
x = np.arange(0, 4+dx, dx)
y = np.arange(0, 4+dy, dy)
a1, b1 = np.meshgrid(x, y)

c = [[0, 0, 0, 0, 0],
     [0, 1, 2, 3, 4],
     [0, 1, 3, 4, 6],
     [0, 1, 3, 4, 7],
     [0, 1, 3, 4, 7]]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = a1
Y = b1
Z = np.array(c)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.7)
ax.set_xlabel('A Label')
ax.set_ylabel('B Label')
ax.set_zlabel('C Label')

plt.show()