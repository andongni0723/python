from vpython import *
# from visual import *

v = vector(0, 0, 1)
dt = 0.001
t = 0
ground = box(pos=vector(0, 0, 0), length=3, height=0.005, width=3, color=color.red)
cube = box(pos=vector(-1, 0.5 / 2, -1), length=0.5, height=0.5, width=0.5, )
dire = True

# -1,-1     1,-1
# -1, 1     1, 1
while True:
    rate(2000)
    t += dt
    cube.pos += v * dt
    # print("\r", cube.pos, v, end="", flush=True)
    if cube.pos.z >= 1 and cube.pos.x <= -1:
        if dire:
            v = vector(1, 0, 0)
        else:
            v = vector(0, 0, -1)
    elif cube.pos.x >= 1 and cube.pos.z >= 1:
        if dire:
            v = vector(0, 0, -1)
        else:
            v = vector(-1, 0, 0)
    elif cube.pos.z <= -1 and cube.pos.x >= 1:
        if dire:
            v = vector(-1, 0, 0)
        else:
            v = vector(0, 0, 1)
    elif cube.pos.x <= -1 and cube.pos.z <= -1:
        if dire:
            v = vector(1, 0, 0)
        else:
            v = vector(0, 0, 1)
        dire = not dire