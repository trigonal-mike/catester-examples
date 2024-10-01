var1 = 1
#$VARIABLETEST test-1
#$PROPERTY setUpCode "var2 = var1\ndel var1"
#$TESTVAR var1
#$TESTVAR var2

#$VARIABLETEST test-2
#$PROPERTY setUpCode ["var2 = var1", "del var1"]
#$TESTVAR var1
#$TESTVAR var2

#$VARIABLETEST test-3
#$PROPERTY setUpCode "var2 = var1"
#$PROPERTY setUpCode "del var1"
#$TESTVAR var1
#$TESTVAR var2
