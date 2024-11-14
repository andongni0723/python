import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode Ms']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

data_lst = [1, 2, 3, 4]
stock1 = [4, 8, 2, 6]
stock2 = [10, 12, 5, 3]

# matlab
'''
plt.figure(figsize=(9, 10))
plt.subplot(211)  # 2 row 1 column no.1 graph
plt.bar(data_lst, stock1)
plt.subplot(212)
plt.plot(data_lst, stock2, "b^--")
plt.show()
'''

fig, axes = plt.subplots(2, 1, figsize=(9, 10))
axes[0].bar(data_lst, stock1)
axes[1].plot(data_lst, stock2, "b^--")
plt.tight_layout()
plt.show()
