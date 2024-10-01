var1 = "_abcdefgh_"
#$VARIABLETEST string-1
#$TESTVAR var1
#$PROPERTY qualification matches
#$PROPERTY pattern "_abcdefgh_"

#$TESTVAR var1
#$PROPERTY qualification contains
#$PROPERTY pattern "cde"

#$TESTVAR var1
#$PROPERTY qualification startsWith
#$PROPERTY pattern "_a"

#$TESTVAR var1
#$PROPERTY qualification endsWith
#$PROPERTY pattern "gh_"

#$TESTVAR var1
#$PROPERTY qualification count
#$PROPERTY countRequirement 2
#$PROPERTY pattern "_"

#$TESTVAR var1
#$PROPERTY qualification regexp
#$PROPERTY pattern "^_[a-h]+_$"

#$TESTVAR var1
#$PROPERTY qualification regexp
#$PROPERTY pattern "^\\w+$"
