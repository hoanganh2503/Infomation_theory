import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Hàm tính Entropy của nguồn
def entropy(p, q, r):
    return -p*np.log2(p) - q*np.log2(q) - r*np.log2(r)

# Khởi tạo các giá trị p, q, r
p_values = np.linspace(0, 1, 10)
q_values = np.linspace(0, 1, 10)
r_values = np.linspace(0, 1, 10)

# Tính Entropy tương ứng với từng bộ giá trị p, q, r
entropy_values = np.zeros((len(p_values), len(q_values), len(r_values)))
for i, p in enumerate(p_values):
    for j, q in enumerate(q_values):
        for k, r in enumerate(r_values):
            entropy_values[i,j,k] = entropy(p, q, r)

# Hiển thị đồ thị 3D của các giá trị Entropy tương ứng
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(p_values, q_values)
for k in range(len(r_values)):
    Z = entropy_values[:,:,k]
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('p')
    ax.set_ylabel('q')
    ax.set_zlabel('Entropy')
    ax.set_title('Entropy of (p, q, r={:.2f})'.format(r_values[k]))
    plt.show()