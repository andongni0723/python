import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')
plt.plot(np.random.randn(50))
# plt.savefig("")
plt.show()

plt.style.use('ggplot')
plt.plot(np.random.randn(50))
# plt.savefig("")
plt.show()

# plt.style.use('seaborn-dark')
# plt.plot(np.random.randn(50))
# plt.savefig("")
# plt.show()