#simple variables
var1 = 0.3
var2 = "1"
var3 = True
var4 = [1, 2]
var5 = (1, 2)
var6 = {1, 2}
var7 = "xyz"
var8 = 6
var9 = [1, 2]

def add(x, y):
  zz = 45
  return ( zz + x + y)


#$PROPERTY failureMessage "Some/all tests failed..."
#$PROPERTY relativeTolerance 1.0E-12
#$PROPERTY absoluteTolerance 0.000001

#$VARIABLETEST Test Basic
#$PROPERTY relativeTolerance 1.0E-1
#$PROPERTY absoluteTolerance 0.001
#$TESTVAR var1
#$PROPERTY relativeTolerance 1.0E-33
#$PROPERTY absoluteTolerance 0
#$TESTVAR var2
#$TESTVAR var3
#$TESTVAR var3
#$PROPERTY evalString "not not not False"
#$TESTVAR var4
#$TESTVAR var5
#$TESTVAR var6
#$TESTVAR var7
#$TESTVAR var8
#$PROPERTY evalString "round((1+2+3+0.001)*1)"
#$TESTVAR var9[0]
