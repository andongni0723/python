# # for vpython 2
#
#
# from visual import *
#
# x_axis = arrow(axis=vector(2, 0, 0), shaftwidth=0.01)
# y_axis = arrow(axis=vector(0, 2, 0), shaftwidth=0.01)
# z_axis = arrow(axis=vector(0, 0, 2), shaftwidth=0.01)
# label(pos=vector(2.1, 0, 0), text='x', box=False)
# label(pos=vector(0, 2.1, 0), text='y', box=False)
# label(pos=vector(0, 0, 2.1), text='z', box=False)
#
# w = 2 * pi / 6
# R = 1
# vectors = vector(0, 0, 0)
# last_pos = vector(0, 0, 0)
# last_axis = vector(R, R, 0)
# i = 0
# while i < 6:
#     rate(1)
#     vec = vector(R * cos(w * i), R * sin(w * i), 0)
#
#     if i == 0:
#         arrow(pos=vectors, axis=vec, color=color.red, shaftwidth=0.02)  # 在Vpython裡,電腦只要"看到"arrow,它自動會產生一個箭頭
#         last_pos = vectors
#     else:
#         arrow(pos=last_pos + last_axis, axis=vec, color=color.red, shaftwidth=0.02)  # 在Vpython裡,電腦只要"看到"arrow,它自動會產生一個箭頭
#         last_pos = last_pos + last_axis
#
#     last_axis = vec
#     i += 1