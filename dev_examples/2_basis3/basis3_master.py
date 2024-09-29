#$META title "Kombination von Funktionen"
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
f2 = (x / two_pi)**2 * sin_x**2
f3 = x**3 / two_pi**3 * sin_x**3

# Plot the function values 
plt.figure()
plt.plot(x,f1,'r', label='f1(x)')
plt.plot(x,f2,'b', label='f2(x)')
plt.plot(x,f3,'g', label='f3(x)')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim([x_a,x_e])
plt.legend(loc='lower center')
plt.show()

#$VARIABLETEST startvalues
#$PROPERTY id "startvalues"
#$TESTVAR x_a
#$TESTVAR x_e
#$TESTVAR x_n

#$VARIABLETEST vectors
#$PROPERTY id "vectors"
#$PROPERTY successDependency "startvalues"
#$TESTVAR x
#$TESTVAR f1
#$TESTVAR f2
#$TESTVAR f3

#$GRAPHICSTEST plot
#$PROPERTY storeGraphicsArtifacts false
#$TESTVAR figure(1).axes[0].lines[0].get_color()
#$TESTVAR figure(1).axes[0].lines[1]._color
#$TESTVAR figure(1).axes[0].lines[2]._color
#$TESTVAR figure(1).axes[0].get_xlabel()
#$TESTVAR figure(1).axes[0].get_ylabel()
#$TESTVAR figure(1).axes[0].get_xlim()
#$TESTVAR figure(1).axes[0].get_ylim()
#$TESTVAR figure(1).axes[0].legend().get_texts()[0].get_text()
#$TESTVAR figure(1).axes[0].legend().get_texts()[1].get_text()
#$TESTVAR figure(1).axes[0].legend().get_texts()[2].get_text()

# TODO: Test for legend position
