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



#$META title "Approximation von pi mit Integralen"

#$VARIABLETEST f1
#$PROPERTY entryPoint "pi_int.py"
#$PROPERTY setUpCode ["t_f1=fun_norm(4)"]
#$TESTVAR t_f1


#$VARIABLETEST f2
#$PROPERTY entryPoint "pi_int.py"
#$PROPERTY setUpCode ["t_f2=fun_gamma(4)"]
#$TESTVAR t_f2


#$VARIABLETEST f3
#$PROPERTY entryPoint "pi_int.py"
#$PROPERTY setUpCode ["t_f3=fun_sin(4)"]
#$TESTVAR t_f3

#$VARIABLETEST variables
#$TESTVAR max_iter
#$TESTVAR N
#$TESTVAR iteration_steps
#$TESTVAR pi_norm
#$TESTVAR pi_gamma
#$TESTVAR pi_sin



#$GRAPHICSTEST matplot figures
#$TESTVAR figure(1).axes[0].lines[0].properties()['xydata']
#$TESTVAR figure(1).axes[0].lines[1].properties()['xydata']
#$TESTVAR figure(1).axes[0].lines[2].properties()['xydata']
#$TESTVAR figure(1).axes[0].lines[3].properties()['xydata']
#$TESTVAR figure(1).axes[0].lines[0]._linestyle
#$TESTVAR figure(1).axes[0].lines[1]._linestyle
#$TESTVAR figure(1).axes[0].lines[2]._linestyle
#$TESTVAR figure(1).axes[0].lines[3]._linestyle
#$TESTVAR figure(1).axes[0].get_ylabel()
#$TESTVAR figure(1).axes[0].get_title()
#$TESTVAR figure(1).axes[0].get_xlim()
#$TESTVAR figure(1).axes[0].lines[0]._linestyle
#$TESTVAR figure(1).axes[0].lines[1]._linestyle
#$TESTVAR figure(1).axes[0].lines[2]._linestyle
#$TESTVAR figure(1).axes[0].lines[3]._linestyle
#$TESTVAR figure(1).axes[0].get_legend().get_texts()[0].get_text()
#$TESTVAR figure(1).axes[0].get_legend().get_texts()[1].get_text()
#$TESTVAR figure(1).axes[0].get_legend().get_texts()[2].get_text()
#$TESTVAR figure(1).axes[0].get_legend().get_texts()[3].get_text()
#$TESTVAR figure(1).axes[0].get_legend()._loc
#$TESTVAR figure(1).axes[1].lines[0].properties()['xydata']
#$TESTVAR figure(1).axes[1].lines[1].properties()['xydata']
#$TESTVAR figure(1).axes[1].lines[2].properties()['xydata']
#$TESTVAR figure(1).axes[1].lines[0]._linestyle
#$TESTVAR figure(1).axes[1].lines[1]._linestyle
#$TESTVAR figure(1).axes[1].lines[2]._linestyle
#$TESTVAR figure(1).axes[1].get_xlabel()
#$TESTVAR figure(1).axes[1].get_ylabel()
#$TESTVAR figure(1).axes[1].get_title()
#$TESTVAR figure(1).axes[1].get_xlim()
#$TESTVAR figure(1).axes[1].get_ylim()
#$TESTVAR figure(1).axes[1].lines[0]._linestyle
#$TESTVAR figure(1).axes[1].lines[1]._linestyle
#$TESTVAR figure(1).axes[1].lines[2]._linestyle
#$TESTVAR figure(1).axes[1].get_legend().get_texts()[0].get_text()
#$TESTVAR figure(1).axes[1].get_legend().get_texts()[1].get_text()
#$TESTVAR figure(1).axes[1].get_legend().get_texts()[2].get_text()
#$TESTVAR figure(1).axes[1].get_legend()._loc


#$GRAPHICSTEST color00
#$TESTVAR figure(1).axes[0].lines[0]._color
#$PROPERTY qualification regexp
#$PROPERTY pattern ^(black|k|\(0\.0, 0\.0, 0\.0, 1\)|\(0, 0, 0, 1\)|\(0, 0, 0\)|\(0\.0, 0\.0, 0\.0\)|#000000)$

#$GRAPHICSTEST color01
#$TESTVAR figure(1).axes[0].lines[1]._color
#$PROPERTY qualification regexp
#$PROPERTY pattern ^(red|r|\(1\.0, 0\.0, 0\.0, 1\)|\(255, 0, 0, 1\)|\(255, 0, 0\)|\(1\.0, 0\.0, 0\.0\)|#FF0000)$

#$GRAPHICSTEST color02
#$TESTVAR figure(1).axes[0].lines[2]._color
#$PROPERTY qualification regexp
#$PROPERTY pattern ^(blue|b|\(0.0, 0.0, 1.0, 1\)|\(0, 0, 1, 1\)|\(0, 0, 1\)|\(0.0, 0.0, 1.0\)|#0000FF)$

#$GRAPHICSTEST color03
#$TESTVAR figure(1).axes[0].lines[3]._color
#$PROPERTY qualification regexp
#$PROPERTY pattern ^(green|g|\(0\.0, 1\.0, 0\.0, 1\)|\(0, 255, 0, 1\)|\(0, 255, 0\)|\(0\.0, 1\.0, 0\.0\)|#00FF00)$




#$GRAPHICSTEST color10
#$TESTVAR figure(1).axes[1].lines[0]._color
#$PROPERTY qualification regexp
#$PROPERTY pattern ^(red|r|\(1\.0, 0\.0, 0\.0, 1\)|\(255, 0, 0, 1\)|\(255, 0, 0\)|\(1\.0, 0\.0, 0\.0\)|#FF0000)$


#$GRAPHICSTEST color11
#$TESTVAR figure(1).axes[1].lines[1]._color
#$PROPERTY qualification regexp
#$PROPERTY pattern ^(blue|b|\(0.0, 0.0, 1.0, 1\)|\(0, 0, 1, 1\)|\(0, 0, 1\)|\(0.0, 0.0, 1.0\)|#0000FF)$

#$GRAPHICSTEST color12
#$TESTVAR figure(1).axes[1].lines[2]._color
#$PROPERTY qualification regexp
#$PROPERTY pattern ^(green|g|\(0\.0, 1\.0, 0\.0, 1\)|\(0, 255, 0, 1\)|\(0, 255, 0\)|\(0\.0, 1\.0, 0\.0\)|#00FF00)$

