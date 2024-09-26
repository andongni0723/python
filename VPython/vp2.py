from vpython import *
# from visual import *

# initial
a = -9.8
vy = 0.0
h = 10.0
dt = 0.005
t = 0.0
b = 10

ground = box(pos=vector(0, 0, 0), length=10, height=0.005, width=10)
ball = sphere(pos=vector(0, h, 0), radius=0.2, color=color.red)

last_print_time = 0.0

while ball.pos.y > ground.height / 2 + ball.radius:
    rate(100)
    t += dt
    vy += a * dt
    ball.pos.y += vy * dt

    if t - last_print_time >= 0.2:
        last_print_time = t
        # print(f"t: {t:.1f}, Δ distance: {10 - ball.pos.y:.2f}, vy: {vy:.2f}")
        # print "t:", t, " Δ distance:", 10 - ball.pos.y, ", vy: ", vy:

# print(f"fall time {t:.2f}")
# print "fall time",t

# 執行結果
# t: 0.2, Δ distance: 0.20, vy: -1.96
# t: 0.4, Δ distance: 0.79, vy: -3.92
# t: 0.6, Δ distance: 1.78, vy: -5.88
# t: 0.8, Δ distance: 3.16, vy: -7.84
# t: 1.0, Δ distance: 4.92, vy: -9.80
# t: 1.2, Δ distance: 7.14, vy: -11.81
# t: 1.4, Δ distance: 9.78, vy: -13.82
# fall time 1.41
