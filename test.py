import numpy as np

# Định nghĩa bộ mã
my_code = ['1', '01', '001', '000']

# Chuyển đổi bộ mã thành một ma trận
matrix = np.array([list(map(int, list(word))) for word in my_code])

# Tính số từ mã trong bộ mã
n = len(my_code)

# Kiểm tra từ mã có thể được tạo thành từ tổ hợp tuyến tính của các từ mã khác trong bộ mã hay không
test_codeword = '011'
test_vector = np.array(list(map(int, list(test_codeword))))
for i in range(n):
    A = matrix.copy()
    A[:, i] = test_vector
    if np.linalg.matrix_rank(A) == n:
        coeffs = np.linalg.solve(matrix, test_vector)
        if any(coeffs != 0):
            print(f"The codeword {test_codeword} can be formed as a linear combination of the codewords in the code.")
            break
else:
    print(f"The codeword {test_codeword} cannot be formed as a linear combination of the codewords in the code.")