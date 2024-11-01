# from visual import *
# from visual.graph import *
#
# a = vector(0, -9.8, 0)
# dt = 0.001
# t = 0
#
# # 2. Scene setup
# scene = display(title='Projectile Motion', background=(0.2, 0.6, 0.8))
# floor = box(pos=vector(7.5, 0, 0), length=72, height=0.005, width=5, color=color.yellow)
#
# r = 0.2
# v0 = 20
# n = 0
# thetaMax = 0
# deg = 0
#
# distanceMax = 0
#
# while n <= 20:
#     ball = sphere(pos=vector(0, r + floor.height / 2, 0), radius=r,
#                   color=vector(0.3, 0.1 * n, 0.1 * n), make_trail=True)
#
#     deg = n * 4.5
#     theta = pi * deg / 180
#     ball.v = vector(v0 * cos(theta), v0 * sin(theta), 0)
#
#     t = 0
#     ball.pos = vector(0, r + floor.height / 2, 0)
#
#     while ball.pos.y >= floor.pos.y + floor.height / 2:
#         rate(5000)
#         ball.v += a * dt
#         ball.pos += ball.v * dt
#
#     if ball.pos.x > distanceMax:
#         distanceMax = ball.pos.x
#         thetaMax = deg
#
#     print 'θ =', deg, '°  ', 'R =', ball.pos.x
#     n += 1
#
# print ""
# print 'θ =', thetaMax, '°  ', 'RMax =', distanceMax
