# Họ tên: Lê Sỹ Hoàng Anh
# Mã SV: B21DCAT027
# Nhóm lớp tín chỉ: 10
# Lớp hành chính: D21CQAT03-B
# Bài: 5

import math
import numpy as np
import sympy
from sympy import Matrix
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def limited_Griesmer_code():
    print("Giới hạn Griesmer.")
    Dk = Ddmin = 1
    # Khởi tạo trục tọa độ 
    x = np.arange(0,40+Dk, Dk)
    y = np.arange(0, 40+Ddmin, Ddmin)
    z = []

    for i in x:
        z1 = []
        for j in y:
            distances = 0
            for k in range(0, i):
                distances += math.floor(j / (2**k))
            z1.append((distances))
        z.append(z1)

    k = int(input("Nhập k:"))
    dmin = int(input("Nhập dmin:"))
    print("Độ dài từ mã tối thiểu của bộ mã thỏa mãn giới hạn Griesmer:", z[k][dmin])

    X, Y = np.meshgrid(x, y)
    Z = np.array(z)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.7)

    ax.set_xlabel('k')
    ax.set_ylabel('Dmin')
    ax.set_zlabel('l minimum')

    plt.show()

def limited_Plotkin_code():
    print("Giới hạn Plotkin.")
    Dl = Dk = 1
    x = np.arange(0, 20+Dk, Dk)
    y = np.arange(0, 20+Dl, Dl)
    z = []
    for i in x:
        z1 = []
        for j in y:
            distances = -1
            if i != 0 and j >= i:
                distances = math.floor((j * int(math.pow(2, i-1))) / int(math.pow(2, i) - 1))
            z1.append(distances)
        z.append(z1)

    k = int(input("Nhập k:"))
    l = int(input("Nhập l:"))
    print("Độ dài từ mã tối thiểu của bộ mã thỏa mãn giới hạn Griesmer:", z[k][l])
    X, Y = np.meshgrid(x, y)
    Z = np.array(z)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.7)

    ax.set_xlabel('k')
    ax.set_ylabel('l')
    ax.set_zlabel('dmin minimum')
    plt.show()

def limited_Hamming_code():
    print("Giới hạn Hamming.")
    Dl = Dk = 1
    x = np.arange(0, 20+Dk, Dk)
    y = np.arange(0, 20+Dl, Dl)
    z = []
    for i in x:
        z1 = []
        for j in y:
            distances = -1
            if i != 0 and j >= i:
                distances = math.floor(j - i + 1)
            z1.append(distances)
        z.append(z1)

    k = int(input("Nhập k:"))
    l = int(input("Nhập l:"))
    print("Độ dài từ mã tối đa của bộ mã thỏa mãn giới hạn Hamming:", z[k][l])
    X, Y = np.meshgrid(x, y)
    Z = np.array(z)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.7)

    ax.set_xlabel('k')
    ax.set_ylabel('l')
    ax.set_zlabel('dmin minimum')
    plt.show()


#practice
limited_Griesmer_code()
limited_Plotkin_code()
limited_Hamming_code()