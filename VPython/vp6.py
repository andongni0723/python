# from visual import *
from vpython import *

# 參數設定, 設定變數及初始值, 當 h << d 時週期理論值 3.84669 s

size = 1  # 小球半徑
m = 1  # 小球質量
M = 2E13  # 星球質量
d = 10  # 星球之間的距離*0.5倍
h = 0.8  # 小球在星球連線的中垂線上的距離
G = 6.67E-11  # 重力常數
v0 = 0  # 小球初速
i = 0  # 小球回到初位置的次數
t = 0  # 時間
t0 = 0
dt = 0.0001  # 時間間隔
T = 3.84668793868  # 週期理論值
# print '週期理論值 =', T
print('週期理論值 =', T)

# 畫面設定

# 產生動畫視窗
# scene = display(title='Gravity and SHM', width=600, height=600, x=0, y=0, center=vector(0, 0, 0), background=color.black, range=1.3 * d)
scene = canvas(title='Gravity and SHM', width=600, height=600, x=0, y=0, center=vector(0, 0, 0), background=color.black,
               range=1.3 * d)
# 產生 2 個質量為 M 的星球
s1 = sphere(pos=vector(-d, 0, 0), radius=size, color=color.blue)  # 左星球
s2 = sphere(pos=vector(d, 0, 0), radius=size, color=color.blue)  # 右星球
# 產生質量為 m 的星球並設定初速度
ball = sphere(pos=vector(0, h, 0), radius=0.4 * size, color=color.red)
ballv = vector(0, v0, 0)
# 畫星球間的連線、上端點、下端點
line = cylinder(pos=s1.pos, axis=s2.pos - s1.pos, radius=0.1 * size, color=color.yellow)
top = cylinder(pos=vector(-2, h, 0), axis=vector(4, 0, 0), radius=0.1 * size, color=color.white)
bottom = cylinder(pos=vector(-2, -h, 0), axis=vector(4, 0, 0), radius=0.1 * size, color=color.white)
# 產生表示速度、加速度的箭頭
arrow_v = arrow(pos=ball.pos + vector(1, 0, 0), axis=vector(0, 0, 0), shaftwidth=0.3 * size, color=color.green)
arrow_a = arrow(pos=ball.pos + vector(2, 0, 0), axis=vector(0, 0, 0), shaftwidth=0.3 * size, color=color.magenta)


def mp(x):
    return x.x ** 2 + x.y ** 2 + x.z ** 2


first = True
# 物體運動部分
while 1:
    rate(10000)

    p1 = ball.pos.y

    # 將 r1 設定為左星球到小球的向量
    r1 = ball.pos - s1.pos
    # 將 r2 設定為右星球到小球的向量
    r2 = ball.pos - s2.pos
    # 將 F1 設定為左星球對小球的吸引力(注意方向)
    F1 = -(G * M * m) / mp(r1) * norm(r1)
    # 將 F2 設定為右星球對小球的吸引力(注意方向)
    F2 = -(G * M * m) / mp(r2) * norm(r2)
    F = F1 + F2

    # 計算運動中小球的加速度、速度、位置, 畫出代表速度、加速度的箭頭
    balla = F / m
    ballv += balla * dt
    ball.pos += ballv * dt
    arrow_v.pos = ball.pos + vector(1, 0, 0)
    arrow_a.pos = ball.pos + vector(2, 0, 0)
    arrow_v.axis = ballv
    arrow_a.axis = balla
    # 判斷小球是否回到出發點

    p2 = ball.pos.y
    if p1 > 0.79 and p2 < 0.79:
        if first:
            t0 = t  # 記錄第一次回到起點的時間
            first = False
        else:
            T = t - t0  # 計算週期
            print('T =', T)
            t0 = t
    else:
        trigger = True


    t += dt
