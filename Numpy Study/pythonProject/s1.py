import numpy as np

# 創建一個 3x3 的數組，裡面的值全部為 7。
arr1 = np.ones((3, 3)) * 7
print(arr1)
# 創建一個 5x5 的單位矩陣。
arr2 = np.eye(5, 5)
print(arr2)

# 創建一個包含數字 1 到 10 的一維數組，並計算該數組的平均值。
arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr3.mean())

# 將數組 arr4 = np.array([3, 6, 9, 12]) 乘以 2，並輸出結果。
arr4 = np.array([3, 6, 9, 12]) * 2
print(arr4)

# 創建一個隨機生成的 4x4 數組，並找到其最大值和最小值。
arr5 = np.random.rand(4, 4)
print(arr5.max(), arr5.min())
