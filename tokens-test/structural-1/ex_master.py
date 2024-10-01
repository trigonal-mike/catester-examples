import numpy
var1 = numpy.pi
var2 = "None"
var3 = None
var4 = None
def add(a, b):
    return a + b
#$STRUCTURALTEST structural-1
#$PROPERTY file "ex.py"
#$TESTVAR import
#$PROPERTY allowedOccuranceRange [1, 1]
#$TESTVAR def
#$PROPERTY allowedOccuranceRange [0, 2]
#$TESTVAR None
#$PROPERTY allowedOccuranceRange [2, 2]
#$TESTVAR "None"
#$PROPERTY occuranceType STRING
#$PROPERTY allowedOccuranceRange [1, 1]
#$TESTVAR numpy
#$PROPERTY allowedOccuranceRange [2, 2]
#$TESTVAR scipy
#$PROPERTY allowedOccuranceRange [0, 0]
