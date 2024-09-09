import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate


max_iter = 30
N = 40
iteration_steps = np.linspace(0, max_iter, N)

pi_norm = np.zeros_like(iteration_steps)
pi_gamma = np.zeros_like(iteration_steps)
pi_sin = np.zeros_like(iteration_steps)


fun_norm = lambda x: np.exp(-(x**2))
fun_gamma = lambda x: np.exp(-x) * x ** (-0.5)
fun_sin = lambda x: np.sin(x) / x


pi_approx = [pi_norm, pi_gamma, pi_sin]
functions = [fun_norm, fun_gamma, fun_sin]

for fun_idx, fun in enumerate(functions):
    for step in range(1, len(iteration_steps)):
        pi_approx[fun_idx][step] = (
            pi_approx[fun_idx][step - 1]
            + integrate.quad(fun, iteration_steps[step - 1], iteration_steps[step])[0]
        )

pi_norm = 4 * pi_norm**2
pi_gamma **= 2
pi_sin *= 2


fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
axes[0].axhline(np.pi, color="black", ls=":", label=r"$\pi$")
axes[0].plot(iteration_steps, pi_norm, label="Normal", color="red", marker=".")
axes[0].plot(iteration_steps, pi_gamma, label="Gamma", color="blue", marker=".")
axes[0].plot(iteration_steps, pi_sin, label="Sinus", color="green", marker=".")
axes[0].set_title("Values of the Integrals", fontsize=20)
axes[0].set_ylabel(r"$f(x)$", fontsize=20)
axes[0].legend(loc="lower right", fontsize=10)

axes[1].semilogy(
    iteration_steps, np.abs(np.pi - pi_norm), label="Normal", color="red", marker="."
)
axes[1].semilogy(
    iteration_steps, np.abs(np.pi - pi_gamma), label="Gamma", color="blue", marker="."
)
axes[1].semilogy(
    iteration_steps, np.abs(np.pi - pi_sin), label="Sinus", color="green", marker="."
)
axes[1].set_title("Convergence of the Integrals", fontsize=20)
axes[1].set_xlabel(r"$x$", fontsize=20)
axes[1].set_ylabel(r"$|\pi - f(x)|$", fontsize=20)
axes[1].set_xlim(0, max_iter)
axes[1].legend(loc="lower left", fontsize=10)
# plt.savefig('notes/MediaFiles/plot.png')
plt.show()
