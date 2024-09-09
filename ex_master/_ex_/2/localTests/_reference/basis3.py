import numpy as np
import matplotlib.pyplot as plt

# Define the range of x
x_a = -2 * np.pi
x_e = 2 * np.pi

x_n = 180

x = np.linspace(x_a, x_e, x_n)

# Define the functions
two_pi = 2 * np.pi
sin_x = np.sin(x)

f1 = x / two_pi * sin_x
f2 = (x / two_pi) ** 2 * sin_x**2
f3 = x**3 / two_pi**3 * sin_x**3

# Plot the function values
plt.figure()
plt.plot(x, f1, "r", label="f1(x)")
plt.plot(x, f2, "b", label="f2(x)")
plt.plot(x, f3, "g", label="f3(x)")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim([x_a, x_e])
plt.legend(loc="lower center")
plt.show()


# TODO: Test for legend position
