import numpy as np
import matplotlib.pyplot as plt

data = np.array([1, 2, 3, 4, 5])
value_y = np.array([1, 2, 3, 4, 5])
m = data.size
alpha = 0.001
w = b = 0
tw = tb = 1


def sigma(_x: np.ndarray, _y: np.ndarray, _w, _b, _m, _mode):
    """
    :param _mode:  1: for w, 2: for b
    :return: the result about sigma calculator
    """
    result = 0
    for i in range(_m):
        error = (_x[i] * _w + _b - _y[i])
        match _mode:
            case 1:
                result += error * _x[i]
            case 2:
                result += error

    return result


# fwb(x) = wx + b
# w = w - a d/dw(1/2m)(m sigma i=1)(fwb(xi) - yi)^2
# w = w - a (1/m)(m sigma i=1)(fwb(xi) - yi)xi
# b = b - a d/db(1/2m)(m sigma i=1)(fwb(xi) - yi)^2
# b = b - a (1/m)(m sigma i=1)(fwb(xi) - yi)
threshold = 1e-6
prev_w = prev_b = float('inf')
while not (abs(w - prev_w) < threshold and abs(b - prev_b) < threshold):
    prev_w, prev_b = w, b
    tw = w - alpha * (1 / m) * sigma(data, value_y, w, b, m, 1)
    tb = b - alpha * (1 / m) * sigma(data, value_y, w, b, m, 2)
    w, b = tw, tb

print(f"w = {w} , b = {b}")

# Draw
point_x = np.linspace(0, 10, 10)
pre_y = w * point_x + b
plt.plot(data, value_y, "bo", label="Real De")
plt.plot(point_x, pre_y, "r--", label="預測直線")
plt.title(f"predict w = {w:.5f} , b = {b:.5f}")
plt.xlabel("feature")
plt.ylabel("value")
plt.legend()
plt.show()

