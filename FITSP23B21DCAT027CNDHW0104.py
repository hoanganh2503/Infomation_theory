# Họ tên: Lê Sỹ Hoàng Anh
# Mã SV: B21DCAT027
# Nhóm lớp tín chỉ: 10
# Lớp hành chính: D21CQAT03-B
# Bài: 4

import math
import numpy as np

H = [[1,0,1,1,1,0,0],
     [0,1,0,1,1,1,0],
     [0,0,1,0,1,1,1]]

# question 4.1
def find_dmin_focus_on_column():
    print(H)

# question 4.2
def distance_hammming(x, y):
    return np.sum(x != y)

def find_dmin_by_define():
    H_cols = np.transpose(H)
    row = H_cols.shape[0]
    dmin = 10**9
    for i in range (0, row-1):
        for j in range (i+1, row):
            dmin = min(dmin, distance_hammming(H_cols[i], H_cols[j]))

    print("dmin tìm được theo định nghĩa:", dmin)





# practice

# find_dmin_focus_on_column()
find_dmin_by_define()