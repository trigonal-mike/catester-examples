import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 1000)
y = np.sin(x)
plt.plot(x, y, "-b", label="sine")
plt.show()

#$GRAPHICSTEST graphics-1
#$TESTVAR figure(1).axes[0].lines[0].get_linestyle()
