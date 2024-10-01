import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 1000)
y = np.sin(x)
plt.plot(x, y, "-r", label="sine")
plt.show()

#$GRAPHICSTEST graphics-2
#$PROPERTY storeGraphicsArtifacts true
#$TESTVAR figure(1).axes[0].lines[0].get_linestyle()
