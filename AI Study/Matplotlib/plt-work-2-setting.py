import matplotlib.pyplot as plt
import matplotlib as mplt
import numpy as np

# set font
mplt.rcParams['font.sans-serif'] = ['Arial Unicode Ms']

# set dpi
mplt.rcParams['figure.dpi'] = 300

plt.rcParams.get('figure.figsize')
plt.rcParams.get('font.size')

# set panel to white
rc = {"axes.facecolor": "white",
      "savefig.facecolor": "white"}

mplt.rcParams.update(rc)  # update value more once time

mplt.rcParams['text.usetex'] = True  # can input LaTeX

plt.rcParams['figure.constrained_layout.use'] = True

# plt.style.use('default')
plt.plot(np.random.randn(50))
# plt.show()


# input chinese and LaTex
rc = {"font.family": "Times New Roman",
      "mathtext.fontset": "stix"}

mplt.rcParams.update(rc)


fig, ax = plt.subplots()
ax.set_xlabel(r'D $\mathrm{kg/m}^3$')
ax.text(0.2, 0.8, r'word $\mathrm{words}$', fontsize=20)
ax.text(0.2, 0.6, r'word $words$', fontsize=30)
plt.ylim(0.5, 0.9)
plt.show()
