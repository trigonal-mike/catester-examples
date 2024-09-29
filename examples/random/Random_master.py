import os
import random
import time


var1 = random.randint(1, 100)
var2 = random.random()
var3 = random.randint(1, 100)

var4 = os.getcwd()
var5 = time.time()

var6 = [1, 22, 44]
var7 = [[1, "23", 44]]
var8 = [1, {"23"}, 44]
var9 = "xxx"


#$VARIABLETEST random1
#$PROPERTY id "1"
#$TESTVAR var1
#$TESTVAR var2
#$TESTVAR var3
#$TESTVAR var4
#$TESTVAR var5
#$TESTVAR var6[1]
#$TESTVAR var7[0][1]
#$TESTVAR var7[0][2]
#$TESTVAR var8

#$VARIABLETEST random2
#$PROPERTY successDependency "1"
#$TESTVAR var9

#$VARIABLETEST random3
#$PROPERTY setUpCode ["import random", "b = random.randint(0, 10)"]
#$TESTVAR b
#$PROPERTY absoluteTolerance 0
