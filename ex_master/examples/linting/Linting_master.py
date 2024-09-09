# simple variables
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
    return zz + x + y


#$LINTINGTEST linting1
#$PROPERTY file "Linting.py"
#$TESTVAR -
#$PROPERTY pattern W,E2,E3

#$LINTINGTEST linting2
#$PROPERTY file "Linting.py"
#$TESTVAR -

