# Họ tên: Lê Sỹ Hoàng Anh
# Mã SV: B21DCAT027
# Nhóm lớp tín chỉ: 10
# Lớp hành chính: D21CQAT03-B
# Bài: 3

import math
import numpy as np
import sympy
from sympy import Matrix

codewords = ["1", "01", "001", "000"]

# question 3.1
def check_features():
    # check for even/uneven properties
    check_even = 0
    for i in range(0, len(codewords)-1):
        if(len(codewords[i]) != len(codewords[i+1])):
            check_even = 1
            break
    if(check_even == 1): print("Bộ mã không đều.\n")
    else: print("Bộ mã đều.\n")

    # check singular/non-singular properties
    check_singular = 0
    for i in range(1, len(codewords)):
        for j in range(0, i):
            if(codewords[i] == codewords[j]):
                check_singular = 1
                break
    if(check_singular == 0): 
        print("Bộ mã không suy biến.\nVí dụ:")
        # get example
        x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm']
        for i in range(0, len(codewords)):
            print (x[i], "được mã hóa từ", codewords[i])
    else: print("Bộ mã suy biến.")
    print("\n")

    check_uniquely_decodable = 0






#practice
check_features()