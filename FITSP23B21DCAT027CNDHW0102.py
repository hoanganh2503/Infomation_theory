# Họ tên: Lê Sỹ Hoàng Anh
# Mã SV: B21DCAT027
# Nhóm lớp tín chỉ: 10
# Lớp hành chính: D21CQAT03-B
# Bài: 2

import math
import numpy as np
import sympy
from sympy import Matrix

elsym = ['x_1','x_2','x_3','x_4']
elprob = [0.125,0.25,0.125,0.5]
elcodeword = ['000','01','001','1']

# question 2.1
def encode_source_by_huffman():
    
    sigma_l_2 = avg_l = 0
    for i in range(0, 4):
        avg_l += elprob[i] * len(elcodeword[i])
        
    for i in range(0, 4):
        sigma_l_2 += elprob[i] * (len(elcodeword[i]) - avg_l)**2
        
    print("source: X")
    print("elsym:", elsym)
    print("elprob:", elprob)
    print("elcodeword:", elcodeword)
    print("avg_l:", avg_l)
    print("sigma_l_2:", sigma_l_2)
    print("isNewLess:", 1)
    print("isLeftBrachZero:", 1)

def encode_text():
    s = input("Vui lòng chỉ nhập các kí tự dạng x_1 x_2 x_3 x_4:")
    integers = s.split('x_')
    for i in integers:
        if(i):
            print(elcodeword[int(i)-1], end = '')

#practice
# encode_source_by_huffman()
encode_text()