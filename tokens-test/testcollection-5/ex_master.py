#$META studentSubmissionFiles additional-file.py

#$VARIABLETEST test-1
#$PROPERTY id "test1"
#$PROPERTY entryPoint additional-file.py
#$TESTVAR var1

#$VARIABLETEST test-2
#$PROPERTY setUpCodeDependency "test1"
#$TESTVAR var1

#$VARIABLETEST test-3
#$PROPERTY setUpCodeDependency 2
#$TESTVAR var1

#$VARIABLETEST test-4
#$TESTVAR var1
