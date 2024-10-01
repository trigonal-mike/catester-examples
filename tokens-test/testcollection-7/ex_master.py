#$META studentSubmissionFiles ./additional.py

from additional import get_pi_from_numpy
import math

var1 = get_pi_from_numpy()
var2 = var1 * math.pi

#$VARIABLETEST variables test-1
#$PROPERTY moduleBlacklist ["additional"]
#$TESTVAR var2

#$VARIABLETEST variables test-2
#$PROPERTY moduleBlacklist ["numpy"]
#$TESTVAR var2

#$VARIABLETEST variables test-3
#$PROPERTY moduleBlacklist ["additional", "numpy", "math"]
#$TESTVAR var2
