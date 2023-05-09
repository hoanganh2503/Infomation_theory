# Họ tên: Lê Sỹ Hoàng Anh
# Mã SV: B21DCAT027
# Nhóm lớp tín chỉ: 10
# Lớp hành chính: D21CQAT03-B
# Bài: 4

import math
import numpy as np
import sympy
from sympy import Matrix

H = [[1,0,1,1,1,0,0],
     [0,1,0,1,1,1,0],
     [0,0,1,0,1,1,1]]

# question 4.1
def find_dmin_focus_on_column():
    print("Question 4.1:")
    A = np.array(H)
    num_cols = len(A[0])
    distances = []
    for i in range(num_cols):
        for j in range(i+1, num_cols):
            col1 = A[:,i]
            col2 = A[:,j]
            distance = np.count_nonzero(col1 != col2)
            distances.append(distance)
    dmin = min(distances)
    print("dmin tìm được theo số cột của ma trận:", dmin)


# question 4.2
def check_codeword_valid():
    print("\nQuestion 4.2:")
    vector = []
    # define amount input = 7, else return false
    for i in range(0, 7):
        a = input()
        vector.append(int(a))
    if( np.sum(np.count_nonzero( (vector @ np.transpose(H)) % 2 == 1)) == 0):
        print("Đây là từ mã hợp lệ.")
    else: print("Đây là từ mã không hợp lệ.")

#question 4.3
def list_codewords():
    print("\nQuestion 4.3:")
    string_binary = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    codewords = []
    for i in string_binary:
        result = np.matmul(i, H)
        # print(result)
        for j in range(0, len(result) - 1):
            if(result[j] % 2 == 0): result[j] = 0
            else: result[j] = 1
        codewords.append(list(result))
    
    print("Bộ từ mã của ma trận H:")
    for i in codewords:
        print(i)


# question 4.4
def distance_hammming(x, y):
    return np.sum(x != y)

def find_dmin_by_define():
    print("\nQuestion 4.4:")
    H_cols = np.transpose(H)
    row = H_cols.shape[0]
    dmin = 10**9
    for i in range (0, row-1):
        for j in range (i+1, row):
            dmin = min(dmin, distance_hammming(H_cols[i], H_cols[j]))

    print("dmin tìm được theo định nghĩa:", dmin)
    

#question 4.5
def distance_liner_block_cipher_hammming(x):
    y = [0, 0, 0]
    return np.sum(x != y)

def find_dmin_by_property_of_liner_block_cipher():
    print("\nQuestion 4.5:")
    H_cols = np.transpose(H)
    dmin = 10**9
    for i in H_cols:
        dmin = min(dmin, distance_liner_block_cipher_hammming(i))
    print("dmin tìm được theo tính chất của mã khối tuyến tính:", dmin)


# practice

find_dmin_focus_on_column()
check_codeword_valid()
list_codewords()
find_dmin_by_define()
find_dmin_by_property_of_liner_block_cipher()