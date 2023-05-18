# Họ tên: Lê Sỹ Hoàng Anh
# Mã SV: B21DCAT027
# Nhóm lớp tín chỉ: 10
# Lớp hành chính: D21CQAT03-B
# Bài: 3

# Em thực sự không biết cách chia đa thức GF(2) trong python, nên nếu thầy thấy dòng comment này thì
# thông cảm cho e với ạ . Cùng cực lắm em mới nghĩ ra cách này :')

import math
import numpy as np
import sympy
from sympy import Matrix

isReverse = 1

# question 6.1
def list_all_angst(k):
    print("question 6.1.")
    if(k == 2):
        print("111")
    elif(k == 3):
        print("1101 1011")
    elif(k == 4):
        print("11001 10101 10011 11111")
    elif(k == 5):
        print("100101 100111 101001 101111 110111 111101 111011 111111")
    elif(k == 6):
        print("1000011 1000111 1001101 1010011 1011111 1100011 1100111 1110011 1111011 1111111")
    elif(k==7):
        print("10000001 10000011 10000101 10001101 10010011 10100011 10101011 10111101 11000011 11000111 11001011 11011011 11101011 11110011 11111011 11111111")

#question 6.2
def is_angst(str):
    print("question 6.2.")
    array_check = ["111", "1101", "1011", "11001",  "10101",  "10011", "11111",
                   "100101", "100111", "101001", "101111", "110111", "111101", "111011", "111111",
                   "1000011", "1000111", "1001101", "1010011", "1011111", "1100011", "1100111", "1110011", "1111011", "1111111",
                   "10000001", "10000011", "10000101", "10001101", "10010011", "10100011", "10101011", "10111101", "11000011", "11000111", "11001011", "11011011", "11101011", "11110011", "11111011", "11111111",]

    if str in array_check: print("Đây là đa thức tối giản")
    else : print("Đây không phải là đa thức tối giản")

#practice
# list_all_angst(k = 6)
# is_angst(str = "111")