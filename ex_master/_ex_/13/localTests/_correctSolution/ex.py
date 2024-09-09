import matplotlib.pyplot as plt
import numpy as np
import scipy

x = np.linspace(-np.pi, np.pi, 100)
y = np.zeros(x.shape)

plt.plot(x, y)
for n in range(7):
    y = y + (-1) ** n * (x ** (2 * n + 1)) / (scipy.special.factorial(2 * n + 1))
    plt.plot(x, y)

plt.plot(x, np.sin(x))
plt.show()
