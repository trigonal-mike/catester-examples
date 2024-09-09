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
#$PROPERTY id "values"
#$PROPERTY entryPoint "pskript.py"
#$TESTVAR x_0
#$TESTVAR s
#$TESTVAR x_a
#$TESTVAR x_e
#$TESTVAR x_n

#$VARIABLETEST vectors
#$PROPERTY id "vectors"
#$PROPERTY entryPoint "pskript.py"
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
# TODO: Check legend texts
# TODO: Check if functions are correct

#$EXISTANCETEST existance gauss
#$PROPERTY id "gauss"
#$PROPERTY file "sgauss.py"
#$TESTVAR -

#$EXISTANCETEST existance secansh
#$PROPERTY id "secansh"
#$PROPERTY file "secansh.py"
#$TESTVAR -


#$STRUCTURALTEST structural-tests
#$PROPERTY file "pskript.py"
#$TESTVAR "Gauss"
#$PROPERTY allowedOccuranceRange [1,1]
#$PROPERTY occuranceType STRING
#$TESTVAR "Sech"
#$PROPERTY allowedOccuranceRange [1,1]
#$PROPERTY occuranceType STRING

