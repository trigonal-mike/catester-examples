#$META title "Erstellen und Plotten eigener Funktionen"
#$META studentSubmissionFiles ./secansh.py
#$META studentSubmissionFiles ./sgauss.py
import numpy as np
import matplotlib.pyplot as plt

from secansh import secansh
from sgauss import sgauss

x_0 = 2
s = 0.2

x_a = x_0 - 5*s
x_e = x_0 + 5*s
x_n = 300

x = np.linspace(x_a,x_e,x_n)
g = sgauss(x,x_0,s)
h = secansh(x,x_0,s)


plt.plot(x,g,'r')
plt.plot(x,h,'b')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(('Gauss','Sech'))
plt.show()

#$VARIABLETEST values
#$PROPERTY entryPoint "pskript.py"
#$PROPERTY id "values"
#$TESTVAR x_0
#$TESTVAR s
#$TESTVAR x_a
#$TESTVAR x_e
#$TESTVAR x_n

#$VARIABLETEST vectors
#$PROPERTY entryPoint "pskript.py"
#$PROPERTY id "vectors"
#$TESTVAR x
#$TESTVAR g
#$TESTVAR h

#$GRAPHICSTEST figure
#$PROPERTY storeGraphicsArtifacts false
#$PROPERTY entryPoint "pskript.py"
#$TESTVAR figure(1).axes[0].lines[0].properties()['xydata']
#$TESTVAR figure(1).axes[0].lines[0]._color
#$TESTVAR figure(1).axes[0].lines[1].properties()['xydata']
#$TESTVAR figure(1).axes[0].lines[1]._color
#$TESTVAR figure(1).axes[0].get_xlabel()
#$TESTVAR figure(1).axes[0].get_ylabel()
#$TESTVAR figure(1).axes[0].legend().get_texts()[0].get_text()
#$TESTVAR figure(1).axes[0].legend().get_texts()[1].get_text()

#$EXISTANCETEST existance gauss
#$PROPERTY id "gauss"
#$PROPERTY file "sgauss.py"
#$TESTVAR -

#$EXISTANCETEST existance secansh
#$PROPERTY id "secansh"
#$PROPERTY file "secansh.py"
#$TESTVAR -