# from visual import *
# from visual.graph import *
from vpython import *
# import numpy as

# 1. 畫面設定
# scene = display(width=1000, height=1000, background=(0.5,0.6,0.5))
# table = cylinder(pos=(0,0,0), axis=(0,0,0.02), radius=2.2, material=materials.wood)
ball = sphere(radius=0.08, color=color.blue, pos = (0, 2, 0.1))
rod = cylinder(pos=(0, 0, 0.02+0.08), axis = (0, 2, 0.02+0.08), radius = 0.007)
# 2. 參數設定
m = 1.
R = 2
dt = 0.00005
t = 0
g = 9.8
n = 1.5 #最高點速率至少(gr)^0.5
v0 = (n*g*R)**0.5 #初速率
ballv = vector(v0,0,0) #初速度(向量)
varrow = arrow(pos=ball.pos,color=color.green)
aarrow = arrow(pos=ball.pos,color=color.red)
a_label = label(text='a', height=15, opacity = 0, box= False)
v_label = label(text='v', height=15, opacity = 0, box= False)
# 3. 產生繪圖視窗
# gdE = gdisplay(title="E-t plot", width=600, height=450, x=0, y=600, xtitle="t (s)", ytitle="E (J)")
# Ugt = gcurve(gdisplay=gdE, color=color.yellow)
# Ekt = gcurve(gdisplay=gdE, color=color.blue)
# Et = gcurve(gdisplay=gdE, color=color.red)


t0 = 0
isFirst = False
while True:
    rate(5000)
    rod.axis = ball.pos + vector(0,0,-0.08)
    sinsita = ball.pos.x/R
    v = (v0**2 + 2*g*(R - ball.pos.y))**0.5
    balla = (v**2/R)*(rod.pos-ball.pos)/abs(rod.pos-ball.pos)+g*sinsita*ballv/abs(ballv)
    # 法線加速度(v**2/R)*(rod.pos-ball.pos)/abs(rod.pos-ball.pos)
    # 切線加速度 g*sinsita*ballv/abs(ballv)
    ballv += balla*dt
    ball.pos += ballv*dt

    if ball.pos.x >= 0 and ball.pos.y >= 0 and isFirst:
        isFirst = False
        # print "T=", t
        t = 0

    if ball.pos.x < 0 and ball.pos.y > 0:
        isFirst = True

    varrow.pos = ball.pos
    varrow.axis = ballv*0.08
    aarrow.pos = ball.pos
    aarrow.axis = balla*0.02
    v_label.pos = ball.pos + varrow.axis*1.2
    a_label.pos = ball.pos + aarrow.axis*1.2
    # 重力位能Ug, 動能Ek
    Ug = m*g*ball.pos.y
    Ek = 1./2*m*v**2
    E = Ug + Ek
    # 畫出 Ug-t, Ek-t, E-t 圖
    # Ugt.plot(pos=(t, Ug))
    # Ekt.plot(pos=(t, Ek))
    # Et.plot(pos=(t, E))

    t += dt