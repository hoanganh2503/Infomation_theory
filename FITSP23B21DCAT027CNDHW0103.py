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
codewords2 = ["1", "01", "001", "000"]

# question 3.1
def check_features():
    # check for even/uneven properties
    is_uniform = all(len(word) == len(codewords[0]) for word in codewords)
    if(is_uniform == False): print("Bộ mã không đều.\n")
    else: print("Bộ mã đều.\n")

    # Kiểm tra tính prefix
    is_prefix = all(word1 != word2[:len(word1)] for i, word1 in enumerate(codewords) for word2 in codewords if i != codewords.index(word2))
    if is_prefix:
        print("Bộ mã có tính prefix.")
    else:
        print("Bộ mã không có tính prefix.")    

# question 3.5
def is_permutation(codewords1, codewords2):
    if sorted(codewords1) == sorted(codewords2): print("Đây là 2 hoán vị của nhau")
    else: print("Đây không phải là 2 hoán vị của nhau")


#practice
# check_features()
is_permutation(codewords1 = codewords , codewords2 = codewords2)