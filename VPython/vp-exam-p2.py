# from visual import *
from vpython import *
import math

# scene = display(width=1000, height=1000, background=(0.5, 0.6, 0.5))
scene = canvas(width=1000, height=1000, background=vector(0.5, 0.6, 0.5))
x_axis = arrow(axis=vector(17, 0, 0), shaftwidth=0.1)
y_axis = arrow(axis=vector(0, 17, 0), shaftwidth=0.1)
label(pos=vector(17.5, 0, 0), text='x', box=False)
label(pos=vector(0, 17.5, 0), text='y', box=False)

positions = [
    vector(3, 0, 0), vector(6, 0, 0), vector(9, 0, 0),
    vector(12, 0, 0), vector(15, 0, 0)
]
labels = ["(3,0,0)", "(6,0,0)", "(9,0,0)", "(12,0,0)", "(15,0,0)"]
for i in range(len(positions)):
    label(pos=positions[i] + vector(0, -0.5, 0), text=labels[i], box=False)

y_positions = [vector(0, y, 0) for y in [3, 6, 9, 12, 15]]
y_labels = ["(0,3,0)", "(0,6,0)", "(0,9,0)", "(0,12,0)", "(0,15,0)"]
for i in range(len(y_positions)):
    label(pos=y_positions[i] + vector(-1, 0, 0), text=y_labels[i], box=False)


def generate_polygon(center, sides, color):
    R = 1
    w = 2 * math.pi / sides
    vertices = []
    for i in range(sides):
        vec = vector(R * math.cos(w * i), R * math.sin(w * i), 0)
        vertices.append(vec)


    last_pos = center
    for vec in vertices:
        arrow(pos=last_pos, axis=vec, color=color, shaftwidth=0.02)
        last_pos += vec


polygons = [
    {"center": vector(3, 0, 0), "sides": 3, "color": color.red},
    {"center": vector(6, 0, 0), "sides": 6, "color": color.green},
    {"center": vector(9, 0, 0), "sides": 9, "color": color.blue},
    {"center": vector(12, 0, 0), "sides": 12, "color": color.orange},
    {"center": vector(15, 0, 0), "sides": 15, "color": color.purple},
]

t = 0

arrow_count = 5
while True:
    rate(1)
    if t < len(polygons):
        for i in range(arrow_count):
            generate_polygon(polygons[t]["center"] + vector(0, 3 * i, 0), polygons[t]["sides"], polygons[t]["color"])
        t += 1
        arrow_count -= 1
    else:
        break


