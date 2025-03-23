# -*- coding: utf8 -*-
from vpython import *
import matplotlib.pyplot as plt

# 1. 參數設定
# 加速度
g = 9.8
a = vector(0, -g, 0)  # 加速度值，在 x、z 方向為 0，在 y 方向為 g=-9.8 公尺/秒^2
# 速度
ballv = vector(6, 10, 0)  # 球的初速度（公尺/秒）
# 高度
h = 3  # 球的初始高度，單位為公尺
# 時間間隔
dt = 0.01  # 畫面更新的時間間隔，單位為秒
# 經過時間
t = 0  # 模擬所經過的時間，單位為秒，初始值為0

# 2. 畫面設定
scene = canvas(center=vector(0, h / 2, 0), background=vector(0.5, 0.6, 0))

# 參考地板和牆壁
floor = box(pos=vector(0, 0, 0), length=15, height=0.005, width=5)
wall1 = box(pos=vector((floor.length) / 2, 5, 0), length=0.005, height=10, width=5)
wall2 = box(pos=vector(-(floor.length) / 2, 5, 0), length=0.005, height=10, width=5)

# 球
ball = sphere(pos=vector(0, h, 0), radius=0.2, color=color.yellow, make_trail=True, retain=50)

# 儲存時間和位移資料以繪圖
time_data = []
y_data = []
x_data = []

while t < 20:
    rate(100)
    # 更新球的位置和速度
    ballv += a * dt
    ball.pos += ballv * dt

    # 收集資料
    time_data.append(t)
    y_data.append(ball.pos.y)
    x_data.append(ball.pos.x)

    # 邊界反彈
    if ball.pos.y <= 0 and ballv.y < 0:
        ballv.y = -ballv.y  # 反轉 y 方向速度

    if abs(ball.pos.x) >= floor.length / 2:
        ballv.x = -ballv.x  # 反轉 x 方向速度

    t += dt

# 3. 使用 matplotlib 繪製 y-t 和 x-t 圖表
plt.figure(figsize=(12, 5))

# y-t 圖表
plt.subplot(1, 2, 1)
plt.plot(time_data, y_data, label="y-t 曲線", color="yellow")
plt.xlabel("時間 (s)")
plt.ylabel("高度 y (m)")
plt.title("y-t 圖表")
plt.ylim(-10, 10)
plt.grid(True)

# x-t 圖表
plt.subplot(1, 2, 2)
plt.plot(time_data, x_data, label="x-t 曲線", color="yellow")
plt.xlabel("時間 (s)")
plt.ylabel("水平位置 x (m)")
plt.title("x-t 圖表")
plt.ylim(-10, 10)
plt.grid(True)

plt.tight_layout()
plt.show()