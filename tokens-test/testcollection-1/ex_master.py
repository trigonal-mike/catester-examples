import time
time.sleep(0.25)
var1 = 1
#$VARIABLETEST timeout-pass
#$PROPERTY timeout 0.5
#$TESTVAR var1

#$VARIABLETEST timeout-fail
#$PROPERTY timeout 0.1
#$TESTVAR var1
