# Result

# θ = 0.0 °   R = 4.040000000000002
# θ = 4.5 °   R = 8.334228910009026
# θ = 9.0 °   R = 13.768375467896101
# θ = 13.5 °   R = 19.311266619097985
# θ = 18.0 °   R = 24.575300381067063
# θ = 22.5 °   R = 29.32393636190764
# θ = 27.0 °   R = 33.39492452657972
# θ = 31.5 °   R = 36.68057987051349
# θ = 36.0 °   R = 39.09170116819651
# θ = 40.5 °   R = 40.54484608579267
# θ = 45.0 °   R = 41.01219330881964
# θ = 49.5 °   R = 40.473602371934795
# θ = 54.0 °   R = 38.95840652194676
# θ = 58.5 °   R = 36.48084978846608
# θ = 63.0 °   R = 33.114067051002586
# θ = 67.5 °   R = 28.938521155446377
# θ = 72.0 °   R = 24.053882842146482
# θ = 76.5 °   R = 18.577582055652577
# θ = 81.0 °   R = 12.643033464551763
# θ = 85.5 °   R = 6.400693029477672
# θ = 90.0 °   R = 5.0100300553118555e-15
#
# θ = 45.0 °   RMax = 41.01219330881964


from vpython import *

a = vector(0, -9.8, 0)
dt = 0.001
t = 0

floor = box(pos=vector(7.5, 0, 0), length=72, height=0.005, width=5, color=color.yellow)

r = 0.2
v0 = 20
n = 0
thetaMax = 0
deg = 0

distanceMax = 0


while n <= 20:
    ball = sphere(pos=vector(0, r + floor.height / 2, 0), radius=r, color=vector(0.3, 0.1 * n, 0.1 * n), make_trail=True)

    deg = n * 4.5
    theta = pi * deg / 180
    ball.v = vector(v0 * cos(theta), v0 * sin(theta), 0)

    t = 0
    ball.pos = vector(0, r + floor.height / 2, 0)

    while ball.pos.y >= floor.pos.y + floor.height / 2:
        rate(5000)
        ball.v += a * dt
        ball.pos += ball.v * dt

    if ball.pos.x > distanceMax:
        distanceMax = ball.pos.x
        thetaMax = n * 4.5

    print('θ =', n * 4.5, '°  ', 'R =', ball.pos.x)

    n += 1

print("")
print('θ =', thetaMax, '°  ', 'RMax =', distanceMax)
