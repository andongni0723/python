import numpy as np

# 創建一個 4x4 的隨機數組，選擇其第三列的所有元素。
arr1 = np.random.rand(4, 4)
print(arr1)
# print(arr1[2:3, :])
print(arr1[:, 2])

# 創建一個包含數字 1 到 20 的一維數組，選擇其中所有的偶數。
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print(arr2[arr2 % 2 == 0])

# 將一個一維數組 [1, 2, 3, 4, 5, 6, 7, 8] 轉換為 2x4 的二維數組。
arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
arr3 = arr3.reshape(2, 4)
print(arr3)

# 創建兩個 3x3 的隨機數組，並計算它們的元素積（逐元素相乘）和矩陣乘法。
arr4 = np.random.rand(3, 3)
arr42 = np.random.rand(3, 3)
print(arr4 * arr42)
print(np.dot(arr4, arr42))

# 將一個包含數字 1 到 9 的 3x3 數組展平成一維數組。
arr5 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr5.flatten())
