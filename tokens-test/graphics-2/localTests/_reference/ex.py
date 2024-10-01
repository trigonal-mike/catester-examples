import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 1000)
y = np.sin(x)
plt.plot(x, y, "-r", label="sine")
plt.show()
