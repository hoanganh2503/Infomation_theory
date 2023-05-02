# Họ tên: Lê Sỹ Hoàng Anh
# Mã SV: B21DCAT027
# Nhóm lớp tín chỉ: 10
# Lớp hành chính: D21CQAT03-B
# Bài: 8    

import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# question 8.1
def calculater_entropy():
    p = float(input("Nhập p: "))
    q = float(input("Nhập q: "))
    r = float(input("Nhập r: "))
    ans = -(p * math.log2(p) + q * math.log2(q) + r * math.log2(r))
    print("Entropy của nguồn rời rạc không nhớ có giá trị bằng: ", ans)


# question 8.2
def change_value_entropy():
    dx = dy = 0.001

    # Khởi tạo trục tọa độ 
    x = np.arange(0, 1+dx, dx)
    y = np.arange(0, 1+dy, dy)

    X, Y = np.meshgrid(x, y)
    Z = -(X * np.log2(X) + Y * np.log2(Y) + (1-X-Y) * np.log2(1-X-Y))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.7)

    # Đặt tên cho trục tọa độ
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()


# question 8.3
def find_entropy_max():
    dz = 0.001

    # Khởi tạo trục tọa độ 
    z = np.arange(0, 1+dz, dz)
    x = y = (1-z)/2

    X, Y = np.meshgrid(x, y)
    Z = -(X * np.log2(X) + Y * np.log2(Y) + (1-X-Y) * np.log2(1-X-Y))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.7)

    # Đặt tên cho trục tọa độ
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# practice
calculater_entropy()
change_value_entropy()
find_entropy_max()
