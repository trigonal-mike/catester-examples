import numpy as np
import matplotlib.pyplot as plt

#define the parameters
x_a=-2*np.pi
x_e=2*np.pi
x_n=180

x = np.linspace(x_a, x_e,x_n)

#define the functions
f1 = (x/(2*np.pi))*np.sin(x)
f2 = ((x**2)/(2*np.pi)**2)*np.sin(x)**2
f3 = ((x**3)/(2*np.pi)**3)*np.sin(x)**3

#compute the function values
figure = plt.figure()
plt.plot(x, f1, "r--", label='f1(x)')
plt.plot(x, f2, color=(0.0,0.0,1.0,1.0), label='f2(x)')
plt.plot(x, f3, color=(0.0,0.5,0.0,1.0), label='f3(x)')

x = plt.figure(1).axes[0].lines[0].get_color()
y = plt.figure(1).axes[0].lines[0]._color
print(x)
print(y)
#plot the results
plt.xlabel('x')
plt.ylabel('f(x)')

plt.legend( loc='lower center')

plt.xlim(x_a, x_e)
#plt.show()

