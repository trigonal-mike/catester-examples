import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

# plt.plot(x, y1, color="blue", label="sine")
# plt.plot(x, y1, "-b", label="sine")
plt.plot(x, y1, "b", label="sine")

plt.plot(x, y2, "-r", label="cosine")
# plt.legend(loc="lower left")
plt.legend(loc="lower right")
plt.xlabel("xx", {"fontsize": 14})
plt.ylabel("yy", {"fontsize": 14})
plt.ylim(-1.5, 2.0)
# print(plt.figure(1).axes[0].get_legend()._loc)
print(plt.figure(1).axes[0].lines[0]._color)
plt.show()
