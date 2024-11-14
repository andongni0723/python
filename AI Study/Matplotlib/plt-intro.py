import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode Ms']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

data_lst = [1, 2, 3, 4]
stock1 = [4, 8, 2, 6]
stock2 = [10, 12, 5, 3]

plt.plot(data_lst, stock1, "ro--", label="股票代碼:abc")
plt.plot(data_lst, stock2, "b^--", label="股票代碼:edf")
plt.title("折線圖")
plt.xlabel("時間")
plt.legend()  # 圖例

# plot() format
'''
(r.-) red, dot, line
(go--) green, big dot, dotted line(虛線)
(k+-.) black, plus dot, line + dotted line
(c*:) sky blue, star dot, dot line 
(bs) blue, square (no line)
'''

# more graph type
'''
plot(x, y)
scatter(x, y) 
bar(x, height) / barh(y, width)
stem(x, y)
step(x, y)
fill_between(x, y1, y2)
'''

# arrays and fields
'''
imshow(Z) # grid graph
pcolormesh(x, y, z)
contour(x, y, z)
contourf(x, y, z)
barbs(x, y, u, v)  # wind direction graph
quiver(x, y, u, v)
streamplot(x, y, u, v) # weather line graph
'''

# 刻度
plt.xticks([1, 2, 3, 4])
plt.yticks(np.arange(2, 13, 1))
plt.grid()  # 格子


# set the show scope
plt.xlim(2.5, 4.5)
plt.ylim(1.5, 6.5)
plt.show()


def calc_model_output(w, b, x):
    m = x.shape
    f_wb = np.zeros(m)
    for i in range(len(x)):
        f_wb = w * x[i] + b

    return f_wb
