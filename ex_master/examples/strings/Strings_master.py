var1 = "_x1234567890"

#$VARIABLETEST variables unit1

#$TESTVAR var1
#$PROPERTY qualification matches
#$PROPERTY pattern "_x1234567890"

#$TESTVAR var1
#$PROPERTY qualification contains
#$PROPERTY pattern "_x1234567890"

#$TESTVAR var1
#$PROPERTY qualification startsWith
#$PROPERTY pattern "_x123"

#$TESTVAR var1
#$PROPERTY qualification endsWith
#$PROPERTY pattern "890"

#$TESTVAR var1
#$PROPERTY qualification count
#$PROPERTY countRequirement 1
#$PROPERTY pattern "_"

#$TESTVAR var1
#$PROPERTY qualification regexp
#$PROPERTY pattern "^.*x.*$"
