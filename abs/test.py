import numpy as np

# 3x3の行列を定義
A = np.array([
    [1, -1, -1], 
    [1, 1, 0], 
    [1, 0, 1]
])
B = np.array([
    [-1, 0, 0], 
    [0, 1, 0], 
    [0, 0, 1]
])
C = np.array([
    [1, 1, 1], 
    [-1, 1, 0], 
    [-1, 0, 1]
])

import numpy as np

# 行列の定義
D = np.array([
    [np.sqrt(2), np.sqrt(2), np.sqrt(2)], 
    [-np.sqrt(3), np.sqrt(3), 0], 
    [-1, -1, 2]
]) / np.sqrt(6)

E = np.array([
    [-1, 0, 0], 
    [0, 1, 0], 
    [0, 0, 1]
])

F = np.array([
    [np.sqrt(2), -np.sqrt(3), -1], 
    [np.sqrt(2), np.sqrt(3), -1], 
    [np.sqrt(2), 0, 2]
]) / np.sqrt(6)

# 行列の積を計算
result = np.dot(np.dot(F, E), D)

# 結果を出力
print("D =\n", D)
print("E =\n", E)
print("F =\n", F)
print("F * E * D =\n", result)
