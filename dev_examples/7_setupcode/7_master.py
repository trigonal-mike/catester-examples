#$META studentSubmissionFiles ./func.py
from func import add

x = add(1,2)
print(x)

#$VARIABLETEST values1
#$TESTVAR x

#$VARIABLETEST values2
#$PROPERTY entryPoint "func.py"
#$PROPERTY setUpCode ["x=add(1,2)"]
#$TESTVAR x
