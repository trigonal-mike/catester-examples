import numpy as np
import matplotlib.pyplot as plt

from secansh import secansh
from sgauss import sgauss

x_0 = 4
s = 0.2

x_a = x_0 - 5 * s
x_e = x_0 + 5 * s
x_n = 300

x = np.linspace(x_a, x_e, x_n)
g = sgauss(x, x_0, s)
h = secansh(x, x_0, s)

plt.plot(x, g, "r")
plt.plot(x, h, "b")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(("Gausss", "Sechz"))
plt.show()


# TODO: Check legend texts
# TODO: Check if functions are correct
