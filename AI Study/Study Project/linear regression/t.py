import numpy as np
import matplotlib.pyplot as plt

data = np.array([1, 2, 3, 4, 5])  # 輸入數據
value_y = np.array([1, 2, 3, 4, 5])  # 標籤數據

m = data.size  # 數據點數量
alpha = 0.01  # 學習率
w = b = 0  # 初始參數
tw = tb = 1  # 用於檢查收斂

# 梯度計算函數
def sigma(_x: np.ndarray, _y: np.ndarray, _w, _b, _m, _mode):
    """
    計算梯度（偏導數）:
    - _mode: 1 -> 對 w 偏導, 2 -> 對 b 偏導
    """
    result = 0
    for i in range(_m):
        error = (_x[i] * _w + _b - _y[i])
        match _mode:
            case 1:  # 對 w 偏導
                result += error * _x[i]
            case 2:  # 對 b 偏導
                result += error
    return result

# 梯度下降
threshold = 1e-6  # 收斂判斷閾值
while not (abs(w - tw) < threshold and abs(b - tb) < threshold):
    # 注意公式中的 2m，修正梯度公式
    tw = w - alpha * (1 / m) * sigma(data, value_y, w, b, m, 1)
    tb = b - alpha * (1 / m) * sigma(data, value_y, w, b, m, 2)
    w, b = tw, tb

# 輸出結果
print(f"w = {w:.6f}, b = {b:.6f}")

# 繪製結果
point_x = np.linspace(0, 10, 100)
pre_y = w * point_x + b

plt.plot(data, value_y, "bo", label="Data Points")
plt.plot(point_x, pre_y, "r--", label=f"y = {w:.2f}x + {b:.2f}")
plt.title("Linear Regression using Gradient Descent")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(alpha=0.3)
plt.show()