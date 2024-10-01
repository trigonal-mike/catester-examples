print("abc")
#$STDOUTTEST test-1
#$TESTVAR -

#$STDOUTTEST test-2
#$TESTVAR -
#$PROPERTY qualification startsWith
#$PROPERTY pattern "ab"

#$STDOUTTEST test-3
#$TESTVAR -
#$PROPERTY qualification matches
#$PROPERTY pattern "abcde"
